"""
[v2.8] 数据洞察服务 (Data Insight Service)

基于历史运行数据，生成趋势分析、异常检测和运营洞察。

核心功能:
1. 趋势分析 - 节点数量、通过率、延迟的长期趋势
2. 异常检测 - 识别突发性变化和异常模式
3. 源质量演变 - 追踪订阅源质量变化
4. 运营建议 - 基于数据生成可操作建议
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
class TrendPoint:
    """趋势数据点"""
    timestamp: str
    value: float
    label: str = ""


@dataclass
class Anomaly:
    """异常事件"""
    metric: str  # 指标名
    severity: str  # info / warning / critical
    description: str
    value: float
    expected_range: Tuple[float, float]
    timestamp: str = field(default_factory=lambda: time.strftime("%Y-%m-%d %H:%M:%S"))


@dataclass
class InsightReport:
    """洞察报告"""
    trends: Dict[str, List[Dict]] = field(default_factory=dict)
    anomalies: List[Dict] = field(default_factory=list)
    source_evolution: Dict[str, Dict] = field(default_factory=dict)
    recommendations: List[str] = field(default_factory=list)
    summary: str = ""
    timestamp: str = field(default_factory=lambda: time.strftime("%Y-%m-%d %H:%M:%S"))


class DataInsightService:
    """数据洞察服务"""

    MAX_HISTORY = 60  # 保留最近60轮数据
    ANOMALY_THRESHOLD = 2.0  # 标准差倍数

    def __init__(self, storage_path: Optional[str] = None):
        self.storage_path = storage_path
        self.history: List[Dict] = []
        if storage_path:
            self._load_history()

    def record_run(self, stats: Dict):
        """记录一次运行数据"""
        point = {
            "timestamp": stats.get("timestamp", time.strftime("%Y-%m-%d %H:%M:%S")),
            "nodes_raw": stats.get("nodes_raw", 0),
            "nodes_dedup": stats.get("nodes_dedup", 0),
            "nodes_tcp_ok": stats.get("nodes_tcp_ok", 0),
            "nodes_real_ok": stats.get("nodes_real_ok", 0),
            "nodes_verified": stats.get("nodes_verified_output", 0),
            "duration_sec": stats.get("duration_sec", 0),
            "degraded_mode": stats.get("degraded_mode", False),
            "top_latencies": stats.get("top_latencies_ms", []),
            "source_scores": stats.get("source_scores", {}),
            "protocol_dist": stats.get("protocol_dist", {}),
        }
        self.history.append(point)

        if len(self.history) > self.MAX_HISTORY:
            self.history = self.history[-self.MAX_HISTORY:]

        if self.storage_path:
            self._save_history()

    def analyze(self) -> InsightReport:
        """执行全面洞察分析"""
        report = InsightReport()

        if len(self.history) < 2:
            report.summary = "历史数据不足，需至少2轮运行数据"
            return report

        # 1. 趋势分析
        report.trends = self._analyze_trends()

        # 2. 异常检测
        anomalies = self._detect_anomalies()
        report.anomalies = [
            {
                "metric": a.metric,
                "severity": a.severity,
                "description": a.description,
                "value": a.value,
                "expected_range": list(a.expected_range),
                "timestamp": a.timestamp,
            }
            for a in anomalies
        ]

        # 3. 源质量演变
        report.source_evolution = self._analyze_source_evolution()

        # 4. 生成建议
        report.recommendations = self._generate_recommendations(
            report.trends, anomalies, report.source_evolution
        )

        # 5. 摘要
        report.summary = self._build_summary(report)

        return report

    def _analyze_trends(self) -> Dict[str, List[Dict]]:
        """分析各项指标趋势"""
        trends = {}
        metrics = [
            "nodes_raw", "nodes_dedup", "nodes_tcp_ok",
            "nodes_real_ok", "nodes_verified", "duration_sec",
        ]

        for metric in metrics:
            points = []
            for h in self.history:
                points.append({
                    "timestamp": h["timestamp"],
                    "value": h.get(metric, 0),
                })
            trends[metric] = points

        # 通过率趋势
        pass_rates = []
        for h in self.history:
            dedup = h.get("nodes_dedup", 0)
            real_ok = h.get("nodes_real_ok", 0)
            rate = (real_ok / dedup * 100) if dedup > 0 else 0
            pass_rates.append({
                "timestamp": h["timestamp"],
                "value": round(rate, 1),
            })
        trends["pass_rate"] = pass_rates

        # 平均延迟趋势
        avg_latencies = []
        for h in self.history:
            lats = h.get("top_latencies", [])
            avg = sum(lats) / len(lats) if lats else 0
            avg_latencies.append({
                "timestamp": h["timestamp"],
                "value": round(avg, 1),
            })
        trends["avg_latency"] = avg_latencies

        return trends

    def _detect_anomalies(self) -> List[Anomaly]:
        """检测异常"""
        anomalies = []

        if len(self.history) < 3:
            return anomalies

        latest = self.history[-1]
        recent = self.history[-10:-1]  # 最近9轮(不含最新)

        # 检测节点数量突变
        for metric in ["nodes_verified", "nodes_real_ok"]:
            values = [h.get(metric, 0) for h in recent]
            if not values:
                continue
            mean = sum(values) / len(values)
            std = (sum((v - mean) ** 2 for v in values) / len(values)) ** 0.5
            current = latest.get(metric, 0)

            if std > 0 and abs(current - mean) > self.ANOMALY_THRESHOLD * std:
                severity = "critical" if abs(current - mean) > 3 * std else "warning"
                direction = "骤降" if current < mean else "激增"
                anomalies.append(Anomaly(
                    metric=metric,
                    severity=severity,
                    description=f"{metric} {direction}: 当前 {current}, 近期均值 {mean:.0f}±{std:.0f}",
                    value=current,
                    expected_range=(mean - 2 * std, mean + 2 * std),
                ))

        # 检测降级模式
        if latest.get("degraded_mode", False):
            anomalies.append(Anomaly(
                metric="degraded_mode",
                severity="critical",
                description="本轮运行进入降级模式，真实测试0通过",
                value=1,
                expected_range=(0, 0),
            ))

        # 检测运行时间异常
        durations = [h.get("duration_sec", 0) for h in recent]
        if durations:
            mean_dur = sum(durations) / len(durations)
            current_dur = latest.get("duration_sec", 0)
            if current_dur > mean_dur * 2 and mean_dur > 0:
                anomalies.append(Anomaly(
                    metric="duration_sec",
                    severity="warning",
                    description=f"运行时间异常: {current_dur:.0f}s, 近期均值 {mean_dur:.0f}s",
                    value=current_dur,
                    expected_range=(0, mean_dur * 1.5),
                ))

        return anomalies

    def _analyze_source_evolution(self) -> Dict[str, Dict]:
        """分析订阅源质量演变"""
        evolution = {}

        # 收集每个源的历史分数
        source_scores_history: Dict[str, List[float]] = defaultdict(list)
        for h in self.history:
            for src, score_data in h.get("source_scores", {}).items():
                if isinstance(score_data, dict):
                    score = score_data.get("score", 0)
                else:
                    score = float(score_data) if isinstance(score_data, (int, float)) else 0
                source_scores_history[src].append(score)

        # 分析每个源的趋势
        for src, scores in source_scores_history.items():
            if len(scores) < 3:
                continue
            recent = scores[-3:]
            trend = "stable"
            if all(recent[i] < recent[i + 1] for i in range(len(recent) - 1)):
                trend = "improving"
            elif all(recent[i] > recent[i + 1] for i in range(len(recent) - 1)):
                trend = "declining"

            evolution[src] = {
                "latest_score": scores[-1] if scores else 0,
                "trend": trend,
                "history_length": len(scores),
                "avg_score": round(sum(scores) / len(scores), 2) if scores else 0,
            }

        return evolution

    def _generate_recommendations(
        self,
        trends: Dict,
        anomalies: List[Anomaly],
        source_evolution: Dict,
    ) -> List[str]:
        """生成运营建议"""
        recommendations = []

        # 基于异常的建议
        critical_count = sum(1 for a in anomalies if a.severity == "critical")
        if critical_count > 0:
            recommendations.append(f"🔴 检测到 {critical_count} 个严重异常，需要立即关注")

        # 基于趋势的建议
        pass_rates = trends.get("pass_rate", [])
        if len(pass_rates) >= 5:
            recent_rates = [p["value"] for p in pass_rates[-5:]]
            if all(recent_rates[i] >= recent_rates[i + 1] for i in range(len(recent_rates) - 1)):
                recommendations.append("📉 通过率持续下降，建议审查订阅源质量或调整测试参数")
            elif all(recent_rates[i] <= recent_rates[i + 1] for i in range(len(recent_rates) - 1)):
                recommendations.append("📈 通过率持续上升，系统运行状态良好")

        # 基于源演变的建议
        declining = [src for src, info in source_evolution.items() if info.get("trend") == "declining"]
        if declining:
            recommendations.append(
                f"⚠️ {len(declining)} 个订阅源质量持续下降，建议替换: {', '.join(declining[:3])}"
            )

        if not recommendations:
            recommendations.append("✓ 系统运行正常，无需干预")

        return recommendations

    def _build_summary(self, report: InsightReport) -> str:
        """构建摘要文本"""
        parts = [f"已分析 {len(self.history)} 轮运行数据"]

        anomaly_count = len(report.anomalies)
        if anomaly_count > 0:
            parts.append(f"检测到 {anomaly_count} 个异常")
        else:
            parts.append("未检测到异常")

        rec_count = len(report.recommendations)
        if rec_count > 0:
            parts.append(f"{rec_count} 条建议")

        return "，".join(parts)

    def _load_history(self):
        """从文件加载历史数据"""
        if not self.storage_path:
            return
        path = Path(self.storage_path)
        if not path.exists():
            return
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            self.history = data.get("runs", [])[-self.MAX_HISTORY:]
        except Exception as e:
            logger.warning(f"加载洞察历史失败: {e}")

    def _save_history(self):
        """保存历史数据到文件"""
        if not self.storage_path:
            return
        path = Path(self.storage_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        try:
            data = {"runs": self.history[-self.MAX_HISTORY:]}
            path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        except Exception as e:
            logger.warning(f"保存洞察历史失败: {e}")
