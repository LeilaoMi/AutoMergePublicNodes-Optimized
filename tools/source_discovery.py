#!/usr/bin/env python3
"""从其他公开节点项目发现新订阅源。

扫描若干高 star 的免费节点仓库，提取它们的订阅 URL，列出尚未收录到 config/sources.yaml 的源。
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import List, Set
from urllib.request import urlopen, Request
from urllib.error import URLError

# Projects to scan for source discovery
# These are curated high-star projects that aggregate public node sources
DISCOVERY_TARGETS = [
    {
        "name": "mahdibland/V2RayAggregator",
        "url": "https://raw.githubusercontent.com/mahdibland/V2RayAggregator/master/sub/sub_merge.txt",
        "type": "subscription",
    },
    {
        "name": "Epodonios/v2ray-configs",
        "url": "https://raw.githubusercontent.com/Epodonios/v2ray-configs/main/All_Configs_Sub.txt",
        "type": "subscription",
    },
    {
        "name": "snakem982/proxypool",
        "url": "https://raw.githubusercontent.com/snakem982/proxypool/main/source/v2ray-2.txt",
        "type": "subscription",
    },
    {
        "name": "Pawdroid/Free-servers",
        "url": "https://raw.githubusercontent.com/Pawdroid/Free-servers/main/sub",
        "type": "subscription",
    },
    {
        "name": "Barabama/FreeNodes/nodes",
        "url": "https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/yudou66.txt",
        "type": "subscription",
    },
    {
        "name": "xiaoji235/airport-free",
        "url": "https://raw.githubusercontent.com/xiaoji235/airport-free/main/v2ray.txt",
        "type": "subscription",
    },
]


def load_existing_sources(sources_yaml_path: str) -> Set[str]:
    """Extract existing source URLs from config/sources.yaml."""
    path = Path(sources_yaml_path)
    if not path.exists():
        return set()
    content = path.read_text(encoding="utf-8")
    urls = set(re.findall(r'https?://[^\s\'"]+', content))
    return urls


def fetch_url(url: str, timeout: int = 15) -> str:
    """Fetch URL content with timeout."""
    req = Request(url, headers={"User-Agent": "autonodes-discovery/1.0"})
    with urlopen(req, timeout=timeout) as resp:
        return resp.read().decode("utf-8", errors="replace")


def discover_from_target(target: dict, timeout: int = 15) -> List[str]:
    """Try to fetch a target and return raw subscription content."""
    try:
        content = fetch_url(target["url"], timeout)
        return [line.strip() for line in content.splitlines() if line.strip()]
    except (URLError, OSError, TimeoutError) as e:
        print(f"  [SKIP] {target['name']}: {e}")
        return []


def run_discovery(
    sources_yaml: str = "config/sources.yaml",
    output_path: str = "output/source_discovery.json",
    timeout: int = 15,
) -> dict:
    """Run source discovery and write results."""
    existing = load_existing_sources(sources_yaml)
    print(f"Existing sources: {len(existing)} URLs")

    all_new_nodes: List[str] = []
    scanned = 0
    failed = 0

    for target in DISCOVERY_TARGETS:
        print(f"Scanning {target['name']}...")
        lines = discover_from_target(target, timeout)
        if lines:
            scanned += 1
            # Filter: only keep lines that look like proxy URLs
            node_lines = [
                line for line in lines
                if any(line.startswith(p) for p in
                       ("vmess://", "vless://", "trojan://", "ss://", "ssr://",
                        "hysteria2://", "hysteria://", "tuic://"))
            ]
            all_new_nodes.extend(node_lines)
            print(f"  Found {len(node_lines)} node configs")
        else:
            failed += 1

    # Count unique protocols
    proto_count: dict[str, int] = {}
    for line in all_new_nodes:
        proto = line.split("://")[0] if "://" in line else "unknown"
        proto_count[proto] = proto_count.get(proto, 0) + 1

    payload = {
        "scanned_projects": scanned,
        "failed_projects": failed,
        "total_discovered_nodes": len(all_new_nodes),
        "unique_nodes": len(set(all_new_nodes)),
        "protocol_distribution": proto_count,
        "note": "These nodes come from scanning other public aggregation projects. "
                "They are not auto-added to sources.yaml. Use as candidates for manual review.",
    }

    # Write output
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print(f"\nDiscovery complete: {payload['total_discovered_nodes']} nodes from {scanned} projects")
    print(f"Output: {output_path}")
    return payload


def main():
    p = argparse.ArgumentParser(description="Discover new subscription sources from other projects")
    p.add_argument("--sources", default="config/sources.yaml", help="Our sources.yaml for comparison")
    p.add_argument("--output", default="output/source_discovery.json", help="Output JSON path")
    p.add_argument("--timeout", type=int, default=15, help="HTTP timeout per source")
    args = p.parse_args()
    run_discovery(args.sources, args.output, args.timeout)


if __name__ == "__main__":
    main()
