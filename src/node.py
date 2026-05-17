#!/usr/bin/env python3
"""
节点模型 - 优化版
支持 vmess, ss, ssr, trojan, vless, hysteria2 协议
"""
from dataclasses import dataclass, field
from typing import Dict, Any, Optional, Set, List
from enum import Enum
from urllib.parse import quote, unquote
import json
import base64
import re
import hashlib


class Protocol(Enum):
    VMESS = "vmess"
    SS = "ss"
    SSR = "ssr"
    TROJAN = "trojan"
    VLESS = "vless"
    HYSTERIA2 = "hysteria2"


# Clash 支持的加密方式
CLASH_CIPHER_VMESS = {"auto", "aes-128-gcm", "chacha20-poly1305", "none"}
CLASH_CIPHER_SS = {
    "aes-128-gcm", "aes-192-gcm", "aes-256-gcm",
    "aes-128-cfb", "aes-192-cfb", "aes-256-cfb",
    "aes-128-ctr", "aes-192-ctr", "aes-256-ctr",
    "rc4-md5", "chacha20-ietf", "xchacha20",
    "chacha20-ietf-poly1305", "xchacha20-ietf-poly1305"
}
CLASH_SSR_OBFS = {"plain", "http_simple", "http_post", "random_head", 
                  "tls1.2_ticket_auth", "tls1.2_ticket_fastauth"}
CLASH_SSR_PROTOCOL = {"origin", "auth_sha1_v4", "auth_aes128_md5", 
                      "auth_aes128_sha1", "auth_chain_a", "auth_chain_b"}

DEFAULT_UUID = '8'*8 + '-8888'*3 + '-' + '8'*12


def b64decode(s: str) -> str:
    """Base64 解码，自动补齐填充"""
    s = s + '=' * ((4 - len(s) % 4) % 4)
    try:
        return base64.urlsafe_b64decode(s.encode()).decode('utf-8')
    except:
        return base64.b64decode(s.encode()).decode('utf-8')


def b64encode(s: str) -> str:
    """Base64 编码"""
    return base64.b64encode(s.encode('utf-8')).decode('utf-8')


