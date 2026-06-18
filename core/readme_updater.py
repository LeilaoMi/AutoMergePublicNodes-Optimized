"""README 状态区更新器。

保持仓库主页 synchronized with the latest pipeline stats.

[P0-4] 新增 stale 检测：当 stats.json 的 timestamp 超过 24h 没更新时，
在 README 状态区顶部追加 ⚠️ 数据可能已过期 提示，避免 CI 失败时
用户看到的是过时数据。
"""
from __future__ import annotations

import datetime as _dt
import re
from pathlib import Path
from typing import Any, Dict, List, Optional

START_MARKER = "<!-- AUTONODES_STATS_START -->"
END_MARKER = "<!-- AUTONODES_STATS_END -->"
STALE_THRESHOLD_HOURS = 24


def _table(headers: List[str], rows: List[List[object]]) -> str:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(str(x) for x in row) + " |")
    return "\n".join(lines)


def _fmt_rate(numerator: object, denominator: object) -> str:
    try:
        n = int(numerator or 0)
        d = int(denominator or 0)
    except (TypeError, ValueError):
        return "-"
    if d <= 0:
        return "-"
    return f"{n / d * 100:.1f}%"


def _top_sources(stats: Dict[str, Any], limit: int = 5) -> List[List[object]]:
    source_scores = stats.get("source_scores") or {}
    if not isinstance(source_scores, dict):
        return []

    rows: List[List[object]] = []
    for name, data in sorted(
        source_scores.items(),
        key=lambda x: -float(x[1].get("score", 0)) if isinstance(x[1], dict) else 0,
    )[:limit]:
        if not isinstance(data, dict):
            continue
        rows.append([
            name,
            data.get("score", "-"),
            data.get("tested", 0),
            data.get("recommendation", "-"),
        ])
    return rows


def _is_stale(timestamp: str, now: Optional[_dt.datetime] = None, threshold_hours: int = STALE_THRESHOLD_HOURS) -> bool:
    """[P0-4] 检查 stats 是否过期。

    timestamp 格式: 'YYYY-MM-DD HH:MM:SS'。解析失败或缺失都视为过期。
    """
    if not timestamp or not isinstance(timestamp, str):
        return True
    try:
        ts = _dt.datetime.strptime(timestamp.strip(), "%Y-%m-%d %H:%M:%S")
    except (TypeError, ValueError):
        return True
    ref = now or _dt.datetime.now()
    return (ref - ts) > _dt.timedelta(hours=threshold_hours)


def build_readme_stats_block(stats: Dict[str, Any], now: Optional[_dt.datetime] = None) -> str:
    overview_rows = [
        ["更新时间", stats.get("timestamp", "-")],
        ["版本", stats.get("version", "-")],
        ["订阅源", f"{stats.get('sources_healthy', 0)}/{stats.get('sources_total', 0)}"],
        ["原始节点", stats.get("nodes_raw", 0)],
        ["去重后", stats.get("nodes_dedup", 0)],
        ["TCP 可达", stats.get("nodes_tcp_ok", 0)],
        ["真实可用", stats.get("nodes_real_ok", 0)],
        ["真测通过率", _fmt_rate(stats.get("nodes_real_ok"), stats.get("nodes_tcp_ok"))],
        ["Verified 输出", stats.get("nodes_verified_output", 0)],
        ["Global 输出", stats.get("nodes_global_output", 0)],
        ["All 输出", stats.get("nodes_all_output", 0)],
    ]

    top_score_rows = [
        [
            item.get("score", "-"),
            item.get("type", "-"),
            item.get("latency_ms", "-"),
            item.get("source", "-"),
        ]
        for item in (stats.get("top_scores") or [])[:5]
        if isinstance(item, dict)
    ]

    source_rows = _top_sources(stats, limit=5)

    guard = stats.get("output_guard") or {}
    preserved = []
    if isinstance(guard, dict):
        preserved = [name for name, data in guard.items() if isinstance(data, dict) and data.get("preserved")]
    guard_text = "无" if not preserved else ", ".join(preserved)

    lines = [START_MARKER]
    # [P0-4] stale 标记：超过 24h 没更新的数据不可信
    if _is_stale(stats.get("timestamp", ""), now=now):
        lines.append("## ⚠️ 当前运行状态（数据可能已过期）")
    else:
        lines.append("## 当前运行状态")
    lines.append("")
    lines.append(_table(["指标", "数值"], overview_rows))
    lines.append("")
    lines.append(f"> 输出保护：{guard_text}。完整报告见 `output/health_report.md`、`output/stats.json`。")
    lines.append("")
    lines.append("### Top 节点评分")
    lines.append("")
    lines.append(
        _table(["评分", "协议", "延迟(ms)", "来源"], top_score_rows)
        if top_score_rows else "_暂无评分数据_"
    )
    lines.append("")
    lines.append("### Top 来源质量")
    lines.append("")
    lines.append(
        _table(["来源", "评分", "测试数", "建议"], source_rows)
        if source_rows else "_暂无来源评分数据_"
    )
    lines.append("")
    lines.append(END_MARKER)
    return "\n".join(lines)


def update_readme_stats(readme_path: str, stats: Dict[str, Any]) -> bool:
    path = Path(readme_path)
    if not path.exists():
        return False

    original = path.read_text(encoding="utf-8")
    block = build_readme_stats_block(stats)

    if START_MARKER in original and END_MARKER in original:
        before = original.split(START_MARKER, 1)[0].rstrip()
        after = original.split(END_MARKER, 1)[1].lstrip()
        updated = before + "\n\n" + block + "\n\n" + after
    else:
        updated = original.rstrip() + "\n\n" + block + "\n"

    if updated == original:
        return False

    path.write_text(updated, encoding="utf-8")
    return True
