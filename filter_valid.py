#!/usr/bin/env python3
"""
过滤有效节点
从 list.yml 中只保留 valid_nodes.txt 中的节点
"""
import yaml
import sys

def main():
    try:
        with open('valid_nodes.txt') as f:
            valid_names = set(line.strip() for line in f if line.strip())
    except FileNotFoundError:
        print("valid_nodes.txt 不存在")
        sys.exit(1)
    
    try:
        with open('list.yml') as f:
            data = yaml.safe_load(f)
    except FileNotFoundError:
        print("list.yml 不存在")
        sys.exit(1)
    
    if not data or 'proxies' not in data:
        print("无节点数据")
        sys.exit(0)
    
    original = len(data['proxies'])
    data['proxies'] = [p for p in data['proxies'] if p.get('name', '') in valid_names]
    
    with open('list.yml', 'w') as f:
        f.write(yaml.dump(data, allow_unicode=True, default_flow_style=False))
    
    print(f"过滤完成: {original} -> {len(data['proxies'])} 节点")

if __name__ == "__main__":
    main()
