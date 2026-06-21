"""
节点解析器 - 全协议支持
支持: vmess, vless, trojan, ss, ssr, hysteria, hysteria2, tuic, anytls, socks5, http
所有节点统一输出为 sing-box outbound 格式（Karing 兼容）
"""
from __future__ import annotations

import base64
import json
import logging
import re
import yaml
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional
from urllib.parse import parse_qs, unquote, urlparse


# ============================================================
# 工具函数
# ============================================================

def b64decode(s: str) -> str:
    """容错的 base64 解码"""
    s = s.strip().replace("-", "+").replace("_", "/")
    pad = (-len(s)) % 4
    s = s + "=" * pad
    try:
        return base64.b64decode(s).decode("utf-8", errors="replace")
    except Exception:
        return ""


def is_b64(s: str) -> bool:
    s = s.strip()
    if len(s) < 16:
        return False
    if not re.fullmatch(r"[A-Za-z0-9+/=\-_\s]+", s):
        return False
    decoded = b64decode(s)
    return "://" in decoded or "proxies:" in decoded


# ============================================================
# 统一节点模型 (sing-box outbound 格式)
# ============================================================

logger = logging.getLogger(__name__)


@dataclass
class Node:
    """统一节点格式 (sing-box outbound)"""
    type: str                  # 协议类型
    tag: str                   # 节点名称
    server: str                # 服务器地址
    server_port: int           # 端口
    raw: Dict[str, Any] = field(default_factory=dict)  # sing-box 完整 outbound

    def fingerprint(self) -> str:
        """节点指纹（用于去重）"""
        return f"{self.type}|{self.server}|{self.server_port}|{self._key()}"

    def _key(self) -> str:
        r = self.raw
        if self.type in ("vmess", "vless"):
            return r.get("uuid", "")
        if self.type in ("trojan", "shadowsocks", "hysteria", "hysteria2", "tuic"):
            return r.get("password", "") or r.get("uuid", "")
        return ""

    def to_singbox(self) -> Dict[str, Any]:
        out = dict(self.raw)
        out["type"] = self.type
        out["tag"] = self.tag
        out["server"] = self.server
        out["server_port"] = int(self.server_port)
        return out


class ParseError(Exception):
    pass


# ============================================================
# URL 解析器（各协议）
# ============================================================

def _name(parsed) -> str:
    if parsed.fragment:
        return unquote(parsed.fragment)
    return ""


def parse_vmess(url: str) -> Optional[Node]:
    """vmess://base64({...})"""
    body = url[len("vmess://"):]
    decoded = b64decode(body)
    if not decoded.startswith("{"):
        return None
    try:
        v = json.loads(decoded)
    except Exception:
        return None

    server = v.get("add", "")
    port = int(v.get("port", 0) or 0)
    if not server or not port:
        return None

    raw = {
        "uuid": v.get("id", ""),
        "security": (v.get("scy") or v.get("type", "auto") or "auto"),
        "alter_id": int(v.get("aid", 0) or 0),
    }
    if v.get("tls"):
        raw["tls"] = {
            "enabled": True,
            "server_name": v.get("sni") or v.get("host") or server,
            "insecure": True,
        }
    net = v.get("net", "tcp")
    if net == "ws":
        raw["transport"] = {
            "type": "ws",
            "path": v.get("path", "/"),
            "headers": {"Host": v.get("host", "")} if v.get("host") else {},
        }
    elif net == "grpc":
        raw["transport"] = {"type": "grpc", "service_name": v.get("path", "")}
    elif net == "h2":
        raw["transport"] = {"type": "http", "host": [v.get("host", server)], "path": v.get("path", "/")}

    return Node("vmess", v.get("ps") or f"vmess-{server}", server, port, raw)


