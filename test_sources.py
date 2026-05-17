#!/usr/bin/env python3
"""
订阅源测试脚本
测试所有订阅源的有效性和更新状态
"""
import asyncio
import aiohttp
import re
import time
from datetime import datetime, timedelta
from typing import List, Dict, Tuple, Optional
from urllib.parse import urlparse
import sys

# 测试结果
class SourceStatus:
    def __init__(self, url: str):
        self.url = url
        self.status = "unknown"
        self.nodes = 0
        self.last_update = None
        self.response_time = 0
        self.error = None
        self.protocols = set()
        self.skip = False  # 注释或特殊标记
        
    def __repr__(self):
        if self.skip:
            return f"[SKIP] {self.url}"
        status_emoji = "✅" if self.status == "ok" else "❌" if self.status == "fail" else "⚠️"
        return f"{status_emoji} {self.url} | {self.nodes} nodes | {self.response_time:.2f}s | {self.status}"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

TIMEOUT = aiohttp.ClientTimeout(total=30, connect=10)

# 协议正则
PROTOCOL_PATTERNS = {
    "vmess": re.compile(r"vmess://", re.IGNORECASE),
    "vless": re.compile(r"vless://", re.IGNORECASE),
    "trojan": re.compile(r"trojan://", re.IGNORECASE),
    "ss": re.compile(r"ss://", re.IGNORECASE),
    "ssr": re.compile(r"ssr://", re.IGNORECASE),
    "hysteria": re.compile(r"hysteria(2)?://", re.IGNORECASE),
    "hy2": re.compile(r"hy2://", re.IGNORECASE),
    "tuic": re.compile(r"tuic://", re.IGNORECASE),
    "wireguard": re.compile(r"wireguard://", re.IGNORECASE),
    "socks": re.compile(r"socks[45]://", re.IGNORECASE),
}

def parse_sources_list(filepath: str) -> List[Tuple[str, str]]:
    """解析 sources.list 文件，返回 (类型, URL) 列表"""
    sources = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if line.upper() == "EOF":
                break
            
            # 提取 URL 和参数
            url = line
            source_type = "normal"
            
            if line.startswith("!"):
                source_type = "china_only"
                url = line[1:].split("#")[0].strip()
            elif line.startswith("+"):
                source_type = "dynamic"
                url = line[1:].split("#")[0].strip()
            elif line.startswith("*"):
                source_type = "list"
                url = line[1:].split("#")[0].strip()
            
            # 提取实际 URL
            url = url.split("#")[0].strip()
            if url.startswith("http"):
                sources.append((source_type, url, line))
    
    return sources

def count_protocols(content: str) -> Dict[str, int]:
    """统计内容中的协议类型"""
    counts = {}
    for proto, pattern in PROTOCOL_PATTERNS.items():
        matches = pattern.findall(content)
        if matches:
            counts[proto] = len(matches)
    return counts

async def test_source(session: aiohttp.ClientSession, source_type: str, url: str) -> SourceStatus:
    """测试单个订阅源"""
    status = SourceStatus(url)
    
    # 处理动态日期 URL
    if source_type == "dynamic":
        now = datetime.now()
        url = now.strftime(url)
        status.url = url
    
    try:
        start = time.time()
        async with session.get(url, headers=HEADERS) as resp:
            status.response_time = time.time() - start
            
            if resp.status != 200:
                status.status = "fail"
                status.error = f"HTTP {resp.status}"
                return status
            
            content = await resp.text()
            
            # 检测内容类型
            if "proxies:" in content or "- type:" in content:
                # Clash YAML 格式
                lines = content.split("\n")
                for line in lines:
                    if "server:" in line:
                        status.nodes += 1
            else:
                # Base64 或其他格式
                import base64
                try:
                    decoded = base64.b64decode(content).decode("utf-8")
                    status.nodes = decoded.count("://")
                except:
                    status.nodes = content.count("://")
            
            # 统计协议
            status.protocols = count_protocols(content)
            
            # 检测更新时间
            date_match = re.search(r"(\d{4}-\d{2}-\d{2})", content)
            if date_match:
                status.last_update = date_match.group(1)
            
            status.status = "ok"
            
    except asyncio.TimeoutError:
        status.status = "timeout"
        status.error = "Timeout"
    except Exception as e:
        status.status = "fail"
        status.error = str(e)[:100]
    
    return status

