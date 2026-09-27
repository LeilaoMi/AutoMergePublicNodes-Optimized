# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-27 04:57:38 |
| 运行耗时 | 807.6s |
| 订阅源总数 | 107 |
| 健康订阅源 | 93 |
| 原始节点 | 95804 |
| 去重后节点 | 26625 |
| TCP 可达 | 3000 |
| 真实可用 | 496 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 26625 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.3 |
| geo | 1.6 |
| tcp | 44.0 |
| probe | 281.0 |
| real_test | 377.5 |
| generate | 96.3 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 58211 |
| vmess | 14886 |
| shadowsocks | 11304 |
| trojan | 8999 |
| hysteria2 | 1433 |
| http | 677 |
| shadowsocksr | 167 |
| socks | 79 |
| anytls | 26 |
| hysteria | 15 |
| tuic | 7 |

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
| 78.96 | vless | 279.2 | 640.1 | 21.32 | 0.0 | 10.0 | 10.04 | 19.02 | Au1rxx-base64 | 5.78.159.214 |
| 78.87 | vless | 337.4 | 692.4 | 19.97 | 0.0 | 10.0 | 10.04 | 19.02 | Au1rxx-base64 | 79.141.172.154 |
| 78.14 | vless | 272.4 | 600.1 | 21.47 | 0.0 | 10.0 | 10.04 | 19.02 | Au1rxx-base64 | 15.204.97.216 |
| 77.27 | vless | 288.8 | 643.3 | 21.09 | 0.0 | 10.0 | 10.04 | 19.02 | Au1rxx-base64 | 38.244.20.25 |
| 77.22 | vless | 272.1 | 566.1 | 21.48 | 0.0 | 10.0 | 10.04 | 19.02 | Au1rxx-base64 | 172.235.43.210 |
| 76.95 | vless | 282.1 | 574.8 | 21.25 | 0.0 | 10.0 | 10.04 | 19.02 | Au1rxx-base64 | 195.123.240.65 |
| 76.81 | shadowsocks | 283.6 | 586.5 | 21.21 | 0.0 | 10.0 | 13.12 | 16.48 | Surfboard-tg-mixed | 156.146.38.167 |
| 76.7 | vless | 315.0 | 700.3 | 20.49 | 0.0 | 10.0 | 10.04 | 19.02 | Au1rxx-base64 | 198.251.78.29 |
| 75.62 | hysteria2 | 316.2 | 763.9 | 20.46 | 0.0 | 10.0 | 13.75 | 19.02 | Au1rxx-base64 | 192.255.128.123 |
| 74.87 | shadowsocks | 321.4 | 746.0 | 20.34 | 0.0 | 9.9 | 13.12 | 19.02 | Au1rxx-base64 | yyz-ca-01.blncvpn4u.cc |
| 74.45 | shadowsocks | 311.7 | 764.1 | 20.56 | 0.0 | 10.0 | 13.12 | 16.48 | Surfboard-tg-mixed | 5.78.51.123 |
| 73.88 | vless | 371.7 | 824.4 | 19.17 | 0.0 | 10.0 | 10.04 | 19.02 | Au1rxx-base64 | 38.77.133.202 |
| 73.56 | shadowsocks | 373.0 | 871.6 | 19.14 | 0.0 | 10.0 | 13.12 | 19.02 | Au1rxx-base64 | 142.4.216.225 |
| 73.49 | shadowsocks | 258.4 | 529.4 | 21.8 | 0.0 | 10.0 | 13.12 | 16.48 | Surfboard-tg-mixed | 108.181.0.177 |
| 73.42 | vless | 376.6 | 773.9 | 19.06 | 0.0 | 10.0 | 10.04 | 19.02 | Au1rxx-base64 | 66.70.179.198 |
| 73.22 | shadowsocks | 399.2 | 872.7 | 18.54 | 0.0 | 10.0 | 13.12 | 19.02 | Au1rxx-base64 | 185.156.47.97 |
| 73.13 | shadowsocks | 299.0 | 656.6 | 20.86 | 0.0 | 10.0 | 13.12 | 16.48 | Surfboard-tg-mixed | 198.98.53.130 |
| 72.86 | shadowsocks | 280.7 | 583.3 | 21.28 | 0.0 | 10.0 | 13.12 | 16.48 | Surfboard-tg-mixed | 173.244.56.6 |
| 72.53 | vless | 389.3 | 748.5 | 18.77 | 0.0 | 10.0 | 10.04 | 19.02 | Au1rxx-base64 | 169.40.42.225 |
| 72.46 | vless | 323.6 | 721.1 | 20.29 | 0.0 | 10.0 | 10.04 | 19.02 | Au1rxx-base64 | 23.191.200.207 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.926 | 0.867 | 279 | 1536 | prefer |
| Surfboard-tg-mixed | 0.801 | 0.723 | 195 | 7113 | prefer |
| ermaozi | 0.585 | 0.576 | 33 | 338 | observe |
| mheidari-all | 0.361 | 0.279 | 308 | 22408 | observe |
| ermaozi-get_subscribe | 0.335 | 0.571 | 7 | 361 | observe |
| xiaoji235-airport-v2ray-all | 0.335 | 1.0 | 1 | 6752 | observe |
| roosterkid-openproxylist-v2ray | 0.261 | 1.0 | 1 | 149 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5242 | observe |
| Epodonios-all | 0.255 | None | 0 | 7583 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3996 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 8902 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5686 | observe |
| barry-far-vless | 0.255 | None | 0 | 5907 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4355 | observe |
| DeltaKronecker-all | 0.243 | 0.182 | 11 | 5512 | downweight |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 133 |
| speed | TimeoutError | - | 61 |
| geo | ClientOSError | - | 41 |
| cn-block | ClientOSError | - | 21 |
| 204 | ProxyError | - | 20 |
| speed | ClientOSError | - | 17 |
| cn-block | TimeoutError | - | 16 |
| 204 | ProxyConnectionError | - | 14 |
| 204 | TimeoutError | - | 14 |
| 204 | ClientOSError | - | 4 |
| cn-block | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
