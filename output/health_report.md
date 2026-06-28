# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-06-28 09:24:07 |
| 运行耗时 | 274.7s |
| 订阅源总数 | 107 |
| 健康订阅源 | 105 |
| 原始节点 | 75942 |
| 去重后节点 | 22914 |
| TCP 可达 | 3000 |
| 真实可用 | 585 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22914 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.7 |
| geo | 1.4 |
| tcp | 30.4 |
| probe | 53.5 |
| real_test | 139.3 |
| generate | 45.4 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 42094 |
| trojan | 12644 |
| vmess | 11265 |
| shadowsocks | 9360 |
| hysteria2 | 231 |
| shadowsocksr | 160 |
| http | 135 |
| socks | 45 |
| hysteria | 6 |
| tuic | 2 |

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
| 75.8 | shadowsocks | 226.6 | 625.9 | 22.53 | 0.0 | 10.0 | 12.39 | 14.88 | Au1rxx-base64 | 37.19.198.244 |
| 75.79 | shadowsocks | 227.1 | 628.3 | 22.52 | 0.0 | 10.0 | 12.39 | 14.88 | Au1rxx-base64 | 37.19.198.236 |
| 75.76 | shadowsocks | 228.2 | 632.0 | 22.49 | 0.0 | 10.0 | 12.39 | 14.88 | Au1rxx-base64 | 37.19.198.160 |
| 75.7 | shadowsocks | 231.1 | 644.7 | 22.43 | 0.0 | 10.0 | 12.39 | 14.88 | Au1rxx-base64 | 37.19.198.243 |
| 73.69 | shadowsocks | 246.0 | 660.3 | 22.08 | 0.0 | 10.0 | 12.39 | 13.72 | mheidari-all | 108.181.57.93 |
| 72.7 | vless | 281.8 | 725.0 | 21.26 | 0.0 | 10.0 | 6.22 | 17.32 | Surfboard-tg-mixed | 104.18.42.68 |
| 72.66 | trojan | 279.3 | 619.4 | 21.31 | 0.0 | 10.0 | 12.99 | 13.72 | mheidari-all | 64.94.95.118 |
| 72.57 | shadowsocks | 278.3 | 643.1 | 21.33 | 0.0 | 10.0 | 12.39 | 14.88 | Au1rxx-base64 | 156.146.38.167 |
| 72.14 | shadowsocks | 286.3 | 659.0 | 21.15 | 0.0 | 10.0 | 12.39 | 14.88 | Au1rxx-base64 | 156.146.38.168 |
| 72.06 | trojan | 362.4 | 653.5 | 19.39 | 0.0 | 10.0 | 12.99 | 17.32 | Surfboard-tg-mixed | 94.140.0.100 |
| 71.55 | vless | 266.6 | 750.2 | 21.61 | 0.0 | 10.0 | 6.22 | 13.72 | mheidari-all | 47.253.226.114 |
| 71.3 | vless | 241.2 | 654.6 | 22.2 | 0.0 | 10.0 | 6.22 | 14.88 | Au1rxx-base64 | 159.89.87.21 |
| 71.2 | shadowsocks | 288.4 | 669.3 | 21.1 | 0.0 | 10.0 | 12.39 | 14.88 | Au1rxx-base64 | 156.146.38.170 |
| 71.09 | hysteria2 | 421.3 | 866.3 | 18.03 | 0.0 | 10.0 | 12.0 | 17.32 | Surfboard-tg-mixed | 103.251.167.168 |
| 70.01 | hysteria2 | 355.0 | 691.1 | 19.56 | 0.0 | 10.0 | 12.0 | 14.88 | Au1rxx-base64 | 62.210.124.146 |
| 69.66 | trojan | 455.0 | 813.7 | 17.25 | 0.0 | 10.0 | 12.99 | 17.32 | Surfboard-tg-mixed | 165.215.250.14 |
| 69.26 | shadowsocks | 273.1 | 630.3 | 21.46 | 0.0 | 10.0 | 12.39 | 14.88 | Au1rxx-base64 | 156.146.38.169 |
| 69.04 | vless | 438.6 | 1135.5 | 17.63 | 0.0 | 10.0 | 6.22 | 17.32 | Surfboard-tg-mixed | 15.223.121.250 |
| 69.04 | trojan | 468.2 | 804.3 | 16.94 | 0.0 | 10.0 | 12.99 | 17.32 | Surfboard-tg-mixed | 162.159.17.189 |
| 68.7 | trojan | 478.1 | 1035.0 | 16.71 | 0.0 | 10.0 | 12.99 | 17.32 | Surfboard-tg-mixed | 45.61.58.89 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| mheidari-all | 0.882 | 0.804 | 331 | 16289 | prefer |
| Surfboard-tg-mixed | 0.839 | 0.762 | 235 | 5004 | prefer |
| Au1rxx-base64 | 0.83 | 0.836 | 61 | 117 | prefer |
| DeltaKronecker-all | 0.682 | 0.605 | 86 | 6788 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4327 | observe |
| Epodonios-all | 0.255 | None | 0 | 7560 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3976 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6983 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 3679 | observe |
| barry-far-vless | 0.255 | None | 0 | 4456 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5325 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| xiaoji235-airport-v2ray-all | 0.225 | None | 0 | 1261 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 83 |
| geo | TimeoutError | - | 13 |
| 204 | TimeoutError | - | 13 |
| 204 | ProxyError | - | 12 |
| speed | TimeoutError | - | 12 |
| 204 | ClientOSError | - | 10 |
| cn-block | TimeoutError | - | 9 |
| cn-block | ClientOSError | - | 5 |
| geo | ClientOSError | - | 4 |
| geo | ProxyError | - | 3 |
| cn-block | ProxyError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
