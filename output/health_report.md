# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-12 05:41:34 |
| 运行耗时 | 1175.0s |
| 订阅源总数 | 107 |
| 健康订阅源 | 94 |
| 原始节点 | 99742 |
| 去重后节点 | 27632 |
| TCP 可达 | 3000 |
| 真实可用 | 546 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 27632 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.9 |
| geo | 1.4 |
| tcp | 47.1 |
| probe | 444.7 |
| real_test | 591.9 |
| generate | 84.0 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 58167 |
| vmess | 15773 |
| shadowsocks | 11934 |
| trojan | 11407 |
| hysteria2 | 1489 |
| http | 683 |
| shadowsocksr | 165 |
| socks | 69 |
| anytls | 31 |
| hysteria | 16 |
| tuic | 8 |

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
| 85.87 | vless | 211.8 | 497.9 | 22.88 | 0.0 | 10.0 | 12.99 | 20.0 | Au1rxx-base64 | 137.175.82.40 |
| 85.81 | vless | 214.0 | 528.0 | 22.82 | 0.0 | 10.0 | 12.99 | 20.0 | Au1rxx-base64 | 154.9.241.170 |
| 83.62 | hysteria2 | 229.0 | 232.0 | 22.48 | 6.3 | 9.91 | 12.14 | 20.0 | Au1rxx-base64 | 45.32.10.7 |
| 83.61 | vless | 309.0 | 796.7 | 20.62 | 0.0 | 10.0 | 12.99 | 20.0 | Au1rxx-base64 | 154.29.145.196 |
| 83.35 | vless | 316.6 | 730.7 | 20.45 | 0.0 | 10.0 | 12.99 | 20.0 | Au1rxx-base64 | 154.12.38.202 |
| 83.18 | hysteria2 | 241.3 | 236.1 | 22.19 | 6.14 | 9.86 | 12.14 | 20.0 | Au1rxx-base64 | 158.101.148.79 |
| 82.32 | vless | 316.9 | 785.9 | 20.44 | 0.0 | 10.0 | 12.99 | 20.0 | Au1rxx-base64 | 23.95.222.127 |
| 82.31 | trojan | 258.5 | 609.1 | 21.79 | 0.0 | 10.0 | 14.66 | 18.86 | DeltaKronecker-all | 107.149.159.190 |
| 81.94 | shadowsocks | 214.4 | 535.4 | 22.82 | 0.0 | 10.0 | 13.12 | 20.0 | Au1rxx-base64 | 173.244.56.9 |
| 81.83 | shadowsocks | 219.0 | 546.4 | 22.71 | 0.0 | 10.0 | 13.12 | 20.0 | Au1rxx-base64 | 173.244.56.6 |
| 81.74 | vless | 265.2 | 583.9 | 21.64 | 0.0 | 10.0 | 12.99 | 20.0 | Au1rxx-base64 | 15.204.97.216 |
| 81.63 | vless | 268.7 | 592.1 | 21.56 | 0.0 | 10.0 | 12.99 | 20.0 | Au1rxx-base64 | 15.204.97.197 |
| 80.87 | shadowsocks | 260.3 | 633.8 | 21.75 | 0.0 | 10.0 | 13.12 | 20.0 | Au1rxx-base64 | 156.146.38.170 |
| 80.81 | shadowsocks | 263.1 | 643.7 | 21.69 | 0.0 | 10.0 | 13.12 | 20.0 | Au1rxx-base64 | 156.146.38.169 |
| 80.72 | vless | 297.2 | 620.8 | 20.9 | 0.0 | 10.0 | 12.99 | 20.0 | Au1rxx-base64 | 51.81.203.63 |
| 80.58 | vless | 288.5 | 676.9 | 21.1 | 0.0 | 10.0 | 12.99 | 20.0 | Au1rxx-base64 | 147.45.60.160 |
| 80.35 | shadowsocks | 239.8 | 548.5 | 22.23 | 0.0 | 10.0 | 13.12 | 20.0 | Au1rxx-base64 | 5.78.51.123 |
| 79.62 | vless | 216.4 | 562.6 | 22.77 | 0.0 | 10.0 | 12.99 | 18.86 | DeltaKronecker-all | 178.130.47.207 |
| 79.2 | shadowsocks | 237.6 | 634.0 | 22.28 | 0.0 | 10.0 | 13.12 | 18.3 | mheidari-all | 173.234.25.90 |
| 79.09 | hysteria2 | 290.1 | 567.3 | 21.06 | 0.0 | 10.0 | 12.14 | 20.0 | Au1rxx-base64 | 66.94.121.46 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.978 | 0.907 | 389 | 1810 | prefer |
| ermaozi | 0.683 | 0.66 | 53 | 708 | observe |
| DeltaKronecker-all | 0.505 | 0.424 | 250 | 5372 | observe |
| Surfboard-tg-mixed | 0.349 | 0.667 | 3 | 7200 | observe |
| mheidari-all | 0.342 | 0.259 | 185 | 23656 | observe |
| ermaozi-get_subscribe | 0.279 | 1.0 | 1 | 600 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| Epodonios-all | 0.255 | None | 0 | 7699 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9920 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5717 | observe |
| barry-far-vless | 0.255 | None | 0 | 5961 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4284 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |
| Au1rxx-clash | 0.247 | None | 0 | 1810 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 160 |
| speed | TimeoutError | - | 43 |
| geo | ClientOSError | - | 35 |
| 204 | ProxyError | - | 26 |
| cn-block | TimeoutError | - | 22 |
| speed | ClientOSError | - | 22 |
| 204 | TimeoutError | - | 12 |
| cn-block | ClientOSError | - | 12 |
| cn-block | ProxyError | - | 2 |
| speed | ProxyError | - | 2 |
| geo | ProxyError | - | 2 |
| 204 | ClientOSError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
