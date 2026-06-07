"""
输出健康审计工具
- 检查 output 中订阅文件是否齐全且可解析
- 检查重复 tag/name、URL 数量、协议分布、地区分组
- 输出 JSON 健康报告，供 CI 归档和人工查看
"""
from __future__ import annotations

import argparse
import base64
import json
import sys
import time
from collections import Counter
from pathlib import Path
from typing import Any, Dict, List

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import yaml


def _load_json(path: Path) -> Dict[str, Any]:
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def _load_yaml(path: Path) -> Dict[str, Any]:
    with path.open(encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data if isinstance(data, dict) else {}


def _read_urls(path: Path) -> List[str]:
    return [line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def _read_txt_urls(path: Path) -> List[str]:
    raw = path.read_text(encoding="utf-8").strip()
    if not raw:
        return []
    decoded = base64.b64decode(raw + "=" * ((4 - len(raw) % 4) % 4)).decode("utf-8", errors="replace")
    return [line.strip() for line in decoded.splitlines() if line.strip()]


def _duplicate_items(items: List[str]) -> List[str]:
    counts = Counter(items)
    return sorted(k for k, v in counts.items() if v > 1)


def _audit_prefix(output_dir: Path, prefix: str) -> Dict[str, Any]:
    paths = {ext: output_dir / f"{prefix}.{ext}" for ext in ("json", "yaml", "urls", "txt", "converter.md")}
    full_required = ("json", "yaml", "urls", "txt", "converter.md")
    light_required = ("urls", "txt", "converter.md")
    full_missing = [str(paths[ext].name) for ext in full_required if not paths[ext].exists()]
    light_missing = [str(paths[ext].name) for ext in light_required if not paths[ext].exists()]
    mode = "full" if not full_missing else "light" if not light_missing else "missing"
    report: Dict[str, Any] = {
        "prefix": prefix,
        "mode": mode,
        "missing_files": full_missing if mode == "full" else light_missing,
        "ok": mode != "missing",
    }
    if mode == "missing":
        return report

    urls = _read_urls(paths["urls"])
    txt_urls = _read_txt_urls(paths["txt"])
    report.update({
        "files": {ext: paths[ext].stat().st_size for ext in paths if paths[ext].exists()},
        "url_count": len(urls),
        "txt_url_count": len(txt_urls),
        "json_node_count": 0,
        "yaml_proxy_count": 0,
        "protocol_dist": {},
        "region_group_count": 0,
        "region_groups": [],
        "duplicate_json_tags": [],
        "duplicate_yaml_names": [],
        "url_txt_mismatch": urls != txt_urls,
    })

    if mode == "full":
        singbox = _load_json(paths["json"])
        clash = _load_yaml(paths["yaml"])
        outbounds = [ob for ob in singbox.get("outbounds", []) if isinstance(ob, dict)]
        node_outbounds = [ob for ob in outbounds if ob.get("type") not in {"selector", "url-test", "direct"}]
        tags = [str(ob.get("tag", "")) for ob in node_outbounds]
        proxies = [p for p in clash.get("proxies", []) if isinstance(p, dict)]
        proxy_names = [str(p.get("name", "")) for p in proxies]
        groups = [g for g in clash.get("proxy-groups", []) if isinstance(g, dict)]
        region_groups = [g.get("name") for g in groups if g.get("type") == "url-test" and g.get("name") != "♻️ Auto"]
        report.update({
            "json_node_count": len(node_outbounds),
            "yaml_proxy_count": len(proxies),
            "protocol_dist": dict(Counter(str(ob.get("type", "")) for ob in node_outbounds)),
            "region_group_count": len(region_groups),
            "region_groups": sorted(str(g) for g in region_groups),
            "duplicate_json_tags": _duplicate_items(tags),
            "duplicate_yaml_names": _duplicate_items(proxy_names),
        })

    report["ok"] = (
        report["ok"]
        and not report["duplicate_json_tags"]
        and not report["duplicate_yaml_names"]
        and not report["url_txt_mismatch"]
        and report["url_count"] == report["txt_url_count"]
    )
    return report


def _source_score_rows(mapping: Dict[str, Any], limit: int = 10, reverse: bool = True) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    if not isinstance(mapping, dict):
        return rows
    for name, data in mapping.items():
        if not isinstance(data, dict):
            continue
        row = dict(data)
        row["name"] = name
        rows.append(row)
    rows.sort(key=lambda r: (float(r.get("score", 0) or 0), int(r.get("tested", 0) or 0)), reverse=reverse)
    return rows[:limit]


def _pass_rate_rows(mapping: Dict[str, Any], limit: int = 10, reverse: bool = True) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    if not isinstance(mapping, dict):
        return rows
    for name, counts in mapping.items():
        if not isinstance(counts, dict):
            continue
        passed = int(counts.get("pass", 0) or 0)
        failed = int(counts.get("fail", 0) or 0)
        total = passed + failed
        if total <= 0:
            continue
        rows.append({
            "name": name,
            "pass": passed,
            "fail": failed,
            "total": total,
            "pass_rate": round(passed / total, 3),
        })
    rows.sort(key=lambda r: (r["pass_rate"], r["total"]), reverse=reverse)
    return rows[:limit]


def build_health_report(output_dir: str = "output", verified_prefix: str = "verified") -> Dict[str, Any]:
    out = Path(output_dir)
    prefixes = [verified_prefix, "all"]
    prefix_reports = {prefix: _audit_prefix(out, prefix) for prefix in prefixes}
    stats_path = out / "stats.json"
    source_audit_path = out / "source_audit.json"
    source_cleanup_path = out / "source_cleanup_suggestions.json"
    stats = _load_json(stats_path) if stats_path.exists() else {}
    source_audit_payload = _load_json(source_audit_path) if source_audit_path.exists() else []
    source_cleanup_payload = _load_json(source_cleanup_path) if source_cleanup_path.exists() else {}
    source_rows = source_audit_payload.get("sources", []) if isinstance(source_audit_payload, dict) else source_audit_payload
    if not isinstance(source_rows, list):
        source_rows = []
    dead_sources = [r for r in source_rows if isinstance(r, dict) and r.get("consecutive_dead", 0) >= 2]

    all_report = prefix_reports.get("all", {})
    verified_report = prefix_reports.get(verified_prefix, {})
    all_count = all_report.get("json_node_count", 0)
    verified_count = verified_report.get("json_node_count", 0)
    all_compare_count = all_count if all_report.get("mode") == "full" else all_report.get("url_count", 0)
    strategy_ok = all_compare_count >= verified_count

    # §4.1 — 加报警字段, 让 CI 报警有明确根因
    # protocol_pass_rate 任何协议 pass 率 < 10% 算异常
    low_pass_protocols = []
    for proto, counts in stats.get("protocol_pass_rate", {}).items():
        total = counts.get("pass", 0) + counts.get("fail", 0)
        if total > 0:
            rate = counts.get("pass", 0) / total
            if rate < 0.1:
                low_pass_protocols.append({"protocol": proto, "pass_rate": round(rate, 3)})

    real_test_errors = stats.get("real_test_errors", {})
    tcp_errors = stats.get("tcp_errors", {})
    protocol_pass_rate = stats.get("protocol_pass_rate", {})
    source_pass_rate = stats.get("source_pass_rate", {})
    source_scores = stats.get("source_scores", {})
    protocol_best = _pass_rate_rows(protocol_pass_rate, limit=10, reverse=True)
    protocol_worst = _pass_rate_rows(protocol_pass_rate, limit=10, reverse=False)
    source_best = _pass_rate_rows(source_pass_rate, limit=10, reverse=True)
    source_worst = _pass_rate_rows(source_pass_rate, limit=10, reverse=False)
    source_score_best = _source_score_rows(source_scores, limit=10, reverse=True)
    source_score_worst = _source_score_rows(source_scores, limit=10, reverse=False)
    cleanup_summary = source_cleanup_payload.get("summary", {}) if isinstance(source_cleanup_payload, dict) else {}
    cleanup_suggestions = source_cleanup_payload.get("suggestions", {}) if isinstance(source_cleanup_payload, dict) else {}
    if not isinstance(cleanup_summary, dict):
        cleanup_summary = {}
    if not isinstance(cleanup_suggestions, dict):
        cleanup_suggestions = {}
    source_disable_candidates = [
        row for row in _source_score_rows(source_scores, limit=50, reverse=False)
        if row.get("recommendation") == "disable-candidate"
    ]

    cleanup_disable = cleanup_suggestions.get("disable", []) if isinstance(cleanup_suggestions.get("disable", []), list) else []
    cleanup_downweight = cleanup_suggestions.get("downweight", []) if isinstance(cleanup_suggestions.get("downweight", []), list) else []

    has_alerts = bool(low_pass_protocols or real_test_errors or source_disable_candidates or cleanup_disable)
    ok = all(r.get("ok", False) for r in prefix_reports.values()) and strategy_ok
    if not ok or verified_count == 0:
        status = "critical"
    elif has_alerts:
        status = "warning"
    else:
        status = "ok"

    report = {
        "generated_at": time.strftime("%Y-%m-%d %H:%M:%S"),
        "ok": ok,
        "status": status,
        "prefixes": prefix_reports,
        "strategy": {
            "all_json_nodes": all_count,
            "all_compare_nodes": all_compare_count,
            "verified_json_nodes": verified_count,
            "all_contains_at_least_verified_count": strategy_ok,
            "note": "all.* 来自去重池；verified.* 来自质量过滤/TCP/真测后的 Top N。light 模式下 all_compare_nodes 使用 all.urls 数量。",
        },
        "stats_summary": {
            "nodes_raw": stats.get("nodes_raw"),
            "nodes_dedup": stats.get("nodes_dedup"),
            "nodes_real_ok": stats.get("nodes_real_ok"),
        },
        "rankings": {
            "protocol_best": protocol_best,
            "protocol_worst": protocol_worst,
            "source_best": source_best,
            "source_worst": source_worst,
            "source_score_best": source_score_best,
            "source_score_worst": source_score_worst,
        },
        "source_cleanup": {
            "dead_2_plus_count": len(dead_sources),
            "dead_2_plus": dead_sources,
            "suggestion_summary": cleanup_summary,
            "disable_count": int(cleanup_summary.get("disable", len(cleanup_disable)) or 0),
            "downweight_count": int(cleanup_summary.get("downweight", len(cleanup_downweight)) or 0),
            "prefer_count": int(cleanup_summary.get("prefer", 0) or 0),
            "observe_count": int(cleanup_summary.get("observe", 0) or 0),
            "disable_suggestions": cleanup_disable[:20],
            "downweight_suggestions": cleanup_downweight[:20],
        },
        "alerts": {
            "low_pass_protocols": low_pass_protocols,
            "real_test_errors": real_test_errors,
            "tcp_errors": tcp_errors,
            "source_disable_candidates": source_disable_candidates,
            "source_cleanup_disable_suggestions": cleanup_disable,
        },
    }
    return report


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", default="output")
    parser.add_argument("--verified-prefix", default="verified")
    parser.add_argument("--output", default="output/health_report.json")
    parser.add_argument("--strict", action="store_true",
                        help="§1.5 — 报警时也 exit 1 (默认只记录, 不失败 CI)")
    args = parser.parse_args()

    report = build_health_report(args.output_dir, args.verified_prefix)
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if not report["ok"]:
        raise SystemExit(1)
    # §1.5 — verified 为 0 时硬失败 (这是真测全挂的明确信号)
    if report["prefixes"].get(args.verified_prefix, {}).get("json_node_count", 0) == 0:
        print("::error::verified 输出为 0, 真测全挂或测试源全失效", file=sys.stderr)
        raise SystemExit(2)
    # §1.5 — strict 模式下报警也失败
    if args.strict and report["status"] in {"warning", "critical"}:
        print("::error::alerts 触发, 但启用 --strict 才失败", file=sys.stderr)
        raise SystemExit(3)


if __name__ == "__main__":
    main()
