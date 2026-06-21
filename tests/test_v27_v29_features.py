"""
v2.7-v2.9 新功能集成测试
测试所有新增模块的功能
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pytest
from unittest.mock import Mock


class TestNodeDNAAnalysis:
    """v2.7 节点DNA分析测试"""

    def test_analyze_empty_pool(self):
        """测试空节点池"""
        from core._node_dna import NodeDNAAnalyzer
        analyzer = NodeDNAAnalyzer()
        report = analyzer.analyze_node_pool([], {})
        
        assert report.total_providers == 0
        assert report.total_nodes == 0
        assert report.diversity_score == 0.0
        assert report.concentration_risk == "low"

    def test_analyze_single_provider(self):
        """测试单一提供商"""
        from core._node_dna import NodeDNAAnalyzer
        analyzer = NodeDNAAnalyzer()
        
        # 创建3个同IP段的节点
        nodes = []
        for i in range(3):
            node = Mock()
            node.fingerprint.return_value = f"fp_{i}"
            node.server = f"192.168.1.{i+1}"
            node.type = "vless"
            nodes.append(node)
        
        stats = {f"fp_{i}": {"latency_ms": 100, "score": 80} for i in range(3)}
        
        report = analyzer.analyze_node_pool(nodes, stats)
        
        assert report.total_providers == 1
        assert report.total_nodes == 3
        assert report.concentration_risk == "high"

    def test_diversity_scoring(self):
        """测试多样性评分"""
        from core._node_dna import NodeDNAAnalyzer
        analyzer = NodeDNAAnalyzer()
        
        # 创建多个提供商的节点
        nodes = []
        for i in range(10):
            node = Mock()
            node.fingerprint.return_value = f"fp_{i}"
            # 使用不同的IP段
            node.server = f"192.168.{i//2}.{i%2+1}"
            node.type = "vless"
            nodes.append(node)
        
        stats = {f"fp_{i}": {"latency_ms": 100, "score": 80} for i in range(10)}
        
        report = analyzer.analyze_node_pool(nodes, stats)
        
        assert report.total_providers > 1
        assert 0.0 <= report.diversity_score <= 1.0


class TestUseCaseOptimizer:
    """v2.8 使用场景优化测试"""

    def test_recommend_for_streaming(self):
        """测试流媒体场景推荐"""
        optimizer = UseCaseOptimizer()
        
        # 创建模拟节点
        nodes = []
        for i in range(5):
            node = Mock()
            node.fingerprint.return_value = f"fp_{i}"
            node.tag = f"Node_{i}"
            node.type = "vless"
            nodes.append(node)
        
        stats = {
            f"fp_{i}": {
                "latency_ms": 100,
                "jitter_ms": 10,
                "score": 80 + i,
                "speed_kbps": 1000 + i * 100,
                "unlocked_services": ["netflix", "youtube"],
            }
            for i in range(5)
        }
        
        recs = optimizer.recommend_nodes_for_use_case(nodes, stats, "streaming", top_k=3)
        
        assert len(recs) <= 3
        assert all("node" in r for r in recs)
        assert all("score" in r for r in recs)
        assert all("match_reason" in r for r in recs)

    def test_recommend_for_gaming(self):
        """测试游戏场景推荐"""
        optimizer = UseCaseOptimizer()
        
        nodes = []
        for i in range(5):
            node = Mock()
            node.fingerprint.return_value = f"fp_{i}"
            node.tag = f"Node_{i}"
            node.type = "vless"
            nodes.append(node)
        
        stats = {
            f"fp_{i}": {
                "latency_ms": 50 + i * 20,  # 50-130ms
                "jitter_ms": 5 + i * 5,
                "score": 80,
                "speed_kbps": 500,
            }
            for i in range(5)
        }
        
        recs = optimizer.recommend_nodes_for_use_case(nodes, stats, "gaming", top_k=3)
        
        # 游戏场景应该优先低延迟
        assert len(recs) <= 3


class TestPersonalizedRecommender:
    """v2.8 个性化推荐测试"""

    def test_recommend_new_user(self):
        """测试新用户推荐"""
        recommender = PersonalizedRecommender()
        
        nodes = []
        for i in range(5):
            node = Mock()
            node.fingerprint.return_value = f"fp_{i}"
            node.tag = f"Node_{i}"
            node.type = "vless"
            node.server = f"192.168.1.{i+1}"
            nodes.append(node)
        
        stats = {f"fp_{i}": {"latency_ms": 100, "jitter_ms": 10, "score": 80} for i in range(5)}
        base_scores = {f"fp_{i}": 80.0 for i in range(5)}
        
        recs = recommender.recommend_nodes_for_user("user1", nodes, stats, base_scores, top_k=3)
        
        assert len(recs) <= 3
        assert all("node" in r for r in recs)
        assert all("base_score" in r for r in recs)
        assert all("adjusted_score" in r for r in recs)

    def test_profile_creation(self):
        """测试用户画像创建"""
        recommender = PersonalizedRecommender()
        
        profile = recommender.get_or_create_profile("user1")
        
        assert profile.user_id == "user1"
        assert "user1" in recommender.profiles


class TestOpenAPIPlatform:
    """v2.8 开放API平台测试"""

    def test_generate_api_docs(self):
        """测试API文档生成"""
        platform = OpenAPIPlatform()
        
        docs = platform.generate_api_docs()
        
        assert docs["title"] == "AutoNodes Open API"
        assert docs["version"] == "2.8.0"
        assert "endpoints" in docs
        assert len(docs["endpoints"]) > 0

    def test_get_api_summary(self):
        """测试API摘要"""
        platform = OpenAPIPlatform()
        
        summary = platform.get_api_summary()
        
        assert "active_api_keys" in summary
        assert "total_feedback" in summary


class TestSmartFailover:
    """v2.8 智能故障转移测试"""

    def test_build_failover_chain(self):
        """测试构建故障转移链"""
        manager = SmartFailoverManager()
        
        # 创建主节点和备选节点
        failed_node = Mock()
        failed_node.fingerprint.return_value = "failed_fp"
        failed_node.server = "192.168.1.1"
        failed_node.type = "vless"
        
        scored_valid = []
        for i in range(5):
            node = Mock()
            node.fingerprint.return_value = f"fp_{i}"
            node.tag = f"Node_{i}"
            node.server = f"192.168.1.{i+2}"
            node.type = "vless"
            scored_valid.append((node, 100, 10, 80, "source", {}, Mock()))
        
        stats = {f"fp_{i}": {} for i in range(5)}
        flag_map = {f"192.168.1.{i+2}": "🇺🇸" for i in range(5)}
        
        chain = manager.build_failover_chain(failed_node, scored_valid, stats, flag_map)
        
        assert len(chain) <= manager.FAILOVER_CHAIN_DEPTH
        assert all("node" in c for c in chain)
        assert all("strategy" in c for c in chain)


class TestDataInsightService:
    """v2.8 数据洞察服务测试"""

    def test_record_run(self):
        """测试记录运行数据"""
        service = DataInsightService()
        
        stats = {
            "timestamp": "2024-01-01 00:00:00",
            "nodes_verified_output": 100,
            "duration_sec": 300,
        }
        
        service.record_run(stats)
        
        assert len(service.history) == 1
        assert service.history[0]["nodes_verified"] == 100

    def test_analyze_insufficient_data(self):
        """测试数据不足时的分析"""
        service = DataInsightService()
        
        report = service.analyze()
        
        assert "历史数据不足" in report.summary


class TestFederatedTestNetwork:
    """v2.9 联邦式测试网络测试"""

    def test_register_contributor(self):
        """测试注册贡献者"""
        network = FederatedTestNetwork()
        
        contributor = network.register_contributor(
            "c1", "TestUser", "US", ["vless", "vmess"]
        )
        
        assert contributor.id == "c1"
        assert contributor.name == "TestUser"
        assert contributor.region == "US"
        assert "c1" in network.contributors

    def test_generate_report(self):
        """测试生成报告"""
        network = FederatedTestNetwork()
        
        report = network.generate_report()
        
        assert report.total_contributors == 0
        assert report.active_contributors == 0


class TestCommunityDriven:
    """v2.9 社区驱动系统测试"""

    def test_register_member(self):
        """测试注册成员"""
        system = CommunityDrivenSystem()
        
        member = system.register_member("m1", "TestUser")
        
        assert member.member_id == "m1"
        assert member.name == "TestUser"
        assert "m1" in system.members

    def test_generate_report(self):
        """测试生成报告"""
        system = CommunityDrivenSystem()
        
        report = system.generate_report()
        
        assert report.total_members == 0
        assert report.total_submissions == 0


class TestQualityMap:
    """v2.9 节点质量地图测试"""

    def test_generate_empty(self):
        """测试空数据生成"""
        generator = QualityMapGenerator()
        
        report = generator.generate([], {}, {})
        
        assert len(report.regions) == 0
        assert len(report.protocols) == 0

    def test_generate_with_data(self):
        """测试有数据时生成"""
        generator = QualityMapGenerator()
        
        scored_valid = []
        for i in range(5):
            node = Mock()
            node.fingerprint.return_value = f"fp_{i}"
            node.server = f"192.168.1.{i+1}"
            node.type = "vless"
            result = Mock()
            result.speed_kbps = 1000
            scored_valid.append((node, 100, 10, 80, "source", {}, result))
        
        flag_map = {f"192.168.1.{i+1}": "🇺🇸" for i in range(5)}
        
        report = generator.generate(scored_valid, flag_map, {})
        
        assert len(report.regions) > 0
        # total_nodes 在 regions 内部，不在 report 顶层
        total = sum(r["total_nodes"] for r in report.regions)
        assert total > 0
        assert len(report.protocols) > 0
        assert report.summary != ""


class TestAdaptiveLearning:
    """v2.9 自适应学习系统测试"""

    def test_record_run(self):
        """测试记录运行数据"""
        engine = AdaptiveLearningEngine()
        
        stats = {
            "timestamp": "2024-01-01 00:00:00",
            "nodes_verified": 100,
            "duration_sec": 300,
        }
        
        engine.record_run(stats, {"latency": 30, "speed": 20})
        
        assert len(engine.history) == 1

    def test_learn_insufficient_data(self):
        """测试数据不足时的学习"""
        engine = AdaptiveLearningEngine()
        
        report = engine.learn({"latency": 30})
        
        assert "历史数据不足" in report.summary
        assert len(report.weight_adjustments) == 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
