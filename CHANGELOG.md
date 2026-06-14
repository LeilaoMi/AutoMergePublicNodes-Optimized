# 变更记录

本项目所有重要变更将记录在此文件中。

发布说明索引：[`docs/releases/`](docs/releases/)

## 2.4.0 - 2026-06-14

### 新增

- 新增分块输出：`output/chunks/verified_*.txt`，每 100 个节点一个文件，避免单文件过大被 CDN 缓存卡住。
- 新增协议分文件输出：`output/by_protocol/verified_*.txt`，按 vmess/vless/trojan/ss 等协议类型独立输出订阅。
- 新增节点稳定性追踪：`output/node_stability.json`，记录每个节点指纹的跨轮连续通过/失败历史，最多追踪 5000 个。
- 新增 Netflix 和 ChatGPT 解锁检测，在测试结果中记录（不影响通过/失败判定，仅记录能力）。
- 新增下载速度量化：`stats.json` 的 Top 节点新增 `speed_kbps` 字段。
- 新增 204 延迟三次采样取中位数，提高延迟测量精度。
- 新增源发现工具 `tools/source_discovery.py`，扫描 6 个高 star 项目的候选节点。
- 新增 CI 失败自动创建 Issue（标签 `ci-failure`），CI 恢复后自动关闭并评论。
- 新增优雅降级：真测 0 通过时自动回退到 TCP 可达节点，避免用户订阅变空。
- 新增 sing-box 下载失败时自动回退到旧版本。
- 新增 GitHub Issue 模板，方便社区贡献新订阅源。
- 新增 Cloudflare Worker 订阅加速方案文档 `docs/cloudflare-worker-setup.md`。
- 新增全量对标分析报告 `docs/competitive-analysis-2026-06-14.md`，覆盖 33 个同类项目。
- `stats.json` 新增 `degraded_mode` 字段标记是否降级运行。

### 变更

- `TestResult` 数据类新增 `speed_kbps`、`netflix_ok`、`chatgpt_ok` 字段。
- workflow 的 jsDelivr 缓存清理覆盖 `chunks/` 和 `by_protocol/` 目录。
- workflow 的调试产物包含 `source_discovery.json` 和 `node_stability.json`。
- 版本升级至 2.4.0。

## 2.3.0 - 2026-06-12

详细发布说明：[`docs/releases/2.3.0.md`](docs/releases/2.3.0.md)

### 新增

- 新增可配置加权评分系统 `config/scoring.yaml`，支持延迟、抖动、TCP、协议历史和来源历史五因子加权。
- 新增三套评分模板：`config/scoring.low_latency.yaml`（低延迟优先）、`config/scoring.stability.yaml`（稳定性优先）、`config/scoring.source_quality.yaml`（来源质量优先）。
- `output/stats.json` 新增 Top 节点评分分项拆解 `score_breakdown`。
- `output/health_report.md` 新增评分分项列（延迟分、抖动分、TCP 分、协议历史分、来源历史分）。
- 新增 `tools/scoring_profiles_report.py` 生成 `output/scoring_profiles.md` 评分模板对比报告。
- 新增 GitHub Actions Summary 输出，包含运行概览、评分权重、Top 节点评分分项、来源质量、错误统计、输出保护和链接。
- 新增 README 自动状态区，由 `core/readme_updater.py` 维护。
- 新增评分配置校验和权重总和非 100 时的非阻断式警告。
- 新增回归测试覆盖评分配置、评分分项拆解、评分模板、健康报告和 Actions Summary。

### 变更

- 输出排序改为综合评分优先，延迟作为同分兜底，不再是纯延迟排序。
- GitHub Actions 校验所有 `config/scoring*.yaml` 评分模板。
- GitHub Actions 发布 `output/health_report.md` 和 `output/scoring_profiles.md` 作为调试产物和 jsDelivr 缓存清理对象。
- README 新增评分策略说明、评分模板用法和可观测输出文档。

### 修复

- 修复 `run(args)` 在 `args.scoring_rules` 缺失时的兼容性问题。
- 评分权重总和不等于 100 时不再阻断 CI，改为仅输出警告。

### 注意事项

- 真实代理测试仍然决定节点是否可用，评分仅排序可用节点。
- `config/scoring.yaml` 保持为 CI 默认评分模板。
- README 自动状态数据由定时 workflow 运行生成，可能滞后于最新代码版本。

## 2.2.0 - 2026-06-11

### 新增

- 新增加权评分基础，用于真测通过的节点排序。
- 新增 Markdown 健康报告生成 `core/report.py`。
- 运行时统计新增 `top_scores` 字段。

### 变更

- 真测成功节点按加权评分排序，延迟作为同分兜底。
