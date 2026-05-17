#!/usr/bin/env python3
"""
异步订阅获取器 - 优化版
支持：动态日期URL、订阅列表递归获取、并发控制
"""
import asyncio
import aiohttp
import re
import datetime
from typing import List, Set, Dict, Any, Optional, Callable
from dataclasses import dataclass, field
from urllib.parse import urlparse
import logging

from .node import Node, b64decode, b64encode

logger = logging.getLogger(__name__)


@dataclass
class FetchResult:
    """获取结果"""
    url: str
    nodes: List[Node] = field(default_factory=list)
    error: Optional[str] = None
    count: int = 0


@dataclass
class SourceConfig:
    """订阅源配置"""
    url: str
    is_china: bool = False      # ! 前缀
    is_date: bool = False       # +date 前缀
    is_list: bool = False       # * 前缀
    max_nodes: int = 0          # max=N 参数
    ignore_protos: Set[str] = field(default_factory=set)  # ignore=A,B 参数
    
    @classmethod
    def parse(cls, line: str) -> Optional["SourceConfig"]:
        """解析 sources.list 行"""
        line = line.strip()
        if not line or line.startswith('#') or line == 'EOF':
            return None
        
        is_china = False
        is_date = False
        is_list = False
        max_nodes = 0
        ignore_protos = set()
        
        # 解析前缀
        while line and line[0] in '!+*':
            if line[0] == '!':
                is_china = True
            elif line[0] == '+':
                is_date = True
            elif line[0] == '*':
                is_list = True
            line = line[1:].strip()
        
        # 解析参数 #max=100&ignore=vmess,ss
        if '#' in line:
            line, params_part = line.rsplit('#', 1)
            # 检查是否是配置参数
            if '=' in params_part:
                for param in params_part.split('&'):
                    if '=' in param:
                        key, value = param.split('=', 1)
                        if key == 'max':
                            try:
                                max_nodes = int(value)
                            except:
                                pass
                        elif key == 'ignore':
                            ignore_protos = set(value.split(','))
            # 否则是节点名称，忽略
        
        return cls(
            url=line,
            is_china=is_china,
            is_date=is_date,
            is_list=is_list,
            max_nodes=max_nodes,
            ignore_protos=ignore_protos
        )
    
    def get_actual_url(self) -> str:
        """获取实际URL（处理动态日期）"""
        url = self.url
        if self.is_date:
            now = datetime.datetime.now()
            url = now.strftime(url)
        return url


