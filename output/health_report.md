# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-06-29 20:11:16 |
| 运行耗时 | 261.6s |
| 订阅源总数 | 107 |
| 健康订阅源 | 103 |
| 原始节点 | 75589 |
| 去重后节点 | 23098 |
| TCP 可达 | 3000 |
| 真实可用 | 452 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23098 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.3 |
| geo | 1.4 |
| tcp | 31.0 |
| probe | 57.0 |
| real_test | 131.4 |
| generate | 36.4 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 42317 |
| trojan | 13041 |
| vmess | 10324 |
| shadowsocks | 9275 |
| hysteria2 | 268 |
| shadowsocksr | 151 |
| http | 136 |
| socks | 70 |
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
| 76.86 | shadowsocks | 238.3 | 634.5 | 22.26 | 0.0 | 10.0 | 11.56 | 17.04 | Au1rxx-base64 | 37.19.198.244 |
| 76.83 | vless | 272.9 | 751.2 | 21.46 | 0.0 | 10.0 | 9.27 | 16.1 | mheidari-all | 47.253.226.114 |
| 76.81 | shadowsocks | 240.6 | 642.8 | 22.21 | 0.0 | 10.0 | 11.56 | 17.04 | Au1rxx-base64 | 37.19.198.236 |
| 75.77 | shadowsocks | 285.3 | 779.1 | 21.17 | 0.0 | 10.0 | 11.56 | 17.04 | Au1rxx-base64 | 37.19.198.243 |
| 75.15 | vmess | 301.1 | 807.6 | 20.81 | 0.0 | 10.0 | 12.86 | 15.98 | Surfboard-tg-mixed | 67.220.95.3 |
| 74.89 | shadowsocks | 261.3 | 685.3 | 21.73 | 0.0 | 10.0 | 11.56 | 16.1 | mheidari-all | 108.181.57.93 |
| 73.92 | shadowsocks | 235.6 | 627.9 | 22.32 | 0.0 | 10.0 | 11.56 | 17.04 | Au1rxx-base64 | 37.19.198.160 |
| 73.61 | shadowsocks | 275.5 | 633.1 | 21.4 | 0.0 | 10.0 | 11.56 | 17.04 | Au1rxx-base64 | 156.146.38.167 |
| 73.08 | shadowsocks | 284.9 | 656.8 | 21.18 | 0.0 | 10.0 | 11.56 | 17.04 | Au1rxx-base64 | 156.146.38.168 |
| 72.88 | shadowsocks | 284.9 | 653.2 | 21.18 | 0.0 | 10.0 | 11.56 | 17.04 | Au1rxx-base64 | 156.146.38.170 |
| 72.88 | vless | 396.0 | 650.1 | 18.61 | 0.0 | 10.0 | 9.27 | 16.1 | mheidari-all | 104.18.42.68 |
| 71.16 | shadowsocks | 281.5 | 647.9 | 21.26 | 0.0 | 10.0 | 11.56 | 17.04 | Au1rxx-base64 | 156.146.38.169 |
| 70.84 | vmess | 305.8 | 811.6 | 20.7 | 0.0 | 10.0 | 12.86 | 11.78 | DeltaKronecker-all | 67.220.85.46 |
| 70.73 | hysteria2 | 363.7 | 698.7 | 19.36 | 0.0 | 10.0 | 11.25 | 17.04 | Au1rxx-base64 | 62.210.124.146 |
| 70.03 | trojan | 395.7 | 965.4 | 18.62 | 0.0 | 10.0 | 11.56 | 16.1 | mheidari-all | 64.94.95.118 |
| 69.98 | shadowsocks | 306.1 | 575.5 | 20.69 | 0.0 | 10.0 | 11.56 | 17.04 | Au1rxx-base64 | 173.244.56.6 |
| 69.88 | shadowsocks | 312.3 | 558.0 | 20.55 | 0.0 | 10.0 | 11.56 | 17.04 | Au1rxx-base64 | 173.244.56.9 |
| 69.47 | shadowsocks | 294.7 | 546.1 | 20.96 | 0.0 | 10.0 | 11.56 | 17.04 | Au1rxx-base64 | 108.181.118.10 |
| 68.66 | shadowsocks | 302.2 | 818.8 | 20.78 | 0.0 | 10.0 | 11.56 | 17.04 | Au1rxx-base64 | tinkered-pennies-puppies.freesocks.work |
| 68.45 | shadowsocks | 342.4 | 590.6 | 19.85 | 0.0 | 10.0 | 11.56 | 17.04 | Au1rxx-base64 | 149.22.95.183 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| Au1rxx-base64 | 0.803 | 0.816 | 38 | 79 | prefer |
| mheidari-all | 0.761 | 0.683 | 249 | 15724 | prefer |
| Surfboard-tg-mixed | 0.722 | 0.643 | 305 | 5575 | prefer |
| DeltaKronecker-all | 0.495 | 0.41 | 39 | 7004 | observe |
| Barabama-yudou | 0.318 | 1.0 | 2 | 166 | observe |
| nscl5-all | 0.302 | 1.0 | 1 | 1166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4653 | observe |
| Epodonios-all | 0.255 | None | 0 | 6449 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3980 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6727 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4058 | observe |
| barry-far-vless | 0.255 | None | 0 | 4569 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5353 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 95 |
| 204 | ProxyError | - | 24 |
| 204 | TimeoutError | - | 22 |
| cn-block | TimeoutError | - | 13 |
| speed | TimeoutError | - | 12 |
| geo | TimeoutError | - | 11 |
| 204 | ClientOSError | - | 11 |
| geo | ClientOSError | - | 9 |
| geo | ProxyError | - | 8 |
| cn-block | ProxyError | - | 6 |
| cn-block | ClientOSError | - | 5 |
| speed | ProxyError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
