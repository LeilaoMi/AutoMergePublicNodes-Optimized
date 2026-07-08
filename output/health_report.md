# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-08 19:44:33 |
| 运行耗时 | 179.7s |
| 订阅源总数 | 107 |
| 健康订阅源 | 102 |
| 原始节点 | 83228 |
| 去重后节点 | 24965 |
| TCP 可达 | 3000 |
| 真实可用 | 288 |
| Verified 输出 | 288 |
| Global 输出 | 291 |
| All 输出 | 24965 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.8 |
| geo | 1.4 |
| tcp | 32.3 |
| probe | 43.7 |
| real_test | 75.8 |
| generate | 19.7 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 48859 |
| trojan | 13202 |
| vmess | 10519 |
| shadowsocks | 9472 |
| hysteria2 | 828 |
| shadowsocksr | 140 |
| http | 140 |
| socks | 55 |
| hysteria | 8 |
| anytls | 3 |
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
| 77.14 | shadowsocks | 265.0 | 641.5 | 21.64 | 0.0 | 10.0 | 12.52 | 16.98 | Au1rxx-base64 | 37.19.198.236 |
| 76.93 | shadowsocks | 274.2 | 695.4 | 21.43 | 0.0 | 10.0 | 12.52 | 16.98 | Au1rxx-base64 | 37.19.198.243 |
| 76.8 | shadowsocks | 279.7 | 686.4 | 21.3 | 0.0 | 10.0 | 12.52 | 16.98 | Au1rxx-base64 | 37.19.198.244 |
| 74.49 | shadowsocks | 289.2 | 662.9 | 21.08 | 0.0 | 10.0 | 12.52 | 16.98 | Au1rxx-base64 | 108.181.57.93 |
| 73.3 | shadowsocks | 331.7 | 865.3 | 20.1 | 0.0 | 10.0 | 12.52 | 15.18 | mheidari-all | 185.196.61.82 |
| 73.21 | shadowsocks | 276.5 | 690.4 | 21.38 | 0.0 | 10.0 | 12.52 | 16.98 | Au1rxx-base64 | 37.19.198.160 |
| 72.71 | vmess | 422.7 | 1093.3 | 17.99 | 0.0 | 10.0 | 13.12 | 16.28 | Surfboard-tg-mixed | 67.220.85.46 |
| 72.23 | trojan | 310.2 | 726.4 | 20.6 | 0.0 | 10.0 | 10.27 | 15.18 | mheidari-all | 149.28.241.235 |
| 71.79 | shadowsocks | 309.9 | 636.3 | 20.6 | 0.0 | 10.0 | 12.52 | 16.98 | Au1rxx-base64 | 149.22.95.183 |
| 71.12 | trojan | 257.3 | 605.0 | 21.82 | 0.0 | 10.0 | 10.27 | 12.78 | DeltaKronecker-all | 64.94.95.114 |
| 71.09 | shadowsocks | 277.9 | 675.6 | 21.34 | 0.0 | 10.0 | 12.52 | 16.98 | Au1rxx-base64 | tinkered-pennies-puppies.freesocks.work |
| 70.98 | shadowsocks | 293.2 | 562.7 | 20.99 | 0.0 | 10.0 | 12.52 | 16.98 | Au1rxx-base64 | 173.244.56.6 |
| 70.96 | trojan | 256.1 | 604.9 | 21.85 | 0.0 | 10.0 | 10.27 | 12.78 | DeltaKronecker-all | 64.94.95.115 |
| 70.68 | trojan | 265.6 | 610.7 | 21.63 | 0.0 | 10.0 | 10.27 | 12.78 | DeltaKronecker-all | 64.94.95.117 |
| 70.59 | shadowsocks | 253.6 | 617.5 | 21.91 | 0.0 | 10.0 | 12.52 | 16.98 | Au1rxx-base64 | 156.146.38.168 |
| 70.59 | shadowsocks | 312.2 | 804.7 | 20.55 | 0.0 | 10.0 | 12.52 | 16.98 | Au1rxx-base64 | 198.98.53.130 |
| 70.47 | shadowsocks | 259.4 | 639.9 | 21.77 | 0.0 | 10.0 | 12.52 | 16.98 | Au1rxx-base64 | 156.146.38.170 |
| 69.89 | shadowsocks | 334.0 | 849.0 | 20.05 | 0.0 | 10.0 | 12.52 | 16.98 | Au1rxx-base64 | 147.90.234.133 |
| 69.69 | trojan | 310.9 | 733.4 | 20.58 | 0.0 | 10.0 | 10.27 | 12.78 | DeltaKronecker-all | 45.32.198.247 |
| 69.34 | shadowsocks | 352.8 | 690.7 | 19.61 | 0.0 | 10.0 | 12.52 | 16.98 | Au1rxx-base64 | 108.181.118.10 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| DeltaKronecker-all | 0.921 | 0.849 | 86 | 8321 | prefer |
| mheidari-all | 0.906 | 0.836 | 67 | 18123 | prefer |
| Au1rxx-base64 | 0.845 | 0.851 | 67 | 120 | prefer |
| Surfboard-tg-mixed | 0.69 | 0.612 | 103 | 5933 | observe |
| xiaoji235-airport-v2ray-all | 0.4 | 0.75 | 4 | 3640 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4408 | observe |
| Epodonios-all | 0.255 | None | 0 | 6761 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3976 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6878 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4429 | observe |
| barry-far-vless | 0.255 | None | 0 | 4940 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5361 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| nscl5-all | 0.237 | None | 0 | 1561 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 30 |
| 204 | TimeoutError | - | 10 |
| geo | TimeoutError | - | 8 |
| 204 | ClientOSError | - | 7 |
| geo | ClientOSError | - | 7 |
| geo | ProxyError | - | 5 |
| 204 | ProxyError | - | 4 |
| cn-block | ClientOSError | - | 2 |
| cn-block | ProxyError | - | 2 |
| speed | TimeoutError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 280 | 288 | - |
| global | False | 292 | 291 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
