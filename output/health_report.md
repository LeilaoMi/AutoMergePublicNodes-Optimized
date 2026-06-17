# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-06-17 17:07:44 |
| 运行耗时 | 120.5s |
| 订阅源总数 | 44 |
| 健康订阅源 | 44 |
| 原始节点 | 43696 |
| 去重后节点 | 18208 |
| TCP 可达 | 1500 |
| 真实可用 | 78 |
| Verified 输出 | 78 |
| Global 输出 | 81 |
| All 输出 | 18208 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 3.2 |
| geo | 1.2 |
| tcp | 19.7 |
| probe | 34.8 |
| real_test | 36.6 |
| generate | 25.0 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 22376 |
| shadowsocks | 8305 |
| trojan | 7075 |
| vmess | 5539 |
| hysteria2 | 174 |
| http | 95 |
| shadowsocksr | 87 |
| socks | 38 |
| hysteria | 6 |
| tuic | 1 |

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
| 64.41 | shadowsocks | 244.2 | 649.3 | 22.12 | 0.0 | 10.0 | 7.81 | 13.98 | DeltaKronecker-all | 108.181.57.93 |
| 62.12 | shadowsocks | 292.6 | 765.1 | 21.01 | 0.0 | 10.0 | 7.81 | 13.98 | DeltaKronecker-all | 147.90.234.133 |
| 56.64 | vmess | 555.0 | 975.2 | 14.93 | 0.0 | 10.0 | 12.86 | 13.98 | DeltaKronecker-all | 51.89.41.22 |
| 56.09 | vmess | 588.7 | 1010.9 | 14.15 | 0.0 | 10.0 | 12.86 | 13.98 | DeltaKronecker-all | 159.223.13.109 |
| 55.83 | shadowsocks | 347.3 | 583.2 | 19.74 | 0.0 | 10.0 | 7.81 | 13.98 | DeltaKronecker-all | 107.172.219.230 |
| 55.57 | vmess | 600.2 | 1102.0 | 13.88 | 0.0 | 10.0 | 12.86 | 13.98 | DeltaKronecker-all | 141.95.65.9 |
| 54.72 | trojan | 456.4 | 691.2 | 17.21 | 0.0 | 10.0 | 7.06 | 13.98 | DeltaKronecker-all | 8.6.112.6 |
| 54.47 | trojan | 469.4 | 744.8 | 16.91 | 0.0 | 10.0 | 7.06 | 13.98 | DeltaKronecker-all | 104.17.121.43 |
| 54.47 | vmess | 627.1 | 1115.7 | 13.26 | 0.0 | 10.0 | 12.86 | 13.98 | DeltaKronecker-all | 45.90.106.24 |
| 54.23 | trojan | 481.9 | 761.1 | 16.62 | 0.0 | 10.0 | 7.06 | 13.98 | DeltaKronecker-all | 104.18.152.144 |
| 54.21 | trojan | 483.7 | 758.0 | 16.58 | 0.0 | 10.0 | 7.06 | 13.98 | DeltaKronecker-all | 104.16.122.175 |
| 54.2 | trojan | 479.8 | 761.6 | 16.67 | 0.0 | 10.0 | 7.06 | 13.98 | DeltaKronecker-all | 45.130.125.75 |
| 54.04 | trojan | 481.6 | 770.2 | 16.63 | 0.0 | 10.0 | 7.06 | 13.98 | DeltaKronecker-all | 104.19.64.105 |
| 53.98 | trojan | 487.7 | 745.7 | 16.49 | 0.0 | 10.0 | 7.06 | 13.98 | DeltaKronecker-all | 199.181.197.143 |
| 53.97 | trojan | 485.6 | 757.1 | 16.54 | 0.0 | 10.0 | 7.06 | 13.98 | DeltaKronecker-all | 45.130.125.76 |
| 53.97 | trojan | 486.3 | 759.6 | 16.52 | 0.0 | 10.0 | 7.06 | 13.98 | DeltaKronecker-all | 172.64.229.75 |
| 53.87 | trojan | 489.2 | 771.9 | 16.45 | 0.0 | 10.0 | 7.06 | 13.98 | DeltaKronecker-all | 162.159.253.41 |
| 53.87 | trojan | 492.3 | 768.5 | 16.38 | 0.0 | 10.0 | 7.06 | 13.98 | DeltaKronecker-all | 141.193.213.10 |
| 53.86 | trojan | 482.6 | 716.0 | 16.61 | 0.0 | 10.0 | 7.06 | 13.98 | DeltaKronecker-all | 199.181.197.228 |
| 53.85 | trojan | 480.9 | 764.5 | 16.65 | 0.0 | 10.0 | 7.06 | 13.98 | DeltaKronecker-all | 185.18.250.245 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.791 | 1.0 | 15 | 73 | prefer |
| DeltaKronecker-all | 0.732 | 0.656 | 90 | 7763 | prefer |
| Surfboard-tg-mixed | 0.3 | 0.4 | 5 | 4729 | observe |
| nscl5-all | 0.294 | 1.0 | 1 | 967 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 2000 | observe |
| Epodonios-all | 0.255 | None | 0 | 3000 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3000 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 3000 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 3741 | observe |
| barry-far-vless | 0.255 | None | 0 | 2000 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4541 | observe |
| mheidari-all | 0.255 | None | 0 | 2000 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |
| Barabama-yudou | 0.214 | 0.5 | 2 | 166 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | status | 403 | 10 |
| speed | ClientOSError | - | 7 |
| geo | status | 429 | 5 |
| speed | TimeoutError | - | 4 |
| cn-block | TimeoutError | - | 4 |
| 204 | TimeoutError | - | 3 |
| 204 | ProxyError | - | 1 |
| cn-block | ClientOSError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 140 | 78 | - |
| global | False | 142 | 81 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
