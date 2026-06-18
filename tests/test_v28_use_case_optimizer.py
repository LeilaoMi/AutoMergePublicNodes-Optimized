"""
[v2.8] 使用场景优化器测试

测试不同使用场景的节点选择和推荐功能。
"""
from __future__ import annotations

import unittest
import sys
from pathlib import Path

# 添加项目根目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from core._use_case_optimizer import UseCaseOptimizer
from core.parser import Node


class TestUseCaseOptimizer(unittest.TestCase):
    """使用场景优化器测试类"""
    
    def setUp(self):
        """测试前准备"""
        self.optimizer = UseCaseOptimizer()
        
        # 创建测试节点
        self.nodes = [
            Node(
                type="vless",
                server="1.2.3.4",
                server_port=443,
                tag="高速节点",
                raw={"uuid": "test-uuid-1"}
            ),
            Node(
                type="vmess",
                server="5.6.7.8",
                server_port=8080,
                tag="稳定节点",
                raw={"uuid": "test-uuid-2"}
            ),
            Node(
                type="trojan",
                server="9.10.11.12",
                server_port=443,
                tag="低延迟节点",
                raw={"password": "test-pass"}
            ),
        ]
        
        # 创建测试统计数据
        self.node_stats = {
            self.nodes[0].fingerprint(): {
                "speed_kbps": 1500,
                "latency_ms": 120,
                "jitter_ms": 20,
                "stability_score": 85,
                "unlocked_services": ["netflix", "youtube"],
            },
            self.nodes[1].fingerprint(): {
                "speed_kbps": 800,
                "latency_ms": 80,
                "jitter_ms": 15,
                "stability_score": 95,
                "unlocked_services": [],
            },
            self.nodes[2].fingerprint(): {
                "speed_kbps": 600,
                "latency_ms": 45,
                "jitter_ms": 10,
                "stability_score": 90,
                "unlocked_services": ["youtube"],
            },
        }
    
    def test_init_default_use_case(self):
        """测试默认使用场景"""
        self.assertEqual(self.optimizer.current_use_case, "work")
    
    def test_set_use_case_valid(self):
        """测试设置有效使用场景"""
        result = self.optimizer.set_use_case("gaming")
        self.assertTrue(result)
        self.assertEqual(self.optimizer.current_use_case, "gaming")
    
    def test_set_use_case_invalid(self):
        """测试设置无效使用场景"""
        result = self.optimizer.set_use_case("invalid_case")
        self.assertFalse(result)
        self.assertEqual(self.optimizer.current_use_case, "work")
    
    def test_get_use_case_weights(self):
        """测试获取使用场景权重"""
        weights = self.optimizer.get_use_case_weights("gaming")
        self.assertIn("latency", weights)
        self.assertIn("jitter", weights)
        self.assertIn("speed", weights)
        self.assertGreater(weights["latency"], weights["speed"])
    
    def test_get_use_case_weights_invalid(self):
        """测试获取无效使用场景权重"""
        weights = self.optimizer.get_use_case_weights("invalid")
        self.assertEqual(weights, {})
    
    def test_get_use_case_requirements(self):
        """测试获取使用场景要求"""
        requirements = self.optimizer.get_use_case_requirements("streaming")
        self.assertIn("min_speed_kbps", requirements)
        self.assertIn("unlock_services", requirements)
    
    def test_filter_nodes_by_requirements_streaming(self):
        """测试流媒体场景节点过滤"""
        self.optimizer.set_use_case("streaming")
        filtered = self.optimizer.filter_nodes_by_requirements(
            self.nodes, self.node_stats
        )
        # 应该过滤掉速度不足的节点
        self.assertLess(len(filtered), len(self.nodes))
    
    def test_filter_nodes_by_requirements_gaming(self):
        """测试游戏场景节点过滤"""
        self.optimizer.set_use_case("gaming")
        filtered = self.optimizer.filter_nodes_by_requirements(
            self.nodes, self.node_stats
        )
        # 游戏场景要求低延迟和低抖动
        self.assertGreater(len(filtered), 0)
    
    def test_filter_nodes_by_requirements_download(self):
        """测试下载场景节点过滤"""
        self.optimizer.set_use_case("download")
        filtered = self.optimizer.filter_nodes_by_requirements(
            self.nodes, self.node_stats
        )
        # 下载场景要求高速
        for node in filtered:
            fp = node.fingerprint()
            stats = self.node_stats.get(fp, {})
            self.assertGreaterEqual(stats.get("speed_kbps", 0), 1000)
    
    def test_calculate_weighted_score(self):
        """测试加权评分计算"""
        weights = {"latency": 40, "jitter": 30, "speed": 30}
        stats = {
            "latency_ms": 100,
            "jitter_ms": 20,
            "speed_kbps": 1000,
        }
        score = self.optimizer._calculate_weighted_score(stats, weights)
        self.assertGreater(score, 0)
        self.assertLessEqual(score, 100)
    
    def test_calculate_weighted_score_zero_weights(self):
        """测试零权重评分"""
        weights = {}
        stats = {"latency_ms": 100}
        score = self.optimizer._calculate_weighted_score(stats, weights)
        self.assertEqual(score, 0.0)
    
    def test_recommend_nodes_for_use_case(self):
        """测试使用场景节点推荐"""
        recommendations = self.optimizer.recommend_nodes_for_use_case(
            self.nodes, self.node_stats, "gaming", top_k=2
        )
        self.assertLessEqual(len(recommendations), 2)
        self.assertGreater(len(recommendations), 0)
        
        # 检查推荐结果结构
        for rec in recommendations:
            self.assertIn("node", rec)
            self.assertIn("score", rec)
            self.assertIn("stats", rec)
            self.assertIn("use_case", rec)
            self.assertIn("match_reason", rec)
    
    def test_recommend_nodes_sorted_by_score(self):
        """测试推荐节点按评分排序"""
        recommendations = self.optimizer.recommend_nodes_for_use_case(
            self.nodes, self.node_stats, "work", top_k=3
        )
        if len(recommendations) >= 2:
            # 确保按评分降序排列
            for i in range(len(recommendations) - 1):
                self.assertGreaterEqual(
                    recommendations[i]["score"],
                    recommendations[i + 1]["score"]
                )
    
    def test_generate_match_reason_streaming(self):
        """测试流媒体场景匹配原因生成"""
        node = self.nodes[0]
        stats = self.node_stats[node.fingerprint()]
        reason = self.optimizer._generate_match_reason(node, stats, "streaming")
        self.assertIsInstance(reason, str)
        self.assertGreater(len(reason), 0)
    
    def test_generate_match_reason_gaming(self):
        """测试游戏场景匹配原因生成"""
        node = self.nodes[2]
        stats = self.node_stats[node.fingerprint()]
        reason = self.optimizer._generate_match_reason(node, stats, "gaming")
        self.assertIsInstance(reason, str)
        self.assertGreater(len(reason), 0)
    
    def test_record_usage(self):
        """测试使用历史记录"""
        node = self.nodes[0]
        initial_count = len(self.optimizer.usage_history)
        
        self.optimizer.record_usage(node, "streaming", 3600)
        
        self.assertEqual(len(self.optimizer.usage_history), initial_count + 1)
        last_record = self.optimizer.usage_history[-1]
        self.assertEqual(last_record["node_fingerprint"], node.fingerprint())
        self.assertEqual(last_record["use_case"], "streaming")
        self.assertEqual(last_record["duration"], 3600)
    
    def test_usage_history_limit(self):
        """测试使用历史记录限制"""
        node = self.nodes[0]
        
        # 添加超过1000条记录
        for i in range(1050):
            self.optimizer.record_usage(node, "work", 100)
        
        # 应该保持在1000条以内
        self.assertLessEqual(len(self.optimizer.usage_history), 1000)
    
    def test_detect_preferred_use_case_empty(self):
        """测试空历史记录的偏好检测"""
        preferred = self.optimizer.detect_preferred_use_case()
        self.assertEqual(preferred, self.optimizer.current_use_case)
    
    def test_detect_preferred_use_case_with_history(self):
        """测试有历史记录的偏好检测"""
        node = self.nodes[0]
        
        # 记录不同场景的使用
        for i in range(10):
            self.optimizer.record_usage(node, "gaming", 3600)
        for i in range(5):
            self.optimizer.record_usage(node, "streaming", 3600)
        
        preferred = self.optimizer.detect_preferred_use_case()
        self.assertEqual(preferred, "gaming")
    
    def test_get_use_case_summary(self):
        """测试使用场景摘要"""
        summary = self.optimizer.get_use_case_summary()
        
        self.assertIn("available_use_cases", summary)
        self.assertIn("current_use_case", summary)
        self.assertIn("usage_stats", summary)
        
        # 检查可用场景
        self.assertGreater(len(summary["available_use_cases"]), 0)
        for case in summary["available_use_cases"]:
            self.assertIn("id", case)
            self.assertIn("name", case)
            self.assertIn("description", case)
    
    def test_get_use_case_summary_with_usage(self):
        """测试有使用记录的摘要"""
        node = self.nodes[0]
        self.optimizer.record_usage(node, "streaming", 7200)
        self.optimizer.record_usage(node, "streaming", 3600)
        
        summary = self.optimizer.get_use_case_summary()
        
        self.assertIn("streaming", summary["usage_stats"])
        streaming_stats = summary["usage_stats"]["streaming"]
        self.assertEqual(streaming_stats["total_duration"], 10800)
        self.assertEqual(streaming_stats["usage_count"], 2)
    
    def test_all_use_cases_have_required_fields(self):
        """测试所有使用场景都有必要字段"""
        for case_id, profile in self.optimizer.USE_CASES.items():
            self.assertIsNotNone(profile.name)
            self.assertIsNotNone(profile.description)
            self.assertIsNotNone(profile.weights)
            self.assertIsNotNone(profile.requirements)
            self.assertIsNotNone(profile.preferences)
            
            # 权重应该包含基本指标
            self.assertIn("latency", profile.weights)
            self.assertIn("jitter", profile.weights)
            self.assertIn("speed", profile.weights)
    
    def test_use_case_weights_sum_positive(self):
        """测试使用场景权重总和为正"""
        for case_id, profile in self.optimizer.USE_CASES.items():
            total_weight = sum(profile.weights.values())
            self.assertGreater(total_weight, 0, f"{case_id} 的权重总和应该大于0")


if __name__ == "__main__":
    unittest.main()