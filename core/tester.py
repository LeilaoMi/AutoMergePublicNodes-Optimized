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
from dataclasses import dataclass, field
from typing import Any, Dict, List, Iterable, Optional

import aiohttp
from aiohttp_socks import ProxyConnector

from core._tester_concurrency import (
    ConcurrencyConfig,
    ProcessPoolGate,
    build_concurrency_config,
)
from core.parser import Node


# 测试目标 4 层
# - 204: youtube / google 204 = 真的墙外节点, 不能直连的才是好节点
# - cn-block: 必须能访问中国大陆站 (baidu), 否则节点根本没流量代理能力
# - geo: 出口 IP 不能是中国 (cloudflare trace), 否则就是"挂在中国机房的出口", 没意义
# - speed: 必须真的能下完 100KB, 证明可承载真实流量
# 第 4 层为带宽测试，能下完才算"真用得起来"
TEST_TARGETS = [
    ("https://www.youtube.com/generate_204",   "204"),
    ("https://www.google.com/generate_204",    "204"),
    ("https://www.baidu.com/robots.txt",       "cn-block"),
    ("https://www.cloudflare.com/cdn-cgi/trace", "geo"),
    ("https://speed.cloudflare.com/__down?bytes=102400", "speed"),
]
SPEED_REQUIRED_BYTES = 100_000
SPEED_TIMEOUT_SEC = 8

# 可选的解锁检测（不影响 pass/fail，只记录能力）
# [P1-3] 扩为能力画像：每个能力独立检测、独立字段
UNLOCK_TARGETS = [
    ("https://www.netflix.com/title/81215567",   "netflix"),
    ("https://chat.openai.com/cdn-cgi/trace",     "chatgpt"),
    ("https://www.disneyplus.com/",               "disney"),
    ("https://www.youtube.com/premium",          "youtube_premium"),
    ("https://t.me/",                            "telegram"),
    ("https://github.com/",                      "github"),
]

# exit-ip geo check 通过时, body 里 country 字段不能等于这个
GEO_BLOCKED_COUNTRY = "CN"

# [v2.5] DNS 泄露检测目标
DNS_LEAK_TARGET = ("https://dnsleaktest.com/api/v1/query", "dns-leak")

DEFAULT_MIN_LATENCY_MS = 30.0  # 低于此值视为可疑节点；可通过 CLI 设为 0 关闭


@dataclass
class TestResult:
    node: Node
    success: bool = False
    latency_ms: float = 0.0
    jitter_ms: float = 0.0  # 延迟抖动（max deviation from avg）
    error: str = ""
    error_detail: Dict[str, Any] = field(default_factory=dict)
    speed_kbps: float = 0.0  # 下载速度 KB/s
    netflix_ok: bool = False  # Netflix 解锁（兼容旧字段）
    chatgpt_ok: bool = False  # ChatGPT 可访问（兼容旧字段）
    # [P1-3] 结构化能力画像
    capabilities: Dict[str, bool] = field(default_factory=dict)
    capability_latency_ms: Dict[str, float] = field(default_factory=dict)
    # [v2.5] DNS 泄露 + 协议指纹对抗
    dns_leak: bool = False  # True = 检测到 DNS 泄露
    fingerprint_resistance: str = ""  # high/medium/low/none
    fingerprint_resistance_score: float = 0.0  # [v2.5.1] 0~1 数值，供评分系统直接使用


