"""
[v2.8] 个性化智能推荐系统 (Personalized Recommendation System)

基于用户行为学习偏好，提供个性化的节点推荐。

核心功能:
1. 用户偏好学习 - 从使用历史中学习用户偏好
2. 偏好画像管理 - 维护用户偏好画像
3. 个性化评分调整 - 根据偏好调整节点评分
4. 智能推荐 - 基于偏好推荐最佳节点
"""
from __future__ import annotations

from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass, field
import logging
import json
from pathlib import Path
from collections import defaultdict

logger = logging.getLogger(__name__)


@dataclass
class UserPreferenceProfile:
    """用户偏好画像"""
    user_id: str
    # 协议偏好权重
    protocol_preferences: Dict[str, float] = field(default_factory=dict)
    # 地区偏好权重
    region_preferences: Dict[str, float] = field(default_factory=dict)
    # 性能指标偏好权重
    metric_preferences: Dict[str, float] = field(default_factory=lambda: {
        "latency": 1.0,
        "jitter": 1.0,
        "speed": 1.0,
        "stability": 1.0,
    })
    # 使用场景偏好
    use_case_preferences: Dict[str, float] = field(default_factory=dict)
    # 历史使用统计
    usage_stats: Dict[str, any] = field(default_factory=lambda: {
        "total_usage_count": 0,
        "total_duration_seconds": 0.0,
        "avg_session_duration": 0.0,
        "preferred_time_slots": {},
    })
    # 置信度 (0-1)
    confidence: float = 0.0


