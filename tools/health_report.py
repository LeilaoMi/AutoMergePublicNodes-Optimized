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
    missing = [str(p.name) for p in paths.values() if not p.exists()]
    report: Dict[str, Any] = {
        "prefix": prefix,
        "missing_files": missing,
        "ok": not missing,
    }
    if missing:
        return report

    singbox = _load_json(paths["json"])
    clash = _load_yaml(paths["yaml"])
    urls = _read_urls(paths["urls"])
    txt_urls = _read_txt_urls(paths["txt"])

    outbounds = [ob for ob in singbox.get("outbounds", []) if isinstance(ob, dict)]
    node_outbounds = [ob for ob in outbounds if ob.get("type") not in {"selector", "url-test", "direct"}]
    tags = [str(ob.get("tag", "")) for ob in node_outbounds]
    proxies = [p for p in clash.get("proxies", []) if isinstance(p, dict)]
    proxy_names = [str(p.get("name", "")) for p in proxies]
    groups = [g for g in clash.get("proxy-groups", []) if isinstance(g, dict)]
    region_groups = [g.get("name") for g in groups if g.get("type") == "url-test" and g.get("name") != "♻️ Auto"]

    report.update({
        "files": {ext: paths[ext].stat().st_size for ext in paths},
        "url_count": len(urls),
        "txt_url_count": len(txt_urls),
        "json_node_count": len(node_outbounds),
        "yaml_proxy_count": len(proxies),
        "protocol_dist": dict(Counter(str(ob.get("type", "")) for ob in node_outbounds)),
        "region_group_count": len(region_groups),
        "region_groups": sorted(str(g) for g in region_groups),
        "duplicate_json_tags": _duplicate_items(tags),
        "duplicate_yaml_names": _duplicate_items(proxy_names),
        "url_txt_mismatch": urls != txt_urls,
    })
    report["ok"] = (
        report["ok"]
        and not report["duplicate_json_tags"]
        and not report["duplicate_yaml_names"]
        and not report["url_txt_mismatch"]
        and report["url_count"] == report["txt_url_count"]
    )
    return report


def build_health_report(output_dir: str = "output", verified_prefix: str = "verified") -> Dict[str, Any]:
    out = Path(output_dir)
    prefixes = [verified_prefix, "all"]
    prefix_reports = {prefix: _audit_prefix(out, prefix) for prefix in prefixes}
    stats_path = out / "stats.json"
    source_audit_path = out / "source_audit.json"
    stats = _load_json(stats_path) if stats_path.exists() else {}
    source_audit_payload = _load_json(source_audit_path) if source_audit_path.exists() else []
    source_rows = source_audit_payload.get("sources", []) if isinstance(source_audit_payload, dict) else source_audit_payload
    if not isinstance(source_rows, list):
        source_rows = []
    dead_sources = [r for r in source_rows if isinstance(r, dict) and r.get("consecutive_dead", 0) >= 2]

    all_count = prefix_reports.get("all", {}).get("json_node_count", 0)
    verified_count = prefix_reports.get(verified_prefix, {}).get("json_node_count", 0)
    strategy_ok = all_count >= verified_count

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

    report = {
        "generated_at": time.strftime("%Y-%m-%d %H:%M:%S"),
        "ok": all(r.get("ok", False) for r in prefix_reports.values()) and strategy_ok,
        "prefixes": prefix_reports,
        "strategy": {
            "all_json_nodes": all_count,
            "verified_json_nodes": verified_count,
            "all_contains_at_least_verified_count": strategy_ok,
            "note": "all.* 来自去重池；verified.* 来自质量过滤/TCP/真测后的 Top N。",
        },
        "stats_summary": {
            "nodes_raw": stats.get("nodes_raw"),
            "nodes_dedup": stats.get("nodes_dedup"),
            "nodes_real_ok": stats.get("nodes_real_ok"),
        },
        "source_cleanup": {
            "dead_2_plus_count": len(dead_sources),
            "dead_2_plus": dead_sources,
        },
        "alerts": {
            "low_pass_protocols": low_pass_protocols,
            "real_test_errors": real_test_errors,
        },
    }
    return report


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", default="output")
    parser.add_argument("--verified-prefix", default="verified")
    parser.add_argument("--output", default="output/health_report.json")
    args = parser.parse_args()

    report = build_health_report(args.output_dir, args.verified_prefix)
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if not report["ok"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
