#!/usr/bin/env python3
"""本地二次筛选工具。

用途：GitHub Actions 的真测环境通常在海外机房，不能代表用户本地网络。
本脚本读取 output/all.urls、output/global.urls 或任意订阅文件，在本地做解析、TCP 预筛选，
并输出 local_verified.*，供用户再导入客户端或继续用 sing-box/第三方工具复测。

示例：
  python tools/local_filter.py --input output/global.urls --output-prefix local_verified --top-n 100
  python tools/local_filter.py --input output/all.txt --output-dir output --tcp-timeout 2 --concurrency 300
"""
from __future__ import annotations

import argparse
import asyncio
import base64
import sys
from pathlib import Path
from typing import List, Tuple

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from core.generator import write_outputs
from core.parser import Node, parse_content
from main import dedupe, quality_prefilter, load_filter_rules, tcp_check_batch


def read_subscription(path: str) -> str:
    text = Path(path).read_text(encoding="utf-8", errors="replace")
    stripped = text.strip()
    # .txt 通常是 base64 订阅；如果能解出包含协议 URL 的正文，就优先使用解码结果。
    if stripped and "//" not in stripped[:200]:
        try:
            padded = stripped + "=" * ((4 - len(stripped) % 4) % 4)
            decoded = base64.b64decode(padded).decode("utf-8", errors="replace")
            if "://" in decoded:
                return decoded
        except Exception:
            pass
    return text


async def run(args: argparse.Namespace) -> int:
    content = read_subscription(args.input)
    nodes = parse_content(content)
    print(f"[1/4] 解析输入: {len(nodes)} 个节点")

    nodes = dedupe(nodes)
    print(f"[2/4] 去重: {len(nodes)} 个节点")

    if args.quality_filter:
        rules = load_filter_rules(args.filter_rules)
        before = len(nodes)
        nodes, hits = quality_prefilter(nodes, max_per_server=args.max_per_server, rules=rules)
        hit_summary = ", ".join(f"{k}={v}" for k, v in sorted(hits.items(), key=lambda x: -x[1])[:8])
        print(f"[3/4] 质量过滤: {before} -> {len(nodes)}" + (f"；规则命中: {hit_summary}" if hit_summary else ""))
    else:
        print("[3/4] 跳过质量过滤")

    if args.tcp_check:
        print(f"[4/4] 本地 TCP 预筛选（并发 {args.concurrency}, 超时 {args.tcp_timeout}s）...")
        tcp_results: List[Tuple[Node, float]] = await tcp_check_batch(nodes, args.concurrency, args.tcp_timeout)
        tcp_results.sort(key=lambda item: item[1])
        selected = [n for n, _ in tcp_results[: args.top_n if args.top_n > 0 else None]]
        print(f"      TCP 可达: {len(tcp_results)}；输出: {len(selected)}")
    else:
        selected = nodes[: args.top_n if args.top_n > 0 else None]
        print(f"[4/4] 未 TCP 筛选；输出: {len(selected)}")

    Path(args.output_dir).mkdir(parents=True, exist_ok=True)
    count = write_outputs(
        selected,
        args.output_dir,
        prefix=args.output_prefix,
        repo_path=args.repo,
        branch=args.branch,
        mode=args.output_mode,
    )
    print(f"✅ 已生成 {count} 个节点: {args.output_dir}/{args.output_prefix}.txt / .urls" + (" / .yaml / .json" if args.output_mode == "full" else ""))
    return 0


def main() -> None:
    p = argparse.ArgumentParser(description="本地二次筛选公共节点订阅")
    p.add_argument("--input", default="output/global.urls", help="输入订阅文件，支持 .urls 或 base64 .txt")
    p.add_argument("--output-dir", default="output")
    p.add_argument("--output-prefix", default="local_verified")
    p.add_argument("--top-n", type=int, default=100, help="输出上限；0=不限")
    p.add_argument("--tcp-check", action=argparse.BooleanOptionalAction, default=True)
    p.add_argument("--concurrency", type=int, default=200)
    p.add_argument("--tcp-timeout", type=float, default=3.0)
    p.add_argument("--quality-filter", action=argparse.BooleanOptionalAction, default=True)
    p.add_argument("--filter-rules", default="config/filter_rules.yaml")
    p.add_argument("--max-per-server", type=int, default=0)
    p.add_argument("--output-mode", choices=("full", "light"), default="full")
    p.add_argument("--repo", default="LeilaoMi/AutoMergePublicNodes-Optimized")
    p.add_argument("--branch", default="main")
    args = p.parse_args()

    if args.top_n < 0:
        p.error("--top-n 必须 >= 0")
    if args.concurrency <= 0:
        p.error("--concurrency 必须 > 0")
    if args.tcp_timeout <= 0:
        p.error("--tcp-timeout 必须 > 0")

    raise SystemExit(asyncio.run(run(args)))


if __name__ == "__main__":
    main()