@dataclass
class Node:
    """代理节点"""
    name: str
    server: str
    port: int
    protocol: Protocol
    data: Dict[str, Any] = field(default_factory=dict)
    
    # 缓存
    _url: Optional[str] = field(default=None, repr=False, compare=False)
    _hash: Optional[int] = field(default=None, repr=False, compare=False)
    _is_fake: bool = field(default=False, repr=False)
    
    @classmethod
    def from_url(cls, url: str) -> "Node":
        """从 URL 解析节点"""
        url = url.strip()
        if not url or "://" not in url:
            raise ValueError(f"Invalid URL: {url[:50]}...")
        
        # 处理协议类型
        proto_part, data_part = url.split("://", 1)
        proto_str = ''.join(c for c in proto_part if c.isascii())
        if proto_str == "hy2":
            proto_str = "hysteria2"
        
        try:
            protocol = Protocol(proto_str.lower())
        except ValueError:
            raise ValueError(f"Unsupported protocol: {proto_str}")
        
        parser = PARSERS.get(protocol)
        if not parser:
            raise ValueError(f"No parser for: {protocol}")
        
        data = parser(data_part)
        data['type'] = protocol.value
        
        return cls(
            name=data.get('name', 'unnamed'),
            server=data['server'],
            port=data['port'],
            protocol=protocol,
            data=data
        )
    
    @classmethod
    def from_clash(cls, data: Dict[str, Any]) -> "Node":
        """从 Clash 格式创建节点"""
        proto_str = data.get('type', '')
        try:
            protocol = Protocol(proto_str)
        except ValueError:
            raise ValueError(f"Unsupported protocol: {proto_str}")
        
        return cls(
            name=data.get('name', 'unnamed'),
            server=data['server'],
            port=data['port'],
            protocol=protocol,
            data=data
        )
    
    @property
    def url(self) -> str:
        """生成 URL"""
        if self._url is None:
            generator = GENERATORS.get(self.protocol)
            if not generator:
                raise ValueError(f"No generator for: {self.protocol}")
            self._url = generator(self.data)
        return self._url
    
    def __hash__(self) -> int:
        """节点去重哈希"""
        if self._hash is None:
            # 基于关键参数生成哈希
            key_parts = [
                self.protocol.value,
                self.server,
                str(self.port)
            ]
            
            # 添加协议特定参数
            for k in ['uuid', 'password', 'obfs', 'protocol']:
                if k in self.data:
                    key_parts.append(str(self.data[k]))
            
            key = ':'.join(key_parts)
            self._hash = hash(key)
        return self._hash
    
    def __eq__(self, other) -> bool:
        if isinstance(other, Node):
            return hash(self) == hash(other)
        return False
    
    @property
    def clash_data(self) -> Dict[str, Any]:
        """生成 Clash 格式数据"""
        ret = self.data.copy()
        
        # 处理数字密码
        if 'password' in ret and str(ret['password']).isdigit():
            ret['password'] = '!!str ' + str(ret['password'])
        
        # 清理不需要的字段
        ret.pop('group', None)
        
        # 默认加密方式
        if 'cipher' in ret and not ret['cipher']:
            ret['cipher'] = 'auto'
        
        # 处理 flow 后缀
        if self.protocol == Protocol.VLESS and 'flow' in ret:
            flow = ret['flow']
            if flow.endswith('-udp443'):
                ret['flow'] = flow[:-7]
            elif flow.endswith('!'):
                ret['flow'] = flow[:-1]
        
        # 处理 alpn 字符串
        if 'alpn' in ret and isinstance(ret['alpn'], str):
            ret['alpn'] = ret['alpn'].replace(' ', '').split(',')
        
        return ret
    
    def supports_clash(self) -> bool:
        """是否支持 Clash（非 Meta）"""
        if self.protocol == Protocol.VLESS:
            return False
        
        if self.protocol in (Protocol.VMESS, Protocol.SS, Protocol.SSR):
            cipher = self.data.get('cipher', 'auto')
            if cipher and cipher not in (CLASH_CIPHER_VMESS if self.protocol == Protocol.VMESS else CLASH_CIPHER_SS):
                return False
            
            if self.protocol == Protocol.SSR:
                obfs = self.data.get('obfs', 'plain')
                protocol = self.data.get('protocol', 'origin')
                if obfs not in CLASH_SSR_OBFS or protocol not in CLASH_SSR_PROTOCOL:
                    return False
        
        return True
    
    def supports_meta(self) -> bool:
        """是否支持 Clash Meta"""
        return True  # Meta 支持所有协议


# ========== 协议解析器 ==========

def parse_vmess(data_str: str) -> Dict[str, Any]:
    """解析 vmess:// 协议"""
    try:
        v = json.loads(b64decode(data_str))
    except:
        raise ValueError("Invalid vmess data")
    
    data = {
        'name': v.get('ps', 'unnamed'),
        'server': v.get('add', '0.0.0.0'),
        'port': int(v.get('port', 0)),
        'uuid': v.get('id', DEFAULT_UUID),
        'alterId': int(v.get('aid', 0)),
        'cipher': v.get('scy', 'auto'),
        'tls': v.get('tls', '') == 'tls'
    }
    
    # 网络设置
    net = v.get('net', 'tcp')
    if net:
        data['network'] = net
    
    if net == 'ws':
        opts = {}
        if 'path' in v:
            opts['path'] = v['path']
        if 'host' in v:
            opts['headers'] = {'Host': v['host']}
        data['ws-opts'] = opts
    elif net == 'h2':
        opts = {}
        if 'path' in v:
            opts['path'] = v['path']
        if 'host' in v:
            opts['host'] = v['host'].split(',')
        data['h2-opts'] = opts
    elif net == 'grpc' and 'path' in v:
        data['grpc-opts'] = {'grpc-service-name': v['path']}
    
    # SNI
    if 'sni' in v:
        data['servername'] = v['sni']
    elif 'host' in v:
        data['servername'] = v['host']
    
    return data


