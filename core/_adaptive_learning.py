"""
[v2.9] 自适应学习系统 (Adaptive Learning Engine)

基于历史运行数据自动优化评分权重、采样策略和过滤规则。

核心功能:
1. 权重自适应 - 根据实际效果动态调整评分权重
2. 采样优化 - 优化测试采样策略提升效率
3. 规则学习 - 自动学习和优化过滤规则
4. 性能预测 - 预测下轮运行结果
"""
from __future__ import annotations

from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass, field
from collections import defaultdict
import json
import logging
import time
from pathlib import Path

logger = logging.getLogger(__name__)


@dataclass
class WeightAdjustment:
    """权重调整建议"""
    parameter: str  # 参数名
    current_value: float
    suggested_value: float
    reason: str
    confidence: float  # 0-1
    applied: bool = False


@dataclass
class LearningReport:
    """学习报告"""
    weight_adjustments: List[Dict] = field(default_factory=list)
    sampling_suggestions: List[Dict] = field(default_factory=list)
    filter_suggestions: List[Dict] = field(default_factory=list)
    performance_prediction: Dict = field(default_factory=dict)
    learning_progress: Dict = field(default_factory=dict)
    summary: str = ""
    timestamp: str = field(default_factory=lambda: time.strftime("%Y-%m-%d %H:%M:%S"))