def parse_vless(url: str) -> Optional[Node]:
    """vless://uuid@host:port?params#name"""
    p = urlparse(url)
    if not p.hostname or not p.port:
        return None
    q = parse_qs(p.query)
    raw: Dict[str, Any] = {"uuid": unquote(p.username or "")}

    sec = (q.get("security", [""])[0]).lower()
    sni = q.get("sni", [""])[0] or q.get("peer", [""])[0] or p.hostname
    flow = q.get("flow", [""])[0]
    if flow:
        raw["flow"] = flow

    if sec in ("tls", "reality", "xtls"):
        tls: Dict[str, Any] = {"enabled": True, "server_name": sni, "insecure": True}
        if sec == "reality":
            tls["reality"] = {
                "enabled": True,
                "public_key": q.get("pbk", [""])[0],
                "short_id": q.get("sid", [""])[0],
            }
            fp = q.get("fp", [""])[0]
            if fp:
                tls["utls"] = {"enabled": True, "fingerprint": fp}
        raw["tls"] = tls

    net = (q.get("type", ["tcp"])[0] or "tcp").lower()
    if net == "ws":
        raw["transport"] = {
            "type": "ws",
            "path": q.get("path", ["/"])[0],
            "headers": {"Host": q.get("host", [""])[0]} if q.get("host", [""])[0] else {},
        }
    elif net == "grpc":
        raw["transport"] = {"type": "grpc", "service_name": q.get("serviceName", [""])[0]}
    elif net == "http":
        raw["transport"] = {"type": "http", "host": [q.get("host", [p.hostname])[0]], "path": q.get("path", ["/"])[0]}

    return Node("vless", _name(p) or f"vless-{p.hostname}", p.hostname, p.port, raw)


def parse_trojan(url: str) -> Optional[Node]:
    """trojan://password@host:port?params#name"""
    p = urlparse(url)
    if not p.hostname or not p.port:
        return None
    q = parse_qs(p.query)
    sni = q.get("sni", [""])[0] or q.get("peer", [""])[0] or p.hostname
    raw: Dict[str, Any] = {
        "password": unquote(p.username or ""),
        "tls": {"enabled": True, "server_name": sni, "insecure": True},
    }
    net = (q.get("type", ["tcp"])[0] or "tcp").lower()
    if net == "ws":
        raw["transport"] = {
            "type": "ws",
            "path": q.get("path", ["/"])[0],
            "headers": {"Host": q.get("host", [""])[0]} if q.get("host", [""])[0] else {},
        }
    elif net == "grpc":
        raw["transport"] = {"type": "grpc", "service_name": q.get("serviceName", [""])[0]}
    return Node("trojan", _name(p) or f"trojan-{p.hostname}", p.hostname, p.port, raw)


def parse_ss(url: str) -> Optional[Node]:
    """ss://base64(method:password)@host:port#name 或 ss://base64(method:password@host:port)#name"""
    body = url[len("ss://"):]
    name = ""
    if "#" in body:
        body, name = body.split("#", 1)
        name = unquote(name)
    plugin = ""
    if "?" in body:
        body, query = body.split("?", 1)
        q = parse_qs(query)
        if "plugin" in q:
            plugin = unquote(q["plugin"][0])

    if "@" in body:
        userinfo, hostport = body.rsplit("@", 1)
        userinfo_dec = b64decode(userinfo) if not (":" in userinfo and not is_b64(userinfo)) else userinfo
        if ":" not in userinfo_dec:
            userinfo_dec = b64decode(userinfo)
        if ":" not in userinfo_dec:
            return None
        method, password = userinfo_dec.split(":", 1)
    else:
        decoded = b64decode(body)
        if "@" not in decoded or ":" not in decoded:
            return None
        userinfo, hostport = decoded.rsplit("@", 1)
        if ":" not in userinfo:
            return None
        method, password = userinfo.split(":", 1)

    # 处理 IPv6
    if hostport.startswith("["):
        m = re.match(r"\[([^\]]+)\]:(\d+)", hostport)
        if not m:
            return None
        host, port = m.group(1), int(m.group(2))
    else:
        if hostport.count(":") != 1:
            return None
        host, port = hostport.rsplit(":", 1)
        port = int(port)

    raw: Dict[str, Any] = {"method": method, "password": password}
    if plugin:
        raw["plugin"] = plugin.split(";", 1)[0]
        if ";" in plugin:
            raw["plugin_opts"] = plugin.split(";", 1)[1]
    return Node("shadowsocks", name or f"ss-{host}", host, port, raw)


def parse_ssr(url: str) -> Optional[Node]:
    """ssr://base64(host:port:protocol:method:obfs:base64(password)/?params)"""
    body = url[len("ssr://"):]
    decoded = b64decode(body)
    if "/?" not in decoded:
        return None
    head, query = decoded.split("/?", 1)
    parts = head.split(":")
    if len(parts) != 6:
        return None
    host, port, protocol, method, obfs, password_b64 = parts
    password = b64decode(password_b64)
    q = parse_qs(query)
    name = b64decode(q.get("remarks", [""])[0]) if q.get("remarks") else ""
    raw = {
        "method": method,
        "password": password,
        "protocol": protocol,
        "obfs": obfs,
    }
    if q.get("obfsparam"):
        raw["obfs_param"] = b64decode(q["obfsparam"][0])
    if q.get("protoparam"):
        raw["protocol_param"] = b64decode(q["protoparam"][0])
    # sing-box 用 shadowsocksr type
    return Node("shadowsocksr", name or f"ssr-{host}", host, int(port), raw)


