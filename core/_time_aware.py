"""[v2.5] 时段自适应调度 — 不同时段对不同地区节点给予评分调整。

背景：
  - 晚高峰（18-23 点 CST）日本/韩国节点延迟上升最多（中国出口拥堵）
  - 凌晨（0-6 点）国际链路空闲，所有地区延迟最低
  - 美国节点受中国时段影响较小（物理距离远，瓶颈在跨太平洋链路而非最后一公里）

此模块提供时段感知的评分微调，不改变主评分逻辑，只做 bonus/penalty。
"""
from __future__ import annotations

from datetime import datetime, timezone, timedelta
from typing import Dict, Optional

CST = timezone(timedelta(hours=8))

# 时段定义
TIME_SLOTS = {
    "night": (0, 6),        # 凌晨，国际链路空闲
    "morning": (6, 9),      # 早高峰
    "forenoon": (9, 12),    # 上午
    "noon": (12, 14),       # 午休
    "afternoon": (14, 18),  # 下午
    "evening": (18, 23),    # 晚高峰，延迟最高
    "late_night": (23, 24), # 深夜
}

# 时段 → 地区 → 评分调整（正值加分，负值扣分）
# 基于经验数据：晚高峰日韩延迟上升 30-50%，美国影响 < 10%
TIME_SLOT_BONUSES: Dict[str, Dict[str, float]] = {
    "evening": {
        "JP": -0.08, "KR": -0.08, "TW": -0.06, "HK": -0.05,
        "SG": -0.04, "US": 0.04, "EU": 0.04, "CA": 0.03,
    },
    "night": {
        "JP": 0.06, "KR": 0.06, "SG": 0.04, "US": 0.03,
        "HK": 0.04, "TW": 0.04,
    },
    "morning": {
        "US": -0.04, "EU": -0.04, "CA": -0.03,
    },
    "noon": {
        "JP": -0.03, "KR": -0.03,
    },
    "late_night": {
        "JP": 0.04, "KR": 0.04, "SG": 0.03,
    },
}


def get_time_slot(now: Optional[datetime] = None) -> str:
    """返回当前 CST 时段标签。"""
    if now is None:
        now = datetime.now(CST)
    hour = now.hour
    for slot_name, (start, end) in TIME_SLOTS.items():
        if start <= hour < end:
            return slot_name
    return "late_night"


def time_slot_bonus(region: str, slot: Optional[str] = None) -> float:
    """根据时段和地区返回评分调整值。

    Args:
        region: ISO 国家代码（如 "JP", "US"）
        slot: 时段标签（None 时自动获取当前时段）

    Returns:
        评分调整值（加到归一化分数上，范围约 -0.08 ~ +0.06）
    """
    if slot is None:
        slot = get_time_slot()
    bonuses = TIME_SLOT_BONUSES.get(slot, {})
    return bonuses.get(region, 0.0)


def time_slot_description(slot: Optional[str] = None) -> str:
    """返回时段的可读描述。"""
    if slot is None:
        slot = get_time_slot()
    descriptions = {
        "night": "凌晨 (0-6): 国际链路空闲，延迟最低",
        "morning": "早高峰 (6-9): 国内出口拥堵开始",
        "forenoon": "上午 (9-12): 链路逐渐稳定",
        "noon": "午休 (12-14): 小高峰",
        "afternoon": "下午 (14-18): 相对平稳",
        "evening": "晚高峰 (18-23): 延迟最高，日韩节点受影响最大",
        "late_night": "深夜 (23-24): 链路逐渐恢复",
    }
    return descriptions.get(slot, f"未知时段: {slot}")