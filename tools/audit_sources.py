"""
订阅源审计工具
- 测试每个源的存活性（HTTP 状态、节点数）
- 估算"最近更新时间"：通过比较两次抓取的节点 fingerprint 集合
- 标记动态 URL vs 静态 URL
- 输出建议禁用的源
"""
from __future__ import annotations

import argparse
import asyncio
import json
import sys
import time
from pathlib import Path
from typing import Dict

# 让脚本能从仓库根运行
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import yaml

from core.fetcher import fetch_all, load_sources


def is_dynamic(url: str) -> bool:
    return "%" in url


def load_previous_audit(path: str) -> Dict[str, int]:
    """加载上次审计结果，返回 {name: consecutive_dead}"""
    try:
        with open(path, "r", encoding="utf-8") as f:
            prev = json.load(f)
        return {r["name"]: r.get("consecutive_dead", 0) for r in prev}
    except (FileNotFoundError, json.JSONDecodeError, KeyError):
        return {}




def disable_dead_sources(sources_path: str, dead_urls: set[str]) -> int:
    if not dead_urls:
        return 0
    path = Path(sources_path)
    with path.open(encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    changed = 0
    for entry in data.get("sources", []):
        if isinstance(entry, dict) and entry.get("url") in dead_urls and entry.get("enabled", True):
            entry["enabled"] = False
            changed += 1
    if changed:
        path.write_text(yaml.dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8")
    return changed

async def audit(sources_path: str, output: str, concurrency: int = 30, disable_dead_threshold: int = 0):
    sources = load_sources(sources_path)
    print(f"加载 {len(sources)} 个订阅源")
    print(f"  动态 URL: {sum(1 for s in sources if is_dynamic(s.url))}")
    print(f"  静态 URL: {sum(1 for s in sources if not is_dynamic(s.url))}")

    # 加载上次审计历史
    prev_dead = load_previous_audit(output)

    print(f"\n开始抓取...")
    start = time.time()
    results = await fetch_all(sources, concurrency=concurrency, timeout=15)
    elapsed = time.time() - start
    print(f"完成（{elapsed:.1f}s）")

    rows = []
    healthy, broken = 0, 0
    for r in results:
        is_dead = not r.success or len(r.nodes) == 0
        prev_count = prev_dead.get(r.source.name, 0)
        consecutive = (prev_count + 1) if is_dead else 0

        row = {
            "url": r.source.url,
            "name": r.source.name,
            "dynamic": is_dynamic(r.source.url),
            "ok": r.success,
            "nodes": len(r.nodes),
            "bytes": r.bytes_received,
            "duration": round(r.duration, 2),
            "error": r.error,
            "consecutive_dead": consecutive,
        }
        rows.append(row)
        if r.success and len(r.nodes) > 0:
            healthy += 1
        else:
            broken += 1

    # 按节点数降序
    rows.sort(key=lambda x: -x["nodes"])

    # 文本报告
    lines = [
        "=" * 80,
        f"订阅源审计报告 - {time.strftime('%Y-%m-%d %H:%M:%S')}",
        "=" * 80,
        f"总数: {len(rows)} | 健康: {healthy} | 失效: {broken}",
        "",
        f"{'状态':<6}{'节点':<7}{'类型':<5}{'耗时':<7}{'连续死源':<8}URL",
        "-" * 80,
    ]
    for r in rows:
        status = "✅" if r["ok"] and r["nodes"] > 0 else ("⚠️ " if r["ok"] else "❌")
        kind = "动态" if r["dynamic"] else "静态"
        dead_str = f"{r['consecutive_dead']}次" if r["consecutive_dead"] > 0 else "-"
        lines.append(f"{status:<6}{r['nodes']:<7}{kind:<5}{r['duration']}s   {dead_str:<8}{r['url'][:60]}")
        if r["error"]:
            lines.append(f"        错误: {r['error']}")

    lines.append("")
    lines.append("建议禁用的源（无节点或抓取失败）:")
    for r in rows:
        if not r["ok"] or r["nodes"] == 0:
            lines.append(f"  - {r['url']}")

    # 连续 2 次 0 节点的源（建议自动下线）
    auto_disable = [r for r in rows if r["consecutive_dead"] >= 2]
    if auto_disable:
        lines.append("")
        lines.append("⚠️ 连续 2+ 次 0 节点的源（建议自动下线）:")
        for r in auto_disable:
            lines.append(f"  - [{r['consecutive_dead']}次] {r['name']}: {r['url']}")

    disabled_count = 0
    if disable_dead_threshold > 0:
        dead_urls = {r["url"] for r in rows if r["consecutive_dead"] >= disable_dead_threshold}
        disabled_count = disable_dead_sources(sources_path, dead_urls)
        lines.append("")
        lines.append(f"自动禁用阈值: {disable_dead_threshold} 次；本次禁用: {disabled_count} 个源")

    report = "\n".join(lines)
    print(report)

    # JSON 输出
    payload = {
        "generated_at": time.strftime("%Y-%m-%d %H:%M:%S"),
        "sources_total": len(rows),
        "healthy": healthy,
        "broken": broken,
        "auto_disable_candidates": auto_disable,
        "disabled_count": disabled_count,
        "sources": rows,
    }
    with open(output, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print(f"\nJSON 已保存到: {output}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--sources", default="config/sources.yaml")
    parser.add_argument("--output", default="output/source_audit.json")
    parser.add_argument("--concurrency", type=int, default=30)
    parser.add_argument("--disable-dead-threshold", type=int, default=0,
                        help="连续死亡次数达到该阈值时自动将源 enabled=false；0 表示只报告不修改")
    args = parser.parse_args()
    
    # 参数验证
    if args.concurrency <= 0:
        parser.error("--concurrency must be positive")
    if args.disable_dead_threshold < 0:
        parser.error("--disable-dead-threshold must be >= 0")
    
    asyncio.run(audit(args.sources, args.output, args.concurrency, args.disable_dead_threshold))


if __name__ == "__main__":
    main()
