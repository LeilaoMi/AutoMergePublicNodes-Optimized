"""
[v2.8] 使用场景优化器 (Use Case Optimizer)

针对不同使用场景（流媒体、游戏、下载、工作）优化节点选择和配置。

核心功能:
1. 场景识别 - 识别用户的主要使用场景
2. 场景权重配置 - 为不同场景设置不同的评分权重
3. 场景化推荐 - 根据场景推荐最佳节点
"""
from __future__ import annotations

from typing import List, Dict, Optional
from dataclasses import dataclass
import logging

logger = logging.getLogger(__name__)


@dataclass
class UseCaseProfile:
    """使用场景配置"""
    name: str
    description: str
    weights: Dict[str, float]  # 评分权重
    requirements: Dict[str, any]  # 硬性要求
    preferences: Dict[str, float]  # 偏好设置


class UseCaseOptimizer:
    """使用场景优化器"""
    
    # 预定义的使用场景
    USE_CASES = {
        "streaming": UseCaseProfile(
            name="流媒体",
            description="Netflix、YouTube、Disney+ 等流媒体服务",
            weights={
                "latency": 15,      # 延迟不太重要
                "jitter": 20,       # 稳定性重要
                "speed": 35,        # 速度很重要
                "stability": 20,    # 稳定性重要
                "unlock_capability": 10,  # 解锁能力重要
            },
            requirements={
                "min_speed_kbps": 500,  # 最低500KB/s
                "unlock_services": ["netflix", "youtube", "disney"],
            },
            preferences={
                "prefer_high_bandwidth": 1.5,  # 偏好高带宽
                "prefer_stable_connection": 1.3,
            }
        ),
        
        "gaming": UseCaseProfile(
            name="游戏",
            description="在线游戏、低延迟应用",
            weights={
                "latency": 40,      # 延迟最重要
                "jitter": 30,       # 稳定性很重要
                "speed": 15,        # 速度不太重要
                "stability": 15,    # 稳定性重要
                "unlock_capability": 0,
            },
            requirements={
                "max_latency_ms": 100,  # 最高100ms
                "max_jitter_ms": 50,    # 最高50ms抖动
            },
            preferences={
                "prefer_low_latency": 2.0,
                "prefer_stable_connection": 1.5,
            }
        ),
        
        "download": UseCaseProfile(
            name="下载",
            description="大文件下载、批量下载",
            weights={
                "latency": 10,      # 延迟不重要
                "jitter": 10,       # 稳定性不太重要
                "speed": 50,        # 速度最重要
                "stability": 30,    # 稳定性重要
                "unlock_capability": 0,
            },
            requirements={
                "min_speed_kbps": 1000,  # 最低1MB/s
            },
            preferences={
                "prefer_high_bandwidth": 2.0,
                "prefer_stable_connection": 1.2,
            }
        ),
        
        "work": UseCaseProfile(
            name="工作",
            description="视频会议、远程办公、日常浏览",
            weights={
                "latency": 25,      # 延迟重要
                "jitter": 25,       # 稳定性重要
                "speed": 20,        # 速度重要
                "stability": 30,    # 稳定性最重要
                "unlock_capability": 0,
            },
            requirements={
                "min_speed_kbps": 300,  # 最低300KB/s
                "max_latency_ms": 200,  # 最高200ms
            },
            preferences={
                "prefer_stable_connection": 1.8,
                "prefer_low_latency": 1.3,
            }
        ),
    }
    
    def __init__(self):
        self.current_use_case = "work"  # 默认使用工作场景
        self.usage_history = []  # 使用历史记录
    
    def set_use_case(self, use_case: str) -> bool:
        """设置当前使用场景"""
        if use_case not in self.USE_CASES:
            logger.warning(f"未知的使用场景: {use_case}")
            return False
        
        self.current_use_case = use_case
        logger.info(f"切换到使用场景: {self.USE_CASES[use_case].name}")
        return True
    
    def get_use_case_weights(self, use_case: Optional[str] = None) -> Dict[str, float]:
        """获取使用场景的评分权重"""
        case = use_case or self.current_use_case
        if case not in self.USE_CASES:
            return {}
        
        return self.USE_CASES[case].weights
    
    def get_use_case_requirements(self, use_case: Optional[str] = None) -> Dict[str, any]:
        """获取使用场景的硬性要求"""
        case = use_case or self.current_use_case
        if case not in self.USE_CASES:
            return {}
        
        return self.USE_CASES[case].requirements
    
    def filter_nodes_by_requirements(
        self,
        nodes: List,  # List[Node]
        node_stats: Dict[str, Dict],
        use_case: Optional[str] = None,
    ) -> List:
        """根据使用场景的硬性要求过滤节点"""
        case = use_case or self.current_use_case
        if case not in self.USE_CASES:
            return nodes
        
        requirements = self.USE_CASES[case].requirements
        filtered = []
        
        for node in nodes:
            fp = node.fingerprint()
            stats = node_stats.get(fp, {})
            
            # 检查最低速度要求
            if "min_speed_kbps" in requirements:
                if stats.get("speed_kbps", 0) < requirements["min_speed_kbps"]:
                    continue
            
            # 检查最大延迟要求
            if "max_latency_ms" in requirements:
                if stats.get("latency_ms", 999) > requirements["max_latency_ms"]:
                    continue
            
            # 检查最大抖动要求
            if "max_jitter_ms" in requirements:
                if stats.get("jitter_ms", 999) > requirements["max_jitter_ms"]:
                    continue
            
            # 检查解锁服务要求
            if "unlock_services" in requirements:
                required_services = requirements["unlock_services"]
                unlocked = stats.get("unlocked_services", [])
                # 至少解锁一个要求的服务
                if not any(svc in unlocked for svc in required_services):
                    continue
            
            filtered.append(node)
        
        logger.info(f"使用场景 '{self.USE_CASES[case].name}' 过滤: {len(nodes)} -> {len(filtered)} 个节点")
        return filtered
    
    def adjust_scores_for_use_case(
        self,
        scores: Dict[str, float],
        use_case: Optional[str] = None,
    ) -> Dict[str, float]:
        """根据使用场景调整节点评分"""
        case = use_case or self.current_use_case
        if case not in self.USE_CASES:
            return scores
        
        profile = self.USE_CASES[case]
        adjusted = {}
        
        for fp, base_score in scores.items():
            adjusted_score = base_score
            
            # 应用偏好设置
            # 这里简化处理，实际应该根据节点的具体属性调整
            # 例如：如果偏好高带宽且节点速度高，则加分
            
            adjusted[fp] = adjusted_score
        
        return adjusted
    
    def recommend_nodes_for_use_case(
        self,
        nodes: List,
        node_stats: Dict[str, Dict],
        use_case: Optional[str] = None,
        top_k: int = 10,
    ) -> List[Dict]:
        """为指定使用场景推荐最佳节点"""
        case = use_case or self.current_use_case
        if case not in self.USE_CASES:
            return []
        
        # 1. 根据硬性要求过滤
        filtered = self.filter_nodes_by_requirements(nodes, node_stats, case)
        
        # 2. 计算评分
        scores = {}
        for node in filtered:
            fp = node.fingerprint()
            stats = node_stats.get(fp, {})
            
            # 使用场景权重计算评分
            weights = self.get_use_case_weights(case)
            score = self._calculate_weighted_score(stats, weights)
            scores[fp] = score
        
        # 3. 根据偏好调整评分
        scores = self.adjust_scores_for_use_case(scores, case)
        
        # 4. 排序并返回前K个
        sorted_nodes = sorted(
            filtered,
            key=lambda n: scores.get(n.fingerprint(), 0),
            reverse=True
        )[:top_k]
        
        # 5. 构建推荐结果
        recommendations = []
        for node in sorted_nodes:
            fp = node.fingerprint()
            stats = node_stats.get(fp, {})
            recommendations.append({
                "node": node,
                "score": scores.get(fp, 0),
                "stats": stats,
                "use_case": case,
                "match_reason": self._generate_match_reason(node, stats, case),
            })
        
        return recommendations
    
    def _calculate_weighted_score(
        self,
        stats: Dict,
        weights: Dict[str, float],
    ) -> float:
        """根据权重计算加权评分"""
        score = 0.0
        total_weight = sum(weights.values())
        
        if total_weight == 0:
            return 0.0
        
        # 延迟评分 (越低越好，反转)
        if "latency" in weights:
            latency = stats.get("latency_ms", 1000)
            # 假设0-1000ms范围，越低越好
            latency_score = max(0, 100 - latency / 10)
            score += (latency_score / 100) * weights["latency"]
        
        # 抖动评分 (越低越好，反转)
        if "jitter" in weights:
            jitter = stats.get("jitter_ms", 100)
            jitter_score = max(0, 100 - jitter)
            score += (jitter_score / 100) * weights["jitter"]
        
        # 速度评分 (越高越好)
        if "speed" in weights:
            speed = stats.get("speed_kbps", 0)
            # 假设0-2000KB/s范围
            speed_score = min(100, speed / 20)
            score += (speed_score / 100) * weights["speed"]
        
        # 稳定性评分 (越高越好)
        if "stability" in weights:
            stability = stats.get("stability_score", 50)
            score += (stability / 100) * weights["stability"]
        
        # 归一化
        return (score / total_weight) * 100
    
    def _generate_match_reason(
        self,
        node,
        stats: Dict,
        use_case: str,
    ) -> str:
        """生成节点匹配原因说明"""
        reasons = []
        profile = self.USE_CASES[use_case]
        
        if use_case == "streaming":
            if stats.get("speed_kbps", 0) > 1000:
                reasons.append("高带宽适合流媒体")
            unlocked = stats.get("unlocked_services", [])
            if "netflix" in unlocked:
                reasons.append("解锁Netflix")
            if "youtube" in unlocked:
                reasons.append("解锁YouTube")
        
        elif use_case == "gaming":
            if stats.get("latency_ms", 999) < 80:
                reasons.append("超低延迟适合游戏")
            if stats.get("jitter_ms", 999) < 30:
                reasons.append("连接稳定")
        
        elif use_case == "download":
            if stats.get("speed_kbps", 0) > 1500:
                reasons.append("极速下载")
        
        elif use_case == "work":
            if stats.get("stability_score", 0) > 80:
                reasons.append("高稳定性适合工作")
            if stats.get("latency_ms", 999) < 150:
                reasons.append("低延迟视频会议流畅")
        
        if not reasons:
            reasons.append("综合评分优秀")
        
        return "，".join(reasons)
    
    def record_usage(self, node, use_case: str, duration_seconds: float):
        """记录使用历史（用于学习用户偏好）"""
        self.usage_history.append({
            "node_fingerprint": node.fingerprint(),
            "use_case": use_case,
            "duration": duration_seconds,
            "timestamp": None,  # 应该记录实际时间戳
        })
        
        # 保持历史记录不超过1000条
        if len(self.usage_history) > 1000:
            self.usage_history = self.usage_history[-1000:]
    
    def detect_preferred_use_case(self) -> str:
        """根据使用历史检测偏好的使用场景"""
        if not self.usage_history:
            return self.current_use_case
        
        # 统计各场景的使用时长
        use_case_duration = {}
        for record in self.usage_history:
            case = record["use_case"]
            duration = record["duration"]
            use_case_duration[case] = use_case_duration.get(case, 0) + duration
        
        if not use_case_duration:
            return self.current_use_case
        
        # 返回使用时长最长的场景
        preferred = max(use_case_duration.items(), key=lambda x: x[1])[0]
        return preferred
    
    def get_use_case_summary(self) -> Dict:
        """获取使用场景摘要"""
        summary = {
            "available_use_cases": [],
            "current_use_case": self.current_use_case,
            "usage_stats": {},
        }
        
        for case_id, profile in self.USE_CASES.items():
            summary["available_use_cases"].append({
                "id": case_id,
                "name": profile.name,
                "description": profile.description,
            })
        
        # 统计使用历史
        if self.usage_history:
            for record in self.usage_history:
                case = record["use_case"]
                duration = record["duration"]
                if case not in summary["usage_stats"]:
                    summary["usage_stats"][case] = {
                        "total_duration": 0,
                        "usage_count": 0,
                    }
                summary["usage_stats"][case]["total_duration"] += duration
                summary["usage_stats"][case]["usage_count"] += 1
        
        return summary