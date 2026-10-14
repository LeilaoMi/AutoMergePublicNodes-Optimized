# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-14 11:02:07 |
| 运行耗时 | 376.3s |
| 订阅源总数 | 107 |
| 健康订阅源 | 93 |
| 原始节点 | 98253 |
| 去重后节点 | 27210 |
| TCP 可达 | 3000 |
| 真实可用 | 68 |
| Verified 输出 | 68 |
| Global 输出 | 74 |
| All 输出 | 27210 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 8.3 |
| geo | 1.6 |
| tcp | 116.8 |
| probe | 102.0 |
| real_test | 89.4 |
| generate | 58.2 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 58044 |
| vmess | 16103 |
| shadowsocks | 11810 |
| trojan | 10207 |
| hysteria2 | 1304 |
| http | 483 |
| shadowsocksr | 167 |
| socks | 86 |
| anytls | 25 |
| hysteria | 18 |
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
| 80.76 | shadowsocks | 242.4 | 615.9 | 22.17 | 0.0 | 10.0 | 13.77 | 18.82 | Au1rxx-base64 | 156.146.38.170 |
| 78.74 | vless | 244.7 | 549.1 | 22.11 | 0.0 | 9.91 | 8.64 | 18.82 | Au1rxx-base64 | 45.32.69.110 |
| 78.32 | vless | 247.3 | 554.7 | 22.05 | 0.0 | 9.9 | 8.64 | 18.82 | Au1rxx-base64 | 144.202.126.147 |
| 77.71 | shadowsocks | 244.6 | 630.1 | 22.12 | 0.0 | 10.0 | 13.77 | 18.82 | Au1rxx-base64 | 156.146.38.169 |
| 76.3 | shadowsocks | 276.8 | 591.3 | 21.37 | 0.0 | 9.68 | 13.77 | 18.82 | Au1rxx-base64 | 173.244.56.6 |
| 76.02 | hysteria2 | 381.5 | 843.4 | 18.95 | 0.0 | 10.0 | 11.84 | 18.82 | Au1rxx-base64 | 66.94.121.46 |
| 74.7 | shadowsocks | 332.6 | 766.5 | 20.08 | 0.0 | 10.0 | 13.77 | 18.82 | Au1rxx-base64 | 37.19.198.160 |
| 74.66 | shadowsocks | 344.4 | 793.9 | 19.81 | 0.0 | 10.0 | 13.77 | 18.82 | Au1rxx-base64 | 37.19.198.244 |
| 73.83 | vless | 292.3 | 601.3 | 21.01 | 0.0 | 9.15 | 8.64 | 18.82 | Au1rxx-base64 | 154.29.145.196 |
| 73.7 | shadowsocks | 337.6 | 780.7 | 19.96 | 0.0 | 9.59 | 13.77 | 18.82 | Au1rxx-base64 | 37.19.198.243 |
| 73.55 | shadowsocks | 340.6 | 726.4 | 19.89 | 0.0 | 10.0 | 13.77 | 18.82 | Au1rxx-base64 | 140.82.63.79 |
| 71.61 | vless | 329.4 | 773.1 | 20.15 | 0.0 | 9.83 | 8.64 | 18.82 | Au1rxx-base64 | 15.204.97.195 |
| 71.1 | hysteria2 | 301.2 | 729.7 | 20.81 | 0.0 | 6.13 | 11.84 | 18.82 | Au1rxx-base64 | 129.213.91.185 |
| 68.82 | vless | 325.3 | 765.5 | 20.25 | 0.0 | 8.1 | 8.64 | 18.82 | Au1rxx-base64 | 216.9.226.22 |
| 68.5 | shadowsocks | 407.1 | 986.2 | 18.35 | 0.0 | 8.4 | 13.77 | 18.82 | Au1rxx-base64 | 15.204.233.41 |
| 68.45 | vless | 473.1 | 847.5 | 16.83 | 0.0 | 9.15 | 8.64 | 18.82 | Au1rxx-base64 | 154.12.38.159 |
| 67.12 | vless | 312.7 | 688.9 | 20.54 | 0.0 | 6.75 | 8.64 | 18.82 | Au1rxx-base64 | 69.48.201.136 |
| 66.15 | vless | 390.0 | 852.9 | 18.75 | 0.0 | 6.64 | 8.64 | 18.82 | Au1rxx-base64 | 185.164.57.152 |
| 65.06 | shadowsocks | 243.2 | 627.2 | 22.15 | 0.0 | 0.0 | 13.77 | 16.14 | Surfboard-tg-mixed | 156.146.38.167 |
| 64.92 | vless | 437.3 | 962.7 | 17.65 | 0.0 | 5.02 | 8.64 | 18.82 | Au1rxx-base64 | 209.200.246.148 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi-get_subscribe | 0.946 | 0.935 | 62 | 598 | prefer |
| mheidari-all | 0.898 | 0.83 | 53 | 23983 | prefer |
| zhangkai | 0.861 | 1.0 | 17 | 144 | prefer |
| Au1rxx-base64 | 0.773 | 0.704 | 199 | 1786 | prefer |
| Surfboard-tg-mixed | 0.634 | 0.556 | 81 | 7056 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5125 | observe |
| DeltaKronecker-all | 0.255 | None | 0 | 4803 | observe |
| Epodonios-all | 0.255 | None | 0 | 7542 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 10026 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5579 | observe |
| barry-far-vless | 0.255 | None | 0 | 5831 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4216 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 73 |
| geo | ClientOSError | - | 10 |
| speed | ClientOSError | - | 9 |
| cn-block | ClientOSError | - | 5 |
| 204 | TimeoutError | - | 3 |
| cn-block | ProxyError | - | 2 |
| 204 | ProxyError | - | 2 |
| cn-block | TimeoutError | - | 2 |
| 204 | ServerDisconnectedError | - | 1 |
| 204 | ClientOSError | - | 1 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 57 | 68 | - |
| global | False | 75 | 74 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
