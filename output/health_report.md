# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-15 08:27:05 |
| 运行耗时 | 207.6s |
| 订阅源总数 | 107 |
| 健康订阅源 | 104 |
| 原始节点 | 75676 |
| 去重后节点 | 22853 |
| TCP 可达 | 3000 |
| 真实可用 | 292 |
| Verified 输出 | 292 |
| Global 输出 | 300 |
| All 输出 | 22853 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.2 |
| geo | 1.6 |
| tcp | 31.7 |
| probe | 43.4 |
| real_test | 87.7 |
| generate | 39.0 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 42346 |
| trojan | 11672 |
| vmess | 11121 |
| shadowsocks | 9883 |
| hysteria2 | 343 |
| http | 138 |
| shadowsocksr | 124 |
| socks | 31 |
| hysteria | 10 |
| anytls | 5 |
| tuic | 3 |

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
| 75.77 | shadowsocks | 253.1 | 623.5 | 21.92 | 0.0 | 10.0 | 13.03 | 14.82 | mheidari-all | 198.98.53.130 |
| 74.1 | vmess | 337.0 | 896.8 | 19.98 | 0.0 | 10.0 | 12.5 | 16.12 | Surfboard-tg-mixed | 67.220.95.3 |
| 72.68 | shadowsocks | 310.4 | 804.1 | 20.59 | 0.0 | 10.0 | 13.03 | 14.82 | mheidari-all | 108.181.57.93 |
| 71.41 | trojan | 287.2 | 700.5 | 21.13 | 0.0 | 10.0 | 14.08 | 9.2 | DeltaKronecker-all | 64.94.95.115 |
| 69.74 | trojan | 308.5 | 656.9 | 20.64 | 0.0 | 10.0 | 14.08 | 16.12 | Surfboard-tg-mixed | 172.64.145.202 |
| 69.12 | trojan | 284.6 | 680.4 | 21.19 | 0.0 | 10.0 | 14.08 | 9.2 | DeltaKronecker-all | 64.94.95.114 |
| 68.18 | trojan | 392.2 | 986.1 | 18.7 | 0.0 | 10.0 | 14.08 | 9.2 | DeltaKronecker-all | 64.94.95.117 |
| 67.8 | vmess | 552.7 | 1509.0 | 14.98 | 0.0 | 10.0 | 12.5 | 14.82 | mheidari-all | 67.220.85.46 |
| 67.41 | trojan | 431.0 | 638.0 | 17.8 | 0.0 | 10.0 | 14.08 | 16.12 | Surfboard-tg-mixed | 104.17.151.126 |
| 67.39 | trojan | 522.6 | 844.0 | 15.68 | 0.0 | 10.0 | 14.08 | 16.12 | Surfboard-tg-mixed | 104.18.152.219 |
| 67.33 | trojan | 515.6 | 841.2 | 15.84 | 0.0 | 10.0 | 14.08 | 16.12 | Surfboard-tg-mixed | 104.16.174.12 |
| 66.73 | trojan | 540.4 | 867.6 | 15.27 | 0.0 | 10.0 | 14.08 | 16.12 | Surfboard-tg-mixed | 104.16.174.117 |
| 66.7 | trojan | 704.5 | 1931.9 | 11.47 | 0.0 | 10.0 | 14.08 | 14.82 | mheidari-all | 64.94.95.118 |
| 66.64 | trojan | 499.2 | 804.6 | 16.22 | 0.0 | 10.0 | 14.08 | 14.82 | mheidari-all | 45.130.125.158 |
| 66.53 | shadowsocks | 387.7 | 1018.5 | 18.8 | 0.0 | 10.0 | 13.03 | 9.2 | DeltaKronecker-all | 185.196.61.82 |
| 66.46 | trojan | 528.3 | 912.7 | 15.55 | 0.0 | 10.0 | 14.08 | 16.12 | Surfboard-tg-mixed | 172.64.147.227 |
| 66.26 | shadowsocks | 420.7 | 747.6 | 18.04 | 0.0 | 10.0 | 13.03 | 16.12 | Surfboard-tg-mixed | 158.173.24.73 |
| 66.18 | trojan | 505.1 | 829.9 | 16.09 | 0.0 | 10.0 | 14.08 | 14.82 | mheidari-all | 104.18.152.97 |
| 65.68 | trojan | 541.8 | 758.0 | 15.24 | 0.0 | 10.0 | 14.08 | 14.82 | mheidari-all | 216.24.57.7 |
| 65.54 | trojan | 551.3 | 759.8 | 15.02 | 0.0 | 10.0 | 14.08 | 14.82 | mheidari-all | 104.16.174.37 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| mheidari-all | 0.818 | 0.743 | 101 | 16158 | prefer |
| DeltaKronecker-all | 0.721 | 0.643 | 140 | 6421 | prefer |
| Surfboard-tg-mixed | 0.627 | 0.547 | 159 | 5640 | observe |
| 10ium-ScrapeCategorize-Vless | 0.335 | 1.0 | 1 | 3759 | observe |
| Au1rxx-base64 | 0.317 | 1.0 | 2 | 149 | observe |
| Epodonios-all | 0.255 | None | 0 | 6608 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3975 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6437 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4320 | observe |
| barry-far-vless | 0.255 | None | 0 | 4712 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5187 | observe |
| xiaoji235-airport-v2ray-all | 0.245 | None | 0 | 1741 | observe |
| nscl5-all | 0.231 | 0.333 | 3 | 1300 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 65 |
| speed | ClientOSError | - | 46 |
| 204 | TimeoutError | - | 12 |
| cn-block | TimeoutError | - | 11 |
| geo | ClientOSError | - | 6 |
| speed | TimeoutError | - | 5 |
| cn-block | ClientOSError | - | 4 |
| 204 | ProxyError | - | 2 |
| cn-block | ProxyError | - | 1 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 285 | 292 | - |
| global | False | 293 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
