#!/usr/bin/env python3
"""AutoMergePublicNodes-Optimized 本地环境诊断工具。"""
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
        return True, out.strip().splitlines()[0] if out.strip() else "正常"
    except Exception as exc:
        return False, str(exc)


def build_doctor_report(sources: str, filter_rules: str, singbox: str, output_dir: str) -> Tuple[bool, str]:
    checks: List[Tuple[str, bool, str]] = []

    py_ok = sys.version_info >= (3, 11)
    checks.append(("Python >= 3.11", py_ok, platform.python_version()))

    for pkg in ("aiohttp", "aiohttp_socks", "yaml"):
        checks.append((f"Python package: {pkg}", _check_import(pkg), "已安装" if _check_import(pkg) else "缺失"))

    source_errors = validate_sources(sources)
    checks.append(("sources.yaml", not source_errors, "; ".join(source_errors[:3]) if source_errors else "正常"))

    filter_errors = validate_filter_rules(filter_rules)
    checks.append(("filter_rules.yaml", not filter_errors, "; ".join(filter_errors[:3]) if filter_errors else "正常"))

    sb_path = Path(singbox)
    if sb_path.exists():
        ok, msg = _run([str(sb_path), "version"])
        checks.append(("sing-box 可执行文件", ok, msg))
    else:
        checks.append(("sing-box 可执行文件", False, f"缺失：{singbox}"))

    out = Path(output_dir)
    checks.append(("output 目录", out.exists(), str(out)))
    for name in ("verified.urls", "global.urls", "all.urls", "stats.json", "health_report.json"):
        p = out / name
        checks.append((f"output/{name}", p.exists(), f"{p.stat().st_size} bytes" if p.exists() else "缺失"))

    git_ok, git_msg = _run(["git", "--version"])
    checks.append(("git", git_ok, git_msg))

    lines = ["# AutoNodes 环境诊断", "", f"工作目录：{Path.cwd()}", "", "| 检查项 | 状态 | 详情 |", "| --- | --- | --- |"]
    all_ok = True
    for name, ok, detail in checks:
        all_ok = all_ok and ok
        lines.append(f"| {name} | {'通过' if ok else '失败'} | {str(detail).replace('|', '/')} |")
    lines.append("")
    lines.append("总体状态：" + ("通过" if all_ok else "失败"))
    return all_ok, "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--sources", default="config/sources.yaml")
    parser.add_argument("--filter-rules", default="config/filter_rules.yaml")
    parser.add_argument("--singbox", default="./sing-box")
    parser.add_argument("--output-dir", default="output")
    parser.add_argument("--strict", action="store_true", help="任一检查失败时退出码为 1")
    args = parser.parse_args()

    ok, report = build_doctor_report(args.sources, args.filter_rules, args.singbox, args.output_dir)
    print(report)
    if args.strict and not ok:
        raise SystemExit(1)


if __name__ == "__main__":
    main()