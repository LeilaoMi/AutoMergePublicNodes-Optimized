# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-12 08:29:05 |
| 运行耗时 | 213.0s |
| 订阅源总数 | 107 |
| 健康订阅源 | 103 |
| 原始节点 | 76269 |
| 去重后节点 | 24037 |
| TCP 可达 | 3000 |
| 真实可用 | 408 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 24037 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.9 |
| geo | 1.3 |
| tcp | 31.7 |
| probe | 46.3 |
| real_test | 94.1 |
| generate | 34.7 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 43775 |
| trojan | 11950 |
| vmess | 10598 |
| shadowsocks | 9341 |
| hysteria2 | 271 |
| shadowsocksr | 148 |
| http | 136 |
| socks | 38 |
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
| 78.3 | trojan | 300.4 | 742.5 | 20.82 | 0.0 | 10.0 | 14.26 | 15.72 | Au1rxx-base64 | 149.28.241.235 |
| 77.07 | shadowsocks | 248.7 | 620.7 | 22.02 | 0.0 | 10.0 | 13.33 | 15.72 | Au1rxx-base64 | 156.146.38.168 |
| 77.03 | shadowsocks | 250.6 | 615.6 | 21.98 | 0.0 | 10.0 | 13.33 | 15.72 | Au1rxx-base64 | 198.98.53.130 |
| 76.84 | shadowsocks | 258.6 | 630.2 | 21.79 | 0.0 | 10.0 | 13.33 | 15.72 | Au1rxx-base64 | 156.146.38.167 |
| 76.8 | shadowsocks | 260.5 | 642.7 | 21.75 | 0.0 | 10.0 | 13.33 | 15.72 | Au1rxx-base64 | 156.146.38.169 |
| 76.69 | shadowsocks | 265.1 | 662.7 | 21.64 | 0.0 | 10.0 | 13.33 | 15.72 | Au1rxx-base64 | 37.19.198.236 |
| 76.54 | shadowsocks | 271.8 | 679.9 | 21.49 | 0.0 | 10.0 | 13.33 | 15.72 | Au1rxx-base64 | 37.19.198.243 |
| 75.73 | shadowsocks | 263.4 | 662.8 | 21.68 | 0.0 | 10.0 | 13.33 | 15.72 | Au1rxx-base64 | 37.19.198.160 |
| 74.92 | shadowsocks | 255.2 | 631.5 | 21.87 | 0.0 | 10.0 | 13.33 | 15.72 | Au1rxx-base64 | 156.146.38.170 |
| 73.65 | trojan | 308.0 | 753.2 | 20.65 | 0.0 | 10.0 | 14.26 | 11.54 | mheidari-all | 45.32.195.168 |
| 72.95 | shadowsocks | 317.1 | 818.8 | 20.44 | 0.0 | 10.0 | 13.33 | 15.72 | Au1rxx-base64 | 37.19.198.244 |
| 71.63 | shadowsocks | 281.0 | 685.5 | 21.27 | 0.0 | 10.0 | 13.33 | 11.54 | mheidari-all | 108.181.57.93 |
| 71.35 | trojan | 352.8 | 872.3 | 19.61 | 0.0 | 10.0 | 14.26 | 11.54 | mheidari-all | 64.94.95.118 |
| 71.17 | shadowsocks | 317.4 | 615.2 | 20.43 | 0.0 | 10.0 | 13.33 | 15.72 | Au1rxx-base64 | 149.22.95.183 |
| 71.14 | trojan | 312.3 | 732.2 | 20.55 | 0.0 | 10.0 | 14.26 | 9.14 | DeltaKronecker-all | 45.32.198.247 |
| 70.98 | shadowsocks | 309.8 | 798.7 | 20.61 | 0.0 | 10.0 | 13.33 | 11.54 | mheidari-all | 185.196.61.82 |
| 70.89 | shadowsocks | 307.4 | 544.3 | 20.66 | 0.0 | 10.0 | 13.33 | 15.72 | Au1rxx-base64 | 173.244.56.6 |
| 70.72 | trojan | 299.7 | 730.8 | 20.84 | 0.0 | 10.0 | 14.26 | 9.14 | DeltaKronecker-all | 64.94.95.115 |
| 70.68 | trojan | 294.2 | 704.7 | 20.97 | 0.0 | 10.0 | 14.26 | 9.14 | DeltaKronecker-all | 64.94.95.117 |
| 69.93 | trojan | 302.8 | 732.9 | 20.77 | 0.0 | 10.0 | 14.26 | 9.14 | DeltaKronecker-all | 64.94.95.114 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| mheidari-all | 0.824 | 0.75 | 84 | 16299 | prefer |
| Au1rxx-base64 | 0.784 | 0.789 | 57 | 118 | prefer |
| DeltaKronecker-all | 0.716 | 0.638 | 185 | 8141 | prefer |
| Surfboard-tg-mixed | 0.65 | 0.57 | 256 | 5318 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4003 | observe |
| Epodonios-all | 0.255 | None | 0 | 6278 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3972 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6422 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4019 | observe |
| barry-far-vless | 0.255 | None | 0 | 4645 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5416 | observe |
| xiaoji235-airport-v2ray-all | 0.235 | None | 0 | 1508 | observe |
| nscl5-all | 0.233 | None | 0 | 1439 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 83 |
| geo | TimeoutError | - | 45 |
| 204 | ProxyError | - | 18 |
| geo | ClientOSError | - | 14 |
| cn-block | ClientOSError | - | 14 |
| 204 | TimeoutError | - | 9 |
| speed | TimeoutError | - | 7 |
| cn-block | ProxyError | - | 6 |
| 204 | ClientOSError | - | 6 |
| cn-block | TimeoutError | - | 5 |
| geo | ProxyError | - | 3 |
| speed | ProxyError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
