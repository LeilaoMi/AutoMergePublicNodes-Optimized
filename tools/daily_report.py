#!/usr/bin/env python3
"""从 output/*.json 生成人类可读的每日状态报告。

输出 Markdown 格式，可直接在 GitHub 查看，或纳入 workflow 产物。脚本只读输出文件、不修改订阅，最终写入 daily_report.md。
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
        "# AutoNodes Daily Report",
        "",
        f"Generated at: {time.strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Summary",
        "",
    ]
    cleanup = health.get("source_cleanup", {}) if isinstance(health, dict) else {}
    lines.extend(_md_table(["Metric", "Value"], [
        ["Health status", health.get("status", "unknown")],
        ["Health ok", health.get("ok", "unknown")],
        ["Sources healthy", f"{source_audit.get('healthy', '-')}/{source_audit.get('sources_total', '-')}"] if isinstance(source_audit, dict) else ["Sources healthy", "-"],
        ["Cleanup disable/downweight", f"{cleanup.get('disable_count', '-')}/{cleanup.get('downweight_count', '-')}"] if isinstance(cleanup, dict) else ["Cleanup disable/downweight", "-"],
        ["Cleanup prefer/observe", f"{cleanup.get('prefer_count', '-')}/{cleanup.get('observe_count', '-')}"] if isinstance(cleanup, dict) else ["Cleanup prefer/observe", "-"],
        ["Raw nodes", stats.get("nodes_raw", "-")],
        ["Dedup nodes", stats.get("nodes_dedup", "-")],
        ["TCP ok", stats.get("nodes_tcp_ok", "-")],
        ["Real ok", stats.get("nodes_real_ok", "-")],
        ["Verified output", verified_count],
        ["Global output", global_count],
        ["All output", all_count],
        ["All output mode", stats.get("all_output_mode", "-")],
    ]))

    lines += ["", "## Stage Durations", ""]
    durations = stats.get("stage_durations", {})
    if isinstance(durations, dict) and durations:
        lines.extend(_md_table(["Stage", "Seconds"], sorted(durations.items())))
    else:
        lines.append("No stage duration data.")

    lines += ["", "## Protocol Pass Rate", ""]
    proto_rows = _protocol_rows(stats)
    if proto_rows:
        lines.extend(_md_table(["Protocol", "Tested", "Passed", "Failed", "Pass Rate"], proto_rows))
    else:
        lines.append("No protocol data.")

    lines += ["", "## Main Real-Test Errors", ""]
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
        lines.extend(_md_table(["Error", "Count"], rows))
    else:
        lines.append("No real-test error data.")

    tcp_errors = stats.get("tcp_errors", {})
    if isinstance(tcp_errors, dict) and tcp_errors:
        lines += ["", "## TCP Precheck Errors", ""]
        lines.extend(_md_table(["Error", "Count"], _top_counter_rows(tcp_errors)))

    rankings = health.get("rankings", {}) if isinstance(health, dict) else {}
    source_score_best = rankings.get("source_score_best", []) if isinstance(rankings, dict) else []
    source_score_worst = rankings.get("source_score_worst", []) if isinstance(rankings, dict) else []
    if source_score_best:
        lines += ["", "## Best Sources By Score", ""]
        lines.extend(_md_table(
            ["Source", "Score", "Recommendation", "Tested", "Pass Rate", "Parsed"],
            [[r.get("name"), r.get("score"), r.get("recommendation"), r.get("tested"), r.get("pass_rate"), r.get("parsed_nodes")] for r in source_score_best if isinstance(r, dict)],
        ))
    if source_score_worst:
        lines += ["", "## Sources Needing Attention", ""]
        lines.extend(_md_table(
            ["Source", "Score", "Recommendation", "Tested", "Pass Rate", "Dead", "Parsed"],
            [[r.get("name"), r.get("score"), r.get("recommendation"), r.get("tested"), r.get("pass_rate"), r.get("consecutive_dead"), r.get("parsed_nodes")] for r in source_score_worst if isinstance(r, dict)],
        ))

    cleanup_disable = cleanup.get("disable_suggestions", []) if isinstance(cleanup, dict) else []
    cleanup_downweight = cleanup.get("downweight_suggestions", []) if isinstance(cleanup, dict) else []
    if cleanup_disable or cleanup_downweight:
        lines += ["", "## Source Cleanup Suggestions", ""]
        rows = []
        for bucket, items in (("disable", cleanup_disable), ("downweight", cleanup_downweight)):
            if not isinstance(items, list):
                continue
            for r in items[:10]:
                if isinstance(r, dict):
                    rows.append([bucket, r.get("name"), r.get("score"), r.get("tested"), r.get("pass_rate"), r.get("consecutive_dead"), r.get("reason", "-")])
        lines.extend(_md_table(["Bucket", "Source", "Score", "Tested", "Pass Rate", "Dead", "Reason"], rows))

    source_worst = rankings.get("source_worst", []) if isinstance(rankings, dict) else []
    if source_worst:
        lines += ["", "## Worst Sources By Real-Test Pass Rate", ""]
        lines.extend(_md_table(
            ["Source", "Pass Rate", "Passed", "Failed", "Tested"],
            [[r.get("name"), r.get("pass_rate"), r.get("pass"), r.get("fail"), r.get("total")] for r in source_worst if isinstance(r, dict)],
        ))

    lines += ["", "## Top Sources By Parsed Nodes", ""]
    source_rows = _source_rows(source_audit)
    if source_rows:
        lines.extend(_md_table(["Source", "Nodes", "OK", "Duration", "Consecutive Dead"], source_rows))
    else:
        lines.append("No source audit data.")

    lines += ["", "## Trend Alerts", ""]
    trend_alerts = trend.get("alerts", []) if isinstance(trend, dict) else []
    if trend_alerts:
        lines.extend(_md_table(
            ["Type", "Message"],
            [[a.get("type", "-"), a.get("message", "-")] for a in trend_alerts if isinstance(a, dict)],
        ))
    else:
        lines.append("No trend alerts.")

    lines += ["", "## Health Alerts", ""]
    alerts = health.get("alerts", {}) if isinstance(health, dict) else {}
    low_pass = alerts.get("low_pass_protocols", []) if isinstance(alerts, dict) else []
    real_errors = alerts.get("real_test_errors", {}) if isinstance(alerts, dict) else {}
    if low_pass:
        lines.append("### Low-pass protocols")
        lines.extend(_md_table(["Protocol", "Pass Rate"], [[x.get("protocol"), x.get("pass_rate")] for x in low_pass if isinstance(x, dict)]))
        lines.append("")
    if real_errors:
        lines.append("### Real-test error alerts")
        lines.extend(_md_table(["Error", "Count"], _top_counter_rows(real_errors)))
    if not low_pass and not real_errors:
        lines.append("No alerts.")

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
    print(f"daily report written to {path}")


if __name__ == "__main__":
    main()
