# Changelog

本项目所有 notable 变更记录于此。按时间倒序排列。

## 2026-10-16 国内检查缓存、守门与 Pages 测速

- 国内检查结果跨轮缓存（`china_cache.json`，放在 data 分支）：可达结果 12 小时、不可达 24 小时内直接复用，额度用来检查排名更靠后的节点。
- 国内检查完全失败（GlobalPing 故障或额度用完）时，verified 保留上一轮，不再把未经国内验证的海外结果发布成 verified。
- CI 缩水守门默认从 0（关闭）改为 0.5；连续保留上限 3 轮，避免真实缩水时一直发布旧节点。
- 明文 HTTP/SOCKS 代理（无 TLS）不再进入 verified/global。
- Pages：删除"网关连通性测速"。它实际请求的是 speed.cloudflare.com，测不到节点本身。改为显示 CI 实测结果（国内可达 / 海外可用和延迟），新增"只看 CI 实测通过""只看国内可达"筛选和按实测延迟排序。

## 2026-10-16 改写历史：移除 output/ 的历史版本

- 已从 `main` 的全部历史中删除 `output/` 目录（这些是每轮自动生成的产物），代码、文档、配置的历史完整保留，当前产物另作为一个提交恢复。仓库克隆体积从约 1.5 GB 降到约 20 MB。
- 所有提交 SHA 已变化。fork 或本地克隆请执行 `git fetch origin && git reset --hard origin/main`（会丢弃本地改动，请先备份），或者重新 fork。
- 改写前的 `main` 保留在 `refs/backup/main-pre-rewrite`（默认克隆不会拉取）。

## 2026-10-16 大文件迁到 data 分支

- `all.*`（约 30 MB）、`geo_cache.json`、`node_stability.json`、`score_details.json` 不再提交到 `main`，改为每轮以**单个孤立提交强推到 `data` 分支**。`main` 每轮新增从约 35 MB 降到约 1 MB，`data` 分支始终只有一个提交。
- CI 开跑前从 `data` 分支恢复 `geo_cache.json` / `node_stability.json`。迁移后的第一轮 `data` 分支还不存在，沿用 `main` 里的旧副本。
- **订阅地址变化**：`verified.*` / `global.*` 不变；`all.*` 改为 `.../AutoMergePublicNodes-Optimized@data/output/all.yaml`（raw 为 `.../data/output/all.yaml`）。Pages 网关已同步修改。
- `main` 已有的约 1.5 GB 历史不在本次处理范围（需要改写历史并强推）。

## 2026-10-16 国内检查、评分与测试器修复

### 🐛 产出修复
- `global.*` 改为基于全部海外真测通过节点构建。此前国内检查把不可达节点从 `valid` 中剔除后，`global.*` 也跟着丢失这些节点（上一轮 471 个真测通过，global 只剩 106 个）。
- 国内检查（GlobalPing）改为三态：可达 / 实测不可达 / 未知。额度用完、探针离线、超时都记为"未知"，不再当作不可达。
- 先查 `/v1/limits` 的剩余额度，按"剩余 - 预留 20"收缩预算，单轮最多检查 200 个（`--china-check-max`），按评分顺序优先检查。遇到 429 立即停止创建测量。匿名额度为每 IP 每小时 250 次；可选环境变量 `GLOBALPING_TOKEN`（同一账号的所有 token 共用 500 次/小时额度）。
- 国内检查从 TCP traceroute 改为 **TCP ping**（从国内探针向节点端口真实握手 3 次，任意一次成功即可达）。traceroute 在国际链路上末跳常为空：抽样 10 个节点，traceroute 判 0 个可达，TCP ping 判 4 个可达。
- 同一 `server:port` 只测一次。

### 📊 评分
- 抖动改为同一目标（YouTube 204）热连接采样的极差。此前用不同目标之间的延迟偏差，测到的是距离差，所有节点都 ≥ 323ms，超过 400ms 阈值，抖动因子（15 分）恒为 0。
- 统计：`nodes_real_ok` 改为海外真测通过数；新增 `nodes_china_reachable` / `nodes_china_unreachable` / `nodes_china_unknown`。

