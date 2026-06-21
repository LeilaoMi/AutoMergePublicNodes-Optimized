#!/usr/bin/env python3
"""根据 output/stats.json 和 output/source_audit.json 生成订阅源清理建议。

默认只读；可输出 Markdown 报告、机器可读 JSON，以及禁用源的 YAML 预览。
"""
from __future__ import annotations

import argparse
import json
import time
from pathlib import Path
from typing import Any, Dict, Iterable, List, Set

import yaml


def _load_json(path: Path, default: Any) -> Any:
    try:
        with path.open(encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return default


def _md_table(headers: Iterable[str], rows: Iterable[Iterable[Any]]) -> List[str]:
    headers = [str(h) for h in headers]
    lines = ["| " + " | ".join(headers) + " |", "| " + " | ".join("---" for _ in headers) + " |"]
    for row in rows:
        lines.append("| " + " | ".join(str(c) for c in row) + " |")
    return lines


def _audit_by_name(source_audit: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    rows = source_audit.get("sources", []) if isinstance(source_audit, dict) else []
    if not isinstance(rows, list):
        return {}
    return {str(r.get("name")): r for r in rows if isinstance(r, dict) and r.get("name")}


def build_cleanup_suggestions(
    stats: Dict[str, Any],
    source_audit: Dict[str, Any],
    min_tested: int = 5,
    disable_dead_threshold: int = 2,
) -> Dict[str, List[Dict[str, Any]]]:
    scores = stats.get("source_scores", {}) if isinstance(stats, dict) else {}
    if not isinstance(scores, dict):
        scores = {}
    audit = _audit_by_name(source_audit)

    disable: List[Dict[str, Any]] = []
    downweight: List[Dict[str, Any]] = []
    prefer: List[Dict[str, Any]] = []
    observe: List[Dict[str, Any]] = []

    names = set(scores) | set(audit)
    for name in sorted(names):
        score_data = scores.get(name, {}) if isinstance(scores.get(name, {}), dict) else {}
        audit_data = audit.get(name, {}) if isinstance(audit.get(name, {}), dict) else {}
        rec = str(score_data.get("recommendation") or "observe")
        tested = int(score_data.get("tested", 0) or 0)
        score = float(score_data.get("score", 0) or 0)
        consecutive_dead = int(score_data.get("consecutive_dead", audit_data.get("consecutive_dead", 0)) or 0)
        row = {
            "name": name,
            "url": audit_data.get("url", ""),
            "score": round(score, 3),
            "recommendation": rec,
            "tested": tested,
            "pass_rate": score_data.get("pass_rate"),
            "parsed_nodes": score_data.get("parsed_nodes", audit_data.get("nodes", 0)),
            "consecutive_dead": consecutive_dead,
            "reason": "",
        }
        if consecutive_dead >= disable_dead_threshold or rec == "disable-candidate":
            row["reason"] = f"连续死亡次数 >= {disable_dead_threshold}"
            disable.append(row)
        elif rec == "downweight" or (tested >= min_tested and score < 0.25):
            row["reason"] = f"已测数量 >= {min_tested} 且评分偏低"
            downweight.append(row)
        elif rec == "prefer":
            row["reason"] = "源评分较高"
            prefer.append(row)
        else:
            row["reason"] = "证据不足或评分中性"
            observe.append(row)

    disable.sort(key=lambda r: (-int(r.get("consecutive_dead", 0)), float(r.get("score", 0))))
    downweight.sort(key=lambda r: (float(r.get("score", 0)), -int(r.get("tested", 0))))
    prefer.sort(key=lambda r: (-float(r.get("score", 0)), -int(r.get("tested", 0))))
    observe.sort(key=lambda r: (str(r.get("name", ""))))
    return {"disable": disable, "downweight": downweight, "prefer": prefer, "observe": observe}


def _format_rows(rows: List[Dict[str, Any]]) -> List[List[Any]]:
    return [[
        r.get("name", "-"),
        r.get("score", "-"),
        r.get("tested", 0),
        r.get("pass_rate", "-"),
        r.get("parsed_nodes", 0),
        r.get("consecutive_dead", 0),
        r.get("reason", "-"),
        r.get("url", "-"),
    ] for r in rows]


def build_cleanup_payload(
    output_dir: str = "output",
    min_tested: int = 5,
    disable_dead_threshold: int = 2,
) -> Dict[str, Any]:
    out = Path(output_dir)
    stats = _load_json(out / "stats.json", {})
    audit = _load_json(out / "source_audit.json", {})
    suggestions = build_cleanup_suggestions(stats, audit, min_tested, disable_dead_threshold)
    return {
        "generated_at": time.strftime("%Y-%m-%d %H:%M:%S"),
        "min_tested": min_tested,
        "disable_dead_threshold": disable_dead_threshold,
        "summary": {key: len(value) for key, value in suggestions.items()},
        "suggestions": suggestions,
    }


def build_cleanup_report(
    output_dir: str = "output",
    min_tested: int = 5,
    disable_dead_threshold: int = 2,
) -> str:
    payload = build_cleanup_payload(output_dir, min_tested, disable_dead_threshold)
    suggestions = payload["suggestions"]

    lines: List[str] = [
        "# 订阅源清理建议",
        "",
        f"生成时间：{payload['generated_at']}",
        "",
        "本报告默认只读。修改 `config/sources.yaml` 前请人工复核。",
        "",
        "## 摘要",
        "",
    ]
    lines.extend(_md_table(["分类", "数量"], [[k, len(v)] for k, v in suggestions.items()]))

    headers = ["订阅源", "评分", "已测", "通过率", "解析数", "连续死亡", "原因", "URL"]
    for title, key in [
        ("建议禁用", "disable"),
        ("建议降权", "downweight"),
        ("建议优先保留", "prefer"),
        ("继续观察", "observe"),
    ]:
        rows = suggestions[key]
        lines += ["", f"## {title}", ""]
        if rows:
            lines.extend(_md_table(headers, _format_rows(rows)))
        else:
            lines.append("无记录。")
    return "\n".join(lines) + "\n"


def filter_names(names: Set[str], only: Set[str] | None = None, exclude: Set[str] | None = None) -> Set[str]:
    """根据白名单/黑名单过滤待处理订阅源名称。"""
    filtered = set(names)
    if only:
        filtered &= set(only)
    if exclude:
        filtered -= set(exclude)
    return filtered


def _parse_name_set(value: str) -> Set[str]:
    return {item.strip() for item in value.split(",") if item.strip()}


def _disable_sources_data(data: Dict[str, Any], disable_names: Set[str]) -> int:
    changed = 0
    for entry in data.get("sources", []):
        if isinstance(entry, dict) and entry.get("name") in disable_names and entry.get("enabled", True):
            entry["enabled"] = False
            changed += 1
    return changed


def build_disable_patch_preview(sources_path: str, disable_names: Set[str]) -> str:
    path = Path(sources_path)
    with path.open(encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    changed = _disable_sources_data(data, disable_names)
    return yaml.dump({"changed": changed, "preview": data}, allow_unicode=True, sort_keys=False)


def apply_disable_suggestions(sources_path: str, disable_names: Set[str]) -> int:
    """Apply disable suggestions with atomic write. Caller must perform confirmation checks."""
    if not disable_names:
        return 0
    path = Path(sources_path)
    with path.open(encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    changed = _disable_sources_data(data, disable_names)
    if changed:
        tmp = path.with_suffix(path.suffix + ".tmp")
        tmp.write_text(yaml.dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8")
        tmp.replace(path)
    return changed


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", default="output")
    parser.add_argument("--sources", default="config/sources.yaml")
    parser.add_argument("--output", default="output/source_cleanup_suggestions.md")
    parser.add_argument("--json-output", default="", help="可选：机器可读 JSON 输出路径")
    parser.add_argument("--patch-preview", default="", help="可选：禁用源 YAML 预览输出路径")
    parser.add_argument("--apply", action="store_true", help="将禁用建议应用到 sources.yaml；必须同时传 --confirm-disable")
    parser.add_argument("--confirm-disable", action="store_true", help="--apply 的安全确认开关")
    parser.add_argument("--only", default="", help="逗号分隔的允许处理源名称；为空表示允许全部禁用建议")
    parser.add_argument("--exclude", default="", help="逗号分隔的排除源名称")
    parser.add_argument("--min-tested", type=int, default=5)
    parser.add_argument("--disable-dead-threshold", type=int, default=2)
    args = parser.parse_args()

    if args.min_tested < 0:
        parser.error("--min-tested 必须 >= 0")
    if args.disable_dead_threshold < 1:
        parser.error("--disable-dead-threshold 必须 >= 1")
    if args.apply and not args.confirm_disable:
        parser.error("--apply 必须同时传 --confirm-disable")

    only_names = _parse_name_set(args.only)
    exclude_names = _parse_name_set(args.exclude)

    report = build_cleanup_report(args.output_dir, args.min_tested, args.disable_dead_threshold)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(report, encoding="utf-8")
    print(f"订阅源清理建议已写入：{output}")

    if args.json_output:
        payload = build_cleanup_payload(args.output_dir, args.min_tested, args.disable_dead_threshold)
        json_path = Path(args.json_output)
        json_path.parent.mkdir(parents=True, exist_ok=True)
        json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"订阅源清理 JSON 已写入：{json_path}")

    if args.patch_preview:
        stats = _load_json(Path(args.output_dir) / "stats.json", {})
        audit = _load_json(Path(args.output_dir) / "source_audit.json", {})
        suggestions = build_cleanup_suggestions(stats, audit, args.min_tested, args.disable_dead_threshold)
        disable_names = filter_names({str(r["name"]) for r in suggestions["disable"] if r.get("name")}, only_names, exclude_names)
        preview = build_disable_patch_preview(args.sources, disable_names)
        patch_path = Path(args.patch_preview)
        patch_path.parent.mkdir(parents=True, exist_ok=True)
        patch_path.write_text(preview, encoding="utf-8")
        print(f"禁用源预览已写入：{patch_path}")

    if args.apply:
        stats = _load_json(Path(args.output_dir) / "stats.json", {})
        audit = _load_json(Path(args.output_dir) / "source_audit.json", {})
        suggestions = build_cleanup_suggestions(stats, audit, args.min_tested, args.disable_dead_threshold)
        disable_names = filter_names({str(r["name"]) for r in suggestions["disable"] if r.get("name")}, only_names, exclude_names)
        changed = apply_disable_suggestions(args.sources, disable_names)
        print(f"已应用禁用建议到 {args.sources}；变更数量={changed}")


if __name__ == "__main__":
    main()
