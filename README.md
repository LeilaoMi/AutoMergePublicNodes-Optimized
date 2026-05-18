# autonodes

🚀 **自动聚合公开代理节点 + TCP 预筛选 + 客户端实测**

> ⚠️ **设计理念**：GitHub Actions 在美国机房，**"美国 CI 能连通" ≠ "中国手机能用"**。
> 实测发现 CI 严测反而会过滤掉本来能用的节点。
> 所以本项目默认 **只做基础质量过滤 + TCP 可达性检查**，把"真实代理可用"的最终判断**交给你的客户端**（Karing / v2rayN 等都自带延迟测试）。

## ✨ 特性

- 📡 **全协议支持**：vmess / vless / trojan / ss / ssr / hysteria / hysteria2 / tuic / anytls / wireguard / socks5 / http
- 🔁 **自动更新**：GitHub Actions 每 6 小时跑一次
- 🧹 **质量过滤**：去重 / 端口黑名单（0/80/8080）/ 同 server 限 2 个 / 协议优先级
- ⚡ **TCP 可达性**：剔除连不上的死节点，按 TCP 延迟排序
- 📦 **大池子 + 精选**：`all.*` 全部可达节点（约 1500 个），`top.*` 延迟最低的 100 个
- 📥 **4 种格式**：sing-box JSON / Clash YAML / V2Ray Base64 / URL 列表
- 🌐 **动态 URL**：支持 `%Y/%m/%d` 日期模板自动填充
- 🔍 **源审计工具**：一键检测哪些源失效了
- 🧪 **可选真测**：手动触发时可加 `--real-test`（仅供参考）

## 📌 订阅链接（公开仓库，永久有效）

### 推荐用法

**导入 `all.*` 到客户端，用客户端的"延迟测试"在你的真实网络环境下挑选。**

### 🌍 全部可达节点

| 客户端 | GitHub raw（直链） | jsDelivr CDN（国内加速） |
|--------|-------------------|------------------------|
| Karing / sing-box | `https://raw.githubusercontent.com/LeilaoMi/AutoMergePublicNodes-Optimized/main/output/all.json` | `https://cdn.jsdelivr.net/gh/LeilaoMi/AutoMergePublicNodes-Optimized@main/output/all.json` |
| Clash / Mihomo | `https://raw.githubusercontent.com/LeilaoMi/AutoMergePublicNodes-Optimized/main/output/all.yaml` | `https://cdn.jsdelivr.net/gh/LeilaoMi/AutoMergePublicNodes-Optimized@main/output/all.yaml` |
| V2RayN / v2rayNG | `https://raw.githubusercontent.com/LeilaoMi/AutoMergePublicNodes-Optimized/main/output/all.txt` | `https://cdn.jsdelivr.net/gh/LeilaoMi/AutoMergePublicNodes-Optimized@main/output/all.txt` |

### 🎯 精选 Top 100（按 TCP 延迟最低）

| 客户端 | GitHub raw | jsDelivr CDN |
|--------|------------|--------------|
| Karing / sing-box | `https://raw.githubusercontent.com/LeilaoMi/AutoMergePublicNodes-Optimized/main/output/top.json` | `https://cdn.jsdelivr.net/gh/LeilaoMi/AutoMergePublicNodes-Optimized@main/output/top.json` |
| Clash / Mihomo | `https://raw.githubusercontent.com/LeilaoMi/AutoMergePublicNodes-Optimized/main/output/top.yaml` | `https://cdn.jsdelivr.net/gh/LeilaoMi/AutoMergePublicNodes-Optimized@main/output/top.yaml` |
| V2RayN / v2rayNG | `https://raw.githubusercontent.com/LeilaoMi/AutoMergePublicNodes-Optimized/main/output/top.txt` | `https://cdn.jsdelivr.net/gh/LeilaoMi/AutoMergePublicNodes-Optimized@main/output/top.txt` |

## 🛠️ 本地运行

```bash
pip install -r requirements.txt

# 默认模式（推荐）：抓取 → 去重 → TCP 检查 → 输出
python main.py

# 加上 sing-box 真测（仅参考，CI 视角）
python main.py --real-test

# 审计订阅源
python tools/audit_sources.py
```

## ⚙️ 命令行参数

```
--top-n N              top.* 输出节点数（默认 100，按 TCP 延迟）
--tcp-check / --no-tcp-check    默认开
--tcp-concurrency N    默认 200
--tcp-timeout S        默认 3
--real-test            可选启用 sing-box 真测（默认关闭）
--test-limit N         真测时下采样上限（默认 0=不限）
--fetch-concurrency N  默认 30
--fetch-timeout S      默认 15
```

## 📂 项目结构

```
autonodes/
├── core/                  # 核心模块
│   ├── parser.py          # 协议解析（统一为 sing-box outbound）
│   ├── fetcher.py         # 异步订阅抓取（支持动态 URL / 列表）
│   ├── tester.py          # sing-box 真实测试（可选）
│   └── generator.py       # 4 种格式订阅生成
├── tools/
│   └── audit_sources.py   # 源审计
├── config/
│   └── sources.yaml       # 订阅源配置
├── output/                # 生成的订阅文件
├── main.py                # 入口
└── .github/workflows/update.yml
```

## 📜 添加/移除订阅源

编辑 `config/sources.yaml`：

```yaml
sources:
  - { url: "https://example.com/sub.txt", name: "示例", kind: url }
  - { url: "https://example.com/uploads/%Y/%m/%Y%m%d.yaml", name: "动态日期", kind: dynamic }
  - { url: "https://example.com/list.txt", name: "订阅列表", kind: list }
  - { url: "...", name: "带过滤", ignore_protocols: [ssr], max_nodes: 200 }
```

## 🤝 致谢

聚合了以下高质量公共源（2026 年仍在活跃更新）：

- [rtwo2/FastNodes](https://github.com/rtwo2/FastNodes) - 每 3 小时
- [VovaplusEXP/p-configs](https://github.com/VovaplusEXP/p-configs) - 每 6 小时
- [Au1rxx/free-vpn-subscriptions](https://github.com/Au1rxx/free-vpn-subscriptions) - 每小时
- [ninjastrikers/v2ray-configs](https://github.com/ninjastrikers/v2ray-configs) - 每 60 分钟
- [MhdiTaheri/V2rayCollector](https://github.com/MhdiTaheri/V2rayCollector)
- 以及 51 个其他 GitHub / Telegram 频道源

## ⚠️ 免责

所有节点均来自互联网公开来源。请合法使用，不要用于浏览敏感账户或财务网站。
