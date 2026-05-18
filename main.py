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
from typing import Dict, List

# 让脚本能直接运行
sys.path.insert(0, str(Path(__file__).resolve().parent))

from core.fetcher import Source, fetch_all, load_sources, FetchResult
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


async def tcp_check_batch(nodes: List[Node], concurrency: int = 200, timeout: float = 3.0) -> List[Node]:
    """快速 TCP 预筛选：仅保留端口可达的节点"""
    sem = asyncio.Semaphore(concurrency)

    async def _check(n: Node) -> bool:
        async with sem:
            try:
                fut = asyncio.open_connection(n.server, n.server_port)
                reader, writer = await asyncio.wait_for(fut, timeout=timeout)
                writer.close()
                try:
                    await writer.wait_closed()
                except Exception:
                    pass
                return True
            except Exception:
                return False

    results = await asyncio.gather(*[_check(n) for n in nodes], return_exceptions=True)
    return [n for n, ok in zip(nodes, results) if ok is True]


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
    for r in fr_list:
        for n in r.nodes:
            all_nodes.append(n)
            proto_count[n.type] = proto_count.get(n.type, 0) + 1

    # 3) 去重
    nodes = dedupe(all_nodes)
    print(f"[3/6] 去重: {len(all_nodes)} -> {len(nodes)}")
    for k, v in sorted(proto_count.items(), key=lambda x: -x[1]):
        print(f"        {k:14s}: {v}")

    # 4) TCP 预筛选
    if args.tcp_check:
        print(f"[4/6] TCP 预筛选（并发 {args.tcp_concurrency}, 超时 {args.tcp_timeout}s）...")
        nodes = await tcp_check_batch(nodes, args.tcp_concurrency, args.tcp_timeout)
        print(f"      TCP 可达: {len(nodes)}")
    else:
        print(f"[4/6] 跳过 TCP 预筛选")

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
            [(r.node, r.latency_ms) for r in results if r.success],
            key=lambda x: x[1],
        )
        print(f"      真实可用: {len(valid)}/{len(nodes)}")
        if valid:
            print(f"      最快: {valid[0][1]}ms  最慢: {valid[-1][1]}ms")
    else:
        valid = [(n, 0) for n in nodes]
        print(f"[5/6] 跳过真实测试")

    # 取 Top N 并改名加入延迟
    top = valid[:args.top_n]
    final_nodes: List[Node] = []
    for i, (n, lat) in enumerate(top, 1):
        if lat > 0:
            n.tag = f"[{lat:>4}ms] {n.tag[:30]}"
        final_nodes.append(n)

    # 6) 生成输出
    print(f"[6/6] 生成订阅文件...")
    from core.generator import write_outputs
    n_top = write_outputs(final_nodes, args.output_dir, prefix="top50")
    # 同时生成全量备份
    all_valid = [n for n, _ in valid]
    n_all = write_outputs(all_valid, args.output_dir, prefix="all")

    elapsed = time.time() - t0
    print(f"\n┌─────────────────────────────────────────────┐")
    print(f"│  ✅ 完成 [{elapsed:.1f}s]                       ")
    print(f"│  • 原始节点:  {total_raw:>6}")
    print(f"│  • 去重后:    {len(set(nd.fingerprint() for nd in all_nodes)):>6}")
    print(f"│  • TCP 可达:  {len(nodes):>6}")
    print(f"│  • 真实可用:  {len(valid):>6}")
    print(f"│  • Top 输出:  {n_top:>6}")
    print(f"└─────────────────────────────────────────────┘")

    # 统计 JSON
    stats = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "duration_sec": round(elapsed, 1),
        "sources_total": len(sources),
        "sources_healthy": healthy,
        "nodes_raw": total_raw,
        "nodes_dedup": len(set(nd.fingerprint() for nd in all_nodes)),
        "nodes_tcp_ok": len(nodes),
        "nodes_real_ok": len(valid),
        "nodes_output": n_top,
        "protocol_dist": proto_count,
        "top_latencies_ms": [lat for _, lat in top if lat > 0][:20],
    }
    os.makedirs(args.output_dir, exist_ok=True)
    with open(f"{args.output_dir}/stats.json", "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--sources", default="config/sources.yaml")
    p.add_argument("--output-dir", default="output")
    p.add_argument("--singbox", default="./sing-box")
    p.add_argument("--top-n", type=int, default=50, help="最终输出的节点数")

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

    args = p.parse_args()
    asyncio.run(run(args))


if __name__ == "__main__":
    main()
