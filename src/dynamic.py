#!/usr/bin/env python3
"""
动态订阅源 - 优化版
从各种来源动态获取订阅链接和节点
"""
import re
import datetime
import asyncio
import aiohttp
from typing import List, Set, Optional, Callable, Any
from dataclasses import dataclass
import logging

logger = logging.getLogger(__name__)


@dataclass
class DynamicSource:
    """动态订阅源定义"""
    name: str
    fetcher: Callable
    description: str = ""
    enabled: bool = True


class DynamicFetcher:
    """动态订阅源获取器"""
    
    def __init__(self, session: Optional[aiohttp.ClientSession] = None):
        self.session = session
        self._own_session = session is None
    
    async def __aenter__(self):
        if self._own_session:
            self.session = aiohttp.ClientSession(
                timeout=aiohttp.ClientTimeout(total=15),
                headers={"User-Agent": "Mozilla/5.0"}
            )
        return self
    
    async def __aexit__(self, *args):
        if self._own_session and self.session:
            await self.session.close()
    
    async def fetch_text(self, url: str) -> Optional[str]:
        """获取文本内容"""
        if not self.session:
            return None
        try:
            async with self.session.get(url) as resp:
                if resp.status == 200:
                    return await resp.text()
        except Exception as e:
            logger.debug(f"Fetch error {url[:50]}...: {e}")
        return None
    
    async def fetch_github_dir(self, api_url: str) -> List[str]:
        """获取 GitHub 目录内容"""
        content = await self.fetch_text(api_url)
        if not content:
            return []
        
        import json
        try:
            items = json.loads(content)
            return [item.get('download_url', '') for item in items if item.get('download_url')]
        except:
            return []
    
    # ========== 内置动态源 ==========
    
    async def sharkdoor(self) -> Set[str]:
        """从 sharkDoor/vpn-free-nodes 获取"""
        now = datetime.datetime.now()
        api_url = now.strftime(
            'https://api.github.com/repos/sharkDoor/vpn-free-nodes/contents/node-list/%Y-%m?ref=master'
        )
        
        urls = await self.fetch_github_dir(api_url)
        if not urls:
            return set()
        
        # 获取最新文件
        latest_url = urls[-1] if urls else None
        if not latest_url:
            return set()
        
        content = await self.fetch_text(latest_url)
        if not content:
            return set()
        
        nodes = set()
        for line in content.split('\n'):
            if '://' in line:
                # 格式: name|protocol://...|...
                parts = line.split('|')
                for part in parts:
                    if '://' in part:
                        nodes.add(part)
        
        logger.info(f"[sharkdoor] Found {len(nodes)} nodes")
        return nodes
    
    async def peasoft(self) -> str:
        """从 peasoft Gist 获取"""
        content = await self.fetch_text(
            "https://gist.githubusercontent.com/peasoft/8a0613b7a2be881d1b793a6bb7536281/raw/"
        )
        if content:
            logger.info(f"[peasoft] Found content")
        return content or ""
    
    async def w1770946466(self) -> Set[str]:
        """从 w1770946466/Auto_proxy 获取"""
        content = await self.fetch_text(
            "https://raw.githubusercontent.com/w1770946466/Auto_proxy/main/README.md"
        )
        if not content:
            return set()
        
        subs = set()
        for line in content.strip().split('\n'):
            if line.startswith("`http"):
                sub = line.strip().strip('`')
                if not sub.startswith("https://raw.githubusercontent.com"):
                    subs.add(sub)
        
        logger.info(f"[w1770946466] Found {len(subs)} subscriptions")
        return subs
    
    async def crossxx_free(self) -> List[str]:
        """从 crossxx-labs/free-proxy 获取"""
        content = await self.fetch_text(
            "https://raw.githubusercontent.com/crossxx-labs/free-proxy/main/README.md"
        )
        if not content:
            return []
        
        urls = re.findall(
            r'https://clash\.crossxx\.com/sub/\w+/\d+',
            content
        )
        
        logger.info(f"[crossxx] Found {len(urls)} subscriptions")
        return list(set(urls))
    
    async def fetch_all_sources(self, sources: List[DynamicSource]) -> dict:
        """获取所有动态源"""
        results = {}
        
        async def fetch_one(source: DynamicSource):
            if not source.enabled:
                return source.name, None
            
            try:
                result = await source.fetcher()
                return source.name, result
            except Exception as e:
                logger.error(f"[{source.name}] Error: {e}")
                return source.name, None
        
        tasks = [fetch_one(s) for s in sources]
        for name, result in await asyncio.gather(*tasks):
            results[name] = result
        
        return results


# 预定义的动态源
DEFAULT_SOURCES = [
    DynamicSource(
        name="sharkdoor",
        fetcher=DynamicFetcher().sharkdoor,
        description="GitHub: sharkDoor/vpn-free-nodes"
    ),
    DynamicSource(
        name="peasoft",
        fetcher=DynamicFetcher().peasoft,
        description="peasoft Gist"
    ),
    DynamicSource(
        name="crossxx",
        fetcher=DynamicFetcher().crossxx_free,
        description="GitHub: crossxx-labs/free-proxy"
    ),
]


# ========== 兼容旧版接口 ==========

async def get_auto_urls() -> List[str]:
    """获取自动发现的订阅URL"""
    async with DynamicFetcher() as fetcher:
        urls = set()
        
        # sharkdoor
        nodes = await fetcher.sharkdoor()
        urls.update(nodes)
        
        # peasoft
        content = await fetcher.peasoft()
        if content:
            # 解析内容中的URL
            for line in content.split('\n'):
                if '://' in line:
                    urls.add(line.strip())
        
        return list(urls)


# 命令行测试
if __name__ == "__main__":
    async def test():
        async with DynamicFetcher() as fetcher:
            print("Testing dynamic sources...\n")
            
            # sharkdoor
            nodes = await fetcher.sharkdoor()
            print(f"sharkdoor: {len(nodes)} nodes")
            
            # peasoft
            content = await fetcher.peasoft()
            print(f"peasoft: {len(content)} chars")
            
            # crossxx
            urls = await fetcher.crossxx_free()
            print(f"crossxx: {len(urls)} URLs")
    
    asyncio.run(test())
