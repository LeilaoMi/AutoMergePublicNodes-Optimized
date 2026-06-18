"""[v2.5] 节点生命周期预测 — 基于历史数据预测节点何时死亡。

用途：让用户提前知道哪些节点"快不行了"，在 tag 或报告中展示预测。

算法：
  - 线性回归判断延迟趋势（上升/稳定/恢复）
  - 结合连续通过次数估计剩余可用轮次
  - 返回 confidence（置信度）和 trend（趋势方向）
"""
from __future__ import annotations

import statistics
from typing import Any, Dict, Optional


def predict_remaining_life(
    stability_data: Dict[str, Dict[str, Any]],
    latency_history: Dict[str, Dict[str, Any]],
    fingerprint: str,
    bad_latency_ms: float = 1200.0,
) -> Optional[Dict[str, Any]]:
    """预测节点剩余可用轮次。

    Args:
        stability_data: node_stability.json 的 nodes 字典
        latency_history: latency_history.json 的 nodes 字典
        fingerprint: 节点指纹
        bad_latency_ms: 延迟超过此值视为不可用

    Returns:
        {"estimated_rounds": N, "confidence": 0.0~1.0, "trend": "stable|degrading|recovering"}
        或 None（历史数据不足）
    """
    stab = stability_data.get(fingerprint, {})
    hist_entry = latency_history.get(fingerprint, {})
    hist = hist_entry.get("history", []) if isinstance(hist_entry, dict) else []

    if not hist or len(hist) < 3:
        return None

    consecutive_pass = int(stab.get("consecutive_pass", 0)) if isinstance(stab, dict) else 0
    latencies = [h["latency_ms"] for h in hist if isinstance(h, dict) and h.get("success")]

    if len(latencies) < 3:
        # 历史太少，只能给粗略估计
        return {
            "estimated_rounds": max(consecutive_pass, 1),
            "confidence": 0.15,
            "trend": "unknown",
        }

    n = len(latencies)
    x_mean = (n - 1) / 2.0
    y_mean = statistics.mean(latencies)

    numerator = sum((i - x_mean) * (latencies[i] - y_mean) for i in range(n))
    denominator = sum((i - x_mean) ** 2 for i in range(n))
    slope = numerator / denominator if denominator > 0 else 0

    if slope > 5:
        # 每轮延迟增加 > 5ms，趋势恶化
        trend = "degrading"
        if slope > 0 and latencies[-1] < bad_latency_ms:
            rounds_left = max(1, int((bad_latency_ms - latencies[-1]) / slope))
        else:
            rounds_left = 0
    elif slope < -5:
        # 每轮延迟降低 > 5ms，趋势恢复
        trend = "recovering"
        rounds_left = max(consecutive_pass * 2, 10)
    else:
        trend = "stable"
        rounds_left = max(consecutive_pass, 8)

    # 抖动越大，置信度越低
    try:
        jitter_ratio = statistics.stdev(latencies) / y_mean if y_mean > 0 else 1.0
    except (statistics.StatisticsError, ZeroDivisionError):
        jitter_ratio = 0.5

    confidence = min(1.0, len(hist) / 10.0) * max(0.2, 1.0 - jitter_ratio)

    return {
        "estimated_rounds": max(0, rounds_left),
        "confidence": round(confidence, 2),
        "trend": trend,
        "slope_ms_per_round": round(slope, 2),
    }


def batch_predict(
    stability_data: Dict[str, Dict[str, Any]],
    latency_history: Dict[str, Dict[str, Any]],
    fingerprints: list[str],
    bad_latency_ms: float = 1200.0,
) -> Dict[str, Dict[str, Any]]:
    """批量预测多个节点的生命周期。

    Returns:
        {fingerprint: prediction_dict}
    """
    results: Dict[str, Dict[str, Any]] = {}
    for fp in fingerprints:
        pred = predict_remaining_life(
            stability_data, latency_history, fp, bad_latency_ms
        )
        if pred is not None:
            results[fp] = pred
    return results