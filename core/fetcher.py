"""
订阅源抓取器
- 异步并发抓取
- 支持动态 URL (日期模板 %Y/%m/%d)
- 支持订阅列表 (一个 URL 中含多个 URL)
- 自动 base64 解码
- 重试机制
"""
from __future__ import annotations

import asyncio
import datetime
import re
from dataclasses import dataclass, field
from typing import List, Optional, Set, Tuple

import aiohttp
import yaml

from core.parser import Node, parse_content


@dataclass
class Source:
    url: str
    name: str = ""                # 来源名称
    kind: str = "url"             # url | dynamic | list
    enabled: bool = True
    ignore_protocols: Set[str] = field(default_factory=set)
    max_nodes: int = 0            # 0 表示不限

    @property
    def resolved_url(self) -> str:
        """处理动态 URL（日期模板）"""
        if "%" not in self.url:
            return self.url
        now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8)))
        return now.strftime(self.url)


@dataclass
class FetchResult:
    source: Source
    success: bool = False
    nodes: List[Node] = field(default_factory=list)
    error: str = ""
    duration: float = 0.0
    bytes_received: int = 0


JSDELIVR_RE = re.compile(r"https?://raw\.githubusercontent\.com/([^/]+)/([^/]+)/(?:refs/heads/)?([^/]+)/(.+)")


def to_jsdelivr(url: str) -> str:
    """将 raw.githubusercontent.com 转 jsdelivr CDN（国内更稳定）"""
    m = JSDELIVR_RE.match(url)
    if not m:
        return url
    user, repo, branch, path = m.groups()
    return f"https://cdn.jsdelivr.net/gh/{user}/{repo}@{branch}/{path}"


async def _fetch_one(session: aiohttp.ClientSession, url: str, timeout: int = 15, retries: int = 2) -> Tuple[bool, str, int]:
    """抓取单个 URL，返回 (成功, 内容/错误, 字节数)，带重试"""
    last_err = ""
    for attempt in range(retries + 1):
        try:
            async with session.get(url, timeout=aiohttp.ClientTimeout(total=timeout)) as resp:
                if resp.status != 200:
                    last_err = f"HTTP {resp.status}"
                    if resp.status == 429 and attempt < retries:
                        await asyncio.sleep(1.5 * (attempt + 1))
                        continue
                    return False, last_err, 0
                data = await resp.read()
                try:
                    text = data.decode("utf-8", errors="replace")
                except Exception:
                    text = ""
                return True, text, len(data)
        except asyncio.TimeoutError:
            last_err = "timeout"
            if attempt < retries:
                await asyncio.sleep(0.5 * (attempt + 1))
                continue
            return False, "timeout", 0
        except Exception as e:
            last_err = str(e)[:100]
            if attempt < retries:
                await asyncio.sleep(0.5 * (attempt + 1))
                continue
            return False, last_err, 0
    return False, last_err, 0


async def fetch_source(session: aiohttp.ClientSession, src: Source, timeout: int = 15) -> FetchResult:
    """抓取单个订阅源"""
    start = asyncio.get_event_loop().time()
    result = FetchResult(source=src)

    url = src.resolved_url

    # 先尝试原始 URL，失败则尝试 jsdelivr CDN
    candidates = [url]
    cdn = to_jsdelivr(url)
    if cdn != url:
        candidates.append(cdn)

    last_err = ""
    text = ""
    for candidate in candidates:
        ok, content, n_bytes = await _fetch_one(session, candidate, timeout, retries=2)
        if ok:
            text = content
            result.bytes_received = n_bytes
            break
        last_err = content

    if not text:
        result.error = last_err
        result.duration = asyncio.get_event_loop().time() - start
        return result

    # 订阅列表：每行是另一个 URL
    if src.kind == "list":
        sub_urls = []
        for line in text.splitlines():
            line = line.strip()
            if line and "://" in line and not line.startswith("#"):
                sub_urls.append(line)
        # 递归抓取（限制深度为 1）
        for sub_url in sub_urls[:50]:  # 防止失控
            ok, content, _ = await _fetch_one(session, sub_url, timeout)
            if ok:
                result.nodes.extend(parse_content(content))
    else:
        result.nodes = parse_content(text)

    # 协议过滤
    if src.ignore_protocols:
        result.nodes = [n for n in result.nodes if n.type not in src.ignore_protocols]

    # 数量限制
    if src.max_nodes > 0 and len(result.nodes) > src.max_nodes:
        result.nodes = result.nodes[:src.max_nodes]

    result.success = True
    result.duration = asyncio.get_event_loop().time() - start
    return result


async def fetch_all(sources: List[Source], concurrency: int = 30, timeout: int = 15) -> List[FetchResult]:
    """并发抓取所有订阅源"""
    sem = asyncio.Semaphore(concurrency)
    connector = aiohttp.TCPConnector(limit=concurrency * 2, ssl=False)
    headers = {
        "User-Agent": "ClashforWindows/0.20.39 (clash-meta)",
        "Accept": "*/*",
    }

    async def _wrapped(session, src):
        async with sem:
            return await fetch_source(session, src, timeout)

    async with aiohttp.ClientSession(connector=connector, headers=headers) as session:
        tasks = [_wrapped(session, s) for s in sources if s.enabled]
        return await asyncio.gather(*tasks)


def load_sources(path: str) -> List[Source]:
    """从 YAML 配置加载订阅源"""
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}

    sources: List[Source] = []
    for entry in data.get("sources", []):
        if isinstance(entry, str):
            sources.append(Source(url=entry))
        elif isinstance(entry, dict):
            src = Source(
                url=entry["url"],
                name=entry.get("name", ""),
                kind=entry.get("kind", "url"),
                enabled=entry.get("enabled", True),
                ignore_protocols=set(entry.get("ignore_protocols", [])),
                max_nodes=int(entry.get("max_nodes", 0)),
            )
            sources.append(src)
    return sources
