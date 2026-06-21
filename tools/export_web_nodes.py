#!/usr/bin/env python3
"""
导出节点元数据至 web/nodes.json，供 GitHub Pages 前端网关使用。
用法: python tools/export_web_nodes.py --input output/all.yaml --output web/nodes.json
"""
import sys
import json
import argparse
import yaml
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

def export_nodes(input_path: str, output_path: str):
    if not Path(input_path).exists():
        print(f"Error: {input_path} not found.")
        return

    with open(input_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    if not data or "proxies" not in data:
        print("No proxies found in input file.")
        return

    web_nodes = []
    for p in data["proxies"]:
        # 提取前端所需的极简元数据
        node = {
            "name": p.get("name", "Unknown"),
            "protocol": p.get("type", "unknown"),
            "region": p.get("name", "").split("-")[0] if "-" in p.get("name", "") else "UNKNOWN", # 简单启发式提取地区
            "clash_yaml": yaml.dump(p, allow_unicode=True, default_flow_style=False).strip()
        }
        # 如果是通用订阅格式，可能需要不同的解析，这里假设输入是 Clash YAML
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
