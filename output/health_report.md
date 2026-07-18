# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-18 08:06:36 |
| 运行耗时 | 347.2s |
| 订阅源总数 | 107 |
| 健康订阅源 | 98 |
| 原始节点 | 80195 |
| 去重后节点 | 21663 |
| TCP 可达 | 3000 |
| 真实可用 | 835 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 21663 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.9 |
| geo | 1.3 |
| tcp | 31.2 |
| probe | 67.7 |
| real_test | 207.3 |
| generate | 34.8 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 47138 |
| trojan | 11258 |
| vmess | 10730 |
| shadowsocks | 10466 |
| hysteria2 | 312 |
| shadowsocksr | 124 |
| socks | 99 |
| http | 54 |
| hysteria | 9 |
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
| 80.0 | shadowsocks | 229.7 | 631.3 | 22.46 | 0.0 | 10.0 | 13.82 | 17.72 | Au1rxx-base64 | 37.19.198.243 |
| 79.99 | shadowsocks | 230.4 | 636.7 | 22.45 | 0.0 | 10.0 | 13.82 | 17.72 | Au1rxx-base64 | 37.19.198.244 |
| 79.93 | shadowsocks | 232.8 | 647.1 | 22.39 | 0.0 | 10.0 | 13.82 | 17.72 | Au1rxx-base64 | 37.19.198.236 |
| 78.99 | shadowsocks | 230.0 | 636.0 | 22.45 | 0.0 | 10.0 | 13.82 | 17.72 | Au1rxx-base64 | 37.19.198.160 |
| 76.78 | shadowsocks | 283.6 | 650.4 | 21.21 | 0.0 | 10.0 | 13.82 | 17.72 | Au1rxx-base64 | 156.146.38.169 |
| 76.59 | shadowsocks | 287.0 | 657.8 | 21.13 | 0.0 | 10.0 | 13.82 | 17.72 | Au1rxx-base64 | 156.146.38.168 |
| 76.32 | shadowsocks | 275.8 | 624.6 | 21.39 | 0.0 | 10.0 | 13.82 | 17.72 | Au1rxx-base64 | 156.146.38.167 |
| 76.28 | shadowsocks | 274.8 | 615.7 | 21.42 | 0.0 | 10.0 | 13.82 | 17.72 | Au1rxx-base64 | 156.146.38.170 |
| 74.9 | shadowsocks | 316.8 | 587.8 | 20.44 | 0.0 | 10.0 | 13.82 | 15.14 | mheidari-all | 68.168.222.210 |
| 74.64 | shadowsocks | 328.2 | 899.8 | 20.18 | 0.0 | 10.0 | 13.82 | 15.14 | mheidari-all | 108.181.57.93 |
| 74.57 | shadowsocks | 331.1 | 864.2 | 20.11 | 0.0 | 10.0 | 13.82 | 15.14 | mheidari-all | 50.114.177.235 |
| 73.19 | shadowsocks | 307.3 | 581.8 | 20.66 | 0.0 | 10.0 | 13.82 | 17.72 | Au1rxx-base64 | 173.244.56.6 |
| 72.96 | hysteria2 | 407.6 | 843.0 | 18.34 | 0.0 | 10.0 | 12.0 | 19.08 | nscl5-all | 62.210.124.146 |
| 72.95 | shadowsocks | 345.1 | 866.8 | 19.79 | 0.0 | 10.0 | 13.82 | 15.14 | mheidari-all | 185.196.61.82 |
| 72.85 | shadowsocks | 232.7 | 603.6 | 22.39 | 0.0 | 10.0 | 13.82 | 15.14 | mheidari-all | 198.98.53.130 |
| 71.0 | shadowsocks | 369.4 | 719.1 | 19.23 | 0.0 | 10.0 | 13.82 | 17.72 | Au1rxx-base64 | 108.181.118.10 |
| 69.82 | shadowsocks | 414.3 | 846.9 | 18.19 | 0.0 | 10.0 | 13.82 | 17.72 | Au1rxx-base64 | 108.181.0.177 |
| 69.34 | trojan | 438.4 | 768.8 | 17.63 | 0.0 | 10.0 | 14.56 | 15.14 | mheidari-all | 104.17.121.9 |
| 68.89 | shadowsocks | 291.4 | 805.0 | 21.03 | 0.0 | 10.0 | 13.82 | 15.14 | mheidari-all | 147.90.234.133 |
| 68.89 | trojan | 453.3 | 787.0 | 17.28 | 0.0 | 10.0 | 14.56 | 15.14 | mheidari-all | 185.18.250.245 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.976 | 1.0 | 36 | 61 | prefer |
| Surfboard-tg-mixed | 0.909 | 0.832 | 173 | 5606 | prefer |
| nscl5-all | 0.904 | 0.836 | 55 | 1976 | prefer |
| Au1rxx-base64 | 0.887 | 0.887 | 133 | 150 | prefer |
| mheidari-all | 0.647 | 0.567 | 834 | 19158 | observe |
| DeltaKronecker-all | 0.44 | 0.354 | 48 | 3620 | observe |
| xiaoji235-airport-v2ray-all | 0.335 | 1.0 | 1 | 4321 | observe |
| Epodonios-all | 0.255 | None | 0 | 6683 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3974 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6902 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4250 | observe |
| barry-far-vless | 0.255 | None | 0 | 4807 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5334 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 232 |
| speed | ClientOSError | - | 103 |
| cn-block | TimeoutError | - | 30 |
| speed | TimeoutError | - | 26 |
| geo | ClientOSError | - | 16 |
| 204 | TimeoutError | - | 15 |
| 204 | ProxyError | - | 9 |
| cn-block | ProxyError | - | 6 |
| 204 | ClientOSError | - | 6 |
| cn-block | ClientOSError | - | 5 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
