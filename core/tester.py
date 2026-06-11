"""
真实代理测试器
- 使用 sing-box 启动每个节点为本地 SOCKS5
- 真实 HTTP 请求测试连通性、延迟和基础带宽
- 支持多轮 retest，降低偶发可用节点进入 verified 的概率
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
from typing import Any, Dict, Iterable, List

import aiohttp
from aiohttp_socks import ProxyConnector

from core.parser import Node

TEST_TARGETS = [
    ("https://www.youtube.com/generate_204", "204"),
    ("https://www.google.com/generate_204", "204"),
    ("https://www.baidu.com/robots.txt", "cn-block"),
    ("https://ipinfo.io/json", "geo"),
    ("https://speed.cloudflare.com/__down?bytes=102400", "speed"),
]
SPEED_REQUIRED_BYTES = 100_000
SPEED_TIMEOUT_SEC = 8
GEO_BLOCKED_COUNTRY = "CN"
DEFAULT_MIN_LATENCY_MS = 30.0


@dataclass
class TestResult:
    node: Node
    success: bool = False
    latency_ms: float = 0.0
    jitter_ms: float = 0.0
    error: str = ""
    error_detail: Dict[str, Any] = field(default_factory=dict)
    round_passed: int = 0
    round_total: int = 0


def build_error_detail(error: str) -> Dict[str, Any]:
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
        "outbounds": [outbound, {"type": "direct", "tag": "direct"}],
        "route": {"final": outbound["tag"]},
    }


class SingBoxTester:
    def __init__(
        self,
        sb_path: str = "./sing-box",
        concurrency: int = 30,
        startup_wait: float = 0.6,
        request_timeout: float = 6.0,
        min_latency_ms: float = DEFAULT_MIN_LATENCY_MS,
        skip_target_kinds: Iterable[str] | None = None,
    ):
        if not os.path.exists(sb_path):
            raise FileNotFoundError(f"sing-box binary not found: {sb_path}")
        self.sb_path = os.path.abspath(sb_path)
        self.concurrency = concurrency
        self.startup_wait = startup_wait
        self.request_timeout = request_timeout
        self.min_latency_ms = min_latency_ms
        self.skip_target_kinds = set(skip_target_kinds or [])

    def _alloc_port(self) -> int:
        import random

        for _ in range(200):
            start = random.randint(30000, 49999)
            try:
                return _find_free_port(start, start + 1)
            except RuntimeError:
                continue
        raise RuntimeError("no free ports after 200 attempts")

    async def test_one(self, node: Node) -> TestResult:
        result = TestResult(node=node)
        try:
            port = self._alloc_port()
        except RuntimeError:
            result.error = "no free ports"
            return result

        tmpdir = tempfile.mkdtemp(prefix="sb-")
        config_path = os.path.join(tmpdir, "config.json")
        stderr_path = os.path.join(tmpdir, "sb.err")
        proc = None
        stderr_fh = None
        try:
            with open(config_path, "w", encoding="utf-8") as f:
                json.dump(build_singbox_config(node, port), f)

            stderr_fh = open(stderr_path, "w", encoding="utf-8")
            proc = await asyncio.create_subprocess_exec(
                self.sb_path,
                "run",
                "-c",
                config_path,
                stdout=asyncio.subprocess.DEVNULL,
                stderr=stderr_fh,
            )
            await asyncio.sleep(self.startup_wait)

            if proc.returncode is not None:
                stderr_fh.close()
                err_text = ""
                try:
                    with open(stderr_path, encoding="utf-8", errors="replace") as f:
                        err_text = f.read()[:500].strip()
                except Exception:
                    pass
                if err_text:
                    first_lines = " | ".join(
                        line.strip() for line in err_text.splitlines()[:3] if line.strip()
                    )[:300]
                    result.error = f"sing-box exited {proc.returncode}: {first_lines}"
                else:
                    result.error = f"sing-box exited {proc.returncode}"
                return result

            connector = ProxyConnector.from_url(f"socks5://127.0.0.1:{port}")
            async with aiohttp.ClientSession(connector=connector) as session:
                latencies = []
                failed_target = None
                for target_url, target_kind in TEST_TARGETS:
                    if target_kind in self.skip_target_kinds:
                        continue
                    started = time.monotonic()
                    try:
                        timeout = aiohttp.ClientTimeout(
                            total=SPEED_TIMEOUT_SEC if target_kind == "speed" else self.request_timeout
                        )
                        async with session.get(target_url, timeout=timeout) as resp:
                            if target_kind == "204":
                                if resp.status != 204:
                                    failed_target = f"{target_kind}:status={resp.status}"
                                    break
                                if await resp.read():
                                    failed_target = f"{target_kind}:non-empty-body"
                                    break
                            elif target_kind == "cn-block":
                                if resp.status != 200:
                                    failed_target = f"{target_kind}:status={resp.status}"
                                    break
                            elif target_kind == "geo":
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
                                if resp.status != 200:
                                    failed_target = f"{target_kind}:status={resp.status}"
                                    break
                                total = 0
                                async for chunk in resp.content.iter_chunked(8192):
                                    total += len(chunk)
                                if total < SPEED_REQUIRED_BYTES:
                                    failed_target = f"{target_kind}:only-{total}B"
                                    break
                        latencies.append((target_kind, (time.monotonic() - started) * 1000))
                    except Exception as e:
                        failed_target = f"{target_kind}:{type(e).__name__}"
                        break

                if failed_target is None and latencies:
                    latency_targets = [lat for kind, lat in latencies if kind != "speed"]
                    avg_latency = sum(latency_targets) / len(latency_targets) if latency_targets else latencies[0][1]
                    jitter = max(abs(lat - avg_latency) for lat in latency_targets) if len(latency_targets) >= 2 else 0.0
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
            try:
                if stderr_fh and not stderr_fh.closed:
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

    async def _test_all_once(self, nodes: List[Node], progress_every: int = 50) -> List[TestResult]:
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
            if r.round_total == 0:
                r.round_total = 1
                r.round_passed = 1 if r.success else 0
            results.append(r)
            done += 1
            if r.success:
                valid += 1
            if done % progress_every == 0 or done == len(nodes):
                print(f"  进度: {done}/{len(nodes)} 通过: {valid}", flush=True)
        return results

    async def test_all(
        self,
        nodes: List[Node],
        progress_every: int = 50,
        rounds: int = 1,
        retest_delay: float = 0.0,
    ) -> List[TestResult]:
        if rounds <= 1:
            return await self._test_all_once(nodes, progress_every)

        print(f"  [retest] 第 1/{rounds} 轮 ...", flush=True)
        round1 = await self._test_all_once(nodes, progress_every)
        round1_pass_nodes = [r.node for r in round1 if r.success]
        if not round1_pass_nodes:
            print("  [retest] 第 1 轮 0 通过，跳过后续轮次", flush=True)
            for r in round1:
                r.round_total = 1
                r.round_passed = 0
                if r.error and not r.error.startswith("retest:"):
                    r.error = f"retest:round1-fail:{r.error}"
            return round1

        if retest_delay > 0:
            print(f"  [retest] 第 1 轮通过 {len(round1_pass_nodes)}/{len(nodes)}，等待 {retest_delay}s 后复测 ...", flush=True)
            await asyncio.sleep(retest_delay)

        print(f"  [retest] 第 2/{rounds} 轮 ...", flush=True)
        round2 = await self._test_all_once(round1_pass_nodes, progress_every)

        r1_map = {r.node.fingerprint(): r for r in round1}
        r2_map = {r.node.fingerprint(): r for r in round2}
        merged: List[TestResult] = []
        for fp, r1 in r1_map.items():
            if not r1.success:
                r1.round_total = 1
                r1.round_passed = 0
                if r1.error and not r1.error.startswith("retest:"):
                    r1.error = f"retest:round1-fail:{r1.error}"
                merged.append(r1)
                continue

            r2 = r2_map.get(fp)
            if r2 and r2.success:
                merged.append(TestResult(
                    node=r1.node,
                    success=True,
                    latency_ms=(r1.latency_ms + r2.latency_ms) / 2,
                    jitter_ms=max(r1.jitter_ms, r2.jitter_ms),
                    round_passed=2,
                    round_total=2,
                ))
            else:
                merged.append(TestResult(
                    node=r1.node,
                    success=False,
                    error=f"retest:round2-fail:{r2.error if r2 else 'missing'}",
                    round_passed=1,
                    round_total=2,
                ))

        final_pass = sum(1 for r in merged if r.success)
        print(f"  [retest] 最终通过 {final_pass}/{len(nodes)}", flush=True)
        return merged

    async def test_all_single(self, nodes: List[Node], progress_every: int = 50) -> List[TestResult]:
        return await self.test_all(nodes, progress_every, rounds=1)
