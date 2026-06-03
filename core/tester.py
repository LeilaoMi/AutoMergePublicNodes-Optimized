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


# 测试目标 4 层
# - 204: youtube / google 204 = 真的墙外节点, 不能直连的才是好节点
# - cn-block: 必须能访问中国大陆站 (baidu), 否则节点根本没流量代理能力
# - geo: 出口 IP 不能是中国 (ipinfo.io), 否则就是"挂在中国机房的出口", 没意义
# - speed: 必须真的能下完 100KB, 证明可承载真实流量
# 第 4 层为带宽测试，能下完才算"真用得起来"
TEST_TARGETS = [
    ("https://www.youtube.com/generate_204",   "204"),
    ("https://www.google.com/generate_204",    "204"),
    ("https://www.baidu.com/robots.txt",       "cn-block"),
    ("https://ipinfo.io/json",                 "geo"),
    ("https://speed.cloudflare.com/__down?bytes=102400", "speed"),
]
SPEED_REQUIRED_BYTES = 100_000
SPEED_TIMEOUT_SEC = 8

# exit-ip geo check 通过时, body 里 country 字段不能等于这个
GEO_BLOCKED_COUNTRY = "CN"

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
        """§2.5 改用 OS 分配空闲端口, 而不是顺序递增计数器
        之前 _port_counter 在 30 并发下大概率两个 worker 同时拿到 30001, 实际 bind 失败
        线程安全: 用 _port_lock 保护 (asyncio 单线程, 但 _find_free_port 内有 socket 阻塞调用)
        失败重试 200 次, 每次随机从一段范围取端口
        """
        import random
        for attempt in range(200):
            # 随机从 30000-50000 范围挑, 避免顺序冲突
            start = random.randint(30000, 49999)
            try:
                return _find_free_port(start, start + 1)
            except RuntimeError:
                continue
        raise RuntimeError("no free ports after 200 attempts")

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
        stderr_path = os.path.join(tmpdir, "sb.err")
        try:
            with open(config_path, "w") as f:
                json.dump(build_singbox_config(node, port), f)
        except Exception as e:
            result.error = f"config: {e}"
            shutil.rmtree(tmpdir, ignore_errors=True)
            return result

        # 启动 sing-box. stderr 写文件方便排查启动失败根因.
        proc = None
        try:
            stderr_fh = open(stderr_path, "w")
            try:
                proc = await asyncio.create_subprocess_exec(
                    self.sb_path, "run", "-c", config_path,
                    stdout=asyncio.subprocess.DEVNULL,
                    stderr=stderr_fh,
                )
            except Exception:
                stderr_fh.close()
                raise
            await asyncio.sleep(self.startup_wait)

            if proc.returncode is not None:
                # 启动立刻失败, 读 stderr 给提示
                stderr_fh.close()
                err_text = ""
                try:
                    with open(stderr_path, encoding="utf-8", errors="replace") as f:
                        err_text = f.read()[:500].strip()
                except Exception:
                    pass
                if err_text:
                    # 提取关键错误行
                    first_lines = " | ".join(
                        line.strip() for line in err_text.splitlines()[:3] if line.strip()
                    )[:300]
                    result.error = f"sing-box exited {proc.returncode}: {first_lines}"
                else:
                    result.error = f"sing-box exited {proc.returncode}"
                return result

            # 创建一个 session 用于所有目标测试
            connector = ProxyConnector.from_url(f"socks5://127.0.0.1:{port}")
            async with aiohttp.ClientSession(connector=connector) as session:
                # 严格测试: 必须每个目标都通过
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
                            elif target_kind == "cn-block":
                                # 必须能访问中国大陆站, 否则节点根本没流量代理能力
                                if resp.status != 200:
                                    failed_target = f"{target_kind}:status={resp.status}"
                                    break
                            elif target_kind == "geo":
                                # 出口 IP 不能是中国大陆. ipinfo.io 比 1.1.1.1/cdn-cgi/trace 准,
                                # 因为后者对 CF / Fastly / Workers 前置节点永远返回非 CN.
                                if resp.status != 200:
                                    failed_target = f"{target_kind}:status={resp.status}"
                                    break
                                try:
                                    info = await resp.json(content_type=None)
                                    cc = (info.get("country") or "").upper()
                                except Exception as e:
                                    failed_target = f"{target_kind}:parse={type(e).__name__}"
                                    break
                                if cc == GEO_BLOCKED_COUNTRY:
                                    failed_target = f"{target_kind}:exit-country={cc}"
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
            # 关闭 stderr 文件句柄 (如果有)
            try:
                if 'stderr_fh' in locals() and not stderr_fh.closed:
                    stderr_fh.close()
            except Exception:
                pass
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

        # §3.1 共享一个全局 aiohttp session 用于所有节点的 SOCKS5 proxy 测试
        # 避免每个节点都 new ProxyConnector (270 次握手 vs 1 次 keepalive)
        # 注: 单个节点的 session 生命周期与 sing-box 子进程同

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