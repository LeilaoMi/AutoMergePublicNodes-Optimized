# AutoMergePublicNodes-Optimized global 输出第一阶段续接

任务目标：在保留严格 `verified.*` 的前提下，新增“兼顾数量”的 `global.*` 输出：严格真测失败但仅因 `cn-block`（百度连通）失败的节点，复测时跳过 `cn-block`，若仍通过 YouTube/Google 204、geo 非 CN、100KB speed，则纳入 `global.*`。

项目路径：`/home/workspace/AutoMergePublicNodes-Optimized`
当前分支：`main`
当前远端：`origin/main`

已完成：
- `core/tester.py`
  - `SingBoxTester.__init__` 新增 `skip_target_kinds`，默认空集合，严格行为不变。
  - 测试循环可跳过指定 target kind。
  - 修正延迟统计为 `(kind, latency)`，避免跳过目标后 zip 原始 `TEST_TARGETS` 导致均值错位。
- `main.py`
  - 新增 `build_output_nodes()`，复用 tag 加延迟/抖动逻辑。
  - 严格 `verified.*` 仍来自原 `valid`。
  - 新增 `global.*`：默认 `--global-output` 开启；对 `cn-block:*` 失败节点用 `skip_target_kinds={"cn-block"}` 复测，成功后追加进 global。
  - `stats.json` 新增 `nodes_global_output`、`nodes_global_extra_from_cn_block`、`global_skip_target_kinds`。
- `tests/test_regressions.py`
  - 旧 stats mock Args 补 `global_output=False`。
  - 新增 `test_global_output_adds_cn_block_retry_successes`。
  - 新增 `test_singbox_tester_records_skipped_target_kinds`。
- 已运行验证：
  - `python -m compileall -q main.py core tools tests` 通过。
  - `python -m unittest -v tests.test_regressions` 通过，31 tests OK。

未完成：
1. `tools/prepare_artifact_output.py` 需要加入 `global.*`。
2. `.github/workflows/update.yml` 的 Upload debug artifact / jsDelivr purge 需要加入 global 文件。
3. `README.md` 需要同步说明 `global.*` 的用途和订阅地址。
4. 再跑完整验证：compileall、unittest、git diff --check。
5. 不要部署、不 push，除非用户确认。

注意：不要泄露任何 token。本任务不涉及密钥。
