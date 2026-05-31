"""
订阅文件生成器
输出多种格式:
- {prefix}.json   : sing-box 完整配置（Karing 直接导入）
- {prefix}.yaml   : Clash Meta YAML
- {prefix}.txt    : V2Ray base64 订阅
- {prefix}.urls   : 节点 URL 列表（一行一个）
"""
from __future__ import annotations

import base64
import json
from typing import Any, Dict, List
from urllib.parse import quote

import yaml

from core.parser import Node


# ============================================================
# Node → URL (V2Ray 订阅格式)
# ============================================================

def node_to_url(n: Node) -> str:
    t = n.type
    r = n.raw

    if t == "vmess":
        cfg = {
            "v": "2",
            "ps": n.tag,
            "add": n.server,
            "port": str(n.server_port),
            "id": r.get("uuid", ""),
            "aid": str(r.get("alter_id", 0)),
            "scy": r.get("security", "auto"),
            "net": "tcp",
            "type": "none",
            "host": "",
            "path": "",
            "tls": "",
            "sni": "",
        }
        if r.get("tls", {}).get("enabled"):
            cfg["tls"] = "tls"
            cfg["sni"] = r["tls"].get("server_name", "")
        tp = r.get("transport", {})
        if tp.get("type") == "ws":
            cfg["net"] = "ws"
            cfg["path"] = tp.get("path", "/")
            cfg["host"] = (tp.get("headers", {}) or {}).get("Host", "")
        elif tp.get("type") == "grpc":
            cfg["net"] = "grpc"
            cfg["path"] = tp.get("service_name", "")
        elif tp.get("type") == "http":
            cfg["net"] = "h2"
            cfg["path"] = tp.get("path", "/")
            cfg["host"] = ", ".join(tp.get("host", []))
        body = base64.b64encode(json.dumps(cfg, separators=(",", ":")).encode()).decode()
        return f"vmess://{body}"

    if t == "vless":
        params: List[str] = []
        tls = r.get("tls", {})
        if tls.get("enabled"):
            if tls.get("reality"):
                params.append("security=reality")
                params.append(f"pbk={tls['reality'].get('public_key','')}")
                if tls["reality"].get("short_id"):
                    params.append(f"sid={tls['reality']['short_id']}")
            else:
                params.append("security=tls")
            fp = (tls.get("utls") or {}).get("fingerprint")
            if fp:
                params.append(f"fp={fp}")
            params.append(f"sni={tls.get('server_name','')}")
        if r.get("flow"):
            params.append(f"flow={r['flow']}")
        tp = r.get("transport", {})
        if tp.get("type"):
            params.append(f"type={tp['type']}")
            if tp["type"] == "ws":
                params.append(f"path={quote(tp.get('path','/'))}")
                host = (tp.get("headers", {}) or {}).get("Host", "")
                if host:
                    params.append(f"host={host}")
            elif tp["type"] == "grpc":
                params.append(f"serviceName={tp.get('service_name','')}")
            elif tp["type"] == "http":
                params.append(f"path={quote(tp.get('path','/'))}")
                host = ", ".join(tp.get("host", []))
                if host:
                    params.append(f"host={host}")
        else:
            params.append("type=tcp")
        qs = "&".join(params)
        return f"vless://{r.get('uuid','')}@{n.server}:{n.server_port}?{qs}#{quote(n.tag)}"

    if t == "trojan":
        params = [f"sni={r.get('tls',{}).get('server_name', n.server)}"]
        tp = r.get("transport", {})
        if tp.get("type") == "ws":
            params.append("type=ws")
            params.append(f"path={quote(tp.get('path','/'))}")
        elif tp.get("type") == "grpc":
            params.append("type=grpc")
            params.append(f"serviceName={tp.get('service_name','')}")
        elif tp.get("type") == "http":
            params.append("type=http")
            params.append(f"path={quote(tp.get('path','/'))}")
            host = ", ".join(tp.get("host", []))
            if host:
                params.append(f"host={host}")
        qs = "&".join(params)
        return f"trojan://{r.get('password','')}@{n.server}:{n.server_port}?{qs}#{quote(n.tag)}"

    if t == "shadowsocks":
        userinfo = f"{r.get('method','')}:{r.get('password','')}"
        b64 = base64.urlsafe_b64encode(userinfo.encode()).decode().rstrip("=")
        url = f"ss://{b64}@{n.server}:{n.server_port}"
        if r.get("plugin"):
            opts = r["plugin"]
            if r.get("plugin_opts"):
                opts = f"{opts};{r['plugin_opts']}"
            url += f"?plugin={quote(opts)}"
        return f"{url}#{quote(n.tag)}"

    if t == "shadowsocksr":
        password_b64 = base64.urlsafe_b64encode(r.get("password", "").encode()).decode().rstrip("=")
        head = f"{n.server}:{n.server_port}:{r.get('protocol','origin')}:{r.get('method','')}:{r.get('obfs','plain')}:{password_b64}"
        params = [f"remarks={base64.urlsafe_b64encode(n.tag.encode()).decode().rstrip('=')}"]
        if r.get("obfs_param"):
            params.append(f"obfsparam={base64.urlsafe_b64encode(r['obfs_param'].encode()).decode().rstrip('=')}")
        if r.get("protocol_param"):
            params.append(f"protoparam={base64.urlsafe_b64encode(r['protocol_param'].encode()).decode().rstrip('=')}")
        full = f"{head}/?{'&'.join(params)}"
        return "ssr://" + base64.urlsafe_b64encode(full.encode()).decode().rstrip("=")

    if t == "hysteria2":
        sni = r.get("tls", {}).get("server_name", n.server)
        url = f"hysteria2://{quote(r.get('password',''))}@{n.server}:{n.server_port}?sni={sni}&insecure=1"
        if r.get("obfs"):
            url += f"&obfs={r['obfs'].get('type','')}&obfs-password={quote(r['obfs'].get('password',''))}"
        return f"{url}#{quote(n.tag)}"

    if t == "hysteria":
        sni = r.get("tls", {}).get("server_name", n.server)
        url = f"hysteria://{n.server}:{n.server_port}?auth={quote(r.get('auth_str',''))}&peer={sni}&upmbps={r.get('up_mbps',10)}&downmbps={r.get('down_mbps',50)}&insecure=1"
        return f"{url}#{quote(n.tag)}"

    if t == "tuic":
        sni = r.get("tls", {}).get("server_name", n.server)
        alpn = ",".join(r.get("tls", {}).get("alpn", ["h3"]))
        url = f"tuic://{r.get('uuid','')}:{quote(r.get('password',''))}@{n.server}:{n.server_port}?sni={sni}&alpn={alpn}&congestion_control={r.get('congestion_control','bbr')}"
        return f"{url}#{quote(n.tag)}"

    if t == "anytls":
        sni = r.get("tls", {}).get("server_name", n.server)
        return f"anytls://{quote(r.get('password',''))}@{n.server}:{n.server_port}?sni={sni}#{quote(n.tag)}"

    if t == "socks":
        userinfo = ""
        if r.get("username"):
            userinfo = f"{quote(r['username'])}:{quote(r.get('password',''))}@"
        return f"socks5://{userinfo}{n.server}:{n.server_port}#{quote(n.tag)}"

    return ""


