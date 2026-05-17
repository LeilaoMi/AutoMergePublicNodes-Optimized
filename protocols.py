#!/usr/bin/env python3
"""
协议扩展模块
添加对 socks5, tuic, hysteria, wireguard 等协议的支持
"""

import json
from urllib.parse import urlparse, unquote, quote
from typing import Dict, Any, Optional

# 协议类型映射
PROTOCOL_ALIASES = {
    'hy2': 'hysteria2',
    'hy': 'hysteria',
    'socks': 'socks5',
    'socks5h': 'socks5',
}

# 支持的协议列表
SUPPORTED_PROTOCOLS = [
    'vmess', 'vless', 'trojan', 'ss', 'ssr', 
    'hysteria2', 'hysteria', 'socks5', 'tuic', 
    'wireguard', 'http', 'https'
]

# Xray 支持的协议（用于真实代理测试）
XRAY_SUPPORTED = [
    'vmess', 'vless', 'trojan', 'ss', 
    'hysteria2', 'socks5', 'wireguard', 'http'
]

# Clash Meta 支持的协议
CLASH_META_SUPPORTED = [
    'vmess', 'vless', 'trojan', 'ss', 'ssr',
    'hysteria2', 'hysteria', 'socks5', 'tuic', 'wireguard', 'http'
]

# Clash Premium 支持的协议
CLASH_PREMIUM_SUPPORTED = [
    'vmess', 'trojan', 'ss', 'ssr', 'socks5', 'http'
]


def parse_socks5(url: str) -> Dict[str, Any]:
    """解析 socks5:// 链接"""
    parsed = urlparse(url)
    data = {
        'type': 'socks5',
        'name': unquote(parsed.fragment) if parsed.fragment else 'SOCKS5',
        'server': parsed.hostname,
        'port': parsed.port or 1080,
    }
    
    if parsed.username:
        data['username'] = unquote(parsed.username)
    if parsed.password:
        data['password'] = unquote(parsed.password)
    
    # 解析查询参数
    if parsed.query:
        for kv in parsed.query.split('&'):
            if '=' in kv:
                k, v = kv.split('=', 1)
                if k == 'tls':
                    data['tls'] = v == 'true'
                elif k == 'sni':
                    data['sni'] = v
                elif k == 'skip-cert-verify':
                    data['skip-cert-verify'] = v == 'true'
                elif k == 'udp':
                    data['udp'] = v == 'true'
    
    return data


def parse_tuic(url: str) -> Dict[str, Any]:
    """解析 tuic:// 链接 (TUIC v5)"""
    parsed = urlparse(url)
    data = {
        'type': 'tuic',
        'name': unquote(parsed.fragment) if parsed.fragment else 'TUIC',
        'server': parsed.hostname,
        'port': parsed.port or 443,
    }
    
    # TUIC v5 格式: tuic://UUID:PASSWORD@SERVER:PORT?PARAMS#NAME
    if parsed.username:
        data['uuid'] = unquote(parsed.username)
    if parsed.password:
        data['password'] = unquote(parsed.password)
    
    # 解析查询参数
    if parsed.query:
        for kv in parsed.query.split('&'):
            if '=' in kv:
                k, v = kv.split('=', 1)
                if k == 'congestion_control' or k == 'cc':
                    data['congestion-controller'] = v
                elif k == 'alpn':
                    data['alpn'] = v.split(',')
                elif k == 'sni':
                    data['sni'] = v
                elif k == 'disable_sni':
                    data['disable-sni'] = v == 'true'
                elif k == 'skip_cert_verify':
                    data['skip-cert-verify'] = v == 'true'
                elif k == 'udp_relay_mode':
                    data['udp-relay-mode'] = v
                elif k == 'heartbeat_interval':
                    data['heartbeat-interval'] = v
    
    # 默认值
    if 'congestion-controller' not in data:
        data['congestion-controller'] = 'cubic'
    
    return data


