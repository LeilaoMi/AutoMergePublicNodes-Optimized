# Release Notes

This directory contains user-facing release notes for notable project versions.

| Version | Date | Summary |
|---|---|---|
| [2.3.0](2.3.0.md) | 2026-06-12 | Configurable scoring profiles, score breakdown, observability reports, Actions Summary, and README status automation |

For concise change history, see [`../../CHANGELOG.md`](../../CHANGELOG.md).

## Maintenance checklist

When adding a new project version:

1. Add a new `docs/releases/<version>.md` file for user-facing release notes.
2. Add the version to the table above.
3. Add the concise technical change log to [`../../CHANGELOG.md`](../../CHANGELOG.md).
4. Keep README pointing to this release notes index instead of a single version file.

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
