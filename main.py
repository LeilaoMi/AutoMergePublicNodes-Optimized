#!/usr/bin/env python3
"""
autonodes - 主入口
功能流水线:
1) 抓取所有订阅源（异步并发）
2) 解析全协议节点（vmess/vless/trojan/ss/ssr/hysteria/hysteria2/tuic/anytls/socks5/http）
3) 去重 + TCP 预筛选
4) sing-box 真实代理测试（Karing 同源内核）
5) 综合评分排序，取 Top N
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
from typing import Dict, List, Tuple, Any

# 让脚本能直接运行
sys.path.insert(0, str(Path(__file__).resolve().parent))

__version__ = "2.4.0"  # chunked output + protocol split + node stability + unlock detection + degraded mode

from core.fetcher import fetch_all, load_sources
from core.geo import geo_flag_map, flag_for_server
from core.parser import Node
from core.filtering import load_filter_rules, quality_prefilter, filter_ssrf
from core.sampling import protocol_priority, sample_for_real_test, sample_for_real_test_weighted
from core.stats import build_source_scores, load_historical_pass_rates, update_trend_history, update_node_stability, load_node_stability, get_stable_nodes
from core.scoring import ScoreInput, calculate_score, calculate_score_breakdown, load_scoring_config
from core.report import write_health_report
from core.readme_updater import update_readme_stats


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




def count_existing_urls(output_dir: str, prefix: str) -> int:
    path = Path(output_dir) / f"{prefix}.urls"
    if not path.exists():
        return 0
    try:
        return sum(1 for line in path.read_text(encoding="utf-8").splitlines() if line.strip())
    except Exception:
        return 0


def should_preserve_previous_output(new_count: int, previous_count: int, min_retain_ratio: float) -> bool:
    if previous_count <= 0 or min_retain_ratio <= 0:
        return False
    return new_count < int(previous_count * min_retain_ratio)


async def tcp_check_batch(
    nodes: List[Node],
    concurrency: int = 200,
    timeout: float = 3.0,
    error_counts: Dict[str, int] | None = None,
) -> List[Tuple[Node, float]]:
    """快速 TCP 预筛选：返回 [(node, tcp_latency_ms)]，按延迟升序。

    可选 error_counts 用于记录失败异常类型，便于 stats/health report 定位网络问题。
    """
    queue: asyncio.Queue[Node] = asyncio.Queue()
    for n in nodes:
        queue.put_nowait(n)

    ok: List[Tuple[Node, float]] = []
    errors = error_counts if error_counts is not None else {}

    async def _worker():
        while True:
            try:
                n = queue.get_nowait()
            except asyncio.QueueEmpty:
                return
            t0 = time.perf_counter()
            writer = None
            try:
                fut = asyncio.open_connection(n.server, n.server_port)
                _, writer = await asyncio.wait_for(fut, timeout=timeout)
                lat_ms = (time.perf_counter() - t0) * 1000
                ok.append((n, lat_ms))
            except Exception as exc:
                key = type(exc).__name__
                errors[key] = errors.get(key, 0) + 1
            finally:
                if writer:
                    writer.close()
                    try:
                        await writer.wait_closed()
                    except Exception:
                        pass
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
    scoring_rules_path = getattr(args, "scoring_rules", "config/scoring.yaml")
    scoring_config = load_scoring_config(scoring_rules_path)
    protocol_rates, source_rates = load_historical_pass_rates(args.output_dir)
    print(f"[1/6] 加载 {len(sources)} 个订阅源")
    if protocol_rates or source_rates:
        print(f"      历史通过率: {len(source_rates)} 个源, {len(protocol_rates)} 个协议")

    # 2) 抓取
    print(f"[2/6] 异步抓取（并发 {args.fetch_concurrency}，总超时 {args.fetch_overall_timeout}s）...")
    fr_list = await fetch_all(
        sources,
        concurrency=args.fetch_concurrency,
        timeout=args.fetch_timeout,
        overall_timeout=args.fetch_overall_timeout,
    )
    stage_durations["fetch"] = round(time.time() - stage_start, 1)
    stage_start = time.time()

    total_raw = sum(len(r.nodes) for r in fr_list)
    healthy = sum(1 for r in fr_list if r.success and len(r.nodes) > 0)
    print(f"      抓取完成: {healthy}/{len(sources)} 源有节点, 共 {total_raw} 个原始节点")

    all_nodes: List[Node] = []
    proto_count: Dict[str, int] = {}
    source_nodes: Dict[str, int] = {}
    source_dead_counts: Dict[str, int] = {}
    # 跟踪每个节点来自哪个 source（用于 per-source 通过率统计）
    node_source_map: Dict[str, str] = {}  # fingerprint -> source_name
    for r in fr_list:
        src_name = r.source.name or r.source.url[:80]
        source_nodes[src_name] = source_nodes.get(src_name, 0) + len(r.nodes)
        if not r.success or len(r.nodes) == 0:
            source_dead_counts[src_name] = 1
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

    # 3.4) SSRF 防投毒（无条件执行，不受 --no-quality-filter 影响）
    nodes, ssrf_dropped = filter_ssrf(nodes)
    if ssrf_dropped > 0:
        print(f"[3.4] SSRF 拦截: 剔除 {ssrf_dropped} 个指向私有/元数据地址的节点")

    filter_rule_hits: Dict[str, int] = {}
    # 3.5) 质量预过滤 (可选)
    if args.quality_filter:
        before = len(nodes)
        filter_rules = load_filter_rules(args.filter_rules)
        nodes, filter_rule_hits = quality_prefilter(nodes, max_per_server=args.max_per_server, rules=filter_rules, protocol_priority=protocol_priority)
        mode = str(filter_rules.get("mode", "block"))
        hit_summary = ", ".join(f"{k}={v}" for k, v in sorted(filter_rule_hits.items(), key=lambda x: -x[1])[:5])
        suffix = f"；规则命中: {hit_summary}" if hit_summary else ""
        if args.max_per_server > 0:
            print(f"[3.5] 质量过滤（配置规则 mode={mode} + 同 server 限 {args.max_per_server}）: {before} -> {len(nodes)}{suffix}")
        else:
            print(f"[3.5] 质量过滤（配置规则 mode={mode}, 同 server 不限）: {before} -> {len(nodes)}{suffix}")
    else:
        print(f"[3.5] 跳过质量过滤（输出全部去重节点）")

    # 4) TCP 预筛选
    tcp_errors: Dict[str, int] = {}
    if args.tcp_check:
        print(f"[4/6] TCP 预筛选（并发 {args.tcp_concurrency}, 超时 {args.tcp_timeout}s）...")
        tcp_results = await tcp_check_batch(nodes, args.tcp_concurrency, args.tcp_timeout, tcp_errors)
        stage_durations["tcp"] = round(time.time() - stage_start, 1)
        stage_start = time.time()
        nodes_tcp_reachable = len(tcp_results)  # TCP 真实可达数(下采样前)
        print(f"      TCP 可达: {nodes_tcp_reachable}")
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

    # 4.5) lightweight probe 轻量探活（可选）
    nodes_before_probe = len(nodes)  # TCP 后、probe 前的节点数
    if args.lightweight_probe and args.real_test and nodes:
        from core.tester import SingBoxTester
        print(f"[4.5/6] 轻量探活（并发 {args.probe_concurrency}, 超时 {args.probe_timeout}s）...")
        probe_tester = SingBoxTester(
            sb_path=args.singbox,
            concurrency=args.probe_concurrency,
            startup_wait=args.probe_startup_wait,
            request_timeout=args.probe_timeout,
            min_latency_ms=0,
            probe_only=True,
        )
        probe_results = await probe_tester.test_all(nodes, progress_every=100)
        probe_pass_fps = {r.node.fingerprint() for r in probe_results if r.success}
        before_probe = len(nodes)
        nodes = [n for n in nodes if n.fingerprint() in probe_pass_fps]
        stage_durations["probe"] = round(time.time() - stage_start, 1)
        stage_start = time.time()
        print(f"      探活通过: {len(nodes)}/{before_probe}")
        # 记录 probe 失败原因分布, 填补可观测性空白
        probe_error_counts: Dict[str, int] = {}
        for r in probe_results:
            if not r.success and r.error:
                key = r.error.split(":")[0] if ":" in r.error else r.error
                probe_error_counts[key] = probe_error_counts.get(key, 0) + 1
        probe_error_top = sorted(probe_error_counts.items(), key=lambda x: -x[1])[:10]
        if probe_error_top:
            print(f"      探活失败 Top: {', '.join(f'{k}={v}' for k, v in probe_error_top)}")
    nodes_after_probe = len(nodes)  # probe 后的节点数

    # 5) 真实代理测试（sing-box）
    valid: List[tuple] = []  # [(node, latency_ms, jitter_ms)]
    scored_valid: List[tuple] = []  # [(node, latency_ms, jitter_ms, score, source, breakdown)]
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

        # Load node stability for scoring boost
        stability_data = load_node_stability(args.output_dir)
        stable_fingerprints = set(get_stable_nodes(stability_data, min_consecutive=2)) if stability_data else set()

        scored_valid = []
        for r in results:
            if not r.success:
                continue

            fp = r.node.fingerprint()
            src_name = node_source_map.get(fp, "unknown")
            score_input = ScoreInput(
                latency_ms=r.latency_ms,
                jitter_ms=r.jitter_ms,
                tcp_latency_ms=tcp_latency.get(fp, 0),
                protocol=r.node.type,
                source=src_name,
                protocol_rates=protocol_rates,
                source_rates=source_rates,
                speed_kbps=getattr(r, "speed_kbps", 0),
                fingerprint_resistance=getattr(r, "fingerprint_resistance_score", 0.0),
            )
            score = calculate_score(score_input, scoring_config)
            breakdown = calculate_score_breakdown(score_input, scoring_config)

            # Stability bonus: 连续多轮通过的节点更值得信赖, 给予评分加成
            stability_bonus = 0.0
            if fp in stable_fingerprints:
                # 连续通过 2 轮 +2, 3 轮 +3, 上限 +5 (满分 100 内)
                stability_count = stability_data.get(fp, {}).get("consecutive_passes", 0) if stability_data else 0
                stability_bonus = min(5.0, float(stability_count))
                score = round(score + stability_bonus, 2)

            scored_valid.append((r.node, r.latency_ms, r.jitter_ms, score, src_name, breakdown, r, stability_bonus))

        scored_valid.sort(key=lambda x: (-x[3], x[1]))
        valid = [(n, lat, jit) for n, lat, jit, _, _, _, _, _ in scored_valid]
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

    # TCP 延迟只保留为"是否可达"信息, 不参与延迟排序. 真测 0 通过时降级.
    degraded_mode = False
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
        # 真测 0 成功: 降级到 TCP 模式, 避免用户订阅完全变空
        err_counter: Dict[str, int] = {}
        for r in results:
            if not r.success and r.error:
                key = r.error[:60]
                err_counter[key] = err_counter.get(key, 0) + 1
        top_errs = sorted(err_counter.items(), key=lambda x: -x[1])[:5]
        print(f"      ⚠️ 真测 0 通过 — 降级到 TCP 模式")
        for err, cnt in top_errs:
            print(f"        [{cnt}×] {err}")
        global _REAL_TEST_FAIL_REASONS
        _REAL_TEST_FAIL_REASONS = dict(err_counter)
        # 降级: 用 TCP 可达节点填充输出
        valid = sorted(
            [(n, tcp_latency.get(n.fingerprint(), 0), 0.0) for n in nodes],
            key=lambda x: x[1],
        )
        degraded_mode = True
        print(f"      降级输出 {len(valid)} 个 TCP 可达节点 (未经真测验证)")

    # 真实测试失败原因统计 — 让 stats.json 自带诊断
    from core.tester import build_error_detail
    real_test_errors: Dict[str, int] = {}
    real_test_error_details_counter: Dict[str, int] = {}
    real_test_error_structured_counter: Dict[tuple, Dict[str, object]] = {}
    for r in results if args.real_test else []:
        if r.success:
            continue
        error = r.error or "unknown"
        detail = r.error_detail or build_error_detail(error)
        target = str(detail.get("target", error.split(":", 1)[0]))
        reason = str(detail.get("reason", "unknown"))
        err_key = target
        real_test_errors[err_key] = real_test_errors.get(err_key, 0) + 1
        detail_key = error[:120]
        real_test_error_details_counter[detail_key] = real_test_error_details_counter.get(detail_key, 0) + 1
        struct_key = (target, reason, str(detail.get("status", detail.get("value", ""))))
        row = real_test_error_structured_counter.setdefault(struct_key, {
            "target": target,
            "reason": reason,
            "status": detail.get("status"),
            "value": detail.get("value"),
            "count": 0,
        })
        row["count"] = int(row["count"]) + 1
    real_test_error_details = [
        {"error": error, "count": count}
        for error, count in sorted(real_test_error_details_counter.items(), key=lambda x: -x[1])[:10]
    ]
    real_test_error_structured = sorted(
        real_test_error_structured_counter.values(),
        key=lambda row: -int(row.get("count", 0)),
    )[:20]

    # 取 Top N 并改名加入延迟。构造新 Node，避免污染 all.* 的原始去重池。
    # §2.1 tag 不再在 main.py 截断 30 字符, 留给 generator._clamp_tag 统一处理
    top = valid[:args.top_n]
    final_nodes = build_output_nodes(valid, flag_map, args.top_n)
    global_valid = sorted(valid + cn_block_retry_valid, key=lambda x: x[1])
    global_nodes = build_output_nodes(global_valid, flag_map, args.top_n)

    # 6) 生成输出
    print(f"[6/6] 生成订阅文件...")
    from core.generator import write_outputs, write_chunked_outputs, write_protocol_outputs

    output_guard: Dict[str, Dict[str, object]] = {}

    previous_verified = count_existing_urls(args.output_dir, "verified")
    proposed_verified = len([n for n in final_nodes if n])
    if should_preserve_previous_output(proposed_verified, previous_verified, args.min_retain_ratio):
        n_top = previous_verified
        output_guard["verified"] = {
            "preserved": True,
            "previous_count": previous_verified,
            "proposed_count": proposed_verified,
            "min_retain_ratio": args.min_retain_ratio,
        }
        print(f"      verified.* 保留上一轮: {previous_verified}（本轮 {proposed_verified} 低于阈值）")
    else:
        n_top = write_outputs(final_nodes, args.output_dir, prefix="verified", repo_path=args.repo, branch=args.branch)
        # P0: 分块输出 (verified)
        write_chunked_outputs(final_nodes, args.output_dir, prefix="verified",
                             repo_path=args.repo, branch=args.branch, chunk_size=100)
        # P1: 协议分文件输出 (verified)
        write_protocol_outputs(final_nodes, args.output_dir, prefix="verified",
                              repo_path=args.repo, branch=args.branch)
        output_guard["verified"] = {"preserved": False, "previous_count": previous_verified, "proposed_count": n_top}

    if args.global_output:
        previous_global = count_existing_urls(args.output_dir, "global")
        proposed_global = len([n for n in global_nodes if n])
        if should_preserve_previous_output(proposed_global, previous_global, args.min_retain_ratio):
            n_global = previous_global
            output_guard["global"] = {
                "preserved": True,
                "previous_count": previous_global,
                "proposed_count": proposed_global,
                "min_retain_ratio": args.min_retain_ratio,
            }
            print(f"      global.* 保留上一轮: {previous_global}（本轮 {proposed_global} 低于阈值）")
        else:
            n_global = write_outputs(global_nodes, args.output_dir, prefix="global", repo_path=args.repo, branch=args.branch)
            # P0: 分块输出 (global)
            write_chunked_outputs(global_nodes, args.output_dir, prefix="global",
                                 repo_path=args.repo, branch=args.branch, chunk_size=100)
            # P1: 协议分文件输出 (global)
            write_protocol_outputs(global_nodes, args.output_dir, prefix="global",
                                  repo_path=args.repo, branch=args.branch)
            output_guard["global"] = {"preserved": False, "previous_count": previous_global, "proposed_count": n_global}
    else:
        n_global = 0
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
    source_scores = build_source_scores(source_nodes, src_pass, source_dead_counts)

    stats = {
        "version": __version__,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "duration_sec": round(elapsed, 1),
        "degraded_mode": degraded_mode,
        "stage_durations": stage_durations,
        "sources_total": len(sources),
        "sources_healthy": healthy,
        "nodes_raw": total_raw,
        "nodes_dedup": len(set(nd.fingerprint() for nd in all_nodes)),
        "nodes_tcp_ok": nodes_before_probe,
        "nodes_tcp_reachable": nodes_tcp_reachable if args.tcp_check else len(nodes),
        "nodes_probe_ok": nodes_after_probe,
        "nodes_real_ok": len(valid),
        "probe_error_details": probe_error_top if (args.lightweight_probe and args.real_test) else [],
        "nodes_verified_output": n_top,
        "nodes_global_output": n_global,
        "output_guard": output_guard,
        "nodes_global_extra_from_cn_block": len(cn_block_retry_valid),
        "global_skip_target_kinds": ["cn-block"] if args.global_output else [],
        "nodes_all_output": n_all,
        "all_output_mode": args.all_output_mode,
        "protocol_dist": proto_count,
        "filter_rule_hits": filter_rule_hits,
        "protocol_pass_rate": proto_pass,
        "source_pass_rate": src_pass,
        "source_nodes": source_nodes,
        "source_scores": source_scores,
        "tcp_errors": tcp_errors,
        "real_test_errors": real_test_errors,
        "real_test_error_details": real_test_error_details,
        "real_test_error_structured": real_test_error_structured,
        "top_latencies_ms": [round(lat, 1) for _, lat, _ in top if lat > 0][:20],
        "top_jitters_ms": [round(jit, 1) for _, _, jit in top if jit > 0][:20],
        "scoring": {
            "weights": scoring_config.weights,
            "excellent_latency_ms": scoring_config.excellent_latency_ms,
            "bad_latency_ms": scoring_config.bad_latency_ms,
            "bad_jitter_ms": scoring_config.bad_jitter_ms,
            "excellent_tcp_latency_ms": scoring_config.excellent_tcp_latency_ms,
            "bad_tcp_latency_ms": scoring_config.bad_tcp_latency_ms,
            "missing_tcp_score": scoring_config.missing_tcp_score,
            "missing_history_score": scoring_config.missing_history_score,
        },
        "top_scores": [
            {
                "tag": n.tag,
                "server": n.server,
                "type": n.type,
                "source": source,
                "latency_ms": round(lat, 1),
                "jitter_ms": round(jit, 1),
                "score": score,
                "score_breakdown": breakdown,
                "stability_bonus": stability_bonus,
                "speed_kbps": getattr(r, "speed_kbps", 0) if r else 0,
                "fingerprint_resistance": getattr(r, "fingerprint_resistance", "") if r else "",
                "netflix": getattr(r, "netflix_ok", False) if r else False,
                "chatgpt": getattr(r, "chatgpt_ok", False) if r else False,
                "stability_bonus": stability_bonus,
            }
            for n, lat, jit, score, source, breakdown, r, stability_bonus in scored_valid[:20]
        ],
    }
    os.makedirs(args.output_dir, exist_ok=True)
    with open(f"{args.output_dir}/stats.json", "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)
    update_trend_history(args.output_dir, stats)

    # Node stability tracking
    if args.real_test and results:
        passed_fps = [r.node.fingerprint() for r in results if r.success]
        failed_fps = [r.node.fingerprint() for r in results if not r.success]
        stability = update_node_stability(args.output_dir, passed_fps, failed_fps,
                                          stats.get("timestamp", ""))
        stats["node_stability_count"] = stability.get("total_tracked", 0) if isinstance(stability, dict) else 0
        # Re-write stats with stability count
        with open(f"{args.output_dir}/stats.json", "w", encoding="utf-8") as f:
            json.dump(stats, f, ensure_ascii=False, indent=2)
    report_path = write_health_report(args.output_dir, stats)
    print(f"      健康报告: {report_path}")
    if update_readme_stats("README.md", stats):
        print("      README 状态区已更新")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--sources", default="config/sources.yaml")
    p.add_argument("--output-dir", default="output")
    p.add_argument("--singbox", default="./sing-box")
    p.add_argument("--top-n", type=int, default=100, help="最终输出的节点数")

    p.add_argument("--fetch-concurrency", type=int, default=30)
    p.add_argument("--fetch-timeout", type=int, default=15)
    p.add_argument("--fetch-overall-timeout", type=int, default=120,
                   help="整批订阅抓取总超时秒数，超时后返回已完成源的部分结果")

    p.add_argument("--tcp-check", action=argparse.BooleanOptionalAction, default=True)
    p.add_argument("--tcp-concurrency", type=int, default=500)
    p.add_argument("--tcp-timeout", type=float, default=3.0)

    p.add_argument("--real-test", action=argparse.BooleanOptionalAction, default=True)
    p.add_argument("--test-concurrency", type=int, default=50)
    p.add_argument("--lightweight-probe", action=argparse.BooleanOptionalAction, default=True)
    p.add_argument("--probe-concurrency", type=int, default=100)
    p.add_argument("--probe-timeout", type=float, default=4.0)
    p.add_argument("--probe-startup-wait", type=float, default=0.4)
    p.add_argument("--test-timeout", type=float, default=6.0)
    p.add_argument("--startup-wait", type=float, default=0.6)
    p.add_argument("--test-limit", type=int, default=3000, help="送入真实测试的最大节点数(0=不限)")
    p.add_argument("--quality-filter", action=argparse.BooleanOptionalAction, default=True,
                   help="启用质量预过滤（配置规则 + 同 server/type 降噪）")
    p.add_argument("--filter-rules", default="config/filter_rules.yaml",
                   help="质量过滤规则配置文件；不存在时使用保守默认规则")
    p.add_argument("--scoring-rules", default="config/scoring.yaml",
                   help="节点评分权重配置文件；不存在时使用内置默认权重")
    p.add_argument("--max-per-server", type=int, default=0,
                   help="§2.2 同 server IP 最多保留的节点数 (0=不限, 默认; 1/2=严格, 但可能误杀 AWS/Hetzner 上不同用户的节点)")
    p.add_argument("--min-latency", type=float, default=30.0,
                   help="真实测试最低延迟阈值(ms)，低于此值视为可疑；设为 0 可关闭")
    p.add_argument("--global-output", action=argparse.BooleanOptionalAction, default=True,
                   help="额外生成 global.*：严格 verified + 仅跳过 cn-block 复测通过的节点")
    p.add_argument("--min-retain-ratio", type=float, default=0.7,
                   help="verified/global 本轮数量低于上一轮该比例时保留上一轮输出；设为 0 可关闭")
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
    if args.fetch_overall_timeout <= 0:
        p.error("--fetch-overall-timeout 必须 > 0")
    if args.tcp_concurrency <= 0:
        p.error("--tcp-concurrency 必须 > 0")
    if args.test_concurrency <= 0:
        p.error("--test-concurrency 必须 > 0")
    if args.test_limit < 0:
        p.error("--test-limit 必须 >= 0")
    if args.min_latency < 0:
        p.error("--min-latency 必须 >= 0")
    if args.min_retain_ratio < 0:
        p.error("--min-retain-ratio 必须 >= 0")

    # 环境变量覆盖（CI 或容器场景常用）
    if os.environ.get("AUTONODES_TOP_N"):
        args.top_n = int(os.environ["AUTONODES_TOP_N"])
    if os.environ.get("AUTONODES_TEST_LIMIT"):
        args.test_limit = int(os.environ["AUTONODES_TEST_LIMIT"])
    asyncio.run(run(args))


if __name__ == "__main__":
    main()