def parse_ss(data_str: str) -> Dict[str, Any]:
    """解析 ss:// 协议"""
    data = {'name': 'unnamed'}
    
    # 格式: method:password@server:port#name 或 base64@server:port#name
    if '@' in data_str:
        info = data_str.split('@')
        userinfo = info[0]
        server_part = '@'.join(info[1:])
        
        # 解析服务器部分
        if '#' in server_part:
            server_part, name = server_part.rsplit('#', 1)
            data['name'] = unquote(name)
        
        if ':' in server_part:
            server, port = server_part.rsplit(':', 1)
            data['server'] = server
            data['port'] = int(port)
        
        # 解析用户信息
        if ':' in userinfo:
            method, password = userinfo.split(':', 1)
            data['cipher'] = method
            data['password'] = password
        else:
            # Base64 编码
            try:
                decoded = b64decode(userinfo)
                if ':' in decoded:
                    method, password = decoded.split(':', 1)
                    data['cipher'] = method
                    data['password'] = password
            except:
                pass
    
    # 插件
    if 'plugin=' in data_str:
        plugin_match = re.search(r'plugin=([^;#]+)', data_str)
        if plugin_match:
            data['plugin'] = plugin_match.group(1)
            plugin_opts = {}
            for opt in re.findall(r'(\w+)=([^;#]+)', data_str):
                if opt[0] != 'plugin':
                    plugin_opts[opt[0]] = opt[1]
            if plugin_opts:
                data['plugin-opts'] = plugin_opts
    
    return data


def parse_ssr(data_str: str) -> Dict[str, Any]:
    """解析 ssr:// 协议"""
    try:
        decoded = b64decode(data_str)
    except:
        raise ValueError("Invalid ssr data")
    
    # 格式: server:port:protocol:method:obfs:password_base64/?params
    parts = decoded.split('/?', 1)
    main_part = parts[0]
    params = parts[1] if len(parts) > 1 else ''
    
    fields = main_part.split(':')
    if len(fields) < 6:
        raise ValueError("Invalid ssr format")
    
    data = {
        'server': fields[0],
        'port': int(fields[1]),
        'protocol': fields[2],
        'cipher': fields[3],
        'obfs': fields[4],
        'password': b64decode(fields[5]),
        'name': 'unnamed'
    }
    
    # 解析参数
    if params:
        for param in params.split('&'):
            if '=' in param:
                key, value = param.split('=', 1)
                if key == 'remarks':
                    data['name'] = b64decode(value)
                elif key == 'obfsparam':
                    data['obfs-param'] = b64decode(value)
                elif key == 'protoparam':
                    data['protocol-param'] = b64decode(value)
    
    return data


def parse_trojan(data_str: str) -> Dict[str, Any]:
    """解析 trojan:// 协议"""
    # 格式: password@server:port?sni=xxx&type=tcp#name
    data = {'name': 'unnamed'}
    
    if '#' in data_str:
        data_str, name = data_str.rsplit('#', 1)
        data['name'] = unquote(name)
    
    if '?' in data_str:
        main_part, params_str = data_str.split('?', 1)
    else:
        main_part = data_str
        params_str = ''
    
    # 解析主部分
    if '@' in main_part:
        password, server_part = main_part.split('@', 1)
        data['password'] = unquote(password)
        
        if ':' in server_part:
            server, port = server_part.rsplit(':', 1)
            data['server'] = server
            data['port'] = int(port)
    
    # 解析参数
    if params_str:
        params = {}
        for param in params_str.split('&'):
            if '=' in param:
                key, value = param.split('=', 1)
                params[key] = value
        
        if 'sni' in params:
            data['sni'] = params['sni']
        if 'type' in params:
            data['network'] = params['type']
            if params['type'] == 'ws':
                opts = {}
                if 'host' in params:
                    opts['headers'] = {'Host': params['host']}
                if 'path' in params:
                    opts['path'] = params['path']
                data['ws-opts'] = opts
            elif params['type'] == 'grpc':
                if 'serviceName' in params:
                    data['grpc-opts'] = {'grpc-service-name': params['serviceName']}
    
    return data


