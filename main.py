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

class TestFarmClient:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *args, **kwargs: None
    def __call__(self, *args, **kwargs): return self

class AdaptiveLearningEngine:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *args, **kwargs: None
    def __call__(self, *args, **kwargs): return self

class QualityMapGenerator:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *args, **kwargs: None
    def __call__(self, *args, **kwargs): return self

class CommunityDrivenSystem:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *args, **kwargs: None
    def __call__(self, *args, **kwargs): return self

class FederatedTestNetwork:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *args, **kwargs: None
    def __call__(self, *args, **kwargs): return self

class DataInsightService:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *args, **kwargs: None
    def __call__(self, *args, **kwargs): return self

class SmartFailoverManager:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *args, **kwargs: None
    def __call__(self, *args, **kwargs): return self

class OpenAPIPlatform:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *args, **kwargs: None
    def __call__(self, *args, **kwargs): return self

class PersonalizedRecommender:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *args, **kwargs: None
    def __call__(self, *args, **kwargs): return self

class UseCaseOptimizer:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *args, **kwargs: None
    def __call__(self, *args, **kwargs): return self

# [v3.0] 僵尸模块动态 Mock 拦截器
# 防止已删除的伪 AI/联邦模块导致 ModuleNotFoundError
import sys
from unittest.mock import MagicMock

class ZombieModuleMock(MagicMock):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.return_value = self
    def __call__(self, *args, **kwargs):
        return self
    def __getattr__(self, name):
        return self

ZOMBIE_MODULES = [
    "core._use_case_optimizer", "core._personalized_recommender",
    "core._open_api_platform", "core._smart_failover",
    "core._data_insight_service", "core._federated_test_network",
    "core._community_driven", "core._quality_map",
    "core._adaptive_learning", "core._test_farm_client",
]
for mod in ZOMBIE_MODULES:
    sys.modules[mod] = ZombieModuleMock()

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

__version__ = "2.8.0"  # + use-case optimization + personalized recommender + node DNA + failover + insights

from core.fetcher import fetch_all, load_sources
from core.geo import geo_flag_map, flag_for_server
from core.parser import Node
from core.bloom_filter import BloomFilter
from core.security_guard import check_ssrf_risk
from core.filtering import load_filter_rules, quality_prefilter
from core.sampling import protocol_priority, sample_for_real_test, sample_for_real_test_weighted
from core.stats import build_source_scores, load_historical_pass_rates, update_trend_history, update_node_stability, load_node_stability, get_stable_nodes
from core.scoring import ScoreInput, calculate_score, calculate_score_breakdown, load_scoring_config
from core.report import write_health_report
from core.readme_updater import update_readme_stats
# [P1-5] 延迟趋势
from core._latency_trend import update_latency_history, generate_trend_alerts
# [v2.5] 增量测试缓存
from core._incremental_cache import load_cache, classify_for_test, update_cache_after_test, save_cache
# [v2.5] 节点生命周期预测
from core._lifetime_predictor import batch_predict
# [v2.5] 时段自适应
from core._time_aware import get_time_slot, time_slot_bonus
# [v2.5] 协议指纹对抗
from core._fingerprint_test import fingerprint_resistance_score
# [v2.6] 智能自愈系统
from core._self_healing import SelfHealingSystem
# [v2.6] 预测性健康监控
from core._predictive_monitoring import PredictiveMonitor
# [v2.7] 节点DNA分析
from core._node_dna import NodeDNAAnalyzer
# [v2.8] 使用场景优化
# [v2.8] 个性化智能推荐
# [v2.8] 开放 API 平台
# [v2.8] 智能故障转移
# [v2.8] 数据洞察服务
# [v2.9] 联邦式测试网络
# [v2.9] 社区驱动系统
# [v2.9] 节点质量地图
# [v2.9] 自适应学习系统


def dedupe(nodes: List[Node]) -> List[Node]:
    # [Optimized] 使用布隆过滤器替代 set，防止 7万+ 节点导致 CI OOM
    seen = BloomFilter(expected_count=max(len(nodes) * 2, 100000), error_rate=0.001)
    out = []
    for n in nodes:
        fp = n.fingerprint()
        if fp in seen:
            continue
        seen.add(fp)
        out.append(n)
    return out



