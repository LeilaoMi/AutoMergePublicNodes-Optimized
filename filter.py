#!/usr/bin/env python3
# filter.py - TCP连通性测试，过滤无效节点并同步所有格式文件

import yaml
import socket
import threading
import sys
import base64
from typing import List, Dict, Any

# ========== 配置 ==========
TIMEOUT   = 10    # TCP 连接超时（秒）
MAX_WORKERS = 150 # 最大并发线程数
MAX_NODES = 150  # 最多保留节点数
# ==========================

def test_tcp(host: str, port: int) -> bool:
    try:
        sock = socket.create_connection((str(host), int(port)), timeout=TIMEOUT)
        sock.close()
        return True
    except:
        return False

def read_yaml_with_comment(path: str):
    with open(path, encoding='utf-8') as f:
        content = f.read()
    lines = content.splitlines(keepends=True)
    comment = lines[0] if lines and lines[0].startswith('#') else ''
    return comment, yaml.full_load(content)

def filter_groups(proxy_groups, valid_names):
    for group in proxy_groups:
        if isinstance(group.get('proxies'), list) and len(group['proxies']) > 5:
            filtered = [p for p in group['proxies'] if p in valid_names]
            if filtered:
                group['proxies'] = filtered
    return proxy_groups

# ========== 读取节点 ==========
print("读取节点列表...")
comment_meta, meta = read_yaml_with_comment('list.meta.yml')
all_proxies: List[Dict[str, Any]] = meta.get('proxies', [])
print(f"共 {len(all_proxies)} 个节点，开始并发测试连通性...")

# ========== 并发 TCP 测试 ==========
results: Dict[int, bool] = {}
lock = threading.Lock()
active = [0]

def worker(idx: int, proxy: Dict[str, Any]):
    host = proxy.get('server', '')
    port = proxy.get('port', 0)
    ok = test_tcp(host, port)
    with lock:
        results[idx] = ok
        active[0] -= 1
        done = len(results)
        if done % 200 == 0 or done == len(all_proxies):
            print(f"  进度: {done}/{len(all_proxies)}，"
                  f"有效: {sum(results.values())}")

threads = []
for i, proxy in enumerate(all_proxies):
    # 控制并发上限
    while active[0] >= MAX_WORKERS:
        pass
    t = threading.Thread(target=worker, args=(i, proxy), daemon=True)
    threads.append(t)
    with lock:
        active[0] += 1
    t.start()

for t in threads:
    t.join(timeout=TIMEOUT + 3)

# ========== 筛选 ==========
valid_proxies = [all_proxies[i] for i in range(len(all_proxies))
                 if results.get(i, False)]
print(f"\n有效节点: {len(valid_proxies)} / {len(all_proxies)}")

if len(valid_proxies) > MAX_NODES:
    valid_proxies = valid_proxies[:MAX_NODES]
    print(f"限制为最多 {MAX_NODES} 个节点")

valid_names = {p['name'] for p in valid_proxies}

# ========== 更新 list.meta.yml ==========
meta['proxies'] = valid_proxies
meta['proxy-groups'] = filter_groups(meta.get('proxy-groups', []), valid_names)

with open('list.meta.yml', 'w', encoding='utf-8') as f:
    f.write(comment_meta)
    f.write(yaml.dump(meta, allow_unicode=True).replace('!!str ', ''))
print("✓ list.meta.yml 已更新")

# ========== 更新 list.yml ==========
try:
    comment_yml, clash = read_yaml_with_comment('list.yml')
    clash['proxies'] = [p for p in clash.get('proxies', [])
                        if p['name'] in valid_names]
    clash['proxy-groups'] = filter_groups(
        clash.get('proxy-groups', []), valid_names)

    with open('list.yml', 'w', encoding='utf-8') as f:
        f.write(comment_yml)
        f.write(yaml.dump(clash, allow_unicode=True).replace('!!str ', ''))
    print("✓ list.yml 已更新")
except Exception as e:
    print(f"✗ list.yml 更新失败: {e}")

# ========== 更新 list.txt（V2Ray 格式）==========
try:
    sys.path.insert(0, '.')
    from fetch import Node, b64encodes  # 复用 fetch.py 里的 Node 类

    txt = ''
    for p in valid_proxies:
        try:
            n = Node(p)
            if n.supports_ray():
                txt += n.url + '\n'
        except:
            pass

    with open('list_raw.txt', 'w', encoding='utf-8') as f:
        f.write(txt)
    with open('list.txt', 'w', encoding='utf-8') as f:
        f.write(b64encodes(txt))
    print(f"✓ list.txt 已更新，共 {txt.count(chr(10))} 条")
except Exception as e:
    print(f"✗ list.txt 更新失败: {e}")

print("\n过滤完成！")

