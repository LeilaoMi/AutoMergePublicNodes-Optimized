"""
[v2.8] 智能故障转移系统 (Smart Failover Manager)

当节点失效时，自动选择最佳替代节点，保障连接连续性。

核心功能:
1. 故障检测 - 快速识别节点失效
2. 替代推荐 - 根据相似度推荐替代节点
3. 转移策略 - 多级降级策略保障可用性
4. 历史学习 - 从故障历史中优化转移路径
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
class FailoverRecord:
    """故障转移记录"""
    failed_fp: str  # 失败节点指纹
    failed_tag: str  # 失败节点标签
    fallback_fp: str  # 替代节点指纹
    fallback_tag: str  # 替代节点标签
    reason: str  # 失败原因
    strategy: str  # 转移策略: same_provider / same_protocol / same_region / any
    timestamp: float = field(default_factory=time.time)
    success: bool = False  # 替代节点是否成功


@dataclass
class FailoverReport:
    """故障转移报告"""
    total_failovers: int = 0
    successful_failovers: int = 0
    failed_failovers: int = 0
    avg_fallback_rank: float = 0.0  # 平均替代节点排名
    strategy_distribution: Dict[str, int] = field(default_factory=dict)
    recent_failovers: List[Dict] = field(default_factory=list)
    failover_paths: Dict[str, List[str]] = field(default_factory=dict)  # fp -> [fallback_fps]
    timestamp: str = field(default_factory=lambda: time.strftime("%Y-%m-%d %H:%M:%S"))


class SmartFailoverManager:
    """智能故障转移管理器"""

    MAX_FAILOVER_HISTORY = 500
    FAILOVER_CHAIN_DEPTH = 5  # 最多尝试5个替代节点

    def __init__(self, storage_path: Optional[str] = None):
        self.storage_path = storage_path
        self.failover_history: List[FailoverRecord] = []
        self.failover_paths: Dict[str, List[str]] = defaultdict(list)  # 已知转移路径
        if storage_path:
            self._load_history()

    def record_failover(self, record: FailoverRecord):
        """记录一次故障转移"""
        self.failover_history.append(record)

        # 更新转移路径
        if record.success:
            self.failover_paths[record.failed_fp].append(record.fallback_fp)
            # 保持路径列表不超过10条
            if len(self.failover_paths[record.failed_fp]) > 10:
                self.failover_paths[record.failed_fp] = \
                    self.failover_paths[record.failed_fp][-10:]

        # 限制历史记录
        if len(self.failover_history) > self.MAX_FAILOVER_HISTORY:
            self.failover_history = self.failover_history[-self.MAX_FAILOVER_HISTORY:]

        if self.storage_path:
            self._save_history()

    def build_failover_chain(
        self,
        failed_node,  # Node
        scored_valid: List[tuple],  # [(node, latency, jitter, score, source, breakdown, result)]
        node_stats: Dict[str, Dict],
        flag_map: Dict[str, str] = None,
    ) -> List[Dict]:
        """构建故障转移链：为失败节点生成有序的替代节点列表"""
        flag_map = flag_map or {}
        chain = []
        failed_fp = failed_node.fingerprint()
        failed_server = failed_node.server
        failed_type = failed_node.type

        # 提取失败节点的IP段
        failed_ip_prefix = ".".join(failed_server.split(".")[:3]) if "." in failed_server else ""
        failed_flag = flag_map.get(failed_server, "")

        # 策略1: 历史成功转移路径
        known_paths = self.failover_paths.get(failed_fp, [])
        for fp in known_paths:
            for entry in scored_valid:
                if entry[0].fingerprint() == fp and entry[0].fingerprint() != failed_fp:
                    chain.append({
                        "node": entry[0],
                        "score": entry[3],
                        "strategy": "historical_path",
                        "reason": "历史成功转移路径",
                        "latency_ms": entry[1],
                        "jitter_ms": entry[2],
                    })

        # 策略2: 同提供商(同IP段) + 同协议
        for entry in scored_valid:
            n = entry[0]
            if n.fingerprint() == failed_fp:
                continue
            n_prefix = ".".join(n.server.split(".")[:3]) if "." in n.server else ""
            if n_prefix == failed_ip_prefix and n.type == failed_type:
                chain.append({
                    "node": n,
                    "score": entry[3],
                    "strategy": "same_provider_protocol",
                    "reason": f"同提供商同协议 ({n.type})",
                    "latency_ms": entry[1],
                    "jitter_ms": entry[2],
                })

        # 策略3: 同地区 + 同协议
        for entry in scored_valid:
            n = entry[0]
            if n.fingerprint() == failed_fp:
                continue
            n_flag = flag_map.get(n.server, "")
            if n_flag and n_flag == failed_flag and n.type == failed_type:
                chain.append({
                    "node": n,
                    "score": entry[3],
                    "strategy": "same_region_protocol",
                    "reason": f"同地区同协议 ({failed_flag}, {n.type})",
                    "latency_ms": entry[1],
                    "jitter_ms": entry[2],
                })

        # 策略4: 同协议 (任意地区)
        for entry in scored_valid:
            n = entry[0]
            if n.fingerprint() == failed_fp:
                continue
            if n.type == failed_type:
                chain.append({
                    "node": n,
                    "score": entry[3],
                    "strategy": "same_protocol",
                    "reason": f"同协议 ({n.type})",
                    "latency_ms": entry[1],
                    "jitter_ms": entry[2],
                })

        # 策略5: 任意可用节点 (最终降级)
        for entry in scored_valid:
            n = entry[0]
            if n.fingerprint() == failed_fp:
                continue
            chain.append({
                "node": n,
                "score": entry[3],
                "strategy": "any_available",
                "reason": "任意可用节点",
                "latency_ms": entry[1],
                "jitter_ms": entry[2],
            })

        # 去重：保留第一次出现(策略优先级最高的)
        seen = set()
        deduped = []
        for item in chain:
            fp = item["node"].fingerprint()
            if fp not in seen:
                seen.add(fp)
                deduped.append(item)

        # 按策略优先级排序，同策略内按score排序
        strategy_order = {
            "historical_path": 0,
            "same_provider_protocol": 1,
            "same_region_protocol": 2,
            "same_protocol": 3,
            "any_available": 4,
        }
        deduped.sort(key=lambda x: (strategy_order.get(x["strategy"], 99), -x["score"]))

        return deduped[:self.FAILOVER_CHAIN_DEPTH]

    def generate_report(
        self,
        scored_valid: List[tuple],
        failed_nodes: List = None,
        flag_map: Dict[str, str] = None,
    ) -> FailoverReport:
        """生成故障转移报告"""
        report = FailoverReport()

        # 统计历史转移
        for rec in self.failover_history:
            report.total_failovers += 1
            if rec.success:
                report.successful_failovers += 1
            else:
                report.failed_failovers += 1
            report.strategy_distribution[rec.strategy] = \
                report.strategy_distribution.get(rec.strategy, 0) + 1

        # 最近的10次转移
        for rec in self.failover_history[-10:]:
            report.recent_failovers.append({
                "failed": rec.failed_tag,
                "fallback": rec.fallback_tag,
                "strategy": rec.strategy,
                "success": rec.success,
                "timestamp": rec.timestamp,
            })

        # 转移路径
        report.failover_paths = dict(self.failover_paths)

        return report

    def _load_history(self):
        """从文件加载故障转移历史"""
        if not self.storage_path:
            return
        path = Path(self.storage_path)
        if not path.exists():
            return
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            self.failover_paths = defaultdict(list, data.get("paths", {}))
            for item in data.get("history", [])[-self.MAX_FAILOVER_HISTORY:]:
                self.failover_history.append(FailoverRecord(
                    failed_fp=item.get("failed_fp", ""),
                    failed_tag=item.get("failed_tag", ""),
                    fallback_fp=item.get("fallback_fp", ""),
                    fallback_tag=item.get("fallback_tag", ""),
                    reason=item.get("reason", ""),
                    strategy=item.get("strategy", ""),
                    timestamp=item.get("timestamp", 0),
                    success=item.get("success", False),
                ))
        except Exception as e:
            logger.warning(f"加载故障转移历史失败: {e}")

    def _save_history(self):
        """保存故障转移历史到文件"""
        if not self.storage_path:
            return
        path = Path(self.storage_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        try:
            data = {
                "paths": dict(self.failover_paths),
                "history": [
                    {
                        "failed_fp": r.failed_fp,
                        "failed_tag": r.failed_tag,
                        "fallback_fp": r.fallback_fp,
                        "fallback_tag": r.fallback_tag,
                        "reason": r.reason,
                        "strategy": r.strategy,
                        "timestamp": r.timestamp,
                        "success": r.success,
                    }
                    for r in self.failover_history[-self.MAX_FAILOVER_HISTORY:]
                ],
            }
            path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        except Exception as e:
            logger.warning(f"保存故障转移历史失败: {e}")
