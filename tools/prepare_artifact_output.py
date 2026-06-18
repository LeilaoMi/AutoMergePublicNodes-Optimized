#!/usr/bin/env python3
"""整理最新输出文件，供单独的 artifact 分支发布使用。

本脚本仅本地操作：把生成的输出文件复制到一个干净目录，方便后续由 workflow 或维护者发布到 artifact/data 分支。不执行 git 命令、不修改 output/。
"""
from __future__ import annotations

import argparse
import shutil
from pathlib import Path

DEFAULT_PATTERNS = (
    "verified.*",
    "global.*",
    "all.txt",
    "all.urls",
    "all.converter.md",
    "stats.json",
    "health_report.json",
    "daily_report.md",
    "source_scores.md",
    "source_cleanup_suggestions.md",
    "source_cleanup_suggestions.json",
    "source_audit.json",
    "geo_cache.json",
)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", default="output")
    parser.add_argument("--dest-dir", default="artifact-output")
    args = parser.parse_args()

    source = Path(args.output_dir)
    dest = Path(args.dest_dir)
    if not source.exists():
        raise SystemExit(f"missing output dir: {source}")

    if dest.exists():
        shutil.rmtree(dest)
    dest.mkdir(parents=True)

    copied = []
    for pattern in DEFAULT_PATTERNS:
        for path in sorted(source.glob(pattern)):
            if path.is_file():
                shutil.copy2(path, dest / path.name)
                copied.append(path.name)

    manifest = dest / "MANIFEST.txt"
    manifest.write_text("\n".join(copied) + "\n", encoding="utf-8")
    print(f"copied {len(copied)} files to {dest}")
    print(f"manifest: {manifest}")


if __name__ == "__main__":
    main()
