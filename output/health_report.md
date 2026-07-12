# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-12 19:16:14 |
| 运行耗时 | 204.0s |
| 订阅源总数 | 107 |
| 健康订阅源 | 103 |
| 原始节点 | 77366 |
| 去重后节点 | 24159 |
| TCP 可达 | 3000 |
| 真实可用 | 266 |
| Verified 输出 | 266 |
| Global 输出 | 294 |
| All 输出 | 24159 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.3 |
| geo | 1.3 |
| tcp | 31.9 |
| probe | 45.8 |
| real_test | 78.8 |
| generate | 42.0 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 44831 |
| trojan | 11673 |
| vmess | 10639 |
| shadowsocks | 9572 |
| hysteria2 | 329 |
| shadowsocksr | 143 |
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
| 78.3 | shadowsocks | 251.3 | 601.9 | 21.96 | 0.0 | 10.0 | 12.2 | 18.14 | Au1rxx-base64 | 156.146.38.168 |
| 78.24 | shadowsocks | 254.1 | 630.0 | 21.9 | 0.0 | 10.0 | 12.2 | 18.14 | Au1rxx-base64 | 198.98.53.130 |
| 78.19 | shadowsocks | 256.0 | 614.6 | 21.85 | 0.0 | 10.0 | 12.2 | 18.14 | Au1rxx-base64 | 156.146.38.169 |
| 78.09 | shadowsocks | 260.3 | 638.9 | 21.75 | 0.0 | 10.0 | 12.2 | 18.14 | Au1rxx-base64 | 156.146.38.170 |
| 77.34 | trojan | 312.8 | 732.3 | 20.54 | 0.0 | 10.0 | 11.74 | 18.14 | Au1rxx-base64 | 45.32.195.168 |
| 77.27 | trojan | 318.2 | 740.5 | 20.41 | 0.0 | 10.0 | 11.74 | 18.14 | Au1rxx-base64 | 149.28.241.235 |
| 77.16 | shadowsocks | 300.4 | 760.5 | 20.82 | 0.0 | 10.0 | 12.2 | 18.14 | Au1rxx-base64 | 156.146.38.167 |
| 76.67 | shadowsocks | 288.5 | 727.5 | 21.1 | 0.0 | 10.0 | 12.2 | 18.14 | Au1rxx-base64 | 37.19.198.160 |
| 76.55 | shadowsocks | 308.8 | 781.4 | 20.63 | 0.0 | 10.0 | 12.2 | 18.14 | Au1rxx-base64 | 37.19.198.243 |
| 75.93 | shadowsocks | 332.2 | 862.5 | 20.09 | 0.0 | 10.0 | 12.2 | 18.14 | Au1rxx-base64 | 185.196.61.82 |
| 75.13 | shadowsocks | 280.8 | 695.4 | 21.28 | 0.0 | 10.0 | 12.2 | 18.14 | Au1rxx-base64 | 37.19.198.244 |
| 74.68 | trojan | 308.8 | 747.2 | 20.63 | 0.0 | 10.0 | 11.74 | 15.14 | DeltaKronecker-all | 45.32.198.247 |
| 74.43 | shadowsocks | 273.9 | 672.2 | 21.44 | 0.0 | 10.0 | 12.2 | 18.14 | Au1rxx-base64 | 37.19.198.236 |
| 74.12 | shadowsocks | 368.2 | 934.9 | 19.25 | 0.0 | 10.0 | 12.2 | 18.14 | Au1rxx-base64 | 108.181.57.93 |
| 73.46 | trojan | 300.9 | 666.1 | 20.81 | 0.0 | 10.0 | 11.74 | 16.66 | Surfboard-tg-mixed | 104.21.52.100 |
| 73.05 | shadowsocks | 296.0 | 547.2 | 20.93 | 0.0 | 10.0 | 12.2 | 18.14 | Au1rxx-base64 | 149.22.95.183 |
| 72.48 | shadowsocks | 305.1 | 545.0 | 20.72 | 0.0 | 10.0 | 12.2 | 18.14 | Au1rxx-base64 | 173.244.56.6 |
| 71.05 | shadowsocks | 322.4 | 595.6 | 20.31 | 0.0 | 10.0 | 12.2 | 18.14 | Au1rxx-base64 | 108.181.118.10 |
| 70.87 | vmess | 446.5 | 1137.5 | 17.44 | 0.0 | 10.0 | 12.86 | 16.66 | Surfboard-tg-mixed | 67.220.85.46 |
| 70.71 | shadowsocks | 367.1 | 774.2 | 19.28 | 0.0 | 10.0 | 12.2 | 18.14 | Au1rxx-base64 | 108.181.0.177 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| Au1rxx-base64 | 0.833 | 0.838 | 68 | 115 | prefer |
| mheidari-all | 0.77 | 0.696 | 69 | 16307 | prefer |
| Surfboard-tg-mixed | 0.737 | 0.66 | 97 | 5587 | prefer |
| DeltaKronecker-all | 0.646 | 0.567 | 104 | 8141 | observe |
| xiaoji235-airport-v2ray-all | 0.315 | 1.0 | 1 | 1508 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4003 | observe |
| Epodonios-all | 0.255 | None | 0 | 6616 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6361 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4317 | observe |
| barry-far-vless | 0.255 | None | 0 | 4906 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5438 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 27 |
| cn-block | TimeoutError | - | 21 |
| cn-block | ClientOSError | - | 15 |
| 204 | TimeoutError | - | 10 |
| geo | TimeoutError | - | 9 |
| 204 | ProxyError | - | 8 |
| 204 | ClientOSError | - | 7 |
| cn-block | ProxyError | - | 5 |
| speed | TimeoutError | - | 4 |
| geo | ProxyError | - | 3 |
| geo | ClientOSError | - | 1 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 284 | 266 | - |
| global | False | 300 | 294 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