def parse_hysteria2(url: str) -> Optional[Node]:
    """hysteria2://auth@host:port?params#name"""
    p = urlparse(url)
    if not p.hostname or not p.port:
        return None
    q = parse_qs(p.query)
    raw: Dict[str, Any] = {
        "password": unquote(p.username or "") or q.get("auth", [""])[0],
        "tls": {
            "enabled": True,
            "server_name": q.get("sni", [p.hostname])[0],
            "insecure": str(q.get("insecure", ["1"])[0]).lower() in ("1", "true"),
        },
    }
    if q.get("obfs", [""])[0]:
        raw["obfs"] = {"type": q["obfs"][0], "password": q.get("obfs-password", [""])[0]}
    return Node("hysteria2", _name(p) or f"hy2-{p.hostname}", p.hostname, p.port, raw)


def parse_hysteria(url: str) -> Optional[Node]:
    """hysteria://host:port?params#name"""
    p = urlparse(url)
    if not p.hostname or not p.port:
        return None
    q = parse_qs(p.query)
    raw: Dict[str, Any] = {
        "auth_str": q.get("auth", [""])[0] or unquote(p.username or ""),
        "up_mbps": int(q.get("upmbps", ["10"])[0]),
        "down_mbps": int(q.get("downmbps", ["50"])[0]),
        "tls": {"enabled": True, "server_name": q.get("peer", [p.hostname])[0], "insecure": True},
    }
    if q.get("obfs", [""])[0]:
        raw["obfs"] = q["obfs"][0]
    return Node("hysteria", _name(p) or f"hy-{p.hostname}", p.hostname, p.port, raw)


def parse_tuic(url: str) -> Optional[Node]:
    """tuic://uuid:password@host:port?params#name"""
    p = urlparse(url)
    if not p.hostname or not p.port:
        return None
    userinfo = unquote(p.username or "")
    password = unquote(p.password or "")
    if not password and ":" in userinfo:
        userinfo, password = userinfo.split(":", 1)
    q = parse_qs(p.query)
    raw: Dict[str, Any] = {
        "uuid": userinfo,
        "password": password,
        "congestion_control": q.get("congestion_control", ["bbr"])[0],
        "tls": {
            "enabled": True,
            "server_name": q.get("sni", [p.hostname])[0],
            "alpn": q.get("alpn", ["h3"])[0].split(","),
            "insecure": True,
        },
    }
    return Node("tuic", _name(p) or f"tuic-{p.hostname}", p.hostname, p.port, raw)


def parse_anytls(url: str) -> Optional[Node]:
    """anytls://password@host:port?sni=...#name"""
    p = urlparse(url)
    if not p.hostname or not p.port:
        return None
    q = parse_qs(p.query)
    raw: Dict[str, Any] = {
        "password": unquote(p.username or ""),
        "tls": {
            "enabled": True,
            "server_name": q.get("sni", [p.hostname])[0],
            "insecure": True,
        },
    }
    return Node("anytls", _name(p) or f"anytls-{p.hostname}", p.hostname, p.port, raw)


def parse_socks(url: str) -> Optional[Node]:
    """socks5://[user:pass@]host:port#name 或 socks://"""
    p = urlparse(url)
    if not p.hostname or not p.port:
        return None
    raw: Dict[str, Any] = {"version": "5"}
    if p.username:
        raw["username"] = unquote(p.username)
        raw["password"] = unquote(p.password or "")
    return Node("socks", _name(p) or f"socks-{p.hostname}", p.hostname, p.port, raw)


def parse_http(url: str) -> Optional[Node]:
    """http://user:pass@host:port#name 或 https://"""
    p = urlparse(url)
    if not p.hostname or not p.port:
        return None
    raw: Dict[str, Any] = {}
    if p.username:
        raw["username"] = unquote(p.username)
        raw["password"] = unquote(p.password or "")
    if p.scheme == "https":
        raw["tls"] = {"enabled": True, "server_name": p.hostname, "insecure": True}
    return Node("http", _name(p) or f"http-{p.hostname}", p.hostname, p.port, raw)


# ============================================================
# Clash YAML 节点 → Node
# ============================================================

