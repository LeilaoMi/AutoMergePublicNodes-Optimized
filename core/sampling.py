"""真测采样助手。"""
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
    """[P0-2] 双层采样：协议多样性探索 + 历史通过率加权。

    旧实现只采样 1/5 探索，剩下的纯按历史排序。问题：
      - 新协议/新源永远进不去真测（被历史高分源挤掉）
      - 长尾节点被永久饿死
      - 协议分布逐渐塌缩到 top3

    新实现：
      1. phase1 探索：保证每个协议至少 N 个节点进入真测，避免协议分布塌缩
      2. phase2 加权：剩下的按 (source_rate, protocol_rate, latency) 排序
      3. 同协议内按 TCP 延迟升序（旧的 latency tiebreaker 行为不变）
    """
    if limit <= 0 or len(nodes) <= limit:
        return nodes

    # phase1: 协议多样性探索（占 30% 配额，按 TCP 延迟从各协议里均匀挑）
    explore_quota = max(int(limit * 0.3), len(set(n.type for n in nodes)))
    explore_quota = min(explore_quota, limit)
    sampled = sample_for_real_test(nodes, tcp_latency, explore_quota)
    used = {n.fingerprint() for n in sampled}

    def score(n: Node) -> Tuple[float, float, int]:
        fp = n.fingerprint()
        src = node_source_map.get(fp, "")
        source_rate = source_rates.get(src, 0.5)
        protocol_rate = protocol_rates.get(n.type, 0.5)
        latency = tcp_latency.get(fp, float("inf"))
        return (-(source_rate * 0.7 + protocol_rate * 0.3), latency, protocol_priority(n.type))

    # phase2: 历史加权（占 70% 配额）
    remaining = [n for n in nodes if n.fingerprint() not in used]
    remaining.sort(key=score)
    sampled.extend(remaining[:max(limit - len(sampled), 0)])
    return sampled[:limit]