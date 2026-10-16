"""GlobalPing 国内探针 TCP 连通性检查。

从中国境内的 GlobalPing 探针向节点端口发起 TCP ping（真实三次握手），
验证"中国用户 → 节点"是否可达。补上海外 CI 测不到的视角。

不用 traceroute：国际链路常超过 20 跳且末段不回 ICMP，traceroute 末跳多为空，
实测把能握手成功的节点也判成不可达。

额度（https://globalping.io/credits）：
- 匿名：每 IP 每小时 250 次测试（GitHub Runner 的出口 IP 是共享的，额度可能已被他人消耗）
- 登录 token：每账号每小时 500 次（同一账号的所有 token 共用）

因此本模块：
1. 先查 /v1/limits 拿剩余额度，按剩余额度 - reserve 收缩本轮预算，且不超过 max_checks；
2. 只检查调用方传入顺序（已按评分排序）里的前 N 个节点；
3. 区分三态：True=国内可达，False=实测不可达，None=未测/额度用完/探针故障（未知）。
   未知不等于不可达，调用方不应把未知节点当坏节点丢弃。

可选环境变量 GLOBALPING_TOKEN：有则带 Bearer 认证（注意与同账号其他项目共用额度）。
"""
from __future__ import annotations

import asyncio
import ipaddress
import json
import os
import time
import urllib.error
import urllib.request
from typing import Any, Dict, List, Optional, Tuple

API_BASE = "https://api.globalping.io/v1"
# 每次测量用的国内探针数（1 个探针 = 1 次测试额度）
CN_PROBE_LIMIT = 1
# 每次 TCP ping 的握手次数（额度按探针计，与次数无关）
TCP_PING_PACKETS = 3
# 创建测量后的轮询间隔与单测量超时
POLL_INTERVAL_SEC = 3
POLL_TIMEOUT_SEC = 60
# 并发创建测量的数量
CREATE_CONCURRENCY = 20
# 单轮最多检查多少个节点（verified 只需要 top_n 个，没必要全测）
DEFAULT_MAX_CHECKS = 200
# 给同 IP / 同账号的其他任务留的余量
DEFAULT_RESERVE = 20


class RateLimited(Exception):
    """GlobalPing 返回 429：本小时额度已用完。"""


def _headers(token: str = "") -> Dict[str, str]:
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "AutoMergePublicNodes-Optimized/2.4 (+https://github.com/LeilaoMi/AutoMergePublicNodes-Optimized)",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


def _api(method: str, path: str, data: dict | None = None, token: str = "") -> dict:
    url = f"{API_BASE}{path}"
    body = json.dumps(data).encode() if data else None
    req = urllib.request.Request(url, data=body, headers=_headers(token), method=method)
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        if e.code == 429:
            raise RateLimited(str(e)) from e
        raise


def read_remaining_tests(token: str = "") -> Optional[int]:
    """返回本小时剩余可创建的测试次数；查询失败返回 None。"""
    try:
        data = _api("GET", "/limits", token=token)
    except Exception:
        return None
    try:
        return int(data["rateLimit"]["measurements"]["create"]["remaining"])
    except (KeyError, TypeError, ValueError):
        return None


def plan_budget(candidates: int, remaining: Optional[int], max_checks: int = DEFAULT_MAX_CHECKS,
                reserve: int = DEFAULT_RESERVE, per_target: int = CN_PROBE_LIMIT) -> int:
    """本轮最多检查多少个节点。remaining 未知时按 max_checks 尝试（429 时会提前停）。"""
    budget = min(candidates, max(0, max_checks))
    if remaining is not None:
        affordable = max(0, remaining - reserve) // max(per_target, 1)
        budget = min(budget, affordable)
    return budget


def _create_measurement(server: str, port: int, token: str = "") -> str:
    payload = {
        "type": "ping",
        "target": server,
        "locations": [{"country": "CN", "limit": CN_PROBE_LIMIT}],
        "measurementOptions": {"protocol": "TCP", "port": port, "packets": TCP_PING_PACKETS},
    }
    result = _api("POST", "/measurements", payload, token=token)
    return result["id"]


