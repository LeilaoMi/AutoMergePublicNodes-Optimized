#!/usr/bin/env python3
"""AutoMergePublicNodes-Optimized 本地环境诊断。"""
from __future__ import annotations

import argparse
import importlib.util
import platform
import subprocess
import sys
from pathlib import Path
from typing import List, Tuple

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tools.validate_config import validate_filter_rules, validate_sources


def _check_import(name: str) -> bool:
    return importlib.util.find_spec(name) is not None


def _run(cmd: List[str], timeout: int = 5) -> Tuple[bool, str]:
    try:
        out = subprocess.check_output(cmd, stderr=subprocess.STDOUT, text=True, timeout=timeout)
        return True, out.strip().splitlines()[0] if out.strip() else "ok"
    except Exception as exc:
        return False, str(exc)


def build_doctor_report(sources: str, filter_rules: str, singbox: str, output_dir: str) -> Tuple[bool, str]:
    checks: List[Tuple[str, bool, str]] = []

    py_ok = sys.version_info >= (3, 11)
    checks.append(("Python >= 3.11", py_ok, platform.python_version()))

    for pkg in ("aiohttp", "aiohttp_socks", "yaml"):
        checks.append((f"Python package: {pkg}", _check_import(pkg), "installed" if _check_import(pkg) else "missing"))

    source_errors = validate_sources(sources)
    checks.append(("sources.yaml", not source_errors, "; ".join(source_errors[:3]) if source_errors else "ok"))

    filter_errors = validate_filter_rules(filter_rules)
    checks.append(("filter_rules.yaml", not filter_errors, "; ".join(filter_errors[:3]) if filter_errors else "ok"))

    sb_path = Path(singbox)
    if sb_path.exists():
        ok, msg = _run([str(sb_path), "version"])
        checks.append(("sing-box binary", ok, msg))
    else:
        checks.append(("sing-box binary", False, f"missing: {singbox}"))

    out = Path(output_dir)
    checks.append(("output directory", out.exists(), str(out)))
    for name in ("verified.urls", "global.urls", "all.urls", "stats.json", "health_report.json"):
        p = out / name
        checks.append((f"output/{name}", p.exists(), f"{p.stat().st_size} bytes" if p.exists() else "missing"))

    git_ok, git_msg = _run(["git", "--version"])
    checks.append(("git", git_ok, git_msg))

    lines = ["# AutoNodes Doctor", "", f"Working directory: {Path.cwd()}", "", "| Check | Status | Detail |", "| --- | --- | --- |"]
    all_ok = True
    for name, ok, detail in checks:
        all_ok = all_ok and ok
        lines.append(f"| {name} | {'OK' if ok else 'FAIL'} | {str(detail).replace('|', '/')} |")
    lines.append("")
    lines.append("Overall: " + ("OK" if all_ok else "FAIL"))
    return all_ok, "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--sources", default="config/sources.yaml")
    parser.add_argument("--filter-rules", default="config/filter_rules.yaml")
    parser.add_argument("--singbox", default="./sing-box")
    parser.add_argument("--output-dir", default="output")
    parser.add_argument("--strict", action="store_true", help="exit 1 when any check fails")
    args = parser.parse_args()

    ok, report = build_doctor_report(args.sources, args.filter_rules, args.singbox, args.output_dir)
    print(report)
    if args.strict and not ok:
        raise SystemExit(1)


if __name__ == "__main__":
    main()