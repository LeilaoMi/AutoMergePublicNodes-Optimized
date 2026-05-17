#!/usr/bin/env python3
"""
真实代理连通性测试
通过代理发送 HTTP 请求，验证节点真正可用
"""
import asyncio
import aiohttp
import time
import base64
import json
from typing import List, Dict, Any, Optional, Tuple
from dataclasses import dataclass
import logging

logger = logging.getLogger(__name__)

# 测试 URL（用于验证代理是否真正可用）
TEST_URLS = [
    "https://www.google.com/generate_204",
    "https://cp.cloudflare.com/generate_204", 
    "https://www.youtube.com/generate_204",
]

# 代理测试超时
PROXY_TIMEOUT = 10  # 秒
MAX_CONCURRENT = 50  # 最大并发


@dataclass
class ProxyTestResult:
    """代理测试结果"""
    node: Dict[str, Any]
    success: bool
    delay_ms: float
    test_url: str
    error: Optional[str] = None


def node_to_clash_proxy(node: Dict[str, Any]) -> Dict[str, Any]:
    """将节点转换为 Clash 代理格式"""
    proxy = {"name": node.get("name", "unknown")}
    
    server = node.get("server") or node.get("add") or node.get("host")
    port = node.get("port")
    
    if not server or not port:
        return None
    
    proxy["server"] = server
    proxy["port"] = int(port)
    
    # 根据协议类型设置
    protocol = node.get("type", "vmess")
    proxy["type"] = protocol
    
    if protocol == "vmess":
        proxy.update({
            "uuid": node.get("uuid") or node.get("id"),
            "alterId": int(node.get("alterId", 0)),
            "cipher": node.get("cipher") or node.get("scy", "auto"),
            "udp": True,
        })
        if node.get("tls") == "tls":
            proxy["tls"] = True
        if node.get("net") == "ws":
            proxy["network"] = "ws"
            proxy["ws-opts"] = {
                "path": node.get("path", "/"),
                "headers": {"Host": node.get("host", server)}
            }
        if node.get("net") == "grpc":
            proxy["network"] = "grpc"
            proxy["grpc-opts"] = {
                "grpc-service-name": node.get("path", "")
            }
    
    elif protocol == "ss":
        proxy.update({
            "cipher": node.get("cipher") or node.get("method"),
            "password": node.get("password"),
        })
    
    elif protocol == "trojan":
        proxy.update({
            "password": node.get("password"),
            "udp": True,
            "skip-cert-verify": node.get("skip-cert-verify", False),
        })
        if node.get("sni"):
            proxy["sni"] = node.get("sni")
        if node.get("network") == "ws":
            proxy["network"] = "ws"
            proxy["ws-opts"] = {
                "path": node.get("ws-opts", {}).get("path", "/"),
            }
    
    elif protocol == "vless":
        proxy.update({
            "uuid": node.get("uuid") or node.get("id"),
            "udp": True,
            "tls": node.get("tls", False),
            "skip-cert-verify": node.get("skip-cert-verify", False),
        })
        if node.get("flow"):
            proxy["flow"] = node.get("flow")
        if node.get("network") == "ws":
            proxy["network"] = "ws"
            proxy["ws-opts"] = {
                "path": node.get("path", "/"),
            }
        elif node.get("network") == "grpc":
            proxy["network"] = "grpc"
            proxy["grpc-opts"] = {
                "grpc-service-name": node.get("grpc-opts", {}).get("grpc-service-name", "")
            }
    
    elif protocol == "hysteria2":
        proxy.update({
            "password": node.get("password"),
            "skip-cert-verify": node.get("skip-cert-verify", False),
        })
        if node.get("sni"):
            proxy["sni"] = node.get("sni")
    
    elif protocol == "ssr":
        proxy.update({
            "cipher": node.get("cipher"),
            "password": node.get("password"),
            "obfs": node.get("obfs"),
            "obfs-param": node.get("obfs-param"),
            "protocol": node.get("protocol"),
            "protocol-param": node.get("protocol-param"),
        })
    
    return proxy


async def test_proxy_http(
    proxy_config: Dict[str, Any],
    test_url: str,
    timeout: float = PROXY_TIMEOUT
) -> Tuple[bool, float, Optional[str]]:
    """
    通过 HTTP 代理测试节点
    返回: (是否成功, 延迟ms, 错误信息)
    """
    try:
        # 构建代理 URL（需要本地有代理客户端监听）
        # 这里假设使用 clash 的 RESTful API
        server = proxy_config.get("server")
        port = proxy_config.get("port")
        
        # 直接 TCP 连接测试（简化版，无法测试真实代理）
        # 真实测试需要启动本地代理客户端
        start = time.time()
        
        # 使用 aiohttp 通过代理请求
        # 注意：这需要本地有代理客户端（如 clash）运行
        connector = aiohttp.TCPConnector(limit=1)
        
        async with aiohttp.ClientSession(
            connector=connector,
            timeout=aiohttp.ClientTimeout(total=timeout)
        ) as session:
            try:
                async with session.get(test_url, proxy=f"http://{server}:{port}") as resp:
                    delay = (time.time() - start) * 1000
                    if resp.status in [200, 204]:
                        return True, delay, None
                    return False, delay, f"HTTP {resp.status}"
            except Exception as e:
                return False, (time.time() - start) * 1000, str(e)
    
    except Exception as e:
        return False, 0, str(e)


