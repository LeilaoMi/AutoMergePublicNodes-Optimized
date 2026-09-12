# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-12 10:36:24 |
| 运行耗时 | 639.5s |
| 订阅源总数 | 107 |
| 健康订阅源 | 94 |
| 原始节点 | 83079 |
| 去重后节点 | 22882 |
| TCP 可达 | 3000 |
| 真实可用 | 438 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22882 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.7 |
| geo | 1.4 |
| tcp | 37.9 |
| probe | 267.8 |
| real_test | 245.0 |
| generate | 81.7 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 50235 |
| vmess | 12626 |
| shadowsocks | 9809 |
| trojan | 7846 |
| hysteria2 | 1728 |
| http | 634 |
| shadowsocksr | 128 |
| socks | 50 |
| hysteria | 11 |
| tuic | 10 |
| anytls | 2 |

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
| 81.11 | shadowsocks | 246.9 | 593.9 | 22.06 | 0.0 | 10.0 | 14.09 | 18.96 | Au1rxx-base64 | 156.146.38.168 |
| 80.5 | shadowsocks | 253.1 | 626.0 | 21.92 | 0.0 | 10.0 | 14.09 | 18.96 | Au1rxx-base64 | 156.146.38.169 |
| 80.23 | shadowsocks | 284.9 | 713.7 | 21.18 | 0.0 | 10.0 | 14.09 | 18.96 | Au1rxx-base64 | 37.19.198.243 |
| 79.95 | shadowsocks | 296.9 | 747.5 | 20.9 | 0.0 | 10.0 | 14.09 | 18.96 | Au1rxx-base64 | 156.146.38.170 |
| 78.71 | shadowsocks | 241.5 | 593.0 | 22.19 | 0.0 | 10.0 | 14.09 | 18.96 | Au1rxx-base64 | 198.98.53.130 |
| 77.97 | vless | 254.0 | 659.4 | 21.9 | 0.0 | 10.0 | 7.11 | 18.96 | Au1rxx-base64 | 216.152.147.28 |
| 77.78 | trojan | 257.2 | 609.6 | 21.82 | 0.0 | 10.0 | 10.0 | 18.96 | Au1rxx-base64 | 64.94.95.114 |
| 77.62 | shadowsocks | 314.8 | 801.3 | 20.49 | 0.0 | 8.08 | 14.09 | 18.96 | Au1rxx-base64 | ca225.vpnbook.com |
| 77.22 | vless | 286.5 | 723.3 | 21.15 | 0.0 | 10.0 | 7.11 | 18.96 | Au1rxx-base64 | 47.253.226.114 |
| 76.96 | vless | 297.6 | 719.6 | 20.89 | 0.0 | 10.0 | 7.11 | 18.96 | Au1rxx-base64 | 169.40.42.184 |
| 76.95 | vless | 298.0 | 711.1 | 20.88 | 0.0 | 10.0 | 7.11 | 18.96 | Au1rxx-base64 | 169.40.42.16 |
| 76.75 | vless | 306.8 | 815.0 | 20.68 | 0.0 | 10.0 | 7.11 | 18.96 | Au1rxx-base64 | 79.141.172.154 |
| 76.03 | shadowsocks | 445.0 | 1184.6 | 17.48 | 0.0 | 10.0 | 14.09 | 18.96 | Au1rxx-base64 | 15.204.247.206 |
| 75.96 | shadowsocks | 391.6 | 981.4 | 18.71 | 0.0 | 10.0 | 14.09 | 18.96 | Au1rxx-base64 | 51.222.155.113 |
| 75.83 | hysteria2 | 272.3 | 674.7 | 21.48 | 0.0 | 10.0 | 13.85 | 11.6 | mheidari-all | 159.223.157.129 |
| 75.8 | vless | 334.3 | 694.2 | 20.04 | 0.0 | 10.0 | 7.11 | 18.96 | Au1rxx-base64 | 169.40.42.15 |
| 75.78 | shadowsocks | 345.0 | 801.8 | 19.79 | 0.0 | 10.0 | 14.09 | 18.96 | Au1rxx-base64 | 142.4.216.225 |
| 75.68 | shadowsocks | 301.2 | 632.3 | 20.81 | 0.0 | 10.0 | 14.09 | 18.96 | Au1rxx-base64 | 149.22.95.183 |
| 74.98 | trojan | 286.3 | 695.6 | 21.15 | 0.0 | 10.0 | 10.0 | 18.96 | Au1rxx-base64 | 64.94.95.118 |
| 74.9 | vless | 381.5 | 977.4 | 18.95 | 0.0 | 10.0 | 7.11 | 18.96 | Au1rxx-base64 | 185.95.231.156 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.894 | 0.832 | 286 | 1613 | prefer |
| mheidari-all | 0.695 | 0.617 | 94 | 15628 | observe |
| Surfboard-tg-mixed | 0.676 | 0.597 | 149 | 7286 | observe |
| DeltaKronecker-all | 0.605 | 0.526 | 38 | 5970 | observe |
| ermaozi | 0.573 | 0.558 | 52 | 434 | observe |
| tg-oneclickvpnkeys | 0.262 | 1.0 | 1 | 181 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4793 | observe |
| Epodonios-all | 0.255 | None | 0 | 7695 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5895 | observe |
| barry-far-vless | 0.255 | None | 0 | 6084 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4207 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.24 | None | 0 | 1613 | observe |
| ermaozi-get_subscribe | 0.23 | 0.25 | 12 | 459 | downweight |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | ClientOSError | - | 63 |
| 204 | ProxyError | - | 27 |
| 204 | TimeoutError | - | 17 |
| speed | TimeoutError | - | 17 |
| cn-block | TimeoutError | - | 16 |
| speed | ClientOSError | - | 15 |
| cn-block | ClientOSError | - | 13 |
| 204 | ProxyConnectionError | - | 12 |
| geo | TimeoutError | - | 8 |
| 204 | ClientOSError | - | 3 |
| geo | ProxyError | - | 3 |
| cn-block | ProxyError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
