"""
[v3.0] 安全防御网关 (Security Guard)
针对公开订阅源（尤其是 TG 频道）的防投毒与 SSRF 防御。
在节点解析与测试阶段，拦截恶意载荷，保护 CI 运行环境。
"""
from __future__ import annotations
import ipaddress
from typing import Optional
from urllib.parse import urlparse

# 危险 IP 列表：云厂商元数据服务、本地环回、链路本地
DANGEROUS_IPS = {
    "169.254.169.254",  # AWS/GCP/Azure 元数据服务
    "100.100.100.200",  # 阿里云元数据服务
    "127.0.0.1",
    "::1",
}

# 危险域名后缀
DANGEROUS_DOMAINS = {
    "metadata.google.internal",
    "metadata.internal",
}

def _is_private_ip(ip_str: str) -> bool:
    """检查是否为 RFC1918 私有地址或保留地址"""
    try:
        ip = ipaddress.ip_address(ip_str)
        return ip.is_private or ip.is_loopback or ip.is_link_local or ip.is_reserved
    except ValueError:
        return False

def check_ssrf_risk(target: str) -> Optional[str]:
    """
    校验目标地址是否存在 SSRF 风险。
    返回 None 表示安全，返回字符串表示风险原因。
    """
    if not target:
        return None

    # 1. 纯 IP 校验
    if _is_private_ip(target) or target in DANGEROUS_IPS:
        return f"Blocked dangerous IP: {target}"

    # 2. URL/Domain 校验
    try:
        parsed = urlparse(target if "://" in target else f"http://{target}")
        hostname = parsed.hostname or ""
        
        if not hostname:
            return None
            
        hostname_lower = hostname.lower()
        
        # 拦截元数据域名
        for domain in DANGEROUS_DOMAINS:
            if hostname_lower == domain or hostname_lower.endswith(f".{domain}"):
                return f"Blocked metadata domain: {hostname}"
                
        # 拦截解析后为私有 IP 的域名 (基础防御)
        if _is_private_ip(hostname) or hostname in DANGEROUS_IPS:
            return f"Blocked private IP in URL: {hostname}"
            
        # 拦截包含特殊字符或明显畸形的域名
        if ".." in hostname or hostname.startswith("-"):
            return f"Blocked malformed domain: {hostname}"
            
    except Exception:
        return f"Blocked unparseable target: {target}"

    return None
