# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-16 16:45:41 |
| 运行耗时 | 707.4s |
| 订阅源总数 | 107 |
| 健康订阅源 | 96 |
| 原始节点 | 89601 |
| 去重后节点 | 24453 |
| TCP 可达 | 3000 |
| 真实可用 | 416 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 24453 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.4 |
| geo | 1.5 |
| tcp | 41.9 |
| probe | 282.7 |
| real_test | 243.0 |
| generate | 133.9 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 53292 |
| vmess | 14355 |
| shadowsocks | 10573 |
| trojan | 9130 |
| hysteria2 | 1490 |
| http | 561 |
| shadowsocksr | 127 |
| socks | 60 |
| hysteria | 8 |
| tuic | 3 |
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
| 82.24 | vless | 201.0 | 517.8 | 23.13 | 0.0 | 10.0 | 10.79 | 18.32 | Au1rxx-base64 | 107.173.237.146 |
| 81.46 | hysteria2 | 237.6 | 542.7 | 22.28 | 0.0 | 10.0 | 12.6 | 18.32 | Au1rxx-base64 | 66.94.121.46 |
| 81.43 | hysteria2 | 180.0 | 476.4 | 23.61 | 0.0 | 10.0 | 12.6 | 16.22 | mheidari-all | 45.149.172.74 |
| 80.86 | vless | 260.6 | 637.0 | 21.75 | 0.0 | 10.0 | 10.79 | 18.32 | Au1rxx-base64 | 198.200.42.129 |
| 79.48 | shadowsocks | 259.1 | 626.5 | 21.78 | 0.0 | 10.0 | 13.77 | 18.32 | Au1rxx-base64 | 156.146.38.170 |
| 78.98 | vless | 221.6 | 504.2 | 22.65 | 0.0 | 10.0 | 10.79 | 15.54 | DeltaKronecker-all | 47.251.108.158 |
| 78.86 | shadowsocks | 281.1 | 725.2 | 21.27 | 0.0 | 10.0 | 13.77 | 18.32 | Au1rxx-base64 | 108.181.0.177 |
| 78.82 | vless | 250.5 | 503.4 | 21.98 | 0.0 | 10.0 | 10.79 | 18.32 | Au1rxx-base64 | 144.172.104.26 |
| 78.55 | shadowsocks | 304.9 | 760.4 | 20.72 | 0.0 | 10.0 | 13.77 | 18.32 | Au1rxx-base64 | 156.146.38.168 |
| 78.33 | shadowsocks | 234.8 | 538.9 | 22.34 | 0.0 | 10.0 | 13.77 | 16.22 | mheidari-all | 173.244.56.9 |
| 78.0 | shadowsocks | 301.2 | 743.2 | 20.81 | 0.0 | 10.0 | 13.77 | 18.32 | Au1rxx-base64 | 156.146.38.169 |
| 77.35 | vless | 195.9 | 497.2 | 23.24 | 0.0 | 10.0 | 10.79 | 18.32 | Au1rxx-base64 | 45.149.172.80 |
| 76.91 | shadowsocks | 230.4 | 544.5 | 22.44 | 0.0 | 10.0 | 13.77 | 14.7 | Surfboard-tg-mixed | 173.244.56.6 |
| 76.69 | shadowsocks | 284.4 | 724.5 | 21.2 | 0.0 | 10.0 | 13.77 | 16.22 | mheidari-all | 108.181.118.10 |
| 76.38 | shadowsocks | 253.1 | 601.9 | 21.92 | 0.0 | 10.0 | 13.77 | 14.7 | Surfboard-tg-mixed | 156.146.38.167 |
| 76.31 | hysteria2 | 197.5 | 474.7 | 23.2 | 0.0 | 10.0 | 12.6 | 16.22 | mheidari-all | 45.149.172.80 |
| 76.28 | vless | 355.7 | 847.5 | 19.54 | 0.0 | 10.0 | 10.79 | 18.32 | Au1rxx-base64 | 15.204.97.216 |
| 76.11 | shadowsocks | 267.6 | 547.0 | 21.58 | 0.0 | 10.0 | 13.77 | 18.32 | Au1rxx-base64 | 149.22.95.183 |
| 75.84 | vless | 302.2 | 550.9 | 20.78 | 0.0 | 10.0 | 10.79 | 18.32 | Au1rxx-base64 | 150.241.102.181 |
| 74.68 | vless | 218.1 | 509.1 | 22.73 | 0.0 | 10.0 | 10.79 | 18.32 | Au1rxx-base64 | 104.18.34.14 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.87 | 0.804 | 260 | 1702 | prefer |
| ermaozi | 0.842 | 0.852 | 27 | 353 | prefer |
| mheidari-all | 0.833 | 0.759 | 79 | 17973 | prefer |
| DeltaKronecker-all | 0.761 | 0.684 | 114 | 6081 | prefer |
| Surfboard-tg-mixed | 0.609 | 0.53 | 83 | 7470 | observe |
| mahdibland-V2RayAggregator | 0.335 | 1.0 | 1 | 4206 | observe |
| tg-oneclickvpnkeys | 0.263 | 1.0 | 1 | 207 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5115 | observe |
| Epodonios-all | 0.255 | None | 0 | 7938 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9093 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5979 | observe |
| barry-far-vless | 0.255 | None | 0 | 6195 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 2484 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | TimeoutError | - | 31 |
| geo | ClientOSError | - | 29 |
| cn-block | TimeoutError | - | 19 |
| geo | TimeoutError | - | 17 |
| speed | ClientOSError | - | 16 |
| 204 | ProxyError | - | 12 |
| cn-block | ClientOSError | - | 12 |
| speed | TimeoutError | - | 8 |
| cn-block | ProxyError | - | 4 |
| 204 | ClientOSError | - | 3 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
