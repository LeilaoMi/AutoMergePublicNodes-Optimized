# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-31 14:25:12 |
| 运行耗时 | 241.2s |
| 订阅源总数 | 107 |
| 健康订阅源 | 102 |
| 原始节点 | 79052 |
| 去重后节点 | 22809 |
| TCP 可达 | 3000 |
| 真实可用 | 438 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22809 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.2 |
| geo | 1.4 |
| tcp | 33.1 |
| probe | 50.4 |
| real_test | 110.5 |
| generate | 41.7 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 46556 |
| vmess | 11996 |
| shadowsocks | 10336 |
| trojan | 9310 |
| hysteria2 | 575 |
| http | 98 |
| shadowsocksr | 70 |
| socks | 55 |
| anytls | 26 |
| tuic | 16 |
| hysteria | 14 |

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
| 79.58 | http | 328.4 | 715.1 | 20.18 | 0.0 | 10.0 | 14.82 | 19.84 | zhangkai | 156.146.59.8 |
| 79.4 | http | 333.1 | 755.7 | 20.07 | 0.0 | 10.0 | 14.82 | 19.84 | zhangkai | 156.146.59.7 |
| 78.72 | hysteria2 | 314.8 | 771.1 | 20.49 | 0.0 | 10.0 | 12.35 | 16.98 | Au1rxx-base64 | 159.223.157.129 |
| 78.52 | http | 285.0 | 572.4 | 21.18 | 0.0 | 10.0 | 14.82 | 19.84 | zhangkai | 138.199.35.202 |
| 78.41 | trojan | 250.4 | 585.7 | 21.98 | 0.0 | 10.0 | 12.45 | 16.98 | Au1rxx-base64 | 64.94.95.117 |
| 78.39 | trojan | 251.5 | 632.2 | 21.96 | 0.0 | 10.0 | 12.45 | 16.98 | Au1rxx-base64 | 64.94.95.114 |
| 78.32 | http | 285.1 | 577.5 | 21.18 | 0.0 | 10.0 | 14.82 | 19.84 | zhangkai | 138.199.35.205 |
| 78.26 | http | 291.8 | 592.2 | 21.02 | 0.0 | 10.0 | 14.82 | 19.84 | zhangkai | 138.199.35.198 |
| 78.21 | http | 292.2 | 598.0 | 21.01 | 0.0 | 10.0 | 14.82 | 19.84 | zhangkai | 138.199.35.196 |
| 78.18 | http | 295.8 | 607.5 | 20.93 | 0.0 | 10.0 | 14.82 | 19.84 | zhangkai | 138.199.35.218 |
| 78.03 | http | 314.7 | 705.0 | 20.49 | 0.0 | 10.0 | 14.82 | 19.84 | zhangkai | 156.146.59.5 |
| 77.67 | hysteria2 | 319.5 | 787.7 | 20.38 | 0.0 | 8.96 | 12.35 | 16.98 | Au1rxx-base64 | usa1.spectrumproxy.shop |
| 77.5 | http | 330.9 | 708.0 | 20.12 | 0.0 | 10.0 | 14.82 | 19.84 | zhangkai | 138.199.35.207 |
| 77.42 | http | 327.7 | 703.4 | 20.19 | 0.0 | 10.0 | 14.82 | 19.84 | zhangkai | 138.199.35.204 |
| 77.4 | http | 326.5 | 695.9 | 20.22 | 0.0 | 10.0 | 14.82 | 19.84 | zhangkai | 138.199.35.209 |
| 77.21 | http | 292.1 | 593.4 | 21.02 | 0.0 | 10.0 | 14.82 | 19.84 | zhangkai | 138.199.35.197 |
| 76.94 | trojan | 253.0 | 636.8 | 21.92 | 0.0 | 10.0 | 12.45 | 16.98 | Au1rxx-base64 | 64.94.95.115 |
| 76.69 | http | 283.5 | 564.9 | 21.21 | 0.0 | 10.0 | 14.82 | 19.84 | zhangkai | 138.199.35.220 |
| 76.46 | shadowsocks | 274.0 | 719.1 | 21.44 | 0.0 | 10.0 | 12.04 | 16.98 | Au1rxx-base64 | 156.146.38.168 |
| 76.38 | shadowsocks | 277.0 | 696.0 | 21.36 | 0.0 | 10.0 | 12.04 | 16.98 | Au1rxx-base64 | 156.146.38.167 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.992 | 1.0 | 80 | 110 | prefer |
| Au1rxx-base64 | 0.877 | 0.818 | 395 | 1533 | prefer |
| mheidari-all | 0.735 | 0.667 | 27 | 16815 | prefer |
| DeltaKronecker-all | 0.563 | 0.481 | 27 | 5144 | observe |
| Surfboard-tg-mixed | 0.324 | 0.375 | 8 | 5429 | observe |
| tg-OutlineReleasedKey | 0.257 | 1.0 | 1 | 48 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5507 | observe |
| Epodonios-all | 0.255 | None | 0 | 5989 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3966 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7049 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4260 | observe |
| barry-far-vless | 0.255 | None | 0 | 4528 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5074 | observe |
| xiaoji235-airport-v2ray-all | 0.249 | None | 0 | 1861 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 21 |
| geo | ClientOSError | - | 17 |
| cn-block | TimeoutError | - | 17 |
| speed | TimeoutError | - | 13 |
| 204 | ProxyError | - | 12 |
| 204 | TimeoutError | - | 8 |
| 204 | ClientOSError | - | 7 |
| speed | ClientOSError | - | 5 |
| cn-block | ClientOSError | - | 2 |
| cn-block | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
