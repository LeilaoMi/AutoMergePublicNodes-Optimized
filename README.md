# AutoMergePublicNodes-Optimized

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.11+-blue)]()
[![Update Nodes](https://github.com/LeilaoMi/AutoMergePublicNodes-Optimized/actions/workflows/update.yml/badge.svg)](https://github.com/LeilaoMi/AutoMergePublicNodes-Optimized/actions/workflows/update.yml)

> 29 个社区源 · sing-box 真实代理测试 · 自动优选 · 多格式订阅输出 · CI 安全发布

⚠️ **声明：仅供学习研究。公开节点稳定性差，请自行甄别可用性与合规风险。**

---

## ✅ 普通用户怎么选

| 场景 | 推荐文件 | 说明 |
|---|---|---|
| Clash / Mihomo / Clash Meta | `output/verified.yaml` | 最推荐，真测通过后输出 |
| 想兼顾数量 | `output/global.yaml` / `output/global.txt` | 在严格真测基础上，额外纳入仅因百度连通失败、但海外 204 / 非 CN 出口 / 100KB 下载仍通过的节点 |
| v2rayN / 通用订阅 | `output/verified.txt` / `output/verified.urls` | base64 或 URL 列表 |
| Karing / sing-box | `output/verified.json` | sing-box JSON，已兼容新版 inbound 配置 |
| 自己客户端再测速 | `output/all.txt` / `output/all.urls` / `output/all.yaml` | 全量去重候选池，数量多、质量未保证 |
| 排障 / 看状态 | `output/health_report.json` / `output/stats.json` | 机器可读状态、报警、阶段耗时、错误明细 |

当前 verified 数量不是固定 100：`--top-n` 是上限；如果真测通过不足 100，只输出实际通过数量。

---

## 📦 订阅地址

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

### jsDelivr CDN

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

### 转换链接

- `output/verified.converter.md`
- `output/global.converter.md`
- `output/all.converter.md`

内置多个第三方订阅转换服务，可转换为 Clash / sing-box / V2Ray / Surge / Quantumult X / Loon / Shadowrocket 等格式。第三方转换服务可能不可用或记录 URL，优先使用本仓库直接生成的 `verified.yaml/json/txt`。

---

## 🔧 工作流程

```text
29 个社区订阅源
    ↓ 异步抓取（并发 30，重试 + CDN 回退）
    ↓ 多协议解析（vless / vmess / trojan / ss / ssr / hy2 / tuic / anytls / socks / http）
    ↓ 指纹去重（type | server | port | key）
    ↓ GeoIP 国旗映射（带缓存）
    ↓ 质量预过滤（端口黑名单 + server/protocol 降噪）
    ↓ TCP 预筛选（固定 worker 队列，避免海量协程）
    ↓ 协议基础探索 + 历史源/协议通过率加权下采样
    ↓ sing-box 真实代理测试
       - Google / YouTube 204
       - 出口地理检测
       - 中国站点连通性检测
       - 小文件下载测速
       - 可疑低延迟过滤
    ↓ 按真实延迟排序，取 Top N
    ↓ 输出 verified.*、global.*、all.*、converter、stats、health report
```

---

## ✨ 功能特性

### 节点测试

- **sing-box 真测**：不是只测 TCP 握手，而是实际通过节点访问测试目标。
- **多层验证**：204、geo、cn-block、speed 多维度判断。
- **可疑低延迟过滤**：默认拒绝 `<30ms` 的可疑节点，可用 `--min-latency 0` 关闭。
- **延迟 + 抖动**：verified tag 中标注延迟和 jitter。
- **失败原因聚合**：`stats.json` 输出 `real_test_errors` 与 `real_test_error_details`。

### 输出格式

- Clash / Mihomo YAML：`verified.yaml`、`global.yaml`、`all.yaml`
- sing-box / Karing JSON：`verified.json`、`global.json`、`all.json`
- V2Ray base64：`verified.txt`、`global.txt`、`all.txt`
- URL 列表：`verified.urls`、`global.urls`、`all.urls`
- 转换链接：`*.converter.md`

### 发布安全

- workflow 不再自动 fallback force push。
- `force_push` 手动输入已移除。
- rebase 冲突时直接失败，避免覆盖人工修改。
- `top_n` / `test_limit` 在 workflow 层有限制，避免误填导致 CI 超时。
- CI 失败时上传 debug artifact：`stats.json`、`source_audit.json`、`health_report.json`、converter 文件。
- jsDelivr purge 会记录 HTTP 状态，不再完全静默。

### 可观测性

- `health_report.json` 包含：
  - `ok`: 结构是否可用
  - `status`: `ok` / `warning` / `critical`
  - 输出文件完整性
  - 重复 tag/name
  - low pass 协议报警
  - real test 错误聚合
- `stats.json` 包含：
  - raw / dedup / tcp / real / verified / global 数量
  - protocol/source pass rate
  - `stage_durations` 阶段耗时
  - `real_test_error_details` 错误明细 Top 10
  - `all_output_mode`

### 仓库体积控制准备

默认仍保持 `all.*` 全格式输出，兼容旧订阅 URL。

如果后续要减少 `all.json/all.yaml` 大文件成本，可启用：

```bash
python main.py --all-output-mode light
# 或
AUTONODES_ALL_OUTPUT_MODE=light python main.py
```

light 模式下 `all.*` 只生成：

- `all.txt`
- `all.urls`
- `all.converter.md`

另有 `tools/prepare_artifact_output.py` 可把适合发布的 output 文件复制到独立目录，为后续 artifact/data 分支发布做准备；该脚本不执行 git 命令、不 push。

---

## ⚠️ 为什么 verified 有时很少

这是正常现象，不代表项目坏了：

1. 公共节点波动极大，很多源只是“能解析”，不代表能代理。
2. GitHub Actions 在美国机房测试，通过结果不等于你本地一定可用。
3. 本项目筛选比较严格：TCP 可达后还要经过 sing-box 真测。
4. `verified.*` 会要求百度连通；`global.*` 会额外纳入仅因百度连通失败、但海外 204、非 CN 出口和 100KB 下载仍通过的节点。
5. 会拒绝可疑低延迟节点，避免 Cloudflare 反代、假代理或异常链路混入。
6. 某些协议字段在不同客户端版本差异很大，配置不兼容会被剔除。

建议：质量优先导入 `verified.yaml/txt/json`；想兼顾数量可导入 `global.yaml/txt/json`；再在自己的客户端里重新测速。

---

## 🔄 触发更新

- 自动：GitHub Actions 每 6 小时运行。
- 手动：`Actions → Update Nodes → Run workflow`
  - `top_n`：verified 输出节点数上限，默认 300，workflow 限制最大 1000。
  - `test_limit`：送入真测的最大节点数，默认 1500，workflow 限制最大 3000。
  - `audit`：是否同时跑源审计。

---

## 🧪 本地运行

```bash
git clone https://github.com/LeilaoMi/AutoMergePublicNodes-Optimized.git
cd AutoMergePublicNodes-Optimized
pip install -r requirements.txt

# 下载 sing-box
VERSION=$(curl -fsSL https://api.github.com/repos/SagerNet/sing-box/releases/latest | jq -r '.tag_name')
VER_NUM="${VERSION#v}"
curl -fsSL -L -o sb.tar.gz "https://github.com/SagerNet/sing-box/releases/download/${VERSION}/sing-box-${VER_NUM}-linux-amd64.tar.gz"
tar -xzf sb.tar.gz
mv "sing-box-${VER_NUM}-linux-amd64/sing-box" ./sing-box
chmod +x ./sing-box

# 运行完整流水线
python main.py --top-n 100 --test-limit 500

# 只生成轻量 all 输出
python main.py --all-output-mode light
```

### 常用检查

```bash
python -m compileall -q main.py core tools tests
python -m unittest -v tests.test_regressions
python tools/health_report.py --output-dir output --verified-prefix verified --output output/health_report.json
```

当前回归测试覆盖：fetch timeout、测试不污染 output、workflow 安全逻辑、health status、sing-box 兼容、TCP worker 队列、下采样策略、light 输出模式、artifact 准备脚本、协议 fixture corpus。

---

## 📁 项目结构

```text
AutoMergePublicNodes-Optimized/
├── main.py                         # 主流水线 + CLI
├── core/
│   ├── fetcher.py                  # 异步抓取、重试、CDN 回退
│   ├── parser.py                   # 多协议解析
│   ├── tester.py                   # sing-box 真实代理测试
│   ├── generator.py                # Clash / sing-box / V2Ray / converter 输出
│   └── geo.py                      # GeoIP 国旗映射与缓存
├── tools/
│   ├── audit_sources.py            # 源健康审计
│   ├── health_report.py            # 输出健康报告
│   └── prepare_artifact_output.py  # artifact/data 分支输出准备
├── config/
│   └── sources.yaml                # 订阅源配置
├── tests/
│   ├── test_regressions.py         # 回归测试
│   └── fixtures/protocols/         # 协议 fixture corpus
├── output/                         # CI 生成输出
├── docs/
│   ├── audit-2026-06-04.md
│   └── staged-improvement-plan-2026-06-04.md
└── .github/workflows/update.yml
```

---

## 📖 文档

- [docs/audit-2026-06-04.md](docs/audit-2026-06-04.md) — 项目审计与改进建议
- [docs/staged-improvement-plan-2026-06-04.md](docs/staged-improvement-plan-2026-06-04.md) — 阶段推进记录

---

## License

MIT

## 致谢

- [sing-box](https://github.com/SagerNet/sing-box)
- 所有公开订阅源维护者与社区贡献者