def _get_measurement(mid: str, token: str = "") -> dict:
    return _api("GET", f"/measurements/{mid}", token=token)


def _same_ip(a: str, b: str) -> bool:
    try:
        return ipaddress.ip_address(a) == ipaddress.ip_address(b)
    except ValueError:
        return False


def is_reachable(measurement: dict, target_ip: str = "") -> Optional[bool]:
    """解析 TCP ping 结果。

    True：至少一次握手成功。
    False：探针正常完成但全部握手失败。
    None：探针离线/失败/无结果，无法判断。
    """
    any_finished = False
    for res in measurement.get("results", []) or []:
        result = res.get("result", {}) or {}
        if result.get("status") in ("failed", "offline"):
            continue
        stats = result.get("stats") or {}
        if "rcv" not in stats:
            continue
        any_finished = True
        try:
            if int(stats.get("rcv") or 0) > 0:
                return True
        except (TypeError, ValueError):
            continue
    return False if any_finished else None


async def check_china_reachability(
    nodes: List[Tuple[Any, float, float]],
    timeout: float = 300.0,
    max_checks: int = DEFAULT_MAX_CHECKS,
    reserve: int = DEFAULT_RESERVE,
    token: Optional[str] = None,
) -> Dict[str, Optional[bool]]:
    """对通过海外真测的节点做国内 TCP 可达性检查。

    Args:
        nodes: [(node, latency_ms, jitter_ms), ...]，应已按评分排序；只检查前 budget 个。
        timeout: 整个检查的总超时（秒）
        max_checks: 单轮最多检查的节点数
        reserve: 给其他任务预留的测试额度
        token: GlobalPing token；None 时读环境变量 GLOBALPING_TOKEN

    Returns:
        {fingerprint: True/False/None}。None 表示未知（未测、额度用完、探针故障）。
    """
    results: Dict[str, Optional[bool]] = {}
    if not nodes:
        return results
    if token is None:
        token = os.environ.get("GLOBALPING_TOKEN", "")

    loop = asyncio.get_event_loop()
    remaining = await loop.run_in_executor(None, read_remaining_tests, token)
    budget = plan_budget(len(nodes), remaining, max_checks=max_checks, reserve=reserve)
    print(f"      GlobalPing 剩余额度: {remaining if remaining is not None else '未知'}，本轮检查 {budget}/{len(nodes)} 个")

    # 同一 server:port 只测一次
    targets: List[Tuple[str, int]] = []
    seen = set()
    for n, _, _ in nodes:
        key = (n.server, int(n.server_port))
        if key in seen:
            continue
        seen.add(key)
        targets.append(key)
        if len(targets) >= budget:
            break

    sem = asyncio.Semaphore(CREATE_CONCURRENCY)
    rate_limited = asyncio.Event()
    by_target: Dict[Tuple[str, int], Optional[bool]] = {}

    async def _check_one(server: str, port: int) -> None:
        key = (server, port)
        async with sem:
            if rate_limited.is_set():
                by_target[key] = None
                return
            try:
                mid = await loop.run_in_executor(None, _create_measurement, server, port, token)
            except RateLimited:
                rate_limited.set()
                by_target[key] = None
                return
            except Exception:
                by_target[key] = None
                return
        deadline = time.time() + POLL_TIMEOUT_SEC
        while time.time() < deadline:
            await asyncio.sleep(POLL_INTERVAL_SEC)
            try:
                m = await loop.run_in_executor(None, _get_measurement, mid, token)
            except Exception:
                continue
            if m.get("status") == "finished":
                by_target[key] = is_reachable(m)
                return
        by_target[key] = None

    try:
        await asyncio.wait_for(
            asyncio.gather(*[_check_one(s, p) for s, p in targets]),
            timeout=timeout,
        )
    except asyncio.TimeoutError:
        pass
    if rate_limited.is_set():
        print("      GlobalPing 额度用完，剩余节点记为未知")

    for n, _, _ in nodes:
        results[n.fingerprint()] = by_target.get((n.server, int(n.server_port)))
    return results
