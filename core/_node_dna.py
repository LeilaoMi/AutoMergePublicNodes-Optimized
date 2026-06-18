"""
[v2.7] 节点DNA分析系统 (Node DNA Analysis)

通过分析节点的ASN、IP段、延迟模式等特征，识别节点提供商，
避免过度依赖单一提供商，提升整体可靠性。

核心功能:
1. 提供商聚类 - 根据ASN和IP段识别同一提供商的节点
2. 多样性评分 - 评估节点池的提供商多样性
3. 风险分散建议 - 识别过度集中的提供商并建议替代方案
"""
from __future__ import annotations

from typing import List, Dict, Set, Tuple
from dataclasses import dataclass, field
import ipaddress
import logging

logger = logging.getLogger(__name__)


@dataclass
class ProviderProfile:
    """提供商画像"""
    name: str  # 提供商名称/标识
    asn: str  # ASN号
    node_count: int = 0  # 节点数量
    avg_latency: float = 0.0  # 平均延迟
    avg_score: float = 0.0  # 平均评分
    stability_score: float = 0.0  # 稳定性评分
    ip_ranges: Set[str] = field(default_factory=set)  # IP段集合
    protocols: Set[str] = field(default_factory=set)  # 协议集合
    nodes: List[str] = field(default_factory=list)  # 节点指纹列表


@dataclass
class DiversityReport:
    """多样性报告"""
    total_providers: int = 0  # 提供商总数
    total_nodes: int = 0  # 节点总数
    diversity_score: float = 0.0  # 多样性评分 (0-1)
    concentration_risk: str = "low"  # 集中风险: low/medium/high
    dominant_providers: List[Dict] = field(default_factory=list)  # 主导提供商
    recommendations: List[str] = field(default_factory=list)  # 建议


