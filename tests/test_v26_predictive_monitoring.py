#!/usr/bin/env python3
"""
[v2.6] 预测性健康监控系统测试
"""
import sys
import os
import unittest
from pathlib import Path
from datetime import datetime

# 添加项目根目录到路径
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from core._predictive_monitoring import (
    PredictiveMonitor,
    RiskAssessment,
    PredictiveReport,
)
from core.parser import Node


class TestPredictiveMonitoring(unittest.TestCase):
    """测试预测性健康监控系统"""
    
    def setUp(self):
        """测试前准备"""
        self.output_dir = Path("/tmp/test_predictive_monitoring")
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.monitor = PredictiveMonitor(str(self.output_dir))
    
    def tearDown(self):
        """测试后清理"""
        import shutil
        if self.output_dir.exists():
            shutil.rmtree(self.output_dir)
    
    def test_init(self):
        """测试初始化"""
        monitor = PredictiveMonitor("/tmp/test")
        self.assertIsNotNone(monitor)
        self.assertEqual(monitor.output_dir, Path("/tmp/test"))
    
    def test_calculate_latency_risk_low(self):
        """测试延迟风险计算 - 低风险"""
        history = {
            'history': [
                {'latency_ms': 100},
                {'latency_ms': 105},
                {'latency_ms': 102},
            ]
        }
        risk = self.monitor._calculate_latency_risk(history, 110)
        self.assertLess(risk, 0.5)
    
    def test_calculate_latency_risk_degradation(self):
        """测试延迟风险计算 - 延迟恶化"""
        history = {
            'history': [
                {'latency_ms': 100},
                {'latency_ms': 105},
                {'latency_ms': 110},
            ]
        }
        # 延迟从110增加到350，恶化240ms > 200ms阈值
        risk = self.monitor._calculate_latency_risk(history, 350)
        self.assertGreaterEqual(risk, 0.9)
    
    def test_calculate_latency_risk_trend(self):
        """测试延迟风险计算 - 上升趋势"""
        history = {
            'history': [
                {'latency_ms': 100},
                {'latency_ms': 150},
                {'latency_ms': 210},
            ]
        }
        # 趋势上升110ms > 100ms
        risk = self.monitor._calculate_latency_risk(history, 220)
        self.assertGreaterEqual(risk, 0.7)
    
    def test_calculate_latency_risk_high_absolute(self):
        """测试延迟风险计算 - 绝对延迟过高"""
        history = {
            'history': [
                {'latency_ms': 800},
                {'latency_ms': 850},
                {'latency_ms': 900},
            ]
        }
        risk = self.monitor._calculate_latency_risk(history, 1100)
        self.assertGreaterEqual(risk, 0.8)
    
    def test_calculate_jitter_risk_low(self):
        """测试抖动风险计算 - 低风险"""
        risk = self.monitor._calculate_jitter_risk(20)
        self.assertLess(risk, 0.3)
    
    def test_calculate_jitter_risk_high(self):
        """测试抖动风险计算 - 高风险"""
        risk = self.monitor._calculate_jitter_risk(150)
        self.assertGreaterEqual(risk, 0.7)
    
    def test_calculate_jitter_risk_critical(self):
        """测试抖动风险计算 - 危急风险"""
        risk = self.monitor._calculate_jitter_risk(250)
        self.assertGreaterEqual(risk, 0.9)
    
    def test_calculate_stability_risk_good(self):
        """测试稳定性风险计算 - 良好"""
        stability_data = {
            'consecutive_pass': 10,
            'consecutive_fail': 0,
            'total_pass': 50,
            'total_fail': 2,
        }
        risk = self.monitor._calculate_stability_risk(stability_data)
        self.assertLessEqual(risk, 0.1)
    
    def test_calculate_stability_risk_consecutive_fail(self):
        """测试稳定性风险计算 - 连续失败"""
        stability_data = {
            'consecutive_pass': 0,
            'consecutive_fail': 3,
            'total_pass': 10,
            'total_fail': 5,
        }
        risk = self.monitor._calculate_stability_risk(stability_data)
        self.assertGreaterEqual(risk, 0.95)
    
    def test_calculate_stability_risk_low_success_rate(self):
        """测试稳定性风险计算 - 低成功率"""
        stability_data = {
            'consecutive_pass': 0,
            'consecutive_fail': 2,  # 连续失败2次会触发更高风险
            'total_pass': 20,
            'total_fail': 30,
        }
        risk = self.monitor._calculate_stability_risk(stability_data)
        self.assertGreaterEqual(risk, 0.7)  # 连续失败2次 + 低成功率
    
    def test_calculate_score_risk_good(self):
        """测试评分风险计算 - 良好"""
        risk = self.monitor._calculate_score_risk(90)
        self.assertLess(risk, 0.3)
    
    def test_calculate_score_risk_poor(self):
        """测试评分风险计算 - 评分过低"""
        risk = self.monitor._calculate_score_risk(25)
        self.assertGreaterEqual(risk, 0.9)
    
    def test_determine_risk_level(self):
        """测试风险等级判定"""
        self.assertEqual(self.monitor._determine_risk_level(0.2), 'low')
        self.assertEqual(self.monitor._determine_risk_level(0.4), 'low')  # < 0.5 是 low
        self.assertEqual(self.monitor._determine_risk_level(0.6), 'medium')  # >= 0.5 且 < 0.7 是 medium
        self.assertEqual(self.monitor._determine_risk_level(0.85), 'high')
        self.assertEqual(self.monitor._determine_risk_level(0.95), 'critical')
    
    def test_generate_prediction(self):
        """测试预测生成"""
        prediction = self.monitor._generate_prediction(
            'critical',
            {'latency_trend': 0.9, 'stability': 0.8},
            {}
        )
        self.assertIsInstance(prediction, str)
        self.assertGreater(len(prediction), 0)
    
    def test_generate_recommended_action(self):
        """测试建议动作生成"""
        action = self.monitor._generate_recommended_action(
            'critical',
            {'latency_trend': 0.9, 'stability': 0.8}
        )
        self.assertIsInstance(action, str)
        self.assertGreater(len(action), 0)
    
    def test_assess_node_risk(self):
        """测试节点风险评估"""
        latency_history = {
            'history': [
                {'latency_ms': 100},
                {'latency_ms': 105},
                {'latency_ms': 110},
            ]
        }
        stability_data = {
            'consecutive_pass': 5,
            'consecutive_fail': 0,
            'total_pass': 20,
            'total_fail': 2,
        }
        
        risk = self.monitor._assess_node_risk(
            fingerprint="test_node",
            current_latency=120,
            current_jitter=30,
            current_score=85,
            latency_history=latency_history,
            stability_data=stability_data,
        )
        
        self.assertIsInstance(risk, RiskAssessment)
        self.assertEqual(risk.fingerprint, "test_node")
        self.assertIsInstance(risk.risk_score, float)
        self.assertGreaterEqual(risk.risk_score, 0)
        self.assertLessEqual(risk.risk_score, 1)
        self.assertIn(risk.risk_level, ['low', 'medium', 'high', 'critical'])
        self.assertIsInstance(risk.factors, dict)
        self.assertIsInstance(risk.prediction, str)
        self.assertIsInstance(risk.recommended_action, str)
    
    def test_predict_failures(self):
        """测试故障预测"""
        # 创建测试数据
        nodes = [
            Node("node1", "vless", "1.2.3.4", 443, {"tls": True}),
            Node("node2", "trojan", "5.6.7.8", 443, {"tls": True}),
        ]
        
        # 模拟scored_valid数据
        scored_valid = []
        for i, node in enumerate(nodes):
            # (node, latency, jitter, score, source, breakdown, test_result)
            latency = 100 + i * 50
            jitter = 20 + i * 30
            score = 85 - i * 20
            scored_valid.append((
                node,
                latency,
                jitter,
                score,
                f"source_{i}",
                {},  # breakdown
                None,  # test_result
            ))
        
        latency_history = {
            "node1|vless|1.2.3.4|443|": {
                'history': [
                    {'latency_ms': 90},
                    {'latency_ms': 95},
                    {'latency_ms': 100},
                ]
            }
        }
        
        node_stability = {
            "node1|vless|1.2.3.4|443|": {
                'consecutive_pass': 5,
                'consecutive_fail': 0,
                'total_pass': 20,
                'total_fail': 2,
            }
        }
        
        report = self.monitor.predict_failures(
            scored_valid=scored_valid,
            latency_history=latency_history,
            node_stability=node_stability,
        )
        
        self.assertIsInstance(report, PredictiveReport)
        self.assertEqual(report.total_nodes, 2)
        self.assertIsInstance(report.at_risk_nodes, list)
        self.assertIsInstance(report.summary, str)
    
    def test_generate_summary(self):
        """测试摘要生成"""
        report = PredictiveReport(
            timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            total_nodes=10,
            healthy_nodes=8,
            critical_nodes=1,
            at_risk_nodes=[
                RiskAssessment("node1", 0.95, "critical", {}, "", ""),
                RiskAssessment("node2", 0.85, "high", {}, "", ""),
            ],
        )
        
        summary = self.monitor._generate_summary(report)
        self.assertIsInstance(summary, str)
        self.assertIn("1", summary)  # critical count
        self.assertIn("2", summary)  # at_risk count
    
    def test_save_report(self):
        """测试报告保存"""
        report = PredictiveReport(
            timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            total_nodes=5,
            healthy_nodes=4,
            critical_nodes=0,
            at_risk_nodes=[
                RiskAssessment("node1", 0.7, "medium", {"latency_trend": 0.7}, "Test prediction", "Test action"),
            ],
        )
        
        self.monitor.save_report(report)
        
        report_path = self.output_dir / "predictive_report.json"
        self.assertTrue(report_path.exists())
        
        import json
        with open(report_path, 'r', encoding='utf-8') as f:
            saved_report = json.load(f)
        
        self.assertEqual(saved_report['total_nodes'], 5)
        self.assertEqual(saved_report['at_risk_count'], 1)
        self.assertEqual(saved_report['at_risk_nodes'][0]['fingerprint'], "node1")


if __name__ == '__main__':
    unittest.main()