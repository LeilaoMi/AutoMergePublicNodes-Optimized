# Release Notes

This directory contains user-facing release notes for notable project versions.

| Version | Date | Summary |
|---|---|---|
| [2.4.0](2.4.0.md) | 2026-06-14 | 分块输出、协议分文件、节点稳定性追踪、解锁检测、降级容错、CI 通知、源发现 |
| [2.3.0](2.3.0.md) | 2026-06-12 | 可配置评分模板、评分分项拆解、可观测报告、Actions Summary、README 状态自动化 |

如需简洁的变更历史，请查看 [`../../CHANGELOG.md`](../../CHANGELOG.md)。

## 维护清单

新增项目版本时：

1. 新增 `docs/releases/<version>.md` 用户向发布说明。
2. 将版本号加入上方表格。
3. 在 [`../../CHANGELOG.md`](../../CHANGELOG.md) 中添加简洁的技术变更记录。
4. README 固定指向本发布说明索引，不直接指向单个版本文件。

## GitHub Release publishing

After CI is green, publish a GitHub Release from the repository root:

```bash
git fetch origin main
git checkout main
git pull --ff-only origin main
git tag -a v2.3.0 -m "AutoMergePublicNodes-Optimized 2.3.0"
git push origin v2.3.0
```

Then create the GitHub Release using `docs/releases/2.3.0.md` as the release body.

With GitHub CLI:

```bash
gh release create v2.3.0 \
  --title "AutoMergePublicNodes-Optimized 2.3.0" \
  --notes-file docs/releases/2.3.0.md
```
