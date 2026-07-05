# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-05 09:17:14 |
| 运行耗时 | 203.3s |
| 订阅源总数 | 107 |
| 健康订阅源 | 103 |
| 原始节点 | 79402 |
| 去重后节点 | 23931 |
| TCP 可达 | 3000 |
| 真实可用 | 367 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23931 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.7 |
| geo | 5.5 |
| tcp | 30.9 |
| probe | 49.2 |
| real_test | 75.6 |
| generate | 37.4 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 46286 |
| trojan | 12369 |
| vmess | 10440 |
| shadowsocks | 9498 |
| hysteria2 | 461 |
| shadowsocksr | 153 |
| http | 135 |
| socks | 48 |
| hysteria | 6 |
| tuic | 6 |

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
| 78.15 | shadowsocks | 220.5 | 596.5 | 22.67 | 0.0 | 10.0 | 13.38 | 16.1 | Au1rxx-base64 | 198.98.53.130 |
| 77.97 | shadowsocks | 228.4 | 633.3 | 22.49 | 0.0 | 10.0 | 13.38 | 16.1 | Au1rxx-base64 | 37.19.198.244 |
| 77.87 | shadowsocks | 232.9 | 644.6 | 22.39 | 0.0 | 10.0 | 13.38 | 16.1 | Au1rxx-base64 | 37.19.198.236 |
| 77.81 | shadowsocks | 235.3 | 657.2 | 22.33 | 0.0 | 10.0 | 13.38 | 16.1 | Au1rxx-base64 | 37.19.198.160 |
| 77.08 | shadowsocks | 245.4 | 652.9 | 22.1 | 0.0 | 10.0 | 13.38 | 16.1 | Au1rxx-base64 | 108.181.57.93 |
| 76.46 | trojan | 344.3 | 596.1 | 19.81 | 0.0 | 10.0 | 13.75 | 17.44 | Surfboard-tg-mixed | 104.26.15.137 |
| 75.93 | shadowsocks | 230.3 | 633.5 | 22.45 | 0.0 | 10.0 | 13.38 | 16.1 | Au1rxx-base64 | 37.19.198.243 |
| 75.25 | shadowsocks | 274.5 | 632.3 | 21.42 | 0.0 | 10.0 | 13.38 | 16.1 | Au1rxx-base64 | 156.146.38.169 |
| 75.2 | trojan | 291.9 | 651.0 | 21.02 | 0.0 | 10.0 | 13.75 | 15.96 | DeltaKronecker-all | 64.94.95.114 |
| 74.96 | shadowsocks | 270.9 | 627.4 | 21.51 | 0.0 | 10.0 | 13.38 | 16.1 | Au1rxx-base64 | 156.146.38.170 |
| 74.87 | shadowsocks | 284.8 | 664.8 | 21.19 | 0.0 | 10.0 | 13.38 | 16.1 | Au1rxx-base64 | 156.146.38.168 |
| 74.2 | shadowsocks | 315.0 | 755.6 | 20.49 | 0.0 | 10.0 | 13.38 | 16.1 | Au1rxx-base64 | 156.146.38.167 |
| 73.85 | trojan | 403.8 | 976.6 | 18.43 | 0.0 | 10.0 | 13.75 | 19.08 | mheidari-all | 64.94.95.118 |
| 73.58 | trojan | 326.8 | 747.4 | 20.21 | 0.0 | 10.0 | 13.75 | 15.96 | DeltaKronecker-all | 45.32.195.168 |
| 73.45 | trojan | 364.5 | 867.3 | 19.34 | 0.0 | 10.0 | 13.75 | 15.96 | DeltaKronecker-all | 64.94.95.117 |
| 73.24 | trojan | 332.1 | 773.7 | 20.09 | 0.0 | 10.0 | 13.75 | 15.96 | DeltaKronecker-all | 45.32.198.247 |
| 73.08 | trojan | 333.4 | 774.1 | 20.06 | 0.0 | 10.0 | 13.75 | 15.96 | DeltaKronecker-all | 64.94.95.115 |
| 71.74 | trojan | 413.7 | 1016.9 | 18.2 | 0.0 | 10.0 | 13.75 | 15.96 | DeltaKronecker-all | 149.28.241.235 |
| 71.36 | trojan | 476.3 | 816.9 | 16.75 | 0.0 | 10.0 | 13.75 | 19.08 | mheidari-all | 172.64.147.166 |
| 71.27 | trojan | 471.5 | 807.2 | 16.86 | 0.0 | 10.0 | 13.75 | 19.08 | mheidari-all | 172.66.44.211 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| mheidari-all | 0.913 | 0.841 | 82 | 16512 | prefer |
| Surfboard-tg-mixed | 0.893 | 0.819 | 105 | 6080 | prefer |
| DeltaKronecker-all | 0.818 | 0.74 | 200 | 7739 | prefer |
| Au1rxx-base64 | 0.804 | 0.818 | 33 | 109 | prefer |
| nscl5-all | 0.308 | 1.0 | 1 | 1323 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4662 | observe |
| Epodonios-all | 0.255 | None | 0 | 7028 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3975 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6942 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4554 | observe |
| barry-far-vless | 0.255 | None | 0 | 5158 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5372 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 21 |
| 204 | ProxyError | - | 18 |
| 204 | ClientOSError | - | 15 |
| speed | ClientOSError | - | 11 |
| 204 | TimeoutError | - | 11 |
| geo | ClientOSError | - | 6 |
| cn-block | ClientOSError | - | 4 |
| cn-block | ProxyError | - | 2 |
| geo | ProxyError | - | 2 |
| cn-block | TimeoutError | - | 2 |
| speed | TimeoutError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
