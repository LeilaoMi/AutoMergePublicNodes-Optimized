# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-07 14:52:58 |
| 运行耗时 | 198.3s |
| 订阅源总数 | 107 |
| 健康订阅源 | 102 |
| 原始节点 | 85387 |
| 去重后节点 | 24893 |
| TCP 可达 | 3000 |
| 真实可用 | 284 |
| Verified 输出 | 284 |
| Global 输出 | 293 |
| All 输出 | 24893 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.4 |
| geo | 1.4 |
| tcp | 32.2 |
| probe | 42.5 |
| real_test | 73.3 |
| generate | 43.5 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 51100 |
| trojan | 13117 |
| vmess | 10624 |
| shadowsocks | 9495 |
| hysteria2 | 699 |
| shadowsocksr | 144 |
| http | 140 |
| socks | 53 |
| hysteria | 8 |
| tuic | 4 |
| anytls | 3 |

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
| 77.38 | trojan | 279.8 | 715.8 | 21.3 | 0.0 | 10.0 | 12.34 | 16.24 | mheidari-all | 149.28.241.235 |
| 76.1 | shadowsocks | 255.4 | 618.4 | 21.87 | 0.0 | 8.87 | 12.44 | 16.92 | Au1rxx-base64 | 156.146.38.169 |
| 75.81 | shadowsocks | 268.3 | 647.2 | 21.57 | 0.0 | 8.88 | 12.44 | 16.92 | Au1rxx-base64 | 156.146.38.170 |
| 75.79 | shadowsocks | 269.0 | 698.3 | 21.55 | 0.0 | 8.88 | 12.44 | 16.92 | Au1rxx-base64 | 156.146.38.167 |
| 74.73 | shadowsocks | 314.7 | 833.6 | 20.49 | 0.0 | 8.88 | 12.44 | 16.92 | Au1rxx-base64 | 156.146.38.168 |
| 74.69 | trojan | 246.8 | 593.6 | 22.07 | 0.0 | 10.0 | 12.34 | 13.28 | DeltaKronecker-all | 64.94.95.117 |
| 74.62 | trojan | 249.5 | 609.8 | 22.0 | 0.0 | 10.0 | 12.34 | 13.28 | DeltaKronecker-all | 64.94.95.115 |
| 74.25 | trojan | 287.0 | 737.7 | 21.13 | 0.0 | 10.0 | 12.34 | 13.28 | DeltaKronecker-all | 45.32.195.168 |
| 73.12 | trojan | 336.2 | 887.4 | 20.0 | 0.0 | 10.0 | 12.34 | 13.28 | DeltaKronecker-all | 45.32.198.247 |
| 71.61 | shadowsocks | 273.2 | 545.1 | 21.45 | 0.0 | 8.86 | 12.44 | 16.92 | Au1rxx-base64 | 108.181.0.177 |
| 71.18 | shadowsocks | 334.1 | 280.9 | 20.04 | 4.47 | 8.82 | 12.44 | 16.92 | Au1rxx-base64 | 149.22.87.204 |
| 71.02 | trojan | 247.0 | 608.7 | 22.06 | 0.0 | 10.0 | 12.34 | 13.28 | DeltaKronecker-all | 64.94.95.114 |
| 70.93 | shadowsocks | 280.5 | 560.6 | 21.28 | 0.0 | 8.86 | 12.44 | 16.92 | Au1rxx-base64 | 108.181.118.10 |
| 70.45 | shadowsocks | 273.2 | 537.7 | 21.45 | 0.0 | 8.87 | 12.44 | 16.92 | Au1rxx-base64 | 173.244.56.9 |
| 70.04 | shadowsocks | 342.0 | 637.7 | 19.86 | 0.0 | 8.88 | 12.44 | 16.92 | Au1rxx-base64 | 198.98.53.130 |
| 69.56 | shadowsocks | 333.0 | 731.4 | 20.07 | 0.0 | 8.82 | 12.44 | 16.92 | Au1rxx-base64 | 37.19.198.243 |
| 69.35 | shadowsocks | 334.5 | 738.0 | 20.03 | 0.0 | 8.87 | 12.44 | 16.92 | Au1rxx-base64 | 37.19.198.160 |
| 69.32 | shadowsocks | 330.7 | 703.8 | 20.12 | 0.0 | 8.81 | 12.44 | 16.92 | Au1rxx-base64 | 149.22.95.183 |
| 68.02 | shadowsocks | 336.2 | 739.9 | 20.0 | 0.0 | 8.87 | 12.44 | 16.92 | Au1rxx-base64 | 37.19.198.244 |
| 67.61 | shadowsocks | 420.1 | 928.7 | 18.05 | 0.0 | 10.0 | 12.44 | 16.24 | mheidari-all | 185.196.61.82 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| DeltaKronecker-all | 0.807 | 0.731 | 108 | 8472 | prefer |
| Au1rxx-base64 | 0.799 | 0.803 | 66 | 123 | prefer |
| Surfboard-tg-mixed | 0.772 | 0.697 | 89 | 6181 | prefer |
| mheidari-all | 0.755 | 0.68 | 75 | 18192 | prefer |
| xiaoji235-airport-v2ray-all | 0.391 | 1.0 | 2 | 3626 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4700 | observe |
| Epodonios-all | 0.255 | None | 0 | 7142 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3965 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7271 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4677 | observe |
| barry-far-vless | 0.255 | None | 0 | 5363 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5338 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | ProxyError | - | 17 |
| geo | ClientOSError | - | 13 |
| speed | ClientOSError | - | 10 |
| 204 | ClientOSError | - | 9 |
| cn-block | TimeoutError | - | 8 |
| 204 | TimeoutError | - | 7 |
| geo | TimeoutError | - | 7 |
| speed | ProxyError | - | 6 |
| geo | ProxyError | - | 5 |
| cn-block | ProxyError | - | 5 |
| speed | TimeoutError | - | 4 |
| cn-block | ClientOSError | - | 3 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 284 | - |
| global | False | 300 | 293 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
