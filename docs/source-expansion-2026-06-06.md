# 订阅源扩容记录（2026-06-06）

## 目标

在不降低发布安全性的前提下，增加公开节点候选池，让 GitHub Actions 后续真测有更多可筛选节点。

本次只调整订阅源配置与说明文档，不改测试逻辑、输出逻辑、workflow 发布逻辑。

## 变更摘要

`config/sources.yaml` 从 29 个社区源扩展到 44 个社区源。

新增源分三组：

### v3.2：本地验证新增源

| name | 说明 | 限流 |
|---|---|---|
| `Epodonios-all` | 聚合型 v2ray config 源，新增贡献明显 | `max_nodes: 3000` |
| `roosterkid-openproxylist-v2ray` | openproxylist V2Ray RAW 源，小体量补充 | 无 |

### v3.3：深挖验证新增源

| name | 说明 | 限流 |
|---|---|---|
| `DeltaKronecker-all` | 聚合型 all configs | 无 |
| `moneyfly1-collectSub` | collectSub merged nodes | 无 |
| `nscl5-all` | configs/all.txt | 无 |
| `10ium-HighSpeed` | HighSpeed 节点列表 | 无 |
| `SoliSpirit-all` | 聚合型 all configs，体量较大 | `max_nodes: 3000` |
| `10ium-ScrapeCategorize-Vless` | 分类抓取的 VLESS 输出，体量较大 | `max_nodes: 2000` |


### v3.4：补充遗漏订阅源

| name | 说明 | 限流 |
|---|---|---|
| `MatinGhanbari-all-sub` | MatinGhanbari v2ray 全量订阅源 | `max_nodes: 3000` |
| `barry-far-vless` | barry-far 按协议拆分的 VLESS 源 | `max_nodes: 2000` |
| `barry-far-Sub2` | barry-far 分片订阅 2 | 无 |
| `barry-far-Sub1` | barry-far 分片订阅 1 | 无 |
| `MatinGhanbari-super-sub` | MatinGhanbari super subscription 聚合源 | `max_nodes: 3000` |


### v3.5：用户指出的遗漏源补齐

| name | 说明 | 本地单源解析 | 限流 |
|---|---|---:|---|
| `xiaoji235-airport-v2ray-all` | `xiaoji235/airport-free` 全量 v2ray 订阅 | 621 | 无 |
| `abc-configs-readme-latest30` | `FreeFolksOn/abc-configs-free-vpn-proxy-list` README 最新 30 条表格源 | 15 | 无 |

## 本地验证结果

验证命令：

```bash
python tools/audit_sources.py --sources config/sources.yaml --output /home/.z/workspaces/con_hxC6m5p17RjrVHXZ/audit-current-config-44-final.json --concurrency 20

python main.py \
  --sources config/sources.yaml \
  --output-dir /home/.z/workspaces/con_hxC6m5p17RjrVHXZ/output-current-config-44-final \
  --no-real-test \
  --no-tcp-check \
  --all-output-mode light \
  --top-n 0 \
  --test-limit 0 \
  --min-retain-ratio 0 \
  --repo LeilaoMi/AutoMergePublicNodes-Optimized

python -m compileall -q main.py core tools tests
python -m unittest discover -s tests -v
git diff --check
```

结果：

```text
sources_total: 44
sources_healthy: 44
sources_broken: 0
nodes_raw: 40437
nodes_dedup: 15755
nodes_all_output: 11022
all_output_mode: light
compileall: pass
unittest: 35 tests OK
git diff --check: pass
```

对比本次扩容前正式 `output/stats.json`：

```text
扩容前 nodes_dedup: 8515
扩容后临时 nodes_dedup: 15755
新增去重候选约: +7240
```

## 取舍说明

- 没有加入 404、403、0 节点或解析失败的候选源。
- 没有加入与现有源语义明显重复、且新增贡献较低的候选源。
- 对体量较大的聚合源设置 `max_nodes`，避免单源过度放大 CI 抓取和解析成本。
- 本地没有可执行 `sing-box`，因此本次本地验证只覆盖抓取、解析、去重、输出生成、语法和回归测试；真实代理可用性仍由 GitHub Actions 下载 `sing-box` 后执行真测。

## 后续观察重点

push 后观察下一轮 GitHub Actions：

1. `output/source_audit.json` 是否仍为 44 源健康。
2. `output/stats.json` 中 `nodes_raw` / `nodes_dedup` 是否明显上涨。
3. `verified_count` / `global_count` 是否上涨；如果不上涨，说明新增候选多但真实可用率一般。
4. `real_test_error_details` 是否出现某个新增源集中失败。
5. workflow 是否接近 30 分钟超时；若接近，应降低大源 `max_nodes` 或启用更轻量策略。

## 最终状态

- 状态：已完成本地 44 源扩容与验证，等待提交/push 后由 GitHub Actions 做线上真测。
- 涉及文件：`config/sources.yaml`、`README.md`、`docs/source-expansion-2026-06-06.md`。
- 敏感信息：无密钥、无 token、无私有凭证。