async def test_all_sources(filepath: str, max_concurrent: int = 20) -> List[SourceStatus]:
    """测试所有订阅源"""
    sources = parse_sources_list(filepath)
    results = []
    
    connector = aiohttp.TCPConnector(limit=max_concurrent)
    async with aiohttp.ClientSession(timeout=TIMEOUT, connector=connector) as session:
        tasks = []
        for source_type, url, original in sources:
            tasks.append(test_source(session, source_type, url))
        
        print(f"开始测试 {len(tasks)} 个订阅源...")
        
        for i, future in enumerate(asyncio.as_completed(tasks)):
            result = await future
            results.append(result)
            print(f"[{i+1}/{len(tasks)}] {result}")
    
    return results

def generate_report(results: List[SourceStatus]) -> str:
    """生成测试报告"""
    ok = [r for r in results if r.status == "ok"]
    fail = [r for r in results if r.status == "fail"]
    timeout = [r for r in results if r.status == "timeout"]
    
    report = []
    report.append("=" * 60)
    report.append("订阅源测试报告")
    report.append("=" * 60)
    report.append(f"总测试数: {len(results)}")
    report.append(f"✅ 有效: {len(ok)}")
    report.append(f"❌ 失败: {len(fail)}")
    report.append(f"⏱️ 超时: {len(timeout)}")
    report.append("")
    
    # 按节点数排序
    ok_sorted = sorted(ok, key=lambda x: x.nodes, reverse=True)
    
    report.append("=" * 60)
    report.append("有效订阅源 (按节点数排序)")
    report.append("=" * 60)
    for r in ok_sorted[:50]:  # 只显示前50个
        protocols = ", ".join(r.protocols.keys()) if r.protocols else "unknown"
        report.append(f"{r.url}")
        report.append(f"  节点: {r.nodes} | 协议: {protocols} | 响应: {r.response_time:.2f}s")
    
    if fail:
        report.append("")
        report.append("=" * 60)
        report.append("无效订阅源")
        report.append("=" * 60)
        for r in fail:
            report.append(f"❌ {r.url}")
            report.append(f"   错误: {r.error}")
    
    return "\n".join(report)

def generate_new_sources_list(results: List[SourceStatus], original_file: str) -> str:
    """生成新的 sources.list，移除无效源"""
    ok_urls = {r.url for r in results if r.status == "ok"}
    
    new_lines = []
    with open(original_file, "r", encoding="utf-8") as f:
        for line in f:
            stripped = line.strip()
            
            # 保留注释和空行
            if not stripped or stripped.startswith("#") or stripped.upper() == "EOF":
                new_lines.append(line.rstrip())
                continue
            
            # 检查 URL 是否有效
            url = stripped.split("#")[0].strip()
            if url.startswith("!") or url.startswith("+") or url.startswith("*"):
                url = url[1:]
            
            if any(ok_url in stripped for ok_url in ok_urls):
                new_lines.append(stripped)
            else:
                new_lines.append(f"# [已失效] {stripped}")
    
    return "\n".join(new_lines)

async def main():
    import argparse
    parser = argparse.ArgumentParser(description="测试订阅源有效性")
    parser.add_argument("file", help="sources.list 文件路径")
    parser.add_argument("--output", "-o", help="输出报告文件")
    parser.add_argument("--new-sources", help="生成新的 sources.list 文件")
    parser.add_argument("--concurrent", "-c", type=int, default=20, help="并发数")
    args = parser.parse_args()
    
    results = await test_all_sources(args.file, args.concurrent)
    
    report = generate_report(results)
    print("\n" + report)
    
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(report)
        print(f"\n报告已保存到: {args.output}")
    
    if args.new_sources:
        new_content = generate_new_sources_list(results, args.file)
        with open(args.new_sources, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"新的订阅列表已保存到: {args.new_sources}")

if __name__ == "__main__":
    asyncio.run(main())
