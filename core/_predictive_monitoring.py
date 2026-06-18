"""[v2.6] 预测性健康监控 (Predictive Health Monitoring)

基于延迟趋势、抖动模式和成功率变化，提前预警节点故障。
核心价值：从"故障后修复"变成"故障前预防"
"""
from __future__ import annotations

import json
import logging
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

logger = logging.getLogger(__name__)


@dataclass
class RiskAssessment:
    """节点风险评估"""
    fingerprint: str
    risk_score: float  # 0-1, 越高风险越大
    risk_level: str  # 'low', 'medium', 'high', 'critical'
    factors: Dict[str, float] = field(default_factory=dict)  # 各风险因子得分
    prediction: str = ""  # 预测描述
    recommended_action: str = ""  # 建议动作


@dataclass
class PredictiveReport:
    """预测性监控报告"""
    timestamp: str
    total_nodes: int
    at_risk_nodes: List[RiskAssessment] = field(default_factory=list)
    healthy_nodes: int = 0
    critical_nodes: int = 0
    summary: str = ""


class PredictiveMonitor:
    """预测性健康监控系统"""
    
    # 风险阈值
    RISK_THRESHOLDS = {
        'low': 0.3,
        'medium': 0.6,
        'high': 0.8,
        'critical': 0.9,
    }
    
    # 延迟恶化阈值（毫秒）
    LATENCY_DEGRADATION_THRESHOLD = 200  # 延迟增加超过200ms视为恶化
    JITTER_SPIKE_THRESHOLD = 100  # 抖动峰值超过100ms
    
    def __init__(self, output_dir: str = "output"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.risk_log = self.output_dir / "risk_assessments.json"
        
    def predict_failures(
        self,
        scored_valid: List[tuple],
        latency_history: Dict,
        node_stability: Dict,
    ) -> PredictiveReport:
        """预测节点故障并生成报告
        
        Args:
            scored_valid: [(node, latency, jitter, score, source, breakdown, test_result), ...]
            latency_history: 延迟历史数据
            node_stability: 节点稳定性数据
            
        Returns:
            PredictiveReport: 预测性监控报告
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        report = PredictiveReport(
            timestamp=timestamp,
            total_nodes=len(scored_valid),
        )
        
        logger.info(f"[PredictiveMonitor] 开始评估 {len(scored_valid)} 个节点的风险...")
        
        for entry in scored_valid:
            if len(entry) < 7:
                continue
            
            node, latency_ms, jitter_ms, score, source, breakdown, test_result = entry
            fingerprint = node.fingerprint()
            
            # 评估风险
            risk = self._assess_node_risk(
                fingerprint=fingerprint,
                current_latency=latency_ms,
                current_jitter=jitter_ms,
                current_score=score,
                latency_history=latency_history.get(fingerprint, {}),
                stability_data=node_stability.get(fingerprint, {}),
            )
            
            # 分类统计
            if risk.risk_level in ('high', 'critical'):
                report.at_risk_nodes.append(risk)
                if risk.risk_level == 'critical':
                    report.critical_nodes += 1
            else:
                report.healthy_nodes += 1
        
        # 按风险分数排序
        report.at_risk_nodes.sort(key=lambda r: r.risk_score, reverse=True)
        
        # 生成摘要
        report.summary = self._generate_summary(report)
        
        # 保存风险日志
        self._save_risk_log(report)
        
        logger.info(
            f"[PredictiveMonitor] 评估完成: "
            f"{report.healthy_nodes} 健康, "
            f"{len(report.at_risk_nodes)} 风险, "
            f"{report.critical_nodes} 危急"
        )
        
        return report
    
    def _assess_node_risk(
        self,
        fingerprint: str,
        current_latency: float,
        current_jitter: float,
        current_score: float,
        latency_history: Dict,
        stability_data: Dict,
    ) -> RiskAssessment:
        """评估单个节点的风险"""
        factors = {}
        
        # 因子1: 延迟趋势风险
        latency_risk = self._calculate_latency_risk(latency_history, current_latency)
        factors['latency_trend'] = latency_risk
        
        # 因子2: 抖动风险
        jitter_risk = self._calculate_jitter_risk(current_jitter)
        factors['jitter'] = jitter_risk
        
        # 因子3: 稳定性风险
        stability_risk = self._calculate_stability_risk(stability_data)
        factors['stability'] = stability_risk
        
        # 因子4: 评分风险
        score_risk = self._calculate_score_risk(current_score)
        factors['score'] = score_risk
        
        # 综合风险分数（加权平均）
        weights = {
            'latency_trend': 0.35,
            'jitter': 0.20,
            'stability': 0.30,
            'score': 0.15,
        }
        
        risk_score = sum(factors[k] * weights[k] for k in weights.keys())
        risk_score = min(1.0, max(0.0, risk_score))
        
        # 确定风险等级
        risk_level = self._determine_risk_level(risk_score)
        
        # 生成预测
        prediction = self._generate_prediction(risk_level, factors, latency_history)
        
        # 生成建议动作
        recommended_action = self._generate_recommended_action(risk_level, factors)
        
        return RiskAssessment(
            fingerprint=fingerprint,
            risk_score=risk_score,
            risk_level=risk_level,
            factors=factors,
            prediction=prediction,
            recommended_action=recommended_action,
        )
    
    def _calculate_latency_risk(self, latency_history: Dict, current_latency: float) -> float:
        """计算延迟趋势风险"""
        history = latency_history.get('history', [])
        
        if not history or len(history) < 3:
            return 0.2  # 历史数据不足，低风险
        
        # 分析最近3次的延迟
        recent_latencies = [h.get('latency_ms', 0) for h in history[-3:]]
        avg_recent = sum(recent_latencies) / len(recent_latencies)
        
        # 风险因子1: 延迟恶化
        if current_latency > avg_recent + self.LATENCY_DEGRADATION_THRESHOLD:
            return 0.9  # 高风险：延迟显著恶化
        
        # 风险因子2: 延迟趋势
        if len(recent_latencies) >= 2:
            trend = recent_latencies[-1] - recent_latencies[0]
            if trend > 100:  # 延迟持续上升
                return 0.7
            elif trend > 50:
                return 0.5
        
        # 风险因子3: 绝对延迟
        if current_latency > 1000:
            return 0.8
        elif current_latency > 500:
            return 0.5
        elif current_latency > 300:
            return 0.3
        
        return 0.1  # 低风险
    
    def _calculate_jitter_risk(self, current_jitter: float) -> float:
        """计算抖动风险"""
        if current_jitter > self.JITTER_SPIKE_THRESHOLD * 2:
            return 0.9  # 极高风险
        elif current_jitter > self.JITTER_SPIKE_THRESHOLD:
            return 0.7  # 高风险
        elif current_jitter > 50:
            return 0.4  # 中风险
        elif current_jitter > 30:
            return 0.2  # 低风险
        
        return 0.1  # 很低风险
    
    def _calculate_stability_risk(self, stability_data: Dict) -> float:
        """计算稳定性风险"""
        consecutive_pass = stability_data.get('consecutive_pass', 0)
        consecutive_fail = stability_data.get('consecutive_fail', 0)
        total_pass = stability_data.get('total_pass', 0)
        total_fail = stability_data.get('total_fail', 0)
        
        # 风险因子1: 连续失败
        if consecutive_fail >= 3:
            return 0.95  # 极高风险
        elif consecutive_fail >= 2:
            return 0.8
        elif consecutive_fail >= 1:
            return 0.6
        
        # 风险因子2: 总体成功率
        total_tests = total_pass + total_fail
        if total_tests > 0:
            success_rate = total_pass / total_tests
            if success_rate < 0.5:
                return 0.8
            elif success_rate < 0.7:
                return 0.5
            elif success_rate < 0.9:
                return 0.3
        
        # 风险因子3: 连续成功（反向指标）
        if consecutive_pass >= 10:
            return 0.05  # 很稳定
        elif consecutive_pass >= 5:
            return 0.1
        elif consecutive_pass >= 3:
            return 0.2
        
        return 0.3  # 默认中低风险
    
    def _calculate_score_risk(self, current_score: float) -> float:
        """计算评分风险"""
        # 评分越低，风险越高
        if current_score < 30:
            return 0.9  # 高风险
        elif current_score < 50:
            return 0.7
        elif current_score < 70:
            return 0.4
        elif current_score < 85:
            return 0.2
        
        return 0.1  # 低风险
    
    def _determine_risk_level(self, risk_score: float) -> str:
        """确定风险等级"""
        if risk_score >= self.RISK_THRESHOLDS['critical']:
            return 'critical'
        elif risk_score >= self.RISK_THRESHOLDS['high']:
            return 'high'
        elif risk_score >= self.RISK_THRESHOLDS['medium']:
            return 'medium'
        else:
            return 'low'
    
    def _generate_prediction(
        self,
        risk_level: str,
        factors: Dict[str, float],
        latency_history: Dict,
    ) -> str:
        """生成预测描述"""
        if risk_level == 'critical':
            return "节点可能在下次测试中失败，建议立即寻找替代节点"
        elif risk_level == 'high':
            return "节点质量正在恶化，预计1-2次测试后可能失效"
        elif risk_level == 'medium':
            return "节点存在潜在风险，需要持续监控"
        else:
            return "节点状态稳定，短期内无故障风险"
    
    def _generate_recommended_action(
        self,
        risk_level: str,
        factors: Dict[str, float],
    ) -> str:
        """生成建议动作"""
        if risk_level == 'critical':
            return "立即准备备用节点，考虑从当前订阅中移除"
        elif risk_level == 'high':
            if factors.get('latency_trend', 0) > 0.7:
                return "延迟持续恶化，建议降低优先级并准备替代方案"
            elif factors.get('stability', 0) > 0.7:
                return "稳定性下降，建议增加测试频率"
            else:
                return "多项指标异常，建议密切关注"
        elif risk_level == 'medium':
            return "保持监控，可在下次测试后重新评估"
        else:
            return "无需特殊处理"
    
    def _generate_summary(self, report: PredictiveReport) -> str:
        """生成摘要"""
        total = report.total_nodes
        at_risk = len(report.at_risk_nodes)
        critical = report.critical_nodes
        
        if critical > 0:
            return f"⚠️ 警告: {critical}个节点处于危急状态，{at_risk}个节点存在风险"
        elif at_risk > total * 0.3:
            return f"⚠️ 注意: {at_risk}个节点({at_risk/total*100:.1f}%)存在风险"
        elif at_risk > 0:
            return f"✓ 良好: 仅{at_risk}个节点存在风险"
        else:
            return "✓ 优秀: 所有节点状态稳定"
    
    def _save_risk_log(self, report: PredictiveReport):
        """保存风险日志"""
        log_data = []
        
        if self.risk_log.exists():
            try:
                with open(self.risk_log, 'r', encoding='utf-8') as f:
                    log_data = json.load(f)
            except Exception:
                log_data = []
        
        # 添加新报告
        report_dict = {
            "timestamp": report.timestamp,
            "total_nodes": report.total_nodes,
            "healthy_nodes": report.healthy_nodes,
            "at_risk_count": len(report.at_risk_nodes),
            "critical_count": report.critical_nodes,
            "summary": report.summary,
            "at_risk_nodes": [
                {
                    "fingerprint": r.fingerprint,
                    "risk_score": r.risk_score,
                    "risk_level": r.risk_level,
                    "factors": r.factors,
                    "prediction": r.prediction,
                }
                for r in report.at_risk_nodes[:10]  # 只保存前10个风险最高的
            ],
        }
        
        log_data.append(report_dict)
        
        # 只保留最近100次
        log_data = log_data[-100:]
        
        with open(self.risk_log, 'w', encoding='utf-8') as f:
            json.dump(log_data, f, ensure_ascii=False, indent=2)
        
        logger.info(f"[PredictiveMonitor] 风险日志已保存: {self.risk_log}")
    
    def save_report(self, report: PredictiveReport):
        """保存完整的预测报告到独立文件"""
        report_path = self.output_dir / "predictive_report.json"
        report_dict = {
            "timestamp": report.timestamp,
            "total_nodes": report.total_nodes,
            "healthy_nodes": report.healthy_nodes,
            "critical_nodes": report.critical_nodes,
            "at_risk_count": len(report.at_risk_nodes),
            "summary": report.summary,
            "at_risk_nodes": [
                {
                    "fingerprint": r.fingerprint,
                    "risk_score": r.risk_score,
                    "risk_level": r.risk_level,
                    "factors": r.factors,
                    "prediction": r.prediction,
                    "recommended_action": r.recommended_action,
                }
                for r in report.at_risk_nodes
            ],
        }
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(report_dict, f, ensure_ascii=False, indent=2)
        logger.info(f"[PredictiveMonitor] 预测报告已保存: {report_path}")