class PersonalizedRecommender:
    """个性化推荐器"""
    
    # 学习率
    LEARNING_RATE = 0.1
    # 最小样本数才计算置信度
    MIN_SAMPLES_FOR_CONFIDENCE = 10
    # 偏好权重范围
    PREFERENCE_RANGE = (0.0, 3.0)
    
    def __init__(self, storage_path: Optional[str] = None):
        self.profiles: Dict[str, UserPreferenceProfile] = {}
        self.storage_path = storage_path
        if storage_path:
            self._load_profiles()
    
    def get_or_create_profile(self, user_id: str) -> UserPreferenceProfile:
        """获取或创建用户偏好画像"""
        if user_id not in self.profiles:
            self.profiles[user_id] = UserPreferenceProfile(user_id=user_id)
            logger.info(f"创建新用户偏好画像: {user_id}")
        return self.profiles[user_id]
    
    def record_usage_event(
        self,
        user_id: str,
        node,  # Node
        duration_seconds: float,
        use_case: str = "unknown",
        metadata: Optional[Dict] = None,
    ):
        """记录用户使用事件，用于学习偏好"""
        profile = self.get_or_create_profile(user_id)
        
        # 更新使用统计
        profile.usage_stats["total_usage_count"] += 1
        profile.usage_stats["total_duration_seconds"] += duration_seconds
        profile.usage_stats["avg_session_duration"] = (
            profile.usage_stats["total_duration_seconds"] / 
            profile.usage_stats["total_usage_count"]
        )
        
        # 学习协议偏好
        protocol = node.type
        if protocol not in profile.protocol_preferences:
            profile.protocol_preferences[protocol] = 1.0
        
        # 增加使用过的协议权重
        profile.protocol_preferences[protocol] = min(
            self.PREFERENCE_RANGE[1],
            profile.protocol_preferences[protocol] * (1 + self.LEARNING_RATE)
        )
        
        # 衰减其他协议权重
        for proto in profile.protocol_preferences:
            if proto != protocol:
                profile.protocol_preferences[proto] = max(
                    self.PREFERENCE_RANGE[0],
                    profile.protocol_preferences[proto] * (1 - self.LEARNING_RATE * 0.5)
                )
        
        # 学习地区偏好
        region = self._extract_region_from_node(node)
        if region:
            if region not in profile.region_preferences:
                profile.region_preferences[region] = 1.0
            
            profile.region_preferences[region] = min(
                self.PREFERENCE_RANGE[1],
                profile.region_preferences[region] * (1 + self.LEARNING_RATE)
            )
            
            # 衰减其他地区
            for reg in profile.region_preferences:
                if reg != region:
                    profile.region_preferences[reg] = max(
                        self.PREFERENCE_RANGE[0],
                        profile.region_preferences[reg] * (1 - self.LEARNING_RATE * 0.3)
                    )
        
        # 学习使用场景偏好
        if use_case not in profile.use_case_preferences:
            profile.use_case_preferences[use_case] = 1.0
        
        profile.use_case_preferences[use_case] = min(
            self.PREFERENCE_RANGE[1],
            profile.use_case_preferences[use_case] * (1 + self.LEARNING_RATE)
        )
        
        # 衰减其他场景
        for uc in profile.use_case_preferences:
            if uc != use_case:
                profile.use_case_preferences[uc] = max(
                    self.PREFERENCE_RANGE[0],
                    profile.use_case_preferences[uc] * (1 - self.LEARNING_RATE * 0.3)
                )
        
        # 更新置信度
        if profile.usage_stats["total_usage_count"] >= self.MIN_SAMPLES_FOR_CONFIDENCE:
            profile.confidence = min(
                1.0,
                profile.usage_stats["total_usage_count"] / 100.0
            )
        
        # 保存
        if self.storage_path:
            self._save_profiles()
    
    def _extract_region_from_node(self, node) -> Optional[str]:
        """从节点提取地区信息"""
        # 尝试从 tag 中提取国旗 emoji
        if hasattr(node, 'tag') and node.tag:
            tag = node.tag
            # 简单检查是否包含国旗 emoji (前2个字符)
            if len(tag) >= 2:
                potential_flag = tag[:2]
                # 国旗 emoji 范围: U+1F1E6 to U+1F1FF
                if len(potential_flag) == 2:
                    cp1, cp2 = ord(potential_flag[0]), ord(potential_flag[1])
                    if 0x1F1E6 <= cp1 <= 0x1F1FF and 0x1F1E6 <= cp2 <= 0x1F1FF:
                        # 转换为 ISO 代码
                        return chr(cp1 - 0x1F1E6 + ord('A')) + chr(cp2 - 0x1F1E6 + ord('A'))
        return None
    
    def adjust_score_by_preference(
        self,
        user_id: str,
        node,
        base_score: float,
        node_stats: Dict,
    ) -> float:
        """根据用户偏好调整节点评分"""
        profile = self.profiles.get(user_id)
        if not profile or profile.confidence < 0.3:
            return base_score
        
        adjusted_score = base_score
        adjustments = []
        
        # 协议偏好调整
        protocol = node.type
        if protocol in profile.protocol_preferences:
            pref_weight = profile.protocol_preferences[protocol]
            # 偏好权重 > 1.0 加分，< 1.0 减分
            adjustment = (pref_weight - 1.0) * 10 * profile.confidence
            adjusted_score += adjustment
            adjustments.append(f"protocol:{protocol}:{adjustment:+.1f}")
        
        # 地区偏好调整
        region = self._extract_region_from_node(node)
        if region and region in profile.region_preferences:
            pref_weight = profile.region_preferences[region]
            adjustment = (pref_weight - 1.0) * 8 * profile.confidence
            adjusted_score += adjustment
            adjustments.append(f"region:{region}:{adjustment:+.1f}")
        
        # 性能指标偏好调整
        # 根据用户历史行为推断偏好
        if profile.usage_stats["total_usage_count"] > 0:
            # 如果用户经常使用，说明偏好稳定性
            if profile.usage_stats["avg_session_duration"] > 3600:  # > 1小时
                stability_bonus = 5 * profile.confidence
                adjusted_score += stability_bonus
                adjustments.append(f"stability_bonus:{stability_bonus:+.1f}")
        
        # 限制评分范围
        adjusted_score = max(0.0, min(100.0, adjusted_score))
        
        if adjustments:
            logger.debug(f"个性化调整: {base_score:.1f} -> {adjusted_score:.1f} ({', '.join(adjustments)})")
        
        return adjusted_score
    
    def recommend_nodes_for_user(
        self,
        user_id: str,
        nodes: List,
        node_stats: Dict[str, Dict],
        base_scores: Dict[str, float],
        top_k: int = 10,
    ) -> List[Dict]:
        """为用户推荐个性化节点列表"""
        profile = self.profiles.get(user_id)
        
        # 调整评分
        adjusted_scores = {}
        for node in nodes:
            fp = node.fingerprint()
            base = base_scores.get(fp, 0.0)
            adjusted = self.adjust_score_by_preference(user_id, node, base, node_stats.get(fp, {}))
            adjusted_scores[fp] = adjusted
        
        # 排序
        scored_nodes = []
        for node in nodes:
            fp = node.fingerprint()
            stats = node_stats.get(fp, {})
            scored_nodes.append({
                "node": node,
                "base_score": base_scores.get(fp, 0.0),
                "adjusted_score": adjusted_scores.get(fp, 0.0),
                "stats": stats,
                "preference_match": self._calculate_preference_match(profile, node),
            })
        
        scored_nodes.sort(key=lambda x: x["adjusted_score"], reverse=True)
        
        # 添加推荐理由
        recommendations = scored_nodes[:top_k]
        for rec in recommendations:
            rec["recommendation_reason"] = self._generate_recommendation_reason(
                profile, rec["node"], rec["stats"], rec["preference_match"]
            )
        
        return recommendations
    
    def _calculate_preference_match(
        self,
        profile: Optional[UserPreferenceProfile],
        node,
    ) -> Dict[str, float]:
        """计算节点与用户偏好的匹配度"""
        if not profile:
            return {}
        
        matches = {}
        
        # 协议匹配度
        protocol = node.type
        if protocol in profile.protocol_preferences:
            matches["protocol"] = profile.protocol_preferences[protocol]
        
        # 地区匹配度
        region = self._extract_region_from_node(node)
        if region and region in profile.region_preferences:
            matches["region"] = profile.region_preferences[region]
        
        return matches
    
    def _generate_recommendation_reason(
        self,
        profile: Optional[UserPreferenceProfile],
        node,
        stats: Dict,
        preference_match: Dict[str, float],
    ) -> str:
        """生成推荐理由"""
        if not profile or profile.confidence < 0.3:
            return "综合评分推荐"
        
        reasons = []
        
        # 协议偏好
        if "protocol" in preference_match and preference_match["protocol"] > 1.5:
            reasons.append(f"您偏好的 {node.type} 协议")
        
        # 地区偏好
        region = self._extract_region_from_node(node)
        if region and "region" in preference_match and preference_match["region"] > 1.5:
            reasons.append(f"您偏好的 {region} 地区")
        
        # 性能指标
        if stats.get("speed_kbps", 0) > 1000 and profile.usage_stats.get("avg_session_duration", 0) > 1800:
            reasons.append("高带宽适合长时间使用")
        
        if stats.get("stability_score", 0) > 85:
            reasons.append("高稳定性")
        
        if not reasons:
            reasons.append("综合评分优秀")
        
        return "，".join(reasons)
    
    def get_recommendation_explanation(self, user_id: str) -> Dict:
        """获取推荐系统的解释说明"""
        profile = self.profiles.get(user_id)
        if not profile:
            return {
                "has_profile": False,
                "message": "暂无用户偏好数据，使用默认推荐",
            }
        
        explanation = {
            "has_profile": True,
            "confidence": profile.confidence,
            "total_usage": profile.usage_stats["total_usage_count"],
            "preferred_protocols": sorted(
                profile.protocol_preferences.items(),
                key=lambda x: x[1],
                reverse=True
            )[:3],
            "preferred_regions": sorted(
                profile.region_preferences.items(),
                key=lambda x: x[1],
                reverse=True
            )[:3],
            "preferred_use_cases": sorted(
                profile.use_case_preferences.items(),
                key=lambda x: x[1],
                reverse=True
            )[:3],
            "message": self._generate_explanation_message(profile),
        }
        
        return explanation
    
    def _generate_explanation_message(self, profile: UserPreferenceProfile) -> str:
        """生成解释说明文本"""
        if profile.confidence < 0.3:
            return "您的偏好数据较少，推荐系统仍在学习您的偏好"
        
        messages = []
        
        # 协议偏好
        if profile.protocol_preferences:
            top_protocol = max(profile.protocol_preferences.items(), key=lambda x: x[1])
            if top_protocol[1] > 1.5:
                messages.append(f"您偏好使用 {top_protocol[0]} 协议")
        
        # 地区偏好
        if profile.region_preferences:
            top_region = max(profile.region_preferences.items(), key=lambda x: x[1])
            if top_region[1] > 1.5:
                messages.append(f"您偏好 {top_region[0]} 地区的节点")
        
        # 使用习惯
        if profile.usage_stats["avg_session_duration"] > 3600:
            messages.append("您倾向于长时间使用，推荐高稳定性节点")
        
        if not messages:
            messages.append("推荐系统已学习您的偏好，将为您个性化推荐节点")
        
        return "。".join(messages)
    
    def reset_profile(self, user_id: str):
        """重置用户偏好画像"""
        if user_id in self.profiles:
            del self.profiles[user_id]
            logger.info(f"已重置用户偏好画像: {user_id}")
            if self.storage_path:
                self._save_profiles()
    
    def _load_profiles(self):
        """从文件加载用户偏好画像"""
        if not self.storage_path:
            return
        
        path = Path(self.storage_path)
        if not path.exists():
            return
        
        try:
            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            for user_id, profile_data in data.items():
                profile = UserPreferenceProfile(
                    user_id=user_id,
                    protocol_preferences=profile_data.get("protocol_preferences", {}),
                    region_preferences=profile_data.get("region_preferences", {}),
                    metric_preferences=profile_data.get("metric_preferences", {}),
                    use_case_preferences=profile_data.get("use_case_preferences", {}),
                    usage_stats=profile_data.get("usage_stats", {}),
                    confidence=profile_data.get("confidence", 0.0),
                )
                self.profiles[user_id] = profile
            
            logger.info(f"已加载 {len(self.profiles)} 个用户偏好画像")
        except Exception as e:
            logger.error(f"加载用户偏好画像失败: {e}")
    
    def _save_profiles(self):
        """保存用户偏好画像到文件"""
        if not self.storage_path:
            return
        
        path = Path(self.storage_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        
        try:
            data = {}
            for user_id, profile in self.profiles.items():
                data[user_id] = {
                    "protocol_preferences": profile.protocol_preferences,
                    "region_preferences": profile.region_preferences,
                    "metric_preferences": profile.metric_preferences,
                    "use_case_preferences": profile.use_case_preferences,
                    "usage_stats": profile.usage_stats,
                    "confidence": profile.confidence,
                }
            
            with open(path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            
            logger.debug(f"已保存 {len(self.profiles)} 个用户偏好画像")
        except Exception as e:
            logger.error(f"保存用户偏好画像失败: {e}")