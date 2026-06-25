# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-06-25 09:37:37 |
| 运行耗时 | 249.1s |
| 订阅源总数 | 107 |
| 健康订阅源 | 105 |
| 原始节点 | 82741 |
| 去重后节点 | 22707 |
| TCP 可达 | 3000 |
| 真实可用 | 393 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22707 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 18.6 |
| geo | 1.3 |
| tcp | 30.1 |
| probe | 54.7 |
| real_test | 107.3 |
| generate | 37.0 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 46696 |
| trojan | 14188 |
| vmess | 11086 |
| shadowsocks | 10173 |
| hysteria2 | 237 |
| shadowsocksr | 154 |
| http | 129 |
| socks | 70 |
| hysteria | 6 |
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
| 75.72 | shadowsocks | 230.7 | 641.2 | 22.44 | 0.0 | 10.0 | 13.4 | 13.88 | Au1rxx-base64 | 37.19.198.243 |
| 75.68 | shadowsocks | 232.3 | 644.5 | 22.4 | 0.0 | 10.0 | 13.4 | 13.88 | Au1rxx-base64 | 37.19.198.160 |
| 75.68 | shadowsocks | 232.4 | 645.5 | 22.4 | 0.0 | 10.0 | 13.4 | 13.88 | Au1rxx-base64 | 37.19.198.244 |
| 74.27 | vless | 267.7 | 659.7 | 21.58 | 0.0 | 10.0 | 8.11 | 16.58 | Surfboard-tg-mixed | 104.16.9.20 |
| 73.38 | trojan | 345.6 | 901.0 | 19.78 | 0.0 | 10.0 | 11.98 | 12.62 | DeltaKronecker-all | 104.17.148.22 |
| 72.83 | shadowsocks | 278.6 | 648.7 | 21.33 | 0.0 | 10.0 | 13.4 | 13.88 | Au1rxx-base64 | 156.146.38.170 |
| 72.28 | shadowsocks | 281.1 | 647.9 | 21.27 | 0.0 | 10.0 | 13.4 | 13.88 | Au1rxx-base64 | 156.146.38.169 |
| 72.17 | shadowsocks | 275.8 | 634.1 | 21.39 | 0.0 | 10.0 | 13.4 | 13.88 | Au1rxx-base64 | 156.146.38.167 |
| 71.91 | vless | 340.9 | 825.7 | 19.89 | 0.0 | 10.0 | 8.11 | 16.58 | Surfboard-tg-mixed | 15.223.121.250 |
| 71.55 | shadowsocks | 277.3 | 628.9 | 21.36 | 0.0 | 10.0 | 13.4 | 13.88 | Au1rxx-base64 | 156.146.38.168 |
| 71.23 | shadowsocks | 228.1 | 624.8 | 22.5 | 0.0 | 10.0 | 13.4 | 13.88 | Au1rxx-base64 | 198.98.53.130 |
| 70.77 | shadowsocks | 228.4 | 632.1 | 22.49 | 0.0 | 10.0 | 13.4 | 13.88 | Au1rxx-base64 | 37.19.198.236 |
| 69.97 | shadowsocks | 250.9 | 654.7 | 21.97 | 0.0 | 10.0 | 13.4 | 13.88 | Au1rxx-base64 | 108.181.57.93 |
| 69.77 | vless | 332.3 | 875.1 | 20.08 | 0.0 | 10.0 | 8.11 | 16.58 | Surfboard-tg-mixed | 82.39.213.150 |
| 68.87 | shadowsocks | 309.6 | 582.1 | 20.61 | 0.0 | 10.0 | 13.4 | 13.88 | Au1rxx-base64 | 173.244.56.9 |
| 68.66 | vless | 337.2 | 631.8 | 19.97 | 0.0 | 10.0 | 8.11 | 16.58 | Surfboard-tg-mixed | 172.252.125.77 |
| 68.61 | trojan | 370.1 | 870.1 | 19.21 | 0.0 | 10.0 | 11.98 | 13.52 | mheidari-all | 64.94.95.118 |
| 68.01 | shadowsocks | 316.6 | 557.9 | 20.45 | 0.0 | 10.0 | 13.4 | 13.88 | Au1rxx-base64 | 108.181.118.10 |
| 67.95 | shadowsocks | 323.7 | 598.9 | 20.29 | 0.0 | 10.0 | 13.4 | 13.88 | Au1rxx-base64 | 149.22.95.183 |
| 67.58 | shadowsocks | 316.3 | 546.8 | 20.46 | 0.0 | 10.0 | 13.4 | 13.88 | Au1rxx-base64 | 108.181.0.177 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.977 | 1.0 | 36 | 82 | prefer |
| Au1rxx-base64 | 0.973 | 1.0 | 30 | 111 | prefer |
| Surfboard-tg-mixed | 0.794 | 0.716 | 250 | 5237 | prefer |
| mheidari-all | 0.65 | 0.571 | 77 | 15925 | observe |
| DeltaKronecker-all | 0.582 | 0.502 | 201 | 12590 | observe |
| Barabama-yudou | 0.318 | 1.0 | 2 | 166 | observe |
| nscl5-all | 0.3 | 1.0 | 1 | 1136 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4787 | observe |
| Epodonios-all | 0.255 | None | 0 | 7823 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7435 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 3919 | observe |
| barry-far-vless | 0.255 | None | 0 | 4701 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5133 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 72 |
| 204 | ProxyError | - | 32 |
| geo | TimeoutError | - | 22 |
| 204 | TimeoutError | - | 18 |
| 204 | ClientOSError | - | 12 |
| geo | ClientOSError | - | 11 |
| cn-block | ClientOSError | - | 11 |
| cn-block | TimeoutError | - | 8 |
| geo | ProxyError | - | 6 |
| cn-block | ProxyError | - | 5 |
| speed | TimeoutError | - | 4 |
| speed | ProxyError | - | 3 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
