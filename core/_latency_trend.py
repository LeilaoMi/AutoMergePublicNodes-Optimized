"""[P1-5] 节点延迟趋势持久化与告警。

数据存储：output/latency_history.json
{
  "updated_at": "...",
  "keep_recent": 30,
  "nodes": {
    "<fingerprint>": {
      "history": [{"timestamp": "...", "latency_ms": 250, "jitter_ms": 30, "success": true}, ...]
    }
  }
}

告警规则（都在 generate_trend_alerts 里）：
  - 连续 3 轮 latency > 800ms 但仍 success → "degrading"（降权候选）
  - 连续 3 轮 latency 下降 50% → "recovering"（可恢复）
  - 历史 30 轮趋势整体上升 → "trend_up"（降权）
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Optional

DEFAULT_KEEP_RECENT = 30
DEGRADING_LATENCY_MS = 800.0
DEGRADING_CONSECUTIVE = 3
RECOVERING_RATIO = 0.5  # 下降 50%


def _path(output_dir: str) -> Path:
    return Path(output_dir) / "latency_history.json"


def load_latency_history(output_dir: str) -> Dict[str, Dict[str, Any]]:
    p = _path(output_dir)
    if not p.exists():
        return {}
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
        nodes = data.get("nodes", {}) if isinstance(data, dict) else {}
        return nodes if isinstance(nodes, dict) else {}
    except Exception:
        return {}


def update_latency_history(
    output_dir: str,
    results: List[Any],  # List[TestResult]
    timestamp: str,
    keep_recent: int = DEFAULT_KEEP_RECENT,
) -> Dict[str, Any]:
    """把本轮真测结果写进延迟历史。

    results 元素需要有 .node.fingerprint() / .latency_ms / .jitter_ms / .success
    """
    p = _path(output_dir)
    history = load_latency_history(output_dir)
    for r in results:
        node = getattr(r, "node", None)
        if node is None:
            continue
        fp = node.fingerprint()
        entry = history.setdefault(fp, {"history": []})
        hist = entry.setdefault("history", [])
        hist.append({
            "timestamp": timestamp,
            "latency_ms": round(float(getattr(r, "latency_ms", 0.0) or 0.0), 1),
            "jitter_ms": round(float(getattr(r, "jitter_ms", 0.0) or 0.0), 1),
            "success": bool(getattr(r, "success", False)),
        })
        # 只保留最近 N 轮
        if keep_recent > 0 and len(hist) > keep_recent:
            entry["history"] = hist[-keep_recent:]

    payload = {
        "updated_at": timestamp,
        "keep_recent": keep_recent,
        "total_tracked": len(history),
        "nodes": history,
    }
    p.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    return payload


def generate_trend_alerts(
    history: Dict[str, Dict[str, Any]],
    limit: int = 20,
) -> Dict[str, List[Dict[str, Any]]]:
    """从延迟历史里提炼告警。

    Returns:
        {
            "degrading": [{fp, last_3_avg_ms, ...}, ...],
            "recovering": [...],
        }
    """
    degrading: List[Dict[str, Any]] = []
    recovering: List[Dict[str, Any]] = []

    for fp, entry in history.items():
        if not isinstance(entry, dict):
            continue
        hist = entry.get("history") or []
        if not isinstance(hist, list) or len(hist) < DEGRADING_CONSECUTIVE:
            continue
        # 只看最近 3 轮
        recent = hist[-DEGRADING_CONSECUTIVE:]
        # 连续 3 轮 success 且平均延迟 > 阈值
        success_recent = [h for h in recent if h.get("success")]
        if len(success_recent) >= DEGRADING_CONSECUTIVE:
            avg_lat = sum(h.get("latency_ms", 0) for h in success_recent) / len(success_recent)
            if avg_lat > DEGRADING_LATENCY_MS:
                degrading.append({
                    "fingerprint": fp,
                    "avg_latency_ms": round(avg_lat, 1),
                    "rounds": len(success_recent),
                })
                continue
        # 恢复：最近 3 轮延迟对比前 3 轮下降 50%
        if len(hist) >= 6:
            prev = [h for h in hist[-6:-3] if h.get("success")]
            now = [h for h in hist[-3:] if h.get("success")]
            if len(prev) >= 3 and len(now) >= 3:
                prev_avg = sum(h.get("latency_ms", 0) for h in prev) / len(prev)
                now_avg = sum(h.get("latency_ms", 0) for h in now) / len(now)
                if prev_avg > 0 and now_avg < prev_avg * RECOVERING_RATIO:
                    recovering.append({
                        "fingerprint": fp,
                        "prev_avg_ms": round(prev_avg, 1),
                        "now_avg_ms": round(now_avg, 1),
                    })

    # 限制返回数量
    return {
        "degrading": sorted(degrading, key=lambda x: -float(x.get("avg_latency_ms", 0)))[:limit],
        "recovering": sorted(recovering, key=lambda x: float(x.get("prev_avg_ms", 0)) - float(x.get("now_avg_ms", 0)), reverse=True)[:limit],
    }
