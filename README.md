# AutoMergePublicNodes-Optimized

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.12-blue)](requirements.txt)
[![节点更新](https://github.com/LeilaoMi/AutoMergePublicNodes-Optimized/actions/workflows/update.yml/badge.svg)](https://github.com/LeilaoMi/AutoMergePublicNodes-Optimized/actions/workflows/update.yml)

每 6 小时从 100 多个公开订阅源收集节点，用 sing-box 逐个做真实代理连接测试，再用海内探针检查能否连上，最后输出可直接导入客户端的订阅。

> 仅供学习研究。公开节点来源不明、随时失效，可能记录流量，请勿用于登录重要账号或传输敏感信息，并自行评估合规风险。

---

## 怎么选订阅

| 你在哪 | 用哪个 | 说明 |
|---|---|---|
| **海内** | `verified` | 海外真测通过，并且海内探针能和节点端口完成 TCP 握手。数量较少（通常几十个），但最有希望直接能用 |
| 海外，或 verified 不够用 | `global` | 海外真测通过即可，最多 300 个，按综合评分排序。不保证海内能连上 |
| 想自己测 | `all`（在 `data` 分支） | 去重后的全量候选池，约 2.7 万个，**未经测试** |

每个档位都有四种格式：`.yaml`（Clash / Mihomo）、`.txt`（Base64，v2rayN / v2rayNG / Shadowrocket）、`.json`（sing-box / Karing）、`.urls`（明文链接，每行一个）。

### 订阅地址

jsDelivr（海内通常更快）：

```text
https://cdn.jsdelivr.net/gh/LeilaoMi/AutoMergePublicNodes-Optimized@main/output/verified.yaml
https://cdn.jsdelivr.net/gh/LeilaoMi/AutoMergePublicNodes-Optimized@main/output/verified.txt
https://cdn.jsdelivr.net/gh/LeilaoMi/AutoMergePublicNodes-Optimized@main/output/verified.json
https://cdn.jsdelivr.net/gh/LeilaoMi/AutoMergePublicNodes-Optimized@main/output/global.yaml
https://cdn.jsdelivr.net/gh/LeilaoMi/AutoMergePublicNodes-Optimized@main/output/global.txt
https://cdn.jsdelivr.net/gh/LeilaoMi/AutoMergePublicNodes-Optimized@main/output/global.json
https://cdn.jsdelivr.net/gh/LeilaoMi/AutoMergePublicNodes-Optimized@data/output/all.yaml
https://cdn.jsdelivr.net/gh/LeilaoMi/AutoMergePublicNodes-Optimized@data/output/all.txt
```

GitHub Raw（jsDelivr 不可用时）：

```text
https://raw.githubusercontent.com/LeilaoMi/AutoMergePublicNodes-Optimized/main/output/verified.yaml
https://raw.githubusercontent.com/LeilaoMi/AutoMergePublicNodes-Optimized/main/output/global.yaml
https://raw.githubusercontent.com/LeilaoMi/AutoMergePublicNodes-Optimized/data/output/all.yaml
```

> 文件名把 `verified` / `global` 换掉、扩展名换成需要的格式即可。另有按协议（`by_protocol/`）、按地区（`by_region/`）和每 100 个一块（`chunks/`）的拆分订阅，见 [输出文件](#输出文件)。订阅转换链接在 `output/*.converter.md`，第三方转换服务可能失效或记录订阅地址，能直接用本仓库文件就别转换。

### 在线筛选

👉 **[节点筛选页](https://leilaomi.github.io/AutoMergePublicNodes-Optimized/)**：在浏览器里按地区、协议、关键词筛选全量池，标出每个节点的 CI 实测结果（海内可达 / 海外可用 + 延迟），可以只看实测通过的、按延迟排序，然后导出 Clash YAML、Base64 或 sing-box JSON。全部在本地计算，不经过任何服务器。

> 浏览器无法直接连接代理协议，所以页面不做测速，延迟数据来自最近一轮 CI。

👉 **[订阅源健康面板](https://leilaomi.github.io/AutoMergePublicNodes-Optimized/sources.html)**：各订阅源的抓取状态、死源清单、贡献排行和最近 30 轮的漏斗趋势。

---

<!-- AUTONODES_STATS_START -->
## 当前运行状态

| 指标 | 数值 |
| --- | --- |
| 更新时间 | 2026-10-24 12:52（北京时间） |
| 订阅源（可用/总数） | 86/107 |
| 原始节点 → 去重后 | 92457 → 24506 |
| 送入测试 → 探活通过 → 真测通过 | 3000 → 599 → 449 |
| 国内可达 / 不可达 / 未知 | 161 / 288 / 0 |
| 国内检查缓存命中 | 255 |
| **verified 输出** | 161 |
| **global 输出** | 300 |
| all 全量池 | 24506 |
| 本轮耗时 | 309.6 秒 |

> 输出保护：无。完整报告见 `output/health_report.md`、`output/stats.json`。

### Top 节点评分

| 评分 | 协议 | 延迟(ms) | 来源 |
| --- | --- | --- | --- |
| 94.88 | vless | 209.4 | Au1rxx-base64 |
| 94.61 | vless | 214.7 | Au1rxx-base64 |
| 94.37 | vless | 197.5 | Au1rxx-base64 |
| 94.35 | vless | 196.0 | Au1rxx-base64 |
| 93.41 | shadowsocks | 257.0 | Au1rxx-base64 |

### Top 来源质量

| 来源 | 评分 | 测试数 | 建议 |
| --- | --- | --- | --- |
| ermaozi | 1.0 | 79 | prefer |
| Au1rxx-base64 | 0.958 | 270 | prefer |
| Surfboard-tg-mixed | 0.942 | 56 | prefer |
| mheidari-all | 0.469 | 173 | observe |
| roosterkid-openproxylist-v2ray | 0.406 | 4 | observe |

<!-- AUTONODES_STATS_END -->

---

## 工作原理

```text
107 个订阅源
  → 抓取与解析（ss / ssr / vmess / vless / trojan / hysteria2 / tuic / anytls / socks / http）
  → 指纹去重、GeoIP 标记
  → 质量预过滤、TCP 预筛（DNS 解析后拦截内网和云元数据地址）
  → 按协议与来源的历史通过率加权抽样，最多 3000 个送测（15% 名额留给历史数据少的来源）
  → 轻量探活：100 并发，只测 YouTube generate_204，4 秒超时
  → 完整真测：75 并发，每个请求 6 秒、每个节点总计 15 秒
  → 综合评分排序                                  ──→ global（最多 300 个）
  → 海内检查：GlobalPing 探针 TCP 握手（带缓存）──→ verified
```

### 完整真测测什么

通过 sing-box 本地起代理后依次请求：

| 目标 | 作用 | 不通过的后果 |
|---|---|---|
| YouTube / Google `generate_204` | 基本连通，同时采样延迟和抖动 | 淘汰 |
| `baidu.com/robots.txt` | 出口能否访问海内站点 | 不进 verified，但会再测一次，通过就进 global |
| Cloudflare `cdn-cgi/trace` | 出口国家；出口在海内的节点无法连接 | 出口在海内或请求失败则淘汰 |
| Cloudflare 100 KB 下载 | 测速，必须完整下载 | 淘汰 |
| Netflix / ChatGPT | 解锁情况，**只记录、不影响去留** | — |

延迟低于 30 ms 的节点会被当作异常（多为本机回环或假节点）剔除。明文 HTTP / SOCKS 代理（无 TLS）不进入 verified 和 global，all 里仍保留。

### 海内检查

海外 CI 测不出"从当地能不能连上"，所以对真测通过的节点，再让 [GlobalPing](https://globalping.io) 的探针向节点的 IP 和端口发起 TCP 握手（3 次，任一次成功即算可达）。

- **额度**：匿名每小时 250 次，GitHub Runner 的出口 IP 是共享的，额度可能已被别人用掉。程序先查剩余额度，每轮最多新检查 200 个。
- **缓存**：结果存在 `data` 分支的 `china_cache.json`。可达结果 12 小时内复用，不可达 24 小时内复用，省下的额度用来检查排名更靠后的节点，几轮之后基本能覆盖全部真测通过的节点。
- **三种结果**：可达进 verified；不可达和未检查（未知）的都只进 global，未知不等于坏。
- **局限**：TCP 握手成功只说明 IP 和端口没被封，不能保证代理协议本身不被识别（比如按 SNI 或流量特征封锁）。

### 综合评分

排序用 `config/scoring.yaml` 的加权分数，满分 100，再加上稳定性奖励：

| 因子 | 权重 | 说明 |
|---|---:|---|
| 延迟 | 25 | 真测延迟 |
| 来源历史 | 20 | 订阅源历史通过率（EWMA） |
| 抖动 | 15 | 同一节点多次采样的波动 |
| 协议历史 | 15 | 协议历史通过率 |
| TCP | 10 | TCP 预筛延迟 |
| 速度 | 10 | 100 KB 下载速度 |
| 抗识别 | 5 | REALITY / uTLS / WS+TLS、443 端口等加分 |

连续通过 2 轮及以上的节点额外加分，加分等于连续轮数，最多 +5。另有三个预设模板可在本地用 `--scoring-rules` 切换：`scoring.low_latency.yaml`（偏速度）、`scoring.stability.yaml`（偏稳定）、`scoring.source_quality.yaml`（偏来源质量）。

### 防止输出突然缩水

- 本轮 verified 或 global 少于上一轮的一半时，保留上一轮的文件；最多连续保留 3 轮，避免节点真的变少时一直发布旧数据。
- 海内检查完全失败（GlobalPing 故障或额度耗尽）时，verified 保留上一轮，不会把未经当地验证的节点当作 verified 发布。
- 真测全部失败时降级为 TCP 结果，避免订阅变空，并在 `stats.json` 里标记 `degraded_mode`。

---

## 输出文件

`main` 分支 `output/` 下：

| 文件 | 内容 |
|---|---|
| `verified.{yaml,txt,json,urls}` | 海外真测通过 + 海内可达 |
| `global.{yaml,txt,json,urls}` | 海外真测通过，最多 300 个 |
| `by_protocol/{verified,global}_<协议>.txt` | 按协议拆分（Base64） |
| `by_region/<地区>.{txt,urls}` | 按地区拆分，基于 global，每轮重建 |
| `chunks/{verified,global}_<n>.txt` | 每 100 个节点一块（Base64） |
| `*.converter.md` | 常见订阅转换服务的转换链接 |
| `stats.json` | 本轮全部统计：各阶段数量和耗时、失败原因、协议和来源通过率 |
| `health_report.md` / `.json` | 健康检查（ok / warning / critical） |
| `daily_report.md` | 给人看的每日摘要 |
| `source_scores.md`、`source_cleanup_suggestions.{md,json}`、`source_audit.json`、`source_discovery.json` | 订阅源评分、清理建议、审计结果、新源发现 |
| `scoring_profiles.md` | 各评分模板对比 |
| `trend_history.json` | 最近 30 轮的趋势 |

`data` 分支 `output/` 下（每轮只保留一个提交，不积累历史）：

| 文件 | 内容 |
|---|---|
| `all.{yaml,txt,json,urls}` | 去重后的全量候选池（未测试） |
| `geo_cache.json` | IP 归属地缓存 |
| `node_stability.json` | 节点跨轮稳定性 |
| `china_cache.json` | 海内检查缓存 |
| `score_details.json` | 每个节点的评分明细 |

---

## 自动运行

- **时间**：每 6 小时一次，当地时间约 01:23、07:23、13:23、19:23（GitHub 的定时任务可能晚几分钟到几十分钟）。一轮约 5 到 8 分钟。
- **手动运行**：`Actions → 更新节点 → Run workflow`，可调 `top_n`（默认 300，上限 1000）、`test_limit`（默认 3000，上限 5000）、`min_retain_ratio`（默认 0.5，0 为关闭缩水保护）。
- **只有 main 分支的运行会提交结果**，在其他分支手动运行只做测试，不会推送。
- 失败时自动开 Issue，下一次成功后自动关闭。
- 每轮结束后刷新 jsDelivr 缓存。

---

## 本地运行

```bash
git clone https://github.com/LeilaoMi/AutoMergePublicNodes-Optimized.git
cd AutoMergePublicNodes-Optimized
pip install -r requirements.txt
# 把 sing-box 可执行文件放到仓库根目录，然后：
python main.py --top-n 100 --test-limit 500
```

常用参数：`--no-china-check`（跳过海内检查）、`--no-real-test`（只做 TCP 测试）、`--scoring-rules config/scoring.stability.yaml`（换评分模板）。完整参数见 `python main.py --help`。

检查命令：

```bash
python -m unittest -v tests.test_regressions   # 回归测试
python tools/validate_config.py --sources config/sources.yaml --filter-rules config/filter_rules.yaml --scoring-rules config/scoring.yaml
python tools/doctor.py                          # 本地环境诊断
python tools/import_contract.py                 # 检查悬空 import
```

在 global 基础上本地再筛一遍：

```bash
python tools/local_filter.py --input output/global.urls --output-prefix local_verified --top-n 100
```

> 设置环境变量 `GLOBALPING_TOKEN` 可以用自己的 GlobalPing 账号额度（每小时 500 次，同账号所有 token 共用）。

---

## 维护订阅源

订阅源在 `config/sources.yaml`。每轮开始前会审计所有源，连续 20 轮抓不到节点的源自动停用。新增源前建议确认：能访问、能解析出节点、和现有源相比有去重后的新增，大体量源设置 `max_nodes`。

清理建议默认只读，真要停用需要显式确认：

```bash
python tools/suggest_source_cleanup.py --output-dir output --sources config/sources.yaml \
  --apply --confirm-disable --only source-a,source-b
```

---

## 项目结构

```text
main.py              主流程与命令行参数
core/
  fetcher.py         抓取订阅源（重试、CDN 回退）
  parser.py          协议解析
  filtering.py       质量预过滤、SSRF 拦截
  sampling.py        按历史通过率加权抽样
  tester.py          sing-box 真测（探活 + 完整测试）
  scoring.py         综合评分
  _fingerprint_test.py  抗识别评分
  globalping.py      海内 TCP 检查与缓存
  geo.py             IP 归属地（ip-api.com，带缓存）
  generator.py       生成各格式订阅
  stats.py           来源评分、趋势、稳定性
  report.py / readme_updater.py  健康报告、更新 README 状态区
tools/               审计、报告、源清理、源发现、本地筛选、诊断
config/              订阅源、过滤规则、评分模板
docs/                筛选页、源健康面板、客户端指南
tests/               回归测试与协议样例
.github/workflows/update.yml  自动运行
```

---

## 关于 2026-10-16 的历史改写

为了给仓库瘦身（完整 clone 从约 1.5 GB 降到约 26 MB），`main` 分支的历史在 2026-10-16 被改写，删除了历史中所有 `output/` 产物，大文件此后发布在 `data` 分支。订阅地址（`@main`、`@data`）不受影响，但旧的 commit 链接已经失效。

如果你在此之前 fork 或 clone 过本仓库，请重新 fork，或在本地执行（会丢弃本地未提交的改动，请先备份）：

```bash
git fetch origin
git reset --hard origin/main
```

---

## 文档

- [客户端导入指南](docs/client-guide.md)
- [测速、转换和排障资源](docs/resources.md)
- [变更记录](CHANGELOG.md) · [版本说明](docs/releases/)

## 致谢

[sing-box](https://github.com/SagerNet/sing-box) · [GlobalPing](https://globalping.io) · 所有公开订阅源的维护者

## License

MIT
