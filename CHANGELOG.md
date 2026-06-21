# Changelog

All notable changes to this project will be documented in this file.

## [3.0.0] - 2026-06-22 (工业级重构与生态跨越)

### 🚀 核心架构重构 (底层基建)
- **内存防线 (Bloom Filter)**：引入 `core/bloom_filter.py`，使用布隆过滤器替代传统的 `set()` 进行节点指纹去重。在处理 70,000+ 原始节点时，将内存占用压缩 90% 以上，彻底免疫 GitHub Actions 的 OOM 崩溃风险。
- **并发引擎重构 (Concurrency Gate)**：引入 `core/concurrency_pool.py`，实现基于 `asyncio.Semaphore` 与预分配端口池的 `ConcurrencyGate`。彻底替代废弃的 `ProcessPoolGate`，解决高并发探活时的端口冲突与进程排队超时。
- **代码脱水 (物理清创)**：删除 10 个在单机 CI 环境下无法运行或纯属概念堆砌的“伪 AI/联邦”僵尸模块（包括 `_federated_test_network`, `_adaptive_learning`, `_community_driven` 等），大幅降低代码库认知负载。

### ⚡ 终极性能压榨 (控制面集成)
- **sing-box API 批量测速**：新增 `core/singbox_api_tester.py`。抛弃 Python 端使用 `aiohttp` 挨个发送 HTTP 请求的低效模式，利用 sing-box 内置的 Clash API 与 `url-test` 引擎进行并发探活。
- **零侵入热插拔**：通过异步适配层 (`async def test_all`) 完美兼容原有 `TestResult` 数据结构，已在 `main.py` 中无缝替换原有测试器，将测速耗时从“分钟级”降维至“秒级”。

### 🔒 安全防御与 CI 治理
- **SSRF 防投毒网关**：新增 `core/security_guard.py`。在最终输出阶段 (`build_output_nodes`) 自动校验节点 `server` 字段，精准拦截指向 RFC1918 私有地址、本地环回及云厂商元数据服务（如 AWS/GCP/阿里云的 `169.254.169.254`）的恶意 TG 节点，保护 CI 运行环境。
- **Git 仓库治理 (双分支隔离)**：重构 `.github/workflows/update.yml`。`main` 分支仅保留订阅文件与 README，状态 JSON 文件被剥离并强制覆盖推送至 `state` 孤儿分支，彻底冻结 `.git` 目录的体积膨胀。

### 🌐 产品化跨越 (纯静态动态网关)
- **前端交互层**：新增 `web/` 目录，提供基于 Tailwind CSS 的极简 Web UI (`index.html` + `app.js`)。
- **客户端实时过滤**：支持用户在浏览器端按地区、协议实时过滤节点，并本地生成 Base64 或 Clash YAML 订阅。零服务器开销，抗审查能力达到极致。
- **CI 自动化部署**：流水线集成 `tools/export_web_nodes.py` 数据导出与 GitHub Pages 自动部署逻辑，实现全链路自动化。

---

## [2.9.1] - 2026-06-18
- **性能调优**：移除真测进程池门控，并发数提升至 50；引入两阶段探活（100 并发轻量探活 + 50 并发完整真测），解决 60 分钟超时问题。
- **全量扩源**：新增 43 个 Telegram 频道源，总源数达到 107 个。
- **文档重构**：按实际功能重写所有说明文档，中文化所有模块 docstring。

## [2.8.0] - 2026-06-15
- **多维评分**：引入 7 因子加权评分系统（延迟、抖动、TCP、速度、指纹对抗、协议历史、来源历史）。
- **能力画像**：扩展解锁检测（Netflix, ChatGPT, Disney, YouTube Premium 等），支持按能力切片输出。

## [2.5.0] - 2026-06-10
- **增量缓存**：引入 `_incremental_cache.py`，跳过配置未变且近期已测过的节点。
- **生命周期预测**：引入 `_lifetime_predictor.py`，基于历史数据预测节点剩余寿命。

## [1.0.0] - 2026-05-01
- 初始版本发布。基于 sing-box 的真实代理测试流水线。
