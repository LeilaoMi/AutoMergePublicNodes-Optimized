#!/usr/bin/env python3
"""
导出节点元数据至 web/nodes.json，供 GitHub Pages 前端网关使用。
纯标准库 + PyYAML 实现，不依赖 core 内部函数，确保 CI 绝对稳定。
"""
import sys
import json
import argparse
import yaml
from pathlib import Path

def export_nodes(input_path: str, output_path: str):
    if not Path(input_path).exists():
        print(f"Warning: {input_path} not found. Skipping export.")
        return

    with open(input_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    if not data or "proxies" not in data:
        print("No proxies found in input file.")
        return

    web_nodes = []
    for p in data["proxies"]:
        node = {
            "name": p.get("name", "Unknown"),
            "protocol": p.get("type", "unknown"),
            "region": p.get("name", "").split("-")[0] if "-" in p.get("name", "") else "UNKNOWN",
            "clash_yaml": yaml.dump(p, allow_unicode=True, default_flow_style=False).strip()
        }
        web_nodes.append(node)

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(web_nodes, f, ensure_ascii=False, indent=2)
    
    print(f"Exported {len(web_nodes)} nodes to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="output/all.yaml")
    parser.add_argument("--output", default="web/nodes.json")
    args = parser.parse_args()
    export_nodes(args.input, args.output)
