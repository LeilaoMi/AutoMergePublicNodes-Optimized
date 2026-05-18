"""
真实代理测试器
- 使用 sing-box（Karing 内核同源）启动每个节点为本地 SOCKS5
- 真实 HTTP 请求测试连通性和延迟
- 每个 worker 独立端口避免冲突
- 失败快速跳过

为什么用 sing-box 而不是 xray:
- Karing 用的就是 sing-box，测试结果与 Karing 一致
- 原生支持 hysteria2/tuic/anytls/wireguard 等新协议
- 配置格式统一，无需协议转换映射
"""
from __future__ import annotations

import asyncio
import json
import os
import shutil
import socket
import tempfile
import time
from dataclasses import dataclass
from typing import List, Optional

import aiohttp

from core.parser import Node


# 测试 URL（Google 204，全球可达，1KB 响应）
TEST_URL = "http://www.gstatic.com/generate_204"
EXPECTED_STATUS = 204


@dataclass
class TestResult:
    node: Node
    success: bool = False
    latency_ms: int = 0
    error: str = ""


def _find_free_port(start: int, end: int) -> int:
    """找一个空闲端口"""
    for port in range(start, end):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            try:
                s.bind(("127.0.0.1", port))
                return port
            except OSError:
                continue
    raise RuntimeError("no free port available")


def build_singbox_config(node: Node, socks_port: int) -> dict:
    """构造 sing-box 临时配置：SOCKS5 入站 + 节点出站"""
    inbound = {
        "type": "socks",
        "tag": "socks-in",
        "listen": "127.0.0.1",
        "listen_port": socks_port,
        "sniff": False,
    }
    outbound = node.to_singbox()
    return {
        "log": {"level": "error"},
        "inbounds": [inbound],
        "outbounds": [
            outbound,
            {"type": "direct", "tag": "direct"},
        ],
        "route": {"final": outbound["tag"]},
    }


class SingBoxTester:
    def __init__(self, sb_path: str = "./sing-box", concurrency: int = 30,
                 startup_wait: float = 0.6, request_timeout: float = 6.0):
        if not os.path.exists(sb_path):
            raise FileNotFoundError(f"sing-box binary not found: {sb_path}")
        self.sb_path = os.path.abspath(sb_path)
        self.concurrency = concurrency
        self.startup_wait = startup_wait
        self.request_timeout = request_timeout
        self._port_counter = 30000

    def _alloc_port(self) -> int:
        # 在线程安全前提下从一段大端口范围找空闲
        for _ in range(200):
            self._port_counter += 1
            if self._port_counter > 60000:
                self._port_counter = 30000
            try:
                return _find_free_port(self._port_counter, self._port_counter + 1)
            except RuntimeError:
                continue
        raise RuntimeError("no free ports")

    async def test_one(self, node: Node) -> TestResult:
        result = TestResult(node=node)
        port = self._alloc_port()

        # 写临时配置
        tmpdir = tempfile.mkdtemp(prefix="sb-")
        config_path = os.path.join(tmpdir, "config.json")
        try:
            with open(config_path, "w") as f:
                json.dump(build_singbox_config(node, port), f)
        except Exception as e:
            result.error = f"config: {e}"
            shutil.rmtree(tmpdir, ignore_errors=True)
            return result

        # 启动 sing-box
        proc = None
        try:
            proc = await asyncio.create_subprocess_exec(
                self.sb_path, "run", "-c", config_path,
                stdout=asyncio.subprocess.DEVNULL,
                stderr=asyncio.subprocess.DEVNULL,
            )
            # 等待启动
            await asyncio.sleep(self.startup_wait)

            if proc.returncode is not None:
                result.error = f"sing-box exited {proc.returncode}"
                return result

            # 通过本地 SOCKS5 发起请求测试
            connector = aiohttp.TCPConnector(ssl=False, limit=1)
            try:
                from aiohttp_socks import ProxyConnector
                connector = ProxyConnector.from_url(f"socks5://127.0.0.1:{port}")
            except ImportError:
                pass

            start = time.monotonic()
            try:
                async with aiohttp.ClientSession(connector=connector) as session:
                    async with session.get(
                        TEST_URL,
                        timeout=aiohttp.ClientTimeout(total=self.request_timeout),
                    ) as resp:
                        latency = int((time.monotonic() - start) * 1000)
                        if resp.status == EXPECTED_STATUS:
                            result.success = True
                            result.latency_ms = latency
                        else:
                            result.error = f"status {resp.status}"
            except asyncio.TimeoutError:
                result.error = "timeout"
            except Exception as e:
                result.error = type(e).__name__

        except Exception as e:
            result.error = f"start: {e}"
        finally:
            if proc and proc.returncode is None:
                try:
                    proc.terminate()
                    try:
                        await asyncio.wait_for(proc.wait(), timeout=2)
                    except asyncio.TimeoutError:
                        proc.kill()
                        await proc.wait()
                except ProcessLookupError:
                    pass
            shutil.rmtree(tmpdir, ignore_errors=True)

        return result

    async def test_all(self, nodes: List[Node], progress_every: int = 50) -> List[TestResult]:
        sem = asyncio.Semaphore(self.concurrency)
        results: List[TestResult] = []
        done = 0
        valid = 0

        async def _wrap(n: Node) -> TestResult:
            async with sem:
                return await self.test_one(n)

        tasks = [asyncio.create_task(_wrap(n)) for n in nodes]
        for fut in asyncio.as_completed(tasks):
            r = await fut
            results.append(r)
            done += 1
            if r.success:
                valid += 1
            if done % progress_every == 0 or done == len(nodes):
                print(f"  进度: {done}/{len(nodes)} 通过: {valid}", flush=True)
        return results
