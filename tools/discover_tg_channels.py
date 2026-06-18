#!/usr/bin/env python3
"""扫描 Telegram 频道，找出适合加入 sources.yaml 的高产源。

对每个候选频道：
  1. 测试 https://t.me/s/<频道名> 网页预览是否可访问（无需 Telegram 登录）
  2. 提取页面里的 vmess:// / vless:// / trojan:// / ss:// / ssr:// 链接
  3. 用服务器 IP 做 GeoIP 标记，统计节点地区分布
  4. 输出 Markdown 报告 + 可直接粘贴的 sources.yaml 片段

用法：
  python tools/discover_tg_channels.py --channels @chan1,@chan2 --output output/tg_channel_scan.md
  python tools/discover_tg_channels.py --channels-file channels.txt --output output/tg_channel_scan.md

注意：本脚本只读公开网页预览，不登录、不调用 Telegram API、不需要 token。
"""
from __future__ import annotations

import argparse
import asyncio
import json
import os
import re
import socket
import sys
import time
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from urllib.parse import unquote

import aiohttp

# 节点链接正则（从 parser.py 同款简化版）
NODE_PATTERNS = [
    (re.compile(r"vmess://([A-Za-z0-9+/=]+)"), "vmess"),
    (re.compile(r"vless://[A-Za-z0-9?=&%@.:/_\-]+"), "vless"),
    (re.compile(r"trojan://[A-Za-z0-9?=&%@.:/_\-]+"), "trojan"),
    (re.compile(r"ss://[A-Za-z0-9+/=?&%@.:/_\-]+"), "ss"),
    (re.compile(r"ssr://[A-Za-z0-9+/=]+"), "ssr"),
    (re.compile(r"hysteria2?://[A-Za-z0-9?=&%@.:/_\-]+"), "hysteria2"),
    (re.compile(r"tuic://[A-Za-z0-9?=&%@.:/_\-]+"), "tuic"),
    (re.compile(r"hy2://[A-Za-z0-9?=&%@.:/_\-]+"), "hysteria2"),
]

# 从节点链接提取 server:port
SERVER_RE = re.compile(r"@([^:/?#]+):(\d+)")
# vmess base64 里的 add/port
VMESS_ADDR_RE = re.compile(r'"add"\s*:\s*"([^"]+)".*?"port"\s*:\s*"?(\d+)"?', re.DOTALL)


def extract_nodes(html: str) -> List[Tuple[str, str, str]]:
    """从 HTML 提取节点，返回 [(protocol, raw_link, server_ip)]"""
    nodes = []
    seen = set()
    for pat, proto in NODE_PATTERNS:
        for m in pat.finditer(html):
            raw = m.group(0)
            # 清理 HTML 实体
            raw = raw.replace("&amp;", "&")
            if raw in seen:
                continue
            seen.add(raw)
            # 提取 server
            server = ""
            if proto == "vmess":
                try:
                    import base64
                    b64 = raw.split("://", 1)[1]
                    b64 += "=" * (4 - len(b64) % 4) if len(b64) % 4 else ""
                    decoded = base64.b64decode(b64).decode("utf-8", errors="ignore")
                    sm = VMESS_ADDR_RE.search(decoded)
                    if sm:
                        server = sm.group(1)
                except Exception:
                    pass
            else:
                sm = SERVER_RE.search(raw)
                if sm:
                    server = sm.group(1)
            nodes.append((proto, raw, server))
    return nodes


def ip_to_country(ip: str) -> str:
    """简单 GeoIP：用 socket + 已知 IP 段粗判，精确判断留给主流水线"""
    if not ip:
        return "??"
    # 去掉端口
    ip = ip.split(":")[0]
    try:
        # 验证是 IP 还是域名
        socket.inet_aton(ip)
    except OSError:
        # 域名，跳过（主流水线的 GeoIP 会精确处理）
        return "domain"
    # 粗略判断几个大陆常用地区段（不是完整 GeoIP，只做扫描期排序参考）
    first = int(ip.split(".")[0])
    if first in (47, 43):
        return "CN?"  # 可能中国
    return "??"


async def scan_channel(session: aiohttp.ClientSession, channel: str, timeout: int = 15) -> Dict:
    """扫描单个频道，返回结果字典"""
    channel = channel.strip().lstrip("@")
    if not channel:
        return {"channel": channel, "status": "empty_name"}
    url = f"https://t.me/s/{channel}"
    result = {
        "channel": f"@{channel}",
        "url": url,
        "status": "unknown",
        "node_count": 0,
        "protocols": {},
        "servers_sample": [],
        "error": "",
        "fetched_at": time.strftime("%Y-%m-%d %H:%M:%S"),
    }
    try:
        async with session.get(url, timeout=aiohttp.ClientTimeout(total=timeout), ssl=False) as resp:
            result["http_status"] = resp.status
            if resp.status != 200:
                result["status"] = f"http_{resp.status}"
                result["error"] = f"HTTP {resp.status}"
                return result
            html = await resp.text(errors="ignore")
    except asyncio.TimeoutError:
        result["status"] = "timeout"
        result["error"] = "抓取超时"
        return result
    except Exception as e:
        result["status"] = "error"
        result["error"] = f"{type(e).__name__}: {str(e)[:100]}"
        return result

    # 检查是否是频道不存在/无预览
    if "If you have Telegram, you can view and join" in html and len(html) < 5000:
        result["status"] = "no_preview"
        result["error"] = "频道存在但无网页预览（可能被关闭）"
        return result

    nodes = extract_nodes(html)
    if not nodes:
        # 检查页面是否有消息内容但没节点
        if "tgme_widget_message_wrap" in html:
            result["status"] = "no_nodes"
            result["error"] = "频道有消息但近期无节点链接"
        else:
            result["status"] = "empty"
            result["error"] = "页面无消息内容"
        return result

    result["status"] = "ok"
    result["node_count"] = len(nodes)
    proto_counts: Dict[str, int] = {}
    servers = []
    for proto, raw, server in nodes:
        proto_counts[proto] = proto_counts.get(proto, 0) + 1
        if server:
            servers.append(server)
    result["protocols"] = proto_counts
    result["servers_sample"] = servers[:20]  # 只取样前 20 个
    return result


