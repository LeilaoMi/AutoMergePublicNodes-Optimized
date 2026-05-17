#!/usr/bin/env python3
"""
生成输出文件
生成 Clash YAML 和 V2Ray Base64 订阅
"""
import yaml
import base64
import sys

def main():
    try:
        with open('list.yml') as f:
            data = yaml.safe_load(f)
    except FileNotFoundError:
        print("list.yml 不存在")
        sys.exit(1)
    
    if not data or 'proxies' not in data:
        print("无节点数据")
        sys.exit(0)
    
    proxies = data['proxies']
    
    # 复制 YAML
    with open('output/clash.yml', 'w') as f:
        f.write(yaml.dump(data, allow_unicode=True, default_flow_style=False))
    
    # 生成 V2Ray 订阅 (Base64)
    urls = []
    for p in proxies:
        name = p.get('name', 'node')
        server = p.get('server', '')
        port = p.get('port', '')
        ptype = p.get('type', '')
        urls.append(f'{ptype}://{server}:{port}#{name}')
    
    with open('output/list.txt', 'w') as f:
        f.write(base64.b64encode('\n'.join(urls).encode()).decode())
    
    print(f"生成 {len(proxies)} 个节点")

if __name__ == "__main__":
    main()
