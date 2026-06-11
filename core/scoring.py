"""Weighted node scoring helpers.

The real proxy test decides whether a node is usable. This module only ranks usable
nodes by combining current test metrics with historical protocol/source quality.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict


@dataclass(frozen=True)
class ScoreInput:
    latency_ms: float
    jitter_ms: float
    tcp_latency_ms: float
    protocol: str
    source: str
    protocol_rates: Dict[str, float]
    source_rates: Dict[str, float]


def clamp(value: float, min_value: float = 0.0, max_value: float = 1.0) -> float:
    return max(min_value, min(value, max_value))


def latency_score(latency_ms: float) -> float:
    if latency_ms <= 0:
        return 0.0
    if latency_ms <= 120:
        return 1.0
    if latency_ms >= 1200:
        return 0.0
    return clamp(1 - (latency_ms - 120) / 1080)


def jitter_score(jitter_ms: float) -> float:
    if jitter_ms <= 0:
        return 1.0
    if jitter_ms >= 400:
        return 0.0
    return clamp(1 - jitter_ms / 400)


def tcp_score(tcp_latency_ms: float) -> float:
    if tcp_latency_ms <= 0:
        return 0.5
    if tcp_latency_ms <= 100:
        return 1.0
    if tcp_latency_ms >= 1000:
        return 0.0
    return clamp(1 - (tcp_latency_ms - 100) / 900)


def historical_rate_score(name: str, rates: Dict[str, float], default: float = 0.5) -> float:
    if not name:
        return default
    try:
        return clamp(float(rates.get(name, default)))
    except (TypeError, ValueError):
        return default


def calculate_score(data: ScoreInput) -> float:
    """Return a 0..100 quality score for a node.

    Weights:
    - real-test latency: 35
    - real-test jitter: 15
    - TCP latency: 10
    - historical protocol quality: 20
    - historical source quality: 20
    """
    score = (
        latency_score(data.latency_ms) * 35
        + jitter_score(data.jitter_ms) * 15
        + tcp_score(data.tcp_latency_ms) * 10
        + historical_rate_score(data.protocol, data.protocol_rates) * 20
        + historical_rate_score(data.source, data.source_rates) * 20
    )
    return round(score, 2)
