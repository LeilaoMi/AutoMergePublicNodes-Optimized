# Changelog

All notable changes to this project will be documented in this file.

Release notes index: [`docs/releases/`](docs/releases/)

## 2.9.0 - 2026-06-16

### ✨ Features

- **联邦式测试网络 (Federated Test Network)**: `core/_federated_test_network.py`
  - 贡献者注册与信誉系统
  - 测试任务分发与负载均衡
  - 结果聚合与共识验证
  - 地区覆盖统计

- **社区驱动系统 (Community Driven System)**: `core/_community_driven.py`
  - 成员注册与信誉管理
  - 节点提交与审批流程
  - 投票机制与质量评估
  - 贡献者排行榜

- **节点质量地图 (Node Quality Map)**: `core/_quality_map.py`
  - 地区级质量统计（平均分、延迟、抖动）
  - 协议级质量分析
  - 质量分布可视化数据（S/A/B/C/D 等级）
  - 最佳/最差地区识别

- **自适应学习系统 (Adaptive Learning Engine)**: `core/_adaptive_learning.py`
  - 评分权重自动优化建议
  - 测试采样策略改进建议
  - 过滤规则学习
  - 性能预测与趋势分析

### 🔧 Technical

- 所有模块集成至 `main.py` 流水线，生成完整统计报告
- 统一使用 `scored_valid` 数据结构（7元组）
- 支持持久化状态存储（JSON格式）
- 所有功能模块支持优雅降级（失败不影响主流程）

### 🧪 Tests

- 新增 `tests/test_v27_v29_features.py`：25个测试用例覆盖所有新模块
- 使用 Mock 对象进行单元测试，无需真实网络环境

---

## 2.8.0 - 2026-06-16

### ✨ Features

- **使用场景优化 (Use Case Optimizer)**: `core/_use_case_optimizer.py`
  - 4种预定义场景：流媒体、游戏、下载、工作
  - 场景特定评分权重（延迟/速度/稳定性/解锁能力）
  - 硬性要求过滤（最低速度、最大延迟等）
  - 智能推荐与匹配原因说明

- **个性化智能推荐 (Personalized Recommender)**: `core/_personalized_recommender.py`
  - 用户偏好学习与画像构建
  - 基于历史行为的评分调整
  - 协议/地区/稳定性偏好权重
  - 置信度评估（最低样本要求）

- **开放API平台 (Open API Platform)**: `core/_open_api_platform.py`
  - 8个RESTful API端点（节点查询、统计、推荐、反馈等）
  - API Key管理与权限控制（read/write/admin）
  - 速率限制（每分钟请求上限）
  - 自动生成API文档（JSON格式）

- **智能故障转移 (Smart Failover Manager)**: `core/_smart_failover.py`
  - 5级降级策略（历史路径→同提供商→同地区→同协议→任意可用）
  - 故障转移链构建（最多5个备选节点）
  - 历史成功路径学习
  - 转移记录与统计分析

- **数据洞察服务 (Data Insight Service)**: `core/_data_insight_service.py`
  - 历史运行数据记录（最多60轮）
  - 异常检测（节点数量骤降、降级模式、运行时间异常）
  - 趋势分析（通过率、延迟变化）
  - 智能建议生成

### 🔧 Technical

- 所有模块集成至 `main.py`，在流水线末尾执行
- 输出文件：`api_docs.json`、`api_state.json`、`failover_history.json`、`insight_history.json`、`user_preferences.json`

---

## 2.7.0 - 2026-06-16

### ✨ Features

- **节点DNA分析系统 (Node DNA Analysis)**: `core/_node_dna.py`
  - 提供商识别（基于IP段前3段聚类）
  - 多样性评分（赫芬达尔-赫希曼指数 HHI）
  - 集中度风险评估（low/medium/high）
  - 主导提供商识别（占比>30%）
  - 优化建议生成

### 🔧 Technical

