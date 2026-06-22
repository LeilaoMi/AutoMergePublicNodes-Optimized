# AutoMergePublicNodes-Optimized

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.11+-blue)]()
[![节点更新](https://github.com/LeilaoMi/AutoMergePublicNodes-Optimized/actions/workflows/update.yml/badge.svg)](https://github.com/LeilaoMi/AutoMergePublicNodes-Optimized/actions/workflows/update.yml)

> 自动聚合公开代理订阅源，使用 sing-box 真实代理测试，输出可直接导入主流客户端的订阅文件，并提供零服务器成本的浏览器端动态订阅网关。
> *仅供学习研究。公开节点稳定性不可控，请自行评估可用性与合规风险。*

---

## 🌟 核心特性

- **⚡ 两阶段测活**：先用 100 并发轻量探活（只测 204）快速筛掉不可达节点，再对剩余节点做完整真测，总耗时从 60+ 分钟降到 ~8 分钟。
- **🎯 7 因子加权评分**：延迟、抖动、TCP、下载速度、指纹抗检测、协议历史、来源历史。REALITY/uTLS 优先，443 端口加成，跨周期稳定节点加分。
- **🔒 SSRF 防投毒**：拦截指向私有地址与云元数据端点（如 `169.254.169.254`）的恶意节点，保护 CI 运行环境。
- **📈 节点稳定性追踪**：跨周期连续真测通过的节点获评分加成，历史稳定的老节点优先排在前面。
- **🌐 动态订阅网关**：GitHub Pages 浏览器端实时筛选，多 CDN 故障转移，本地测速，一键导出 Clash / Base64 / sing-box JSON。

---

## 🚀 动态订阅网关 (推荐)

访问项目的 **GitHub Pages** 站点，在浏览器端实时过滤并生成专属订阅链接：
👉 **[点击进入动态网关](https://leilaomi.github.io/AutoMergePublicNodes-Optimized/)**

### 订阅网关
- 按地区、协议、关键词实时筛选全量节点池
- 多 CDN 自动故障转移（jsDelivr → Statically → GitHub Raw），单源挂了也能用
- 浏览器端测速：对筛选结果并发 TCP 连通性测试，标红超时节点，超时阈值可调
- 一键下载 Clash YAML（含多分组策略）/ Base64 通用订阅 / sing-box JSON / 复制专属订阅链接
- 计算全在本地，保护隐私，零服务器开销

### 订阅源健康面板

👉 **[订阅源健康](https://leilaomi.github.io/AutoMergePublicNodes-Optimized/sources.html)**

- 订阅源抓取状态总览（健康 / 失效 / 自动禁用计数）
- 趋势图：30 轮运行漏斗（原始节点 → 去重 → TCP → 真测 → Verified）
- 死源清单：连续死亡计数、抓取错误、抓取耗时
- 源贡献排行：按解析节点数排序，识别高价值源

*支持条件：地区 (如 `HK,JP`)、协议 (如 `vless,trojan`)。*

---

## 快速选择

| 使用场景 | 推荐文件 | 说明 |
|---|---|---|
| Clash / Mihomo | `output/verified.yaml` | 首选，真测通过后输出 |
| v2rayN / v2rayNG | `output/verified.txt` | base64 通用订阅 |
| Karing / sing-box | `output/verified.json` | sing-box JSON 配置 |
| 兼顾数量 | `output/global.yaml` / `output/global.txt` / `output/global.json` | 海外测试通过，但国内站点连通不一定稳定 |
| 自行测速 | `output/all.urls` / `output/all.txt` / `output/all.yaml` | 全量去重候选池，不保证可用 |
| 查看状态 | `output/daily_report.md` / `output/health_report.md` / `output/health_report.json` / `output/source_scores.md` / `output/scoring_profiles.md` / `output/source_cleanup_suggestions.md` | 日报、健康报告、评分模板、源评分、清理建议 |

`verified.*` 数量不是固定值。`--top-n` 只是上限，实际数量取决于本轮真测结果。

---

## 订阅地址

### GitHub Raw
```text
https://raw.githubusercontent.com/LeilaoMi/AutoMergePublicNodes-Optimized/main/output/verified.txt
https://raw.githubusercontent.com/LeilaoMi/AutoMergePublicNodes-Optimized/main/output/verified.yaml
https://raw.githubusercontent.com/LeilaoMi/AutoMergePublicNodes-Optimized/main/output/verified.json
https://raw.githubusercontent.com/LeilaoMi/AutoMergePublicNodes-Optimized/main/output/global.txt
https://raw.githubusercontent.com/LeilaoMi/AutoMergePublicNodes-Optimized/main/output/global.yaml
https://raw.githubusercontent.com/LeilaoMi/AutoMergePublicNodes-Optimized/main/output/global.json
https://raw.githubusercontent.com/LeilaoMi/AutoMergePublicNodes-Optimized/main/output/all.txt
https://raw.githubusercontent.com/LeilaoMi/AutoMergePublicNodes-Optimized/main/output/all.yaml
```

### jsDelivr
```text
https://cdn.jsdelivr.net/gh/LeilaoMi/AutoMergePublicNodes-Optimized@main/output/verified.txt
https://cdn.jsdelivr.net/gh/LeilaoMi/AutoMergePublicNodes-Optimized@main/output/verified.yaml
https://cdn.jsdelivr.net/gh/LeilaoMi/AutoMergePublicNodes-Optimized@main/output/verified.json
https://cdn.jsdelivr.net/gh/LeilaoMi/AutoMergePublicNodes-Optimized@main/output/global.txt
https://cdn.jsdelivr.net/gh/LeilaoMi/AutoMergePublicNodes-Optimized@main/output/global.yaml
https://cdn.jsdelivr.net/gh/LeilaoMi/AutoMergePublicNodes-Optimized@main/output/global.json
https://cdn.jsdelivr.net/gh/LeilaoMi/AutoMergePublicNodes-Optimized@main/output/all.txt
https://cdn.jsdelivr.net/gh/LeilaoMi/AutoMergePublicNodes-Optimized@main/output/all.yaml
```
转换链接见 `output/*.converter.md`。第三方转换服务可能不可用或记录订阅地址，优先使用本仓库直接生成的订阅文件。

---

## 流程概览

```text
订阅源配置
  → 异步抓取与重试
  → 多协议解析
  → 指纹去重 → GeoIP 标记 → SSRF 防投毒拦截
  → 质量预过滤 → TCP 预筛选 → 历史权重下采样
  → 轻量探活（100 并发只测 204，快速筛掉不可达节点）
  → sing-box 真实代理测试（50 并发，完整目标）
  → 综合评分排序输出
  → 生成健康报告、日报、源评分与清理建议
```

两阶段测试是性能关键：先用高并发探活把 3000 候选筛到 ~1000，再对剩余节点做完整真测，总耗时从 60+ 分钟降到 ~8 分钟。

完整真测包含：海外 204 检测、出口地理检测（cloudflare trace，避免 ipinfo 限流）、中国站点连通检测（baidu）、小文件下载测速、可疑低延迟过滤、Netflix/ChatGPT/Disney 解锁检测、DNS 泄露检测。

---

## 评分策略

节点排序不再只看单次延迟，而是使用 `config/scoring.yaml` 的综合评分。默认权重：

| 因子 | 默认权重 | 说明 |
|---|---:|---|
| `latency` | 25 | sing-box 真实代理测试延迟，越低越好 |
| `jitter` | 15 | 多目标测试抖动，越低越稳定 |
| `tcp` | 10 | TCP 预筛选延迟，用作基础可达性参考 |
| `speed` | 10 | 小文件下载测速，反映实际带宽 |
| `fingerprint_resistance` | 5 | 指纹抗识别评分，优先不易被识别的节点 |
| `protocol_history` | 15 | 协议历史通过率，降低长期低质协议权重 |
| `source_history` | 20 | 订阅源历史通过率，优先稳定来源 |

权重总和 100，便于分数解释和跨轮对比。配置校验会检查字段、阈值和默认值范围。

可选评分模板：

| 模板 | 适用场景 | 特点 |
|---|---|---|
| `config/scoring.yaml` | 默认均衡 | 兼顾延迟、抖动、TCP、协议历史和来源历史 |
| `config/scoring.low_latency.yaml` | 追求速度 | 提高 `latency` 权重，优先低延迟节点 |
| `config/scoring.stability.yaml` | 追求稳定 | 提高 `jitter` 和 `source_history` 权重，减少波动节点 |
| `config/scoring.source_quality.yaml` | 公开池噪声较高 | 强化订阅源和协议历史质量 |

本地运行时可指定模板：
```bash
python main.py --scoring-rules config/scoring.stability.yaml
```
CI 默认仍使用 `config/scoring.yaml`。如需切换默认策略，请修改 workflow 中的 `--scoring-rules`。

---

## 输出文件

| 文件 | 用途 |
|---|---|
| `verified.txt/yaml/json/urls` | 严格真测通过节点 |
| `global.txt/yaml/json/urls` | 海外可用的扩展节点 |
| `all.txt/yaml/json/urls` | 全量去重候选节点 |
| `chunks/verified_*.txt` | 分块订阅（每 100 节点一块，避免单文件过大） |
| `by_protocol/verified_*.txt` | 按协议分文件（vmess/vless/trojan/ss/hysteria2 独立订阅） |
| `by_region/{region}.txt/yaml/urls` | 按地区分文件（HK/JP/US/SG 等） |

| `stats.json` | 数量、耗时、协议通过率、错误明细、探活/真测阶段数据、节点速度和解锁状态 |
| `health_report.md` | 当前流水线健康报告，包含评分、来源质量、失败原因与输出保护 |
| `health_report.json` | 输出完整性、重复项、报警、源清理摘要 |
| `daily_report.md` | 面向人工阅读的每日摘要 |
| `source_scores.md` | 订阅源质量评分 |
| `scoring_profiles.md` | 评分模板权重、阈值和默认值对比 |
| `source_cleanup_suggestions.md/json` | 订阅源清理建议 |
| `source_discovery.json` | 从其他项目扫描发现的候选节点统计 |
| `node_stability.json` | 节点跨轮稳定性追踪（连续通过/失败计数） |
| `trend_history.json` | 最近 30 轮核心趋势 |
| `signature_manifest.json` | 输出文件签名清单（完整性校验） |
| `api_docs.json` | Open API 平台接口文档 |

健康状态说明：
- `ok`：输出结构正常，未发现关键报警。
- `warning`：输出可用，但存在低通过率协议、真测错误或源质量问题。
- `critical`：输出缺失、解析异常、`verified` 为 0 或核心结构不满足要求。

---

## 源维护

`config/sources.yaml` 维护公开订阅源。建议新增源前检查：
1. URL 可访问。
2. 能解析出有效节点。
3. 与现有源相比有去重贡献。
4. 大体量源设置 `max_nodes`。
5. 通过配置校验和回归测试。

清理建议默认只读：
```bash
python tools/suggest_source_cleanup.py \
  --output-dir output \
  --sources config/sources.yaml \
  --output output/source_cleanup_suggestions.md \
  --json-output output/source_cleanup_suggestions.json
```
如需应用禁用建议，必须显式确认：
```bash
python tools/suggest_source_cleanup.py \
  --output-dir output \
  --sources config/sources.yaml \
  --apply \
  --confirm-disable \
  --only source-a,source-b \
  --exclude source-b
```

---

## 本地运行

```bash
git clone https://github.com/LeilaoMi/AutoMergePublicNodes-Optimized.git
cd AutoMergePublicNodes-Optimized
pip install -r requirements.txt

# 下载 sing-box 后运行
python main.py --top-n 100 --test-limit 500
```

常用检查：
```bash
python -m compileall -q main.py core tools tests
python tools/import_contract.py
python tools/validate_config.py --sources config/sources.yaml --filter-rules config/filter_rules.yaml --scoring-rules config/scoring.yaml
python tools/doctor.py
python -m unittest -v tests.test_regressions
python tools/health_report.py --output-dir output --verified-prefix verified --output output/health_report.json
python tools/daily_report.py --output-dir output --output output/daily_report.md
python tools/source_scores_report.py --output-dir output --output output/source_scores.md
python tools/scoring_profiles_report.py --profiles 'config/scoring*.yaml' --output output/scoring_profiles.md
python tools/suggest_source_cleanup.py --output-dir output --sources config/sources.yaml --output output/source_cleanup_suggestions.md --json-output output/source_cleanup_suggestions.json
```

本地二次筛选：
```bash
python tools/local_filter.py --input output/global.urls --output-prefix local_verified --top-n 100
```

---

## GitHub Actions

- 自动运行：每 6 小时一次。
- 手动运行：`Actions → 更新节点 → Run workflow`。
- `top_n`：`verified.*` 输出上限，默认 300，最大 1000。
- `test_limit`：进入下采样的节点上限，默认 3000，最大 5000。
- `min_retain_ratio`：缩水守门比例，默认 0 表示关闭。
- 轻量探活：默认启用（`--lightweight-probe`），100 并发先筛不可达节点，再真测剩余。
- 真测并发：50（`--test-concurrency 50`），完整目标测试。
- 超时上限：30 分钟（`timeout-minutes: 30`）。

CI 会自动生成并上传调试产物：`stats.json`、`health_report.md`、`health_report.json`、`daily_report.md`、`source_scores.md`、`scoring_profiles.md`、`source_cleanup_suggestions.*`、`trend_history.json`。

---

## 项目结构

```text
AutoMergePublicNodes-Optimized/
├── main.py                         # 主流水线与 CLI
├── core/
│   ├── fetcher.py                  # 异步抓取、重试、jsDelivr/CDN 回退
│   ├── parser.py                   # 多协议解析（ss/ssr/vmess/vless/trojan/hysteria2/tuic/anytls/socks/http）
│   ├── tester.py                   # sing-box 真实代理测试（两阶段：轻量探活 + 完整真测）
│   ├── filtering.py                # 质量预过滤、同源降噪、SSRF 防投毒（拦截私有/元数据地址）
│   ├── sampling.py                 # 真测下采样与历史权重排序
│   ├── generator.py                # 多格式订阅输出（yaml/txt/json/urls，大文件紧凑）
│   ├── scoring.py                  # 综合节点评分（7 因子加权）
│   ├── _fingerprint_test.py        # 协议指纹抗检测评分（REALITY/uTLS/WS+TLS/端口加成）
│   ├── report.py                   # Markdown 健康报告
│   ├── readme_updater.py           # README 状态区自动更新
│   ├── stats.py                    # 源评分、趋势、节点稳定性追踪（EWMA 历史通过率）
│   └── geo.py                      # GeoIP 标记与缓存（ip-api.com 批量）
├── tools/
│   ├── audit_sources.py            # 源健康审计
│   ├── health_report.py            # 输出健康报告
│   ├── daily_report.py             # Markdown 日报
│   ├── source_scores_report.py     # 源质量评分报告
│   ├── scoring_profiles_report.py  # 评分模板对比报告
│   ├── suggest_source_cleanup.py   # 源清理建议与安全应用
│   ├── source_discovery.py         # 从其他项目发现新源
│   ├── discover_tg_channels.py     # Telegram 频道源发现
│   ├── validate_config.py          # 配置静态校验
│   ├── import_contract.py          # 导入契约检查（防悬空 import）
│   ├── doctor.py                   # 本地环境诊断
│   ├── local_filter.py             # 本地二次筛选
│   ├── actions_summary.py          # GitHub Actions 运行摘要
│   └── prepare_artifact_output.py  # 发布产物整理
├── config/                         # 源配置、过滤规则、评分模板
├── tests/                          # 回归测试与协议样例
├── output/                         # CI 输出文件（订阅 + 报告）
├── docs/                           # 使用指南、网关页面、发布说明
│   ├── index.html                  # 动态订阅网关（GitHub Pages）
│   ├── sources.html                # 订阅源健康面板
│   ├── client-guide.md             # 客户端导入指南
│   ├── resources.md                # 测速、转换和排障资源
│   └── releases/                   # 版本发布说明
├── CHANGELOG.md                    # 版本变更记录
└── .github/workflows/update.yml    # 自动更新流程（每 6 小时 + Pages）
```

---

## 文档

- [`docs/index.html`](https://leilaomi.github.io/AutoMergePublicNodes-Optimized/)：动态订阅网关（浏览器端筛选生成订阅）。
- [`docs/sources.html`](https://leilaomi.github.io/AutoMergePublicNodes-Optimized/sources.html)：订阅源健康面板。
- [`docs/client-guide.md`](docs/client-guide.md)：客户端导入指南。
- [`docs/resources.md`](docs/resources.md)：测速、转换和排障资源。
- [`docs/releases/`](docs/releases/)：版本发布说明索引。
- [`CHANGELOG.md`](CHANGELOG.md)：版本变更记录。

## License

MIT

## 致谢
- [sing-box](https://github.com/SagerNet/sing-box)
- 所有公开订阅源维护者与社区贡献者

<!-- AUTONODES_STATS_START -->
## 当前运行状态

| 指标 | 数值 |
| --- | --- |
| 更新时间 | 2026-06-22 05:06:41 |
| 版本 | 2.4.0 |
| 订阅源 | 105/107 |
| 原始节点 | 74096 |
| 去重后 | 22723 |
| TCP 可达 | 3000 |
| 真实可用 | 633 |
| 真测通过率 | 21.1% |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22723 |

> 输出保护：无。完整报告见 `output/health_report.md`、`output/stats.json`。

### Top 节点评分

| 评分 | 协议 | 延迟(ms) | 来源 |
| --- | --- | --- | --- |
| 79.68 | shadowsocks | 201.2 | Au1rxx-base64 |
| 79.4 | shadowsocks | 191.8 | Au1rxx-base64 |
| 79.39 | shadowsocks | 192.2 | Au1rxx-base64 |
| 78.58 | shadowsocks | 248.9 | Au1rxx-base64 |
| 78.45 | shadowsocks | 254.5 | Au1rxx-base64 |

### Top 来源质量

| 来源 | 评分 | 测试数 | 建议 |
| --- | --- | --- | --- |
| snakem982 | 0.991 | 69 | prefer |
| mheidari-all | 0.865 | 380 | prefer |
| Au1rxx-base64 | 0.797 | 108 | prefer |
| DeltaKronecker-all | 0.726 | 269 | prefer |
| Surfboard-tg-mixed | 0.373 | 5 | observe |

<!-- AUTONODES_STATS_END -->

