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
    args = parser.parse_args()

    errors = validate_sources(args.sources) + validate_filter_rules(args.filter_rules)
    if errors:
        print("配置校验失败：", file=sys.stderr)
        for err in errors:
            print(f"- {err}", file=sys.stderr)
        raise SystemExit(1)
    print("配置校验通过")


if __name__ == "__main__":
    main()