async def test_node_via_clash_api(
    clash_url: str,
    proxy_name: str,
    timeout: float = PROXY_TIMEOUT
) -> Tuple[bool, float, Optional[str]]:
    """
    通过 Clash RESTful API 测试代理延迟
    需要 Clash/Meta 运行并开启 external-controller
    """
    try:
        async with aiohttp.ClientSession() as session:
            # Clash API: GET /proxies/{name}/delay?timeout=5000&url=...
            url = f"{clash_url}/proxies/{proxy_name}/delay"
            params = {
                "timeout": int(timeout * 1000),
                "url": "https://www.gstatic.com/generate_204"
            }
            
            start = time.time()
            async with session.get(url, params=params, timeout=timeout + 5) as resp:
                data = await resp.json()
                delay = data.get("delay", 0)
                
                if delay > 0:
                    return True, delay, None
                else:
                    return False, 0, data.get("message", "timeout")
    
    except Exception as e:
        return False, 0, str(e)


async def test_proxies_batch(
    proxies: List[Dict[str, Any]],
    max_concurrent: int = MAX_CONCURRENT,
    timeout: float = PROXY_TIMEOUT,
    clash_url: Optional[str] = None
) -> List[ProxyTestResult]:
    """
    批量测试代理
    """
    results = []
    semaphore = asyncio.Semaphore(max_concurrent)
    
    async def test_single(proxy: Dict[str, Any]) -> ProxyTestResult:
        async with semaphore:
            name = proxy.get("name", "unknown")
            
            if clash_url:
                # 使用 Clash API 测试
                success, delay, error = await test_node_via_clash_api(
                    clash_url, name, timeout
                )
            else:
                # 直接 HTTP 测试（简化版）
                test_url = TEST_URLS[0]
                success, delay, error = await test_proxy_http(
                    proxy, test_url, timeout
                )
            
            return ProxyTestResult(
                node=proxy,
                success=success,
                delay_ms=delay,
                test_url=TEST_URLS[0] if not clash_url else "clash-api",
                error=error
            )
    
    tasks = [test_single(p) for p in proxies]
    results = await asyncio.gather(*tasks)
    
    return list(results)


def filter_valid_proxies(
    proxies: List[Dict[str, Any]],
    max_concurrent: int = MAX_CONCURRENT,
    timeout: float = PROXY_TIMEOUT,
    clash_url: Optional[str] = None
) -> List[Dict[str, Any]]:
    """
    过滤出真正可用的代理
    """
    async def run():
        results = await test_proxies_batch(
            proxies, max_concurrent, timeout, clash_url
        )
        
        valid = []
        for r in results:
            if r.success:
                # 更新节点延迟信息
                r.node["delay_test"] = r.delay_ms
                valid.append(r.node)
        
        # 按延迟排序
        valid.sort(key=lambda x: x.get("delay_test", 99999))
        
        return valid
    
    return asyncio.run(run())


# ==================== 命令行接口 ====================

if __name__ == "__main__":
    import argparse
    import yaml
    
    parser = argparse.ArgumentParser(description="真实代理连通性测试")
    parser.add_argument("-i", "--input", default="list.yml", help="输入 YAML 文件")
    parser.add_argument("-o", "--output", default="list_valid.yml", help="输出文件")
    parser.add_argument("-t", "--timeout", type=float, default=10, help="超时秒数")
    parser.add_argument("-c", "--concurrent", type=int, default=50, help="并发数")
    parser.add_argument("--clash-url", default=None, help="Clash API 地址")
    
    args = parser.parse_args()
    
    # 加载节点
    with open(args.input, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    
    proxies = data.get("proxies", [])
    print(f"加载了 {len(proxies)} 个节点")
    
    # 测试代理
    print("开始真实代理测试...")
    valid = filter_valid_proxies(
        proxies,
        max_concurrent=args.concurrent,
        timeout=args.timeout,
        clash_url=args.clash_url
    )
    
    print(f"\n有效节点: {len(valid)}/{len(proxies)}")
    
    # 输出
    if args.output.endswith(".yml") or args.output.endswith(".yaml"):
        data["proxies"] = valid
        with open(args.output, "w", encoding="utf-8") as f:
            yaml.dump(data, f, allow_unicode=True, default_flow_style=False)
    else:
        # Base64 编码输出
        lines = []
        for p in valid:
            # 生成节点 URL
            url = generate_proxy_url(p)
            if url:
                lines.append(url)
        
        content = "\n".join(lines)
        b64 = base64.b64encode(content.encode()).decode()
        
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(b64)
    
    print(f"已保存到 {args.output}")


def generate_proxy_url(proxy: Dict[str, Any]) -> Optional[str]:
    """生成代理 URL"""
    ptype = proxy.get("type", "")
    server = proxy.get("server", "")
    port = proxy.get("port", "")
    name = proxy.get("name", "")
    
    if ptype == "vmess":
        vmess = {
            "v": "2",
            "ps": name,
            "add": server,
            "port": port,
            "id": proxy.get("uuid", ""),
            "aid": proxy.get("alterId", 0),
            "scy": proxy.get("cipher", "auto"),
            "net": proxy.get("network", "tcp"),
            "type": "none",
            "host": "",
            "path": "",
            "tls": "tls" if proxy.get("tls") else "",
        }
        return "vmess://" + base64.b64encode(
            json.dumps(vmess).encode()
        ).decode()
    
    elif ptype == "ss":
        # ss://method:password@server:port#name
        cipher = proxy.get("cipher", "")
        password = proxy.get("password", "")
        user_info = f"{cipher}:{password}"
        b64_user = base64.b64encode(user_info.encode()).decode()
        return f"ss://{b64_user}@{server}:{port}#{name}"
    
    elif ptype == "trojan":
        password = proxy.get("password", "")
        return f"trojan://{password}@{server}:{port}?sni={proxy.get('sni', server)}#{name}"
    
    elif ptype == "vless":
        uuid = proxy.get("uuid", "")
        return f"vless://{uuid}@{server}:{port}?type={proxy.get('network', 'tcp')}#{name}"
    
    return None
