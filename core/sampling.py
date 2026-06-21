"""Sampling helpers for real proxy tests."""
from __future__ import annotations

from typing import Dict, List, Tuple

from core.parser import Node


# 协议优先级（数字越小越好；reality > hy2 > tuic > trojan > vmess > ss）
PROTO_PRIORITY = {
    "vless": 0, "hysteria2": 1, "tuic": 2, "trojan": 3,
    "vmess": 4, "anytls": 4,
    "shadowsocks": 5, "shadowsocksr": 6,
    "socks": 7, "http": 7,
}


def protocol_priority(t: str) -> int:
    return PROTO_PRIORITY.get(t, 9)


def sample_for_real_test(nodes: List[Node], tcp_latency: Dict[str, float], limit: int) -> List[Node]:
    if limit <= 0 or len(nodes) <= limit:
        return nodes

    by_type: Dict[str, List[Node]] = {}
    for n in nodes:
        by_type.setdefault(n.type, []).append(n)
    for lst in by_type.values():
        lst.sort(key=lambda n: tcp_latency.get(n.fingerprint(), float("inf")))

    sampled: List[Node] = []
    used = set()
    per = max(limit // max(len(by_type), 1), 1)
    for t in sorted(by_type, key=protocol_priority):
        for n in by_type[t][:per]:
            if len(sampled) >= limit:
                return sampled
            fp = n.fingerprint()
            if fp not in used:
                sampled.append(n)
                used.add(fp)

    remaining = [
        n for n in nodes
        if n.fingerprint() not in used
    ]
    remaining.sort(key=lambda n: (tcp_latency.get(n.fingerprint(), float("inf")), protocol_priority(n.type)))
    sampled.extend(remaining[:max(limit - len(sampled), 0)])
    return sampled[:limit]


def sample_for_real_test_weighted(
    nodes: List[Node],
    tcp_latency: Dict[str, float],
    limit: int,
    node_source_map: Dict[str, str],
    protocol_rates: Dict[str, float],
    source_rates: Dict[str, float],
) -> List[Node]:
    if limit <= 0 or len(nodes) <= limit:
        return nodes
    base_quota = max(limit // 5, 1)
    sampled = sample_for_real_test(nodes, tcp_latency, min(base_quota, limit))
    used = {n.fingerprint() for n in sampled}

    def score(n: Node) -> Tuple[float, float, int]:
        fp = n.fingerprint()
        src = node_source_map.get(fp, "")
        source_rate = source_rates.get(src, 0.5)
        protocol_rate = protocol_rates.get(n.type, 0.5)
        latency = tcp_latency.get(fp, float("inf"))
        return (-(source_rate * 0.7 + protocol_rate * 0.3), latency, protocol_priority(n.type))

    remaining = [n for n in nodes if n.fingerprint() not in used]
    remaining.sort(key=score)
    sampled.extend(remaining[:max(limit - len(sampled), 0)])
    return sampled[:limit]