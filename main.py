#!/usr/bin/env python3
"""
AutoMergePublicNodes - 主程序
自动合并公开代理节点，生成多格式订阅

特性：
- 异步并发获取订阅
- 动态日期URL支持
- 订阅列表递归获取
- TCP连通性测试过滤
- 多格式输出（V2Ray/Clash/Meta）
- 按地区分类节点
"""
import asyncio
import argparse
import logging
import sys
import os
from pathlib import Path
from typing import List, Set
from datetime import datetime

# 添加 src 到路径
sys.path.insert(0, str(Path(__file__).parent))

from src.node import Node
from src.fetcher import AsyncFetcher, SourceConfig, load_sources, FetchResult
from src.filter import NodeFilter
from src.generator import SubscriptionGenerator
from src.dynamic import DynamicFetcher

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger(__name__)


async def main(
    sources_path: str = "config/sources.list",
    config_path: str = "config/config.yaml",
    output_dir: str = "output",
    max_nodes: int = 200,
    timeout: int = 10,
    concurrent: int = 20,
    test_tcp: bool = True,
    tcp_timeout: int = 5,
    tcp_concurrent: int = 100,
    use_dynamic: bool = True
):
    """主流程"""
    start_time = datetime.now()
    
    # 加载配置
    import yaml
    with open(config_path, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    
    # 加载订阅源
    sources = load_sources(sources_path)
    logger.info(f"Loaded {len(sources)} subscription sources")
    
    # 加载动态源
    if use_dynamic:
        logger.info("Fetching dynamic sources...")
        async with DynamicFetcher() as dynamic:
            # 获取 peasoft
            peasoft_content = await dynamic.peasoft()
            if peasoft_content:
                # 解析节点
                peasoft_config = SourceConfig(url="dynamic://peasoft")
                peasoft_nodes = []
                for line in peasoft_content.split('\n'):
                    if '://' in line:
                        try:
                            peasoft_nodes.append(Node.from_url(line.strip()))
                        except:
                            pass
                logger.info(f"  peasoft: {len(peasoft_nodes)} nodes")
            
            # 获取 crossxx
            crossxx_urls = await dynamic.crossxx_free()
            for url in crossxx_urls[:5]:  # 限制数量
                sources.append(SourceConfig(url=url))
            logger.info(f"  crossxx: {len(crossxx_urls)} URLs")
    
    all_nodes: Set[Node] = set()
    
    # 获取订阅
    logger.info("Fetching subscriptions...")
    async with AsyncFetcher(timeout=timeout, max_concurrent=concurrent) as fetcher:
        
        def progress(current: int, total: int, url: str, count: int):
            logger.info(f"  [{current}/{total}] {url[:50]}... -> {count} nodes")
        
        results: List[FetchResult] = await fetcher.fetch_all(sources, progress)
        
        # 合并节点
        all_nodes = fetcher.merge_nodes(results, max_total=max_nodes * 3)
        logger.info(f"Total unique nodes: {len(all_nodes)}")
    
    if not all_nodes:
        logger.error("No nodes found!")
        return
    
    # TCP 连通性测试
    valid_nodes: List[Node] = list(all_nodes)
    if test_tcp:
        logger.info("Testing node connectivity...")
        node_filter = NodeFilter(timeout=tcp_timeout, max_concurrent=tcp_concurrent)
        valid_nodes = await node_filter.filter_nodes(list(all_nodes), max_nodes=max_nodes)
        logger.info(f"Valid nodes after TCP test: {len(valid_nodes)}")
    
    if not valid_nodes:
        logger.error("No valid nodes after filtering!")
        return
    
    # 生成订阅
    logger.info("Generating subscriptions...")
    generator = SubscriptionGenerator(config)
    
    # 加载分类配置
    categories = {}
    categories_disp = {}
    snippets_path = Path("snippets/_config.yml")
    if snippets_path.exists():
        with open(snippets_path, 'r', encoding='utf-8') as f:
            snippets_config = yaml.safe_load(f) or {}
        categories = snippets_config.get('categories', {})
        categories_disp = snippets_config.get('categories_disp', {})
    
    generator.generate_all(
        valid_nodes,
        output_dir=output_dir,
        categories=categories,
        categories_disp=categories_disp
    )
    
    elapsed = (datetime.now() - start_time).total_seconds()
    logger.info(f"Done! Elapsed: {elapsed:.1f}s")


def cli():
    """命令行入口"""
    parser = argparse.ArgumentParser(
        description="AutoMergePublicNodes - 自动合并公开代理节点"
    )
    parser.add_argument(
        "-s", "--sources",
        default="config/sources.list",
        help="订阅源配置文件"
    )
    parser.add_argument(
        "-c", "--config",
        default="config/config.yaml",
        help="Clash 配置模板"
    )
    parser.add_argument(
        "-o", "--output",
        default="output",
        help="输出目录"
    )
    parser.add_argument(
        "-n", "--max-nodes",
        type=int,
        default=200,
        help="最大节点数"
    )
    parser.add_argument(
        "-t", "--timeout",
        type=int,
        default=10,
        help="获取超时（秒）"
    )
    parser.add_argument(
        "--concurrent",
        type=int,
        default=20,
        help="并发获取数"
    )
    parser.add_argument(
        "--no-tcp-test",
        action="store_true",
        help="跳过 TCP 连通性测试"
    )
    parser.add_argument(
        "--tcp-timeout",
        type=int,
        default=5,
        help="TCP 测试超时（秒）"
    )
    parser.add_argument(
        "--tcp-concurrent",
        type=int,
        default=100,
        help="TCP 测试并发数"
    )
    parser.add_argument(
        "--no-dynamic",
        action="store_true",
        help="跳过动态源"
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="详细输出"
    )
    
    args = parser.parse_args()
    
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    asyncio.run(main(
        sources_path=args.sources,
        config_path=args.config,
        output_dir=args.output,
        max_nodes=args.max_nodes,
        timeout=args.timeout,
        concurrent=args.concurrent,
        test_tcp=not args.no_tcp_test,
        tcp_timeout=args.tcp_timeout,
        tcp_concurrent=args.tcp_concurrent,
        use_dynamic=not args.no_dynamic
    ))


if __name__ == "__main__":
    cli()
