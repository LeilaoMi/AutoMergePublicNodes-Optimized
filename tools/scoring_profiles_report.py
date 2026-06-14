#!/usr/bin/env python3
"""生成评分模板对比 Markdown 报告。"""
from __future__ import annotations

import argparse
import glob
from pathlib import Path
from typing import Any, Dict, List

import yaml


WEIGHT_KEYS = ["latency", "jitter", "tcp", "protocol_history", "source_history"]
THRESHOLD_KEYS = [
    "excellent_latency_ms",
    "bad_latency_ms",
    "bad_jitter_ms",
    "excellent_tcp_latency_ms",
    "bad_tcp_latency_ms",
]
DEFAULT_KEYS = ["missing_tcp_score", "missing_history_score"]


def _load_yaml(path: Path) -> Dict[str, Any]:
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except Exception:
        return {}
    return data if isinstance(data, dict) else {}


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


def _number(value: Any, default: object = "-") -> object:
    try:
        number = float(value)
    except (TypeError, ValueError):
        return default
    return int(number) if number.is_integer() else round(number, 4)


def build_scoring_profiles_report(patterns: List[str]) -> str:
    paths: List[Path] = []
    seen = set()
    for pattern in patterns:
        matches = sorted(glob.glob(pattern)) if any(ch in pattern for ch in "*?[") else [pattern]
        for item in matches:
            if item not in seen:
                seen.add(item)
                paths.append(Path(item))

    rows = []
    threshold_rows = []
    default_rows = []
    for path in paths:
        data = _load_yaml(path)
        weights = data.get("weights") if isinstance(data.get("weights"), dict) else {}
        thresholds = data.get("thresholds") if isinstance(data.get("thresholds"), dict) else {}
        defaults = data.get("defaults") if isinstance(data.get("defaults"), dict) else {}
        weight_values = [_number(weights.get(key), 0) for key in WEIGHT_KEYS]
        total = round(sum(float(v) for v in weight_values), 4)
        rows.append([path.name, *weight_values, int(total) if float(total).is_integer() else total])
        threshold_rows.append([path.name, *[_number(thresholds.get(key)) for key in THRESHOLD_KEYS]])
        default_rows.append([path.name, *[_number(defaults.get(key)) for key in DEFAULT_KEYS]])

    return f"""# 评分模板对比报告

本报告对比所有评分模板 YAML 文件。真实代理测试仍然决定节点是否可用，评分模板仅排序可用节点。

## 权重

{_table(["模板", *WEIGHT_KEYS, "总和"], rows)}

## 阈值

{_table(["模板", *THRESHOLD_KEYS], threshold_rows)}

## 默认值

{_table(["模板", *DEFAULT_KEYS], default_rows)}

---

本文件由 `tools/scoring_profiles_report.py` 自动生成。
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--profiles", action="append", default=["config/scoring*.yaml"], help="评分模板路径或 glob 通配符，可重复传入。")
    parser.add_argument("--output", default="output/scoring_profiles.md")
    args = parser.parse_args()

    content = build_scoring_profiles_report(args.profiles)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(content, encoding="utf-8")
    print(str(output))


if __name__ == "__main__":
    main()
