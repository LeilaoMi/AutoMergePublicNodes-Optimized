# AutoMergePublicNodes-Optimized

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.11+-blue)]()
[![更新节点](https://github.com/LeilaoMi/AutoMergePublicNodes-Optimized/actions/workflows/update.yml/badge.svg)](https://github.com/LeilaoMi/AutoMergePublicNodes-Optimized/actions/workflows/update.yml)

> 自动聚合公开代理订阅源，使用 sing-box 真实代理测试，输出可直接导入主流客户端的订阅文件，并生成健康报告、源评分与清理建议。

> 仅供学习研究。公开节点稳定性不可控，请自行评估可用性与合规风险。

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
  → 指纹去重
  → GeoIP 标记
  → 质量预过滤
  → TCP 预筛选
  → 历史权重下采样
  → [4.5] 轻量探活（100 并发只测 204，快速筛掉不可达节点）
  → [5] sing-box 真实代理测试（50 并发，完整目标）
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
| `by_capability/{cap}.txt/yaml/urls` | 按解锁能力分文件（netflix/chatgpt/disney 等） |
| `recommended/clash.yaml` | 推荐 Clash 配置（精选节点 + 分组规则） |
| `recommended/singbox.json` | 推荐 sing-box 配置 |
| `recommended/mobile.yaml` | 移动端推荐配置 |
| `recommended/streaming.yaml` | 流媒体推荐配置 |
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
python tools/suggest_source_cleanup.py   --output-dir output   --sources config/sources.yaml   --output output/source_cleanup_suggestions.md   --json-output output/source_cleanup_suggestions.json
```

如需应用禁用建议，必须显式确认：

```bash
python tools/suggest_source_cleanup.py   --output-dir output   --sources config/sources.yaml   --apply   --confirm-disable   --only source-a,source-b   --exclude source-b
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
- 超时上限：15 分钟（`timeout-minutes: 15`）。

CI 会自动生成并上传调试产物：`stats.json`、`health_report.md`、`health_report.json`、`daily_report.md`、`source_scores.md`、`scoring_profiles.md`、`source_cleanup_suggestions.*`、`trend_history.json`。

---

## 项目结构

```text
AutoMergePublicNodes-Optimized/
├── main.py                         # 主流水线与 CLI
├── core/
│   ├── fetcher.py                  # 异步抓取、重试、CDN 回退
│   ├── parser.py                   # 多协议解析
│   ├── tester.py                   # sing-box 真实代理测试（两阶段：探活 + 真测）
│   ├── filtering.py                # 质量预过滤与同源降噪
│   ├── sampling.py                 # 真测下采样与历史权重排序
│   ├── generator.py                # 多格式订阅输出（含分块/按协议/按地区/按能力切片）
│   ├── scoring.py                  # 综合节点评分（7 因子加权）
│   ├── report.py                   # Markdown 健康报告
│   ├── readme_updater.py           # README 状态区自动更新
│   ├── stats.py                    # 源评分、趋势与报警统计（EWMA 历史通过率）
│   ├── geo.py                      # GeoIP 标记与缓存
│   ├── _incremental_cache.py       # [v2.5] 增量测试缓存，跳过未变更节点
│   ├── _latency_trend.py           # [v2.5] 节点延迟趋势持久化与告警
│   ├── _lifetime_predictor.py      # [v2.5] 节点剩余寿命预测
│   ├── _time_aware.py              # [v2.5] 时段感知评分加成
│   ├── _recommended_configs.py     # [v2.5] 推荐配置生成（Clash/sing-box/移动端/流媒体）
│   ├── _tester_concurrency.py      # [v2.5] 进程池/IO 并发解耦层
│   ├── _logging.py                 # [v2.5] 结构化日志
│   ├── _fingerprint_test.py        # [v2.6] 指纹抗识别检测
│   ├── _self_healing.py            # [v2.6] 流水线自愈（源失败自动降级/重试）
│   ├── _predictive_monitoring.py   # [v2.6] 预测性监控（提前识别风险节点）
│   ├── _smart_failover.py          # [v2.6] 智能故障转移链生成
│   ├── _node_dna.py                # [v2.7] 节点 DNA 分析（特征聚类）
│   ├── _use_case_optimizer.py      # [v2.8] 使用场景优化器
│   ├── _personalized_recommender.py# [v2.8] 个性化推荐
│   ├── _data_insight_service.py    # [v2.8] 数据洞察服务
│   ├── _quality_map.py             # [v2.9] 节点质量地图（地区/协议级统计）
│   ├── _adaptive_learning.py       # [v2.9] 自适应学习引擎（权重/采样/过滤优化建议）
│   ├── _community_driven.py        # [v2.9] 社区驱动系统（需外部成员参与）
│   ├── _federated_test_network.py  # [v2.9] 联邦测试网络（需外部贡献者参与）
│   ├── _open_api_platform.py       # [v2.9] Open API 平台（接口文档生成）
│   └── _test_farm_client.py        # [v2.9] 测试农场客户端（接口已定义，待实施）
├── tools/
│   ├── audit_sources.py            # 源健康审计
│   ├── health_report.py            # 输出健康报告
│   ├── daily_report.py             # Markdown 日报
│   ├── source_scores_report.py     # 源质量评分报告
│   ├── scoring_profiles_report.py  # 评分模板对比报告
│   ├── source_discovery.py         # 从其他项目发现新源
│   ├── suggest_source_cleanup.py   # 源清理建议与安全应用
│   ├── source_proposal_validator.py# 新源提案验证
│   ├── validate_config.py          # 配置静态校验
│   ├── doctor.py                   # 本地环境诊断
│   ├── local_filter.py             # 本地二次筛选
│   ├── notify.py                   # Telegram/Webhook 通知
│   ├── sign_output.py              # 输出文件签名
│   ├── actions_summary.py          # GitHub Actions 运行摘要
│   └── prepare_artifact_output.py  # 发布产物整理
├── config/                         # 源配置与过滤规则
├── tests/                          # 回归测试（221 用例）与协议样例
├── output/                         # CI 输出文件
├── docs/                           # 使用指南、资源与历史报告
├── CHANGELOG.md                    # 版本变更记录
└── .github/workflows/update.yml    # 自动更新流程
```

> 标注 `[v2.9]` 的社区驱动/联邦测试网络/测试农场需要外部用户或基础设施参与，单仓库运行时这些模块的统计字段为 0，不影响主流程。

---

## 文档

- [`docs/client-guide.md`](docs/client-guide.md)：客户端导入指南。
- [`docs/resources.md`](docs/resources.md)：测速、转换和排障资源。
- [`docs/reports/`](docs/reports/)：历史审查与复核报告。
- [`docs/cloudflare-worker-setup.md`](docs/cloudflare-worker-setup.md)：Cloudflare Worker 订阅加速方案。
- [`docs/competitive-analysis-2026-06-14.md`](docs/competitive-analysis-2026-06-14.md)：33 个同类项目全量对标分析。
- [`CHANGELOG.md`](CHANGELOG.md)：版本变更记录。
- [`docs/releases/`](docs/releases/)：版本发布说明索引，包含 2.3.0 等用户向发布说明。

## License

MIT

## 致谢

- [sing-box](https://github.com/SagerNet/sing-box)
- 所有公开订阅源维护者与社区贡献者

<!-- AUTONODES_STATS_START -->
## 当前运行状态

| 指标 | 数值 |
| --- | --- |
| 更新时间 | 2026-06-18 04:21:59 |
| 版本 | 2.9.1 |
| 订阅源 | 44/44 |
| 原始节点 | 67675 |
| 去重后 | 22191 |
| TCP 可达 | 799 |
| 真实可用 | 618 |
| 真测通过率 | 77.3% |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22191 |

> 输出保护：无。完整报告见 `output/health_report.md`、`output/stats.json`。

### Top 节点评分

| 评分 | 协议 | 延迟(ms) | 来源 |
| --- | --- | --- | --- |
| 77.88 | trojan | 256.1 | Surfboard-tg-mixed |
| 77.09 | shadowsocks | 227.4 | Au1rxx-base64 |
| 76.98 | shadowsocks | 232.5 | Au1rxx-base64 |
| 76.84 | shadowsocks | 238.3 | Au1rxx-base64 |
| 75.91 | shadowsocks | 278.5 | Au1rxx-base64 |

### Top 来源质量

| 来源 | 评分 | 测试数 | 建议 |
| --- | --- | --- | --- |
| snakem982 | 0.966 | 25 | prefer |
| Surfboard-tg-mixed | 0.941 | 350 | prefer |
| mheidari-all | 0.837 | 216 | prefer |
| Au1rxx-base64 | 0.817 | 83 | prefer |
| DeltaKronecker-all | 0.58 | 112 | observe |

<!-- AUTONODES_STATS_END -->

