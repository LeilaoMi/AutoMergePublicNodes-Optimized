"""GlobalPing 国内探针 TCP 连通性检查。

从中国境内的 GlobalPing 探针向节点发起 TCP traceroute，
验证"中国用户 → 节点"第一跳是否可达。补上海外 CI 测不到的视角。

免费额度：匿名 250 次/小时。300 节点/轮 ≈ 300 次测量，在额度内。
"""
from __future__ import annotations

import asyncio
import json
import time
import urllib.request
from typing import Dict, List, Tuple, Any

API_BASE = "https://api.globalping.io/v1"
# 每次测量用的国内探针数。1 个够用，2 个更稳（但消耗翻倍）。
CN_PROBE_LIMIT = 1
# 创建测量后的轮询间隔与总超时
POLL_INTERVAL_SEC = 5
POLL_TIMEOUT_SEC = 60
# 并发创建测量的数量（GlobalPing 限流 250/小时，保守取 30 并发）
CREATE_CONCURRENCY = 30


def _api(method: str, path: str, data: dict | None = None) -> dict:
    url = f"{API_BASE}{path}"
    headers = {"Content-Type": "application/json", "User-Agent": "AutoMergePublicNodes-Optimized/2.4"}
    body = json.dumps(data).encode() if data else None
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def _create_measurement(server: str, port: int) -> str:
    payload = {
        "type": "traceroute",
        "target": server,
        "locations": [{"country": "CN", "limit": CN_PROBE_LIMIT}],
        "measurementOptions": {"protocol": "TCP", "port": port},
    }
    result = _api("POST", "/measurements", payload)
    return result["id"]


def _get_measurement(mid: str) -> dict:
    return _api("GET", f"/measurements/{mid}")


def _is_reachable(measurement: dict) -> bool:
    """traceroute 到达目标 IP 即判定为 TCP 可达。"""
    for res in measurement.get("results", []):
        hops = res.get("result", {}).get("hops") or []
        if hops and hops[-1].get("resolvedAddress"):
            return True
    return False


async def check_china_reachability(
    nodes: List[Tuple[Any, float, float]],
    timeout: float = 300.0,
) -> Dict[str, bool]:
    """对通过海外真测的节点做国内 TCP 可达性检查。

    Args:
        nodes: [(node, latency_ms, jitter_ms), ...]，node 需有 .server/.server_port/.fingerprint()
        timeout: 整个检查的总超时（秒）

    Returns:
        {fingerprint: True/False}，True=国内可达。API 失败或超时的节点记为 False。
    """
    results: Dict[str, bool] = {}
    if not nodes:
        return results

    sem = asyncio.Semaphore(CREATE_CONCURRENCY)
    loop = asyncio.get_event_loop()

    async def _check_one(node) -> Tuple[str, bool]:
        fp = node.fingerprint()
        async with sem:
            try:
                mid = await loop.run_in_executor(None, _create_measurement, node.server, node.server_port)
            except Exception:
                return fp, False
        # 轮询等结果
        deadline = time.time() + POLL_TIMEOUT_SEC
        while time.time() < deadline:
            await asyncio.sleep(POLL_INTERVAL_SEC)
            try:
                m = await loop.run_in_executor(None, _get_measurement, mid)
            except Exception:
                continue
            if m.get("status") == "finished":
                return fp, _is_reachable(m)
        return fp, False

    try:
        done = await asyncio.wait_for(
            asyncio.gather(*[_check_one(n) for n, _, _ in nodes]),
            timeout=timeout,
        )
        for fp, ok in done:
            results[fp] = ok
    except asyncio.TimeoutError:
        pass
    # 没拿到结果的按不可达处理（保守）
    for n, _, _ in nodes:
        results.setdefault(n.fingerprint(), False)
    return results
