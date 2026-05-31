#!/usr/bin/env python3
"""
autonodes - 主入口
功能流水线:
1) 抓取所有订阅源（异步并发）
2) 解析全协议节点（vmess/vless/trojan/ss/ssr/hysteria/hysteria2/tuic/anytls/wireguard/socks5/http）
3) 去重 + TCP 预筛选
4) sing-box 真实代理测试（Karing 同源内核）
5) 按延迟排序，取 Top N
6) 生成多格式订阅
"""
from __future__ import annotations

import argparse
import asyncio
import json
import os
import socket
import sys
import time
from pathlib import Path
from typing import Dict, List, Tuple

# 让脚本能直接运行
sys.path.insert(0, str(Path(__file__).resolve().parent))

from core.fetcher import Source, fetch_all, load_sources, FetchResult
from core.geo import geo_flag_map, flag_for_server
from core.parser import Node


def dedupe(nodes: List[Node]) -> List[Node]:
    seen = set()
    out = []
    for n in nodes:
        fp = n.fingerprint()
        if fp in seen:
            continue
        seen.add(fp)
        out.append(n)
    return out


# 协议优先级（数字越小越好；reality > hy2 > tuic > trojan > vmess > ss）
_PROTO_PRIORITY = {
    "vless": 0, "hysteria2": 1, "tuic": 2, "trojan": 3,
    "vmess": 4, "anytls": 4, "wireguard": 4,
    "shadowsocks": 5, "shadowsocksr": 6,
    "socks": 7, "http": 7,
}


def protocol_priority(t: str) -> int:
    return _PROTO_PRIORITY.get(t, 9)


# 端口黑名单（容易被运营商干扰 / 明文）
_PORT_BLOCKLIST = {0, 80, 8080}


def quality_prefilter(nodes: List[Node]) -> List[Node]:
    """质量预过滤：剔除无效端口、按 server+protocol 强去重、同 server 限 2 个"""
    # 1) 端口黑名单
    nodes = [n for n in nodes if n.server_port not in _PORT_BLOCKLIST]

    # 2) 同 server+protocol+port 已经被 dedupe 处理；这里按 (server, type) 再去重
    by_st: Dict[tuple, Node] = {}
    for n in nodes:
        key = (n.server, n.type)
        if key not in by_st:
            by_st[key] = n
    step2 = list(by_st.values())

    # 3) 同 server IP 最多保留 2 个（按协议优先级排）
    by_server: Dict[str, List[Node]] = {}
    for n in step2:
        by_server.setdefault(n.server, []).append(n)
    out: List[Node] = []
    for server, lst in by_server.items():
        lst.sort(key=lambda n: protocol_priority(n.type))
        out.extend(lst[:2])
    return out


async def tcp_check_batch(nodes: List[Node], concurrency: int = 200, timeout: float = 3.0) -> List[Tuple[Node, float]]:
    """快速 TCP 预筛选：返回 [(node, tcp_latency_ms)]，按延迟升序"""
    sem = asyncio.Semaphore(concurrency)

    async def _check(n: Node):
        async with sem:
            t0 = time.perf_counter()
            try:
                fut = asyncio.open_connection(n.server, n.server_port)
                reader, writer = await asyncio.wait_for(fut, timeout=timeout)
                lat_ms = (time.perf_counter() - t0) * 1000
                writer.close()
                try:
                    await writer.wait_closed()
                except Exception:
                    pass
                return (n, lat_ms)
            except Exception:
                return None

    results = await asyncio.gather(*[_check(n) for n in nodes], return_exceptions=True)
    ok = [r for r in results if isinstance(r, tuple)]
    ok.sort(key=lambda x: x[1])
    return ok


