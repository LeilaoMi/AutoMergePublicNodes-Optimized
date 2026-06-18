"""
[v2.9] 节点质量地图 (Quality Map Generator)

生成基于地理位置和网络拓扑的节点质量可视化数据。

核心功能:
1. 地理质量分布 - 按地区统计节点质量
2. 协议质量分布 - 按协议类型统计质量
3. 质量热力图数据 - 生成可用于可视化的热力图数据
4. 质量对比 - 不同维度的质量对比分析
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
class RegionQuality:
    """地区质量统计"""
    region: str  # 地区代码 (如 US, JP, SG)
    flag: str  # 国旗 emoji
    total_nodes: int = 0
    avg_score: float = 0.0
    avg_latency_ms: float = 0.0
    avg_jitter_ms: float = 0.0
    avg_speed_kbps: float = 0.0
    stability_rate: float = 0.0  # 高稳定性节点占比
    protocols: Dict[str, int] = field(default_factory=dict)
    quality_tier: str = "unknown"  # S/A/B/C/D


@dataclass
class ProtocolQuality:
    """协议质量统计"""
    protocol: str
    total_nodes: int = 0
    avg_score: float = 0.0
    avg_latency_ms: float = 0.0
    success_rate: float = 0.0
    quality_tier: str = "unknown"


@dataclass
class QualityMapReport:
    """质量地图报告"""
    regions: List[Dict] = field(default_factory=list)
    protocols: List[Dict] = field(default_factory=list)
    heatmap_data: List[Dict] = field(default_factory=list)
    quality_distribution: Dict[str, int] = field(default_factory=dict)
    best_regions: List[Dict] = field(default_factory=list)
    worst_regions: List[Dict] = field(default_factory=list)
    summary: str = ""
    timestamp: str = field(default_factory=lambda: time.strftime("%Y-%m-%d %H:%M:%S"))


class QualityMapGenerator:
    """节点质量地图生成器"""

    # 质量等级阈值
    TIER_THRESHOLDS = {
        "S": 90, "A": 75, "B": 60, "C": 45, "D": 0,
    }

    def __init__(self):
        pass

    def generate(
        self,
        scored_valid: List[tuple],  # [(node, latency, jitter, score, source, breakdown, result)]
        flag_map: Dict[str, str],
        stability_data: Dict[str, Dict] = None,
    ) -> QualityMapReport:
        """生成完整质量地图"""
        report = QualityMapReport()
        stability_data = stability_data or {}

        if not scored_valid:
            report.summary = "无可用节点数据"
            return report

        # 1. 按地区聚合
        report.regions = self._aggregate_by_region(scored_valid, flag_map, stability_data)

        # 2. 按协议聚合
        report.protocols = self._aggregate_by_protocol(scored_valid)

        # 3. 热力图数据
        report.heatmap_data = self._generate_heatmap_data(scored_valid, flag_map)

        # 4. 质量分布
        report.quality_distribution = self._calculate_quality_distribution(scored_valid)

        # 5. 最佳/最差地区
        sorted_regions = sorted(report.regions, key=lambda r: r["avg_score"], reverse=True)
        report.best_regions = sorted_regions[:5]
        report.worst_regions = sorted_regions[-5:][::-1] if len(sorted_regions) > 5 else []

        # 6. 摘要
        report.summary = self._build_summary(report)

        return report

    def _aggregate_by_region(
        self,
        scored_valid: List[tuple],
        flag_map: Dict[str, str],
        stability_data: Dict,
    ) -> List[Dict]:
        """按地区聚合质量数据"""
        region_data: Dict[str, Dict] = defaultdict(lambda: {
            "scores": [], "latencies": [], "jitters": [],
            "speeds": [], "protocols": defaultdict(int),
            "stable_count": 0, "flag": "",
        })

        for entry in scored_valid:
            node, lat, jit, score, source, breakdown, result = entry[:7]
            flag = flag_map.get(node.server, "")
            if not flag:
                flag = "🏴"

            # 使用国旗作为地区键
            region_key = flag[:2] if len(flag) >= 2 else flag
            rd = region_data[region_key]
            rd["flag"] = flag
            rd["scores"].append(score)
            rd["latencies"].append(lat)
            rd["jitters"].append(jit)
            rd["protocols"][node.type] += 1

            speed = getattr(result, "speed_kbps", 0) if result else 0
            if speed > 0:
                rd["speeds"].append(speed)

            fp = node.fingerprint()
            consecutive = stability_data.get(fp, {}).get("consecutive_pass", 0) if stability_data else 0
            if consecutive >= 3:
                rd["stable_count"] += 1

        regions = []
        for region_key, rd in region_data.items():
            n = len(rd["scores"])
            avg_score = sum(rd["scores"]) / n if n > 0 else 0
            avg_lat = sum(rd["latencies"]) / n if n > 0 else 0
            avg_jit = sum(rd["jitters"]) / n if n > 0 else 0
            avg_speed = sum(rd["speeds"]) / len(rd["speeds"]) if rd["speeds"] else 0
            stability_rate = rd["stable_count"] / n if n > 0 else 0

            tier = self._classify_tier(avg_score)

            regions.append({
                "region": region_key,
                "flag": rd["flag"],
                "total_nodes": n,
                "avg_score": round(avg_score, 1),
                "avg_latency_ms": round(avg_lat, 1),
                "avg_jitter_ms": round(avg_jit, 1),
                "avg_speed_kbps": round(avg_speed, 1),
                "stability_rate": round(stability_rate, 2),
                "protocols": dict(rd["protocols"]),
                "quality_tier": tier,
            })

        regions.sort(key=lambda r: r["avg_score"], reverse=True)
        return regions

    def _aggregate_by_protocol(self, scored_valid: List[tuple]) -> List[Dict]:
        """按协议聚合质量数据"""
        proto_data: Dict[str, Dict] = defaultdict(lambda: {
            "scores": [], "latencies": [], "count": 0,
        })

        for entry in scored_valid:
            node, lat, jit, score = entry[0], entry[1], entry[2], entry[3]
            pd = proto_data[node.type]
            pd["scores"].append(score)
            pd["latencies"].append(lat)
            pd["count"] += 1

        protocols = []
        for proto, pd in proto_data.items():
            n = pd["count"]
            avg_score = sum(pd["scores"]) / n if n > 0 else 0
            avg_lat = sum(pd["latencies"]) / n if n > 0 else 0

            protocols.append({
                "protocol": proto,
                "total_nodes": n,
                "avg_score": round(avg_score, 1),
                "avg_latency_ms": round(avg_lat, 1),
                "quality_tier": self._classify_tier(avg_score),
            })

        protocols.sort(key=lambda p: p["avg_score"], reverse=True)
        return protocols

    def _generate_heatmap_data(
        self,
        scored_valid: List[tuple],
        flag_map: Dict[str, str],
    ) -> List[Dict]:
        """生成热力图数据点"""
        heatmap = []
        for entry in scored_valid[:200]:  # 限制数据量
            node, lat, jit, score = entry[0], entry[1], entry[2], entry[3]
            flag = flag_map.get(node.server, "")
            heatmap.append({
                "server": node.server,
                "flag": flag,
                "type": node.type,
                "score": round(score, 1),
                "latency_ms": round(lat, 1),
            })
        return heatmap

    def _calculate_quality_distribution(self, scored_valid: List[tuple]) -> Dict[str, int]:
        """计算质量等级分布"""
        dist = {"S": 0, "A": 0, "B": 0, "C": 0, "D": 0}
        for entry in scored_valid:
            score = entry[3]
            tier = self._classify_tier(score)
            dist[tier] += 1
        return dist

    def _classify_tier(self, score: float) -> str:
        """根据分数分类质量等级"""
        if score >= self.TIER_THRESHOLDS["S"]:
            return "S"
        elif score >= self.TIER_THRESHOLDS["A"]:
            return "A"
        elif score >= self.TIER_THRESHOLDS["B"]:
            return "B"
        elif score >= self.TIER_THRESHOLDS["C"]:
            return "C"
        else:
            return "D"

    def _build_summary(self, report: QualityMapReport) -> str:
        """构建摘要"""
        total = sum(r["total_nodes"] for r in report.regions)
        regions_count = len(report.regions)
        s_tier = report.quality_distribution.get("S", 0)
        a_tier = report.quality_distribution.get("A", 0)

        best = report.best_regions[0]["flag"] if report.best_regions else "N/A"
        best_score = report.best_regions[0]["avg_score"] if report.best_regions else 0

        return (
            f"覆盖 {regions_count} 个地区, {total} 个节点 | "
            f"最优地区: {best} ({best_score}分) | "
            f"S级: {s_tier}, A级: {a_tier}"
        )

    def save_report(self, report: QualityMapReport, output_dir: str):
        """保存质量地图报告"""
        path = Path(output_dir) / "quality_map.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        try:
            data = {
                "regions": report.regions,
                "protocols": report.protocols,
                "heatmap_data": report.heatmap_data,
                "quality_distribution": report.quality_distribution,
                "best_regions": report.best_regions,
                "worst_regions": report.worst_regions,
                "summary": report.summary,
                "timestamp": report.timestamp,
            }
            path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
            logger.info(f"质量地图已保存: {path}")
        except Exception as e:
            logger.warning(f"保存质量地图失败: {e}")
