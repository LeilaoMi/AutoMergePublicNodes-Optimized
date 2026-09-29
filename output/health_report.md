# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-29 22:13:46 |
| 运行耗时 | 523.3s |
| 订阅源总数 | 107 |
| 健康订阅源 | 94 |
| 原始节点 | 96969 |
| 去重后节点 | 27166 |
| TCP 可达 | 3000 |
| 真实可用 | 402 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 27166 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.3 |
| geo | 1.4 |
| tcp | 45.8 |
| probe | 227.0 |
| real_test | 155.7 |
| generate | 88.1 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 59106 |
| vmess | 15091 |
| shadowsocks | 11363 |
| trojan | 9149 |
| hysteria2 | 1388 |
| http | 584 |
| shadowsocksr | 168 |
| socks | 73 |
| anytls | 24 |
| hysteria | 15 |
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
| 81.45 | hysteria2 | 271.1 | 605.2 | 21.5 | 0.0 | 9.9 | 13.97 | 17.86 | Au1rxx-base64 | 192.255.128.123 |
| 79.74 | vless | 280.5 | 717.2 | 21.29 | 0.0 | 9.97 | 10.62 | 17.86 | Au1rxx-base64 | 79.141.172.154 |
| 79.72 | hysteria2 | 330.4 | 827.7 | 20.13 | 0.0 | 10.0 | 13.97 | 17.72 | mheidari-all | 159.223.157.129 |
| 79.61 | vless | 284.5 | 670.9 | 21.19 | 0.0 | 9.94 | 10.62 | 17.86 | Au1rxx-base64 | 198.251.78.29 |
| 78.72 | shadowsocks | 243.9 | 593.7 | 22.13 | 0.0 | 9.94 | 12.79 | 17.86 | Au1rxx-base64 | 156.146.38.169 |
| 75.94 | vless | 338.4 | 760.3 | 19.95 | 0.0 | 10.0 | 10.62 | 17.86 | Au1rxx-base64 | 66.70.179.198 |
| 75.62 | vless | 279.7 | 552.3 | 21.3 | 0.0 | 10.0 | 10.62 | 17.72 | mheidari-all | 47.251.108.158 |
| 75.56 | vless | 298.1 | 667.4 | 20.88 | 0.0 | 10.0 | 10.62 | 17.86 | Au1rxx-base64 | 195.123.235.177 |
| 75.49 | shadowsocks | 315.3 | 751.1 | 20.48 | 0.0 | 9.93 | 12.79 | 17.86 | Au1rxx-base64 | 37.19.198.160 |
| 75.23 | shadowsocks | 334.2 | 854.9 | 20.04 | 0.0 | 9.04 | 12.79 | 17.86 | Au1rxx-base64 | yyz-ca-01.blncvpn4u.cc |
| 75.18 | shadowsocks | 307.5 | 757.3 | 20.66 | 0.0 | 9.94 | 12.79 | 17.86 | Au1rxx-base64 | 37.19.198.236 |
| 75.11 | shadowsocks | 248.6 | 642.9 | 22.02 | 0.0 | 10.0 | 12.79 | 17.86 | Au1rxx-base64 | 156.146.38.167 |
| 75.1 | vless | 332.1 | 774.7 | 20.09 | 0.0 | 9.95 | 10.62 | 17.86 | Au1rxx-base64 | 169.40.42.232 |
| 75.07 | vless | 403.5 | 971.5 | 18.44 | 0.0 | 9.98 | 10.62 | 17.86 | Au1rxx-base64 | 185.95.231.156 |
| 74.9 | vless | 299.1 | 610.9 | 20.85 | 0.0 | 9.93 | 10.62 | 17.86 | Au1rxx-base64 | 172.235.43.210 |
| 74.68 | hysteria2 | 325.5 | 342.2 | 20.24 | 2.17 | 8.41 | 13.97 | 17.86 | Au1rxx-base64 | open.2ml.bid |
| 74.64 | vless | 300.7 | 599.2 | 20.82 | 0.0 | 9.96 | 10.62 | 17.86 | Au1rxx-base64 | 172.233.139.46 |
| 74.57 | hysteria2 | 482.7 | 771.1 | 16.6 | 0.0 | 9.94 | 13.97 | 17.86 | Au1rxx-base64 | 66.94.121.46 |
| 74.56 | vless | 293.1 | 604.5 | 20.99 | 0.0 | 10.0 | 10.62 | 17.86 | Au1rxx-base64 | 192.3.247.109 |
| 74.4 | vless | 382.8 | 922.1 | 18.92 | 0.0 | 9.98 | 10.62 | 17.86 | Au1rxx-base64 | 169.40.42.224 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Surfboard-tg-mixed | 0.98 | 0.929 | 28 | 7082 | prefer |
| mheidari-all | 0.916 | 0.842 | 114 | 22763 | prefer |
| Au1rxx-base64 | 0.882 | 0.812 | 304 | 1792 | prefer |
| ermaozi | 0.86 | 0.871 | 31 | 291 | prefer |
| tg-oneclickvpnkeys | 0.36 | 1.0 | 3 | 62 | observe |
| DeltaKronecker-all | 0.335 | 1.0 | 1 | 5528 | observe |
| ermaozi-get_subscribe | 0.323 | 1.0 | 2 | 293 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5314 | observe |
| Epodonios-all | 0.255 | None | 0 | 7556 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9172 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5695 | observe |
| barry-far-vless | 0.255 | None | 0 | 5942 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4338 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 30 |
| cn-block | TimeoutError | - | 18 |
| 204 | ProxyError | - | 8 |
| speed | TimeoutError | - | 7 |
| geo | TimeoutError | - | 6 |
| 204 | TimeoutError | - | 5 |
| cn-block | ClientOSError | - | 4 |
| 204 | ClientOSError | - | 2 |
| cn-block | ProxyError | - | 1 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
