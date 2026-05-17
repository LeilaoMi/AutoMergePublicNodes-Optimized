#!/usr/bin/env python3
"""
订阅生成器 - 优化版
生成 V2Ray、Clash、Meta 格式订阅
"""
import yaml
import copy
import datetime
from typing import List, Dict, Any, Optional, Set
from pathlib import Path
import logging

from .node import Node, b64encode

logger = logging.getLogger(__name__)


class SubscriptionGenerator:
    """订阅生成器"""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    
    def generate_v2ray(self, nodes: List[Node]) -> str:
        """生成 V2Ray 订阅格式"""
        lines = []
        for node in nodes:
            try:
                lines.append(node.url)
            except Exception as e:
                logger.debug(f"Skip node {node.name}: {e}")
        
        return '\n'.join(lines) + '\n'
    
    def generate_clash(
        self,
        nodes: List[Node],
        proxy_groups: Optional[List[Dict]] = None,
        rules: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """生成 Clash 配置"""
        config = copy.deepcopy(self.config)
        
        # 过滤 Clash 不支持的节点
        clash_nodes = [n for n in nodes if n.supports_clash()]
        
        # 设置节点
        config['proxies'] = [n.clash_data for n in clash_nodes]
        
        # 设置代理组
        names = [n.name for n in clash_nodes]
        if proxy_groups:
            for group in proxy_groups:
                if not group.get('proxies'):
                    group['proxies'] = names.copy()
            config['proxy-groups'] = proxy_groups
        elif 'proxy-groups' in config:
            for group in config['proxy-groups']:
                if not group.get('proxies'):
                    group['proxies'] = names.copy()
        
        # 设置规则
        if rules:
            config['rules'] = rules
        
        return config
    
    def generate_meta(
        self,
        nodes: List[Node],
        proxy_groups: Optional[List[Dict]] = None,
        rules: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """生成 Meta 配置"""
        config = copy.deepcopy(self.config)
        
        # 设置节点
        config['proxies'] = [n.clash_data for n in nodes]
        
        # 设置代理组
        names = [n.name for n in nodes]
        if proxy_groups:
            for group in proxy_groups:
                if not group.get('proxies'):
                    group['proxies'] = names.copy()
            config['proxy-groups'] = proxy_groups
        elif 'proxy-groups' in config:
            for group in config['proxy-groups']:
                if not group.get('proxies'):
                    group['proxies'] = names.copy()
        
        # 设置规则
        if rules:
            config['rules'] = rules
        
        return config
    
    def save_yaml(
        self,
        data: Dict[str, Any],
        path: str,
        comment: str = ""
    ):
        """保存 YAML 文件"""
        with open(path, 'w', encoding='utf-8') as f:
            if comment:
                f.write(f"# {comment}\n")
            yaml.dump(data, f, allow_unicode=True, default_flow_style=False)
    
    def save_v2ray(self, content: str, path: str):
        """保存 V2Ray 订阅"""
        # 原始格式
        Path(path).with_suffix('.raw.txt').write_text(content, encoding='utf-8')
        # Base64 格式
        Path(path).write_text(b64encode(content), encoding='utf-8')
    
    def categorize_nodes(
        self,
        nodes: List[Node],
        categories: Dict[str, List[str]]
    ) -> Dict[str, List[Node]]:
        """按地区分类节点"""
        result: Dict[str, List[Node]] = {ctg: [] for ctg in categories}
        
        for node in nodes:
            matched = []
            for ctg, keywords in categories.items():
                for keyword in keywords:
                    if keyword in node.name:
                        matched.append(ctg)
                        break
            
            # 只归入一个分类
            if len(matched) == 1:
                result[matched[0]].append(node)
        
        return result
    
    def generate_all(
        self,
        nodes: List[Node],
        output_dir: str = "output",
        categories: Optional[Dict[str, List[str]]] = None,
        categories_disp: Optional[Dict[str, str]] = None
    ):
        """生成所有订阅文件"""
        output_path = Path(output_dir)
        output_path.mkdir(exist_ok=True)
        
        # 生成 V2Ray 订阅
        logger.info("Generating V2Ray subscription...")
        v2ray_content = self.generate_v2ray(nodes)
        self.save_v2ray(v2ray_content, str(output_path / "list.txt"))
        logger.info(f"  -> list.txt ({len(nodes)} nodes)")
        
        # 生成 Clash 订阅
        logger.info("Generating Clash subscription...")
        clash_config = self.generate_clash(nodes)
        clash_config['metadata'] = {
            'updated': self.timestamp,
            'count': len([n for n in nodes if n.supports_clash()])
        }
        self.save_yaml(
            clash_config,
            str(output_path / "list.yml"),
            f"Update: {self.timestamp}"
        )
        logger.info(f"  -> list.yml")
        
        # 生成 Meta 订阅
        logger.info("Generating Meta subscription...")
        meta_config = self.generate_meta(nodes)
        meta_config['metadata'] = {
            'updated': self.timestamp,
            'count': len(nodes)
        }
        self.save_yaml(
            meta_config,
            str(output_path / "list.meta.yml"),
            f"Update: {self.timestamp}"
        )
        logger.info(f"  -> list.meta.yml")
        
        # 按地区分类
        if categories and categories_disp:
            logger.info("Categorizing nodes by region...")
            categorized = self.categorize_nodes(nodes, categories)
            
            for ctg, ctg_nodes in categorized.items():
                if ctg_nodes and ctg in categories_disp:
                    # 生成分类订阅
                    ctg_clash = self.generate_clash(ctg_nodes)
                    self.save_yaml(
                        ctg_clash,
                        str(output_path / f"nodes_{ctg}.yml")
                    )
                    
                    ctg_meta = self.generate_meta(ctg_nodes)
                    self.save_yaml(
                        ctg_meta,
                        str(output_path / f"nodes_{ctg}.meta.yml")
                    )
                    
                    logger.info(f"  -> {ctg}: {len(ctg_nodes)} nodes")
        
        # 生成统计信息
        stats = self._generate_stats(nodes, output_dir)
        (output_path / "README.md").write_text(stats, encoding='utf-8')
        
        logger.info(f"All subscriptions generated in {output_dir}/")
    
    def _generate_stats(self, nodes: List[Node], output_dir: str) -> str:
        """生成统计信息"""
        import os
        
        # 协议统计
        proto_count: Dict[str, int] = {}
        for node in nodes:
            proto = node.protocol.value
            proto_count[proto] = proto_count.get(proto, 0) + 1
        
        repo = os.environ.get('GITHUB_REPOSITORY', 'user/repo')
        
        stats = f"""# 订阅统计

- 更新时间: {self.timestamp}
- 有效节点: {len(nodes)}

## 协议分布

| 协议 | 数量 |
|------|------|
"""
        for proto, count in sorted(proto_count.items(), key=lambda x: -x[1]):
            stats += f"| {proto} | {count} |\n"
        
        stats += f"""
## 订阅链接

| 格式 | 链接 |
|------|------|
| V2Ray | `https://raw.githubusercontent.com/{repo}/main/{output_dir}/list.txt` |
| Clash | `https://raw.githubusercontent.com/{repo}/main/{output_dir}/list.yml` |
| Meta | `https://raw.githubusercontent.com/{repo}/main/{output_dir}/list.meta.yml` |

## 使用方法

1. 复制订阅链接
2. 在客户端中添加订阅
3. 更新订阅即可使用
"""
        return stats