### ⚡ 测试器
- Netflix / ChatGPT 解锁检测挪到 `success` 置位之后，并单独限时 4s；单节点总超时触发时，已通过的结果会保留。此前解锁检测较慢时，会把已通过的节点判成 `test_one_timeout`。
- Netflix 只认 200（此前 403 也算解锁）；ChatGPT 解析 `cdn-cgi/trace` 的 `loc=`，排除不支持的地区（此前任何地区都返回 200）。
- sing-box 报 `address already in use`（端口竞态）时换端口重试一次。

### 🎯 采样
- 新增 15% 来源探索配额：每个来源轮流取 TCP 最快的节点，无历史数据的来源优先，打破"历史分低 → 不被测 → 分数一直低"的反馈环。

### 🕒 调度
- cron 从 `0 */6` 改为 `23 */6`，避开整点高峰（整点调度实测常被延迟 3~4 小时）。
- `push` 触发限定为 `main` 分支，`Commit & push` 步骤只在默认分支执行。此前推送任何功能分支都会触发流水线，并把未合并的分支提交 rebase 后推上 main。

## 2026-06-22 动态订阅网关与防投毒

### 🌐 动态订阅网关（GitHub Pages）
- 新增 `docs/index.html`：浏览器端实时筛选全量节点池，按地区/协议/关键词过滤，本地生成 Clash YAML / Base64 / sing-box JSON 订阅。
- 多 CDN 故障转移（jsDelivr → Statically → GitHub Raw），单源挂掉仍可用；浏览器端 TCP 测速，标红超时节点。
- 新增 `docs/sources.html`：订阅源健康面板，含 30 轮运行漏斗、死源清单、源贡献排行。
- 部署方式：GitHub Pages 从 `main` 分支 `/docs` 目录自动构建（Pages 服务端监听，非 workflow 部署步骤）。CI 推送 `output/` 后页面自动刷新。

### 🔒 SSRF 防投毒
- 在 `core/filtering.py` 增加私有地址 / 云元数据端点拦截：剔除 `server` 指向 RFC1918、本地环回、`169.254.169.254` 等的恶意节点，保护 CI 环境。
- 新增 `tools/import_contract.py`：CI 阶段检查导入契约，防止悬空 import（曾因引入未实现模块导致 CI 连续崩溃）。

### 🧹 回退与清理
- 回退此前一次"工业级重构"：该重构引入大量 `_*` 占位模块（bloom_filter / concurrency_pool / singbox_api_tester 等），在单机 CI 下无法运行，导致连续失败。已回退到两步测活稳定版本，并清理残留僵尸文件（-4.1MB，12 文件）。
- 修正 stability ranking bonus 使用的 counter 字段。

## 2026-06-18 全量扩源与两阶段测活

- 新增 Telegram 频道源支持与频道发现工具 `tools/discover_tg_channels.py`。
- 全量扩源：新增 43 个 Telegram 频道源，总源数从 64 提升至 107。
- 两阶段测活：100 并发轻量探活（只测 generate_204）先筛不可达节点，再对剩余做 50 并发完整真测，总耗时从 60+ 分钟降到约 8 分钟。
- 移除真测进程池门控，改用 `asyncio.Semaphore` 并发控制，解决高并发端口冲突。

## 2026-06-15 多维评分

- 7 因子加权评分：延迟、抖动、TCP、下载速度、指纹抗检测、协议历史、来源历史。
- REALITY / uTLS 优先，443 端口加成，跨周期稳定节点加分（`core/_fingerprint_test.py`）。

## 2026-06-14 (2.4.0) 分块输出与稳定性追踪

- 分块订阅输出（`chunks/`，每 100 节点一块）、按协议分文件（`by_protocol/`）、按地区分文件（`by_region/`）。
- 节点跨轮稳定性追踪（`node_stability.json`，连续通过/失败计数）。
- 降级容错、CI 失败自动开 Issue、源发现工具。

## 2026-06-12 (2.3.0) 可配置评分与可观测报告

- 可配置评分模板（`config/scoring.*.yaml`）、评分分项拆解。
- 健康报告、每日摘要、Actions Summary、README 状态区自动化（`core/readme_updater.py`）。

## 2026-05-01 (1.0.0) 初始版本

- 基于 sing-box 的真实代理测试流水线：聚合公开订阅源 → 去重 → TCP 预筛 → sing-box 真测 → 评分排序 → 输出多格式订阅。