def parse_hysteria(url: str) -> Dict[str, Any]:
    """解析 hysteria:// 链接 (Hysteria v1/v2)"""
    parsed = urlparse(url)
    
    # 判断是 hysteria v1 还是 v2
    if parsed.username and '@' in url:
        # hysteria2 格式
        data = {
            'type': 'hysteria2',
            'name': unquote(parsed.fragment) if parsed.fragment else 'Hysteria2',
            'server': parsed.hostname,
            'password': unquote(parsed.username),
        }
        
        # 端口处理
        if ':' in parsed.netloc:
            port_part = parsed.netloc.split(':')[1]
            if ',' in port_part:
                # 端口跳跃
                data['port'], data['ports'] = port_part.split(',', 1)
            else:
                data['port'] = int(port_part) if port_part.isdigit() else 443
        else:
            data['port'] = parsed.port or 443
    else:
        # hysteria v1 格式
        data = {
            'type': 'hysteria',
            'name': unquote(parsed.fragment) if parsed.fragment else 'Hysteria',
            'server': parsed.hostname,
            'port': parsed.port or 443,
        }
        
        if parsed.username:
            data['auth-str'] = unquote(parsed.username)
    
    # 解析查询参数
    if parsed.query:
        for kv in parsed.query.split('&'):
            if '=' in kv:
                k, v = kv.split('=', 1)
                if k == 'upmbps':
                    data['up'] = v
                elif k == 'downmbps':
                    data['down'] = v
                elif k == 'obfs':
                    data['obfs'] = v
                elif k == 'obfsParam' or k == 'obfs-password':
                    data['obfs-password'] = v
                elif k == 'auth':
                    data['auth-str'] = v
                elif k == 'insecure':
                    data['skip-cert-verify'] = v == '1' or v == 'true'
                elif k == 'sni':
                    data['sni'] = v
                elif k == 'alpn':
                    data['alpn'] = v.split(',')
                elif k == 'protocol':
                    data['protocol'] = v
                elif k == 'recv-window-conn':
                    data['recv-window-conn'] = int(v)
                elif k == 'recv-window':
                    data['recv-window'] = int(v)
                elif k == 'ca':
                    data['ca'] = v
                elif k == 'ca-str':
                    data['ca-str'] = v
                elif k == 'disable-mtu-discovery':
                    data['disable-mtu-discovery'] = v == 'true'
                elif k == 'fast-open':
                    data['fast-open'] = v == 'true'
    
    # hysteria2 默认值
    if data.get('type') == 'hysteria2':
        if 'ports' not in data and 'port' not in data:
            data['port'] = 443
    
    return data


def parse_wireguard(url: str) -> Dict[str, Any]:
    """解析 wireguard:// 链接"""
    parsed = urlparse(url)
    data = {
        'type': 'wireguard',
        'name': unquote(parsed.fragment) if parsed.fragment else 'WireGuard',
        'server': parsed.hostname,
        'port': parsed.port or 51820,
    }
    
    # WireGuard 格式: wireguard://PRIVATEKEY@SERVER:PORT?PARAMS#NAME
    if parsed.username:
        data['private-key'] = unquote(parsed.username)
    
    # 解析查询参数
    if parsed.query:
        for kv in parsed.query.split('&'):
            if '=' in kv:
                k, v = kv.split('=', 1)
                if k == 'publicKey' or k == 'public-key':
                    data['peer-public-key'] = v
                elif k == 'presharedKey' or k == 'pre-shared-key':
                    data['pre-shared-key'] = v
                elif k == 'ip' or k == 'local-address':
                    data['local-address'] = v
                elif k == 'dns':
                    data['dns'] = v.split(',')
                elif k == 'mtu':
                    data['mtu'] = int(v)
                elif k == 'udp':
                    data['udp'] = v == 'true'
    
    return data


