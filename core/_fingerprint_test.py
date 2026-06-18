"""[v2.5] 协议指纹对抗检测 — 评估节点的流量伪装能力。

GFW 使用 DPI（深度包检测）识别代理流量。不同协议的抗检测能力差异巨大：
  - REALITY: 伪装为正常 TLS 握手，目前最难检测 → resistance=high
  - uTLS:    模拟浏览器 TLS 指纹（JA3/JA4），中等抗检测 → resistance=medium
  - 普通 TLS: 标准 TLS 但无指纹伪装 → resistance=low
  - 无 TLS:   明文传输，极易被识别 → resistance=none

此模块为评分系统提供 fingerprint_resistance 因子。
"""
from __future__ import annotations

from typing import Any, Dict

from core.parser import Node


# 抗检测等级映射
RESISTANCE_LEVELS = {
    "high": 1.0,    # REALITY — 目前最强
    "medium": 0.7,  # uTLS / WebSocket+TLS — 有伪装
    "low": 0.4,     # 普通 TLS — 标准但有指纹
    "none": 0.1,    # 无 TLS — 明文
}


def analyze_fingerprint_resistance(node: Node) -> Dict[str, Any]:
    """分析单个节点的流量指纹抗检测能力。

    Returns:
        {
            "resistance": "high|medium|low|none",
            "score": 0.0~1.0,
            "has_reality": bool,
            "has_utls": bool,
            "has_ws_tls": bool,
            "tls_enabled": bool,
            "detail": str,
        }
    """
    r = node.raw or {}
    tls = r.get("tls", {}) or {}
    transport = r.get("transport", {}) or {}

    has_reality = bool(tls.get("reality", {}).get("enabled"))
    has_utls = bool(tls.get("utls", {}).get("fingerprint"))
    tls_enabled = bool(tls.get("enabled"))
    transport_type = transport.get("type", "tcp")

    # WebSocket + TLS 组合有一定伪装能力（看起来像正常 HTTPS 流量）
    has_ws_tls = (transport_type == "ws" and tls_enabled)

    # gRPC + TLS 也有一定伪装能力
    has_grpc_tls = (transport_type == "grpc" and tls_enabled)

    # HTTP/2 + TLS
    has_h2_tls = (transport_type == "http" and tls_enabled)

    # 判定等级
    if has_reality:
        resistance = "high"
        detail = "REALITY protocol — strongest DPI resistance"
    elif has_utls and tls_enabled:
        resistance = "medium"
        fp = tls.get("utls", {}).get("fingerprint", "unknown")
        detail = f"uTLS fingerprint ({fp}) — browser-like TLS"
    elif has_ws_tls:
        resistance = "medium"
        detail = "WebSocket + TLS — HTTPS-like traffic"
    elif has_grpc_tls or has_h2_tls:
        resistance = "medium"
        detail = f"{transport_type} + TLS — structured protocol masking"
    elif tls_enabled:
        resistance = "low"
        detail = "Plain TLS — standard fingerprint detectable"
    else:
        resistance = "none"
        detail = "No TLS — plaintext traffic, easily identified"

    # 协议本身也有影响：QUIC 类协议（hy2/tuic）有额外混淆
    if node.type in ("hysteria2", "tuic") and tls_enabled:
        if resistance == "low":
            resistance = "medium"
            detail += " + QUIC-based protocol adds obfuscation"

    return {
        "resistance": resistance,
        "score": RESISTANCE_LEVELS.get(resistance, 0.1),
        "has_reality": has_reality,
        "has_utls": has_utls,
        "has_ws_tls": has_ws_tls,
        "tls_enabled": tls_enabled,
        "detail": detail,
    }


def fingerprint_resistance_score(node: Node) -> float:
    """快速返回 0~1 的抗检测评分，可直接用于 scoring。"""
    return analyze_fingerprint_resistance(node)["score"]