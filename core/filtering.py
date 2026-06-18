"""节点质量过滤助手。

保留可配置的质量规则与服务器级预筛选逻辑，避免 main.py 臃肿。
"""
from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List, Tuple

import yaml

from core.parser import Node


# 端口黑名单。80/8080 可能是合法 WS/TLS/HTTP 伪装端口，不再硬删除。
PORT_BLOCKLIST = {0}
DEFAULT_FILTER_RULES: Dict[str, Any] = {
    "enabled": True,
    "mode": "block",
    "blocked": {"ports": sorted(PORT_BLOCKLIST)},
}


def load_filter_rules(path: str | None) -> Dict[str, Any]:
    """加载质量过滤规则。

    配置缺失或解析失败时返回保守默认规则，避免 CI 因本地配置问题中断。
    """
    if not path:
        return dict(DEFAULT_FILTER_RULES)
    p = Path(path)
    if not p.exists():
        return dict(DEFAULT_FILTER_RULES)
    try:
        data = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
    except Exception as exc:
        print(f"      ⚠️  过滤规则读取失败，使用默认规则: {exc}")
        return dict(DEFAULT_FILTER_RULES)
    if not isinstance(data, dict):
        return dict(DEFAULT_FILTER_RULES)
    data.setdefault("enabled", True)
    data.setdefault("mode", "block")
    data.setdefault("blocked", {})
    return data


def _lower_set(values: Any) -> set[str]:
    if not isinstance(values, list):
        return set()
    return {str(v).strip().lower() for v in values if str(v).strip()}


def filter_rule_reasons(n: Node, rules: Dict[str, Any]) -> List[str]:
    """返回节点命中过滤规则的原因列表。"""
    if not rules or rules.get("enabled") is False:
        return []
    blocked = rules.get("blocked") or {}
    reasons: List[str] = []

    ports = {int(p) for p in blocked.get("ports", list(PORT_BLOCKLIST)) if str(p).lstrip("-").isdigit()}
    if n.server_port in ports:
        reasons.append(f"port:{n.server_port}")

    protocols = _lower_set(blocked.get("protocols"))
    if n.type.lower() in protocols:
        reasons.append(f"protocol:{n.type}")

    if n.type == "shadowsocks":
        method = str(n.raw.get("method", "")).lower()
        if method in _lower_set(blocked.get("ss_methods")):
            reasons.append(f"ss_method:{method}")

    if n.type == "shadowsocksr":
        method = str(n.raw.get("method", "")).lower()
        if method in _lower_set(blocked.get("ssr_methods")):
            reasons.append(f"ssr_method:{method}")

    if n.type == "vmess":
        security = str(n.raw.get("security", "")).lower()
        if security in _lower_set(blocked.get("vmess_security")):
            reasons.append(f"vmess_security:{security}")
        network = str((n.raw.get("transport") or {}).get("type", "tcp")).lower()
        clash_network = "h2" if network == "http" else network
        if clash_network in _lower_set(blocked.get("vmess_network")):
            reasons.append(f"vmess_network:{clash_network}")

    return reasons


def quality_prefilter(
    nodes: List[Node],
    max_per_server: int = 0,
    rules: Dict[str, Any] | None = None,
    protocol_priority=None,
    strong_dedup: bool = False,
) -> Tuple[List[Node], Dict[str, int]]:
    """质量预过滤：配置化剔除异常协议特征、按 server+protocol 强去重、同 server 限流。

    [P1-1] 新增 strong_dedup：True 时按 (server, port, type, sni, host, path) 强去重。
    旧行为 (server, type) 弱去重保留为默认，向后兼容。

    返回 (过滤后的节点, 命中规则统计)。rules.mode=annotate 时只统计不剔除。
    """
    rules = rules or dict(DEFAULT_FILTER_RULES)
    mode = str(rules.get("mode", "block")).lower()
    priority = protocol_priority or (lambda t: 9)
    reason_counts: Dict[str, int] = {}

    step1: List[Node] = []
    for n in nodes:
        reasons = filter_rule_reasons(n, rules)
        for reason in reasons:
            reason_counts[reason] = reason_counts.get(reason, 0) + 1
        if reasons and mode == "block":
            continue
        step1.append(n)

    # [P1-1] 强去重：按 fingerprint(strong=True) 精确去重
    if strong_dedup:
        seen: set = set()
        step2: List[Node] = []
        for n in step1:
            fp = n.fingerprint(strong=True)
            if fp in seen:
                continue
            seen.add(fp)
            step2.append(n)
    else:
        # 旧行为：(server, type) 弱去重，保留每组第一个
        by_st: Dict[tuple, Node] = {}
        for n in step1:
            key = (n.server, n.type)
            if key not in by_st:
                by_st[key] = n
        step2 = list(by_st.values())

    # 同 server IP 最多保留 max_per_server 个 (按协议优先级排)
    if max_per_server <= 0:
        return step2, reason_counts
    by_server: Dict[str, List[Node]] = {}
    for n in step2:
        by_server.setdefault(n.server, []).append(n)
    out: List[Node] = []
    for server, lst in by_server.items():
        lst.sort(key=lambda n: priority(n.type))
        out.extend(lst[:max_per_server])
    return out, reason_counts
