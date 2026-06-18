"""
[v2.7] 节点DNA分析系统测试

测试提供商聚类、多样性评分和风险分散建议
"""
from __future__ import annotations

import unittest
import sys
from pathlib import Path

# 添加项目根目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from core._node_dna import NodeDNAAnalyzer, ProviderProfile, DiversityReport
from core.parser import Node


class TestNodeDNAAnalyzer(unittest.TestCase):
    """测试节点DNA分析器"""
    
    def setUp(self):
        """测试前准备"""
        self.analyzer = NodeDNAAnalyzer()
    
    def test_identify_provider(self):
        """测试提供商识别"""
        # 创建测试节点
        node1 = Node(
            type="vmess",
            tag="Test Node 1",
            server="1.2.3.4",
            server_port=443,
            raw={"uuid": "test-uuid-1"}
        )
        
        node2 = Node(
            type="vmess",
            tag="Test Node 2",
            server="1.2.3.5",  # 同一IP段
            server_port=443,
            raw={"uuid": "test-uuid-2"}
        )
        
        node3 = Node(
            type="vmess",
            tag="Test Node 3",
            server="4.5.6.7",  # 不同IP段
            server_port=443,
            raw={"uuid": "test-uuid-3"}
        )
        
        provider1 = self.analyzer._identify_provider(node1)
        provider2 = self.analyzer._identify_provider(node2)
        provider3 = self.analyzer._identify_provider(node3)
        
        # 同一IP段的节点应该识别为同一提供商
        self.assertEqual(provider1, provider2)
        # 不同IP段的节点应该识别为不同提供商
        self.assertNotEqual(provider1, provider3)
    
    def test_analyze_node_pool_basic(self):
        """测试基本节点池分析"""
        nodes = [
            Node(type="vmess", tag="Node 1", server="1.2.3.4", server_port=443, raw={"uuid": "uuid1"}),
            Node(type="vmess", tag="Node 2", server="1.2.3.5", server_port=443, raw={"uuid": "uuid2"}),
            Node(type="vmess", tag="Node 3", server="1.2.3.6", server_port=443, raw={"uuid": "uuid3"}),
        ]
        
        node_stats = {
            "uuid1": {"latency_ms": 100, "score": 80, "stability": 0.9},
            "uuid2": {"latency_ms": 120, "score": 75, "stability": 0.85},
            "uuid3": {"latency_ms": 110, "score": 85, "stability": 0.95},
        }
        
        report = self.analyzer.analyze_node_pool(nodes, node_stats)
        
        # 验证报告结构
        self.assertIsInstance(report, DiversityReport)
        self.assertEqual(report.total_nodes, 3)
        self.assertGreater(report.total_providers, 0)
        self.assertGreaterEqual(report.diversity_score, 0)
        self.assertLessEqual(report.diversity_score, 1)
    
    def test_diversity_score_single_provider(self):
        """测试单一提供商的多样性评分"""
        nodes = [
            Node(type="vmess", tag="Node 1", server="1.2.3.4", server_port=443, raw={"uuid": "uuid1"}),
            Node(type="vmess", tag="Node 2", server="1.2.3.5", server_port=443, raw={"uuid": "uuid2"}),
            Node(type="vmess", tag="Node 3", server="1.2.3.6", server_port=443, raw={"uuid": "uuid3"}),
        ]
        
        node_stats = {}
        report = self.analyzer.analyze_node_pool(nodes, node_stats)
        
        # 所有节点来自同一提供商，多样性评分应该很低
        self.assertEqual(report.total_providers, 1)
        self.assertLess(report.diversity_score, 0.1)
        self.assertEqual(report.concentration_risk, "high")
    
    def test_diversity_score_multiple_providers(self):
        """测试多个提供商的多样性评分"""
        nodes = [
            Node(type="vmess", tag="Node 1", server="1.2.3.4", server_port=443, raw={"uuid": "uuid1"}),
            Node(type="vmess", tag="Node 2", server="4.5.6.7", server_port=443, raw={"uuid": "uuid2"}),
            Node(type="vmess", tag="Node 3", server="7.8.9.10", server_port=443, raw={"uuid": "uuid3"}),
        ]
        
        node_stats = {}
        report = self.analyzer.analyze_node_pool(nodes, node_stats)
        
        # 多个提供商，多样性评分应该较高
        self.assertEqual(report.total_providers, 3)
        self.assertGreater(report.diversity_score, 0.6)
        self.assertEqual(report.concentration_risk, "low")
    
    def test_dominant_provider_detection(self):
        """测试主导提供商检测"""
        # 创建10个节点，其中7个来自同一提供商
        nodes = []
        for i in range(7):
            nodes.append(Node(
                type="vmess",
                tag=f"Node {i}",
                server=f"1.2.3.{i+1}",
                server_port=443,
                raw={"uuid": f"uuid-{i}"}
            ))
        
        # 添加3个来自其他提供商的节点
        for i in range(3):
            nodes.append(Node(
                type="vmess",
                tag=f"Other Node {i}",
                server=f"{i+4}.5.6.7",
                server_port=443,
                raw={"uuid": f"uuid-other-{i}"}
            ))
        
        node_stats = {}
        report = self.analyzer.analyze_node_pool(nodes, node_stats)
        
        # 应该检测到主导提供商
        self.assertGreater(len(report.dominant_providers), 0)
        # 主导提供商占比应该 >= 30%
        for provider in report.dominant_providers:
            self.assertGreaterEqual(provider["share"], 30)
    
    def test_recommendations_generation(self):
        """测试建议生成"""
        # 测试高风险场景
        nodes = [
            Node(type="vmess", tag="Node 1", server="1.2.3.4", server_port=443, raw={"uuid": "uuid1"}),
            Node(type="vmess", tag="Node 2", server="1.2.3.5", server_port=443, raw={"uuid": "uuid2"}),
        ]
        
        node_stats = {}
        report = self.analyzer.analyze_node_pool(nodes, node_stats)
        
        # 应该有建议
        self.assertGreater(len(report.recommendations), 0)
        # 应该包含风险警告
        has_warning = any("高风险" in rec or "风险" in rec for rec in report.recommendations)
        self.assertTrue(has_warning)
    
    def test_get_similar_nodes(self):
        """测试相似节点查找"""
        target = Node(type="vmess", tag="Target", server="1.2.3.4", server_port=443, raw={"uuid": "target"})
        
        nodes = [
            # 同一提供商，相同协议
            Node(type="vmess", tag="Similar 1", server="1.2.3.5", server_port=443, raw={"uuid": "uuid1"}),
            Node(type="vmess", tag="Similar 2", server="1.2.3.6", server_port=443, raw={"uuid": "uuid2"}),
            # 同一提供商，不同协议
            Node(type="trojan", tag="Same Provider", server="1.2.3.7", server_port=443, raw={"uuid": "uuid3"}),
            # 不同提供商，相同协议
            Node(type="vmess", tag="Same Protocol", server="4.5.6.7", server_port=443, raw={"uuid": "uuid4"}),
            # 完全不同
            Node(type="trojan", tag="Different", server="7.8.9.10", server_port=443, raw={"uuid": "uuid5"}),
        ]
        
        similar = self.analyzer.get_similar_nodes(target, nodes, top_k=3)
        
        # 应该返回最多3个相似节点
        self.assertLessEqual(len(similar), 3)
        
        # 每个结果应该是 (node, score) 元组
        for node, score in similar:
            self.assertIsInstance(node, Node)
            self.assertIsInstance(score, float)
            self.assertGreaterEqual(score, 0)
            self.assertLessEqual(score, 1)
        
        # 相似度应该降序排列
        if len(similar) >= 2:
            for i in range(len(similar) - 1):
                self.assertGreaterEqual(similar[i][1], similar[i+1][1])
    
    def test_provider_profile_aggregation(self):
        """测试提供商画像聚合"""
        nodes = [
            Node(type="vmess", server="1.2.3.4", server_port=443, tag="Node 1", raw={"uuid": "uuid1"}),
            Node(type="trojan", server="1.2.3.5", server_port=443, tag="Node 2", raw={"uuid": "uuid2"}),
            Node(type="vmess", server="1.2.3.6", server_port=443, tag="Node 3", raw={"uuid": "uuid3"}),
        ]
        
        # 使用节点的 fingerprint() 作为 key
        node_stats = {
            nodes[0].fingerprint(): {"latency_ms": 100, "score": 80, "stability": 0.9},
            nodes[1].fingerprint(): {"latency_ms": 120, "score": 75, "stability": 0.85},
            nodes[2].fingerprint(): {"latency_ms": 110, "score": 85, "stability": 0.95},
        }
        
        self.analyzer.analyze_node_pool(nodes, node_stats)
        
        # 应该有1个提供商（同一IP段）
        self.assertEqual(len(self.analyzer.provider_profiles), 1)
        
        # 获取提供商画像
        provider_key = list(self.analyzer.provider_profiles.keys())[0]
        profile = self.analyzer.provider_profiles[provider_key]
        
        # 验证聚合统计
        self.assertEqual(profile.node_count, 3)
        self.assertIn("vmess", profile.protocols)
        self.assertIn("trojan", profile.protocols)
        self.assertGreater(profile.avg_latency, 0)
        self.assertGreater(profile.avg_score, 0)
        self.assertGreater(profile.stability_score, 0)


class TestDiversityReport(unittest.TestCase):
    """测试多样性报告"""
    
    def test_report_initialization(self):
        """测试报告初始化"""
        report = DiversityReport()
        
        self.assertEqual(report.total_providers, 0)
        self.assertEqual(report.total_nodes, 0)
        self.assertEqual(report.diversity_score, 0.0)
        self.assertEqual(report.concentration_risk, "low")
        self.assertEqual(len(report.dominant_providers), 0)
        self.assertEqual(len(report.recommendations), 0)
    
    def test_report_with_data(self):
        """测试带数据的报告"""
        report = DiversityReport(
            total_providers=5,
            total_nodes=100,
            diversity_score=0.85,
            concentration_risk="medium",
            dominant_providers=[
                {"name": "Provider A", "node_count": 35, "share": 35.0}
            ],
            recommendations=["建议增加更多提供商"]
        )
        
        self.assertEqual(report.total_providers, 5)
        self.assertEqual(report.total_nodes, 100)
        self.assertEqual(report.diversity_score, 0.85)
        self.assertEqual(report.concentration_risk, "medium")
        self.assertEqual(len(report.dominant_providers), 1)
        self.assertEqual(len(report.recommendations), 1)


if __name__ == "__main__":
    unittest.main()