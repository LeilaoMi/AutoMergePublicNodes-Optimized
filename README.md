# autonodes

🚀 **自动聚合公开代理节点 + 真实测试 + 多协议全覆盖**

## ✨ 特性

- 📡 **全协议支持**：vmess / vless / trojan / ss / ssr / hysteria / hysteria2 / tuic / anytls / wireguard / socks5 / http
- 🔁 **自动更新**：GitHub Actions 每 6 小时跑一次
- ⚡ **真实测试**：用 sing-box（Karing 同源内核）启动每个节点做真实 HTTP 请求，确保在 Karing 中能用
- 🎯 **Top N 输出**：按真实延迟排序，输出最优 50 个节点
- 📥 **多格式订阅**：sing-box JSON / Clash YAML / V2Ray Base64
- 🌐 **动态 URL**：支持 `%Y/%m/%d` 日期模板自动填充
- 🔍 **源审计工具**：一键检测哪些源失效了

## 📌 订阅链接

> 替换 `LeilaoMi/AutoMergePublicNodes-Optimized` 为你的仓库路径

| 客户端 | 链接 |
|--------|------|
| **Karing / sing-box** | `https://raw.githubusercontent.com/LeilaoMi/AutoMergePublicNodes-Optimized/main/output/top50.json` |
| **Clash / Mihomo** | `https://raw.githubusercontent.com/LeilaoMi/AutoMergePublicNodes-Optimized/main/output/top50.yaml` |
| **V2RayN / v2rayNG** | `https://raw.githubusercontent.com/LeilaoMi/AutoMergePublicNodes-Optimized/main/output/top50.txt` |
| 节点 URL 列表 | `https://raw.githubusercontent.com/LeilaoMi/AutoMergePublicNodes-Optimized/main/output/top50.urls` |
| 统计信息 | `https://raw.githubusercontent.com/LeilaoMi/AutoMergePublicNodes-Optimized/main/output/stats.json` |

`all.*` 系列是测试通过的所有节点（不限 50）。

## 🛠️ 本地运行

```bash
# 1) 安装依赖
pip install -r requirements.txt

# 2) 下载 sing-box（与 workflow 中相同版本）
# https://github.com/SagerNet/sing-box/releases

# 3) 运行完整流水线
python main.py --top-n 50

# 4) 跳过真实测试（仅 TCP 预筛选，快速）
python main.py --no-real-test

# 5) 审计订阅源
python tools/audit_sources.py
```

## ⚙️ 命令行参数

```
--top-n N             最终输出 N 个节点（默认 50）
--test-limit N        送入真实测试的最大节点数（默认 500）
--tcp-check / --no-tcp-check
--real-test / --no-real-test
--fetch-concurrency N (默认 30)
--tcp-concurrency N   (默认 200)
--test-concurrency N  (默认 30)
```

## 📂 项目结构

```
autonodes/
├── core/              # 核心模块
│   ├── parser.py      # 协议解析（统一为 sing-box outbound）
│   ├── fetcher.py     # 异步订阅抓取
│   ├── tester.py      # sing-box 真实测试
│   └── generator.py   # 多格式订阅生成
├── tools/
│   └── audit_sources.py  # 源审计
├── config/
│   └── sources.yaml   # 订阅源配置
├── output/            # 生成的订阅文件
├── main.py            # 入口
└── .github/workflows/update.yml
```

## 📜 添加/移除订阅源

编辑 `config/sources.yaml`：

```yaml
sources:
  # 静态 URL
  - { url: "https://example.com/sub.txt", name: "示例", kind: url }

  # 动态日期 URL
  - { url: "https://example.com/uploads/%Y/%m/%Y%m%d.yaml", name: "示例", kind: dynamic }

  # 订阅列表（文件内每一行又是一个订阅 URL）
  - { url: "https://example.com/sub-list.txt", name: "列表", kind: list }

  # 忽略某些协议 / 限制数量
  - { url: "...", name: "限制示例", ignore_protocols: [ssr], max_nodes: 200 }
```

## 🤝 致谢

聚合了以下高质量公共源（已通过 2026 年活跃性测试）：

- [rtwo2/FastNodes](https://github.com/rtwo2/FastNodes) - 每 3 小时更新
- [VovaplusEXP/p-configs](https://github.com/VovaplusEXP/p-configs) - 每 6 小时
- [Au1rxx/free-vpn-subscriptions](https://github.com/Au1rxx/free-vpn-subscriptions) - 每小时
- [ninjastrikers/v2ray-configs](https://github.com/ninjastrikers/v2ray-configs) - 每 60 分钟
- [MhdiTaheri/V2rayCollector](https://github.com/MhdiTaheri/V2rayCollector)
- 以及其他多个 GitHub / Telegram 频道源

## ⚠️ 免责

所有节点均来自互联网公开来源。请合法使用，不要用于浏览敏感账户。