class AsyncFetcher:
    """异步订阅获取器"""
    
    def __init__(
        self,
        timeout: int = 10,
        max_concurrent: int = 20,
        proxy: Optional[str] = None
    ):
        self.timeout = aiohttp.ClientTimeout(total=timeout)
        self.semaphore = asyncio.Semaphore(max_concurrent)
        self.proxy = proxy
        self.session: Optional[aiohttp.ClientSession] = None
        
        # CDN 加速映射
        self.cdn_map = {
            'raw.githubusercontent.com': 'fastly.jsdelivr.net/gh',
            'github.com': 'ghproxy.net',
        }
    
    def raw2cdn(self, url: str) -> str:
        """转换为 CDN 加速链接"""
        for old, new in self.cdn_map.items():
            if old in url:
                if 'raw.githubusercontent.com' in url:
                    # https://raw.githubusercontent.com/user/repo/branch/file
                    # -> https://fastly.jsdelivr.net/gh/user/repo@branch/file
                    match = re.match(
                        r'https://raw\.githubusercontent\.com/([^/]+)/([^/]+)/([^/]+)/(.+)',
                        url
                    )
                    if match:
                        return f"https://{new}/{match.group(1)}/{match.group(2)}@{match.group(3)}/{match.group(4)}"
                elif 'github.com' in url and 'blob' in url:
                    match = re.match(
                        r'https://github\.com/([^/]+)/([^/]+)/blob/([^/]+)/(.+)',
                        url
                    )
                    if match:
                        return f"https://{new}/https://github.com/{match.group(1)}/{match.group(2)}/blob/{match.group(3)}/{match.group(4)}"
        return url
    
    async def __aenter__(self):
        self.session = aiohttp.ClientSession(
            timeout=self.timeout,
            headers={
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) Clash-verge/v2.0.3"
            }
        )
        return self
    
    async def __aexit__(self, *args):
        if self.session:
            await self.session.close()
    
    async def fetch_url(self, url: str) -> Optional[str]:
        """获取单个URL内容"""
        if not self.session:
            return None
        
        # 尝试 CDN 加速
        urls_to_try = [url]
        cdn_url = self.raw2cdn(url)
        if cdn_url != url:
            urls_to_try.append(cdn_url)
        
        for try_url in urls_to_try:
            try:
                async with self.semaphore:
                    proxy = self.proxy if self.proxy else None
                    async with self.session.get(try_url, proxy=proxy) as resp:
                        if resp.status == 200:
                            return await resp.text()
            except asyncio.TimeoutError:
                logger.debug(f"Timeout: {try_url[:60]}...")
            except Exception as e:
                logger.debug(f"Error fetching {try_url[:60]}...: {e}")
        
        return None
    
    def parse_content(self, content: str, config: SourceConfig) -> List[Node]:
        """解析订阅内容"""
        nodes = []
        
        # 尝试 Base64 解码
        try:
            decoded = b64decode(content.strip())
            # 检查解码后是否包含协议标识
            if any(f"{proto}://" in decoded for proto in ['vmess', 'ss', 'ssr', 'trojan', 'vless', 'hysteria2', 'hy2']):
                content = decoded
        except:
            pass
        
        # 解析节点
        for line in content.split('\n'):
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            
            try:
                # 支持 YAML 格式
                if line.startswith('- ') or ': {'):
                    # 简单 YAML 解析（完整解析需要 yaml 库）
                    continue
                
                # URL 格式
                if '://' in line:
                    # 提取 URL（可能带有其他信息）
                    url_match = re.search(r'(vmess|ss|ssr|trojan|vless|hysteria2|hy2)://[^\s<>"\']+', line)
                    if url_match:
                        node = Node.from_url(url_match.group(0))
                        
                        # 过滤协议
                        if node.protocol.value not in config.ignore_protos:
                            nodes.append(node)
            except Exception as e:
                logger.debug(f"Parse error: {e}")
        
        # 限制节点数
        if config.max_nodes > 0 and len(nodes) > config.max_nodes:
            nodes = nodes[:config.max_nodes]
        
        return nodes
    
    def extract_sub_urls(self, content: str) -> List[str]:
        """从内容中提取订阅链接"""
        urls = []
        
        # 提取 http(s) 链接
        for match in re.finditer(r'https?://[^\s<>"\'\)\]]+', content):
            url = match.group(0)
            # 过滤明显不是订阅的链接
            if any(ext in url.lower() for ext in ['.png', '.jpg', '.gif', '.css', '.js']):
                continue
            if '://' in url and not url.endswith('.html'):
                urls.append(url)
        
        return list(set(urls))
    
    async def fetch_source(
        self,
        config: SourceConfig,
        depth: int = 0
    ) -> FetchResult:
        """获取单个订阅源"""
        url = config.get_actual_url()
        
        content = await self.fetch_url(url)
        if not content:
            return FetchResult(url=url, error="Failed to fetch")
        
        if config.is_list:
            # 递归获取订阅列表
            sub_urls = self.extract_sub_urls(content)
            logger.info(f"Found {len(sub_urls)} sub-urls from {url[:50]}...")
            
            all_nodes = []
            tasks = []
            for sub_url in sub_urls[:50]:  # 限制递归深度
                sub_config = SourceConfig(url=sub_url)
                tasks.append(self.fetch_source(sub_config, depth + 1))
            
            results = await asyncio.gather(*tasks)
            for result in results:
                all_nodes.extend(result.nodes)
            
            return FetchResult(url=url, nodes=all_nodes, count=len(all_nodes))
        else:
            # 解析节点
            nodes = self.parse_content(content, config)
            return FetchResult(url=url, nodes=nodes, count=len(nodes))
    
    async def fetch_all(
        self,
        configs: List[SourceConfig],
        progress_callback: Optional[Callable] = None
    ) -> List[FetchResult]:
        """并发获取所有订阅源"""
        results = []
        
        async def fetch_with_progress(i: int, config: SourceConfig):
            result = await self.fetch_source(config)
            if progress_callback:
                progress_callback(i + 1, len(configs), config.url, result.count)
            return result
        
        tasks = [
            fetch_with_progress(i, config)
            for i, config in enumerate(configs)
        ]
        
        results = await asyncio.gather(*tasks)
        return list(results)
    
    def merge_nodes(
        self,
        results: List[FetchResult],
        max_total: int = 0
    ) -> Set[Node]:
        """合并去重节点"""
        unique_nodes: Set[Node] = set()
        
        for result in results:
            for node in result.nodes:
                unique_nodes.add(node)
        
        # 限制总数
        if max_total > 0 and len(unique_nodes) > max_total:
            unique_nodes = set(list(unique_nodes)[:max_total])
        
        return unique_nodes


def load_sources(path: str = "config/sources.list") -> List[SourceConfig]:
    """加载订阅源配置"""
    configs = []
    
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            config = SourceConfig.parse(line)
            if config:
                configs.append(config)
    
    return configs