# ============================================================
# Node → Clash YAML proxy
# ============================================================

def node_to_clash(n: Node) -> Dict[str, Any]:
    t, r = n.type, n.raw
    base: Dict[str, Any] = {"name": n.tag, "server": n.server, "port": n.server_port}

    if t == "vmess":
        proxy = {**base, "type": "vmess", "uuid": r.get("uuid", ""),
                 "alterId": r.get("alter_id", 0), "cipher": r.get("security", "auto"),
                 "udp": True}
        if r.get("tls", {}).get("enabled"):
            proxy["tls"] = True
            proxy["servername"] = r["tls"].get("server_name", "")
            proxy["skip-cert-verify"] = True
        tp = r.get("transport", {})
        if tp.get("type") == "ws":
            proxy["network"] = "ws"
            proxy["ws-opts"] = {"path": tp.get("path", "/"), "headers": tp.get("headers", {})}
        elif tp.get("type") == "grpc":
            proxy["network"] = "grpc"
            proxy["grpc-opts"] = {"grpc-service-name": tp.get("service_name", "")}
        elif tp.get("type") == "http":
            proxy["network"] = "h2"
            proxy["h2-opts"] = {"path": tp.get("path", "/"), "host": tp.get("host", [])}
        return proxy

    if t == "vless":
        proxy = {**base, "type": "vless", "uuid": r.get("uuid", ""), "udp": True}
        if r.get("flow"):
            proxy["flow"] = r["flow"]
        tls = r.get("tls", {})
        if tls.get("enabled"):
            proxy["tls"] = True
            proxy["servername"] = tls.get("server_name", "")
            proxy["skip-cert-verify"] = True
            if tls.get("reality"):
                proxy["reality-opts"] = {
                    "public-key": tls["reality"].get("public_key", ""),
                    "short-id": tls["reality"].get("short_id", ""),
                }
            fp = (tls.get("utls") or {}).get("fingerprint")
            if fp:
                proxy["client-fingerprint"] = fp
        tp = r.get("transport", {})
        if tp.get("type") == "ws":
            proxy["network"] = "ws"
            proxy["ws-opts"] = {"path": tp.get("path", "/"), "headers": tp.get("headers", {})}
        elif tp.get("type") == "grpc":
            proxy["network"] = "grpc"
            proxy["grpc-opts"] = {"grpc-service-name": tp.get("service_name", "")}
        elif tp.get("type") == "http":
            proxy["network"] = "h2"
            proxy["h2-opts"] = {"path": tp.get("path", "/"), "host": tp.get("host", [])}
        return proxy

    if t == "trojan":
        proxy = {**base, "type": "trojan", "password": r.get("password", ""),
                 "sni": r.get("tls", {}).get("server_name", n.server),
                 "skip-cert-verify": True, "udp": True}
        tp = r.get("transport", {})
        if tp.get("type") == "ws":
            proxy["network"] = "ws"
            proxy["ws-opts"] = {"path": tp.get("path", "/"), "headers": tp.get("headers", {})}
        elif tp.get("type") == "grpc":
            proxy["network"] = "grpc"
            proxy["grpc-opts"] = {"grpc-service-name": tp.get("service_name", "")}
        elif tp.get("type") == "http":
            proxy["network"] = "h2"
            proxy["h2-opts"] = {"path": tp.get("path", "/"), "host": tp.get("host", [])}
        return proxy

    if t == "shadowsocks":
        return {**base, "type": "ss", "cipher": r.get("method", ""),
                "password": r.get("password", ""), "udp": True}

    if t == "shadowsocksr":
        return {**base, "type": "ssr", "cipher": r.get("method", ""),
                "password": r.get("password", ""),
                "protocol": r.get("protocol", "origin"), "obfs": r.get("obfs", "plain"),
                "obfs-param": r.get("obfs_param", ""), "protocol-param": r.get("protocol_param", "")}

    if t == "hysteria2":
        proxy = {**base, "type": "hysteria2", "password": r.get("password", ""),
                 "sni": r.get("tls", {}).get("server_name", n.server),
                 "skip-cert-verify": True}
        if r.get("obfs"):
            proxy["obfs"] = r["obfs"].get("type", "")
            proxy["obfs-password"] = r["obfs"].get("password", "")
        return proxy

    if t == "hysteria":
        return {**base, "type": "hysteria", "auth-str": r.get("auth_str", ""),
                "up": f"{r.get('up_mbps',10)} Mbps", "down": f"{r.get('down_mbps',50)} Mbps",
                "sni": r.get("tls", {}).get("server_name", n.server), "skip-cert-verify": True}

    if t == "tuic":
        return {**base, "type": "tuic", "uuid": r.get("uuid", ""),
                "password": r.get("password", ""),
                "sni": r.get("tls", {}).get("server_name", n.server),
                "congestion-controller": r.get("congestion_control", "bbr"),
                "alpn": r.get("tls", {}).get("alpn", ["h3"]),
                "skip-cert-verify": True, "udp-relay-mode": "native"}

    if t == "anytls":
        return {**base, "type": "anytls", "password": r.get("password", ""),
                "sni": r.get("tls", {}).get("server_name", n.server),
                "skip-cert-verify": True}

    if t == "socks":
        proxy = {**base, "type": "socks5", "udp": True}
        if r.get("username"):
            proxy["username"] = r["username"]
            proxy["password"] = r.get("password", "")
        return proxy

    if t == "http":
        proxy = {**base, "type": "http"}
        if r.get("username"):
            proxy["username"] = r["username"]
            proxy["password"] = r.get("password", "")
        if r.get("tls", {}).get("enabled"):
            proxy["tls"] = True
            proxy["skip-cert-verify"] = True
        return proxy

    return None