def parse_http_proxy(url: str, protocol: str = 'http') -> Dict[str, Any]:
    """解析 http(s):// 代理链接"""
    parsed = urlparse(url)
    data = {
        'type': protocol,
        'name': unquote(parsed.fragment) if parsed.fragment else f'{protocol.upper()} Proxy',
        'server': parsed.hostname,
        'port': parsed.port or (443 if protocol == 'https' else 80),
    }
    
    if parsed.username:
        data['username'] = unquote(parsed.username)
    if parsed.password:
        data['password'] = unquote(parsed.password)
    
    if protocol == 'https':
        data['tls'] = True
        if parsed.query:
            for kv in parsed.query.split('&'):
                if '=' in kv:
                    k, v = kv.split('=', 1)
                    if k == 'sni':
                        data['sni'] = v
                    elif k == 'skip-cert-verify':
                        data['skip-cert-verify'] = v == 'true'
    
    return data


def generate_socks5_url(data: Dict[str, Any]) -> str:
    """生成 socks5:// URL"""
    server = data.get('server', '')
    port = data.get('port', 1080)
    name = quote(data.get('name', 'SOCKS5'))
    
    auth = ''
    if 'username' in data:
        auth = quote(data.get('username', ''))
        if 'password' in data:
            auth += ':' + quote(data.get('password', ''))
        auth += '@'
    
    url = f"socks5://{auth}{server}:{port}"
    
    params = []
    if data.get('tls'):
        params.append('tls=true')
    if data.get('sni'):
        params.append(f"sni={data['sni']}")
    if data.get('skip-cert-verify'):
        params.append('skip-cert-verify=true')
    
    if params:
        url += '?' + '&'.join(params)
    
    url += f'#{name}'
    return url


def generate_tuic_url(data: Dict[str, Any]) -> str:
    """生成 tuic:// URL"""
    server = data.get('server', '')
    port = data.get('port', 443)
    uuid = data.get('uuid', '')
    password = data.get('password', '')
    name = quote(data.get('name', 'TUIC'))
    
    auth = f"{quote(uuid)}:{quote(password)}@" if uuid else ''
    
    url = f"tuic://{auth}{server}:{port}?"
    
    params = []
    if data.get('congestion-controller'):
        params.append(f"congestion_control={data['congestion-controller']}")
    if data.get('alpn'):
        params.append(f"alpn={','.join(data['alpn'])}")
    if data.get('sni'):
        params.append(f"sni={data['sni']}")
    if data.get('skip-cert-verify'):
        params.append('skip_cert_verify=true')
    if data.get('udp-relay-mode'):
        params.append(f"udp_relay_mode={data['udp-relay-mode']}")
    
    url += '&'.join(params) + f'#{name}'
    return url


def generate_hysteria_url(data: Dict[str, Any]) -> str:
    """生成 hysteria:// URL"""
    ptype = data.get('type', 'hysteria2')
    server = data.get('server', '')
    port = data.get('port', 443)
    name = quote(data.get('name', 'Hysteria'))
    
    if ptype == 'hysteria2':
        password = data.get('password', '')
        url = f"hysteria2://{quote(password)}@{server}:{port}"
        
        if 'ports' in data:
            url += f",{data['ports']}"
        
        url += '?'
        
        params = []
        if data.get('skip-cert-verify'):
            params.append('insecure=1')
        if data.get('sni'):
            params.append(f"sni={data['sni']}")
        if data.get('obfs'):
            params.append(f"obfs={data['obfs']}")
        if data.get('obfs-password'):
            params.append(f"obfs-password={data['obfs-password']}")
        
        url += '&'.join(params) + f'#{name}'
    else:
        # hysteria v1
        auth = data.get('auth-str', '')
        url = f"hysteria://{quote(auth)}@{server}:{port}?"
        
        params = []
        if data.get('up'):
            params.append(f"upmbps={data['up']}")
        if data.get('down'):
            params.append(f"downmbps={data['down']}")
        if data.get('obfs'):
            params.append(f"obfs={data['obfs']}")
        if data.get('skip-cert-verify'):
            params.append('insecure=1')
        if data.get('sni'):
            params.append(f"sni={data['sni']}")
        if data.get('alpn'):
            params.append(f"alpn={','.join(data['alpn'])}")
        
        url += '&'.join(params) + f'#{name}'
    
    return url