class NodeDNAAnalyzer:
    """节点DNA分析器"""
    
    def __init__(self):
        self.asn_cache: Dict[str, str] = {}  # IP -> ASN 缓存
        self.provider_profiles: Dict[str, ProviderProfile] = {}
        
    def analyze_node_pool(
        self,
        nodes: List,  # List[Node]
        node_stats: Dict[str, Dict],  # {fingerprint: {latency, score, stability, ...}}
    ) -> DiversityReport:
        """
        分析节点池的提供商多样性
        
        Args:
            nodes: 节点列表
            node_stats: 节点统计数据
            
        Returns:
            DiversityReport: 多样性报告
        """
        logger.info(f"开始分析 {len(nodes)} 个节点的提供商多样性...")
        
        # 清空之前的分析结果
        self.provider_profiles = {}
        
        # 分析每个节点
        for node in nodes:
            provider_key = self._identify_provider(node)
            
            if provider_key not in self.provider_profiles:
                self.provider_profiles[provider_key] = ProviderProfile(
                    name=provider_key,
                    asn=self.asn_cache.get(node.server, "unknown")
                )
            
            profile = self.provider_profiles[provider_key]
            profile.node_count += 1
            profile.nodes.append(node.fingerprint())
            
            # 添加IP段 (取前3段)
            ip_parts = node.server.split('.')
            if len(ip_parts) == 4:
                ip_range = f"{ip_parts[0]}.{ip_parts[1]}.{ip_parts[2]}.0/24"
                profile.ip_ranges.add(ip_range)
            
            # 添加协议
            profile.protocols.add(node.type)
            
            # 统计性能指标
            stats = node_stats.get(node.fingerprint(), {})
            if 'latency_ms' in stats:
                profile.avg_latency += stats['latency_ms']
            if 'score' in stats:
                profile.avg_score += stats['score']
            if 'stability' in stats:
                profile.stability_score += stats['stability']
        
        # 计算平均值
        for profile in self.provider_profiles.values():
            if profile.node_count > 0:
                profile.avg_latency /= profile.node_count
                profile.avg_score /= profile.node_count
                profile.stability_score /= profile.node_count
        
        # 生成多样性报告
        return self._generate_diversity_report()
    
    def _identify_provider(self, node) -> str:
        """
        识别节点提供商
        
        基于:
        1. ASN (如果有)
        2. IP段前3段
        3. 延迟模式相似性
        """
        # 简化的提供商识别：使用IP段前3段作为标识
        ip_parts = node.server.split('.')
        if len(ip_parts) == 4:
            return f"provider_{ip_parts[0]}_{ip_parts[1]}_{ip_parts[2]}"
        
        return "provider_unknown"
    
    def _generate_diversity_report(self) -> DiversityReport:
        """生成多样性报告"""
        if not self.provider_profiles:
            return DiversityReport()
        
        report = DiversityReport()
        report.total_providers = len(self.provider_profiles)
        report.total_nodes = sum(p.node_count for p in self.provider_profiles.values())
        
        if report.total_nodes == 0:
            return report
        
        # 计算多样性评分 (赫芬达尔-赫希曼指数 HHI 的倒数)
        # HHI = sum(market_share^2), 越小说明越分散
        market_shares = [
            p.node_count / report.total_nodes 
            for p in self.provider_profiles.values()
        ]
        hhi = sum(share ** 2 for share in market_shares)
        
        # 多样性评分 = 1 - HHI (归一化到0-1)
        report.diversity_score = 1 - hhi
        
        # 识别主导提供商 (占比 > 30%)
        dominant_threshold = 0.3
        report.dominant_providers = []
        
        for name, profile in self.provider_profiles.items():
            share = profile.node_count / report.total_nodes
            if share >= dominant_threshold:
                report.dominant_providers.append({
                    "name": name,
                    "node_count": profile.node_count,
                    "share": round(share * 100, 1),
                    "avg_score": round(profile.avg_score, 2),
                    "protocols": list(profile.protocols),
                })
        
        # 评估集中风险
        # 关键逻辑：基于最大提供商的市场份额
        if report.dominant_providers:
            max_share = max(p["share"] for p in report.dominant_providers)
            if max_share >= 50:
                report.concentration_risk = "high"
            elif max_share >= 40:
                report.concentration_risk = "medium"
            else:
                # 所有提供商都 < 40%，市场相对分散
                report.concentration_risk = "low"
        else:
            report.concentration_risk = "low"
        
        # 生成建议
        report.recommendations = self._generate_recommendations(report)
        
        logger.info(
            f"多样性分析完成: {report.total_providers} 个提供商, "
            f"多样性评分 {report.diversity_score:.2f}, "
            f"集中风险 {report.concentration_risk}"
        )
        
        return report
    
    def _generate_recommendations(self, report: DiversityReport) -> List[str]:
        """生成优化建议"""
        recommendations = []
        
        if report.concentration_risk == "high":
            recommendations.append(
                "⚠️ 高风险: 节点池过度集中于少数提供商，建议增加其他提供商的节点以提升可靠性"
            )
            
            for provider in report.dominant_providers:
                recommendations.append(
                    f"  - {provider['name']} 占比 {provider['share']}%，"
                    f"包含 {provider['node_count']} 个节点"
                )
        
        elif report.concentration_risk == "medium":
            recommendations.append(
                "⚠️ 中等风险: 存在一个主导提供商，建议适度增加其他提供商的节点"
            )
        
        else:
            recommendations.append(
                "✓ 良好: 节点池提供商多样性良好，风险分散"
            )
        
        # 协议多样性建议
        all_protocols = set()
        for profile in self.provider_profiles.values():
            all_protocols.update(profile.protocols)
        
        if len(all_protocols) < 3:
            recommendations.append(
                f"💡 建议: 当前仅使用 {len(all_protocols)} 种协议 "
                f"({', '.join(sorted(all_protocols))})，"
                f"建议增加更多协议类型以提升兼容性"
            )
        
        # 性能建议
        low_performance_providers = [
            (name, profile) 
            for name, profile in self.provider_profiles.items()
            if profile.node_count >= 3 and profile.avg_score < 60
        ]
        
        if low_performance_providers:
            recommendations.append(
                f"⚠️ 注意: {len(low_performance_providers)} 个提供商平均评分低于60分，"
                f"建议检查或替换这些提供商的节点"
            )
        
        return recommendations
    
    def get_similar_nodes(
        self,
        target_node,  # Node
        nodes: List,  # List[Node]
        top_k: int = 5,
    ) -> List[Tuple]:  # List[(node, similarity_score)]
        """
        获取与目标节点相似的其他节点 (用于故障转移)
        
        相似度基于:
        1. 同一提供商 (权重 0.4)
        2. 相同协议 (权重 0.3)
        3. 延迟接近 (权重 0.3)
        """
        similarities = []
        
        target_provider = self._identify_provider(target_node)
        target_latency = 0  # 需要从stats获取
        
        for node in nodes:
            if node.fingerprint() == target_node.fingerprint():
                continue
            
            score = 0.0
            
            # 提供商相似度
            node_provider = self._identify_provider(node)
            if node_provider == target_provider:
                score += 0.4
            
            # 协议相似度
            if node.type == target_node.type:
                score += 0.3
            
            # 延迟相似度 (简化: 如果类型和提供商相同就给分)
            if node_provider == target_provider and node.type == target_node.type:
                score += 0.3
            
            if score > 0:
                similarities.append((node, score))
        
        # 按相似度排序
        similarities.sort(key=lambda x: x[1], reverse=True)
        
        return similarities[:top_k]