#!/usr/bin/env python3
"""从 output/stats.json 生成 GitHub Actions 任务摘要。"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from typing import Any, Dict, List


def table(headers: List[str], rows: List[List[object]]) -> str:
    if not rows:
        return "_No data_"
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(str(x) for x in row) + " |")
    return "\n".join(lines)


def pct(num: object, den: object) -> str:
    try:
        n = int(num or 0)
        d = int(den or 0)
    except (TypeError, ValueError):
        return "-"
    if d <= 0:
        return "-"
    return f"{n / d * 100:.1f}%"


def top_sources(stats: Dict[str, Any], limit: int = 8) -> List[List[object]]:
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
            data.get("pass_rate", "-"),
            data.get("tested", 0),
            data.get("recommendation", "-"),
        ])
    return rows


def build_summary(stats: Dict[str, Any], repo: str = "", branch: str = "main") -> str:
    overview = [
        ["Version", stats.get("version", "-")],
        ["Updated", stats.get("timestamp", "-")],
        ["Duration", f"{stats.get('duration_sec', 0)}s"],
        ["Sources", f"{stats.get('sources_healthy', 0)}/{stats.get('sources_total', 0)}"],
        ["Raw nodes", stats.get("nodes_raw", 0)],
        ["Dedup nodes", stats.get("nodes_dedup", 0)],
        ["TCP OK", stats.get("nodes_tcp_ok", 0)],
        ["Real OK", stats.get("nodes_real_ok", 0)],
        ["Real pass rate", pct(stats.get("nodes_real_ok"), stats.get("nodes_tcp_ok"))],
        ["Verified output", stats.get("nodes_verified_output", 0)],
        ["Global output", stats.get("nodes_global_output", 0)],
        ["All output", stats.get("nodes_all_output", 0)],
    ]

    stage_rows = [[k, v] for k, v in (stats.get("stage_durations") or {}).items()]

    scoring = stats.get("scoring") or {}
    weights = scoring.get("weights") if isinstance(scoring, dict) else {}
    weight_rows = []
    if isinstance(weights, dict):
        weight_rows = [[key, value] for key, value in weights.items()]

    score_rows = []
    for item in (stats.get("top_scores") or [])[:10]:
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
        ])

    error_rows = [
        [
            item.get("target", "-"),
            item.get("reason", "-"),
            item.get("status") or item.get("value") or "-",
            item.get("count", 0),
        ]
        for item in (stats.get("real_test_error_structured") or [])[:10]
        if isinstance(item, dict)
    ]

    guard = stats.get("output_guard") or {}
    guard_rows = []
    if isinstance(guard, dict):
        for name, data in guard.items():
            if isinstance(data, dict):
                guard_rows.append([
                    name,
                    data.get("preserved", False),
                    data.get("previous_count", 0),
                    data.get("proposed_count", 0),
                ])

    links = ""
    if repo:
        output_base = f"https://cdn.jsdelivr.net/gh/{repo}@{branch}/output"
        repo_base = f"https://github.com/{repo}/blob/{branch}"
        links = (
            f"- [verified.txt]({output_base}/verified.txt)\n"
            f"- [verified.yaml]({output_base}/verified.yaml)\n"
            f"- [verified.json]({output_base}/verified.json)\n"
            f"- [health_report.md]({output_base}/health_report.md)\n"
            f"- [scoring_profiles.md]({output_base}/scoring_profiles.md)\n"
            f"- [stats.json]({output_base}/stats.json)\n"
            f"- [release notes]({repo_base}/docs/releases/README.md)\n"
        )

    return f"""# AutoNodes Run Summary

## Overview

{table(["Metric", "Value"], overview)}

## Stage Durations

{table(["Stage", "Seconds"], stage_rows)}

## Scoring Weights

{table(["Factor", "Weight"], weight_rows)}

## Top Node Scores

{table(["Score", "Protocol", "Latency(ms)", "Jitter(ms)", "Latency pts", "Jitter pts", "TCP pts", "Protocol hist pts", "Source hist pts", "Source"], score_rows)}

## Top Source Quality

{table(["Source", "Score", "Pass rate", "Tested", "Recommendation"], top_sources(stats))}

## Real-Test Error Top

{table(["Target", "Reason", "Status/Value", "Count"], error_rows)}

## Output Guard

{table(["Prefix", "Preserved", "Previous", "Proposed"], guard_rows)}

## Output Links

{links or '_Repository context unavailable._'}
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--stats", default="output/stats.json")
    parser.add_argument("--output", default=os.environ.get("GITHUB_STEP_SUMMARY", ""))
    parser.add_argument("--repo", default=os.environ.get("GITHUB_REPOSITORY", ""))
    parser.add_argument("--branch", default=os.environ.get("GITHUB_REF_NAME", "main"))
    args = parser.parse_args()

    stats_path = Path(args.stats)
    if not stats_path.exists():
        raise SystemExit(f"stats file not found: {stats_path}")

    stats = json.loads(stats_path.read_text(encoding="utf-8"))
    summary = build_summary(stats, repo=args.repo, branch=args.branch)

    if args.output:
        out = Path(args.output)
        with out.open("a", encoding="utf-8") as f:
            f.write(summary)
            f.write("\n")
    else:
        print(summary)


if __name__ == "__main__":
    main()
