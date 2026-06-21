"""
[v3.0] sing-box 控制面集成 (终极性能压榨)
抛弃 Python 端的并发网络请求，利用 sing-box 内置的 Clash API 和 url-test 引擎进行批量测速。
将测试耗时从“分钟级”降维到“秒级”。
"""
from __future__ import annotations
import subprocess
import time
import json
import asyncio
import requests
from typing import List, Dict
from core.parser import Node
from core.tester import TestResult # 导入原有结果对象以兼容主流水线

class SingBoxAPITester:
    def __init__(self, sb_path: str = "./sing-box", api_port: int = 9090, **kwargs):
        """兼容原 SingBoxTester 的初始化签名，忽略多余的并发参数"""
        self.sb_path = sb_path
        self.api_port = api_port
        self.api_base = f"http://127.0.0.1:{api_port}"

    async def test_all(self, nodes: List[Node]) -> List[TestResult]:
        """
        [适配层] 兼容原 SingBoxTester.test_all 接口。
        将同步的进程调用放入线程池，避免阻塞 asyncio 事件循环。
        """
        loop = asyncio.get_running_loop()
        raw_results = await loop.run_in_executor(None, self._batch_test_sync, nodes)
        
        final_results = []
        for n in nodes:
            tag = n.tag
            res_data = raw_results.get(tag, {"success": False, "error": "unknown"})
            
            r = TestResult(node=n)
            r.success = res_data.get("success", False)
            r.latency_ms = res_data.get("latency_ms", 0.0)
            r.error = res_data.get("error", "") if not r.success else ""
            # 注：API 测速无法直接获取 speed_kbps, jitter，此引擎专用于极速连通性探活
            final_results.append(r)
            
        return final_results

    def _batch_test_sync(self, nodes: List[Node], test_url: str = "https://www.gstatic.com/generate_204", timeout: int = 5) -> Dict[str, dict]:
        """同步批量测试核心逻辑"""
        if not nodes:
            return {}

        config = self._build_config(nodes, test_url, timeout)
        config_path = "/tmp/sb_api_test.json"
        with open(config_path, "w", encoding="utf-8") as f:
            json.dump(config, f, ensure_ascii=False)

        proc = subprocess.Popen(
            [self.sb_path, "run", "-c", config_path],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        
        results = {}
        try:
            time.sleep(1.5) # 等待 sing-box 启动并初始化 Clash API
            
            # 主动触发测速
            group_name = "test-group"
            trigger_url = f"{self.api_base}/group/{group_name}/delay?url={test_url}&timeout={timeout * 1000}"
            try:
                requests.get(trigger_url, timeout=timeout + 2)
            except Exception:
                pass 

            # 获取结果
            resp = requests.get(f"{self.api_base}/proxies", timeout=5)
            proxies = resp.json().get("proxies", {})
            
            for n in nodes:
                tag = n.tag
                if tag in proxies:
                    history = proxies[tag].get("history", [])
                    if history and history[-1].get("delay", 0) > 0:
                        results[tag] = {"success": True, "latency_ms": history[-1]["delay"]}
                    else:
                        results[tag] = {"success": False, "error": "timeout"}
                else:
                    results[tag] = {"success": False, "error": "not_found"}
        except Exception as e:
            print(f"[SingBoxAPI] Error: {e}")
        finally:
            proc.terminate()
            try:
                proc.wait(timeout=3)
            except subprocess.TimeoutExpired:
                proc.kill()

        return results

    def _build_config(self, nodes: List[Node], test_url: str, timeout: int) -> dict:
        outbounds = [n.to_singbox() for n in nodes]
        outbounds.append({"type": "direct", "tag": "direct"})
        outbounds.append({
            "type": "urltest",
            "tag": "test-group",
            "outbounds": [n.tag for n in nodes],
            "url": test_url,
            "interval": "1m", 
            "tolerance": 50
        })

        return {
            "log": {"level": "error"},
            "inbounds": [], 
            "outbounds": outbounds,
            "experimental": {
                "clash_api": {
                    "external_controller": f"127.0.0.1:{self.api_port}",
                    "secret": ""
                }
            }
        }