- 集成至 `main.py` 流水线，分析验证通过的节点池
- 输出 `node_dna` 统计至 `stats.json`

---

## 2.5.1 - 2026-06-16

### 🐛 Bug Fixes

- **fingerprint_resistance 类型不匹配修复**: `TestResult` 新增 `fingerprint_resistance_score` 浮点字段（0~1），`tester.py` 从 `_fingerprint_test.py` 同时存储字符串等级和数值分数，`main.py` 读取数值版传入 `ScoreInput`
- **ScoringConfig 默认权重更新**: `latency` 从 30→25，腾出 5% 给新增的 `fingerprint_resistance` 因子

### ✨ Features

- **指纹对抗评分纳入综合评分**: `scoring.py` 新增 `fingerprint_resistance` 权重（默认 5%），REALITY 协议节点自动获得加分，无 TLS 节点自动降分
- **DNS 泄漏惩罚**: `main.py` 评分循环中检测到 `dns_leak=True` 的节点扣 3 分
- **缓存版本控制**: `_incremental_cache.py` 新增 `SCHEMA_VERSION`，版本不匹配时自动失效旧缓存
- **generator._flag_to_cc 统一委托**: 不再重复定义，改为调用 `core.geo._flag_to_cc`
- **4 套评分模板全部更新**: `scoring*.yaml` 均加入 `fingerprint_resistance` 权重和 `missing_fingerprint_score` 默认值
- **validate_config 白名单更新**: `tools/validate_config.py` 接受 `fingerprint_resistance` 权重和 `missing_fingerprint_score` 默认值
- **版本号升级至 2.5.1**

### 🧪 Tests

- 新增 48 个 v2.5.1 回归测试（`test_v25_features.py`）
  - `TestFingerprintScoring` (7): ScoreInput 字段、breakdown 因子、满分/零分/缺失值
  - `TestDNSLeakPenalty` (4): TestResult 字段、扣分逻辑
  - `TestIncrementalCache` (+2): 版本号写入、版本不匹配自动失效
  - `TestValidateConfigSpeed` 重构为 4 个测试：覆盖 fingerprint_resistance 权重/默认值/总和警告

---

## 2.5.0 - 2026-06-16

### 🚀 Performance

- **Incremental Test Caching**: `core/_incremental_cache.py` — skips retesting unchanged nodes, expected 50-60% CI time reduction.
- **latency_history LRU eviction**: auto-prune to 2000 nodes max, preventing unbounded file growth.

### 🔒 Security

- **Tag injection sanitization**: `generator._sanitize_tag()` strips control chars from node tags.
- **DNS leak detection**: compares exit IP vs DNS resolver IP during real proxy test.
- **Fingerprint resistance analysis**: `core/_fingerprint_test.py` — classifies REALITY/uTLS/WS+TLS/plain TLS/no TLS.

### ✨ Features

- **Speed scoring factor**: `speed_kbps` now participates in scoring (weight 10%).
- **Time-aware scoring**: `core/_time_aware.py` — adjusts scores by CST time slot + region.
- **Lifetime prediction**: `core/_lifetime_predictor.py` — linear regression on latency trend.
- **ASN-based GeoIP**: replaces hardcoded Cloudflare IP prefixes with ASN lookup.
- **Structured logging module**: `core/_logging.py`.

### 🐛 Bug Fixes

- **socks/http fingerprint collision**: `_key()` now includes credentials for socks/http.
- **Stability bonus no-op**: was `min(3.0, 0)`, now properly scales with consecutive passes.
- **Netflix deep detection**: checks response body, not just HTTP status code.
- **ChatGPT deep detection**: checks for geo-block keywords in response.
- **204 outlier penalty**: max sample >5× median and >500ms triggers penalty.
- **sing-box inline fallback rules**: domestic domains/IPs always go direct.

### 📊 Stats Enrichment

