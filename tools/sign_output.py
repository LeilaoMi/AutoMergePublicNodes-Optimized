#!/usr/bin/env python3
"""[P2-4] 输出文件签名占位工具。

实际生产签名（如 GPG/SSH）需要密钥管理，这里只暴露：
  - 签名 manifest 生成（SHA256 + 文件大小）
  - 验签脚本

不实际签名（避免在 CI 仓库里管理密钥），但 manifest 可被任何外部工具消费。
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from pathlib import Path
from typing import Any, Dict, List

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


HASHED_FILES = [
    "verified.txt", "verified.yaml", "verified.json", "verified.urls",
    "global.txt", "global.yaml", "global.json", "global.urls",
    "stats.json", "health_report.json",
]


def _sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(64 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def build_manifest(output_dir: str, only: List[str] | None = None) -> Dict[str, Any]:
    """生成 output 目录关键文件的 manifest。"""
    out_dir = Path(output_dir)
    files = only or HASHED_FILES
    files_present: List[Dict[str, Any]] = []
    for name in files:
        p = out_dir / name
        if not p.exists():
            continue
        files_present.append({
            "name": name,
            "size": p.stat().st_size,
            "sha256": _sha256_file(p),
        })
    # 也包括 by_region / by_capability 切片
    for sub in ("by_region", "by_capability"):
        d = out_dir / sub
        if not d.is_dir():
            continue
        for p in sorted(d.glob("*.txt")):
            files_present.append({
                "name": f"{sub}/{p.name}",
                "size": p.stat().st_size,
                "sha256": _sha256_file(p),
            })
    return {
        "schema": "autonodes.output.manifest.v1",
        "output_dir": output_dir,
        "files": files_present,
    }


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--output-dir", default="output")
    p.add_argument("--out", default="output/signature_manifest.json")
    p.add_argument("--only", nargs="*", help="只哈希指定文件名")
    args = p.parse_args()
    manifest = build_manifest(args.output_dir, only=args.only)
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"manifest: {len(manifest['files'])} files → {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
