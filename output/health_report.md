# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-20 20:43:53 |
| 运行耗时 | 521.5s |
| 订阅源总数 | 107 |
| 健康订阅源 | 94 |
| 原始节点 | 83660 |
| 去重后节点 | 23470 |
| TCP 可达 | 3000 |
| 真实可用 | 470 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23470 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.2 |
| geo | 1.5 |
| tcp | 38.0 |
| probe | 193.8 |
| real_test | 206.3 |
| generate | 75.9 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 49978 |
| vmess | 13607 |
| shadowsocks | 9915 |
| trojan | 8218 |
| hysteria2 | 1149 |
| http | 580 |
| shadowsocksr | 131 |
| socks | 66 |
| hysteria | 11 |
| tuic | 4 |
| anytls | 1 |

## 评分权重

| 因子 | 权重 |
| --- | --- |
| latency | 25.0 |
| jitter | 15.0 |
| tcp | 10.0 |
| speed | 10.0 |
| fingerprint_resistance | 5.0 |
| protocol_history | 15.0 |
| source_history | 20.0 |

## Top 节点评分

| 评分 | 协议 | 延迟(ms) | 抖动(ms) | 延迟分 | 抖动分 | TCP分 | 协议历史分 | 来源历史分 | 来源 | 服务器 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 82.19 | vless | 219.6 | 594.5 | 22.69 | 0.0 | 10.0 | 10.92 | 19.58 | Au1rxx-base64 | 195.211.98.43 |
| 81.14 | vless | 308.2 | 765.7 | 20.64 | 0.0 | 10.0 | 10.92 | 19.58 | Au1rxx-base64 | 185.95.231.156 |
| 81.07 | shadowsocks | 248.1 | 601.4 | 22.04 | 0.0 | 10.0 | 13.45 | 19.58 | Au1rxx-base64 | 156.146.38.168 |
| 80.91 | shadowsocks | 254.7 | 627.1 | 21.88 | 0.0 | 10.0 | 13.45 | 19.58 | Au1rxx-base64 | 156.146.38.167 |
| 80.82 | shadowsocks | 258.5 | 656.5 | 21.79 | 0.0 | 10.0 | 13.45 | 19.58 | Au1rxx-base64 | 37.19.198.160 |
| 80.58 | vless | 332.6 | 831.7 | 20.08 | 0.0 | 10.0 | 10.92 | 19.58 | Au1rxx-base64 | 169.40.42.90 |
| 80.31 | vless | 311.2 | 709.3 | 20.57 | 0.0 | 10.0 | 10.92 | 19.58 | Au1rxx-base64 | 169.40.42.95 |
| 80.26 | shadowsocks | 251.2 | 611.3 | 21.96 | 0.0 | 10.0 | 13.45 | 19.58 | Au1rxx-base64 | 156.146.38.170 |
| 80.01 | vless | 285.4 | 722.1 | 21.17 | 0.0 | 10.0 | 10.92 | 19.58 | Au1rxx-base64 | 79.141.172.154 |
| 79.78 | shadowsocks | 250.6 | 678.1 | 21.98 | 0.0 | 9.27 | 13.45 | 19.58 | Au1rxx-base64 | yyz-ca-01.blncvpn4u.cc |
| 79.14 | hysteria2 | 265.8 | 565.2 | 21.62 | 0.0 | 10.0 | 12.75 | 19.58 | Au1rxx-base64 | 66.94.121.46 |
| 78.9 | vless | 405.0 | 1032.6 | 18.4 | 0.0 | 10.0 | 10.92 | 19.58 | Au1rxx-base64 | 169.40.42.173 |
| 78.87 | shadowsocks | 270.9 | 627.3 | 21.51 | 0.0 | 10.0 | 13.45 | 19.58 | Au1rxx-base64 | 23.150.248.20 |
| 78.87 | vless | 277.0 | 685.3 | 21.37 | 0.0 | 10.0 | 10.92 | 19.58 | Au1rxx-base64 | 34.85.179.6 |
| 78.55 | vless | 304.2 | 691.8 | 20.74 | 0.0 | 10.0 | 10.92 | 19.58 | Au1rxx-base64 | 169.40.42.16 |
| 78.05 | vless | 330.0 | 690.9 | 20.14 | 0.0 | 10.0 | 10.92 | 19.58 | Au1rxx-base64 | 169.40.42.35 |
| 77.89 | vless | 300.4 | 681.3 | 20.83 | 0.0 | 10.0 | 10.92 | 19.58 | Au1rxx-base64 | 169.40.42.179 |
| 77.71 | shadowsocks | 263.4 | 672.5 | 21.68 | 0.0 | 10.0 | 13.45 | 19.58 | Au1rxx-base64 | 37.19.198.236 |
| 77.56 | vless | 384.5 | 861.9 | 18.88 | 0.0 | 10.0 | 10.92 | 19.58 | Au1rxx-base64 | 169.40.42.133 |
| 77.51 | vless | 375.4 | 833.2 | 19.09 | 0.0 | 10.0 | 10.92 | 19.58 | Au1rxx-base64 | 169.40.42.15 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.971 | 0.909 | 275 | 1621 | prefer |
| DeltaKronecker-all | 0.926 | 0.875 | 24 | 6092 | prefer |
| ermaozi | 0.897 | 0.917 | 24 | 314 | prefer |
| mheidari-all | 0.701 | 0.625 | 56 | 16265 | prefer |
| Surfboard-tg-mixed | 0.681 | 0.602 | 226 | 7207 | observe |
| tg-oneclickvpnkeys | 0.403 | 1.0 | 4 | 74 | observe |
| mahdibland-V2RayAggregator | 0.335 | 1.0 | 1 | 4315 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| Epodonios-all | 0.255 | None | 0 | 7615 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 8753 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5768 | observe |
| barry-far-vless | 0.255 | None | 0 | 5924 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.238 | None | 0 | 1574 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | ClientOSError | - | 30 |
| 204 | TimeoutError | - | 28 |
| geo | TimeoutError | - | 23 |
| cn-block | TimeoutError | - | 20 |
| 204 | ProxyError | - | 13 |
| speed | ClientOSError | - | 10 |
| cn-block | ClientOSError | - | 9 |
| speed | TimeoutError | - | 9 |
| cn-block | ProxyError | - | 2 |
| 204 | ClientOSError | - | 2 |
| geo | ProxyError | - | 1 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
