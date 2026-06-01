"""
真实代理测试器
- 使用 sing-box（Karing 内核同源）启动每个节点为本地 SOCKS5
- 真实 HTTP 请求测试连通性和延迟
- 每个 worker 独立端口避免冲突
- 失败快速跳过

为什么用 sing-box 而不是 xray:
- Karing 用的就是 sing-box，测试结果与 Karing 一致
- 原生支持 hysteria2/tuic/anytls 等新协议
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
from typing import List

import aiohttp
from aiohttp_socks import ProxyConnector

from core.parser import Node


# 测试目标 4 层 (第 4 层为带宽测试，能下完才算"真用得起来")
TEST_TARGETS = [
    ("https://www.youtube.com/generate_204",   "204"),
    ("https://www.google.com/generate_204",    "204"),
    ("https://1.1.1.1/cdn-cgi/trace",          "geo"),
    ("https://speed.cloudflare.com/__down?bytes=102400", "speed"),  # 100KB 带宽测试
]
SPEED_REQUIRED_BYTES = 100_000
SPEED_TIMEOUT_SEC = 8

DEFAULT_MIN_LATENCY_MS = 30.0  # 低于此值视为可疑节点；可通过 CLI 设为 0 关闭


@dataclass
class TestResult:
    node: Node
    success: bool = False
    latency_ms: float = 0.0
    jitter_ms: float = 0.0  # 延迟抖动（max deviation from avg）
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
        "sniff": True,
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
                 startup_wait: float = 0.6, request_timeout: float = 6.0,
                 min_latency_ms: float = DEFAULT_MIN_LATENCY_MS):
        if not os.path.exists(sb_path):
            raise FileNotFoundError(f"sing-box binary not found: {sb_path}")
        self.sb_path = os.path.abspath(sb_path)
        self.concurrency = concurrency
        self.startup_wait = startup_wait
        self.request_timeout = request_timeout
        self.min_latency_ms = min_latency_ms
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
        
        # 分配端口
        try:
            port = self._alloc_port()
        except RuntimeError:
            result.error = "no free ports"
            return result

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
            await asyncio.sleep(self.startup_wait)

            if proc.returncode is not None:
                result.error = f"sing-box exited {proc.returncode}"
                return result

            # 创建一个 session 用于所有目标测试
            connector = ProxyConnector.from_url(f"socks5://127.0.0.1:{port}")
            async with aiohttp.ClientSession(connector=connector) as session:
                # 严格测试：必须两个被墙的 HTTPS 端点都返回 204
                latencies = []
                failed_target = None
                for target_url, target_kind in TEST_TARGETS:
                    tstart = time.monotonic()
                    try:
                        timeout = aiohttp.ClientTimeout(total=SPEED_TIMEOUT_SEC if target_kind == "speed" else self.request_timeout)
                        async with session.get(target_url, timeout=timeout) as resp:
                            if target_kind == "204":
                                if resp.status != 204:
                                    failed_target = f"{target_kind}:status={resp.status}"
                                    break
                                body = await resp.read()
                                if body:  # 必须空 body
                                    failed_target = f"{target_kind}:non-empty-body"
                                    break
                            elif target_kind == "geo":
                                if resp.status != 200:
                                    failed_target = f"{target_kind}:status={resp.status}"
                                    break
                                text = await resp.text()
                                # 出口 IP 必须不在中国
                                if "loc=CN" in text:
                                    failed_target = f"{target_kind}:exit-loc-CN"
                                    break
                            elif target_kind == "speed":
                                # 必须真的下载完 100KB
                                if resp.status != 200:
                                    failed_target = f"{target_kind}:status={resp.status}"
                                    break
                                total = 0
                                async for chunk in resp.content.iter_chunked(8192):
                                    total += len(chunk)
                                if total < SPEED_REQUIRED_BYTES:
                                    failed_target = f"{target_kind}:only-{total}B"
                                    break
                        latencies.append((time.monotonic() - tstart) * 1000)
                    except Exception as e:
                        failed_target = f"{target_kind}:{type(e).__name__}"
                        break

                if failed_target is None and latencies:
                    # 取前 3 个目标的平均延迟（不算下载耗时）
                    latency_targets = [l for l, (_, k) in zip(latencies, TEST_TARGETS) if k != "speed"]
                    avg_latency = sum(latency_targets) / len(latency_targets) if latency_targets else latencies[0]
                    jitter = max(abs(l - avg_latency) for l in latency_targets) if len(latency_targets) >= 2 else 0.0
                    if self.min_latency_ms > 0 and avg_latency < self.min_latency_ms:
                        result.error = f"latency-too-low:{avg_latency:.1f}ms"
                    else:
                        result.success = True
                        result.latency_ms = avg_latency
                        result.jitter_ms = jitter
                else:
                    result.error = failed_target or "no-test-completed"

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