async def scan_all(channels: List[str], concurrency: int = 10, timeout: int = 15) -> List[Dict]:
    """并发扫描所有频道"""
    sem = asyncio.Semaphore(concurrency)
    async with aiohttp.ClientSession() as session:
        async def _wrap(ch: str) -> Dict:
            async with sem:
                return await scan_channel(session, ch, timeout)

        tasks = [asyncio.create_task(_wrap(ch)) for ch in channels]
        results = []
        for i, fut in enumerate(asyncio.as_completed(tasks), 1):
            r = await fut
            tag = r["channel"]
            if r["status"] == "ok":
                print(f"  [{i}/{len(channels)}] ✓ {tag}: {r['node_count']} 节点, 协议={r['protocols']}", flush=True)
            else:
                print(f"  [{i}/{len(channels)}] ✗ {tag}: {r['status']} ({r.get('error', '')})", flush=True)
            results.append(r)
    return results


def generate_report(results: List[Dict]) -> str:
    """生成 Markdown 报告"""
    ok = [r for r in results if r["status"] == "ok"]
    ok.sort(key=lambda r: r["node_count"], reverse=True)

    lines = [
        "# Telegram 频道扫描报告",
        "",
        f"> 扫描时间: {time.strftime('%Y-%m-%d %H:%M:%S')}",
        f"> 扫描频道数: {len(results)}",
        f"> 可用频道数: {len(ok)}",
        "",
        "## 可用频道（按节点数降序）",
        "",
        "| 频道 | 节点数 | 协议分布 | 状态 |",
        "|---|---:|---|---|",
    ]
    for r in ok:
        proto_str = ", ".join(f"{k}:{v}" for k, v in sorted(r["protocols"].items(), key=lambda x: -x[1]))
        lines.append(f"| {r['channel']} | {r['node_count']} | {proto_str} | ✅ |")

    lines.extend([
        "",
        "## 不可用频道",
        "",
        "| 频道 | 状态 | 原因 |",
        "|---|---|---|",
    ])
    for r in results:
        if r["status"] != "ok":
            lines.append(f"| {r['channel']} | {r['status']} | {r.get('error', '')} |")

    lines.extend([
        "",
        "## 推荐加入 sources.yaml 的频道",
        "",
        "以下频道网页预览可抓取且包含节点链接，可直接加入 `config/sources.yaml`：",
        "",
        "```yaml",
    ])
    for r in ok:
        safe_name = r["channel"].lstrip("@").lower()
        lines.append(f"- url: {r['url']}")
        lines.append(f"  name: tg-{safe_name}")
        lines.append(f"  kind: url")
        lines.append(f"  max_nodes: 500  # 扫描时 {r['node_count']} 节点")
        lines.append("")
    lines.append("```")
    lines.append("")
    lines.append("> 注意：TG 频道节点质量参差不齐，建议设 `max_nodes` 上限防止单源淹没。")
    lines.append("> 频道可能随时关闭网页预览或停更，建议定期重新扫描。")
    lines.append("")

    return "\n".join(lines)


def main():
    p = argparse.ArgumentParser(description="扫描 Telegram 频道，找出适合加入 sources.yaml 的高产源")
    p.add_argument("--channels", help="逗号分隔的频道列表，如 @chan1,@chan2")
    p.add_argument("--channels-file", help="频道列表文件，每行一个频道名")
    p.add_argument("--output", default="output/tg_channel_scan.md", help="输出 Markdown 报告路径")
    p.add_argument("--json-output", default="", help="可选 JSON 结果路径")
    p.add_argument("--concurrency", type=int, default=10, help="并发抓取数")
    p.add_argument("--timeout", type=int, default=15, help="单频道抓取超时秒数")
    args = p.parse_args()

    channels: List[str] = []
    if args.channels:
        channels = [c.strip() for c in args.channels.split(",") if c.strip()]
    if args.channels_file:
        with open(args.channels_file, encoding="utf-8") as f:
            channels = [line.strip() for line in f if line.strip() and not line.startswith("#")]
    if not channels:
        p.error("必须提供 --channels 或 --channels-file")

    print(f"扫描 {len(channels)} 个 Telegram 频道...")
    results = asyncio.run(scan_all(channels, concurrency=args.concurrency, timeout=args.timeout))

    report = generate_report(results)
    os.makedirs(os.path.dirname(args.output) or ".", exist_ok=True)
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(report)
    print(f"\n报告已生成: {args.output}")

    if args.json_output:
        with open(args.json_output, "w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        print(f"JSON 结果: {args.json_output}")

    # 汇总
    ok = [r for r in results if r["status"] == "ok"]
    print(f"\n汇总: {len(ok)}/{len(results)} 频道可用")
    for r in sorted(ok, key=lambda x: x["node_count"], reverse=True):
        print(f"  ✓ {r['channel']}: {r['node_count']} 节点")


if __name__ == "__main__":
    main()
