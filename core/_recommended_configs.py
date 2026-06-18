"""[P2-3] 智能客户端推荐配置生成。

基于真测结果，生成开箱即用的"聪明"订阅：
- output/clash.recommended.yaml：自动分组 + urltest 自动切换
- output/singbox.recommended.json：内置 selector 节点选择器
- output/for_mobile.txt：只保留 hy2/tuic，移动友好
- output/for_streaming.txt：只保留 netflix/disney 解锁的节点

所有输出都是基于已经真测通过（scored_valid）的节点，不引入新的真测。
"""
from __future__ import annotations

import base64
import json
import os
from dataclasses import replace
from typing import Any, Dict, List, Optional

import yaml

from core.parser import Node


# ============================================================
# Clash Meta 推荐配置
# ============================================================

def _node_to_clash_proxy(n: Node) -> Dict[str, Any]:
    """Node → Clash proxy dict（最小子集，sing-box 已经能直接转）。"""
    base = {
        "name": n.tag,
        "type": _clash_type(n.type),
        "server": n.server,
        "port": n.server_port,
    }
    r = n.raw or {}
    if n.type in ("vmess", "vless"):
        base["uuid"] = r.get("uuid", "")
    if n.type == "vmess":
        base["alterId"] = int(r.get("alter_id", 0) or 0)
        base["cipher"] = r.get("security", "auto")
    if n.type in ("trojan", "shadowsocks", "hysteria2"):
        base["password"] = r.get("password", "")
    if n.type == "shadowsocks":
        base["cipher"] = r.get("method", "aes-128-gcm")
    if n.type in ("hysteria", "hysteria2", "tuic", "vless", "trojan"):
        tls = r.get("tls") or {}
        if tls.get("enabled"):
            base["tls"] = True
            base["servername"] = tls.get("server_name", n.server)
    if n.type == "hysteria":
        base["auth-str"] = r.get("auth_str", "")
        base["up"] = f"{r.get('up_mbps', 10)} Mbps"
        base["down"] = f"{r.get('down_mbps', 50)} Mbps"
    if n.type == "tuic":
        base["uuid"] = r.get("uuid", "")
        base["password"] = r.get("password", "")
    return base


def _clash_type(t: str) -> str:
    mapping = {
        "shadowsocks": "ss",
        "shadowsocksr": "ssr",
        "hysteria2": "hysteria2",
        "hysteria": "hysteria",
        "vless": "vless",
        "vmess": "vmess",
        "trojan": "trojan",
        "tuic": "tuic",
        "anytls": "anytls",
    }
    return mapping.get(t, t)


def build_clash_recommended(
    scored_valid: List[tuple],
    top_n: int = 30,
) -> Dict[str, Any]:
    """[P2-3] 生成 Clash Meta 推荐配置：自动分组 + urltest。

    scored_valid: [(node, latency, jitter, score, source, breakdown, test_result), ...]
    """
    nodes = [e[0] for e in scored_valid[:top_n]]
    if not nodes:
        return {}
    proxies = [_node_to_clash_proxy(n) for n in nodes]
    proxy_names = [p["name"] for p in proxies]
    return {
        "mixed-port": 7890,
        "allow-lan": False,
        "mode": "rule",
        "log-level": "info",
        "proxies": proxies,
        "proxy-groups": [
            {
                "name": "🚀 节点选择",
                "type": "select",
                "proxies": ["⚡ 自动选择", "♻️ 手动选择", "DIRECT"] + proxy_names,
            },
            {
                "name": "⚡ 自动选择",
                "type": "url-test",
                "proxies": proxy_names,
                "url": "http://www.gstatic.com/generate_204",
                "interval": 300,
                "tolerance": 50,
            },
            {
                "name": "♻️ 手动选择",
                "type": "select",
                "proxies": proxy_names,
            },
        ],
        "rules": [
            "DOMAIN-SUFFIX,local,DIRECT",
            "IP-CIDR,127.0.0.0/8,DIRECT",
            "GEOIP,CN,DIRECT",
            "MATCH,🚀 节点选择",
        ],
    }