- `top_scores[]` now includes `fingerprint_resistance`, `dns_leak`.
- Root stats includes `incremental_cache_reused`, `time_slot`, `lifetime_predictions`.

### ⚠️ Breaking

- Scoring YAML configs now require `speed` weight + `excellent_speed_kbps`/`bad_speed_kbps` thresholds.

---

## 2.4.0 - 2026-06-14

### Added

- Added chunked output: `output/chunks/verified_*.txt` splits verified nodes into 100-per-file blocks.
- Added protocol-split output: `output/by_protocol/verified_*.txt` separates nodes by protocol type.
- Added node stability tracking: `output/node_stability.json` records per-fingerprint consecutive pass/fail history.
- Added Netflix and ChatGPT unlock detection in test results (non-blocking, informational).
- Added download speed quantification: `speed_kbps` field in `stats.json` top scores.
- Added 204 latency triple-sampling with median for improved accuracy.
- Added source discovery tool `tools/source_discovery.py` scanning 6 high-star projects.
- Added CI failure notification via auto-created Issue with `ci-failure` label.
- Added CI recovery auto-close of `ci-failure` Issues with comment.
- Added graceful degradation: TCP fallback when real-test yields 0 passing nodes.
- Added sing-box download fallback to older versions on download failure.
- Added GitHub Issue template for community source contributions.
- Added Cloudflare Worker acceleration documentation `docs/cloudflare-worker-setup.md`.
- Added full competitive analysis `docs/competitive-analysis-2026-06-14.md` covering 33 projects.
- Added `degraded_mode` field to `stats.json`.

### Changed

- TestResult dataclass extended with `speed_kbps`, `netflix_ok`, `chatgpt_ok` fields.
- Workflow purges chunks/ and by_protocol/ directories via jsDelivr.
- Workflow artifacts include `source_discovery.json` and `node_stability.json`.
- Version bumped to 2.4.0.

## 2.3.0 - 2026-06-12

Detailed release notes: [`docs/releases/2.3.0.md`](docs/releases/2.3.0.md)

### Added

- Added configurable weighted node scoring via `config/scoring.yaml`.
- Added scoring profile templates:
  - `config/scoring.low_latency.yaml`
  - `config/scoring.stability.yaml`
  - `config/scoring.source_quality.yaml`
- Added score breakdown output for Top nodes in `output/stats.json`.
- Added score breakdown columns to `output/health_report.md`.
- Added `tools/scoring_profiles_report.py` to generate `output/scoring_profiles.md`.
- Added GitHub Actions Summary output with run overview, scoring weights, Top node scores, source quality, errors, output guard, and links.
- Added README auto status block maintained by `core/readme_updater.py`.
- Added scoring configuration validation and non-blocking weight-sum warnings.
- Added regression tests for scoring config, scoring breakdown, scoring profiles, health report, and Actions Summary.

### Changed

- Output ranking now uses comprehensive score first and latency as tie-breaker instead of pure latency sorting.
- GitHub Actions validates all `config/scoring*.yaml` profiles.
- GitHub Actions publishes `output/health_report.md` and `output/scoring_profiles.md` as debug artifacts and jsDelivr-purged outputs.
- README now documents scoring strategy, scoring profile usage, and observability outputs.

### Fixed

- Fixed programmatic `run(args)` compatibility when `args.scoring_rules` is missing.
- Avoided blocking CI when scoring weight sum is not exactly 100; it now emits a warning only.

### Notes

- The real proxy test still decides whether a node is usable. Scoring only ranks usable nodes.
- `config/scoring.yaml` remains the default CI scoring profile.
- README auto status data is generated by scheduled workflow runs and may lag behind the latest code version until the next run.

## 2.2.0 - 2026-06-11

### Added

- Added weighted scoring foundation for tested nodes.
- Added Markdown health report generation via `core/report.py`.
- Added `top_scores` to runtime stats.

### Changed

- Real-test successful nodes are sorted by weighted score, with latency as tie-breaker.