class AdaptiveLearningEngine:
    """自适应学习引擎"""

    MAX_HISTORY = 100  # 保留最近100轮
    MIN_HISTORY_FOR_LEARNING = 5  # 至少5轮才开始学习
    MAX_WEIGHT_CHANGE = 0.15  # 单次最大权重变化幅度 (15%)
    LEARNING_RATE = 0.05  # 学习率

    def __init__(self, storage_path: Optional[str] = None):
        self.storage_path = storage_path
        self.history: List[Dict] = []
        self.applied_adjustments: List[Dict] = []
        if storage_path:
            self._load_state()

    def record_run(self, stats: Dict, scoring_config: Dict = None):
        """记录一次运行数据"""
        point = {
            "timestamp": stats.get("timestamp", time.strftime("%Y-%m-%d %H:%M:%S")),
            "nodes_real_ok": stats.get("nodes_real_ok", 0),
            "nodes_verified": stats.get("nodes_verified_output", 0),
            "nodes_dedup": stats.get("nodes_dedup", 0),
            "duration_sec": stats.get("duration_sec", 0),
            "degraded_mode": stats.get("degraded_mode", False),
            "top_latencies": stats.get("top_latencies_ms", []),
            "protocol_dist": stats.get("protocol_dist", {}),
            "protocol_pass_rate": stats.get("protocol_pass_rate", {}),
            "scoring_weights": scoring_config or {},
        }
        self.history.append(point)

        if len(self.history) > self.MAX_HISTORY:
            self.history = self.history[-self.MAX_HISTORY:]

        if self.storage_path:
            self._save_state()

    def learn(self, current_scoring_weights: Dict[str, float] = None) -> LearningReport:
        """执行学习并生成建议"""
        report = LearningReport()

        if len(self.history) < self.MIN_HISTORY_FOR_LEARNING:
            report.summary = f"历史数据不足({len(self.history)}/{self.MIN_HISTORY_FOR_LEARNING}轮)，暂不学习"
            report.learning_progress = {
                "history_count": len(self.history),
                "min_required": self.MIN_HISTORY_FOR_LEARNING,
            }
            return report

        # 1. 权重自适应
        if current_scoring_weights:
            report.weight_adjustments = self._learn_weight_adjustments(
                current_scoring_weights
            )

        # 2. 采样优化建议
        report.sampling_suggestions = self._learn_sampling_strategy()

        # 3. 过滤规则建议
        report.filter_suggestions = self._learn_filter_rules()

        # 4. 性能预测
        report.performance_prediction = self._predict_next_run()

        # 5. 学习进度
        report.learning_progress = {
            "history_count": len(self.history),
            "adjustments_applied": len(self.applied_adjustments),
            "max_history": self.MAX_HISTORY,
        }

        # 6. 摘要
        adj_count = len(report.weight_adjustments)
        samp_count = len(report.sampling_suggestions)
        filt_count = len(report.filter_suggestions)
        report.summary = (
            f"已分析 {len(self.history)} 轮数据: "
            f"{adj_count} 个权重调整, {samp_count} 个采样建议, "
            f"{filt_count} 个过滤建议"
        )

        return report

    def apply_adjustment(self, adjustment: WeightAdjustment) -> bool:
        """应用权重调整"""
        self.applied_adjustments.append({
            "parameter": adjustment.parameter,
            "old_value": adjustment.current_value,
            "new_value": adjustment.suggested_value,
            "reason": adjustment.reason,
            "timestamp": time.time(),
        })
        adjustment.applied = True

        if self.storage_path:
            self._save_state()
        return True

    def _learn_weight_adjustments(
        self, current_weights: Dict[str, float]
    ) -> List[Dict]:
        """学习权重调整"""
        adjustments = []

        if len(self.history) < self.MIN_HISTORY_FOR_LEARNING:
            return adjustments

        # 分析各协议的通过率
        protocol_success: Dict[str, List[float]] = defaultdict(list)
        for h in self.history:
            for proto, rates in h.get("protocol_pass_rate", {}).items():
                if isinstance(rates, dict):
                    passed = rates.get("pass", 0)
                    failed = rates.get("fail", 0)
                    total = passed + failed
                    if total > 0:
                        protocol_success[proto].append(passed / total)

        # 分析延迟与验证数的关系
        recent = self.history[-10:]
        latencies = []
        for h in recent:
            lats = h.get("top_latencies", [])
            if lats:
                latencies.append(sum(lats) / len(lats))

        # 如果延迟持续偏高，建议增加latency权重
        if len(latencies) >= 5:
            avg_lat = sum(latencies) / len(latencies)
            if avg_lat > 200 and "latency" in current_weights:
                current = current_weights.get("latency", 0)
                suggested = min(current + self.MAX_WEIGHT_CHANGE * current, current * 1.1)
                adjustments.append({
                    "parameter": "latency",
                    "current_value": current,
                    "suggested_value": round(suggested, 2),
                    "reason": f"近期平均延迟偏高 ({avg_lat:.0f}ms)，建议提升延迟权重",
                    "confidence": 0.6,
                })

        # 如果某些协议成功率很低，建议降低protocol_bonus
        for proto, rates in protocol_success.items():
            if len(rates) >= 3:
                avg_rate = sum(rates) / len(rates)
                if avg_rate < 0.1 and "source" in current_weights:
                    adjustments.append({
                        "parameter": f"protocol_bonus_{proto}",
                        "current_value": current_weights.get("source", 0),
                        "suggested_value": 0,
                        "reason": f"{proto} 协议成功率仅 {avg_rate*100:.0f}%，建议降低奖励",
                        "confidence": 0.7,
                    })

        return adjustments

    def _learn_sampling_strategy(self) -> List[Dict]:
        """学习采样策略建议"""
        suggestions = []
        if len(self.history) < 5:
            return suggestions

        recent = self.history[-5:]
        avg_dedup = sum(h.get("nodes_dedup", 0) for h in recent) / len(recent)
        avg_real_ok = sum(h.get("nodes_real_ok", 0) for h in recent) / len(recent)
        avg_duration = sum(h.get("duration_sec", 0) for h in recent) / len(recent)

        # 如果通过率很低，说明采样可能不够好
        if avg_dedup > 0:
            pass_rate = avg_real_ok / avg_dedup
            if pass_rate < 0.05:
                suggestions.append({
                    "type": "increase_test_limit",
                    "reason": f"通过率仅 {pass_rate*100:.1f}%，建议增大 test_limit 或优化采样策略",
                    "confidence": 0.7,
                })

        # 如果运行时间过长
        if avg_duration > 300:
            suggestions.append({
                "type": "reduce_test_limit",
                "reason": f"平均运行 {avg_duration:.0f}s，建议降低 test_limit 或增加并发",
                "confidence": 0.5,
            })

        return suggestions

    def _learn_filter_rules(self) -> List[Dict]:
        """学习过滤规则建议"""
        suggestions = []
        if len(self.history) < 10:
            return suggestions

        # 分析协议分布变化
        recent_protocols: Dict[str, List[int]] = defaultdict(list)
        for h in self.history[-10:]:
            for proto, count in h.get("protocol_dist", {}).items():
                recent_protocols[proto].append(count)

        for proto, counts in recent_protocols.items():
            if len(counts) >= 5:
                trend = counts[-1] - counts[0]
                avg = sum(counts) / len(counts)
                if trend < 0 and avg > 0:
                    decline_rate = abs(trend) / avg
                    if decline_rate > 0.5:
                        suggestions.append({
                            "type": "protocol_decline",
                            "protocol": proto,
                            "reason": f"{proto} 节点数量持续下降 ({decline_rate*100:.0f}%)，建议检查源",
                            "confidence": 0.6,
                        })

        return suggestions

    def _predict_next_run(self) -> Dict:
        """预测下轮运行结果"""
        if len(self.history) < 3:
            return {"message": "数据不足，无法预测"}

        recent = self.history[-5:]
        # 简单线性外推
        verified_values = [h.get("nodes_verified", 0) for h in recent]
        avg_verified = sum(verified_values) / len(verified_values)
        trend = (verified_values[-1] - verified_values[0]) / len(verified_values)

        predicted_verified = max(0, avg_verified + trend)

        latencies = []
        for h in recent:
            lats = h.get("top_latencies", [])
            if lats:
                latencies.append(sum(lats) / len(lats))
        predicted_latency = sum(latencies) / len(latencies) if latencies else 0

        return {
            "predicted_verified_nodes": round(predicted_verified),
            "predicted_avg_latency_ms": round(predicted_latency, 1),
            "trend_direction": "improving" if trend > 0 else "declining" if trend < 0 else "stable",
            "confidence": min(0.8, len(recent) / 20),
        }

    def _load_state(self):
        """加载状态"""
        if not self.storage_path:
            return
        path = Path(self.storage_path)
        if not path.exists():
            return
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            self.history = data.get("history", [])[-self.MAX_HISTORY:]
            self.applied_adjustments = data.get("applied_adjustments", [])
        except Exception as e:
            logger.warning(f"加载学习状态失败: {e}")

    def _save_state(self):
        """保存状态"""
        if not self.storage_path:
            return
        path = Path(self.storage_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        try:
            data = {
                "history": self.history[-self.MAX_HISTORY:],
                "applied_adjustments": self.applied_adjustments,
            }
            path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        except Exception as e:
            logger.warning(f"保存学习状态失败: {e}")
