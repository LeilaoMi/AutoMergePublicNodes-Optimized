"""节点加权评分助手。

真测决定节点是否可用；本模块仅对可用节点排序，综合当次测试指标与历史协议/来源质量。
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict

import yaml


@dataclass(frozen=True)
class ScoringConfig:
    weights: Dict[str, float] = field(default_factory=lambda: {
        "latency": 25.0,
        "jitter": 15.0,
        "tcp": 10.0,
        "speed": 10.0,
        "fingerprint_resistance": 5.0,
        "protocol_history": 15.0,
        "source_history": 20.0,
    })
    excellent_latency_ms: float = 120.0
    bad_latency_ms: float = 1200.0
    bad_jitter_ms: float = 400.0
    excellent_tcp_latency_ms: float = 100.0
    bad_tcp_latency_ms: float = 1000.0
    excellent_speed_kbps: float = 500.0
    bad_speed_kbps: float = 10.0
    missing_tcp_score: float = 0.5
    missing_history_score: float = 0.5
    missing_fingerprint_score: float = 0.3


@dataclass(frozen=True)
class ScoreInput:
    latency_ms: float
    jitter_ms: float
    tcp_latency_ms: float
    protocol: str
    source: str
    protocol_rates: Dict[str, float]
    source_rates: Dict[str, float]
    speed_kbps: float = 0.0
    fingerprint_resistance: float = 0.0  # [v2.5.1] 0~1 抗检测评分


def clamp(value: float, min_value: float = 0.0, max_value: float = 1.0) -> float:
    return max(min_value, min(value, max_value))


def _float_value(value: Any, default: float) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def load_scoring_config(path: str = "config/scoring.yaml") -> ScoringConfig:
    config_path = Path(path)
    default = ScoringConfig()
    if not config_path.exists():
        return default

    try:
        data = yaml.safe_load(config_path.read_text(encoding="utf-8")) or {}
    except Exception:
        return default
    if not isinstance(data, dict):
        return default

    weights_raw = data.get("weights") or {}
    if not isinstance(weights_raw, dict):
        weights_raw = {}
    weights = dict(default.weights)
    for key in weights:
        weights[key] = max(0.0, _float_value(weights_raw.get(key), weights[key]))

    thresholds = data.get("thresholds") or {}
    if not isinstance(thresholds, dict):
        thresholds = {}
    defaults = data.get("defaults") or {}
    if not isinstance(defaults, dict):
        defaults = {}

    return ScoringConfig(
        weights=weights,
        excellent_latency_ms=max(1.0, _float_value(thresholds.get("excellent_latency_ms"), default.excellent_latency_ms)),
        bad_latency_ms=max(1.0, _float_value(thresholds.get("bad_latency_ms"), default.bad_latency_ms)),
        bad_jitter_ms=max(1.0, _float_value(thresholds.get("bad_jitter_ms"), default.bad_jitter_ms)),
        excellent_tcp_latency_ms=max(1.0, _float_value(thresholds.get("excellent_tcp_latency_ms"), default.excellent_tcp_latency_ms)),
        bad_tcp_latency_ms=max(1.0, _float_value(thresholds.get("bad_tcp_latency_ms"), default.bad_tcp_latency_ms)),
        excellent_speed_kbps=max(1.0, _float_value(thresholds.get("excellent_speed_kbps"), default.excellent_speed_kbps)),
        bad_speed_kbps=max(0.0, _float_value(thresholds.get("bad_speed_kbps"), default.bad_speed_kbps)),
        missing_tcp_score=clamp(_float_value(defaults.get("missing_tcp_score"), default.missing_tcp_score)),
        missing_history_score=clamp(_float_value(defaults.get("missing_history_score"), default.missing_history_score)),
        missing_fingerprint_score=clamp(_float_value(defaults.get("missing_fingerprint_score"), default.missing_fingerprint_score)),
    )


def latency_score(latency_ms: float, cfg: ScoringConfig | None = None) -> float:
    cfg = cfg or ScoringConfig()
    if latency_ms <= 0:
        return 0.0
    if latency_ms <= cfg.excellent_latency_ms:
        return 1.0
    if latency_ms >= cfg.bad_latency_ms:
        return 0.0
    span = max(cfg.bad_latency_ms - cfg.excellent_latency_ms, 1.0)
    return clamp(1 - (latency_ms - cfg.excellent_latency_ms) / span)


def jitter_score(jitter_ms: float, cfg: ScoringConfig | None = None) -> float:
    cfg = cfg or ScoringConfig()
    if jitter_ms <= 0:
        return 1.0
    if jitter_ms >= cfg.bad_jitter_ms:
        return 0.0
    return clamp(1 - jitter_ms / cfg.bad_jitter_ms)


def tcp_score(tcp_latency_ms: float, cfg: ScoringConfig | None = None) -> float:
    cfg = cfg or ScoringConfig()
    if tcp_latency_ms <= 0:
        return cfg.missing_tcp_score
    if tcp_latency_ms <= cfg.excellent_tcp_latency_ms:
        return 1.0
    if tcp_latency_ms >= cfg.bad_tcp_latency_ms:
        return 0.0
    span = max(cfg.bad_tcp_latency_ms - cfg.excellent_tcp_latency_ms, 1.0)
    return clamp(1 - (tcp_latency_ms - cfg.excellent_tcp_latency_ms) / span)


def speed_score(speed_kbps: float, cfg: ScoringConfig | None = None) -> float:
    """[v2.5] 下载速度评分：speed_kbps 越高越好。"""
    cfg = cfg or ScoringConfig()
    if speed_kbps <= 0:
        return 0.0
    if speed_kbps >= cfg.excellent_speed_kbps:
        return 1.0
    if speed_kbps <= cfg.bad_speed_kbps:
        return 0.0
    span = max(cfg.excellent_speed_kbps - cfg.bad_speed_kbps, 1.0)
    return clamp((speed_kbps - cfg.bad_speed_kbps) / span)


def historical_rate_score(name: str, rates: Dict[str, float], default: float = 0.5) -> float:
    if not name:
        return default
    try:
        return clamp(float(rates.get(name, default)))
    except (TypeError, ValueError):
        return default


def calculate_score_breakdown(data: ScoreInput, config: ScoringConfig | None = None) -> Dict[str, Dict[str, float]]:
    """Return normalized factor scores and weighted contributions.

    Each item contains:
    - `score`: normalized 0..1 factor score
    - `weight`: configured factor weight
    - `points`: factor contribution to final score
    """
    cfg = config or ScoringConfig()
    factors = {
        "latency": latency_score(data.latency_ms, cfg),
        "jitter": jitter_score(data.jitter_ms, cfg),
        "tcp": tcp_score(data.tcp_latency_ms, cfg),
        "speed": speed_score(data.speed_kbps, cfg),
        "fingerprint_resistance": data.fingerprint_resistance if data.fingerprint_resistance > 0 else cfg.missing_fingerprint_score,
        "protocol_history": historical_rate_score(data.protocol, data.protocol_rates, cfg.missing_history_score),
        "source_history": historical_rate_score(data.source, data.source_rates, cfg.missing_history_score),
    }
    breakdown: Dict[str, Dict[str, float]] = {}
    for key, factor_score in factors.items():
        weight = cfg.weights.get(key, 0.0)
        breakdown[key] = {
            "score": round(factor_score, 4),
            "weight": round(weight, 4),
            "points": round(factor_score * weight, 2),
        }
    return breakdown


def calculate_score(data: ScoreInput, config: ScoringConfig | None = None) -> float:
    """Return a 0..100 quality score for a node."""
    breakdown = calculate_score_breakdown(data, config)
    return round(sum(item["points"] for item in breakdown.values()), 2)
