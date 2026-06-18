#!/usr/bin/env python3
"""根据 output/stats.json 与 output/source_audit.json 提出订阅源清理建议。

默认只读：产出 Markdown 报告，并可选地生成 YAML 补丁预览，展示人工复核后会被禁用的源。
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
            row["reason"] = f"consecutive_dead >= {disable_dead_threshold}"
            disable.append(row)
        elif rec == "downweight" or (tested >= min_tested and score < 0.25):
            row["reason"] = f"low score with tested >= {min_tested}"
            downweight.append(row)
        elif rec == "prefer":
            row["reason"] = "high source score"
            prefer.append(row)
        else:
            row["reason"] = "insufficient evidence or neutral score"
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
        "# Source Cleanup Suggestions",
        "",
        f"Generated at: {payload['generated_at']}",
        "",
        "This report is read-only guidance. Review entries before editing `config/sources.yaml`.",
        "",
        "## Summary",
        "",
    ]
    lines.extend(_md_table(["Bucket", "Count"], [[k, len(v)] for k, v in suggestions.items()]))

    headers = ["Source", "Score", "Tested", "Pass Rate", "Parsed", "Dead", "Reason", "URL"]
    for title, key in [
        ("Disable Candidates", "disable"),
        ("Downweight Candidates", "downweight"),
        ("Prefer / Keep Priority", "prefer"),
        ("Observe", "observe"),
    ]:
        rows = suggestions[key]
        lines += ["", f"## {title}", ""]
        if rows:
            lines.extend(_md_table(headers, _format_rows(rows)))
        else:
            lines.append("No rows.")
    return "\n".join(lines) + "\n"


def filter_names(names: Set[str], only: Set[str] | None = None, exclude: Set[str] | None = None) -> Set[str]:
    """Apply optional allow/deny filters to cleanup source names."""
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
    parser.add_argument("--json-output", default="", help="optional machine-readable JSON output path")
    parser.add_argument("--patch-preview", default="", help="optional path for YAML disable preview")
    parser.add_argument("--apply", action="store_true", help="apply disable suggestions to sources.yaml; requires --confirm-disable")
    parser.add_argument("--confirm-disable", action="store_true", help="required safety confirmation for --apply")
    parser.add_argument("--only", default="", help="comma-separated source names allowed for patch/apply; empty means all disable suggestions")
    parser.add_argument("--exclude", default="", help="comma-separated source names to exclude from patch/apply")
    parser.add_argument("--min-tested", type=int, default=5)
    parser.add_argument("--disable-dead-threshold", type=int, default=2)
    args = parser.parse_args()

    if args.min_tested < 0:
        parser.error("--min-tested must be >= 0")
    if args.disable_dead_threshold < 1:
        parser.error("--disable-dead-threshold must be >= 1")
    if args.apply and not args.confirm_disable:
        parser.error("--apply requires --confirm-disable")

    only_names = _parse_name_set(args.only)
    exclude_names = _parse_name_set(args.exclude)

    report = build_cleanup_report(args.output_dir, args.min_tested, args.disable_dead_threshold)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(report, encoding="utf-8")
    print(f"source cleanup suggestions written to {output}")

    if args.json_output:
        payload = build_cleanup_payload(args.output_dir, args.min_tested, args.disable_dead_threshold)
        json_path = Path(args.json_output)
        json_path.parent.mkdir(parents=True, exist_ok=True)
        json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"source cleanup JSON written to {json_path}")

    if args.patch_preview:
        stats = _load_json(Path(args.output_dir) / "stats.json", {})
        audit = _load_json(Path(args.output_dir) / "source_audit.json", {})
        suggestions = build_cleanup_suggestions(stats, audit, args.min_tested, args.disable_dead_threshold)
        disable_names = filter_names({str(r["name"]) for r in suggestions["disable"] if r.get("name")}, only_names, exclude_names)
        preview = build_disable_patch_preview(args.sources, disable_names)
        patch_path = Path(args.patch_preview)
        patch_path.parent.mkdir(parents=True, exist_ok=True)
        patch_path.write_text(preview, encoding="utf-8")
        print(f"disable patch preview written to {patch_path}")

    if args.apply:
        stats = _load_json(Path(args.output_dir) / "stats.json", {})
        audit = _load_json(Path(args.output_dir) / "source_audit.json", {})
        suggestions = build_cleanup_suggestions(stats, audit, args.min_tested, args.disable_dead_threshold)
        disable_names = filter_names({str(r["name"]) for r in suggestions["disable"] if r.get("name")}, only_names, exclude_names)
        changed = apply_disable_suggestions(args.sources, disable_names)
        print(f"applied disable suggestions to {args.sources}; changed={changed}")


if __name__ == "__main__":
    main()