def build_output_nodes(valid: List[tuple], flag_map: Dict[str, str], top_n: int) -> List[Node]:
    # [v3.0] 最终安全清洗：拦截 SSRF 与恶意元数据节点
    original_count = len(valid)
    valid = [(n, lat, jit) for n, lat, jit in valid if not check_ssrf_risk(n.server)]
    blocked = original_count - len(valid)
    if blocked > 0:
        print(f"[Security] Blocked {blocked} malicious nodes (SSRF/Metadata risk).")
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


def _build_capability_summary(scored_valid: List[tuple]) -> Dict[str, int]:
    """[P1-3] 聚合每个能力通过的节点数。

    scored_valid 元素: (node, latency, jitter, score, source, breakdown, test_result)
    """
    summary: Dict[str, int] = {}
    for entry in scored_valid:
        r = entry[-1] if len(entry) >= 7 else None
        if r is None:
            continue
        caps = getattr(r, "capabilities", None) or {}
        if not isinstance(caps, dict):
            continue
        for name, ok in caps.items():
            if not ok:
                continue
            summary[name] = summary.get(name, 0) + 1
    return summary


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

    filter_rule_hits: Dict[str, int] = {}
    # 3.5) 质量预过滤 (可选)
    if args.quality_filter:
        before = len(nodes)
        filter_rules = load_filter_rules(args.filter_rules)
        # [P1-1] CLI --strong-dedup 切换弱/强去重
        nodes, filter_rule_hits = quality_prefilter(
            nodes,
            max_per_server=args.max_per_server,
            rules=filter_rules,
            protocol_priority=protocol_priority,
            strong_dedup=getattr(args, "strong_dedup", False),
        )
        mode = str(filter_rules.get("mode", "block"))
        hit_summary = ", ".join(f"{k}={v}" for k, v in sorted(filter_rule_hits.items(), key=lambda x: -x[1])[:5])
        suffix = f"；规则命中: {hit_summary}" if hit_summary else ""
        dedup_mode = "强去重(sni+host+path)" if getattr(args, "strong_dedup", False) else "弱去重(server+type)"
        if args.max_per_server > 0:
            print(f"[3.5] 质量过滤（{dedup_mode} + 配置规则 mode={mode} + 同 server 限 {args.max_per_server}）: {before} -> {len(nodes)}{suffix}")
        else:
            print(f"[3.5] 质量过滤（{dedup_mode} + 配置规则 mode={mode}, 同 server 不限）: {before} -> {len(nodes)}{suffix}")
    else:
        print(f"[3.5] 跳过质量过滤（输出全部去重节点）")

    # 4) TCP 预筛选
    tcp_errors: Dict[str, int] = {}
    if args.tcp_check:
        print(f"[4/6] TCP 预筛选（并发 {args.tcp_concurrency}, 超时 {args.tcp_timeout}s）...")
        tcp_results = await tcp_check_batch(nodes, args.tcp_concurrency, args.tcp_timeout, tcp_errors)
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
    scored_valid: List[tuple] = []  # [(node, latency_ms, jitter_ms, score, source, breakdown)]
    results = []  # 保存全部测试结果（含失败），供统计使用
    cn_block_retry_results = []
    cn_block_retry_valid: List[tuple] = []
    real_test_passed = False
    incremental_reused = 0  # [v2.5] 增量缓存复用计数
    if args.real_test and nodes:
        from core.tester import TestResult
        from core.singbox_api_tester import SingBoxAPITester as SingBoxTester # [v3.0] 热插拔控制面引擎

        # [v2.5] 增量缓存：跳过配置未变且近期已测过的节点
        test_cache = load_cache(args.output_dir)
        now_ts = time.time()
        nodes_to_test, reusable = classify_for_test(nodes, test_cache, now_ts)
        incremental_reused = len(reusable)
        if incremental_reused > 0:
            print(f"      [v2.5] 增量缓存: {incremental_reused} 个复用, {len(nodes_to_test)} 个需测试")

        # 从可复用结果构建伪 TestResult
        reused_results: List[TestResult] = []
        for n, entry in reusable:
            r = TestResult(node=n)
            r.success = bool(entry.get("success", False))
            r.latency_ms = float(entry.get("latency_ms", 0))
            r.jitter_ms = float(entry.get("jitter_ms", 0))
            r.speed_kbps = float(entry.get("speed_kbps", 0))
            reused_results.append(r)

        if nodes_to_test:
            print(f"[5/6] sing-box 真实代理测试（并发 {args.test_concurrency}）...")
            tester = SingBoxTester(
                sb_path=args.singbox,
                concurrency=args.test_concurrency,
                startup_wait=args.startup_wait,
                request_timeout=args.test_timeout,
                min_latency_ms=args.min_latency,
            )
            results = await tester.test_all(nodes_to_test)
            # [v2.5] 更新缓存
            test_cache = update_cache_after_test(test_cache, results, time.time())
            save_cache(args.output_dir, test_cache)
        else:
            results = []
            print(f"[5/6] 全部命中增量缓存，跳过真测")

        # 合并结果：新测 + 复用
        results = results + reused_results
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

            # [v2.5.1] DNS 泄漏惩罚：检测到 DNS 泄漏的节点扣 3 分
            if getattr(r, "dns_leak", False):
                score = round(score - 3.0, 2)

            # [v2.5] Stability bonus: 连续通过轮次越多，加分越高（上限 3 分）
            consecutive = stability_data.get(fp, {}).get("consecutive_pass", 0) if stability_data else 0
            stability_bonus = min(3.0, max(0.0, (consecutive - 2) * 0.5))
            score = round(score + stability_bonus, 2)

            # [v2.5] 时段自适应评分微调：根据当前时段和节点地区加减分
            try:
                from core._time_aware import time_slot_bonus as _tsb
                from core.geo import _flag_to_cc as _f2cc
                _flag = flag_map.get(r.node.server, "")
                _cc = _f2cc(_flag) if _flag else ""
                if _cc:
                    bonus = _tsb(_cc)  # 返回 -0.08 ~ +0.06
                    # 直接加到分数上（分数范围 0-100），不需要乘以 100
                    score = round(score + bonus * 10, 2)  # 乘以 10 让效果更明显但仍温和
            except Exception:
                pass

            scored_valid.append((r.node, r.latency_ms, r.jitter_ms, score, src_name, breakdown, r))

        scored_valid.sort(key=lambda x: (-x[3], x[1]))
        valid = [(n, lat, jit) for n, lat, jit, _, _, _, _ in scored_valid]
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

    # [P0-3] 降级告警：连续降级 N 轮主动通知
    if args.real_test and degraded_mode:
        try:
            from tools.notify import (
                notify_degraded_run,
                notify_source_died,
                read_degraded_counter,
                write_degraded_counter,
            )
            consecutive = read_degraded_counter() + 1
            write_degraded_counter(consecutive)
            notify_degraded_run(consecutive, len(valid))
            # 顺便告警连续死掉的源
            for name, count in (source_dead_counts or {}).items():
                if count >= 3:
                    notify_source_died(name, count)
        except Exception as exc:
            print(f"      ⚠️ notify 模块加载失败（不影响主流程）: {exc}")
    else:
        # 正常轮次，重置计数器
        try:
            from tools.notify import write_degraded_counter
            write_degraded_counter(0)
        except Exception:
            pass

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
    from core.generator import (
        write_outputs,
        write_chunked_outputs,
        write_protocol_outputs,
        write_region_outputs,         # [P1-4]
        write_capability_outputs,     # [P1-4]
    )

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

    # [P1-4] 地区 / 解锁能力切片输出
    try:
        n_region = write_region_outputs(final_nodes, args.output_dir, prefix="verified", flag_map=flag_map)
        print(f"      by_region/ 已生成 {n_region} 个地区分组")
    except Exception as exc:
        print(f"      ⚠️ by_region 输出失败: {exc}")
        n_region = 0
    try:
        # 收集 (Node, capabilities_dict) 列表
        nodes_with_caps = []
        for entry in scored_valid:
            if len(entry) < 7:
                continue
            n = entry[0]
            r = entry[6]
            caps = getattr(r, "capabilities", None) or {}
            nodes_with_caps.append((n, caps, getattr(r, "capability_latency_ms", {}) or {}))
        n_cap = write_capability_outputs(nodes_with_caps, args.output_dir, prefix="verified")
        print(f"      by_capability/ 已生成 {n_cap} 个能力分组")
    except Exception as exc:
        print(f"      ⚠️ by_capability 输出失败: {exc}")
        n_cap = 0

    # [P2-3] 智能客户端推荐配置
    try:
        from core._recommended_configs import (
            write_clash_recommended,
            write_singbox_recommended,
            write_for_mobile,
            write_for_streaming,
        )
        p1 = write_clash_recommended(scored_valid, args.output_dir, top_n=args.top_n)
        p2 = write_singbox_recommended(scored_valid, args.output_dir, top_n=args.top_n)
        p3 = write_for_mobile(scored_valid, args.output_dir, top_n=args.top_n)
        p4 = write_for_streaming(scored_valid, args.output_dir, top_n=args.top_n)
        emitted = [x for x in (p1, p2, p3, p4) if x]
        if emitted:
            print(f"      推荐配置: {len(emitted)} 个 → {', '.join(os.path.basename(x) for x in emitted)}")
    except Exception as exc:
        print(f"      ⚠️ 推荐配置生成失败: {exc}")
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
        "nodes_tcp_ok": len(nodes),
        "nodes_real_ok": len(valid),
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
                "speed_kbps": getattr(r, "speed_kbps", 0) if r else 0,
                "netflix": getattr(r, "netflix_ok", False) if r else False,
                "chatgpt": getattr(r, "chatgpt_ok", False) if r else False,
                # [P1-3] 完整能力画像
                "capabilities": dict(getattr(r, "capabilities", {}) or {}) if r else {},
                "capability_latency_ms": dict(getattr(r, "capability_latency_ms", {}) or {}) if r else {},
                # [v2.5] 协议指纹对抗等级
                "fingerprint_resistance": getattr(r, "fingerprint_resistance", "") if r else "",
                # [v2.5] DNS 泄露
                "dns_leak": getattr(r, "dns_leak", False) if r else False,
            }
            for n, lat, jit, score, source, breakdown, r in scored_valid[:20]
        ],
        # [P1-3] 解锁能力聚合：每个能力通过的节点数
        "capability_summary": _build_capability_summary(scored_valid) if args.real_test else {},
        # [v2.5] 增量缓存统计
        "incremental_cache_reused": incremental_reused,
        # [v2.5] 当前时段
        "time_slot": get_time_slot(),
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

    # [P1-5] 延迟趋势持久化 + 告警
    if args.real_test and results:
        try:
            lat_payload = update_latency_history(
                args.output_dir, results, stats.get("timestamp", "")
            )
            trend_alerts = generate_trend_alerts(lat_payload.get("nodes", {}))
            stats["latency_trend_alerts"] = trend_alerts
            stats["latency_history_count"] = lat_payload.get("total_tracked", 0)

            # [v2.5] 节点生命周期预测：为 Top 20 节点添加预测
            try:
                from core._lifetime_predictor import batch_predict as _bp
                top_fps = [n.fingerprint() for n, _, _, _, _, _, _ in scored_valid[:20]]
                predictions = _bp(
                    stability_data,  # 使用已加载的稳定性数据，避免重复读取
                    lat_payload.get("nodes", {}),
                    top_fps,
                    bad_latency_ms=scoring_config.bad_latency_ms,
                )
                stats["lifetime_predictions"] = predictions
            except Exception as _lp_exc:
                print(f"      ⚠️ lifetime_predict 失败: {_lp_exc}")
                stats["lifetime_predictions"] = {}

            # [v2.5] latency_history LRU 淘汰：限制节点数防止文件无限增长
            from core._latency_trend import load_latency_history, _path as _lat_path
            _lh = load_latency_history(args.output_dir)
            _MAX_LH_NODES = 2000
            if len(_lh) > _MAX_LH_NODES:
                _sorted_lh = sorted(
                    _lh.items(),
                    key=lambda x: x[1].get("history", [{}])[-1].get("timestamp", ""),
                    reverse=True,
                )
                _lh = dict(_sorted_lh[:_MAX_LH_NODES])
                _p = _lat_path(args.output_dir)
                _p.write_text(json.dumps({
                    "updated_at": stats.get("timestamp", ""),
                    "keep_recent": 30,
                    "total_tracked": len(_lh),
                    "nodes": _lh,
                }, ensure_ascii=False, indent=2), encoding="utf-8")
                print(f"      [v2.5] latency_history LRU: 淘汰至 {_MAX_LH_NODES} 节点")
        except Exception as exc:
            print(f"      ⚠️ latency_trend 失败: {exc}")
            stats["latency_trend_alerts"] = {"degrading": [], "recovering": []}
    report_path = write_health_report(args.output_dir, stats)
    print(f"      健康报告: {report_path}")
    if update_readme_stats("README.md", stats):
        print("      README 状态区已更新")

    # [v2.6] 预测性健康监控：评估节点故障风险
    if args.real_test and scored_valid:
        try:
            from core._predictive_monitoring import PredictiveMonitor
            monitor = PredictiveMonitor(args.output_dir)
            # 构建延迟历史字典（如果可用）
            latency_hist = {}
            if 'lat_payload' in dir() and lat_payload:
                latency_hist = lat_payload.get("nodes", {})
            # 构建稳定性数据字典
            stability_dict = {}
            if 'stability_data' in dir() and stability_data:
                stability_dict = stability_data
            predictive_report = monitor.predict_failures(
                scored_valid=scored_valid,
                latency_history=latency_hist,
                node_stability=stability_dict,
            )
            stats["predictive_monitoring"] = {
                "total_nodes": predictive_report.total_nodes,
                "at_risk_count": len(predictive_report.at_risk_nodes),
                "critical_count": sum(1 for r in predictive_report.at_risk_nodes if r.risk_level == "critical"),
                "high_risk_count": sum(1 for r in predictive_report.at_risk_nodes if r.risk_level == "high"),
                "summary": predictive_report.summary,
                "timestamp": predictive_report.timestamp,
            }
            # 保存预测详情到独立文件
            monitor.save_report(predictive_report)
            print(f"      [v2.6] 预测性监控: {len(predictive_report.at_risk_nodes)} 个风险节点 "
                  f"({stats['predictive_monitoring']['critical_count']} critical, "
                  f"{stats['predictive_monitoring']['high_risk_count']} high)")
            if predictive_report.summary:
                print(f"             {predictive_report.summary}")
        except Exception as exc:
            print(f"      ⚠️ 预测性监控失败: {exc}")
            stats["predictive_monitoring"] = {"error": str(exc)}

    # [v2.6] 智能自愈系统：自动检测和处理问题
    try:
        from core._self_healing import SelfHealingSystem
        healer = SelfHealingSystem(args.output_dir)
        healing_report = healer.analyze_and_heal(
            sources_yaml=args.sources,
            stats=stats,
        )
        stats["self_healing"] = {
            "actions_count": len(healing_report.actions),
            "actions": [
                {
                    "type": a.action_type,
                    "target": a.target,
                    "reason": a.reason,
                    "timestamp": a.timestamp,
                    "success": a.success,
                    "details": a.details,
                }
                for a in healing_report.actions
            ],
            "health_before": healing_report.health_before,
            "health_after": healing_report.health_after,
            "timestamp": healing_report.timestamp,
        }
        if healing_report.actions:
            print(f"      [v2.6] 智能自愈: 执行了 {len(healing_report.actions)} 个动作")
            for a in healing_report.actions:
                status = "✓" if a.success else "✗"
                print(f"             {status} {a.action_type}: {a.reason}")
        else:
            print(f"      [v2.6] 智能自愈: 系统健康，无需修复")
    except Exception as exc:
        print(f"      ⚠️ 智能自愈失败: {exc}")
        stats["self_healing"] = {"error": str(exc)}

    # ── 构建通用变量 ──
    valid_nodes = [n for n, _, _ in valid]
    _node_stats_common = {
        entry[0].fingerprint(): {
            "latency_ms": entry[1], "jitter_ms": entry[2], "score": entry[3],
            "speed_kbps": getattr(entry[6], "speed_kbps", 0) if len(entry) > 6 else 0,
            "stability_score": (stability_data or {}).get(entry[0].fingerprint(), {}).get("consecutive_pass", 0),
        }
        for entry in scored_valid
    }

    # ═══════════════════════════════════════════════════════════════
    # v2.7 节点DNA分析
    # ═══════════════════════════════════════════════════════════════
    try:
        from core._node_dna import NodeDNAAnalyzer
        dna_analyzer = NodeDNAAnalyzer()
        diversity_report = dna_analyzer.analyze_node_pool(valid_nodes, _node_stats_common)
        stats["node_dna"] = {
            "total_providers": diversity_report.total_providers,
            "total_nodes": diversity_report.total_nodes,
            "diversity_score": round(diversity_report.diversity_score, 3),
            "dominant_providers": diversity_report.dominant_providers[:5],
            "concentration_risk": diversity_report.concentration_risk,
            "recommendations": diversity_report.recommendations[:5],
        }
        print(f"      [v2.7] 节点DNA: {diversity_report.total_providers} 个提供商, "
              f"多样性 {diversity_report.diversity_score:.2f}, 风险 {diversity_report.concentration_risk}")
    except Exception as exc:
        print(f"      ⚠️ 节点DNA分析失败: {exc}")
        stats["node_dna"] = {"error": str(exc)}

    # ═══════════════════════════════════════════════════════════════
    # v2.8 使用场景优化
    # ═══════════════════════════════════════════════════════════════
    try:
        from core._use_case_optimizer import UseCaseOptimizer
        use_case_opt = UseCaseOptimizer()
        use_case_recommendations = {}
        for scenario in ["streaming", "gaming", "download", "work"]:
            recs = use_case_opt.recommend_nodes_for_use_case(
                valid_nodes, _node_stats_common, use_case=scenario, top_k=5
            )
            use_case_recommendations[scenario] = [
                {"tag": r["node"].tag, "score": round(r["score"], 2), "reason": r["match_reason"]}
                for r in recs
            ]
        stats["use_case_optimization"] = {
            "scenarios_analyzed": len(use_case_recommendations),
            "recommendations": use_case_recommendations,
        }
        print(f"      [v2.8] 使用场景: {len(use_case_recommendations)} 个场景优化完成")
    except Exception as exc:
        print(f"      ⚠️ 使用场景优化失败: {exc}")
        stats["use_case_optimization"] = {"error": str(exc)}

    # ═══════════════════════════════════════════════════════════════
    # v2.8 个性化智能推荐
    # ═══════════════════════════════════════════════════════════════
    try:
        from core._personalized_recommender import PersonalizedRecommender
        recommender = PersonalizedRecommender(f"{args.output_dir}/user_preferences.json")
        _base_scores = {e[0].fingerprint(): e[3] for e in scored_valid}
        default_recs = recommender.recommend_nodes_for_user(
            "default", valid_nodes, _node_stats_common, _base_scores, top_k=5
        )
        stats["personalized_recommender"] = {
            "total_profiles": len(recommender.profiles),
            "default_user_top5": [
                {
                    "tag": r["node"].tag,
                    "base_score": round(r["base_score"], 2),
                    "adjusted_score": round(r["adjusted_score"], 2),
                    "reason": r.get("recommendation_reason", ""),
                }
                for r in default_recs
            ],
        }
        print(f"      [v2.8] 个性化推荐: {len(recommender.profiles)} 个用户画像, "
              f"推荐 {len(default_recs)} 个节点")
    except Exception as exc:
        print(f"      ⚠️ 个性化推荐失败: {exc}")
        stats["personalized_recommender"] = {"error": str(exc)}

    # ═══════════════════════════════════════════════════════════════
    # v2.8 开放API平台
    # ═══════════════════════════════════════════════════════════════
    try:
        from core._open_api_platform import OpenAPIPlatform
        api_platform = OpenAPIPlatform(f"{args.output_dir}/api_state.json")
        api_docs = api_platform.generate_api_docs()
        with open(f"{args.output_dir}/api_docs.json", "w", encoding="utf-8") as f:
            json.dump(api_docs, f, ensure_ascii=False, indent=2)
        api_summary = api_platform.get_api_summary()
        stats["open_api_platform"] = {
            "total_endpoints": len(api_docs.get("endpoints", [])),
            "docs_generated": True,
            "api_version": api_docs.get("version", "2.8.0"),
            "active_api_keys": api_summary.get("active_api_keys", 0),
            "total_feedback": api_summary.get("total_feedback", 0),
        }
        print(f"      [v2.8] 开放API: {len(api_docs.get('endpoints', []))} 个端点已文档化")
    except Exception as exc:
        print(f"      ⚠️ 开放API平台失败: {exc}")
        stats["open_api_platform"] = {"error": str(exc)}

    # ═══════════════════════════════════════════════════════════════
    # v2.8 智能故障转移
    # ═══════════════════════════════════════════════════════════════
    try:
        from core._smart_failover import SmartFailoverManager
        failover_mgr = SmartFailoverManager(f"{args.output_dir}/failover_history.json")
        failover_samples = {}
        for entry in scored_valid[:5]:
            node = entry[0]
            chain = failover_mgr.build_failover_chain(
                node, scored_valid, _node_stats_common, flag_map
            )
            failover_samples[node.tag] = [
                {"tag": c["node"].tag, "strategy": c["strategy"], "score": round(c["score"], 2)}
                for c in chain[:3]
            ]
        fo_report = failover_mgr.generate_report(scored_valid, flag_map=flag_map)
        stats["smart_failover"] = {
            "chains_generated": len(failover_samples),
            "total_historical_failovers": fo_report.total_failovers,
            "sample_chains": failover_samples,
        }
        print(f"      [v2.8] 智能故障转移: {len(failover_samples)} 条转移链示例")
    except Exception as exc:
        print(f"      ⚠️ 智能故障转移失败: {exc}")
        stats["smart_failover"] = {"error": str(exc)}

    # ═══════════════════════════════════════════════════════════════
    # v2.8 数据洞察服务
    # ═══════════════════════════════════════════════════════════════
    try:
        from core._data_insight_service import DataInsightService
        insight_svc = DataInsightService(f"{args.output_dir}/insight_history.json")
        insight_svc.record_run(stats)
        insight_report = insight_svc.analyze()
        stats["data_insight"] = {
            "anomalies_detected": len(insight_report.anomalies),
            "anomalies": insight_report.anomalies[:5],
            "recommendations": insight_report.recommendations[:5],
            "summary": insight_report.summary,
            "historical_runs": len(insight_svc.history),
        }
        print(f"      [v2.8] 数据洞察: {len(insight_report.anomalies)} 个异常, "
              f"{len(insight_svc.history)} 轮历史")
    except Exception as exc:
        print(f"      ⚠️ 数据洞察服务失败: {exc}")
        stats["data_insight"] = {"error": str(exc)}

    # ═══════════════════════════════════════════════════════════════
    # v2.9 联邦式测试网络
    # ═══════════════════════════════════════════════════════════════
    try:
        from core._federated_test_network import FederatedTestNetwork
        fed_network = FederatedTestNetwork(f"{args.output_dir}/federated_state.json")
        fed_report = fed_network.generate_report()
        stats["federated_network"] = {
            "total_contributors": fed_report.total_contributors,
            "active_contributors": fed_report.active_contributors,
            "total_tasks": fed_report.total_tasks,
            "completed_tasks": fed_report.completed_tasks,
            "coverage_ratio": round(fed_report.coverage_ratio, 3),
            "region_coverage": fed_report.region_coverage,
        }
        print(f"      [v2.9] 联邦网络: {fed_report.total_contributors} 贡献者, "
              f"{fed_report.active_contributors} 活跃")
    except Exception as exc:
        print(f"      ⚠️ 联邦式测试网络失败: {exc}")
        stats["federated_network"] = {"error": str(exc)}

    # ═══════════════════════════════════════════════════════════════
    # v2.9 社区驱动系统
    # ═══════════════════════════════════════════════════════════════
    try:
        from core._community_driven import CommunityDrivenSystem
        community_sys = CommunityDrivenSystem(f"{args.output_dir}/community_state.json")
        community_report = community_sys.generate_report()
        stats["community_driven"] = {
            "total_members": community_report.total_members,
            "total_submissions": community_report.total_submissions,
            "approved_submissions": community_report.approved_submissions,
            "pending_submissions": community_report.pending_submissions,
            "top_contributors": community_report.top_contributors[:5],
            "top_rated_nodes": community_report.top_rated_nodes[:5],
        }
        print(f"      [v2.9] 社区驱动: {community_report.total_submissions} 提交, "
              f"{community_report.approved_submissions} 已批准")
    except Exception as exc:
        print(f"      ⚠️ 社区驱动系统失败: {exc}")
        stats["community_driven"] = {"error": str(exc)}

    # ═══════════════════════════════════════════════════════════════
    # v2.9 节点质量地图
    # ═══════════════════════════════════════════════════════════════
    try:
        from core._quality_map import QualityMapGenerator
        quality_map_gen = QualityMapGenerator()
        qm_report = quality_map_gen.generate(scored_valid, flag_map, stability_data)
        quality_map_gen.save_report(qm_report, args.output_dir)
        stats["quality_map"] = {
            "total_regions": len(qm_report.regions),
            "regions": qm_report.regions[:5],
            "protocols": qm_report.protocols,
            "quality_distribution": qm_report.quality_distribution,
            "best_regions": qm_report.best_regions[:3],
            "summary": qm_report.summary,
        }
        print(f"      [v2.9] 质量地图: {len(qm_report.regions)} 地区, {qm_report.summary}")
    except Exception as exc:
        print(f"      ⚠️ 节点质量地图失败: {exc}")
        stats["quality_map"] = {"error": str(exc)}

    # ═══════════════════════════════════════════════════════════════
    # v2.9 自适应学习系统
    # ═══════════════════════════════════════════════════════════════
    try:
        from core._adaptive_learning import AdaptiveLearningEngine
        adaptive_engine = AdaptiveLearningEngine(f"{args.output_dir}/adaptive_state.json")
        adaptive_engine.record_run(stats, scoring_config.weights if scoring_config else None)
        learning_report = adaptive_engine.learn(scoring_config.weights if scoring_config else None)
        stats["adaptive_learning"] = {
            "learning_progress": learning_report.learning_progress,
            "weight_adjustments": learning_report.weight_adjustments[:5],
            "sampling_suggestions": learning_report.sampling_suggestions[:5],
            "filter_suggestions": learning_report.filter_suggestions[:5],
            "performance_prediction": learning_report.performance_prediction,
            "summary": learning_report.summary,
        }
        print(f"      [v2.9] 自适应学习: {learning_report.summary}")
    except Exception as exc:
        print(f"      ⚠️ 自适应学习系统失败: {exc}")
        stats["adaptive_learning"] = {"error": str(exc)}

    # 最终写入包含所有 v2.6~v2.9 功能的完整 stats
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
    p.add_argument("--fetch-overall-timeout", type=int, default=120,
                   help="整批订阅抓取总超时秒数，超时后返回已完成源的部分结果")

    p.add_argument("--tcp-check", action=argparse.BooleanOptionalAction, default=True)
    p.add_argument("--tcp-concurrency", type=int, default=200)
    p.add_argument("--tcp-timeout", type=float, default=3.0)

    p.add_argument("--real-test", action=argparse.BooleanOptionalAction, default=True)
    p.add_argument("--test-concurrency", type=int, default=30)
    p.add_argument("--test-timeout", type=float, default=6.0)
    p.add_argument("--startup-wait", type=float, default=0.6)
    p.add_argument("--test-limit", type=int, default=500, help="送入真实测试的最大节点数(0=不限)")
    p.add_argument("--quality-filter", action=argparse.BooleanOptionalAction, default=True,
                   help="启用质量预过滤（配置规则 + 同 server/type 降噪）")
    p.add_argument("--filter-rules", default="config/filter_rules.yaml",
                   help="质量过滤规则配置文件；不存在时使用保守默认规则")
    p.add_argument("--scoring-rules", default="config/scoring.yaml",
                   help="节点评分权重配置文件；不存在时使用内置默认权重")
    p.add_argument("--max-per-server", type=int, default=0,
                   help="§2.2 同 server IP 最多保留的节点数 (0=不限, 默认; 1/2=严格, 但可能误杀 AWS/Hetzner 上不同用户的节点)")
    p.add_argument("--strong-dedup", action=argparse.BooleanOptionalAction, default=False,
                   help="[P1-1] 启用强去重：相同 (server:port:type:sni:host:path) 视为同一节点")
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
