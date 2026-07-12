# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-12 13:42:27 |
| 运行耗时 | 202.9s |
| 订阅源总数 | 107 |
| 健康订阅源 | 103 |
| 原始节点 | 77498 |
| 去重后节点 | 24183 |
| TCP 可达 | 3000 |
| 真实可用 | 284 |
| Verified 输出 | 284 |
| Global 输出 | 300 |
| All 输出 | 24183 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.7 |
| geo | 1.3 |
| tcp | 32.4 |
| probe | 45.8 |
| real_test | 74.7 |
| generate | 44.0 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 45039 |
| trojan | 11776 |
| vmess | 10562 |
| shadowsocks | 9487 |
| hysteria2 | 304 |
| shadowsocksr | 151 |
| http | 137 |
| socks | 30 |
| hysteria | 8 |
| tuic | 4 |

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
| 76.63 | shadowsocks | 254.9 | 633.4 | 21.88 | 0.0 | 10.0 | 13.07 | 15.68 | Au1rxx-base64 | 156.146.38.169 |
| 76.56 | shadowsocks | 257.9 | 634.4 | 21.81 | 0.0 | 10.0 | 13.07 | 15.68 | Au1rxx-base64 | 156.146.38.168 |
| 76.38 | shadowsocks | 265.7 | 668.8 | 21.63 | 0.0 | 10.0 | 13.07 | 15.68 | Au1rxx-base64 | 37.19.198.243 |
| 76.03 | shadowsocks | 271.0 | 673.2 | 21.5 | 0.0 | 10.0 | 13.07 | 15.68 | Au1rxx-base64 | 37.19.198.236 |
| 75.87 | shadowsocks | 268.5 | 673.2 | 21.56 | 0.0 | 10.0 | 13.07 | 15.68 | Au1rxx-base64 | 37.19.198.160 |
| 75.64 | shadowsocks | 276.0 | 667.5 | 21.39 | 0.0 | 10.0 | 13.07 | 15.68 | Au1rxx-base64 | 108.181.57.93 |
| 75.58 | trojan | 307.8 | 753.4 | 20.65 | 0.0 | 10.0 | 12.07 | 15.68 | Au1rxx-base64 | 149.28.241.235 |
| 75.41 | shadowsocks | 307.7 | 790.3 | 20.66 | 0.0 | 10.0 | 13.07 | 15.68 | Au1rxx-base64 | 37.19.198.244 |
| 74.87 | shadowsocks | 309.3 | 799.0 | 20.62 | 0.0 | 10.0 | 13.07 | 15.68 | Au1rxx-base64 | 185.196.61.82 |
| 74.51 | trojan | 305.2 | 747.9 | 20.71 | 0.0 | 10.0 | 12.07 | 14.32 | DeltaKronecker-all | 45.32.195.168 |
| 74.37 | trojan | 305.9 | 767.5 | 20.7 | 0.0 | 10.0 | 12.07 | 14.32 | DeltaKronecker-all | 45.32.198.247 |
| 73.61 | trojan | 287.6 | 681.2 | 21.12 | 0.0 | 10.0 | 12.07 | 14.32 | DeltaKronecker-all | 64.94.95.115 |
| 73.57 | shadowsocks | 262.7 | 645.4 | 21.7 | 0.0 | 10.0 | 13.07 | 15.68 | Au1rxx-base64 | 156.146.38.170 |
| 73.56 | shadowsocks | 253.1 | 621.6 | 21.92 | 0.0 | 10.0 | 13.07 | 15.68 | Au1rxx-base64 | 156.146.38.167 |
| 73.37 | trojan | 261.6 | 614.0 | 21.72 | 0.0 | 10.0 | 12.07 | 13.0 | Surfboard-tg-mixed | 64.94.95.118 |
| 71.69 | shadowsocks | 279.0 | 554.6 | 21.32 | 0.0 | 10.0 | 13.07 | 15.68 | Au1rxx-base64 | 173.244.56.6 |
| 70.95 | trojan | 278.3 | 645.1 | 21.33 | 0.0 | 10.0 | 12.07 | 14.32 | DeltaKronecker-all | 64.94.95.117 |
| 70.3 | shadowsocks | 289.4 | 553.9 | 21.08 | 0.0 | 10.0 | 13.07 | 15.68 | Au1rxx-base64 | 108.181.118.10 |
| 70.23 | shadowsocks | 309.0 | 604.9 | 20.63 | 0.0 | 10.0 | 13.07 | 15.68 | Au1rxx-base64 | 108.181.0.177 |
| 69.92 | shadowsocks | 284.3 | 562.3 | 21.2 | 0.0 | 10.0 | 13.07 | 14.32 | DeltaKronecker-all | 107.172.219.230 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| Au1rxx-base64 | 0.907 | 0.923 | 39 | 105 | prefer |
| Surfboard-tg-mixed | 0.833 | 0.759 | 87 | 5528 | prefer |
| mheidari-all | 0.778 | 0.702 | 84 | 16247 | prefer |
| DeltaKronecker-all | 0.757 | 0.68 | 125 | 8141 | prefer |
| Epodonios-all | 0.335 | 1.0 | 1 | 6473 | observe |
| xiaoji235-airport-v2ray-all | 0.315 | 1.0 | 1 | 1508 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4003 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6883 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4291 | observe |
| barry-far-vless | 0.255 | None | 0 | 4831 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5416 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| nscl5-all | 0.233 | None | 0 | 1439 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | TimeoutError | - | 15 |
| speed | ClientOSError | - | 14 |
| geo | TimeoutError | - | 13 |
| cn-block | ClientOSError | - | 9 |
| geo | ClientOSError | - | 9 |
| cn-block | TimeoutError | - | 9 |
| 204 | ProxyError | - | 6 |
| 204 | ClientOSError | - | 5 |
| cn-block | ProxyError | - | 3 |
| geo | ProxyError | - | 3 |
| speed | ProxyError | - | 3 |
| speed | TimeoutError | - | 1 |
| speed | ClientPayloadError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 284 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
