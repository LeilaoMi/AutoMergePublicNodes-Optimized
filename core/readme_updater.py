"""README status block updater.

Keeps the repository homepage synchronized with the latest pipeline stats.
"""
from __future__ import annotations

from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Dict, List

START_MARKER = "<!-- AUTONODES_STATS_START -->"
END_MARKER = "<!-- AUTONODES_STATS_END -->"


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


def _beijing_time(ts: object) -> str:
    """stats.json 的 timestamp 是 UTC，README 显示北京时间。"""
    try:
        dt = datetime.strptime(str(ts), "%Y-%m-%d %H:%M:%S") + timedelta(hours=8)
    except (TypeError, ValueError):
        return str(ts or "-")
    return dt.strftime("%Y-%m-%d %H:%M") + "（北京时间）"


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


def build_readme_stats_block(stats: Dict[str, Any]) -> str:
    overview_rows = [
        ["更新时间", _beijing_time(stats.get("timestamp"))],
        ["订阅源（可用/总数）", f"{stats.get('sources_healthy', 0)}/{stats.get('sources_total', 0)}"],
        ["原始节点 → 去重后", f"{stats.get('nodes_raw', 0)} → {stats.get('nodes_dedup', 0)}"],
        ["送入测试 → 探活通过 → 真测通过", f"{stats.get('nodes_tcp_ok', 0)} → {stats.get('nodes_probe_ok', 0)} → {stats.get('nodes_real_ok', 0)}"],
        ["国内可达 / 不可达 / 未知", f"{stats.get('nodes_china_reachable', 0)} / {stats.get('nodes_china_unreachable', 0)} / {stats.get('nodes_china_unknown', 0)}"],
        ["国内检查缓存命中", stats.get("nodes_china_cache_hits", 0)],
        ["**verified 输出**", stats.get("nodes_verified_output", 0)],
        ["**global 输出**", stats.get("nodes_global_output", 0)],
        ["all 全量池", stats.get("nodes_all_output", 0)],
        ["本轮耗时", f"{stats.get('duration_sec', '-')} 秒"],
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

    lines = [
        START_MARKER,
        "## 当前运行状态",
        "",
        _table(["指标", "数值"], overview_rows),
        "",
        f"> 输出保护：{guard_text}。完整报告见 `output/health_report.md`、`output/stats.json`。",
        "",
        "### Top 节点评分",
        "",
        _table(["评分", "协议", "延迟(ms)", "来源"], top_score_rows) if top_score_rows else "_暂无评分数据_",
        "",
        "### Top 来源质量",
        "",
        _table(["来源", "评分", "测试数", "建议"], source_rows) if source_rows else "_暂无来源评分数据_",
        "",
        END_MARKER,
    ]
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