def parse_vless(data_str: str) -> Dict[str, Any]:
    """解析 vless:// 协议"""
    data = {'name': 'unnamed'}
    
    if '#' in data_str:
        data_str, name = data_str.rsplit('#', 1)
        data['name'] = unquote(name)
    
    if '?' in data_str:
        main_part, params_str = data_str.split('?', 1)
    else:
        main_part = data_str
        params_str = ''
    
    # 解析主部分
    if '@' in main_part:
        uuid, server_part = main_part.split('@', 1)
        data['uuid'] = uuid
        
        if ':' in server_part:
            server, port = server_part.rsplit(':', 1)
            data['server'] = server
            data['port'] = int(port)
    
    # 解析参数
    if params_str:
        params = {}
        for param in params_str.split('&'):
            if '=' in param:
                key, value = param.split('=', 1)
                params[key] = value
        
        if 'sni' in params:
            data['servername'] = params['sni']
        if 'type' in params:
            data['network'] = params['type']
            if params['type'] == 'ws':
                opts = {}
                if 'host' in params:
                    opts['headers'] = {'Host': params['host']}
                if 'path' in params:
                    opts['path'] = params['path']
                data['ws-opts'] = opts
            elif params['type'] == 'grpc':
                if 'serviceName' in params:
                    data['grpc-opts'] = {'grpc-service-name': params['serviceName']}
        if 'flow' in params:
            data['flow'] = params['flow']
        if 'security' in params:
            if params['security'] == 'tls':
                data['tls'] = True
            elif params['security'] == 'reality':
                opts = {}
                if 'pbk' in params:
                    opts['public-key'] = params['pbk']
                if 'sid' in params:
                    opts['short-id'] = params['sid']
                data['reality-opts'] = opts
    
    return data


def parse_hysteria2(data_str: str) -> Dict[str, Any]:
    """解析 hysteria2:// 协议"""
    data = {'name': 'unnamed'}
    
    if '#' in data_str:
        data_str, name = data_str.rsplit('#', 1)
        data['name'] = unquote(name)
    
    if '?' in data_str:
        main_part, params_str = data_str.split('?', 1)
    else:
        main_part = data_str
        params_str = ''
    
    # 解析主部分
    if '@' in main_part:
        password, server_part = main_part.split('@', 1)
        data['password'] = unquote(password)
        
        # 处理多端口
        if ',' in server_part:
            server_part, ports = server_part.split(',', 1)
            data['ports'] = ports
        
        if ':' in server_part:
            server, port = server_part.rsplit(':', 1)
            data['server'] = server
            data['port'] = int(port)
    
    # 解析参数
    if params_str:
        for param in params_str.split('&'):
            if '=' in param:
                key, value = param.split('=', 1)
                if key in ('sni', 'obfs', 'obfs-password', 'insecure'):
                    if key == 'insecure':
                        data['skip-cert-verify'] = value == '1'
                    else:
                        data[key] = value
    
    return data


# 解析器映射
PARSERS = {
    Protocol.VMESS: parse_vmess,
    Protocol.SS: parse_ss,
    Protocol.SSR: parse_ssr,
    Protocol.TROJAN: parse_trojan,
    Protocol.VLESS: parse_vless,
    Protocol.HYSTERIA2: parse_hysteria2,
}


# ========== URL 生成器 ==========

def generate_vmess_url(data: Dict[str, Any]) -> str:
    """生成 vmess URL"""
    v = {
        "v": "2",
        "ps": data.get('name', ''),
        "add": data['server'],
        "port": str(data['port']),
        "id": data.get('uuid', DEFAULT_UUID),
        "aid": str(data.get('alterId', 0)),
        "scy": data.get('cipher', 'auto'),
        "net": data.get('network', 'tcp'),
        "type": "none",
        "host": "",
        "path": "",
        "tls": "tls" if data.get('tls') else "",
        "sni": data.get('servername', '')
    }
    
    # 处理网络选项
    net = data.get('network', 'tcp')
    if net == 'ws' and 'ws-opts' in data:
        opts = data['ws-opts']
        if 'path' in opts:
            v['path'] = opts['path']
        if 'headers' in opts and 'Host' in opts['headers']:
            v['host'] = opts['headers']['Host']
    elif net == 'h2' and 'h2-opts' in data:
        opts = data['h2-opts']
        if 'path' in opts:
            v['path'] = opts['path']
        if 'host' in opts:
            v['host'] = ','.join(opts['host'])
    elif net == 'grpc' and 'grpc-opts' in data:
        v['path'] = data['grpc-opts'].get('grpc-service-name', '')
    
    return "vmess://" + b64encode(json.dumps(v))


