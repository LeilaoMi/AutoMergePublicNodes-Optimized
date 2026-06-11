# AutoMergePublicNodes-Optimized

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.11+-blue)]()
[![节点更新](https://github.com/LeilaoMi/AutoMergePublicNodes-Optimized/actions/workflows/update.yml/badge.svg)](https://github.com/LeilaoMi/AutoMergePublicNodes-Optimized/actions/workflows/update.yml)

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
| 查看状态 | `output/daily_report.md` / `output/health_report.md` / `output/health_report.json` / `output/source_scores.md` / `output/source_cleanup_suggestions.md` | 日报、健康报告、源评分、清理建议 |

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
  → sing-box 真实代理测试
  → 综合评分排序输出
  → 生成健康报告、日报、源评分与清理建议
```

真实测试包含：海外 204 检测、出口地理检测、中国站点连通检测、小文件下载测速、可疑低延迟过滤。

---

## 评分策略

节点排序不再只看单次延迟，而是使用 `config/scoring.yaml` 的综合评分。默认权重：

| 因子 | 默认权重 | 说明 |
|---|---:|---|
| `latency` | 35 | sing-box 真实代理测试延迟，越低越好 |
| `jitter` | 15 | 多目标测试抖动，越低越稳定 |
| `tcp` | 10 | TCP 预筛选延迟，用作基础可达性参考 |
| `protocol_history` | 20 | 协议历史通过率，降低长期低质协议权重 |
| `source_history` | 20 | 订阅源历史通过率，优先稳定来源 |

配置校验会检查字段、阈值和默认值范围。权重总和不等于 100 时只给 warning，不阻断 CI；建议保持 100，便于分数解释和跨轮对比。

---

## 输出文件

| 文件 | 用途 |
|---|---|
| `verified.txt/yaml/json/urls` | 严格真测通过节点 |
| `global.txt/yaml/json/urls` | 海外可用的扩展节点 |
| `all.txt/yaml/json/urls` | 全量去重候选节点 |
| `stats.json` | 数量、耗时、协议通过率、错误明细、缩水守门结果 |
| `health_report.md` | 当前流水线健康报告，包含评分、来源质量、失败原因与输出保护 |
| `health_report.json` | 输出完整性、重复项、报警、源清理摘要 |
| `daily_report.md` | 面向人工阅读的每日摘要 |
| `source_scores.md` | 订阅源质量评分 |
| `source_cleanup_suggestions.md/json` | 订阅源清理建议 |
| `trend_history.json` | 最近 30 轮核心趋势 |

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
python tools/suggest_source_cleanup.py --output-dir output --sources config/sources.yaml --output output/source_cleanup_suggestions.md --json-output output/source_cleanup_suggestions.json
```

本地二次筛选：

```bash
python tools/local_filter.py --input output/global.urls --output-prefix local_verified --top-n 100
```

---

## GitHub Actions

- 自动运行：每 6 小时一次。
- 手动运行：`Actions → 节点更新 → Run workflow`。
- `top_n`：`verified.*` 输出上限，默认 300，最大 1000。
- `test_limit`：进入真测的节点上限，默认 1500，最大 3000。
- `min_retain_ratio`：缩水守门比例，默认 0 表示关闭。

CI 会自动生成并上传调试产物：`stats.json`、`health_report.md`、`health_report.json`、`daily_report.md`、`source_scores.md`、`source_cleanup_suggestions.*`、`trend_history.json`。

---

## 项目结构

```text
AutoMergePublicNodes-Optimized/
├── main.py                         # 主流水线与 CLI
├── core/
│   ├── fetcher.py                  # 异步抓取、重试、CDN 回退
│   ├── parser.py                   # 多协议解析
│   ├── tester.py                   # sing-box 真实代理测试
│   ├── filtering.py                # 质量预过滤与同源降噪
│   ├── sampling.py                 # 真测下采样与历史权重排序
│   ├── generator.py                # 多格式订阅输出
│   ├── scoring.py                  # 综合节点评分
│   ├── report.py                   # Markdown 健康报告
│   ├── readme_updater.py           # README 状态区更新
│   ├── stats.py                    # 源评分、趋势与报警统计
│   └── geo.py                      # GeoIP 标记与缓存
├── tools/
│   ├── audit_sources.py            # 源健康审计
│   ├── health_report.py            # 输出健康报告
│   ├── daily_report.py             # Markdown 日报
│   ├── source_scores_report.py     # 源质量评分报告
│   ├── suggest_source_cleanup.py   # 源清理建议与安全应用
│   ├── validate_config.py          # 配置静态校验
│   ├── doctor.py                   # 本地环境诊断
│   ├── local_filter.py             # 本地二次筛选
│   └── prepare_artifact_output.py  # 发布产物整理
├── config/                         # 源配置与过滤规则
├── tests/                          # 回归测试与协议样例
├── output/                         # CI 输出文件
├── docs/                           # 使用指南、资源与历史报告
└── .github/workflows/update.yml    # 自动更新流程
```

---

## 文档

- [`docs/client-guide.md`](docs/client-guide.md)：客户端导入指南。
- [`docs/resources.md`](docs/resources.md)：测速、转换和排障资源。
- [`docs/reports/`](docs/reports/)：历史审查与复核报告。

## License

MIT

## 致谢

- [sing-box](https://github.com/SagerNet/sing-box)
- 所有公开订阅源维护者与社区贡献者

<!-- AUTONODES_STATS_START -->
## 当前运行状态

| 指标 | 数值 |
| --- | --- |
| 更新时间 | 2026-06-11 23:58:32 |
| 版本 | 2.2.0 |
| 订阅源 | 44/44 |
| 原始节点 | 39955 |
| 去重后 | 15027 |
| TCP 可达 | 1500 |
| 真实可用 | 316 |
| 真测通过率 | 21.1% |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 15027 |

> 输出保护：无。完整报告见 `output/health_report.md`、`output/stats.json`。

### Top 节点评分

| 评分 | 协议 | 延迟(ms) | 来源 |
| --- | --- | --- | --- |
| 57.66 | shadowsocks | 439.9 | Au1rxx-base64 |
| 57.57 | shadowsocks | 439.9 | Au1rxx-base64 |
| 57.51 | shadowsocks | 441.9 | Au1rxx-base64 |
| 57.19 | shadowsocks | 221.6 | Au1rxx-base64 |
| 56.71 | shadowsocks | 236.5 | Au1rxx-base64 |

### Top 来源质量

| 来源 | 评分 | 测试数 | 建议 |
| --- | --- | --- | --- |
| snakem982 | 0.958 | 43 | prefer |
| Au1rxx-base64 | 0.524 | 71 | observe |
| mheidari-all | 0.303 | 92 | observe |
| roosterkid-openproxylist-v2ray | 0.296 | 29 | observe |
| Surfboard-tg-mixed | 0.28 | 752 | observe |

<!-- AUTONODES_STATS_END -->

