#!/usr/bin/env python3
"""Validate project configuration files without network access."""
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
        return [f"missing sources file: {path}"]
    try:
        data = _load_yaml(p) or {}
    except Exception as exc:
        return [f"sources yaml parse failed: {exc}"]
    sources = data.get("sources") if isinstance(data, dict) else None
    if not isinstance(sources, list):
        return ["sources.yaml must contain a list field: sources"]

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
                _add(errors, f"{label}.enabled must be boolean")
            if "max_nodes" in entry:
                try:
                    max_nodes = int(entry.get("max_nodes"))
                    if max_nodes < 0:
                        _add(errors, f"{label}.max_nodes must be >= 0")
                except (TypeError, ValueError):
                    _add(errors, f"{label}.max_nodes must be integer")
            ignore_protocols = entry.get("ignore_protocols", [])
            if ignore_protocols is not None and not isinstance(ignore_protocols, list):
                _add(errors, f"{label}.ignore_protocols must be a list")
            elif isinstance(ignore_protocols, list):
                for proto in ignore_protocols:
                    if str(proto).lower() not in SUPPORTED_PROTOCOLS:
                        _add(errors, f"{label}.ignore_protocols has unsupported protocol: {proto}")
        else:
            _add(errors, f"{label} must be string or mapping")
            continue

        if not url:
            _add(errors, f"{label}.url is empty")
        elif not URL_RE.match(url):
            _add(errors, f"{label}.url must start with http:// or https://: {url}")
        if kind not in SUPPORTED_KINDS:
            _add(errors, f"{label}.kind unsupported: {kind}")
        if url in seen_urls:
            _add(errors, f"duplicate source url: {url}")
        seen_urls.add(url)
        if name:
            if name in seen_names:
                _add(errors, f"duplicate source name: {name}")
            seen_names.add(name)
    return errors


def _as_list(value: Any, label: str, errors: List[str]) -> List[Any]:
    if value is None:
        return []
    if not isinstance(value, list):
        _add(errors, f"{label} must be a list")
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
        return [f"filter rules yaml parse failed: {exc}"]
    if not isinstance(data, dict):
        return ["filter_rules.yaml must be a mapping"]
    if "enabled" in data and not isinstance(data.get("enabled"), bool):
        _add(errors, "filter_rules.enabled must be boolean")
    mode = data.get("mode", "block")
    if mode not in {"block", "annotate"}:
        _add(errors, "filter_rules.mode must be block or annotate")
    blocked = data.get("blocked", {})
    if blocked is None:
        blocked = {}
    if not isinstance(blocked, dict):
        return errors + ["filter_rules.blocked must be a mapping"]

    for port in _as_list(blocked.get("ports"), "blocked.ports", errors):
        try:
            port_i = int(port)
            if not 0 <= port_i <= 65535:
                _add(errors, f"blocked.ports out of range: {port}")
        except (TypeError, ValueError):
            _add(errors, f"blocked.ports must contain integers: {port}")

    for key in ("ssr_methods", "ss_methods", "vmess_security", "vmess_network"):
        for item in _as_list(blocked.get(key), f"blocked.{key}", errors):
            if not str(item).strip():
                _add(errors, f"blocked.{key} contains empty value")

    for proto in _as_list(blocked.get("protocols"), "blocked.protocols", errors):
        if str(proto).lower() not in SUPPORTED_PROTOCOLS:
            _add(errors, f"blocked.protocols has unsupported protocol: {proto}")
    return errors


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--sources", default="config/sources.yaml")
    parser.add_argument("--filter-rules", default="config/filter_rules.yaml")
    args = parser.parse_args()

    errors = validate_sources(args.sources) + validate_filter_rules(args.filter_rules)
    if errors:
        print("configuration validation failed:", file=sys.stderr)
        for err in errors:
            print(f"- {err}", file=sys.stderr)
        raise SystemExit(1)
    print("configuration validation passed")


if __name__ == "__main__":
    main()