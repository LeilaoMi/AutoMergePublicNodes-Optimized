#!/usr/bin/env python3
"""
节点连通性测试 - 优化版
使用异步TCP连接测试节点有效性
"""
import asyncio
import socket
import time
from typing import List, Dict, Any, Set, Optional
from dataclasses import dataclass
import logging

from .node import Node

logger = logging.getLogger(__name__)


@dataclass
class TestResult:
    """测试结果"""
    node: Node
    is_valid: bool
    delay_ms: float = 0.0
    error: Optional[str] = None


class NodeFilter:
    """节点过滤器 - 异步TCP连通性测试"""
    
    def __init__(
        self,
        timeout: int = 5,
        max_concurrent: int = 100
    ):
        self.timeout = timeout
        self.semaphore = asyncio.Semaphore(max_concurrent)
    
    async def test_tcp(
        self,
        host: str,
        port: int
    ) -> tuple[bool, float]:
        """测试TCP连接"""
        start = time.time()
        
        try:
            async with self.semaphore:
                # 使用 asyncio.open_connection
                reader, writer = await asyncio.wait_for(
                    asyncio.open_connection(host, port),
                    timeout=self.timeout
                )
                writer.close()
                await writer.wait_closed()
            
            delay = (time.time() - start) * 1000
            return True, delay
        except asyncio.TimeoutError:
            return False, 0
        except Exception as e:
            return False, 0
    
    async def test_node(self, node: Node) -> TestResult:
        """测试单个节点"""
        is_valid, delay = await self.test_tcp(node.server, node.port)
        return TestResult(
            node=node,
            is_valid=is_valid,
            delay_ms=delay
        )
    
    async def filter_nodes(
        self,
        nodes: List[Node],
        max_nodes: int = 200,
        progress_callback: Optional[callable] = None
    ) -> List[Node]:
        """过滤有效节点"""
        logger.info(f"Testing {len(nodes)} nodes...")
        
        tasks = [self.test_node(node) for node in nodes]
        results: List[TestResult] = await asyncio.gather(*tasks)
        
        # 收集有效节点
        valid_nodes = []
        for result in results:
            if result.is_valid:
                valid_nodes.append(result.node)
        
        logger.info(f"Valid nodes: {len(valid_nodes)}/{len(nodes)}")
        
        # 限制数量
        if max_nodes > 0 and len(valid_nodes) > max_nodes:
            valid_nodes = valid_nodes[:max_nodes]
            logger.info(f"Limited to {max_nodes} nodes")
        
        return valid_nodes
    
    async def filter_with_delay(
        self,
        nodes: List[Node],
        max_nodes: int = 200,
        progress_callback: Optional[callable] = None
    ) -> List[tuple[Node, float]]:
        """过滤并返回延迟信息"""
        tasks = [self.test_node(node) for node in nodes]
        results: List[TestResult] = await asyncio.gather(*tasks)
        
        # 收集有效节点及其延迟
        valid_with_delay = []
        for result in results:
            if result.is_valid:
                valid_with_delay.append((result.node, result.delay_ms))
        
        # 按延迟排序
        valid_with_delay.sort(key=lambda x: x[1])
        
        # 限制数量
        if max_nodes > 0 and len(valid_with_delay) > max_nodes:
            valid_with_delay = valid_with_delay[:max_nodes]
        
        return valid_with_delay


def filter_yaml_nodes(
    input_path: str,
    output_path: str,
    timeout: int = 5,
    max_concurrent: int = 100,
    max_nodes: int = 200
) -> int:
    """过滤YAML文件中的节点"""
    import yaml
    
    async def _filter():
        # 读取 YAML
        with open(input_path, 'r', encoding='utf-8') as f:
            # 保留注释
            lines = f.readlines()
            comment = lines[0] if lines and lines[0].startswith('#') else ''
            data = yaml.safe_load(''.join(lines))
        
        proxies = data.get('proxies', [])
        if not proxies:
            return 0
        
        # 转换为 Node 对象
        nodes = [Node.from_clash(p) for p in proxies]
        
        # 过滤
        node_filter = NodeFilter(timeout=timeout, max_concurrent=max_concurrent)
        valid_nodes = await node_filter.filter_nodes(nodes, max_nodes=max_nodes)
        
        # 获取有效节点名称
        valid_names = {n.name for n in valid_nodes}
        
        # 更新数据
        data['proxies'] = [n.clash_data for n in valid_nodes]
        
        # 更新代理组
        for group in data.get('proxy-groups', []):
            if isinstance(group.get('proxies'), list):
                group['proxies'] = [p for p in group['proxies'] if p in valid_names]
        
        # 写入
        with open(output_path, 'w', encoding='utf-8') as f:
            if comment:
                f.write(comment)
            yaml.dump(data, f, allow_unicode=True, default_flow_style=False)
        
        return len(valid_nodes)
    
    return asyncio.run(_filter())


# 命令行入口
if __name__ == "__main__":
    import argparse
    import sys
    
    parser = argparse.ArgumentParser(description="Filter invalid nodes")
    parser.add_argument("input", help="Input YAML file")
    parser.add_argument("-o", "--output", help="Output file (default: overwrite input)")
    parser.add_argument("-t", "--timeout", type=int, default=5, help="TCP timeout")
    parser.add_argument("-c", "--concurrent", type=int, default=100, help="Max concurrent")
    parser.add_argument("-n", "--max-nodes", type=int, default=200, help="Max nodes to keep")
    
    args = parser.parse_args()
    
    output = args.output or args.input
    count = filter_yaml_nodes(
        args.input,
        output,
        timeout=args.timeout,
        max_concurrent=args.concurrent,
        max_nodes=args.max_nodes
    )
    
    print(f"Filtered {count} valid nodes -> {output}")
