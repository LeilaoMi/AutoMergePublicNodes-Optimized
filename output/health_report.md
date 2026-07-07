# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-07 20:07:04 |
| 运行耗时 | 189.6s |
| 订阅源总数 | 107 |
| 健康订阅源 | 102 |
| 原始节点 | 84823 |
| 去重后节点 | 24903 |
| TCP 可达 | 3000 |
| 真实可用 | 209 |
| Verified 输出 | 209 |
| Global 输出 | 217 |
| All 输出 | 24903 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.6 |
| geo | 1.3 |
| tcp | 31.9 |
| probe | 45.3 |
| real_test | 65.3 |
| generate | 41.2 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 50513 |
| trojan | 13191 |
| vmess | 10612 |
| shadowsocks | 9440 |
| hysteria2 | 715 |
| shadowsocksr | 145 |
| http | 140 |
| socks | 54 |
| hysteria | 8 |
| anytls | 3 |
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
| 76.53 | shadowsocks | 238.6 | 650.4 | 22.25 | 0.0 | 10.0 | 12.3 | 15.98 | Au1rxx-base64 | 37.19.198.160 |
| 76.25 | shadowsocks | 250.7 | 687.4 | 21.97 | 0.0 | 10.0 | 12.3 | 15.98 | Au1rxx-base64 | 37.19.198.243 |
| 76.04 | shadowsocks | 225.4 | 610.4 | 22.56 | 0.0 | 10.0 | 12.3 | 15.98 | Au1rxx-base64 | 198.98.53.130 |
| 75.46 | shadowsocks | 263.2 | 698.2 | 21.68 | 0.0 | 10.0 | 12.3 | 15.98 | Au1rxx-base64 | 108.181.57.93 |
| 75.4 | shadowsocks | 244.2 | 669.1 | 22.12 | 0.0 | 10.0 | 12.3 | 15.98 | Au1rxx-base64 | 37.19.198.244 |
| 74.82 | shadowsocks | 269.3 | 749.0 | 21.54 | 0.0 | 10.0 | 12.3 | 15.98 | Au1rxx-base64 | 37.19.198.236 |
| 72.84 | shadowsocks | 284.9 | 638.9 | 21.18 | 0.0 | 10.0 | 12.3 | 15.98 | Au1rxx-base64 | 156.146.38.169 |
| 72.78 | vmess | 391.4 | 1122.9 | 18.72 | 0.0 | 10.0 | 13.12 | 15.44 | Surfboard-tg-mixed | 67.220.95.3 |
| 72.45 | shadowsocks | 285.9 | 661.4 | 21.16 | 0.0 | 10.0 | 12.3 | 15.98 | Au1rxx-base64 | 156.146.38.168 |
| 72.35 | shadowsocks | 282.3 | 644.8 | 21.24 | 0.0 | 10.0 | 12.3 | 15.98 | Au1rxx-base64 | 156.146.38.170 |
| 72.08 | shadowsocks | 348.3 | 878.9 | 19.72 | 0.0 | 10.0 | 12.3 | 15.98 | Au1rxx-base64 | 185.196.61.82 |
| 71.7 | trojan | 338.4 | 784.7 | 19.95 | 0.0 | 10.0 | 10.83 | 16.14 | DeltaKronecker-all | 45.32.195.168 |
| 70.99 | trojan | 329.9 | 751.5 | 20.14 | 0.0 | 10.0 | 10.83 | 16.14 | DeltaKronecker-all | 45.32.198.247 |
| 70.39 | trojan | 345.0 | 763.8 | 19.79 | 0.0 | 10.0 | 10.83 | 15.44 | Surfboard-tg-mixed | 149.28.241.235 |
| 70.35 | trojan | 294.2 | 637.2 | 20.97 | 0.0 | 10.0 | 10.83 | 15.44 | Surfboard-tg-mixed | 64.94.95.118 |
| 69.43 | trojan | 392.6 | 892.2 | 18.69 | 0.0 | 10.0 | 10.83 | 16.14 | DeltaKronecker-all | 64.94.95.115 |
| 69.06 | trojan | 387.5 | 889.3 | 18.81 | 0.0 | 10.0 | 10.83 | 16.14 | DeltaKronecker-all | 64.94.95.117 |
| 68.98 | hysteria2 | 377.9 | 711.2 | 19.03 | 0.0 | 8.73 | 12.5 | 15.98 | Au1rxx-base64 | 62.210.124.146 |
| 68.44 | shadowsocks | 299.1 | 819.7 | 20.85 | 0.0 | 8.86 | 12.3 | 15.98 | Au1rxx-base64 | tinkered-pennies-puppies.freesocks.work |
| 68.04 | shadowsocks | 235.5 | 636.6 | 22.33 | 0.0 | 10.0 | 12.3 | 15.1 | mheidari-all | 147.90.234.133 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| Au1rxx-base64 | 0.844 | 0.854 | 48 | 104 | prefer |
| mheidari-all | 0.655 | 0.577 | 71 | 18207 | observe |
| Surfboard-tg-mixed | 0.646 | 0.568 | 74 | 6066 | observe |
| DeltaKronecker-all | 0.597 | 0.517 | 87 | 8472 | observe |
| xiaoji235-airport-v2ray-all | 0.349 | 0.667 | 3 | 3626 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| tg-LonUp_M | 0.262 | 1.0 | 1 | 170 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4700 | observe |
| Epodonios-all | 0.255 | None | 0 | 7120 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3970 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7035 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4596 | observe |
| barry-far-vless | 0.255 | None | 0 | 5281 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5339 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | ProxyError | - | 28 |
| 204 | TimeoutError | - | 21 |
| geo | TimeoutError | - | 14 |
| speed | ClientOSError | - | 8 |
| 204 | ClientOSError | - | 8 |
| cn-block | TimeoutError | - | 7 |
| geo | ClientOSError | - | 6 |
| cn-block | ClientOSError | - | 6 |
| cn-block | ProxyError | - | 5 |
| geo | ProxyError | - | 5 |
| speed | ProxyError | - | 3 |
| speed | TimeoutError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 284 | 209 | - |
| global | False | 293 | 217 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
