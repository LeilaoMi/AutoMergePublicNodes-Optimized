# AutoMergePublicNodes

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.11+-blue)]()
[![Update Nodes](https://github.com/LeilaoMi/AutoMergePublicNodes-Optimized/actions/workflows/update.yml/badge.svg)]()

> 自动聚合公开代理节点 · GitHub Actions 用 sing-box 做**真实代理测试** · 每 6 小时更新

⚠️ **声明:仅供学习研究,公开节点稳定性差,请自行甄别合规风险**

---

## 📦 订阅地址

| 用途 | 文件 | 推荐场景 |
|---|---|---|
| ⭐ **真测过的优选节点** | `output/verified.yaml` / `verified.json` / `verified.txt` | **优先用这个**,从 US Actions 视角 HTTP 真测过 |
| 📦 全量未测节点 | `output/all.yaml` / `all.json` / `all.txt` | verified 不够用时备用,自己客户端测速 |
| 📊 运行统计 | `output/stats.json` | 健康源数、协议分布、Top 延迟 |

复制 raw URL 导入 v2rayN / Karing / Clash Meta:

```
https://raw.githubusercontent.com/LeilaoMi/AutoMergePublicNodes-Optimized/main/output/verified.txt
https://raw.githubusercontent.com/LeilaoMi/AutoMergePublicNodes-Optimized/main/output/verified.yaml
https://raw.githubusercontent.com/LeilaoMi/AutoMergePublicNodes-Optimized/main/output/all.yaml
```

---

## 🔧 工作流程(改 v2 后的现状)

```
20 个活跃公开源
    ↓ 异步抓取 (并发 30)
    ↓ 多协议解析 (vless / vmess / trojan / ss / hysteria2 / tuic / ...)
    ↓ 协议级质量过滤 (UUID 格式、字段完整性等)
    ↓ 按指纹去重 (server + port + protocol-specific)
    ↓ TCP 预筛选 (并发 200) - 滤掉端口都不通的死节点
    ↓ 按协议分层下采样到 500 (避免单一协议挤占)
    ↓ ★ sing-box 真测 (并发 30) - 启动节点本地 SOCKS,实际 fetch Google/Cloudflare
    ↓ 过滤同机房假节点(延迟 < MIN_LATENCY_MS)
    ↓ 按真实延迟升序排
    ↓
verified.* (Top 100 真通)  +  all.* (全量去重备份)
```

**关键改动 vs 上版**:
- ✅ 默认开 `--real-test` —— Actions 跑 sing-box 真测,过滤掉 TCP 通但代理死的"假节点"
- ✅ 默认开 `--quality-filter` —— 协议级字段校验
- ✅ 默认 `--test-limit 500` —— Actions 时间可控
- ✅ 删了 31 个 404/0 节点的死源 (51→20)
- ❌ 取消 `top.*` 输出(那时按 TCP 延迟排,误导性强),改为 `verified.*` (真测过的)

---

## ⚠️ 重要提示:CI 视角 vs 你的视角

GitHub Actions 在**美国机房**跑测试,即使节点在 CI 视角通过,**在你网络下仍可能**:
- 被你 ISP 阻断(QoS / RST)
- 被 GFW 干扰
- 节点已被分享给一万人达到限速

所以**导入后还是要在客户端再测一遍**,v2rayN 的"测试所有 真实延迟"是最终标准。verified 的意义是**预先筛掉那些连 US 都连不通的纯死节点**,让你在客户端测的命中率从 ~5% 提高到 ~30-50%。

---

## 🔄 触发更新

- **自动**:GitHub Actions 每 6 小时跑一次 cron,把 `output/*` 自动 commit 回 main
- **手动**:仓库 `Actions → Update Nodes → Run workflow`,可自定义 `top_n` / `test_limit` / 是否同时跑源审计

---

## 📁 项目结构

```
AutoMergePublicNodes-Optimized/
├── main.py                  # 主调度
├── core/
│   ├── fetcher.py           # 异步抓取
│   ├── parser.py            # 多协议解析(vless/vmess/trojan/ss/hy2/tuic/...)
│   ├── tester.py            # sing-box 真实代理测试器
│   └── generator.py         # 输出 yaml/json/txt/url
├── tools/audit_sources.py   # 源健康审计
├── config/sources.yaml      # 20 个活跃源
├── output/                  # CI 写出的订阅
└── .github/workflows/update.yml
```

---

## 🧪 本地手动跑(可选)

```bash
git clone https://github.com/LeilaoMi/AutoMergePublicNodes-Optimized.git
cd AutoMergePublicNodes-Optimized
pip install -r requirements.txt

# 下载 sing-box(macOS/Linux)
curl -fsSL https://github.com/SagerNet/sing-box/releases/latest/download/sing-box-linux-amd64.tar.gz | tar xz

python main.py --top-n 100 --test-limit 500
```

---

## 📜 License

MIT

## 致谢

- [sing-box](https://github.com/SagerNet/sing-box) - 真测内核
- 源贡献者:Au1rxx / tonykongcn / mheidari98 / ninjastrikers / Surfboardv2ray / Barabama / ts-sf / snakem982 / zhangkaiitugithub / qjlxg / vveg26 / Pawdroid / SnapdragonLee / freenode/proxypool / chengaopan / soroushmirzaei / mfuu
