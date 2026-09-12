# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-12 15:30:31 |
| 运行耗时 | 614.2s |
| 订阅源总数 | 107 |
| 健康订阅源 | 94 |
| 原始节点 | 83067 |
| 去重后节点 | 22816 |
| TCP 可达 | 3000 |
| 真实可用 | 470 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22816 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.8 |
| geo | 1.4 |
| tcp | 38.1 |
| probe | 254.2 |
| real_test | 239.0 |
| generate | 76.7 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 50552 |
| vmess | 12589 |
| shadowsocks | 9742 |
| trojan | 7933 |
| hysteria2 | 1468 |
| http | 580 |
| shadowsocksr | 129 |
| socks | 56 |
| hysteria | 9 |
| tuic | 8 |
| anytls | 1 |

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
| 79.53 | vless | 228.1 | 583.1 | 22.5 | 0.0 | 10.0 | 9.15 | 17.88 | Au1rxx-base64 | 216.36.124.176 |
| 79.43 | vless | 232.4 | 589.5 | 22.4 | 0.0 | 10.0 | 9.15 | 17.88 | Au1rxx-base64 | 172.235.38.85 |
| 79.35 | vless | 235.7 | 534.4 | 22.32 | 0.0 | 10.0 | 9.15 | 17.88 | Au1rxx-base64 | 31.58.50.200 |
| 79.03 | vless | 249.5 | 647.1 | 22.0 | 0.0 | 10.0 | 9.15 | 17.88 | Au1rxx-base64 | 172.235.43.210 |
| 79.03 | vless | 249.8 | 631.1 | 22.0 | 0.0 | 10.0 | 9.15 | 17.88 | Au1rxx-base64 | 172.233.139.46 |
| 77.97 | shadowsocks | 300.5 | 756.2 | 20.82 | 0.0 | 10.0 | 13.77 | 17.88 | Au1rxx-base64 | 156.146.38.169 |
| 76.77 | shadowsocks | 328.3 | 842.1 | 20.18 | 0.0 | 10.0 | 13.77 | 17.88 | Au1rxx-base64 | 156.146.38.168 |
| 76.56 | shadowsocks | 189.5 | 489.8 | 23.39 | 0.0 | 10.0 | 13.77 | 13.9 | mheidari-all | 108.181.118.10 |
| 76.17 | hysteria2 | 363.7 | 817.4 | 19.36 | 0.0 | 10.0 | 13.12 | 17.88 | Au1rxx-base64 | 159.223.157.129 |
| 75.2 | shadowsocks | 269.9 | 698.9 | 21.53 | 0.0 | 10.0 | 13.77 | 13.9 | mheidari-all | 173.244.56.9 |
| 74.69 | shadowsocks | 464.0 | 1246.6 | 17.04 | 0.0 | 10.0 | 13.77 | 17.88 | Au1rxx-base64 | 156.146.38.170 |
| 74.54 | shadowsocks | 277.0 | 715.7 | 21.37 | 0.0 | 10.0 | 13.77 | 13.9 | mheidari-all | 108.181.0.177 |
| 74.51 | shadowsocks | 321.4 | 706.5 | 20.34 | 0.0 | 10.0 | 13.77 | 17.88 | Au1rxx-base64 | 149.22.95.183 |
| 74.46 | vless | 385.1 | 941.8 | 18.86 | 0.0 | 10.0 | 9.15 | 17.88 | Au1rxx-base64 | 15.204.97.216 |
| 73.26 | vless | 304.3 | 535.8 | 20.73 | 0.0 | 10.0 | 9.15 | 17.88 | Au1rxx-base64 | 104.18.39.218 |
| 72.48 | shadowsocks | 354.7 | 767.1 | 19.57 | 0.0 | 10.0 | 13.77 | 17.88 | Au1rxx-base64 | 37.19.198.243 |
| 72.46 | vless | 252.5 | 592.3 | 21.93 | 0.0 | 10.0 | 9.15 | 17.88 | Au1rxx-base64 | 172.64.154.8 |
| 72.37 | shadowsocks | 269.2 | 632.2 | 21.55 | 0.0 | 10.0 | 13.77 | 13.52 | Surfboard-tg-mixed | 23.150.248.20 |
| 72.2 | trojan | 372.8 | 900.6 | 19.15 | 0.0 | 10.0 | 10.62 | 17.88 | Au1rxx-base64 | 64.94.95.114 |
| 72.18 | shadowsocks | 358.3 | 761.7 | 19.48 | 0.0 | 10.0 | 13.77 | 17.88 | Au1rxx-base64 | 198.98.53.130 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.93 | 0.875 | 303 | 1455 | prefer |
| DeltaKronecker-all | 0.791 | 0.721 | 43 | 5970 | prefer |
| Surfboard-tg-mixed | 0.765 | 0.688 | 144 | 7345 | prefer |
| mheidari-all | 0.646 | 0.568 | 81 | 15620 | observe |
| ermaozi | 0.637 | 0.629 | 35 | 393 | observe |
| ermaozi-get_subscribe | 0.425 | 0.833 | 6 | 408 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| roosterkid-openproxylist-v2ray | 0.261 | 1.0 | 1 | 150 | observe |
| Epodonios-all | 0.255 | None | 0 | 7743 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 8959 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5912 | observe |
| barry-far-vless | 0.255 | None | 0 | 6112 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4207 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | ClientOSError | - | 53 |
| cn-block | TimeoutError | - | 20 |
| 204 | ProxyError | - | 18 |
| cn-block | ClientOSError | - | 14 |
| speed | ClientOSError | - | 14 |
| 204 | TimeoutError | - | 9 |
| speed | TimeoutError | - | 9 |
| geo | TimeoutError | - | 4 |
| 204 | ClientOSError | - | 3 |
| cn-block | ProxyError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
