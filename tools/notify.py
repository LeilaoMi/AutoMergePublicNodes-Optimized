#!/usr/bin/env python3
"""[P0-3] 告警通知器：连续降级、源死掉、verified 暴跌时主动通知。

支持:
  - Telegram Bot API（推荐；零依赖）
  - Webhook（兼容 Discord/Slack/Bark，自定义 JSON）
  - 文件落盘（CI 调试用）

所有发送失败都不抛异常，只打印 warning，避免通知本身把 CI 搞挂。
"""
from __future__ import annotations

import json
import os
import sys
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional


@dataclass
class NotifyConfig:
    telegram_token: Optional[str] = None
    telegram_chat_id: Optional[str] = None
    webhook_url: Optional[str] = None
    log_path: Optional[str] = None
    dry_run: bool = False

    @classmethod
    def from_env(cls) -> "NotifyConfig":
        return cls(
            telegram_token=os.environ.get("AUTONODES_TG_BOT_TOKEN"),
            telegram_chat_id=os.environ.get("AUTONODES_TG_CHAT_ID"),
            webhook_url=os.environ.get("AUTONODES_WEBHOOK_URL"),
            log_path=os.environ.get("AUTONODES_NOTIFY_LOG"),
            dry_run=os.environ.get("AUTONODES_NOTIFY_DRY_RUN", "").lower() in ("1", "true"),
        )

    @property
    def enabled(self) -> bool:
        return bool(
            (self.telegram_token and self.telegram_chat_id)
            or self.webhook_url
            or self.log_path
            or self.dry_run
        )


def _post_json(url: str, payload: Dict[str, Any], timeout: float = 5.0) -> bool:
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url, data=data, headers={"Content-Type": "application/json"}, method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return 200 <= resp.status < 300
    except Exception as exc:
        print(f"      ⚠️ notify POST failed: {exc}", file=sys.stderr)
        return False


def send_telegram(token: str, chat_id: str, text: str) -> bool:
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    return _post_json(url, {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "Markdown",
        "disable_web_page_preview": True,
    })


def send_webhook(url: str, title: str, message: str, severity: str) -> bool:
    return _post_json(url, {
        "title": title,
        "message": message,
        "severity": severity,
    })


def append_log(path: str, payload: Dict[str, Any]) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("a", encoding="utf-8") as f:
        f.write(json.dumps(payload, ensure_ascii=False) + "\n")


def notify(
    title: str,
    message: str,
    severity: str = "warning",
    config: Optional[NotifyConfig] = None,
) -> List[str]:
    """发出告警，返回已尝试的渠道列表。

    severity: info / warning / critical
    """
    cfg = config or NotifyConfig.from_env()
    if not cfg.enabled:
        return []

    text = f"[{severity.upper()}] {title}\n\n{message}"
    sent: List[str] = []

    if cfg.telegram_token and cfg.telegram_chat_id:
        if cfg.dry_run or send_telegram(cfg.telegram_token, cfg.telegram_chat_id, text):
            sent.append("telegram")

    if cfg.webhook_url:
        if cfg.dry_run or send_webhook(cfg.webhook_url, title, message, severity):
            sent.append("webhook")

    if cfg.log_path:
        try:
            append_log(cfg.log_path, {
                "title": title,
                "message": message,
                "severity": severity,
            })
            sent.append("log")
        except Exception as exc:
            print(f"      ⚠️ notify log write failed: {exc}", file=sys.stderr)

    if not sent and not cfg.dry_run:
        print(f"      ⚠️ notify enabled but no channel succeeded: {title}", file=sys.stderr)
    elif sent:
        print(f"      📣 notify sent via {sent}: {title}")
    return sent


# === 业务告警模板 ===

def notify_degraded_run(consecutive: int, verified_count: int) -> None:
    """连续降级告警。consecutive >= 3 触发 critical。"""
    if consecutive < 2:
        return
    severity = "critical" if consecutive >= 3 else "warning"
    notify(
        title=f"AutoMergePublicNodes 进入降级模式（连续 {consecutive} 轮）",
        message=(
            f"verified 输出为 0，连续 {consecutive} 轮触发降级。\n"
            f"本轮 verified 数量: {verified_count}\n"
            "可能原因：sing-box 测试目标不可达 / 公开节点池枯竭 / CI runner IP 被风控。\n"
            "排查：查看 output/health_report.md 与 output/stats.json。"
        ),
        severity=severity,
    )


def notify_source_died(source: str, consecutive: int) -> None:
    """源连续死亡告警。"""
    if consecutive < 3:
        return
    notify(
        title=f"订阅源 {consecutive} 轮无节点",
        message=(
            f"源 `{source}` 已连续 {consecutive} 轮抓取 0 节点。\n"
            "建议：运行 `python tools/suggest_source_cleanup.py --apply --only " + source + "` 禁用。"
        ),
        severity="warning",
    )


def notify_verified_drop(previous: int, current: int, ratio: float) -> None:
    """verified 暴跌告警。"""
    if ratio > 0.5 or previous <= 0:
        return
    notify(
        title=f"verified 暴跌 {int(ratio * 100)}%",
        message=(
            f"verified 输出: {previous} → {current}（下降 {int((1 - ratio) * 100)}%）\n"
            "可能原因：真测目标不可达 / sing-box 升级不兼容。\n"
            "排查：查看 output/health_report.md。"
        ),
        severity="critical",
    )


# === 退化计数器（持久化）===

DEGRADED_COUNTER_PATH = "output/.degraded_counter"


def read_degraded_counter() -> int:
    p = Path(DEGRADED_COUNTER_PATH)
    if not p.exists():
        return 0
    try:
        return int(p.read_text(encoding="utf-8").strip() or 0)
    except Exception:
        return 0


def write_degraded_counter(value: int) -> None:
    p = Path(DEGRADED_COUNTER_PATH)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(str(int(value)), encoding="utf-8")


def main() -> int:
    """CLI：手动发送测试通知。"""
    p = argparse.ArgumentParser()
    p.add_argument("--title", default="[TEST] AutoMergePublicNodes notification")
    p.add_argument("--message", default="这是一条测试通知。")
    p.add_argument("--severity", default="info", choices=("info", "warning", "critical"))
    args = p.parse_args()
    sent = notify(args.title, args.message, args.severity)
    print(f"sent via: {sent}")
    return 0 if sent else 1


if __name__ == "__main__":
    import argparse
    sys.exit(main())
