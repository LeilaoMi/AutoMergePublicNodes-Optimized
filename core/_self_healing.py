"""[v2.6] 智能自愈系统 (Self-Healing System)

自动检测和处理：
1. 死源自动禁用
2. 新源自动发现和验证
3. 评分参数自动调优
4. 测试策略自动优化

核心思路：闭环反馈 + 自动决策
"""
from __future__ import annotations

import json
import logging
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import yaml

logger = logging.getLogger(__name__)


@dataclass
class HealingAction:
    """自愈动作记录"""
    action_type: str  # 'disable_source', 'add_source', 'tune_weights', 'optimize_schedule'
    target: str  # 目标（源URL、参数名等）
    reason: str  # 触发原因
    timestamp: str
    success: bool = True
    details: Dict = field(default_factory=dict)


@dataclass
class HealingReport:
    """自愈报告"""
    timestamp: str
    actions: List[HealingAction] = field(default_factory=list)
    health_before: Dict = field(default_factory=dict)
    health_after: Dict = field(default_factory=dict)


class SelfHealingSystem:
    """智能自愈系统"""
    
    def __init__(self, output_dir: str = "output"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.actions_log = self.output_dir / "healing_actions.json"
        
    def analyze_and_heal(
        self,
        sources_yaml: str = "config/sources.yaml",
        stats: Optional[Dict] = None,
    ) -> HealingReport:
        """执行完整的自愈流程"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        report = HealingReport(timestamp=timestamp)
        
        # 记录健康状态（修复前）
        if stats:
            report.health_before = self._extract_health_metrics(stats)
        
        # 1. 源健康诊断和自动禁用
        logger.info("[Self-Healing] 开始源健康诊断...")
        dead_sources = self._detect_dead_sources(stats)
        if dead_sources:
            logger.info(f"[Self-Healing] 发现 {len(dead_sources)} 个死源")
            for source in dead_sources:
                action = self._auto_disable_source(source, sources_yaml)
                report.actions.append(action)
        
        # 2. 新源发现和验证
        logger.info("[Self-Healing] 开始新源发现...")
        new_candidates = self._discover_new_sources()
        if new_candidates:
            logger.info(f"[Self-Healing] 发现 {len(new_candidates)} 个候选源")
            validated = self._auto_validate_sources(new_candidates)
            if validated:
                logger.info(f"[Self-Healing] 验证通过 {len(validated)} 个源")
                for source in validated:
                    action = self._auto_add_source(source, sources_yaml)
                    report.actions.append(action)
        
        # 3. 评分自适应调优
        logger.info("[Self-Healing] 开始评分调优...")
        if stats and self._scoring_needs_tuning(stats):
            logger.info("[Self-Healing] 评分参数需要调优")
            action = self._auto_tune_weights(stats)
            report.actions.append(action)
        
        # 4. 测试策略优化
        logger.info("[Self-Healing] 开始测试策略优化...")
        if stats:
            action = self._optimize_test_schedule(stats)
            if action:
                report.actions.append(action)
        
        # 记录健康状态（修复后）
        if stats:
            report.health_after = self._extract_health_metrics(stats)
        
        # 保存动作日志
        self._save_actions_log(report)
        
        logger.info(f"[Self-Healing] 完成，执行了 {len(report.actions)} 个动作")
        return report
    
    def _detect_dead_sources(self, stats: Optional[Dict]) -> List[str]:
        """检测死源"""
        if not stats:
            return []
        
        dead_sources = []
        source_scores = stats.get("source_scores", {})
        
        for source, score_data in source_scores.items():
            score = score_data.get("score", 1.0)
            consecutive_dead = score_data.get("consecutive_dead", 0)
            
            # 连续3次失败或评分低于0.1视为死源
            if consecutive_dead >= 3 or score < 0.1:
                dead_sources.append(source)
        
        return dead_sources
    
    def _auto_disable_source(self, source: str, sources_yaml: str) -> HealingAction:
        """自动禁用死源"""
        action = HealingAction(
            action_type="disable_source",
            target=source,
            reason="连续失败或评分过低",
            timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        )
        
        try:
            path = Path(sources_yaml)
            if not path.exists():
                action.success = False
                action.details["error"] = "sources.yaml 不存在"
                return action
            
            with open(path, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f) or {}
            
            sources = data.get("sources", [])
            disabled = False
            
            for src in sources:
                if isinstance(src, dict) and src.get("url") == source:
                    src["enabled"] = False
                    disabled = True
                    break
                elif isinstance(src, str) and src == source:
                    # 将字符串格式转换为字典格式并禁用
                    idx = sources.index(src)
                    sources[idx] = {"url": src, "enabled": False}
                    disabled = True
                    break
            
            if disabled:
                with open(path, 'w', encoding='utf-8') as f:
                    yaml.safe_dump(data, f, allow_unicode=True, sort_keys=False)
                logger.info(f"[Self-Healing] 已禁用源: {source}")
            else:
                action.success = False
                action.details["error"] = "未找到该源"
        
        except Exception as e:
            logger.error(f"[Self-Healing] 禁用源失败: {e}")
            action.success = False
            action.details["error"] = str(e)
        
        return action
    
    def _discover_new_sources(self) -> List[str]:
        """发现新源（简化版，实际应调用 source_discovery）"""
        # 这里应该调用 tools/source_discovery.py
        # 简化实现：返回空列表
        return []
    
    def _auto_validate_sources(self, candidates: List[str]) -> List[str]:
        """自动验证候选源"""
        # 简化实现：返回空列表
        # 实际应该：抓取、解析、验证节点数量和质量
        return []
    
    def _auto_add_source(self, source: str, sources_yaml: str) -> HealingAction:
        """自动添加新源"""
        action = HealingAction(
            action_type="add_source",
            target=source,
            reason="自动发现并验证通过",
            timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        )
        
        try:
            path = Path(sources_yaml)
            if not path.exists():
                action.success = False
                action.details["error"] = "sources.yaml 不存在"
                return action
            
            with open(path, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f) or {}
            
            sources = data.get("sources", [])
            
            # 检查是否已存在
            existing_urls = [
                src.get("url") if isinstance(src, dict) else src
                for src in sources
            ]
            
            if source not in existing_urls:
                sources.append({"url": source, "enabled": True})
                data["sources"] = sources
                
                with open(path, 'w', encoding='utf-8') as f:
                    yaml.safe_dump(data, f, allow_unicode=True, sort_keys=False)
                
                logger.info(f"[Self-Healing] 已添加源: {source}")
            else:
                action.details["warning"] = "源已存在"
        
        except Exception as e:
            logger.error(f"[Self-Healing] 添加源失败: {e}")
            action.success = False
            action.details["error"] = str(e)
        
        return action
    
    def _scoring_needs_tuning(self, stats: Dict) -> bool:
        """判断评分是否需要调优"""
        # 简化判断：如果通过率过低或过高，可能需要调优
        real_ok = stats.get("nodes_real_ok", 0)
        tcp_ok = stats.get("nodes_tcp_ok", 0)
        
        if tcp_ok == 0:
            return False
        
        pass_rate = real_ok / tcp_ok
        
        # 通过率低于10%或高于90%可能需要调优
        return pass_rate < 0.1 or pass_rate > 0.9
    
    def _auto_tune_weights(self, stats: Dict) -> HealingAction:
        """自动调优评分权重"""
        action = HealingAction(
            action_type="tune_weights",
            target="scoring.yaml",
            reason="通过率异常，自动调优",
            timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        )
        
        # 简化实现：只是记录，实际应该根据统计调整权重
        action.details["suggestion"] = "建议根据测试结果调整权重"
        action.details["current_pass_rate"] = (
            stats.get("nodes_real_ok", 0) / max(stats.get("nodes_tcp_ok", 1), 1)
        )
        
        return action
    
    def _optimize_test_schedule(self, stats: Dict) -> Optional[HealingAction]:
        """优化测试策略"""
        # 简化实现：根据测试数量调整并发
        nodes_tested = stats.get("nodes_tcp_ok", 0)
        
        if nodes_tested > 1000:
            return HealingAction(
                action_type="optimize_schedule",
                target="test_concurrency",
                reason=f"测试节点数较多({nodes_tested})，建议增加并发",
                timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                details={"suggested_concurrency": min(nodes_tested // 10, 100)},
            )
        
        return None
    
    def _extract_health_metrics(self, stats: Dict) -> Dict:
        """提取健康指标"""
        return {
            "sources_total": stats.get("sources_total", 0),
            "sources_healthy": stats.get("sources_healthy", 0),
            "nodes_real_ok": stats.get("nodes_real_ok", 0),
            "nodes_verified_output": stats.get("nodes_verified_output", 0),
            "degraded_mode": stats.get("degraded_mode", False),
        }
    
    def _save_actions_log(self, report: HealingReport):
        """保存动作日志"""
        log_data = []
        
        if self.actions_log.exists():
            try:
                with open(self.actions_log, 'r', encoding='utf-8') as f:
                    log_data = json.load(f)
            except Exception:
                log_data = []
        
        # 添加新报告
        report_dict = {
            "timestamp": report.timestamp,
            "actions": [
                {
                    "action_type": a.action_type,
                    "target": a.target,
                    "reason": a.reason,
                    "timestamp": a.timestamp,
                    "success": a.success,
                    "details": a.details,
                }
                for a in report.actions
            ],
            "health_before": report.health_before,
            "health_after": report.health_after,
        }
        
        log_data.append(report_dict)
        
        # 只保留最近100次
        log_data = log_data[-100:]
        
        with open(self.actions_log, 'w', encoding='utf-8') as f:
            json.dump(log_data, f, ensure_ascii=False, indent=2)
        
        logger.info(f"[Self-Healing] 动作日志已保存: {self.actions_log}")