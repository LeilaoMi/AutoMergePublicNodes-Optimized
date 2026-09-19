# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-19 20:30:53 |
| 运行耗时 | 557.2s |
| 订阅源总数 | 107 |
| 健康订阅源 | 96 |
| 原始节点 | 91254 |
| 去重后节点 | 25369 |
| TCP 可达 | 3000 |
| 真实可用 | 459 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 25369 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 3.8 |
| geo | 1.3 |
| tcp | 42.3 |
| probe | 226.0 |
| real_test | 208.6 |
| generate | 75.1 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 54752 |
| vmess | 14439 |
| shadowsocks | 11269 |
| trojan | 8764 |
| hysteria2 | 1248 |
| http | 576 |
| shadowsocksr | 122 |
| socks | 64 |
| hysteria | 10 |
| tuic | 5 |
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
| 81.2 | http | 194.0 | 500.9 | 23.29 | 0.0 | 10.0 | 12.93 | 17.98 | ermaozi | 138.199.35.216 |
| 81.14 | http | 196.5 | 513.6 | 23.23 | 0.0 | 10.0 | 12.93 | 17.98 | ermaozi | 138.199.35.198 |
| 80.82 | shadowsocks | 215.7 | 535.8 | 22.78 | 0.0 | 10.0 | 14.04 | 18.0 | Au1rxx-base64 | 173.244.56.6 |
| 80.81 | vless | 202.2 | 529.1 | 23.1 | 0.0 | 10.0 | 9.71 | 18.0 | Au1rxx-base64 | 172.235.43.210 |
| 80.71 | shadowsocks | 220.6 | 546.2 | 22.67 | 0.0 | 10.0 | 14.04 | 18.0 | Au1rxx-base64 | 173.244.56.9 |
| 79.81 | shadowsocks | 259.5 | 625.8 | 21.77 | 0.0 | 10.0 | 14.04 | 18.0 | Au1rxx-base64 | 156.146.38.170 |
| 79.07 | shadowsocks | 259.6 | 635.6 | 21.77 | 0.0 | 10.0 | 14.04 | 18.0 | Au1rxx-base64 | 156.146.38.168 |
| 78.41 | vless | 305.9 | 793.7 | 20.7 | 0.0 | 10.0 | 9.71 | 18.0 | Au1rxx-base64 | 198.200.42.129 |
| 76.95 | trojan | 230.3 | 531.4 | 22.45 | 0.0 | 10.0 | 9.0 | 18.0 | Au1rxx-base64 | 100.42.228.109 |
| 76.24 | vless | 217.9 | 516.4 | 22.73 | 0.0 | 10.0 | 9.71 | 13.8 | mheidari-all | 47.251.108.158 |
| 75.95 | shadowsocks | 291.4 | 633.4 | 21.03 | 0.0 | 10.0 | 14.04 | 18.0 | Au1rxx-base64 | 149.22.95.183 |
| 75.9 | vless | 220.0 | 496.2 | 22.69 | 0.0 | 10.0 | 9.71 | 18.0 | Au1rxx-base64 | 104.18.46.234 |
| 74.95 | vless | 332.4 | 749.3 | 20.08 | 0.0 | 10.0 | 9.71 | 18.0 | Au1rxx-base64 | 79.141.172.154 |
| 74.4 | vless | 353.6 | 842.9 | 19.59 | 0.0 | 10.0 | 9.71 | 18.0 | Au1rxx-base64 | 15.204.97.216 |
| 73.54 | vless | 215.4 | 498.0 | 22.79 | 0.0 | 10.0 | 9.71 | 18.0 | Au1rxx-base64 | 172.64.229.170 |
| 73.49 | http | 349.5 | 623.7 | 19.69 | 0.0 | 10.0 | 12.93 | 17.98 | ermaozi | 38.28.193.188 |
| 73.04 | shadowsocks | 342.6 | 729.9 | 19.85 | 0.0 | 10.0 | 14.04 | 18.0 | Au1rxx-base64 | 37.19.198.160 |
| 72.31 | vless | 283.2 | 428.3 | 21.22 | 0.0 | 10.0 | 9.71 | 18.0 | Au1rxx-base64 | 172.64.158.146 |
| 72.13 | vless | 390.6 | 789.3 | 18.74 | 0.0 | 10.0 | 9.71 | 18.0 | Au1rxx-base64 | 150.241.102.181 |
| 71.9 | vless | 274.9 | 428.3 | 21.42 | 0.0 | 10.0 | 9.71 | 18.0 | Au1rxx-base64 | 104.18.47.113 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.915 | 0.851 | 303 | 1650 | prefer |
| ermaozi | 0.899 | 0.92 | 25 | 250 | prefer |
| Surfboard-tg-mixed | 0.728 | 0.65 | 157 | 7211 | prefer |
| mheidari-all | 0.631 | 0.552 | 125 | 19269 | observe |
| DeltaKronecker-all | 0.372 | 0.444 | 9 | 6421 | observe |
| mahdibland-V2RayAggregator | 0.335 | 1.0 | 1 | 4251 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5174 | observe |
| Epodonios-all | 0.255 | None | 0 | 7761 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9098 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5765 | observe |
| barry-far-vless | 0.255 | None | 0 | 6077 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 3625 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | ClientOSError | - | 42 |
| geo | TimeoutError | - | 33 |
| cn-block | ClientOSError | - | 26 |
| 204 | TimeoutError | - | 20 |
| cn-block | TimeoutError | - | 14 |
| 204 | ProxyError | - | 11 |
| speed | ClientOSError | - | 7 |
| speed | TimeoutError | - | 6 |
| 204 | ClientOSError | - | 2 |
| cn-block | ProxyError | - | 2 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