def parse_clash_proxy(p: Dict[str, Any]) -> Optional[Node]:
    """从 Clash YAML proxy dict 创建 Node"""
    ptype = p.get("type", "").lower()
    server = p.get("server", "")
    port = int(p.get("port", 0) or 0)
    name = p.get("name", "") or f"{ptype}-{server}"
    if not server or not port:
        return None

    if ptype == "vmess":
        raw = {
            "uuid": p.get("uuid", ""),
            "security": p.get("cipher", "auto"),
            "alter_id": int(p.get("alterId", 0) or 0),
        }
        if p.get("tls"):
            raw["tls"] = {
                "enabled": True,
                "server_name": p.get("servername", server),
                "insecure": p.get("skip-cert-verify", True),
            }
        net = p.get("network", "tcp")
        if net == "ws":
            ws = p.get("ws-opts", {}) or {}
            raw["transport"] = {
                "type": "ws",
                "path": ws.get("path", "/"),
                "headers": ws.get("headers", {}),
            }
        elif net == "grpc":
            g = p.get("grpc-opts", {}) or {}
            raw["transport"] = {"type": "grpc", "service_name": g.get("grpc-service-name", "")}
        return Node("vmess", name, server, port, raw)

    if ptype == "vless":
        raw = {"uuid": p.get("uuid", "")}
        if p.get("flow"):
            raw["flow"] = p["flow"]
        if p.get("tls") or p.get("reality-opts"):
            tls = {
                "enabled": True,
                "server_name": p.get("servername", server),
                "insecure": p.get("skip-cert-verify", True),
            }
            r = p.get("reality-opts", {}) or {}
            if r:
                tls["reality"] = {
                    "enabled": True,
                    "public_key": r.get("public-key", ""),
                    "short_id": r.get("short-id", ""),
                }
            raw["tls"] = tls
        net = p.get("network", "tcp")
        if net == "ws":
            ws = p.get("ws-opts", {}) or {}
            raw["transport"] = {"type": "ws", "path": ws.get("path", "/"), "headers": ws.get("headers", {})}
        elif net == "grpc":
            g = p.get("grpc-opts", {}) or {}
            raw["transport"] = {"type": "grpc", "service_name": g.get("grpc-service-name", "")}
        return Node("vless", name, server, port, raw)

    if ptype == "trojan":
        raw = {
            "password": p.get("password", ""),
            "tls": {
                "enabled": True,
                "server_name": p.get("sni", server),
                "insecure": p.get("skip-cert-verify", True),
            },
        }
        net = p.get("network", "tcp")
        if net == "ws":
            ws = p.get("ws-opts", {}) or {}
            raw["transport"] = {"type": "ws", "path": ws.get("path", "/"), "headers": ws.get("headers", {})}
        elif net == "grpc":
            g = p.get("grpc-opts", {}) or {}
            raw["transport"] = {"type": "grpc", "service_name": g.get("grpc-service-name", "")}
        return Node("trojan", name, server, port, raw)

    if ptype in ("ss", "shadowsocks"):
        raw = {"method": p.get("cipher", "aes-128-gcm"), "password": p.get("password", "")}
        return Node("shadowsocks", name, server, port, raw)

    if ptype in ("ssr", "shadowsocksr"):
        raw = {
            "method": p.get("cipher", ""),
            "password": p.get("password", ""),
            "protocol": p.get("protocol", "origin"),
            "obfs": p.get("obfs", "plain"),
        }
        if p.get("protocol-param"):
            raw["protocol_param"] = p["protocol-param"]
        if p.get("obfs-param"):
            raw["obfs_param"] = p["obfs-param"]
        return Node("shadowsocksr", name, server, port, raw)

    if ptype == "hysteria2":
        raw = {
            "password": p.get("password", "") or p.get("auth", ""),
            "tls": {"enabled": True, "server_name": p.get("sni", server), "insecure": True},
        }
        if p.get("obfs"):
            raw["obfs"] = {"type": p["obfs"], "password": p.get("obfs-password", "")}
        return Node("hysteria2", name, server, port, raw)

    if ptype == "hysteria":
        raw = {
            "auth_str": p.get("auth-str", "") or p.get("auth_str", ""),
            "up_mbps": int(p.get("up", "10").split()[0] if isinstance(p.get("up"), str) else p.get("up", 10)),
            "down_mbps": int(p.get("down", "50").split()[0] if isinstance(p.get("down"), str) else p.get("down", 50)),
            "tls": {"enabled": True, "server_name": p.get("sni", server), "insecure": True},
        }
        return Node("hysteria", name, server, port, raw)

    if ptype == "tuic":
        raw = {
            "uuid": p.get("uuid", ""),
            "password": p.get("password", ""),
            "congestion_control": p.get("congestion-controller", "bbr"),
            "tls": {
                "enabled": True,
                "server_name": p.get("sni", server),
                "alpn": p.get("alpn", ["h3"]),
                "insecure": True,
            },
        }
        return Node("tuic", name, server, port, raw)

    if ptype == "anytls":
        raw = {
            "password": p.get("password", ""),
            "tls": {"enabled": True, "server_name": p.get("sni", server), "insecure": True},
        }
        return Node("anytls", name, server, port, raw)

    if ptype in ("socks", "socks5"):
        raw = {"version": "5"}
        if p.get("username"):
            raw["username"] = p["username"]
            raw["password"] = p.get("password", "")
        return Node("socks", name, server, port, raw)

    if ptype in ("http", "https"):
        raw: Dict[str, Any] = {}
        if p.get("username"):
            raw["username"] = p["username"]
            raw["password"] = p.get("password", "")
        if ptype == "https" or p.get("tls"):
            raw["tls"] = {"enabled": True, "server_name": server, "insecure": True}
        return Node("http", name, server, port, raw)

    return None


