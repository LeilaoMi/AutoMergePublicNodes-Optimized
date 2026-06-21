#!/usr/bin/env python3
"""根据 output/stats.json 生成订阅源质量评分 Markdown 报告。"""
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
        "# 订阅源质量评分",
        "",
        f"生成时间：{time.strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## 摘要",
        "",
    ]
    lines.extend(_md_table(["指标", "值"], [
        ["已评分订阅源总数", total],
        ["建议优先", rec_counts.get("prefer", 0)],
        ["继续观察", rec_counts.get("observe", 0)],
        ["建议降权", rec_counts.get("downweight", 0)],
        ["建议禁用", rec_counts.get("disable-candidate", 0)],
    ]))

    sections = [
        ("建议优先", _score_rows(source_scores, "prefer", True, 30)),
        ("建议降权", _score_rows(source_scores, "downweight", False, 50)),
        ("建议禁用", _score_rows(source_scores, "disable-candidate", False, 50)),
        ("综合前 30", _score_rows(source_scores, None, True, 30)),
        ("综合后 30", _score_rows(source_scores, None, False, 30)),
    ]
    headers = ["订阅源", "评分", "建议", "已测", "通过", "失败", "通过率", "解析数", "连续死亡"]
    for title, rows in sections:
        lines += ["", f"## {title}", ""]
        if rows:
            lines.extend(_md_table(headers, _format_rows(rows)))
        else:
            lines.append("无记录。")

    lines += [
        "",
        "## 说明",
        "",
        "- `prefer`：高置信、高评分源，适合优先采样。",
        "- `observe`：历史不足或表现中性，继续观察。",
        "- `downweight`：已积累测试数据但评分偏低，建议保留但降低优先级。",
        "- `disable-candidate`：本轮或历史审计显示源疑似失效，禁用前请人工复核。",
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
    print(f"订阅源质量评分报告已写入：{path}")


if __name__ == "__main__":
    main()
