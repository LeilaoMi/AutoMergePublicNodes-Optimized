#!/usr/bin/env python3
"""
Xray 真实代理测试
将 Clash YAML 格式节点转换为 Xray 配置，并逐个测试连通性
"""
import yaml
import json
import subprocess
import time
import requests
import base64
import os
import tempfile
from typing import List, Dict, Any, Optional, Tuple
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading

# 测试配置
TEST_URL = "https://www.gstatic.com/generate_204"
TEST_TIMEOUT = 10
MAX_CONCURRENT = 20

class XrayProxyTester:
    """Xray 代理测试器"""
    
    def __init__(self, xray_path: str = "./xray"):
        self.xray_path = xray_path
        self.lock = threading.Lock()
    
    def yaml_to_xray_config(self, proxy: Dict[str, Any]) -> Optional[Dict]:
        """将 Clash YAML 格式转换为 Xray 配置"""
        ptype = proxy.get("type", "")
        
        inbound = {
            "port": 10808,
            "listen": "127.0.0.1",
            "protocol": "socks",
            "settings": {"udp": True}
        }
        
        # 根据协议类型生成 outbound
        if ptype == "vmess":
            outbound = self._vmess_to_xray(proxy)
        elif ptype == "vless":
            outbound = self._vless_to_xray(proxy)
        elif ptype == "trojan":
            outbound = self._trojan_to_xray(proxy)
        elif ptype == "ss":
            outbound = self._ss_to_xray(proxy)
        elif ptype == "ssr":
            outbound = self._ssr_to_xray(proxy)
        elif ptype == "hysteria2":
            outbound = self._hysteria2_to_xray(proxy)
        else:
            print(f"⚠ 不支持的协议: {ptype}")
            return None
        
        if not outbound:
            return None
        
        config = {
            "log": {"loglevel": "error"},
            "inbounds": [inbound],
            "outbounds": [outbound]
        }
        
        return config
    
    def _vmess_to_xray(self, p: Dict) -> Dict:
        """VMess 配置转换"""
        server = p.get("server", "")
        port = p.get("port", 443)
        uuid = p.get("uuid", "")
        alterId = p.get("alterId", 0)
        cipher = p.get("cipher", "auto")
        network = p.get("network", "tcp")
        
        outbound = {
            "protocol": "vmess",
            "settings": {
                "vnext": [{
                    "address": server,
                    "port": port,
                    "users": [{
                        "id": uuid,
                        "alterId": alterId,
                        "security": cipher
                    }]
                }]
            }
        }
        
        # 传输配置
        stream_settings = {"network": network}
        
        if network == "ws":
            ws_opts = p.get("ws-opts", {})
            stream_settings["wsSettings"] = {
                "path": ws_opts.get("path", "/"),
                "headers": {"Host": ws_opts.get("headers", {}).get("Host", server)}
            }
        elif network == "grpc":
            grpc_opts = p.get("grpc-opts", {})
            stream_settings["grpcSettings"] = {
                "serviceName": grpc_opts.get("grpc-service-name", ""),
                "multiMode": True
            }
        elif network == "h2":
            h2_opts = p.get("h2-opts", {})
            stream_settings["httpSettings"] = {
                "path": h2_opts.get("path", "/"),
                "host": h2_opts.get("host", [server])
            }
        
        # TLS
        if p.get("tls"):
            tls_settings = {
                "serverName": p.get("servername", p.get("sni", server)),
                "allowInsecure": p.get("skip-cert-verify", False)
            }
            if p.get("client-fingerprint"):
                tls_settings["fingerprint"] = p.get("client-fingerprint")
            stream_settings["tlsSettings"] = tls_settings
            stream_settings["security"] = "tls"
        
        outbound["streamSettings"] = stream_settings
        return outbound
    
    def _vless_to_xray(self, p: Dict) -> Dict:
        """VLESS 配置转换"""
        server = p.get("server", "")
        port = p.get("port", 443)
        uuid = p.get("uuid", "")
        flow = p.get("flow", "")
        network = p.get("network", "tcp")
        
        outbound = {
            "protocol": "vless",
            "settings": {
                "vnext": [{
                    "address": server,
                    "port": port,
                    "users": [{
                        "id": uuid,
                        "encryption": "none",
                        "flow": flow if flow else ""
                    }]
                }]
            }
        }
        
        stream_settings = {"network": network}
        
        if network == "ws":
            ws_opts = p.get("ws-opts", {})
            stream_settings["wsSettings"] = {
                "path": ws_opts.get("path", "/"),
                "headers": {"Host": ws_opts.get("headers", {}).get("Host", server)}
            }
        elif network == "grpc":
            grpc_opts = p.get("grpc-opts", {})
            stream_settings["grpcSettings"] = {
                "serviceName": grpc_opts.get("grpc-service-name", ""),
                "multiMode": True
            }
        elif network == "tcp":
            if p.get("reality-opts"):
                # REALITY 配置
                reality_opts = p.get("reality-opts", {})
                stream_settings["realitySettings"] = {
                    "serverName": p.get("servername", "www.google.com"),
                    "publicKey": reality_opts.get("public-key", ""),
                    "shortId": reality_opts.get("short-id", ""),
                    "fingerprint": p.get("client-fingerprint", "chrome")
                }
                stream_settings["security"] = "reality"
        
        # TLS
        if p.get("tls") and not p.get("reality-opts"):
            tls_settings = {
                "serverName": p.get("servername", p.get("sni", server)),
                "allowInsecure": p.get("skip-cert-verify", False)
            }
            stream_settings["tlsSettings"] = tls_settings
            stream_settings["security"] = "tls"
        
        outbound["streamSettings"] = stream_settings
        return outbound
    
    def _trojan_to_xray(self, p: Dict) -> Dict:
        """Trojan 配置转换"""
        server = p.get("server", "")
        port = p.get("port", 443)
        password = p.get("password", "")
        sni = p.get("sni", server)
        network = p.get("network", "tcp")
        
        outbound = {
            "protocol": "trojan",
            "settings": {
                "servers": [{
                    "address": server,
                    "port": port,
                    "password": password
                }]
            }
        }
        
        stream_settings = {"network": network}
        
        if network == "ws":
            ws_opts = p.get("ws-opts", {})
            stream_settings["wsSettings"] = {
                "path": ws_opts.get("path", "/"),
                "headers": {"Host": ws_opts.get("headers", {}).get("Host", sni)}
            }
        elif network == "grpc":
            grpc_opts = p.get("grpc-opts", {})
            stream_settings["grpcSettings"] = {
                "serviceName": grpc_opts.get("grpc-service-name", ""),
                "multiMode": True
            }
        
        # TLS
        stream_settings["security"] = "tls"
        stream_settings["tlsSettings"] = {
            "serverName": sni,
            "allowInsecure": p.get("skip-cert-verify", False)
        }
        
        outbound["streamSettings"] = stream_settings
        return outbound
    
    def _ss_to_xray(self, p: Dict) -> Dict:
        """Shadowsocks 配置转换"""
        server = p.get("server", "")
        port = p.get("port", 8388)
        cipher = p.get("cipher", "aes-128-gcm")
        password = p.get("password", "")
        
        outbound = {
            "protocol": "shadowsocks",
            "settings": {
                "servers": [{
                    "address": server,
                    "port": port,
                    "method": cipher,
                    "password": password
                }]
            }
        }
        
        # 插件支持
        if p.get("plugin"):
            plugin = p.get("plugin")
            opts = p.get("plugin-opts", {})
            
            if plugin == "v2ray-plugin":
                transport = {
                    "type": opts.get("mode", "websocket"),
                    "path": opts.get("path", "/"),
                    "host": [opts.get("host", server)]
                }
                outbound["streamSettings"] = {
                    "network": "ws",
                    "wsSettings": transport
                }
        
        return outbound
    
    def _ssr_to_xray(self, p: Dict) -> Optional[Dict]:
        """SSR 配置转换 - Xray 不原生支持 SSR，跳过"""
        print(f"⚠ Xray 不支持 SSR 协议，跳过: {p.get('name', '')}")
        return None
    
    def _hysteria2_to_xray(self, p: Dict) -> Dict:
        """Hysteria2 配置转换"""
        server = p.get("server", "")
        port = p.get("port", 443)
        password = p.get("password", "")
        sni = p.get("sni", server)
        
        outbound = {
            "protocol": "hysteria2",
            "settings": {
                "server": server,
                "serverPort": port,
                "password": password
            }
        }
        
        # TLS
        outbound["streamSettings"] = {
            "security": "tls",
            "tlsSettings": {
                "serverName": sni,
                "allowInsecure": p.get("skip-cert-verify", False)
            }
        }
        
        return outbound
    
    def test_proxy(self, proxy: Dict, index: int = 0) -> Tuple[str, bool, float]:
        """测试单个代理"""
        name = proxy.get("name", f"proxy-{index}")
        
        # 转换配置
        config = self.yaml_to_xray_config(proxy)
        if not config:
            return name, False, 0
        
        # 写入临时配置文件
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            json.dump(config, f)
            config_path = f.name
        
        try:
            # 启动 Xray
            proc = subprocess.Popen(
                [self.xray_path, "run", "-c", config_path],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            
            # 等待启动
            time.sleep(2)
            
            if proc.poll() is not None:
                # 进程已退出，启动失败
                return name, False, 0
            
            # 测试代理
            proxies = {
                "http": "socks5://127.0.0.1:10808",
                "https": "socks5://127.0.0.1:10808"
            }
            
            start = time.time()
            try:
                resp = requests.get(TEST_URL, proxies=proxies, timeout=TEST_TIMEOUT)
                delay = (time.time() - start) * 1000
                
                if resp.status_code == 204:
                    return name, True, delay
                else:
                    return name, False, 0
            except Exception:
                return name, False, 0
            finally:
                proc.terminate()
                proc.wait()
        
        except Exception as e:
            return name, False, 0
        finally:
            os.unlink(config_path)
    
    def test_all(self, proxies: List[Dict], max_workers: int = MAX_CONCURRENT) -> List[Tuple[str, bool, float]]:
        """批量测试代理"""
        results = []
        
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {
                executor.submit(self.test_proxy, p, i): p.get("name", f"proxy-{i}")
                for i, p in enumerate(proxies)
            }
            
            for future in as_completed(futures):
                name, success, delay = future.result()
                results.append((name, success, delay))
                
                if success:
                    print(f"✓ {name}: {delay:.0f}ms")
                else:
                    print(f"✗ {name}")
        
        return results


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Xray 真实代理测试")
    parser.add_argument("--input", default="list.yml", help="输入 YAML 文件")
    parser.add_argument("--output", default="valid_nodes.txt", help="输出有效节点文件")
    parser.add_argument("--xray", default="./xray", help="Xray 路径")
    parser.add_argument("--max-workers", type=int, default=10, help="最大并发数")
    args = parser.parse_args()
    
    # 读取节点
    with open(args.input, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    
    proxies = data.get("proxies", [])
    print(f"共 {len(proxies)} 个节点待测试\n")
    
    # 测试
    tester = XrayProxyTester(args.xray)
    results = tester.test_all(proxies, args.max_workers)
    
    # 统计
    valid = [(name, delay) for name, success, delay in results if success]
    print(f"\n有效节点: {len(valid)}/{len(proxies)}")
    
    # 保存
    with open(args.output, 'w') as f:
        for name, delay in valid:
            f.write(f"{name}\n")
    
    print(f"已保存到 {args.output}")


if __name__ == "__main__":
    main()