# ============================================================
# 统一入口
# ============================================================

URL_PARSERS = {
    "vmess": parse_vmess,
    "vless": parse_vless,
    "trojan": parse_trojan,
    "ss": parse_ss,
    "ssr": parse_ssr,
    "hysteria": parse_hysteria,
    "hy": parse_hysteria,
    "hysteria2": parse_hysteria2,
    "hy2": parse_hysteria2,
    "tuic": parse_tuic,
    "anytls": parse_anytls,
    "socks5": parse_socks,
    "socks": parse_socks,
    "http": parse_http,
    "https": parse_http,
}


def parse_url(url: str, errors: List[str] | None = None) -> Optional[Node]:
    """解析单个节点 URL"""
    url = url.strip()
    if "://" not in url:
        return None
    scheme = url.split("://", 1)[0].lower()
    parser = URL_PARSERS.get(scheme)
    if not parser:
        return None
    try:
        return parser(url)
    except Exception as exc:
        if errors is not None:
            errors.append(f"{scheme}: {type(exc).__name__}: {exc}")
        return None


# 解析时遇到 base64 / 普通文本, 单条源最大的可解析字节数
# 防止恶意源喂几 GB payload 吃光内存 (mheidari-all 单源 4MB 已经接近临界)
MAX_PARSE_BYTES = 10 * 1024 * 1024


def parse_content(text: str) -> List[Node]:
    """从订阅内容中提取所有节点（自动识别格式）"""
    text = text.strip()
    if not text:
        return []

    # §2.3 防止恶意大文件把整篇 base64 一次性 decode 到内存
    if len(text) > MAX_PARSE_BYTES:
        logger.warning("parse_content: input too large (%d bytes), truncate to %d", len(text), MAX_PARSE_BYTES)
        text = text[:MAX_PARSE_BYTES]

    nodes: List[Node] = []

    # 1) YAML (Clash)
    if "proxies:" in text[:2000] or text.startswith("proxies:"):
        try:
            data = yaml.safe_load(text)
            if isinstance(data, dict) and isinstance(data.get("proxies"), list):
                for p in data["proxies"]:
                    if isinstance(p, dict):
                        n = parse_clash_proxy(p)
                        if n:
                            nodes.append(n)
                if nodes:
                    return nodes
        except Exception:
            pass

    # 2) Base64 编码的订阅。忽略注释行后再判断，避免注释前缀导致整段漏解析。
    content_lines = [line.strip() for line in text.splitlines() if line.strip() and not line.lstrip().startswith("#")]
    candidate = "".join(content_lines)
    if "://" not in text[:200] and is_b64(candidate):
        decoded = b64decode(candidate)
        if "://" in decoded or "proxies:" in decoded:
            text = decoded

    # 3) 纯文本：逐行匹配 URL
    url_re = re.compile(r"(?<![A-Za-z0-9+.-])(vmess|vless|trojan|ssr|ss|hysteria2|hy2|hysteria|hy|tuic|anytls|socks5|socks|https?)://[^\s<>'\"]+")
    parse_errors: List[str] = []
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        for match in url_re.finditer(line):
            url = match.group(0).strip("'\",;")
            n = parse_url(url, parse_errors)
            if n:
                nodes.append(n)

    if parse_errors:
        logger.warning("skipped %d invalid node URLs while parsing subscription content", len(parse_errors))
    return nodes
