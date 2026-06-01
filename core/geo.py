"""
GeoIP 工具：将 server IP 映射为国旗 emoji
轻量实现，适合 GitHub Actions 环境
"""
from __future__ import annotations

import asyncio
import ipaddress
import logging
import re
import socket
from typing import Dict, List, Tuple

import aiohttp

logger = logging.getLogger(__name__)


# 常见 Cloudflare Anycast 节点 IP 段 → 不做映射（无法确定国家）
_CF_PREFIXES = (
    "104.16.", "104.17.", "104.18.", "104.19.", "104.20.", "104.21.",
    "104.22.", "104.23.", "104.24.", "104.25.", "104.26.", "104.27.",
    "172.67.", "172.64.", "172.65.", "172.66.",
    "1.1.1.", "1.0.0.",
    "104.28.", "104.29.", "104.30.", "104.31.",
    "162.159.",
)


def _country_flag(cc: str) -> str:
    """国家代码 → 国旗 emoji（ISO 3166-1 alpha-2）"""
    cc = (cc or "").strip().upper()
    if len(cc) != 2 or not cc.isalpha():
        return ""
    return chr(0x1F1E6 + ord(cc[0]) - ord("A")) + chr(0x1F1E6 + ord(cc[1]) - ord("A"))


def _is_public_ip(ip: str) -> bool:
    try:
        addr = ipaddress.ip_address(ip)
    except ValueError:
        return False
    return addr.is_global


def _is_anycast(ip: str) -> bool:
    return any(ip.startswith(p) for p in _CF_PREFIXES)


async def _resolve_server(server: str, timeout: float = 1.0) -> str:
    try:
        ipaddress.ip_address(server)
        return server
    except ValueError:
        pass
    try:
        loop = asyncio.get_running_loop()
        infos = await asyncio.wait_for(
            loop.getaddrinfo(server, None, family=socket.AF_INET, type=socket.SOCK_STREAM),
            timeout=timeout,
        )
    except Exception as exc:
        logger.debug("DNS resolve failed for %s: %s", server, exc)
        return ""
    for family, _, _, _, sockaddr in infos:
        if family == socket.AF_INET and sockaddr:
            return sockaddr[0]
    return ""


async def _lookup_batch(ips: List[str], timeout: float = 5.0) -> Dict[str, str]:
    """批量查询 ip-api.com（免费版 15 requests/min，batch 每次最多 100 个）。"""
    if not ips:
        return {}
    result: Dict[str, str] = {}
    async with aiohttp.ClientSession() as session:
        # 每批最多 100 个；免费版 15 req/min，保守使用 4.2s 间隔。
        for i in range(0, len(ips), 100):
            if i > 0:
                await asyncio.sleep(4.2)
            batch = ips[i:i + 100]
            body = [{"query": ip, "fields": "countryCode"} for ip in batch]
            for attempt in range(2):
                try:
                    async with session.post(
                        "http://ip-api.com/batch?fields=countryCode",
                        json=body,
                        timeout=aiohttp.ClientTimeout(total=timeout),
                    ) as resp:
                        if resp.status == 429 and attempt == 0:
                            retry_after = int(resp.headers.get("X-Ttl", "60") or 60)
                            logger.warning("ip-api rate limited; retrying after %ss", retry_after)
                            await asyncio.sleep(max(retry_after, 1))
                            continue
                        if resp.status != 200:
                            logger.warning("ip-api batch failed: HTTP %s", resp.status)
                            break
                        items = await resp.json()
                        for item, ip in zip(items, batch):
                            cc = item.get("countryCode", "")
                            if cc:
                                result[ip] = cc
                        break
                except Exception as exc:
                    logger.warning("ip-api batch lookup failed: %s", exc)
                    break
    return result


async def geo_flag_map(nodes, max_queries: int = 100, max_domain_resolves: int = 50) -> Dict[str, str]:
    """
    返回 {server: "🇸🇬"} 的映射。
    IP 直接查询；域名在预算内解析到 IPv4 再查询。Cloudflare Anycast 和非公网 IP 跳过映射。
    """
    direct_ips: List[str] = []
    domains: List[str] = []
    seen_servers = set()
    for n in nodes:
        server = n.server
        if not server or server in seen_servers:
            continue
        seen_servers.add(server)
        try:
            ipaddress.ip_address(server)
            direct_ips.append(server)
        except ValueError:
            domains.append(server)

    resolved_pairs: List[Tuple[str, str]] = [(ip, ip) for ip in direct_ips]
    for i in range(0, min(len(domains), max_domain_resolves), 100):
        chunk = domains[i:i + 100]
        resolved_pairs.extend(zip(chunk, await asyncio.gather(*[_resolve_server(server) for server in chunk])))

    unique_ips: List[str] = []
    seen_ips = set()
    server_to_ip: Dict[str, str] = {}
    for server, ip in resolved_pairs:
        if not ip or not _is_public_ip(ip) or _is_anycast(ip):
            continue
        server_to_ip[server] = ip
        if ip not in seen_ips:
            seen_ips.add(ip)
            unique_ips.append(ip)
            if len(unique_ips) >= max_queries:
                break

    ip2cc = await _lookup_batch(unique_ips)
    return {server: _country_flag(ip2cc[ip]) for server, ip in server_to_ip.items() if ip in ip2cc}


def flag_for_server(server: str, flag_map: Dict[str, str]) -> str:
    """查询单个 server 的国旗 emoji"""
    return flag_map.get(server, "")
