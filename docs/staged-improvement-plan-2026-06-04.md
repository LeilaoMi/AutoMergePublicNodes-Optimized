# AutoMergePublicNodes-Optimized 阶段改进任务

> 制定时间：2026-06-04
> 来源：`file docs/audit-2026-06-04.md`
> 原则：先修实锤风险，再提高发布安全，最后优化质量、性能和长期架构。每阶段都必须通过语法检查、回归测试和 diff 审查后再进入下一阶段。

---

## 阶段 1：P0 实锤问题修复（已推进）

目标：先消除会导致失败、污染输出或覆盖人工修改的高风险问题。

### 已完成

1. **修复** `fetch_all` **overall timeout bug**

   - 文件：`file core/fetcher.py`
   - 改动：将 coroutine 列表改为 `asyncio.create_task`，timeout 时返回已完成结果，取消并 drain 未完成任务。
   - 验证：新增 `test_fetch_all_overall_timeout_returns_partial_results`。

2. **修复 unittest 污染 tracked output**

   - 文件：`file tests/test_regressions.py`
   - 改动：`file health_report.py` 子进程测试显式传 `--output` 到临时目录。
   - 验证：测试后 `file output/health_report.json` 不再被改动。

3. **移除 workflow 自动 force push fallback**

   - 文件：`file .github/workflows/update.yml`
   - 改动：删除 `force_push` 手动输入；rebase 失败时直接失败，不再 `--force-with-lease`。

4. **回退 GitHub Actions 主版本到稳定版**

   - 文件：`file .github/workflows/update.yml`
   - 改动：`actions/checkout@v6 → @v4`，`actions/setup-python@v6 → @v5`。

5. **确认 remote 不再含 GitHub token**

   - 结果：`origin` 为标准 HTTPS URL。
   - 注意：旧 token 是否撤销需要用户在 GitHub 后台处理，我无法替用户确认 token 状态。

---

## 阶段 2：发布安全与故障可见性（已推进）

目标：让 CI 失败时更容易排查，让异常输出不再静默发布。

### 已完成

1. **健康报告增加状态等级**

   - 文件：`file tools/health_report.py`
   - 新增：`status = ok | warning | critical`
   - 规则：结构失败或 verified=0 为 `critical`；存在 alerts 为 `warning`；否则 `ok`。
   - 验证：新增 warning / critical 回归测试。

2. **workflow 参数加上限保护**

   - 文件：`file .github/workflows/update.yml`
   - 规则：`top_n <= 1000`，`test_limit <= 3000`，且必须是非负整数。

3. **CI 上传 debug artifact**

   - 文件：`file .github/workflows/update.yml`
   - 上传：`file stats.json`、`file source_audit.json`、`file health_report.json`、converter 文件。

4. **jsDelivr purge 记录 HTTP 状态**

   - 文件：`file .github/workflows/update.yml`
   - 改动：不再静默 `curl || true`，5xx/000 输出 warning。

---

## 阶段 3：质量与兼容性提升（已推进）

目标：提升 verified 质量解释能力，减少客户端导入失败。

### 已完成

1. **输出 sing-box JSON 移除 inbound sniff**

   - 文件：`core/generator.py`
   - 改动：生成给用户导入的 sing-box JSON 中，`mixed-in` inbound 不再包含 `sniff` / `sniff_override_destination`。
   - 原因：测试器配置已按 sing-box 1.13+ 兼容策略移除 inbound sniff，输出配置也应保持一致。
   - 验证：新增 `test_write_outputs_singbox_inbound_compatible_with_1_13`。

2. **细分 real_test_errors**

   - 文件：`main.py`
   - 改动：保留原有 `real_test_errors` 粗分类，同时新增 `real_test_error_details` Top 10 明细，单条错误截断到 120 字符，避免 stats 过大。
   - 输出示例：

   ```json
   "real_test_error_details": [
     {"error": "204:status=403", "count": 120}
   ]
   ```

3. **记录阶段耗时**

   - 文件：`main.py`
   - 改动：新增 `stats.json.stage_durations`。
   - 当前包含：`fetch`、`geo`、`tcp`、`real_test`、`generate`。
   - 验证：新增 `test_main_stats_include_stage_durations_and_error_details`，使用 mock，不触网、不污染 output。

### 延后

4. **README 增加“为什么 verified 很少”说明**

   - 原因：当前 `README.md` 在任务开始前已有 modified 状态，为避免混入不相关文档差异，本阶段暂不改 README。

5. **尝试 `sing-box check -c output/verified.json`**

   - 原因：本地仓库没有 `./sing-box` 二进制；workflow 已能下载 sing-box，但真正启用 check 前建议先在 CI 或本地二进制环境验证 generated config。

---

## 阶段 4：性能与仓库体积控制（已推进）

目标：降低 CI 成本和 Git 历史膨胀。

### 已完成

1. **`tcp_check_batch` 改 worker 队列**

   - 文件：`main.py`
   - 改动：从 `asyncio.gather(*[_check(n) for n in nodes])` 改为 `asyncio.Queue` + 固定数量 worker。
   - 效果：不再为 8K+ 节点一次性创建 8K+ coroutine，只创建 `min(concurrency, len(nodes))` 个 worker。
   - 行为保持：成功结果仍按 TCP 延迟升序返回，失败节点忽略，连接成功后关闭 writer。
   - 验证：新增 `test_tcp_check_batch_uses_worker_queue_and_sorts_results`，mock `asyncio.open_connection`，确认成功节点按延迟排序且失败节点被忽略。

2. 下采样改为“协议基础配额 + 剩余名额按 TCP 延迟补齐”。
3. `all.json/all.yaml` 从 main 输出策略中降级，只保留 all txt/urls 或迁移到 artifact 分支。
4. output 迁移到独立 artifact/data 分支，main 只保留源码和文档。
5. 建立协议 fixture corpus，覆盖 parse → url → clash → sing-box 生成链路。

---

## 当前验证结果

已运行：

```bash
python -m compileall -q main.py core tools tests
python -m unittest -v tests.test_regressions
python tools/health_report.py --output-dir output --verified-prefix verified --output /home/.z/workspaces/con_kpQgciAR2GAokSw0/health-report-check.json
git diff --check
```

结果：

```text
22 tests OK
health_report: ok=True, status=warning, verified=33, all=8095
git diff --check: pass
```

---

## 未执行事项

- 未 push。
- 未部署。
- 未改远端 GitHub token；旧 token 是否撤销需用户在 GitHub 后台确认。
- 未处理任务开始前已有的 `file README.md` modified 状态和未跟踪历史报告文件。