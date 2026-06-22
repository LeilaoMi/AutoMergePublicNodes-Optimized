# Changelog

本项目所有 notable 变更记录于此。按时间倒序排列。

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