# ============================================================
# 完整文件生成
# ============================================================

def write_outputs(nodes: List[Node], output_dir: str, prefix: str = "nodes"):
    """生成全套订阅文件"""
    import os
    os.makedirs(output_dir, exist_ok=True)

    # 1) URL 列表
    urls = [u for n in nodes if (u := node_to_url(n))]
    with open(f"{output_dir}/{prefix}.urls", "w", encoding="utf-8") as f:
        f.write("\n".join(urls) + "\n")

    # 2) base64 订阅
    b64 = base64.b64encode("\n".join(urls).encode()).decode()
    with open(f"{output_dir}/{prefix}.txt", "w", encoding="utf-8") as f:
        f.write(b64)

    # 3) Clash YAML — 带完整 DNS + 分流规则
    proxies = [p for n in nodes if (p := node_to_clash(n))]
    clash = {
        "mixed-port": 7890,
        "allow-lan": False,
        "mode": "rule",
        "proxies": proxies,
        "proxy-groups": [
            {"name": "🚀 Proxy", "type": "select", "proxies": ["♻️ Auto"] + [p["name"] for p in proxies]},
            {"name": "♻️ Auto", "type": "url-test",
             "proxies": [p["name"] for p in proxies] or ["DIRECT"],
             "url": "https://www.gstatic.com/generate_204", "interval": 300},
        ],
        "dns": {
            "enable": True,
            "enhanced-mode": "fake-ip",
            "fake-ip-range": "198.18.0.1/16",
            "nameserver": ["https://223.5.5.5/dns-query", "https://114.114.114.114/dns-query"],
            "fallback": ["https://1.1.1.1/dns-query", "https://dns.google/dns-query"],
            "fallback-filter": {"geoip": True, "geoip-code": "CN"},
        },
        "rules": [
            "GEOSITE,cn,DIRECT",
            "GEOIP,CN,DIRECT",
            "MATCH,🚀 Proxy",
        ],
    }
    with open(f"{output_dir}/{prefix}.yaml", "w", encoding="utf-8") as f:
        yaml.dump(clash, f, allow_unicode=True, sort_keys=False)

    # 4) sing-box JSON (Karing 直接导入) — 带 DNS + 分流规则
    outbounds_list = [n.tag for n in nodes] or ["direct"]
    singbox = {
        "log": {"level": "info"},
        "dns": {
            "servers": [
                {"tag": "dns-proxy", "address": "https://1.1.1.1/dns-query", "detour": "proxy"},
                {"tag": "dns-direct", "address": "https://223.5.5.5/dns-query", "detour": "direct"},
            ],
            "rules": [
                {"outbound": "any", "server": "dns-direct"},
            ],
            "strategy": "prefer_ipv4",
        },
        "inbounds": [
            {"type": "mixed", "tag": "mixed-in", "listen": "127.0.0.1", "listen_port": 2080},
        ],
        "outbounds": [
            {"type": "selector", "tag": "proxy",
             "outbounds": outbounds_list, "default": nodes[0].tag if nodes else "direct"},
            *[n.to_singbox() for n in nodes],
            {"type": "direct", "tag": "direct"},
        ],
        "route": {
            "rules": [
                {"protocol": "dns", "outbound": "dns-proxy"},
                {"rule_set": "geosite-cn", "outbound": "direct"},
                {"rule_set": "geoip-cn", "outbound": "direct"},
            ],
            "rule_set": [
                {"tag": "geosite-cn", "type": "remote", "format": "binary", "url": "https://raw.githubusercontent.com/SagerNet/sing-geosite/rule-set/geosite-cn.srs", "download_detour": "direct"},
                {"tag": "geoip-cn", "type": "remote", "format": "binary", "url": "https://raw.githubusercontent.com/SagerNet/sing-geoip/rule-set/geoip-cn.srs", "download_detour": "direct"},
            ],
            "final": "proxy",
            "auto_detect_interface": True,
        },
    }
    with open(f"{output_dir}/{prefix}.json", "w", encoding="utf-8") as f:
        json.dump(singbox, f, ensure_ascii=False, indent=2)

    return len(urls)
