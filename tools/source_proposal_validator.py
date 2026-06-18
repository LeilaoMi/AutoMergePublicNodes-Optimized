#!/usr/bin/env python3
"""[P2-2] 源贡献自动 PR 验证器。

接收候选订阅源 URL，输出：
  - dry-run 解析样例
  - 预估贡献节点数
  - 风险评分
  - PR body（可直接复制到 GitHub）

不直接发起 PR（PR 由 GitHub Action 发起），本工具只产出验证报告 + 标准化 body。
"""
from __future__ import annotations

import argparse
import asyncio
import base64
import json
import sys
import tempfile
from pathlib import Path
from typing import Any, Dict, List, Optional

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


# 已知恶意 / 风险 IP 段前缀
KNOWN_BAD_PREFIXES = [
    "0.0.0.0",  # 兜底占位
]

# 已知常见扫描器 ASN
KNOWN_BAD_ASN = []


async def _fetch_url(url: str, timeout: float = 15.0) -> Optional[str]:
    """最小化的 URL fetcher。"""
    try:
        import aiohttp
        timeout_obj = aiohttp.ClientTimeout(total=timeout)
        async with aiohttp.ClientSession(timeout=timeout_obj) as session:
            async with session.get(url, allow_redirects=True) as resp:
                if resp.status != 200:
                    return None
                return await resp.text()
    except Exception as exc:
        print(f"      fetch failed: {exc}")
        return None


def _heuristic_risk(text: str) -> Dict[str, Any]:
    """简单的风险评分（不替代专业审计）。"""
    flags: List[str] = []
    if not text:
        return {"risk_level": "unknown", "flags": ["empty_response"]}
    if len(text) > 10 * 1024 * 1024:
        flags.append("oversized_payload")
    if "<script" in text.lower() or "javascript:" in text.lower():
        flags.append("possible_xss")
    if "bitcoin" in text.lower() or "monero" in text.lower() or "wallet" in text.lower():
        flags.append("crypto_keywords")
    if "password" in text.lower() and "leak" in text.lower():
        flags.append("leaked_credentials_keywords")
    level = "low"
    if len(flags) >= 2:
        level = "high"
    elif flags:
        level = "medium"
    return {"risk_level": level, "flags": flags}


async def validate_source(url: str, sample_size: int = 5) -> Dict[str, Any]:
    """抓取 + 解析 + 风险评估。"""
    from core.parser import parse_content

    text = await _fetch_url(url)
    if text is None:
        return {"url": url, "ok": False, "error": "fetch_failed"}
    nodes = parse_content(text)
    risk = _heuristic_risk(text)
    sample = []
    for n in nodes[:sample_size]:
        sample.append({
            "type": n.type,
            "server": n.server,
            "port": n.server_port,
            "tag": n.tag,
        })
    return {
        "url": url,
        "ok": True,
        "node_count": len(nodes),
        "protocol_dist": _protocol_dist(nodes),
        "risk": risk,
        "sample": sample,
    }


def _protocol_dist(nodes: List[Any]) -> Dict[str, int]:
    d: Dict[str, int] = {}
    for n in nodes:
        d[n.type] = d.get(n.type, 0) + 1
    return dict(sorted(d.items(), key=lambda x: -x[1]))


def build_pr_body(report: Dict[str, Any], author: str = "@contributor") -> str:
    """生成 PR body。"""
    if not report.get("ok"):
        return f"❌ 自动验证失败：`{report.get('url')}`\n\n错误：{report.get('error', 'unknown')}"
    risk = report.get("risk", {})
    lines = [
        f"## 📥 候选订阅源贡献：{report['url']}",
        "",
        f"- 解析节点数: **{report.get('node_count', 0)}**",
        f"- 风险等级: **{risk.get('risk_level', 'unknown')}**",
    ]
    if risk.get("flags"):
        lines.append(f"- 风险标记: {', '.join(risk['flags'])}")
    pd = report.get("protocol_dist", {})
    if pd:
        lines.append("- 协议分布: " + ", ".join(f"{k}={v}" for k, v in pd.items()))
    if report.get("sample"):
        lines.append("")
        lines.append("### 样例节点")
        lines.append("```")
        for s in report["sample"]:
            lines.append(f"[{s['type']}] {s['server']}:{s['port']} - {s['tag']}")
        lines.append("```")
    lines.append("")
    lines.append("---")
    lines.append(f"由 {author} 通过 `tools/source_proposal_validator.py` 自动生成。请人工 review 后再合并。")
    return "\n".join(lines)


async def validate_many(urls: List[str], output: Optional[str] = None) -> List[Dict[str, Any]]:
    reports = []
    for url in urls:
        print(f"   - {url}")
        r = await validate_source(url)
        reports.append(r)
    if output:
        Path(output).write_text(json.dumps(reports, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"   报告已写入 {output}")
    return reports


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("urls", nargs="+", help="候选订阅源 URL，空格分隔")
    p.add_argument("--output", "-o", help="报告 JSON 输出路径")
    p.add_argument("--pr-body", action="store_true", help="额外输出 PR body 文本")
    args = p.parse_args()
    reports = asyncio.run(validate_many(args.urls, output=args.output))
    if args.pr_body:
        for r in reports:
            print("---")
            print(build_pr_body(r))
    # 简单的退出码：有 ok=False 的视为失败
    return 0 if all(r.get("ok") for r in reports) else 1


if __name__ == "__main__":
    sys.exit(main())
