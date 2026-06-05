#!/usr/bin/env python3
"""
autonodes - 主入口
功能流水线:
1) 抓取所有订阅源（异步并发）
2) 解析全协议节点（vmess/vless/trojan/ss/ssr/hysteria/hysteria2/tuic/anytls/socks5/http）
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
import sys
import time
from pathlib import Path
from dataclasses import replace
from typing import Dict, List, Tuple

# 让脚本能直接运行
sys.path.insert(0, str(Path(__file__).resolve().parent))

__version__ = "2.1.0"  # §4.5 — 加版本号, 写进 stats.json / health_report

from core.fetcher import fetch_all, load_sources
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
    "vmess": 4, "anytls": 4,
    "shadowsocks": 5, "shadowsocksr": 6,
    "socks": 7, "http": 7,
}


def protocol_priority(t: str) -> int:
    return _PROTO_PRIORITY.get(t, 9)


def _smoothed_pass_rate(stats: Dict[str, int]) -> float:
    passed = int(stats.get("pass", 0) or 0)
    failed = int(stats.get("fail", 0) or 0)
    return (passed + 1) / (passed + failed + 2)


def load_historical_pass_rates(output_dir: str) -> Tuple[Dict[str, float], Dict[str, float]]:
    stats_path = Path(output_dir) / "stats.json"
    if not stats_path.exists():
        return {}, {}
    try:
        stats = json.loads(stats_path.read_text(encoding="utf-8"))
    except Exception:
        return {}, {}
    protocol_rates = {
        name: _smoothed_pass_rate(values)
        for name, values in (stats.get("protocol_pass_rate") or {}).items()
        if isinstance(values, dict)
    }
    source_rates = {
        name: _smoothed_pass_rate(values)
        for name, values in (stats.get("source_pass_rate") or {}).items()
        if isinstance(values, dict)
    }
    return protocol_rates, source_rates


# 端口黑名单。80/8080 可能是合法 WS/TLS/HTTP 伪装端口，不再硬删除。
_PORT_BLOCKLIST = {0}


def quality_prefilter(nodes: List[Node], max_per_server: int = 0) -> List[Node]:
    """质量预过滤：剔除无效端口、按 server+protocol 强去重、同 server 限 max_per_server 个

    §2.2 — 把"同 server 限 2"改为 CLI 参数, 默认 0 = 不限
    原因: 大型 VPS (AWS Lightsail / Azure / Hetzner) 上可能跑多个不同用户不同协议的节点,
    盲目限 2 会误杀一批本应保留的节点。如果限流, 建议在真测通过后做。
    """
    # 1) 端口黑名单
    nodes = [n for n in nodes if n.server_port not in _PORT_BLOCKLIST]

    # 2) 同 server+protocol+port 已经被 dedupe 处理；这里按 (server, type) 再去重
    by_st: Dict[tuple, Node] = {}
    for n in nodes:
        key = (n.server, n.type)
        if key not in by_st:
            by_st[key] = n
    step2 = list(by_st.values())

    # 3) 同 server IP 最多保留 max_per_server 个 (按协议优先级排)
    if max_per_server <= 0:
        return step2
    by_server: Dict[str, List[Node]] = {}
    for n in step2:
        by_server.setdefault(n.server, []).append(n)
    out: List[Node] = []
    for server, lst in by_server.items():
        lst.sort(key=lambda n: protocol_priority(n.type))
        out.extend(lst[:max_per_server])
    return out


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


def build_output_nodes(valid: List[tuple], flag_map: Dict[str, str], top_n: int) -> List[Node]:
    output_nodes: List[Node] = []
    for i, (n, lat, jit) in enumerate(valid[:top_n], 1):
        flag = flag_for_server(n.server, flag_map)
        prefix = f"{flag} " if flag else ""
        new_tag = n.tag
        if lat > 0:
            jitter_str = f" +/-{jit:.0f}ms" if jit > 0 else ""
            new_tag = f"{prefix}[{lat:>5.1f}ms{jitter_str}] {n.tag}"
        output_nodes.append(replace(n, tag=new_tag))
    return output_nodes


async def tcp_check_batch(nodes: List[Node], concurrency: int = 200, timeout: float = 3.0) -> List[Tuple[Node, float]]:
    """快速 TCP 预筛选：返回 [(node, tcp_latency_ms)]，按延迟升序"""
    queue: asyncio.Queue[Node] = asyncio.Queue()
    for n in nodes:
        queue.put_nowait(n)

    ok: List[Tuple[Node, float]] = []

    async def _worker():
        while True:
            try:
                n = queue.get_nowait()
            except asyncio.QueueEmpty:
                return
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
                ok.append((n, lat_ms))
            except Exception:
                pass
            finally:
                queue.task_done()

    worker_count = min(max(concurrency, 1), len(nodes))
    if worker_count > 0:
        await asyncio.gather(*[asyncio.create_task(_worker()) for _ in range(worker_count)])
    ok.sort(key=lambda x: x[1])
    return ok


async def run(args):
    t0 = time.time()
    stage_durations: Dict[str, float] = {}
    stage_start = t0
    print(f"╔══════════════════════════════════════════════╗")
    print(f"║  autonodes - 自动节点聚合 + 真实测试        ║")
    print(f"╚══════════════════════════════════════════════╝\n")

    # 1) 加载订阅源
    sources = load_sources(args.sources)
    protocol_rates, source_rates = load_historical_pass_rates(args.output_dir)
    print(f"[1/6] 加载 {len(sources)} 个订阅源")
    if protocol_rates or source_rates:
        print(f"      历史通过率: {len(source_rates)} 个源, {len(protocol_rates)} 个协议")

    # 2) 抓取
    print(f"[2/6] 异步抓取（并发 {args.fetch_concurrency}）...")
    fr_list = await fetch_all(sources, concurrency=args.fetch_concurrency, timeout=args.fetch_timeout)
    stage_durations["fetch"] = round(time.time() - stage_start, 1)
    stage_start = time.time()

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
    stage_durations["geo"] = round(time.time() - stage_start, 1)
    stage_start = time.time()
    print(f"      国旗映射: {len(flag_map)} 个 IP")

    print(f"[3/6] 去重: {len(all_nodes)} -> {len(nodes)}")
    for k, v in sorted(proto_count.items(), key=lambda x: -x[1]):
        print(f"        {k:14s}: {v}")

    # 3.5) 质量预过滤 (可选)
    if args.quality_filter:
        before = len(nodes)
        nodes = quality_prefilter(nodes, max_per_server=args.max_per_server)
        if args.max_per_server > 0:
            print(f"[3.5] 质量过滤（端口黑名单 + 同 server 限 {args.max_per_server}）: {before} -> {len(nodes)}")
        else:
            print(f"[3.5] 质量过滤（端口黑名单, 同 server 不限）: {before} -> {len(nodes)}")
    else:
        print(f"[3.5] 跳过质量过滤（输出全部去重节点）")

    # 4) TCP 预筛选
    if args.tcp_check:
        print(f"[4/6] TCP 预筛选（并发 {args.tcp_concurrency}, 超时 {args.tcp_timeout}s）...")
        tcp_results = await tcp_check_batch(nodes, args.tcp_concurrency, args.tcp_timeout)
        stage_durations["tcp"] = round(time.time() - stage_start, 1)
        stage_start = time.time()
        print(f"      TCP 可达: {len(tcp_results)}")
        nodes = [n for n, _ in tcp_results]
        tcp_latency = {n.fingerprint(): lat for n, lat in tcp_results}
    else:
        print(f"[4/6] 跳过 TCP 预筛选")
        tcp_latency = {}
        stage_durations["tcp"] = 0.0
        stage_start = time.time()

    # 限制送入真实测试的数量（控制时间）
    if args.test_limit > 0 and len(nodes) > args.test_limit:
        before_sample = len(nodes)
        nodes = sample_for_real_test_weighted(nodes, tcp_latency, args.test_limit, node_source_map, protocol_rates, source_rates)
        print(f"      下采样: {before_sample} -> {len(nodes)}（协议基础探索 + 历史通过率加权）")

    # 5) 真实代理测试（sing-box）
    valid: List[tuple] = []  # [(node, latency_ms, jitter_ms)]
    results = []  # 保存全部测试结果（含失败），供统计使用
    cn_block_retry_results = []
    cn_block_retry_valid: List[tuple] = []
    real_test_passed = False
    if args.real_test and nodes:
        from core.tester import SingBoxTester
        print(f"[5/6] sing-box 真实代理测试（并发 {args.test_concurrency}）...")
        tester = SingBoxTester(
            sb_path=args.singbox,
            concurrency=args.test_concurrency,
            startup_wait=args.startup_wait,
            request_timeout=args.test_timeout,
            min_latency_ms=args.min_latency,
        )
        results = await tester.test_all(nodes)
        stage_durations["real_test"] = round(time.time() - stage_start, 1)
        stage_start = time.time()
        valid = sorted(
            [(r.node, r.latency_ms, r.jitter_ms) for r in results if r.success],
            key=lambda x: x[1],
        )
        real_test_passed = bool(valid)
        print(f"      真实可用: {len(valid)}/{len(nodes)}")
        if valid:
            print(f"      最快: {valid[0][1]:.1f}ms  最慢: {valid[-1][1]:.1f}ms")

        if args.global_output and results:
            cn_block_nodes = [r.node for r in results if (not r.success and r.error.startswith("cn-block:"))]
            if cn_block_nodes:
                print(f"      Global 兼顾复测（跳过百度连通）: {len(cn_block_nodes)} 个...")
                global_tester = SingBoxTester(
                    sb_path=args.singbox,
                    concurrency=args.test_concurrency,
                    startup_wait=args.startup_wait,
                    request_timeout=args.test_timeout,
                    min_latency_ms=args.min_latency,
                    skip_target_kinds={"cn-block"},
                )
                cn_block_retry_results = await global_tester.test_all(cn_block_nodes)
                cn_block_retry_valid = sorted(
                    [(r.node, r.latency_ms, r.jitter_ms) for r in cn_block_retry_results if r.success],
                    key=lambda x: x[1],
                )
                print(f"      Global 追加可用: {len(cn_block_retry_valid)}/{len(cn_block_nodes)}")
    else:
        print(f"[5/6] 跳过真实测试")
        stage_durations["real_test"] = 0.0
        stage_start = time.time()

    if not args.real_test:
        cn_block_retry_results = []
        cn_block_retry_valid = []

    # TCP 延迟只保留为"是否可达"信息, 不参与延迟排序. 真测 0 通过时显式失败.
    if real_test_passed:
        pass
    elif not args.real_test:
        # 用户主动跳过真测, 用 TCP 延迟填充 (向后兼容)
        valid = sorted(
            [(n, tcp_latency.get(n.fingerprint(), 0), 0.0) for n in nodes],
            key=lambda x: x[1],
        )
        print(f"[5/6] TCP 模式: {len(valid)} 节点")
    else:
        # 真测 0 成功: 报警并退出, 不静默回退到 TCP 延迟
        # 统计失败原因, 方便排查
        err_counter: Dict[str, int] = {}
        for r in results:
            if not r.success and r.error:
                # 只取前 60 字符防止爆内存
                key = r.error[:60]
                err_counter[key] = err_counter.get(key, 0) + 1
        top_errs = sorted(err_counter.items(), key=lambda x: -x[1])[:5]
        print(f"      ❌ 真测 0 通过 — sing-box 启动 / 端点可达性 / ip-api 限流可能异常")
        for err, cnt in top_errs:
            print(f"        [{cnt}×] {err}")
        # 把失败原因暂存到全局给 stats 阶段用
        global _REAL_TEST_FAIL_REASONS
        _REAL_TEST_FAIL_REASONS = dict(err_counter)
        # verified 输出空, 写 stats 后 SystemExit
        valid = []

    # 真实测试失败原因统计 — 让 stats.json 自带诊断
    real_test_errors: Dict[str, int] = {}
    real_test_error_details_counter: Dict[str, int] = {}
    for r in results if args.real_test else []:
        if r.success:
            continue
        error = r.error or "unknown"
        err_key = error.split(":", 1)[0]
        real_test_errors[err_key] = real_test_errors.get(err_key, 0) + 1
        detail_key = error[:120]
        real_test_error_details_counter[detail_key] = real_test_error_details_counter.get(detail_key, 0) + 1
    real_test_error_details = [
        {"error": error, "count": count}
        for error, count in sorted(real_test_error_details_counter.items(), key=lambda x: -x[1])[:10]
    ]

    # 取 Top N 并改名加入延迟。构造新 Node，避免污染 all.* 的原始去重池。
    # §2.1 tag 不再在 main.py 截断 30 字符, 留给 generator._clamp_tag 统一处理
    top = valid[:args.top_n]
    final_nodes = build_output_nodes(valid, flag_map, args.top_n)
    global_valid = sorted(valid + cn_block_retry_valid, key=lambda x: x[1])
    global_nodes = build_output_nodes(global_valid, flag_map, args.top_n)

    # 6) 生成输出
    print(f"[6/6] 生成订阅文件...")
    from core.generator import write_outputs

    n_top = write_outputs(final_nodes, args.output_dir, prefix="verified", repo_path=args.repo, branch=args.branch)
    n_global = write_outputs(global_nodes, args.output_dir, prefix="global", repo_path=args.repo, branch=args.branch) if args.global_output else 0
    # 同时生成全量备份(未测速,供客户端再测)
    # all.* = dedup 后完整池(不含质量过滤/TCP/测速),客户端可全测
    all_valid = dedup_pool
    n_all = write_outputs(
        all_valid,
        args.output_dir,
        prefix="all",
        repo_path=args.repo,
        flag_map=flag_map,
        branch=args.branch,
        mode=args.all_output_mode,
    )
    stage_durations["generate"] = round(time.time() - stage_start, 1)

    elapsed = time.time() - t0
    print(f"\n┌─────────────────────────────────────────────┐")
    print(f"│  ✅ 完成 [{elapsed:.1f}s]                       ")
    print(f"│  • 原始节点:  {total_raw:>6}")
    print(f"│  • 去重后:    {len(set(nd.fingerprint() for nd in all_nodes)):>6}")
    print(f"│  • TCP 可达:  {len(nodes):>6}")
    print(f"│  • 真实可用:  {len(valid):>6}")
    print(f"│  • Verified:  {n_top:>6}")
    if args.global_output:
        print(f"│  • Global:    {n_global:>6}")
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
        "version": __version__,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "duration_sec": round(elapsed, 1),
        "stage_durations": stage_durations,
        "sources_total": len(sources),
        "sources_healthy": healthy,
        "nodes_raw": total_raw,
        "nodes_dedup": len(set(nd.fingerprint() for nd in all_nodes)),
        "nodes_tcp_ok": len(nodes),
        "nodes_real_ok": len(valid),
        "nodes_verified_output": n_top,
        "nodes_global_output": n_global,
        "nodes_global_extra_from_cn_block": len(cn_block_retry_valid),
        "global_skip_target_kinds": ["cn-block"] if args.global_output else [],
        "nodes_all_output": n_all,
        "all_output_mode": args.all_output_mode,
        "protocol_dist": proto_count,
        "protocol_pass_rate": proto_pass,
        "source_pass_rate": src_pass,
        "real_test_errors": real_test_errors,
        "real_test_error_details": real_test_error_details,
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
                   help="启用质量预过滤（端口黑名单）")
    p.add_argument("--max-per-server", type=int, default=0,
                   help="§2.2 同 server IP 最多保留的节点数 (0=不限, 默认; 1/2=严格, 但可能误杀 AWS/Hetzner 上不同用户的节点)")
    p.add_argument("--min-latency", type=float, default=30.0,
                   help="真实测试最低延迟阈值(ms)，低于此值视为可疑；设为 0 可关闭")
    p.add_argument("--global-output", action=argparse.BooleanOptionalAction, default=True,
                   help="生成 global.* 兼顾输出：严格 verified 之外，复测并纳入仅因百度连通失败的节点")
    p.add_argument("--all-output-mode", choices=("full", "light"), default=os.environ.get("AUTONODES_ALL_OUTPUT_MODE", "full"),
                   help="all.* 输出模式: full=全格式兼容旧 URL; light=只保留 txt/urls/converter, 降低大文件成本")
    p.add_argument("--repo", default="LeilaoMi/AutoMergePublicNodes-Optimized",
                   help="用于生成 jsDelivr 订阅转换链接的 owner/repo")
    p.add_argument("--branch", default=os.environ.get("AUTONODES_BRANCH", "main"),
                   help="用于生成 jsDelivr 订阅转换链接的分支名 (默认 main; CI 传入 ${{ github.event.repository.default_branch }})")

    args = p.parse_args()
    
    # 参数验证
    if args.top_n < 0:
        p.error("--top-n 必须 >= 0")
    if args.fetch_concurrency <= 0:
        p.error("--fetch-concurrency 必须 > 0")
    if args.tcp_concurrency <= 0:
        p.error("--tcp-concurrency 必须 > 0")
    if args.test_concurrency <= 0:
        p.error("--test-concurrency 必须 > 0")
    if args.test_limit < 0:
        p.error("--test-limit 必须 >= 0")
    if args.min_latency < 0:
        p.error("--min-latency 必须 >= 0")
    
    # 环境变量覆盖（CI 或容器场景常用）
    if os.environ.get("AUTONODES_TOP_N"):
        args.top_n = int(os.environ["AUTONODES_TOP_N"])
    if os.environ.get("AUTONODES_TEST_LIMIT"):
        args.test_limit = int(os.environ["AUTONODES_TEST_LIMIT"])
    asyncio.run(run(args))


if __name__ == "__main__":
    main()
