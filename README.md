# AutoMergePublicNodes

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.11+-blue)]()
[![Update Nodes](https://github.com/LeilaoMi/AutoMergePublicNodes-Optimized/actions/workflows/update.yml/badge.svg)]()

> 29 个社区源 · sing-box 真实代理测试 · 按地区分组 · 每 6 小时自动更新 · 输出 Clash / sing-box / V2Ray 订阅

⚠️ **声明: 仅供学习研究, 公开节点稳定性差, 请自行甄别合规风险**

---

## 📝 更新日志

### 2026-06-01 - 代码质量修复

- **移除未使用导入**: 清理 main.py, parser.py, fetcher.py 中的冗余导入
- **优化 tester.py**: 每个节点复用同一 aiohttp session，减少资源开销
- **改进错误处理**: _alloc_port 失败时返回 TestResult 而非抛异常
- **参数验证**: main.py 和 audit_sources.py 添加参数范围检查
- **Tag 去重**: generator.py 添加截断后 tag 去重逻辑，防止 sing-box 配置冲突

---

## 📦 订阅地址

| 用途 | 文件 | 说明 |
|---|---|---|
| ⭐ **真测优选节点** | `output/verified.yaml` / `.json` / `.txt` | Top 100 真测通过, 带国旗 + 延迟 + 抖动标注 |
| 📦 全量未测节点 | `output/all.yaml` / `.json` / `.txt` | 8K+ 去重池, 供客户端自行测速 |
| 🔗 订阅转换链接 | `output/verified.converter.md` / `all.converter.md` | 一键转换为 Clash / sing-box / V2Ray / Surge / QX / Loon / Shadowrocket |
| 📊 运行统计 | `output/stats.json` | 协议分布、源通过率、Top 延迟 + 抖动 |
| 🔍 源审计报告 | `output/source_audit.json` | 每源节点数、存活性、连续死源计数 |

### Raw URL

```
https://raw.githubusercontent.com/LeilaoMi/AutoMergePublicNodes-Optimized/main/output/verified.txt
https://raw.githubusercontent.com/LeilaoMi/AutoMergePublicNodes-Optimized/main/output/verified.yaml
https://raw.githubusercontent.com/LeilaoMi/AutoMergePublicNodes-Optimized/main/output/all.yaml
```

### jsDelivr CDN (国内更稳)

```
https://cdn.jsdelivr.net/gh/LeilaoMi/AutoMergePublicNodes-Optimized@main/output/verified.txt
https://cdn.jsdelivr.net/gh/LeilaoMi/AutoMergePublicNodes-Optimized@main/output/verified.yaml
https://cdn.jsdelivr.net/gh/LeilaoMi/AutoMergePublicNodes-Optimized@main/output/all.yaml
```

---

## 🔧 工作流程

```
29 个社区订阅源
    ↓ 异步抓取 (并发 30, 失败回退 jsdelivr CDN, 自动重试)
    ↓ 多协议解析 (vless / vmess / trojan / ss / ssr / hy2 / tuic / anytls / wg / socks / http)
    ↓ GeoIP 国旗映射 (ip-api.com 批量查询, 跳过 Cloudflare Anycast)
    ↓ 按指纹去重 (type | server | port | key)
    ↓ 质量预过滤 (端口黑名单 + 同 server+protocol 去重 + 同 IP 限 2)
    ↓ TCP 预筛选 (并发 200, 超时 3s)
    ↓ 按协议分层下采样到 500
    ↓ ★ sing-box 真测 (并发 30):
    │   - 启动节点为本地 SOCKS5 (sniff=on, 域名分流)
    │   - 4 层验证: youtube 204 + google 204 + cloudflare geo(出口非CN) + 100KB 带宽下载
    │   - 拒绝 <30ms 同机房假节点
    │   - 计算延迟 + 抖动(jitter)
    ↓ 按真实延迟升序, 取 Top N
    ↓ 按地区自动分组 (🇭🇰 香港 / 🇯🇵 日本 / 🇺🇸 美国 / ...)
    ↓ 生成输出:
        verified.* (Top 100 真测通过, tag 限长 48 字符)
        all.* (全量去重池)
        *.converter.md (订阅转换链接)
```

---

## ✨ 功能特性

### 节点测试
- **sing-box 真测**: 用 Karing 同源内核启动节点, 实际 fetch 被墙端点, 非 TCP 握手
- **4 层验证**: YouTube/Google 204 + Cloudflare 出口地理 + 100KB 带宽下载
- **假节点过滤**: 延迟 <30ms 判定为同机房假节点
- **延迟 + 抖动**: 每节点记录平均延迟和 jitter, 入 tag 标注

### 输出格式
- **Clash Meta YAML**: 带 DNS 分流 + GEOSITE/GEOIP 规则 + 按地区分组
- **sing-box JSON**: Karing 直接导入, 带 DNS + rule-set 分流 + 按地区分组
- **V2Ray base64**: 通用订阅格式
- **URL 列表**: 一行一个节点 URL
- **订阅转换链接**: 4 个后端 × 8 个客户端 = 32 条一键转换链接

### 按地区分组
Clash 和 sing-box 输出自动按 GeoIP 国旗分组, 生成 `🇭🇰 香港` / `🇯🇵 日本` / `🇺🇸 美国` 等 url-test group (≥2 节点的地区才建组), selector 首页可一键切换地区。

### 源审计
- `tools/audit_sources.py` 测试每个源的存活性和节点数
- 跟踪 `consecutive_dead` (连续 0 节点次数), 连续 2+ 次建议自动下线
- 输出 `source_audit.json`

### CI 优化
- sing-box binary 缓存 (actions/cache@v4), 版本变化时自动更新
- 支持 workflow_dispatch 手动触发, 可自定义 `top_n` / `test_limit`
- 可选同时跑源审计

---

## ⚠️ CI 视角 vs 你的视角

GitHub Actions 在**美国机房**跑测试, 即使节点在 CI 视角通过, **在你网络下仍可能**:
- 被你 ISP 阻断 (QoS / RST)
- 被 GFW 干扰
- 节点已被分享给一万人达到限速

**导入后请在客户端再测一遍**, v2rayN 的 "测试所有 真实延迟" 是最终标准。verified 的意义是**预先筛掉连 US 都连不通的纯死节点**, 让客户端测速命中率从 ~5% 提高到 ~30-50%。

---

## 🔄 触发更新

- **自动**: GitHub Actions 每 6 小时 cron, `output/*` 自动 commit 回 main
- **手动**: `Actions → Update Nodes → Run workflow`
  - `top_n`: verified 输出节点数 (默认 100)
  - `test_limit`: 送入真测的最大节点数 (默认 500)
  - `audit`: 是否同时跑源审计

---

## 📁 项目结构

```
AutoMergePublicNodes-Optimized/
├── main.py                    # 主调度 + CLI
├── core/
│   ├── fetcher.py             # 异步抓取 (重试 + CDN 回退)
│   ├── parser.py              # 全协议解析 → sing-box outbound 格式
│   ├── tester.py              # sing-box 真实代理测试器
│   ├── generator.py           # 输出生成 (Clash / sing-box / V2Ray / 转换链接)
│   └── geo.py                 # GeoIP 国旗映射 (ip-api.com 批量查询)
├── tools/
│   └── audit_sources.py       # 源健康审计 (连续死源追踪)
├── config/
│   └── sources.yaml           # 29 个订阅源配置
├── output/                    # CI 输出 (git 跟踪)
│   ├── verified.*             # Top N 真测节点
│   ├── all.*                  # 全量去重池
│   ├── *.converter.md         # 订阅转换链接
│   ├── stats.json             # 运行统计
│   └── source_audit.json      # 源审计报告
├── requirements.txt           # aiohttp, aiohttp-socks, PyYAML
└── .github/workflows/
    └── update.yml             # CI 流程 (每 6h + 手动触发)
```

---

## 🧪 本地运行

```bash
git clone https://github.com/LeilaoMi/AutoMergePublicNodes-Optimized.git
cd AutoMergePublicNodes-Optimized
pip install -r requirements.txt

# 下载 sing-box (Linux amd64)
VERSION=$(curl -fsSL https://api.github.com/repos/SagerNet/sing-box/releases/latest | jq -r '.tag_name')
VER_NUM="${VERSION#v}"
curl -fsSL "https://github.com/SagerNet/sing-box/releases/download/${VERSION}/sing-box-${VER_NUM}-linux-amd64.tar.gz" | tar xz
mv sing-box-${VER_NUM}-linux-amd64/sing-box ./sing-box && chmod +x ./sing-box

# 运行
python main.py --top-n 100 --test-limit 500

# 环境变量覆盖 (CI/容器场景)
AUTONODES_TOP_N=200 AUTONODES_TEST_LIMIT=800 python main.py
```

### CLI 参数

| 参数 | 默认值 | 说明 |
|---|---|---|
| `--sources` | `config/sources.yaml` | 订阅源配置 |
| `--output-dir` | `output` | 输出目录 |
| `--top-n` | 100 | verified 输出节点数 |
| `--test-limit` | 500 | 送入真测的最大节点数 (0=不限) |
| `--fetch-concurrency` | 30 | 抓取并发数 |
| `--tcp-concurrency` | 200 | TCP 预筛选并发数 |
| `--test-concurrency` | 30 | sing-box 测试并发数 |
| `--test-timeout` | 6.0 | 单节点测试超时 (秒) |
| `--quality-filter` | on | 质量预过滤 (端口黑名单 + 同 server 限 2) |
| `--tcp-check` | on | TCP 预筛选 |
| `--real-test` | on | sing-box 真实测试 |

---

## 📜 License

MIT

## 致谢

- [sing-box](https://github.com/SagerNet/sing-box) — 真测内核
- 源贡献者: Au1rxx / tonykongcn / mheidari98 / ninjastrikers / Surfboardv2ray / Barabama / ts-sf / snakem982 / zhangkaiitugithub / Pawdroid / freefq / ermaozi / mfuu / ripaojiedian / peasoft / mahdibland / Misaka-blog / Mr8AHAL
