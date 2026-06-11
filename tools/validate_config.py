#!/usr/bin/env python3
"""无需联网校验项目配置文件。"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Set

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import yaml

SUPPORTED_KINDS = {"url", "dynamic", "list"}
SUPPORTED_PROTOCOLS = {
    "vmess", "vless", "trojan", "ss", "ssr", "shadowsocks", "shadowsocksr",
    "hysteria", "hysteria2", "hy", "hy2", "tuic", "anytls", "socks", "socks5", "http", "https",
}
URL_RE = re.compile(r"^https?://", re.I)


def _load_yaml(path: Path) -> Any:
    with path.open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def _add(errors: List[str], msg: str) -> None:
    errors.append(msg)


def validate_sources(path: str) -> List[str]:
    errors: List[str] = []
    p = Path(path)
    if not p.exists():
        return [f"缺少源配置文件：{path}"]
    try:
        data = _load_yaml(p) or {}
    except Exception as exc:
        return [f"sources.yaml 解析失败：{exc}"]
    sources = data.get("sources") if isinstance(data, dict) else None
    if not isinstance(sources, list):
        return ["sources.yaml 必须包含列表字段：sources"]

    seen_urls: Set[str] = set()
    seen_names: Set[str] = set()
    for idx, entry in enumerate(sources, 1):
        label = f"sources[{idx}]"
        if isinstance(entry, str):
            url = entry.strip()
            name = ""
            kind = "url"
        elif isinstance(entry, dict):
            url = str(entry.get("url", "")).strip()
            name = str(entry.get("name", "")).strip()
            kind = str(entry.get("kind", "url")).strip()
            if "enabled" in entry and not isinstance(entry.get("enabled"), bool):
                _add(errors, f"{label}.enabled 必须是布尔值")
            if "max_nodes" in entry:
                try:
                    max_nodes = int(entry.get("max_nodes"))
                    if max_nodes < 0:
                        _add(errors, f"{label}.max_nodes 必须 >= 0")
                except (TypeError, ValueError):
                    _add(errors, f"{label}.max_nodes 必须是整数")
            ignore_protocols = entry.get("ignore_protocols", [])
            if ignore_protocols is not None and not isinstance(ignore_protocols, list):
                _add(errors, f"{label}.ignore_protocols 必须是列表")
            elif isinstance(ignore_protocols, list):
                for proto in ignore_protocols:
                    if str(proto).lower() not in SUPPORTED_PROTOCOLS:
                        _add(errors, f"{label}.ignore_protocols 包含不支持的协议：{proto}")
        else:
            _add(errors, f"{label} 必须是字符串或映射")
            continue

        if not url:
            _add(errors, f"{label}.url 不能为空")
        elif not URL_RE.match(url):
            _add(errors, f"{label}.url 必须以 http:// 或 https:// 开头：{url}")
        if kind not in SUPPORTED_KINDS:
            _add(errors, f"{label}.kind 不支持：{kind}")
        if url in seen_urls:
            _add(errors, f"源 URL 重复：{url}")
        seen_urls.add(url)
        if name:
            if name in seen_names:
                _add(errors, f"源名称重复：{name}")
            seen_names.add(name)
    return errors


def _as_list(value: Any, label: str, errors: List[str]) -> List[Any]:
    if value is None:
        return []
    if not isinstance(value, list):
        _add(errors, f"{label} 必须是列表")
        return []
    return value


def _as_number(value: Any, label: str, errors: List[str], *, min_value: float | None = None) -> float | None:
    try:
        number = float(value)
    except (TypeError, ValueError):
        _add(errors, f"{label} 必须是数字")
        return None
    if min_value is not None and number < min_value:
        _add(errors, f"{label} 必须 >= {min_value:g}")
    return number


def validate_scoring_rules(path: str) -> List[str]:
    errors: List[str] = []
    p = Path(path)
    if not p.exists():
        return []
    try:
        data = _load_yaml(p) or {}
    except Exception as exc:
        return [f"scoring.yaml 解析失败：{exc}"]
    if not isinstance(data, dict):
        return ["scoring.yaml 必须是映射"]

    allowed_top = {"weights", "thresholds", "defaults"}
    for key in data:
        if key not in allowed_top:
            _add(errors, f"scoring.yaml 包含未知字段：{key}")

    weights = data.get("weights", {})
    if weights is None:
        weights = {}
    if not isinstance(weights, dict):
        _add(errors, "scoring.weights 必须是映射")
    else:
        required_weights = {"latency", "jitter", "tcp", "protocol_history", "source_history"}
        for key in weights:
            if key not in required_weights:
                _add(errors, f"scoring.weights 包含未知字段：{key}")
        for key in required_weights:
            if key in weights:
                _as_number(weights[key], f"scoring.weights.{key}", errors, min_value=0)

    thresholds = data.get("thresholds", {})
    if thresholds is None:
        thresholds = {}
    if not isinstance(thresholds, dict):
        _add(errors, "scoring.thresholds 必须是映射")
    else:
        allowed_thresholds = {
            "excellent_latency_ms", "bad_latency_ms", "bad_jitter_ms",
            "excellent_tcp_latency_ms", "bad_tcp_latency_ms",
        }
        for key in thresholds:
            if key not in allowed_thresholds:
                _add(errors, f"scoring.thresholds 包含未知字段：{key}")
            else:
                _as_number(thresholds[key], f"scoring.thresholds.{key}", errors, min_value=1)
        excellent_latency = thresholds.get("excellent_latency_ms")
        bad_latency = thresholds.get("bad_latency_ms")
        if excellent_latency is not None and bad_latency is not None:
            try:
                if float(bad_latency) <= float(excellent_latency):
                    _add(errors, "scoring.thresholds.bad_latency_ms 必须大于 excellent_latency_ms")
            except (TypeError, ValueError):
                pass
        excellent_tcp = thresholds.get("excellent_tcp_latency_ms")
        bad_tcp = thresholds.get("bad_tcp_latency_ms")
        if excellent_tcp is not None and bad_tcp is not None:
            try:
                if float(bad_tcp) <= float(excellent_tcp):
                    _add(errors, "scoring.thresholds.bad_tcp_latency_ms 必须大于 excellent_tcp_latency_ms")
            except (TypeError, ValueError):
                pass

    defaults = data.get("defaults", {})
    if defaults is None:
        defaults = {}
    if not isinstance(defaults, dict):
        _add(errors, "scoring.defaults 必须是映射")
    else:
        allowed_defaults = {"missing_tcp_score", "missing_history_score"}
        for key in defaults:
            if key not in allowed_defaults:
                _add(errors, f"scoring.defaults 包含未知字段：{key}")
                continue
            value = _as_number(defaults[key], f"scoring.defaults.{key}", errors, min_value=0)
            if value is not None and value > 1:
                _add(errors, f"scoring.defaults.{key} 必须 <= 1")

    return errors


def validate_scoring_warnings(path: str) -> List[str]:
    warnings: List[str] = []
    p = Path(path)
    if not p.exists():
        return []
    try:
        data = _load_yaml(p) or {}
    except Exception:
        return []
    if not isinstance(data, dict):
        return []

    weights = data.get("weights", {})
    if weights is None or not isinstance(weights, dict):
        return []

    required_weights = {"latency", "jitter", "tcp", "protocol_history", "source_history"}
    total = 0.0
    usable = False
    for key in required_weights:
        if key not in weights:
            continue
        try:
            total += float(weights[key])
            usable = True
        except (TypeError, ValueError):
            return []

    if usable and abs(total - 100.0) > 1e-6:
        warnings.append(f"scoring.weights 当前总和为 {total:g}，建议保持 100，便于分数解释和横向对比")
    return warnings


def validate_filter_rules(path: str) -> List[str]:
    errors: List[str] = []
    p = Path(path)
    if not p.exists():
        return []
    try:
        data = _load_yaml(p) or {}
    except Exception as exc:
        return [f"filter_rules.yaml 解析失败：{exc}"]
    if not isinstance(data, dict):
        return ["filter_rules.yaml 必须是映射"]
    if "enabled" in data and not isinstance(data.get("enabled"), bool):
        _add(errors, "filter_rules.enabled 必须是布尔值")
    mode = data.get("mode", "block")
    if mode not in {"block", "annotate"}:
        _add(errors, "filter_rules.mode 必须是 block 或 annotate")
    blocked = data.get("blocked", {})
    if blocked is None:
        blocked = {}
    if not isinstance(blocked, dict):
        return errors + ["filter_rules.blocked 必须是映射"]

    for port in _as_list(blocked.get("ports"), "blocked.ports", errors):
        try:
            port_i = int(port)
            if not 0 <= port_i <= 65535:
                _add(errors, f"blocked.ports 超出范围：{port}")
        except (TypeError, ValueError):
            _add(errors, f"blocked.ports 必须包含整数：{port}")

    for key in ("ssr_methods", "ss_methods", "vmess_security", "vmess_network"):
        for item in _as_list(blocked.get(key), f"blocked.{key}", errors):
            if not str(item).strip():
                _add(errors, f"blocked.{key} 包含空值")

    for proto in _as_list(blocked.get("protocols"), "blocked.protocols", errors):
        if str(proto).lower() not in SUPPORTED_PROTOCOLS:
            _add(errors, f"blocked.protocols 包含不支持的协议：{proto}")
    return errors


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--sources", default="config/sources.yaml")
    parser.add_argument("--filter-rules", default="config/filter_rules.yaml")
    parser.add_argument("--scoring-rules", default="config/scoring.yaml")
    args = parser.parse_args()

    errors = (
        validate_sources(args.sources)
        + validate_filter_rules(args.filter_rules)
        + validate_scoring_rules(args.scoring_rules)
    )
    warnings = validate_scoring_warnings(args.scoring_rules)
    for warning in warnings:
        print(f"配置警告：{warning}", file=sys.stderr)

    if errors:
        print("配置校验失败：", file=sys.stderr)
        for err in errors:
            print(f"- {err}", file=sys.stderr)
        raise SystemExit(1)
    print("配置校验通过")


if __name__ == "__main__":
    main()