def generate_ss_url(data: Dict[str, Any]) -> str:
    """生成 ss URL"""
    userinfo = f"{data.get('cipher', 'aes-128-gcm')}:{data.get('password', '')}"
    url = f"ss://{b64encode(userinfo)}@{data['server']}:{data['port']}"
    
    if 'name' in data:
        url += f"#{quote(data['name'])}"
    
    return url


def generate_trojan_url(data: Dict[str, Any]) -> str:
    """生成 trojan URL"""
    password = quote(data.get('password', ''))
    url = f"trojan://{password}@{data['server']}:{data['port']}?"
    
    if 'sni' in data:
        url += f"sni={data['sni']}&"
    if 'skip-cert-verify' in data:
        url += f"allowInsecure={int(data['skip-cert-verify'])}&"
    
    net = data.get('network', 'tcp')
    if net != 'tcp':
        url += f"type={net}&"
        if net == 'ws' and 'ws-opts' in data:
            opts = data['ws-opts']
            if 'headers' in opts and 'Host' in opts['headers']:
                url += f"host={opts['headers']['Host']}&"
            if 'path' in opts:
                url += f"path={opts['path']}&"
        elif net == 'grpc' and 'grpc-opts' in data:
            url += f"serviceName={data['grpc-opts'].get('grpc-service-name', '')}&"
    
    url = url.rstrip('&')
    if 'name' in data:
        url += f"#{quote(data['name'])}"
    
    return url


def generate_vless_url(data: Dict[str, Any]) -> str:
    """生成 vless URL"""
    uuid = data.get('uuid', '')
    url = f"vless://{uuid}@{data['server']}:{data['port']}?"
    
    if 'servername' in data:
        url += f"sni={data['servername']}&"
    if 'skip-cert-verify' in data:
        url += f"allowInsecure={int(data['skip-cert-verify'])}&"
    
    net = data.get('network', 'tcp')
    if net != 'tcp':
        url += f"type={net}&"
        if net == 'ws' and 'ws-opts' in data:
            opts = data['ws-opts']
            if 'headers' in opts and 'Host' in opts['headers']:
                url += f"host={opts['headers']['Host']}&"
            if 'path' in opts:
                url += f"path={opts['path']}&"
        elif net == 'grpc' and 'grpc-opts' in data:
            url += f"serviceName={data['grpc-opts'].get('grpc-service-name', '')}&"
    
    if 'flow' in data:
        url += f"flow={data['flow']}&"
    
    if data.get('tls'):
        url += "security=tls&"
    elif 'reality-opts' in data:
        opts = data['reality-opts']
        url += f"security=reality&pbk={opts.get('public-key', '')}&sid={opts.get('short-id', '')}&"
    
    url = url.rstrip('&')
    if 'name' in data:
        url += f"#{quote(data['name'])}"
    
    return url


def generate_hysteria2_url(data: Dict[str, Any]) -> str:
    """生成 hysteria2 URL"""
    password = quote(data.get('password', ''))
    url = f"hysteria2://{password}@{data['server']}:{data['port']}"
    
    if 'ports' in data:
        url += f",{data['ports']}"
    
    url += "?"
    
    if 'sni' in data:
        url += f"sni={data['sni']}&"
    if 'skip-cert-verify' in data:
        url += f"insecure={int(data['skip-cert-verify'])}&"
    if 'obfs' in data:
        url += f"obfs={data['obfs']}&"
    if 'obfs-password' in data:
        url += f"obfs-password={data['obfs-password']}&"
    
    url = url.rstrip('&')
    if 'name' in data:
        url += f"#{quote(data['name'])}"
    
    return url


# 生成器映射
GENERATORS = {
    Protocol.VMESS: generate_vmess_url,
    Protocol.SS: generate_ss_url,
    Protocol.TROJAN: generate_trojan_url,
    Protocol.VLESS: generate_vless_url,
    Protocol.HYSTERIA2: generate_hysteria2_url,
}
