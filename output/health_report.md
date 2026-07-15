# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-15 19:22:46 |
| 运行耗时 | 187.5s |
| 订阅源总数 | 107 |
| 健康订阅源 | 103 |
| 原始节点 | 76371 |
| 去重后节点 | 23023 |
| TCP 可达 | 3000 |
| 真实可用 | 202 |
| Verified 输出 | 202 |
| Global 输出 | 212 |
| All 输出 | 23023 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 3.9 |
| geo | 1.5 |
| tcp | 32.9 |
| probe | 49.9 |
| real_test | 57.3 |
| generate | 42.1 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 43988 |
| trojan | 11516 |
| vmess | 10895 |
| shadowsocks | 9382 |
| hysteria2 | 312 |
| shadowsocksr | 130 |
| http | 98 |
| socks | 29 |
| hysteria | 10 |
| tuic | 6 |
| anytls | 5 |

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
| 73.43 | trojan | 382.8 | 930.5 | 18.92 | 0.0 | 10.0 | 12.8 | 17.06 | mheidari-all | 64.94.95.118 |
| 71.14 | trojan | 383.5 | 1018.1 | 18.9 | 0.0 | 10.0 | 12.8 | 12.44 | DeltaKronecker-all | 64.94.95.117 |
| 70.01 | trojan | 432.2 | 1117.0 | 17.77 | 0.0 | 10.0 | 12.8 | 12.44 | DeltaKronecker-all | 64.94.95.114 |
| 69.02 | vmess | 421.2 | 1058.7 | 18.03 | 0.0 | 10.0 | 12.5 | 16.02 | Surfboard-tg-mixed | 67.220.95.3 |
| 67.02 | trojan | 445.3 | 581.5 | 17.47 | 0.0 | 10.0 | 12.8 | 16.02 | Surfboard-tg-mixed | 104.16.100.66 |
| 66.93 | trojan | 464.7 | 658.4 | 17.02 | 0.0 | 10.0 | 12.8 | 17.06 | mheidari-all | 104.17.151.126 |
| 65.85 | hysteria2 | 232.5 | 506.5 | 22.4 | 0.0 | 10.0 | 12.5 | 6.34 | Au1rxx-base64 | 38.148.249.252 |
| 65.32 | trojan | 380.2 | 1009.5 | 18.98 | 0.0 | 10.0 | 12.8 | 12.44 | DeltaKronecker-all | 64.94.95.115 |
| 65.22 | trojan | 518.4 | 578.7 | 15.78 | 0.0 | 10.0 | 12.8 | 16.02 | Surfboard-tg-mixed | 151.101.1.194 |
| 65.08 | shadowsocks | 378.3 | 879.3 | 19.02 | 0.0 | 10.0 | 11.39 | 12.44 | DeltaKronecker-all | 185.196.61.82 |
| 64.61 | shadowsocks | 445.6 | 805.7 | 17.46 | 0.0 | 10.0 | 11.39 | 12.44 | DeltaKronecker-all | 68.168.222.210 |
| 64.41 | shadowsocks | 250.7 | 651.3 | 21.97 | 0.0 | 10.0 | 11.39 | 6.34 | Au1rxx-base64 | 156.146.38.168 |
| 64.36 | vmess | 427.9 | 1033.0 | 17.87 | 0.0 | 10.0 | 12.5 | 12.44 | DeltaKronecker-all | 67.220.85.46 |
| 64.34 | trojan | 575.4 | 912.9 | 14.46 | 0.0 | 10.0 | 12.8 | 16.02 | Surfboard-tg-mixed | 104.16.174.117 |
| 64.25 | trojan | 565.6 | 860.8 | 14.68 | 0.0 | 10.0 | 12.8 | 16.02 | Surfboard-tg-mixed | 104.18.152.219 |
| 63.98 | shadowsocks | 372.2 | 889.4 | 19.16 | 0.0 | 10.0 | 11.39 | 17.06 | mheidari-all | 147.90.234.133 |
| 63.71 | vless | 365.3 | 978.4 | 19.32 | 0.0 | 10.0 | 1.95 | 12.44 | DeltaKronecker-all | 20.84.155.134 |
| 63.71 | trojan | 445.8 | 478.4 | 17.46 | 0.0 | 10.0 | 12.8 | 16.02 | Surfboard-tg-mixed | 104.21.48.168 |
| 63.0 | http | 723.4 | 1030.0 | 11.03 | 0.0 | 9.43 | 14.61 | 19.52 | snakem982 | 84.239.49.178 |
| 62.95 | http | 725.2 | 1006.2 | 10.99 | 0.0 | 9.4 | 14.61 | 19.52 | snakem982 | 84.239.49.42 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| Surfboard-tg-mixed | 0.739 | 0.663 | 86 | 5510 | prefer |
| mheidari-all | 0.614 | 0.535 | 86 | 16638 | observe |
| DeltaKronecker-all | 0.613 | 0.534 | 103 | 6421 | observe |
| Au1rxx-base64 | 0.494 | 0.875 | 8 | 138 | observe |
| Surfboard-tg-vless | 0.335 | 1.0 | 1 | 4277 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 3759 | observe |
| Epodonios-all | 0.255 | None | 0 | 6514 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3967 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6930 | observe |
| barry-far-vless | 0.255 | None | 0 | 4862 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5183 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| xiaoji235-airport-v2ray-all | 0.245 | None | 0 | 1741 | observe |
| nscl5-all | 0.227 | None | 0 | 1300 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 41 |
| speed | ClientOSError | - | 29 |
| 204 | TimeoutError | - | 16 |
| 204 | ProxyError | - | 9 |
| geo | ClientOSError | - | 8 |
| cn-block | TimeoutError | - | 7 |
| cn-block | ClientOSError | - | 5 |
| speed | TimeoutError | - | 3 |
| cn-block | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 279 | 202 | - |
| global | False | 290 | 212 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
