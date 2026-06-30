# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-06-30 09:55:27 |
| 运行耗时 | 264.4s |
| 订阅源总数 | 107 |
| 健康订阅源 | 104 |
| 原始节点 | 75261 |
| 去重后节点 | 23023 |
| TCP 可达 | 3000 |
| 真实可用 | 418 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23023 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.0 |
| geo | 1.4 |
| tcp | 29.7 |
| probe | 62.6 |
| real_test | 132.4 |
| generate | 33.3 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 41860 |
| trojan | 13014 |
| vmess | 10350 |
| shadowsocks | 9411 |
| hysteria2 | 263 |
| shadowsocksr | 155 |
| http | 135 |
| socks | 66 |
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
| 77.36 | vless | 168.6 | 470.4 | 23.87 | 0.0 | 10.0 | 7.71 | 15.78 | Surfboard-tg-mixed | 64.23.143.23 |
| 74.86 | vless | 257.9 | 590.9 | 21.81 | 0.0 | 10.0 | 7.71 | 15.5 | mheidari-all | 34.213.172.16 |
| 74.18 | vless | 207.9 | 518.6 | 22.97 | 0.0 | 10.0 | 7.71 | 15.5 | mheidari-all | 107.173.237.146 |
| 71.65 | vless | 358.7 | 352.0 | 19.47 | 1.8 | 10.0 | 7.71 | 15.5 | mheidari-all | 104.18.42.68 |
| 70.81 | shadowsocks | 189.0 | 496.8 | 23.4 | 0.0 | 10.0 | 8.49 | 13.42 | Au1rxx-base64 | 108.181.0.177 |
| 70.62 | vless | 358.0 | 747.9 | 19.49 | 0.0 | 10.0 | 7.71 | 13.42 | Au1rxx-base64 | 15.204.97.214 |
| 70.57 | shadowsocks | 221.2 | 498.5 | 22.66 | 0.0 | 10.0 | 8.49 | 13.42 | Au1rxx-base64 | 173.244.56.9 |
| 70.5 | shadowsocks | 224.3 | 526.0 | 22.59 | 0.0 | 10.0 | 8.49 | 13.42 | Au1rxx-base64 | 149.22.95.183 |
| 69.9 | trojan | 245.1 | 522.3 | 22.1 | 0.0 | 10.0 | 11.92 | 15.78 | Surfboard-tg-mixed | 94.140.0.100 |
| 69.58 | shadowsocks | 263.7 | 659.2 | 21.67 | 0.0 | 10.0 | 8.49 | 13.42 | Au1rxx-base64 | 173.244.56.6 |
| 69.49 | trojan | 386.6 | 898.2 | 18.83 | 0.0 | 10.0 | 11.92 | 15.5 | mheidari-all | 64.94.95.118 |
| 68.75 | shadowsocks | 277.9 | 774.5 | 21.34 | 0.0 | 10.0 | 8.49 | 13.42 | Au1rxx-base64 | 108.181.118.10 |
| 66.86 | trojan | 386.2 | 461.2 | 18.84 | 0.0 | 10.0 | 11.92 | 15.78 | Surfboard-tg-mixed | 199.181.197.176 |
| 66.75 | trojan | 395.5 | 481.4 | 18.62 | 0.0 | 10.0 | 11.92 | 15.78 | Surfboard-tg-mixed | 45.131.4.118 |
| 66.29 | shadowsocks | 295.2 | 664.3 | 20.95 | 0.0 | 10.0 | 8.49 | 13.42 | Au1rxx-base64 | 156.146.38.167 |
| 66.2 | shadowsocks | 294.0 | 660.1 | 20.97 | 0.0 | 10.0 | 8.49 | 13.42 | Au1rxx-base64 | 156.146.38.168 |
| 65.69 | trojan | 437.6 | 351.0 | 17.65 | 1.84 | 9.48 | 11.92 | 15.5 | mheidari-all | 119.246.1.143 |
| 65.48 | shadowsocks | 292.6 | 657.1 | 21.01 | 0.0 | 10.0 | 8.49 | 13.42 | Au1rxx-base64 | 156.146.38.169 |
| 65.14 | vless | 275.1 | 442.5 | 21.41 | 0.0 | 10.0 | 7.71 | 15.5 | mheidari-all | 108.162.195.58 |
| 65.14 | vless | 429.7 | 885.7 | 17.83 | 0.0 | 10.0 | 7.71 | 15.5 | mheidari-all | 47.253.226.114 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| Au1rxx-base64 | 0.754 | 0.761 | 46 | 96 | prefer |
| Surfboard-tg-mixed | 0.713 | 0.634 | 287 | 5386 | prefer |
| mheidari-all | 0.62 | 0.541 | 233 | 15701 | observe |
| DeltaKronecker-all | 0.507 | 0.425 | 87 | 7352 | observe |
| Barabama-yudou | 0.318 | 1.0 | 2 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4139 | observe |
| Epodonios-all | 0.255 | None | 0 | 6386 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3981 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6946 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 3959 | observe |
| barry-far-vless | 0.255 | None | 0 | 4573 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5353 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| xiaoji235-airport-v2ray-all | 0.223 | None | 0 | 1204 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 149 |
| geo | TimeoutError | - | 33 |
| 204 | TimeoutError | - | 28 |
| 204 | ClientOSError | - | 14 |
| cn-block | TimeoutError | - | 12 |
| 204 | ProxyError | - | 11 |
| geo | ClientOSError | - | 10 |
| speed | TimeoutError | - | 8 |
| cn-block | ClientOSError | - | 4 |
| cn-block | ProxyError | - | 2 |
| geo | ProxyError | - | 1 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
