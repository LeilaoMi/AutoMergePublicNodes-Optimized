# 资源导航

本页聚合与公共节点筛选、订阅转换、客户端排障相关的常用资源。

## 本地测速 / 二次筛选

- 本仓库：`tools/local_filter.py`
- subs-check：适合批量检测多协议订阅
- LiteSpeedTest：适合生成本地测速结果
- stairspeedtest-reborn：传统测速工具
- nodescatch：节点抓取与筛选工具

建议流程：

```text
all.* 候选池 -> local_filter.py TCP 筛选 -> 客户端/第三方工具真实测速 -> 保留本地可用节点
```

## 订阅转换

- 本仓库：`output/*.converter.md`
- subconverter：建议本地自建，减少第三方记录订阅 URL 的风险
- sub-web / sub-web-v4：适合临时转换

## 客户端

| 平台 | 推荐客户端 | 推荐订阅 |
|---|---|---|
| Windows | v2rayN / Clash Verge Rev | `verified.txt` / `verified.yaml` |
| macOS | Clash Verge Rev / Karing | `verified.yaml` / `verified.json` |
| Linux | Clash Verge Rev / sing-box | `verified.yaml` / `verified.json` |
| Android | v2rayNG / NekoBox / Karing | `verified.txt` / `verified.json` |
| iOS | Shadowrocket / Quantumult X / Loon | 转换链接或本地 subconverter |

## 出口 IP / DNS / 泄漏检测

- https://ipinfo.io/
- https://browserleaks.com/
- https://ipleak.net/
- https://ipleak.org/
- https://www.dnsleaktest.com/
- https://test-ipv6.com/
- https://whoer.net/
- https://whatismyipaddress.com/blacklist-check

## 排障建议

1. 先确认客户端内核支持协议，例如 Reality / Hysteria2 / TUIC。
2. 再确认订阅是否成功更新。
3. 再看节点是否只是 TCP 可达但真实代理失败。
4. 国内网络环境建议运行 `tools/local_filter.py` 后再导入。
5. 如果使用第三方转换服务失败，优先尝试直接导入本仓库生成的 `.yaml` / `.json` / `.txt`。