def write_clash_recommended(
    scored_valid: List[tuple],
    output_dir: str,
    top_n: int = 30,
) -> Optional[str]:
    cfg = build_clash_recommended(scored_valid, top_n=top_n)
    if not cfg:
        return None
    path = os.path.join(output_dir, "clash.recommended.yaml")
    with open(path, "w", encoding="utf-8") as f:
        yaml.safe_dump(cfg, f, allow_unicode=True, sort_keys=False)
    return path


# ============================================================
# sing-box 推荐配置（内置 selector）
# ============================================================

def build_singbox_recommended(
    scored_valid: List[tuple],
    top_n: int = 30,
) -> Dict[str, Any]:
    """[P2-3] 生成 sing-box 推荐配置：selector 自动选 + urltest 探测。"""
    nodes = [e[0] for e in scored_valid[:top_n]]
    if not nodes:
        return {}
    outbounds = [n.to_singbox() for n in nodes]
    # 加 tag 便于 selector 引用
    for tag, ob in zip([n.tag for n in nodes], outbounds):
        ob["tag"] = tag
    outbounds.append({"type": "direct", "tag": "direct"})
    outbounds.append({
        "type": "selector",
        "tag": "auto",
        "outbounds": [n.tag for n in nodes] + ["direct"],
        "default": nodes[0].tag if nodes else "direct",
    })
    outbounds.append({
        "type": "urltest",
        "tag": "urltest",
        "outbounds": [n.tag for n in nodes],
        "url": "http://www.gstatic.com/generate_204",
        "interval": "5m",
        "tolerance": 50,
    })
    return {
        "log": {"level": "info"},
        "inbounds": [
            {"type": "mixed", "tag": "mixed-in", "listen": "127.0.0.1", "listen_port": 2080},
        ],
        "outbounds": outbounds,
        "route": {
            "final": "auto",
            "rules": [
                {"ip_is_private": True, "outbound": "direct"},
            ],
        },
    }


def write_singbox_recommended(
    scored_valid: List[tuple],
    output_dir: str,
    top_n: int = 30,
) -> Optional[str]:
    cfg = build_singbox_recommended(scored_valid, top_n=top_n)
    if not cfg:
        return None
    path = os.path.join(output_dir, "singbox.recommended.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(cfg, f, ensure_ascii=False, indent=2)
    return path


# ============================================================
# 专项筛选：移动 / 流媒体
# ============================================================

MOBILE_FRIENDLY_PROTOCOLS = {"hysteria2", "tuic", "anytls"}


def write_for_mobile(
    scored_valid: List[tuple],
    output_dir: str,
    top_n: int = 50,
) -> Optional[str]:
    """[P2-3] 只保留移动友好协议：hy2/tuic/anytls。"""
    filtered = [e for e in scored_valid if e[0].type in MOBILE_FRIENDLY_PROTOCOLS][:top_n]
    if not filtered:
        return None
    return _write_b64_urls(filtered, output_dir, "for_mobile.txt")


def write_for_streaming(
    scored_valid: List[tuple],
    output_dir: str,
    top_n: int = 50,
) -> Optional[str]:
    """[P2-3] 只保留解锁 Netflix/Disney 的节点。"""
    filtered = []
    for e in scored_valid:
        if len(e) < 7:
            continue
        r = e[6]
        caps = getattr(r, "capabilities", None) or {}
        if caps.get("netflix") or caps.get("disney"):
            filtered.append(e)
        if len(filtered) >= top_n:
            break
    if not filtered:
        return None
    return _write_b64_urls(filtered, output_dir, "for_streaming.txt")


def _write_b64_urls(scored: List[tuple], output_dir: str, name: str) -> Optional[str]:
    """把 scored 列表写成 base64 订阅文件。"""
    from core.generator import node_to_url, _prepare_nodes
    prepared = _prepare_nodes([e[0] for e in scored])
    urls = [u for u in (node_to_url(n) for n in prepared) if u]
    if not urls:
        return None
    b64 = base64.b64encode("\n".join(urls).encode()).decode()
    path = os.path.join(output_dir, name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(b64)
    return path