async def run(args):
    t0 = time.time()
    print(f"╔══════════════════════════════════════════════╗")
    print(f"║  autonodes - 自动节点聚合 + 真实测试        ║")
    print(f"╚══════════════════════════════════════════════╝\n")

    # 1) 加载订阅源
    sources = load_sources(args.sources)
    print(f"[1/6] 加载 {len(sources)} 个订阅源")

    # 2) 抓取
    print(f"[2/6] 异步抓取（并发 {args.fetch_concurrency}）...")
    fr_list = await fetch_all(sources, concurrency=args.fetch_concurrency, timeout=args.fetch_timeout)

    total_raw = sum(len(r.nodes) for r in fr_list)
    healthy = sum(1 for r in fr_list if r.success and len(r.nodes) > 0)
    print(f"      抓取完成: {healthy}/{len(sources)} 源有节点, 共 {total_raw} 个原始节点")

    all_nodes: List[Node] = []
    proto_count: Dict[str, int] = {}
    # 跟踪每个节点来自哪个 source（用于 per-source 通过率统计）
    node_source_map: Dict[str, str] = {}  # fingerprint -> source_name
    for r in fr_list:
        src_name = r.source.name or r.source.url[:80]
        for n in r.nodes:
            all_nodes.append(n)
            proto_count[n.type] = proto_count.get(n.type, 0) + 1
            node_source_map.setdefault(n.fingerprint(), src_name)

    # 3) 去重
    nodes = dedupe(all_nodes)
    dedup_pool = list(nodes)  # 保存完整 deduped 池(8K+),供 all.* 输出

    # GeoIP 国旗映射
    print(f"      GeoIP 查询（batch ip-api.com）...")
    flag_map = await geo_flag_map(all_nodes)
    print(f"      国旗映射: {len(flag_map)} 个 IP")

    print(f"[3/6] 去重: {len(all_nodes)} -> {len(nodes)}")
    for k, v in sorted(proto_count.items(), key=lambda x: -x[1]):
        print(f"        {k:14s}: {v}")

    # 3.5) 质量预过滤 (可选)
    if args.quality_filter:
        before = len(nodes)
        nodes = quality_prefilter(nodes)
        print(f"[3.5] 质量过滤（端口黑名单 + 同 server 限 2）: {before} -> {len(nodes)}")
    else:
        print(f"[3.5] 跳过质量过滤（输出全部去重节点）")

    # 4) TCP 预筛选
    if args.tcp_check:
        print(f"[4/6] TCP 预筛选（并发 {args.tcp_concurrency}, 超时 {args.tcp_timeout}s）...")
        tcp_results = await tcp_check_batch(nodes, args.tcp_concurrency, args.tcp_timeout)
        print(f"      TCP 可达: {len(tcp_results)}")
        nodes = [n for n, _ in tcp_results]
        tcp_latency = {n.fingerprint(): lat for n, lat in tcp_results}
    else:
        print(f"[4/6] 跳过 TCP 预筛选")
        tcp_latency = {}

    # 限制送入真实测试的数量（控制时间）
    if args.test_limit > 0 and len(nodes) > args.test_limit:
        # 简单分布：按协议分层取样（避免某协议挤占）
        by_type: Dict[str, List[Node]] = {}
        for n in nodes:
            by_type.setdefault(n.type, []).append(n)
        sampled: List[Node] = []
        per = max(args.test_limit // max(len(by_type), 1), 1)
        for t, lst in by_type.items():
            sampled.extend(lst[:per])
        nodes = sampled[:args.test_limit]
        print(f"      下采样: {len(nodes)}（每协议最多 {per} 个）")

    # 5) 真实代理测试（sing-box）
    valid: List[tuple] = []  # [(node, latency_ms)]
    results = []  # 保存全部测试结果（含失败），供统计使用
    if args.real_test and nodes:
        from core.tester import SingBoxTester
        print(f"[5/6] sing-box 真实代理测试（并发 {args.test_concurrency}）...")
        tester = SingBoxTester(
            sb_path=args.singbox,
            concurrency=args.test_concurrency,
            startup_wait=args.startup_wait,
            request_timeout=args.test_timeout,
        )
        results = await tester.test_all(nodes)
        valid = sorted(
            [(r.node, r.latency_ms, r.jitter_ms) for r in results if r.success],
            key=lambda x: x[1],
        )
        print(f"      真实可用: {len(valid)}/{len(nodes)}")
        if valid:
            print(f"      最快: {valid[0][1]:.1f}ms  最慢: {valid[-1][1]:.1f}ms")
    else:
        valid = sorted([(n, tcp_latency.get(n.fingerprint(), 0), 0.0) for n in nodes], key=lambda x: x[1])
        print(f"[5/6] 跳过真实测试")

    # 取 Top N 并改名加入延迟
    top = valid[:args.top_n]
    final_nodes: List[Node] = []
    for i, (n, lat, jit) in enumerate(top, 1):
        flag = flag_for_server(n.server, flag_map)
        prefix = f"{flag} " if flag else ""
        if lat > 0:
            jitter_str = f" +/-{jit:.0f}ms" if jit > 0 else ""
            n.tag = f"{prefix}[{lat:>5.1f}ms{jitter_str}] {n.tag[:30]}"
        final_nodes.append(n)

    # 6) 生成输出
    print(f"[6/6] 生成订阅文件...")
    from core.generator import write_outputs, MAX_TAG_LENGTH, _clamp_tag

    # 在生成输出前统一 clamp tag
    for n in final_nodes:
        n.tag = _clamp_tag(n.tag)

    n_top = write_outputs(final_nodes, args.output_dir, prefix="verified")
    # 同时生成全量备份(未测速,供客户端再测)
    # all.* = dedup 后完整池(不含质量过滤/TCP/测速),客户端可全测
    all_valid = dedup_pool
    n_all = write_outputs(all_valid, args.output_dir, prefix="all")

    elapsed = time.time() - t0
    print(f"\n┌─────────────────────────────────────────────┐")
    print(f"│  ✅ 完成 [{elapsed:.1f}s]                       ")
    print(f"│  • 原始节点:  {total_raw:>6}")
    print(f"│  • 去重后:    {len(set(nd.fingerprint() for nd in all_nodes)):>6}")
    print(f"│  • TCP 可达:  {len(nodes):>6}")
    print(f"│  • 真实可用:  {len(valid):>6}")
    print(f"│  • Verified:  {n_top:>6}")
    print(f"└─────────────────────────────────────────────┘")

    # 统计 JSON
    proto_pass: Dict[str, Dict[str, int]] = {}
    for r in results if args.real_test else []:
        t = r.node.type
        if t not in proto_pass:
            proto_pass[t] = {"pass": 0, "fail": 0}
        proto_pass[t]["pass" if r.success else "fail"] += 1

    # per-source 通过率统计
    src_pass: Dict[str, Dict[str, int]] = {}
    for r in results if args.real_test else []:
        src_name = node_source_map.get(r.node.fingerprint(), "unknown")
        if src_name not in src_pass:
            src_pass[src_name] = {"pass": 0, "fail": 0}
        src_pass[src_name]["pass" if r.success else "fail"] += 1

    stats = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "duration_sec": round(elapsed, 1),
        "sources_total": len(sources),
        "sources_healthy": healthy,
        "nodes_raw": total_raw,
        "nodes_dedup": len(set(nd.fingerprint() for nd in all_nodes)),
        "nodes_tcp_ok": len(nodes),
        "nodes_real_ok": len(valid),
        "nodes_verified_output": n_top,
        "protocol_dist": proto_count,
        "protocol_pass_rate": proto_pass,
        "source_pass_rate": src_pass,
        "top_latencies_ms": [round(lat, 1) for _, lat, _ in top if lat > 0][:20],
        "top_jitters_ms": [round(jit, 1) for _, _, jit in top if jit > 0][:20],
    }
    os.makedirs(args.output_dir, exist_ok=True)
    with open(f"{args.output_dir}/stats.json", "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--sources", default="config/sources.yaml")
    p.add_argument("--output-dir", default="output")
    p.add_argument("--singbox", default="./sing-box")
    p.add_argument("--top-n", type=int, default=100, help="最终输出的节点数")

    p.add_argument("--fetch-concurrency", type=int, default=30)
    p.add_argument("--fetch-timeout", type=int, default=15)

    p.add_argument("--tcp-check", action=argparse.BooleanOptionalAction, default=True)
    p.add_argument("--tcp-concurrency", type=int, default=200)
    p.add_argument("--tcp-timeout", type=float, default=3.0)

    p.add_argument("--real-test", action=argparse.BooleanOptionalAction, default=True)
    p.add_argument("--test-concurrency", type=int, default=30)
    p.add_argument("--test-timeout", type=float, default=6.0)
    p.add_argument("--startup-wait", type=float, default=0.6)
    p.add_argument("--test-limit", type=int, default=500, help="送入真实测试的最大节点数(0=不限)")
    p.add_argument("--quality-filter", action=argparse.BooleanOptionalAction, default=True,
                   help="启用质量预过滤（端口黑名单+同server限2）")

    args = p.parse_args()
    # 环境变量覆盖（CI 或容器场景常用）
    if os.environ.get("AUTONODES_TOP_N"):
        args.top_n = int(os.environ["AUTONODES_TOP_N"])
    if os.environ.get("AUTONODES_TEST_LIMIT"):
        args.test_limit = int(os.environ["AUTONODES_TEST_LIMIT"])
    asyncio.run(run(args))


if __name__ == "__main__":
    main()
