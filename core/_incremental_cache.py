"""[v2.5] 增量测试缓存 — 避免每轮全量重测。

核心思路：
  - 维护 node_test_cache.json，记录 {fingerprint: {config_hash, tested_at, success, latency_ms, ...}}
  - 下一轮：配置未变 + 最近 2 小时内测过 → 直接复用结果
  - 失败结果 1 小时内可复用（节点可能恢复，但也可能一直坏）
  - 新节点或配置变化 → 必须真测

预期收益：6 小时间隔下约 60-70% 节点可复用，CI 耗时降低 50-60%。
"""
from __future__ import annotations

import hashlib
import json
import logging
from pathlib import Path
from typing import Any, Dict, List, Tuple

from core.parser import Node

logger = logging.getLogger(__name__)

CACHE_FILE = "node_test_cache.json"
SCHEMA_VERSION = "1.0"         # [v2.5.1] 缓存格式版本号，变更时自动失效旧缓存
REUSE_MAX_AGE_SEC = 7200       # 成功结果 2 小时内可复用
REUSE_FAIL_MAX_AGE_SEC = 3600  # 失败结果 1 小时内可复用
MAX_CACHE_ENTRIES = 10000      # 缓存条目上限，防止文件无限增长


def _config_hash(node: Node) -> str:
    """节点配置指纹 — 配置不变 = 结果可复用。
    
    把 server/port/type/raw 全部哈希，任何一个字段变化都会导致缓存失效。
    """
    raw = json.dumps({
        "type": node.type,
        "server": node.server,
        "port": node.server_port,
        "raw": node.raw,
    }, sort_keys=True, ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()[:16]


def load_cache(output_dir: str) -> Dict[str, Any]:
    """加载缓存文件，失败时返回空字典。
    
    [v2.5.1] 版本控制：如果缓存版本与当前版本不匹配，自动失效返回空字典。
    """
    p = Path(output_dir) / CACHE_FILE
    if not p.exists():
        return {}
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            return {}
        
        # 版本检查：不匹配时自动失效
        cached_version = data.get("version", "0.0")
        if cached_version != SCHEMA_VERSION:
            logger.info("Cache version mismatch (%s vs %s), invalidating cache", 
                       cached_version, SCHEMA_VERSION)
            return {}
        
        entries = data.get("entries", {})
        return entries if isinstance(entries, dict) else {}
    except Exception as exc:
        logger.warning("incremental cache load failed: %s", exc)
        return {}


def save_cache(output_dir: str, cache: Dict[str, Any]) -> None:
    """保存缓存文件，自动 LRU 淘汰超出上限的条目。
    
    [v2.5.1] 版本控制：保存时写入当前版本号。
    """
    if len(cache) > MAX_CACHE_ENTRIES:
        # 按 tested_at 降序，保留最新的 MAX_CACHE_ENTRIES 条
        sorted_items = sorted(
            cache.items(),
            key=lambda x: float(x[1].get("tested_at", 0)),
            reverse=True,
        )
        cache = dict(sorted_items[:MAX_CACHE_ENTRIES])

    p = Path(output_dir) / CACHE_FILE
    p.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "schema": "autonodes.incremental_cache.v1",
        "version": SCHEMA_VERSION,  # [v2.5.1] 版本号
        "total": len(cache),
        "entries": cache,
    }
    tmp = p.with_suffix(p.suffix + ".tmp")
    tmp.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(p)


def classify_for_test(
    nodes: List[Node],
    cache: Dict[str, Any],
    now: float,
) -> Tuple[List[Node], List[Tuple[Node, Dict[str, Any]]]]:
    """将节点分为 (必须测试的, 可复用结果的)。

    Args:
        nodes: 本轮候选节点列表
        cache: 缓存字典 {fingerprint: entry}
        now: 当前时间戳 time.time()

    Returns:
        (must_test, reusable)
        must_test: 需要真测的节点
        reusable: 可复用缓存结果的 (node, cached_entry) 对
    """
    must_test: List[Node] = []
    reusable: List[Tuple[Node, Dict[str, Any]]] = []

    for n in nodes:
        fp = n.fingerprint()
        entry = cache.get(fp)

        if not entry or not isinstance(entry, dict):
            must_test.append(n)
            continue

        # 配置是否变化
        if entry.get("config_hash") != _config_hash(n):
            must_test.append(n)
            continue

        # 年龄检查
        age = now - float(entry.get("tested_at", 0))
        success = bool(entry.get("success", False))
        max_age = REUSE_MAX_AGE_SEC if success else REUSE_FAIL_MAX_AGE_SEC

        if age < max_age:
            reusable.append((n, entry))
        else:
            must_test.append(n)

    return must_test, reusable


def update_cache_after_test(
    cache: Dict[str, Any],
    results: List[Any],  # List[TestResult]
    now: float,
) -> Dict[str, Any]:
    """真测完成后，把结果写入缓存。

    Args:
        cache: 当前缓存字典（会被原地修改）
        results: 本轮真测结果列表
        now: 当前时间戳

    Returns:
        更新后的缓存字典
    """
    for r in results:
        node = getattr(r, "node", None)
        if node is None:
            continue
        fp = node.fingerprint()
        cache[fp] = {
            "config_hash": _config_hash(node),
            "tested_at": now,
            "success": bool(r.success),
            "latency_ms": round(float(getattr(r, "latency_ms", 0) or 0), 1),
            "jitter_ms": round(float(getattr(r, "jitter_ms", 0) or 0), 1),
            "speed_kbps": round(float(getattr(r, "speed_kbps", 0) or 0), 1),
            "error": str(getattr(r, "error", "") or "")[:200],
        }
    return cache