#!/usr/bin/env python3
"""Prepare latest output files for publishing on a separate artifact branch.

This script is intentionally local-only: it copies generated output files into a
clean directory that a workflow or maintainer can publish to an artifact/data
branch later. It does not run git commands and does not mutate output/.
"""
from __future__ import annotations

import argparse
import shutil
from pathlib import Path

DEFAULT_PATTERNS = (
    "verified.*",
    "all.txt",
    "all.urls",
    "all.converter.md",
    "stats.json",
    "health_report.json",
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