def generate_wireguard_url(data: Dict[str, Any]) -> str:
    """生成 wireguard:// URL"""
    server = data.get('server', '')
    port = data.get('port', 51820)
    private_key = data.get('private-key', '')
    name = quote(data.get('name', 'WireGuard'))
    
    url = f"wireguard://{quote(private_key)}@{server}:{port}?"
    
    params = []
    if data.get('peer-public-key'):
        params.append(f"publicKey={data['peer-public-key']}")
    if data.get('pre-shared-key'):
        params.append(f"presharedKey={data['pre-shared-key']}")
    if data.get('local-address'):
        params.append(f"ip={data['local-address']}")
    if data.get('dns'):
        params.append(f"dns={','.join(data['dns'])}")
    if data.get('mtu'):
        params.append(f"mtu={data['mtu']}")
    
    url += '&'.join(params) + f'#{name}'
    return url


# 协议解析器映射
PROTOCOL_PARSERS = {
    'socks5': parse_socks5,
    'tuic': parse_tuic,
    'hysteria': parse_hysteria,
    'hysteria2': parse_hysteria,  # hysteria2 也用同一个解析器
    'wireguard': parse_wireguard,
    'http': lambda url: parse_http_proxy(url, 'http'),
    'https': lambda url: parse_http_proxy(url, 'https'),
}

# 协议 URL 生成器映射
PROTOCOL_GENERATORS = {
    'socks5': generate_socks5_url,
    'tuic': generate_tuic_url,
    'hysteria': generate_hysteria_url,
    'hysteria2': generate_hysteria_url,
    'wireguard': generate_wireguard_url,
    'http': lambda data: f"http://{quote(data.get('username', ''))}:{quote(data.get('password', ''))}@{data.get('server', '')}:{data.get('port', 80)}#{quote(data.get('name', 'HTTP'))}",
    'https': lambda data: f"https://{quote(data.get('username', ''))}:{quote(data.get('password', ''))}@{data.get('server', '')}:{data.get('port', 443)}#{quote(data.get('name', 'HTTPS'))}",
}


def parse_node_url(url: str) -> Optional[Dict[str, Any]]:
    """解析任意协议的节点 URL"""
    if '://' not in url:
        return None
    
    protocol, _ = url.split('://', 1)
    
    # 处理协议别名
    protocol = PROTOCOL_ALIASES.get(protocol, protocol)
    
    if protocol in PROTOCOL_PARSERS:
        try:
            return PROTOCOL_PARSERS[protocol](url)
        except Exception as e:
            print(f"解析 {protocol} 节点失败: {e}")
            return None
    
    return None


def generate_node_url(data: Dict[str, Any]) -> Optional[str]:
    """生成任意协议的节点 URL"""
    ptype = data.get('type', '')
    
    # 处理协议别名
    ptype = PROTOCOL_ALIASES.get(ptype, ptype)
    
    if ptype in PROTOCOL_GENERATORS:
        try:
            return PROTOCOL_GENERATORS[ptype](data)
        except Exception as e:
            print(f"生成 {ptype} URL 失败: {e}")
            return None
    
    return None


def is_protocol_supported(ptype: str, target: str = 'xray') -> bool:
    """检查协议是否被支持"""
    ptype = PROTOCOL_ALIASES.get(ptype, ptype)
    
    if target == 'xray':
        return ptype in XRAY_SUPPORTED
    elif target == 'clash-meta':
        return ptype in CLASH_META_SUPPORTED
    elif target == 'clash-premium':
        return ptype in CLASH_PREMIUM_SUPPORTED
    elif target == 'clash':
        return ptype in CLASH_PREMIUM_SUPPORTED
    
    return ptype in SUPPORTED_PROTOCOLS
