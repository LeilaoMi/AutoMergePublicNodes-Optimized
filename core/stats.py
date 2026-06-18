"""统计助手：采样、源质量、趋势历史与节点稳定性。

本模块把报告/健康度逻辑从 main.py 中抽出来，让流水线入口专注于编排。

[P1-2] 历史通过率改用 EWMA（指数加权移动平均）：
  - 旧实现把全轮平均，老节点统治
  - 新实现 alpha=0.3 → 最近 5 轮权重 ≈ 83%，老数据自然衰减
  - 同时持久化到 trend_history.json 的 recent_runs 字段，下游消费
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List, Optional, Tuple


# [P1-2] EWMA 平滑系数。0.3 表示对最近一轮赋予 30% 权重，历史轮次按 0.7 衰减。
# 数学上：最近 5 轮累计权重 = 1 - 0.7^5 ≈ 0.832
EWMA_ALPHA = 0.3
DEFAULT_HISTORY_WEIGHT = 0.5  # 完全没有历史时的兜底分


def smoothed_pass_rate(stats: Dict[str, int]) -> float:
    passed = int(stats.get("pass", 0) or 0)
    failed = int(stats.get("fail", 0) or 0)
    return (passed + 1) / (passed + failed + 2)


def ewma(values: List[float], alpha: float = EWMA_ALPHA, default: float = DEFAULT_HISTORY_WEIGHT) -> float:
    """[P1-2] 指数加权移动平均。

    Args:
        values: 时间序列（最早 → 最新）
        alpha: 新值权重，0 < alpha <= 1，越大越敏感
        default: 序列为空时的兜底分

    Returns:
        平滑后的值，范围 [0, 1]
    """
    if not values:
        return default
    s = float(values[0])
    for v in values[1:]:
        s = alpha * float(v) + (1 - alpha) * s
    # 兜底夹紧
    if s != s:  # NaN
        return default
    return max(0.0, min(1.0, s))


def ewma_from_runs(runs: List[Dict[str, object]], key: str, alpha: float = EWMA_ALPHA) -> Optional[float]:
    """从 trend_history.json 的 runs 列表提取某字段的 EWMA。"""
    series: List[float] = []
    for r in runs:
        if not isinstance(r, dict):
            continue
        v = r.get(key)
        if v is None:
            continue
        try:
            series.append(float(v))
        except (TypeError, ValueError):
            continue
    if not series:
        return None
    return ewma(series, alpha=alpha)


def build_source_scores(
    source_nodes: Dict[str, int],
    source_pass_rate: Dict[str, Dict[str, int]],
    source_dead_counts: Dict[str, int] | None = None,
) -> Dict[str, Dict[str, object]]:
    """Build stable source quality scores for reporting and weighted sampling.

    score roughly means: historical real-test quality, with small confidence bonus
    for sources that produced enough nodes and penalty for consecutive dead runs.
    """
    source_dead_counts = source_dead_counts or {}
    names = set(source_nodes) | set(source_pass_rate) | set(source_dead_counts)
    scores: Dict[str, Dict[str, object]] = {}
    for name in sorted(names):
        counts = source_pass_rate.get(name, {})
        passed = int(counts.get("pass", 0) or 0)
        failed = int(counts.get("fail", 0) or 0)
        tested = passed + failed
        parsed = int(source_nodes.get(name, 0) or 0)
        consecutive_dead = int(source_dead_counts.get(name, 0) or 0)
        pass_rate = (passed / tested) if tested else None
        smoothed_rate = smoothed_pass_rate({"pass": passed, "fail": failed}) if tested else 0.5
        confidence = min(tested / 20, 1.0)
        parsed_bonus = min(parsed / 2000, 1.0) * 0.08
        dead_penalty = min(consecutive_dead * 0.15, 0.6)
        score = max(0.0, min(1.0, smoothed_rate * (0.35 + 0.65 * confidence) + parsed_bonus - dead_penalty))
        if consecutive_dead >= 2:
            recommendation = "disable-candidate"
        elif tested >= 5 and score < 0.25:
            recommendation = "downweight"
        elif tested >= 5 and score >= 0.7:
            recommendation = "prefer"
        else:
            recommendation = "observe"
        scores[name] = {
            "score": round(score, 3),
            "pass_rate": round(pass_rate, 3) if pass_rate is not None else None,
            "smoothed_pass_rate": round(smoothed_rate, 3),
            "pass": passed,
            "fail": failed,
            "tested": tested,
            "parsed_nodes": parsed,
            "consecutive_dead": consecutive_dead,
            "recommendation": recommendation,
        }
    return scores


def load_historical_pass_rates(output_dir: str) -> Tuple[Dict[str, float], Dict[str, float]]:
    stats_path = Path(output_dir) / "stats.json"
    if not stats_path.exists():
        return {}, {}
    try:
        stats = json.loads(stats_path.read_text(encoding="utf-8"))
    except Exception:
        return {}, {}
    protocol_rates = {
        name: smoothed_pass_rate(values)
        for name, values in (stats.get("protocol_pass_rate") or {}).items()
        if isinstance(values, dict)
    }
    source_scores = stats.get("source_scores") or {}
    source_rates = {
        name: float(values.get("score", 0.5))
        for name, values in source_scores.items()
        if isinstance(values, dict)
    }
    if not source_rates:
        source_rates = {
            name: smoothed_pass_rate(values)
            for name, values in (stats.get("source_pass_rate") or {}).items()
            if isinstance(values, dict)
        }
    return protocol_rates, source_rates


# ============================================================
# Node stability tracking (per-fingerprint pass/fail history)
# ============================================================

def load_node_stability(output_dir: str) -> Dict[str, Dict[str, object]]:
    """Load node stability history from node_stability.json.

    Returns a dict keyed by fingerprint:
        {fp: {"consecutive_pass": N, "consecutive_fail": N, "total_pass": N, "total_fail": N, "last_seen": "..."}}
    """
    path = Path(output_dir) / "node_stability.json"
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(data, dict) and "nodes" in data:
            return data["nodes"]
        return data if isinstance(data, dict) else {}
    except Exception:
        return {}


def update_node_stability(
    output_dir: str,
    passed_fingerprints: List[str],
    failed_fingerprints: List[str],
    timestamp: str,
    keep_recent: int = 5000,
) -> Dict[str, Dict[str, object]]:
    """Update node stability history with this run's results.

    Tracks consecutive pass/fail and total pass/fail per fingerprint.
    Keeps only the most recent `keep_recent` fingerprints to bound file size.
    """
    path = Path(output_dir) / "node_stability.json"
    nodes: Dict[str, Dict[str, object]] = load_node_stability(str(Path(output_dir)))

    all_fps = set(passed_fingerprints) | set(failed_fingerprints)

    for fp in all_fps:
        entry = nodes.get(fp, {
            "consecutive_pass": 0,
            "consecutive_fail": 0,
            "total_pass": 0,
            "total_fail": 0,
            "last_seen": "",
        })
        entry = dict(entry)  # copy
        if fp in passed_fingerprints:
            entry["consecutive_pass"] = int(entry.get("consecutive_pass", 0)) + 1
            entry["consecutive_fail"] = 0
            entry["total_pass"] = int(entry.get("total_pass", 0)) + 1
        else:
            entry["consecutive_fail"] = int(entry.get("consecutive_fail", 0)) + 1
            entry["consecutive_pass"] = 0
            entry["total_fail"] = int(entry.get("total_fail", 0)) + 1
        entry["last_seen"] = timestamp
        nodes[fp] = entry

    # Prune: keep only fingerprints seen recently
    if len(nodes) > keep_recent:
        # Sort by last_seen descending, keep top N
        sorted_nodes = sorted(
            nodes.items(),
            key=lambda x: x[1].get("last_seen", ""),
            reverse=True,
        )
        nodes = dict(sorted_nodes[:keep_recent])

    payload = {
        "updated_at": timestamp,
        "total_tracked": len(nodes),
        "nodes": nodes,
    }
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    return payload


def get_stable_nodes(stability: Dict[str, Dict[str, object]], min_consecutive: int = 3) -> List[str]:
    """Return fingerprints with >= min_consecutive consecutive passes."""
    return [
        fp for fp, data in stability.items()
        if isinstance(data, dict) and int(data.get("consecutive_pass", 0)) >= min_consecutive
    ]


def build_trend_entry(stats: Dict[str, object]) -> Dict[str, object]:
    return {
        "timestamp": stats.get("timestamp"),
        "duration_sec": stats.get("duration_sec"),
        "nodes_raw": stats.get("nodes_raw"),
        "nodes_dedup": stats.get("nodes_dedup"),
        "nodes_tcp_ok": stats.get("nodes_tcp_ok"),
        "nodes_real_ok": stats.get("nodes_real_ok"),
        "nodes_verified_output": stats.get("nodes_verified_output"),
        "nodes_global_output": stats.get("nodes_global_output"),
        "nodes_global_extra_from_cn_block": stats.get("nodes_global_extra_from_cn_block"),
        "real_test_errors": stats.get("real_test_errors", {}),
        "output_guard": stats.get("output_guard", {}),
    }


def build_trend_alerts(runs: List[Dict[str, object]]) -> List[Dict[str, object]]:
    alerts: List[Dict[str, object]] = []
    if len(runs) < 2:
        return alerts

    latest = runs[-1]
    previous = runs[-2]

    latest_verified = int(latest.get("nodes_verified_output") or 0)
    previous_verified = int(previous.get("nodes_verified_output") or 0)
    if previous_verified > 0 and latest_verified < previous_verified * 0.5:
        alerts.append({
            "type": "verified_drop_50pct",
            "message": f"verified output dropped from {previous_verified} to {latest_verified}",
            "previous": previous_verified,
            "current": latest_verified,
        })

    latest_real = int(latest.get("nodes_real_ok") or 0)
    previous_real = int(previous.get("nodes_real_ok") or 0)
    if previous_real > 0 and latest_real < previous_real * 0.5:
        alerts.append({
            "type": "real_ok_drop_50pct",
            "message": f"real-test ok dropped from {previous_real} to {latest_real}",
            "previous": previous_real,
            "current": latest_real,
        })

    if len(runs) >= 4:
        last4 = runs[-4:]
        verified_values = [int(r.get("nodes_verified_output") or 0) for r in last4]
        if all(a > b for a, b in zip(verified_values, verified_values[1:])):
            alerts.append({
                "type": "verified_downtrend_4_runs",
                "message": "verified output decreased for 4 consecutive runs",
                "values": verified_values,
            })

    guard = latest.get("output_guard", {})
    if isinstance(guard, dict):
        preserved = [name for name, data in guard.items() if isinstance(data, dict) and data.get("preserved")]
        if preserved:
            alerts.append({
                "type": "output_guard_preserved",
                "message": "output shrink guard preserved previous files",
                "prefixes": preserved,
            })

    return alerts


def update_trend_history(output_dir: str, stats: Dict[str, object], keep: int = 30) -> Dict[str, object]:
    path = Path(output_dir) / "trend_history.json"
    runs: List[Dict[str, object]] = []
    if path.exists():
        try:
            previous = json.loads(path.read_text(encoding="utf-8"))
            previous_runs = previous.get("runs", []) if isinstance(previous, dict) else previous
            if isinstance(previous_runs, list):
                runs = [r for r in previous_runs if isinstance(r, dict)]
        except Exception:
            runs = []
    runs.append(build_trend_entry(stats))
    if keep > 0:
        runs = runs[-keep:]
    trend_alerts = build_trend_alerts(runs)
    payload = {
        "updated_at": stats.get("timestamp"),
        "keep": keep,
        "runs": runs,
        "alerts": trend_alerts,
    }
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    return payload
