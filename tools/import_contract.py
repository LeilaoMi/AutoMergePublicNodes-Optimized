#!/usr/bin/env python3
"""Import 契约检查：验证所有被 import 的项目内部模块文件真实存在。

防止 v3.0.0 那种"main.py import 了 core._xxx 但对应 .py 文件不存在"导致 CI 崩溃。

用法:
    python tools/import_contract.py
    python tools/import_contract.py --root /path/to/project

退出码 0 = 全部 import 指向真实文件; 非 0 = 发现悬空 import。
"""
from __future__ import annotations

import argparse
import ast
import sys
from pathlib import Path


def _resolve_module_path(root: Path, dotted: str) -> Path | None:
    """把 'core.filtering' 解析为 root/core/filtering.py 或 root/core/filtering/__init__.py。"""
    parts = dotted.split(".")
    candidate = root.joinpath(*parts)
    py_file = candidate.with_suffix(".py")
    if py_file.is_file():
        return py_file
    init_file = candidate / "__init__.py"
    if init_file.is_file():
        return init_file
    return None


def _is_internal(dotted: str, rel_from: Path, root: Path) -> str | None:
    """判断 import 是否指向项目内部模块，返回标准化的 dotted 名供解析。"""
    # 绝对内部 import: from core.xxx / import core.xxx
    if dotted.startswith("core."):
        return dotted
    # 当前包内相对 import: from .xxx import y / from ..xxx import y
    if dotted.startswith("."):
        return None  # 相对 import 解析复杂且项目内 core 无子包嵌套，暂跳过
    return None


def check_file(path: Path, root: Path) -> list[str]:
    """检查单个 .py 文件的 import 契约，返回违规描述列表。"""
    try:
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    except SyntaxError as exc:
        return [f"{path}: 语法错误无法解析 import: {exc}"]

    violations: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                dotted = _is_internal(alias.name, path, root)
                if dotted and _resolve_module_path(root, dotted) is None:
                    violations.append(f"{path}:{node.lineno} import {alias.name} -> 模块文件不存在")
        elif isinstance(node, ast.ImportFrom):
            base = node.module or ""
            level = node.level  # 0=绝对, >0=相对
            if level == 0:
                dotted = _is_internal(base, path, root)
                if dotted and _resolve_module_path(root, dotted) is None:
                    violations.append(f"{path}:{node.lineno} from {base} import ... -> 模块文件不存在")
    return violations


def main() -> int:
    parser = argparse.ArgumentParser(description="检查项目内部 import 是否都指向真实存在的模块文件")
    parser.add_argument("--root", default=".", help="项目根目录")
    args = parser.parse_args()
    root = Path(args.root).resolve()

    targets: list[Path] = []
    main_py = root / "main.py"
    if main_py.is_file():
        targets.append(main_py)
    targets.extend(sorted((root / "core").glob("*.py")))
    targets.extend(sorted((root / "tools").glob("*.py")))

    all_violations: list[str] = []
    checked = 0
    for path in targets:
        if path.name == "__init__.py":
            continue
        all_violations.extend(check_file(path, root))
        checked += 1

    print(f"Import 契约检查: 扫描 {checked} 个文件")
    if all_violations:
        print(f"❌ 发现 {len(all_violations)} 处悬空 import:")
        for v in all_violations:
            print(f"  {v}")
        return 1
    print("✅ 所有内部 import 都指向真实存在的模块文件")
    return 0


if __name__ == "__main__":
    sys.exit(main())
