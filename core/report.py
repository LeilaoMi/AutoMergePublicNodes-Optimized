"""生成 Markdown 健康报告。"""
from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List


def _table(headers: List[str], rows: List[List[object]]) -> str:
    if not rows:
        return "_暂无数据_"

    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(str(x) for x in row) + " |")
    return "\n".join(lines)


def write_health_report(output_dir: str, stats: Dict[str, Any]) -> str:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    report_path = output_path / "health_report.md"

    overview_rows = [
        ["版本", stats.get("version", "-")],
        ["更新时间", stats.get("timestamp", "-")],
        ["运行耗时", f"{stats.get('duration_sec', 0)}s"],
        ["订阅源总数", stats.get("sources_total", 0)],
        ["健康订阅源", stats.get("sources_healthy", 0)],
        ["原始节点", stats.get("nodes_raw", 0)],
        ["去重后节点", stats.get("nodes_dedup", 0)],
        ["TCP 可达", stats.get("nodes_tcp_ok", 0)],
        ["真实可用", stats.get("nodes_real_ok", 0)],
        ["Verified 输出", stats.get("nodes_verified_output", 0)],
        ["Global 输出", stats.get("nodes_global_output", 0)],
        ["All 输出", stats.get("nodes_all_output", 0)],
    ]

    protocol_rows = [
        [name, count]
        for name, count in sorted(
            (stats.get("protocol_dist") or {}).items(),
            key=lambda x: -int(x[1]),
        )
    ]

    source_score_rows = []
    source_scores = stats.get("source_scores") or {}
    if isinstance(source_scores, dict):
        for name, data in sorted(
            source_scores.items(),
            key=lambda x: -float(x[1].get("score", 0)) if isinstance(x[1], dict) else 0,
        )[:15]:
            if not isinstance(data, dict):
                continue
            source_score_rows.append([
                name,
                data.get("score", "-"),
                data.get("pass_rate", "-"),
                data.get("tested", 0),
                data.get("parsed_nodes", 0),
                data.get("recommendation", "-"),
            ])

    error_rows = [
        [
            item.get("target", "-"),
            item.get("reason", "-"),
            item.get("status") or item.get("value") or "-",
            item.get("count", 0),
        ]
        for item in (stats.get("real_test_error_structured") or [])[:15]
        if isinstance(item, dict)
    ]

    scoring = stats.get("scoring") or {}
    weights = scoring.get("weights") if isinstance(scoring, dict) else {}
    scoring_rows = []
    if isinstance(weights, dict):
        scoring_rows = [[key, value] for key, value in weights.items()]

    score_rows = []
    for item in (stats.get("top_scores") or [])[:20]:
        if not isinstance(item, dict):
            continue
        breakdown = item.get("score_breakdown") or {}

        def _points(name: str) -> object:
            value = breakdown.get(name) if isinstance(breakdown, dict) else None
            return value.get("points", "-") if isinstance(value, dict) else "-"

        score_rows.append([
            item.get("score", "-"),
            item.get("type", "-"),
            item.get("latency_ms", "-"),
            item.get("jitter_ms", "-"),
            _points("latency"),
            _points("jitter"),
            _points("tcp"),
            _points("protocol_history"),
            _points("source_history"),
            item.get("source", "-"),
            item.get("server", "-"),
        ])

    guard_rows = []
    output_guard = stats.get("output_guard") or {}
    if isinstance(output_guard, dict):
        for name, data in output_guard.items():
            if isinstance(data, dict):
                guard_rows.append([
                    name,
                    data.get("preserved", False),
                    data.get("previous_count", 0),
                    data.get("proposed_count", 0),
                    data.get("min_retain_ratio", "-"),
                ])

    content = f"""# AutoNodes 健康报告

## 总览

{_table(["指标", "数值"], overview_rows)}

## 阶段耗时

{_table(["阶段", "秒"], [[k, v] for k, v in (stats.get("stage_durations") or {}).items()])}

## 协议分布

{_table(["协议", "数量"], protocol_rows)}

## 评分权重

{_table(["因子", "权重"], scoring_rows)}

## Top 节点评分

{_table(["评分", "协议", "延迟(ms)", "抖动(ms)", "延迟分", "抖动分", "TCP分", "协议历史分", "来源历史分", "来源", "服务器"], score_rows)}

## 来源质量排行

{_table(["来源", "评分", "通过率", "测试数", "解析节点", "建议"], source_score_rows)}

## 真实测试失败原因

{_table(["目标", "原因", "状态/值", "数量"], error_rows)}

## 输出保护

{_table(["前缀", "是否保留旧输出", "上一轮数量", "本轮建议数量", "保护比例"], guard_rows)}

---

此文件由 `core.report.write_health_report()` 自动生成。
"""

    report_path.write_text(content, encoding="utf-8")
    return str(report_path)