def build_error_detail(error: str) -> Dict[str, Any]:
    """Parse tester error strings into a stable diagnostic shape."""
    if not error:
        return {"target": "unknown", "reason": "unknown", "raw": ""}
    if ":" not in error:
        return {"target": "general", "reason": error, "raw": error}
    target, rest = error.split(":", 1)
    detail: Dict[str, Any] = {"target": target, "raw": error}
    if "=" in rest:
        reason, value = rest.split("=", 1)
        detail["reason"] = reason
        detail["value"] = value
        if reason == "status":
            try:
                detail["status"] = int(value)
            except ValueError:
                pass
        elif reason in {"only", "only-bytes"}:
            digits = "".join(ch for ch in value if ch.isdigit())
            if digits:
                detail["bytes"] = int(digits)
    else:
        detail["reason"] = rest
    return detail


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
    """构造 sing-box 临时配置：SOCKS5 入站 + 节点出站

    §1.6 (紧急修复) — sing-box 1.11+ 移除了 inbound 上的 sniff 字段, 移到 route rule action
    之前用 {inbound: sniff: True} 在 1.13+ 报 "legacy inbound fields are deprecated" + exit 1
    新格式: inbounds 只保留 type/tag/listen/listen_port
    """
    inbound = {
        "type": "socks",
        "tag": "socks-in",
        "listen": "127.0.0.1",
        "listen_port": socks_port,
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
                 min_latency_ms: float = DEFAULT_MIN_LATENCY_MS,
                 skip_target_kinds: Iterable[str] | None = None,
                 process_pool_size: Optional[int] = None,
                 io_concurrency: Optional[int] = None,
                 probe_only: bool = False):
        """真实测试器。

        兼容旧签名：concurrency 同时被当作 IO 并发上限。P0-1 之后推荐显式传
        process_pool_size + io_concurrency；不传则按 build_concurrency_config 推断。

        Args:
            sb_path: sing-box 可执行文件路径
            concurrency: 向后兼容参数；当 io_concurrency 未传时同时充当 IO 并发上限
            process_pool_size: sing-box 进程数上限（None=自动推断）
            io_concurrency: IO 任务并发上限（None=用 concurrency）
            probe_only: 轻量探活模式，只测 204 快速探活，geo/解锁检测留给完整真测阶段
        """
        if not os.path.exists(sb_path):
            raise FileNotFoundError(f"sing-box binary not found: {sb_path}")
        self.sb_path = os.path.abspath(sb_path)
        self.startup_wait = startup_wait
        self.request_timeout = request_timeout
        self.min_latency_ms = min_latency_ms
        self.skip_target_kinds = set(skip_target_kinds or [])
        self.probe_only = probe_only
        self._port_counter = 30000

        # [P0-1] 进程池与 IO 并发解耦
        if process_pool_size is None and io_concurrency is None:
            cfg = build_concurrency_config(concurrency=concurrency)
        else:
            cfg = build_concurrency_config(
                concurrency=io_concurrency if io_concurrency is not None else concurrency,
                process_pool_size=process_pool_size,
            )
        self.concurrency: int = cfg.io_concurrency
        self.process_pool_size: int = cfg.process_pool_size
        self._proc_gate: Optional[ProcessPoolGate] = None
        self._proc_gate_init_lock: Optional[asyncio.Lock] = None

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
        # [P0-1] 进程池门：抢到进程槽后才能启动 sing-box 子进程
        # probe_only 模式跳过进程池门：探活只测 204，sing-box 生命周期极短，
        # 100 并发直接全开比排队抢 4 个进程槽快 20+ 倍
        if self.probe_only:
            return await self._test_one_inner(node)
        proc_gate = self._acquire_proc()
        async with proc_gate:
            return await self._test_one_inner(node)

    async def _test_one_inner(self, node: Node) -> TestResult:
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
                speed_download_bytes = 0
                speed_download_time = 0.0

                # probe 模式: 只测 204 快速探活, geo 检测留给完整真测阶段(超时更宽裕)
                probe_targets = TEST_TARGETS[:1] if self.probe_only else TEST_TARGETS
                for target_url, target_kind in probe_targets:
                    if target_kind in self.skip_target_kinds:
                        continue

                    if target_kind == "204":
                        # 多采样：对 204 目标做 3 次取中位数
                        samples = []
                        for _ in range(3):
                            tstart = time.monotonic()
                            try:
                                timeout = aiohttp.ClientTimeout(total=self.request_timeout)
                                async with session.get(target_url, timeout=timeout) as resp:
                                    if resp.status != 204:
                                        failed_target = f"{target_kind}:status={resp.status}"
                                        break
                                    body = await resp.read()
                                    if body:
                                        failed_target = f"{target_kind}:non-empty-body"
                                        break
                                    samples.append((time.monotonic() - tstart) * 1000)
                            except Exception as e:
                                failed_target = f"{target_kind}:{type(e).__name__}"
                                break
                        if failed_target:
                            break
                        if samples:
                            samples.sort()
                            median = samples[len(samples) // 2]
                            # [v2.5] 离群值检测：如果最大值超过中位数 5 倍且 > 500ms，
                            # 说明节点有严重抖动，用均值惩罚而非直接取中位数
                            max_val = samples[-1]
                            if max_val > median * 5 and max_val > 500:
                                median = (median + max_val) / 2
                            latencies.append((target_kind, median))
                        continue

                    tstart = time.monotonic()
                    try:
                        timeout = aiohttp.ClientTimeout(total=SPEED_TIMEOUT_SEC if target_kind == "speed" else self.request_timeout)
                        async with session.get(target_url, timeout=timeout) as resp:
                            if target_kind == "cn-block":
                                if resp.status != 200:
                                    failed_target = f"{target_kind}:status={resp.status}"
                                    break
                            elif target_kind == "geo":
                                if resp.status != 200:
                                    failed_target = f"{target_kind}:status={resp.status}"
                                    break
                                try:
                                    text = (await resp.text()) or ""
                                    cc = ""
                                    exit_ip = ""
                                    for line in text.splitlines():
                                        if line.startswith("loc="):
                                            cc = line[4:].strip().upper()
                                        elif line.startswith("ip="):
                                            exit_ip = line[3:].strip()
                                except Exception as e:
                                    failed_target = f"{target_kind}:parse={type(e).__name__}"
                                    break
                                if cc == GEO_BLOCKED_COUNTRY:
                                    failed_target = f"{target_kind}:exit-country={cc}"
                                    break
                                # [v2.5] 保存出口 IP，供后续 DNS 泄露检测比对
                                if exit_ip:
                                    result.capabilities["geo_ip"] = exit_ip
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
                                speed_download_bytes = total
                                speed_download_time = time.monotonic() - tstart
                        latencies.append((target_kind, (time.monotonic() - tstart) * 1000))
                    except Exception as e:
                        failed_target = f"{target_kind}:{type(e).__name__}"
                        break

                # 解锁检测（只在核心测试通过后做，不影响 pass/fail）
                # [P1-3] 结构化能力画像：每个能力独立检测、记延迟
                if failed_target is None and latencies:
                    for unlock_url, unlock_kind in UNLOCK_TARGETS:
                        t0 = time.monotonic()
                        try:
                            timeout = aiohttp.ClientTimeout(total=self.request_timeout)
                            async with session.get(unlock_url, timeout=timeout, allow_redirects=False) as resp:
                                ok = False
                                if unlock_kind == "netflix":
                                    # [v2.5] 深度检测：检查响应体而非仅状态码
                                    # Netflix 对代理 IP 可能返回 200 但内容是 "Not Available"
                                    if resp.status == 200:
                                        try:
                                            body = await resp.text()
                                            ok = ("Netflix Original" in body or
                                                  "81215567" in body or
                                                  "stranger" in body.lower())
                                        except Exception:
                                            ok = False
                                    else:
                                        ok = False
                                elif unlock_kind == "chatgpt":
                                    # [v2.5] 深度检测：检查是否被地域限制
                                    if resp.status == 200:
                                        try:
                                            body = await resp.text()
                                            ok = "blocked" not in body.lower() and "not available" not in body.lower()
                                        except Exception:
                                            ok = True  # 能拿到 200 就算通过
                                    else:
                                        ok = False
                                elif unlock_kind == "disney":
                                    # Disney+: 200/301/302 都算可访问
                                    ok = resp.status in (200, 301, 302)
                                elif unlock_kind == "youtube_premium":
                                    # YouTube Premium: 首页可访问即可
                                    ok = resp.status == 200
                                elif unlock_kind == "telegram":
                                    # Telegram Web: 200 即可
                                    ok = resp.status == 200
                                elif unlock_kind == "github":
                                    # GitHub: 200/301/302
                                    ok = resp.status in (200, 301, 302)
                                result.capabilities[unlock_kind] = ok
                                if ok:
                                    result.capability_latency_ms[unlock_kind] = round(
                                        (time.monotonic() - t0) * 1000, 1
                                    )
                        except Exception:
                            # 解锁检测失败 = 该能力不可用
                            result.capabilities[unlock_kind] = False
                    # [P1-3] 同步回填到旧字段，保持 main.py/stats.json 兼容
                    result.netflix_ok = result.capabilities.get("netflix", False)
                    result.chatgpt_ok = result.capabilities.get("chatgpt", False)

                    # [v2.5] DNS 泄露检测：通过代理请求 DNS leak 测试 API
                    # 如果返回的 DNS resolver IP 与出口 IP 不同 = DNS 泄露
                    try:
                        dns_url, _ = DNS_LEAK_TARGET
                        dns_timeout = aiohttp.ClientTimeout(total=5)
                        async with session.get(dns_url, timeout=dns_timeout) as dns_resp:
                            if dns_resp.status == 200:
                                dns_info = await dns_resp.json(content_type=None)
                                # 比较 DNS resolver IP 与出口 IP
                                geo_ip = result.capabilities.get("geo_ip", "")
                                dns_ip = dns_info.get("ip", "") or dns_info.get("resolver_ip", "")
                                if geo_ip and dns_ip and geo_ip != dns_ip:
                                    result.dns_leak = True
                                    result.capabilities["dns_leak"] = True
                    except Exception:
                        pass  # DNS 泄露检测失败不影响结果

                    # [v2.5] 协议指纹对抗分析
                    from core._fingerprint_test import analyze_fingerprint_resistance
                    fp_analysis = analyze_fingerprint_resistance(node)
                    result.fingerprint_resistance = fp_analysis["resistance"]
                    result.fingerprint_resistance_score = fp_analysis["score"]  # [v2.5.1] 数值版
                    result.capabilities["fingerprint_resistance"] = fp_analysis["resistance"]

                if failed_target is None and latencies:
                    # 取非下载目标的平均延迟（不算下载耗时）
                    latency_targets = [lat for kind, lat in latencies if kind != "speed"]
                    avg_latency = sum(latency_targets) / len(latency_targets) if latency_targets else latencies[0][1]
                    jitter = max(abs(l - avg_latency) for l in latency_targets) if len(latency_targets) >= 2 else 0.0
                    if self.min_latency_ms > 0 and avg_latency < self.min_latency_ms:
                        result.error = f"latency-too-low:{avg_latency:.1f}ms"
                    else:
                        result.success = True
                        result.latency_ms = avg_latency
                        result.jitter_ms = jitter
                        # 量化下载速度
                        if speed_download_bytes > 0 and speed_download_time > 0:
                            result.speed_kbps = round(speed_download_bytes / 1024 / speed_download_time, 1)
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

        if result.error and not result.error_detail:
            result.error_detail = build_error_detail(result.error)
        return result

    async def test_all(self, nodes: List[Node], progress_every: int = 50) -> List[TestResult]:
        io_sem = asyncio.Semaphore(self.concurrency)
        # [P0-1] 进程池 Semaphore：单次 test_all 内部所有 IO 任务共享
        if self._proc_gate is None:
            # 必须在事件循环内初始化，所以放这里
            self._proc_gate = ProcessPoolGate(self.process_pool_size)
        results: List[TestResult] = []
        done = 0
        valid = 0

        # §3.1 共享一个全局 aiohttp session 用于所有节点的 SOCKS5 proxy 测试
        # 避免每个节点都 new ProxyConnector (270 次握手 vs 1 次 keepalive)
        # 注: 单个节点的 session 生命周期与 sing-box 子进程同

        async def _wrap(n: Node) -> TestResult:
            # [P0-1] 先抢 IO 槽，再抢进程池槽；进程池槽在 test_one 内部释放
            async with io_sem:
                return await self.test_one(n)

        tasks = [asyncio.create_task(_wrap(n)) for n in nodes]
        for fut in asyncio.as_completed(tasks):
            r = await fut
            results.append(r)
            done += 1
            if r.success:
                valid += 1
            if done % progress_every == 0 or done == len(nodes):
                # [P0-1] 在进度日志里把进程池/IO 并发配比打出来，便于调优
                proc_avail = self._proc_gate.available if self._proc_gate else -1
                print(
                    f"  进度: {done}/{len(nodes)} 通过: {valid} "
                    f"(io_concurrency={self.concurrency}, "
                    f"process_pool_size={self.process_pool_size}, "
                    f"proc_avail={proc_avail})",
                    flush=True,
                )
        return results

    def _acquire_proc(self) -> "ProcessPoolGate":
        """拿当前事件循环的进程池门。test_one 内部 await self._proc_gate 用。"""
        if self._proc_gate is None:
            # 第一次调用可能在事件循环外或没有初始化；兜底建一个
            self._proc_gate = ProcessPoolGate(self.process_pool_size)
        return self._proc_gate