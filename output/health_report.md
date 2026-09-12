# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-12 20:34:22 |
| 运行耗时 | 621.1s |
| 订阅源总数 | 107 |
| 健康订阅源 | 94 |
| 原始节点 | 83799 |
| 去重后节点 | 23044 |
| TCP 可达 | 3000 |
| 真实可用 | 462 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23044 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.7 |
| geo | 1.6 |
| tcp | 37.7 |
| probe | 240.0 |
| real_test | 252.8 |
| generate | 81.4 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 50960 |
| vmess | 12594 |
| shadowsocks | 9733 |
| trojan | 8028 |
| hysteria2 | 1673 |
| http | 614 |
| shadowsocksr | 126 |
| socks | 53 |
| hysteria | 8 |
| tuic | 8 |
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
| 81.87 | vless | 194.1 | 482.9 | 23.28 | 0.0 | 10.0 | 9.99 | 18.6 | Au1rxx-base64 | 172.235.43.210 |
| 81.63 | vless | 204.6 | 518.5 | 23.04 | 0.0 | 10.0 | 9.99 | 18.6 | Au1rxx-base64 | 172.235.38.85 |
| 81.62 | vless | 205.2 | 504.6 | 23.03 | 0.0 | 10.0 | 9.99 | 18.6 | Au1rxx-base64 | 172.233.139.46 |
| 81.44 | shadowsocks | 198.2 | 475.7 | 23.19 | 0.0 | 10.0 | 14.15 | 18.6 | Au1rxx-base64 | 108.181.0.177 |
| 78.78 | vless | 241.4 | 525.3 | 22.19 | 0.0 | 10.0 | 9.99 | 18.6 | Au1rxx-base64 | 150.241.102.181 |
| 78.78 | vless | 257.3 | 525.3 | 21.82 | 0.0 | 10.0 | 9.99 | 18.6 | Au1rxx-base64 | 144.172.104.26 |
| 77.2 | vless | 396.1 | 1058.3 | 18.61 | 0.0 | 10.0 | 9.99 | 18.6 | Au1rxx-base64 | 51.81.203.63 |
| 75.9 | hysteria2 | 265.4 | 747.2 | 21.63 | 0.0 | 10.0 | 11.67 | 18.6 | Au1rxx-base64 | 107.175.219.48 |
| 75.69 | shadowsocks | 222.9 | 533.4 | 22.62 | 0.0 | 10.0 | 14.15 | 12.92 | mheidari-all | 173.244.56.6 |
| 75.59 | shadowsocks | 205.5 | 489.8 | 23.02 | 0.0 | 10.0 | 14.15 | 12.92 | mheidari-all | 108.181.118.10 |
| 74.65 | shadowsocks | 267.8 | 652.5 | 21.58 | 0.0 | 10.0 | 14.15 | 12.92 | mheidari-all | 149.22.95.183 |
| 74.29 | shadowsocks | 283.4 | 700.1 | 21.22 | 0.0 | 10.0 | 14.15 | 12.92 | mheidari-all | 173.244.56.9 |
| 74.1 | trojan | 386.5 | 868.2 | 18.83 | 0.0 | 10.0 | 13.56 | 18.6 | Au1rxx-base64 | 64.94.95.118 |
| 73.93 | trojan | 399.0 | 927.8 | 18.54 | 0.0 | 10.0 | 13.56 | 18.6 | Au1rxx-base64 | 64.94.95.114 |
| 73.32 | vless | 314.2 | 820.9 | 20.51 | 0.0 | 10.0 | 9.99 | 15.82 | DeltaKronecker-all | 107.173.237.146 |
| 73.28 | hysteria2 | 356.9 | 695.5 | 19.52 | 0.0 | 10.0 | 11.67 | 18.6 | Au1rxx-base64 | 159.223.157.129 |
| 72.42 | vless | 386.7 | 1039.2 | 18.83 | 0.0 | 10.0 | 9.99 | 18.6 | Au1rxx-base64 | 15.204.97.195 |
| 72.22 | vless | 253.7 | 601.6 | 21.91 | 0.0 | 10.0 | 9.99 | 15.82 | DeltaKronecker-all | 104.18.46.234 |
| 72.18 | vless | 202.6 | 479.2 | 23.09 | 0.0 | 10.0 | 9.99 | 18.6 | Au1rxx-base64 | 172.64.229.170 |
| 71.99 | vless | 379.6 | 753.3 | 18.99 | 0.0 | 10.0 | 9.99 | 18.6 | Au1rxx-base64 | 216.152.147.28 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| mheidari-all | 0.982 | 0.918 | 49 | 15722 | prefer |
| Au1rxx-base64 | 0.893 | 0.829 | 322 | 1650 | prefer |
| DeltaKronecker-all | 0.704 | 0.626 | 179 | 5970 | prefer |
| Surfboard-tg-mixed | 0.58 | 0.5 | 56 | 7382 | observe |
| ermaozi | 0.43 | 0.421 | 19 | 393 | observe |
| tg-oneclickvpnkeys | 0.261 | 1.0 | 1 | 161 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4793 | observe |
| Epodonios-all | 0.255 | None | 0 | 7802 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 8908 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5991 | observe |
| barry-far-vless | 0.255 | None | 0 | 6127 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4295 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.241 | None | 0 | 1650 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | TimeoutError | - | 43 |
| geo | ClientOSError | - | 42 |
| cn-block | TimeoutError | - | 23 |
| 204 | ProxyError | - | 19 |
| speed | ClientOSError | - | 17 |
| cn-block | ClientOSError | - | 7 |
| speed | TimeoutError | - | 6 |
| 204 | ClientOSError | - | 5 |
| geo | TimeoutError | - | 5 |
| 204 | ProxyConnectionError | - | 1 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
