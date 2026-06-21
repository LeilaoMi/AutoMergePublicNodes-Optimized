#!/usr/bin/env python3
"""根据 output/*.json 生成面向人工阅读的每日状态报告。

报告使用 Markdown，便于在 GitHub 或工作流产物中直接查看；只读取现有输出，不修改订阅。
"""
from __future__ import annotations

import argparse
import json
import time
from pathlib import Path
from typing import Any, Dict, Iterable, List


def _load_json(path: Path, default: Any) -> Any:
    try:
        with path.open(encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return default


def _count_urls(path: Path) -> int:
    try:
        return sum(1 for line in path.read_text(encoding="utf-8").splitlines() if line.strip())
    except FileNotFoundError:
        return 0


def _md_table(headers: Iterable[str], rows: Iterable[Iterable[Any]]) -> List[str]:
    headers = [str(h) for h in headers]
    lines = ["| " + " | ".join(headers) + " |", "| " + " | ".join("---" for _ in headers) + " |"]
    for row in rows:
        lines.append("| " + " | ".join(str(c) for c in row) + " |")
    return lines


def _top_counter_rows(mapping: Dict[str, Any], limit: int = 10) -> List[List[Any]]:
    rows = []
    for key, value in sorted(mapping.items(), key=lambda kv: kv[1] if isinstance(kv[1], (int, float)) else 0, reverse=True)[:limit]:
        rows.append([key, value])
    return rows


def _protocol_rows(stats: Dict[str, Any]) -> List[List[Any]]:
    rows = []
    pass_rate = stats.get("protocol_pass_rate", {})
    if isinstance(pass_rate, dict) and pass_rate:
        for proto, counts in sorted(pass_rate.items()):
            if not isinstance(counts, dict):
                continue
            passed = int(counts.get("pass", 0) or 0)
            failed = int(counts.get("fail", 0) or 0)
            total = passed + failed
            rate = f"{passed / total * 100:.1f}%" if total else "-"
            rows.append([proto, total, passed, failed, rate])
        return rows

    dist = stats.get("protocol_dist", {})
    if isinstance(dist, dict):
        return [[proto, count, "-", "-", "-"] for proto, count in sorted(dist.items())]
    return []


def _source_rows(source_audit: Dict[str, Any], limit: int = 10) -> List[List[Any]]:
    sources = source_audit.get("sources", []) if isinstance(source_audit, dict) else []
    if not isinstance(sources, list):
        return []
    rows = []
    for row in sorted([r for r in sources if isinstance(r, dict)], key=lambda r: int(r.get("nodes", 0) or 0), reverse=True)[:limit]:
        rows.append([
            row.get("name") or "-",
            row.get("nodes", 0),
            "yes" if row.get("ok") else "no",
            row.get("duration", "-"),
            row.get("consecutive_dead", 0),
        ])
    return rows


def build_daily_report(output_dir: str = "output") -> str:
    out = Path(output_dir)
    stats = _load_json(out / "stats.json", {})
    health = _load_json(out / "health_report.json", {})
    source_audit = _load_json(out / "source_audit.json", {})
    trend = _load_json(out / "trend_history.json", {})

    verified_count = stats.get("nodes_verified_output") or _count_urls(out / "verified.urls")
    global_count = stats.get("nodes_global_output") or _count_urls(out / "global.urls")
    all_count = stats.get("nodes_all_output") or _count_urls(out / "all.urls")

    lines: List[str] = [
        "# AutoNodes 每日报告",
        "",
        f"生成时间：{time.strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## 摘要",
        "",
    ]
    cleanup = health.get("source_cleanup", {}) if isinstance(health, dict) else {}
    lines.extend(_md_table(["指标", "值"], [
        ["健康状态", health.get("status", "unknown")],
        ["健康检查通过", health.get("ok", "unknown")],
        ["健康源数量", f"{source_audit.get('healthy', '-')}/{source_audit.get('sources_total', '-')}"] if isinstance(source_audit, dict) else ["健康源数量", "-"],
        ["清理建议：禁用/降权", f"{cleanup.get('disable_count', '-')}/{cleanup.get('downweight_count', '-')}"] if isinstance(cleanup, dict) else ["清理建议：禁用/降权", "-"],
        ["清理建议：优先/观察", f"{cleanup.get('prefer_count', '-')}/{cleanup.get('observe_count', '-')}"] if isinstance(cleanup, dict) else ["清理建议：优先/观察", "-"],
        ["原始节点数", stats.get("nodes_raw", "-")],
        ["去重后节点数", stats.get("nodes_dedup", "-")],
        ["TCP 可达数", stats.get("nodes_tcp_ok", "-")],
        ["真测通过数", stats.get("nodes_real_ok", "-")],
        ["verified 输出数", verified_count],
        ["global 输出数", global_count],
        ["all 输出数", all_count],
        ["all 输出模式", stats.get("all_output_mode", "-")],
    ]))

    lines += ["", "## 阶段耗时", ""]
    durations = stats.get("stage_durations", {})
    if isinstance(durations, dict) and durations:
        lines.extend(_md_table(["阶段", "秒"], sorted(durations.items())))
    else:
        lines.append("无阶段耗时数据。")

    lines += ["", "## 协议通过率", ""]
    proto_rows = _protocol_rows(stats)
    if proto_rows:
        lines.extend(_md_table(["协议", "已测", "通过", "失败", "通过率"], proto_rows))
    else:
        lines.append("无协议数据。")

    lines += ["", "## 主要真测错误", ""]
    errors = stats.get("real_test_error_structured") or stats.get("real_test_error_details") or stats.get("real_test_errors") or {}
    if isinstance(errors, list):
        rows = [[
            e.get("error") or ":".join(str(x) for x in (e.get("target", "-"), e.get("reason", "-")) if x),
            e.get("count", 0),
        ] for e in errors if isinstance(e, dict)]
    elif isinstance(errors, dict):
        rows = _top_counter_rows(errors)
    else:
        rows = []
    if rows:
        lines.extend(_md_table(["错误", "数量"], rows))
    else:
        lines.append("无真测错误数据。")

    tcp_errors = stats.get("tcp_errors", {})
    if isinstance(tcp_errors, dict) and tcp_errors:
        lines += ["", "## TCP 预筛选错误", ""]
        lines.extend(_md_table(["错误", "数量"], _top_counter_rows(tcp_errors)))

    rankings = health.get("rankings", {}) if isinstance(health, dict) else {}
    source_score_best = rankings.get("source_score_best", []) if isinstance(rankings, dict) else []
    source_score_worst = rankings.get("source_score_worst", []) if isinstance(rankings, dict) else []
    if source_score_best:
        lines += ["", "## 高评分订阅源", ""]
        lines.extend(_md_table(
            ["订阅源", "评分", "建议", "已测", "通过率", "解析数"],
            [[r.get("name"), r.get("score"), r.get("recommendation"), r.get("tested"), r.get("pass_rate"), r.get("parsed_nodes")] for r in source_score_best if isinstance(r, dict)],
        ))
    if source_score_worst:
        lines += ["", "## 需关注订阅源", ""]
        lines.extend(_md_table(
            ["订阅源", "评分", "建议", "已测", "通过率", "连续死亡", "解析数"],
            [[r.get("name"), r.get("score"), r.get("recommendation"), r.get("tested"), r.get("pass_rate"), r.get("consecutive_dead"), r.get("parsed_nodes")] for r in source_score_worst if isinstance(r, dict)],
        ))

    cleanup_disable = cleanup.get("disable_suggestions", []) if isinstance(cleanup, dict) else []
    cleanup_downweight = cleanup.get("downweight_suggestions", []) if isinstance(cleanup, dict) else []
    if cleanup_disable or cleanup_downweight:
        lines += ["", "## 订阅源清理建议", ""]
        rows = []
        for bucket, items in (("disable", cleanup_disable), ("downweight", cleanup_downweight)):
            if not isinstance(items, list):
                continue
            for r in items[:10]:
                if isinstance(r, dict):
                    rows.append([bucket, r.get("name"), r.get("score"), r.get("tested"), r.get("pass_rate"), r.get("consecutive_dead"), r.get("reason", "-")])
        lines.extend(_md_table(["分类", "订阅源", "评分", "已测", "通过率", "连续死亡", "原因"], rows))

    source_worst = rankings.get("source_worst", []) if isinstance(rankings, dict) else []
    if source_worst:
        lines += ["", "## 真测通过率较低的订阅源", ""]
        lines.extend(_md_table(
            ["订阅源", "通过率", "通过", "失败", "已测"],
            [[r.get("name"), r.get("pass_rate"), r.get("pass"), r.get("fail"), r.get("total")] for r in source_worst if isinstance(r, dict)],
        ))

    lines += ["", "## 解析节点数较高的订阅源", ""]
    source_rows = _source_rows(source_audit)
    if source_rows:
        lines.extend(_md_table(["订阅源", "节点数", "是否正常", "耗时", "连续死亡"], source_rows))
    else:
        lines.append("无源审计数据。")

    lines += ["", "## 趋势报警", ""]
    trend_alerts = trend.get("alerts", []) if isinstance(trend, dict) else []
    if trend_alerts:
        lines.extend(_md_table(
            ["类型", "信息"],
            [[a.get("type", "-"), a.get("message", "-")] for a in trend_alerts if isinstance(a, dict)],
        ))
    else:
        lines.append("无趋势报警。")

    lines += ["", "## 健康报警", ""]
    alerts = health.get("alerts", {}) if isinstance(health, dict) else {}
    low_pass = alerts.get("low_pass_protocols", []) if isinstance(alerts, dict) else []
    real_errors = alerts.get("real_test_errors", {}) if isinstance(alerts, dict) else {}
    if low_pass:
        lines.append("### 低通过率协议")
        lines.extend(_md_table(["协议", "通过率"], [[x.get("protocol"), x.get("pass_rate")] for x in low_pass if isinstance(x, dict)]))
        lines.append("")
    if real_errors:
        lines.append("### 真测错误报警")
        lines.extend(_md_table(["错误", "数量"], _top_counter_rows(real_errors)))
    if not low_pass and not real_errors:
        lines.append("无报警。")

    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", default="output")
    parser.add_argument("--output", default="output/daily_report.md")
    args = parser.parse_args()

    report = build_daily_report(args.output_dir)
    path = Path(args.output)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(report, encoding="utf-8")
    print(f"每日报告已写入：{path}")


if __name__ == "__main__":
    main()
