#!/usr/bin/env python3
"""从 output/stats.json 生成 Markdown 源质量评分报告。"""
from __future__ import annotations

import argparse
import json
import time
from pathlib import Path
from typing import Any, Dict, Iterable, List


def _load_json(path: Path) -> Dict[str, Any]:
    try:
        with path.open(encoding="utf-8") as f:
            data = json.load(f)
        return data if isinstance(data, dict) else {}
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def _md_table(headers: Iterable[str], rows: Iterable[Iterable[Any]]) -> List[str]:
    headers = [str(h) for h in headers]
    lines = ["| " + " | ".join(headers) + " |", "| " + " | ".join("---" for _ in headers) + " |"]
    for row in rows:
        lines.append("| " + " | ".join(str(c) for c in row) + " |")
    return lines


def _score_rows(source_scores: Dict[str, Any], recommendation: str | None = None, reverse: bool = True, limit: int = 50) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    for name, data in source_scores.items():
        if not isinstance(data, dict):
            continue
        if recommendation and data.get("recommendation") != recommendation:
            continue
        row = dict(data)
        row["name"] = name
        rows.append(row)
    rows.sort(key=lambda r: (float(r.get("score", 0) or 0), int(r.get("tested", 0) or 0), int(r.get("parsed_nodes", 0) or 0)), reverse=reverse)
    return rows[:limit]


def _format_rows(rows: List[Dict[str, Any]]) -> List[List[Any]]:
    return [[
        r.get("name", "-"),
        r.get("score", "-"),
        r.get("recommendation", "-"),
        r.get("tested", 0),
        r.get("pass", 0),
        r.get("fail", 0),
        r.get("pass_rate", "-"),
        r.get("parsed_nodes", 0),
        r.get("consecutive_dead", 0),
    ] for r in rows]


def build_source_scores_report(output_dir: str = "output") -> str:
    out = Path(output_dir)
    stats = _load_json(out / "stats.json")
    source_scores = stats.get("source_scores", {})
    if not isinstance(source_scores, dict):
        source_scores = {}

    total = len(source_scores)
    rec_counts: Dict[str, int] = {}
    for data in source_scores.values():
        if isinstance(data, dict):
            rec = str(data.get("recommendation", "unknown"))
            rec_counts[rec] = rec_counts.get(rec, 0) + 1

    lines: List[str] = [
        "# Source Quality Scores",
        "",
        f"Generated at: {time.strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Summary",
        "",
    ]
    lines.extend(_md_table(["Metric", "Value"], [
        ["Total scored sources", total],
        ["Prefer", rec_counts.get("prefer", 0)],
        ["Observe", rec_counts.get("observe", 0)],
        ["Downweight", rec_counts.get("downweight", 0)],
        ["Disable candidates", rec_counts.get("disable-candidate", 0)],
    ]))

    sections = [
        ("Prefer", _score_rows(source_scores, "prefer", True, 30)),
        ("Downweight", _score_rows(source_scores, "downweight", False, 50)),
        ("Disable Candidates", _score_rows(source_scores, "disable-candidate", False, 50)),
        ("Top 30 Overall", _score_rows(source_scores, None, True, 30)),
        ("Bottom 30 Overall", _score_rows(source_scores, None, False, 30)),
    ]
    headers = ["Source", "Score", "Recommendation", "Tested", "Pass", "Fail", "Pass Rate", "Parsed", "Dead"]
    for title, rows in sections:
        lines += ["", f"## {title}", ""]
        if rows:
            lines.extend(_md_table(headers, _format_rows(rows)))
        else:
            lines.append("No rows.")

    lines += [
        "",
        "## Notes",
        "",
        "- `prefer`: high-confidence/high-score source, good candidate for priority sampling.",
        "- `observe`: insufficient history or neutral behavior.",
        "- `downweight`: tested enough and scored poorly; keep but reduce priority.",
        "- `disable-candidate`: source looked dead in this run or historical audit context; review before disabling.",
    ]
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", default="output")
    parser.add_argument("--output", default="output/source_scores.md")
    args = parser.parse_args()

    report = build_source_scores_report(args.output_dir)
    path = Path(args.output)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(report, encoding="utf-8")
    print(f"source scores report written to {path}")


if __name__ == "__main__":
    main()
