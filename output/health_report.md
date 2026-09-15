# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-15 04:38:49 |
| 运行耗时 | 1090.2s |
| 订阅源总数 | 107 |
| 健康订阅源 | 95 |
| 原始节点 | 90171 |
| 去重后节点 | 25748 |
| TCP 可达 | 3000 |
| 真实可用 | 510 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 25748 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.1 |
| geo | 1.5 |
| tcp | 41.0 |
| probe | 372.1 |
| real_test | 583.8 |
| generate | 84.8 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 55825 |
| vmess | 13250 |
| shadowsocks | 10080 |
| trojan | 8399 |
| hysteria2 | 1762 |
| http | 646 |
| shadowsocksr | 124 |
| socks | 53 |
| hysteria | 14 |
| tuic | 10 |
| anytls | 8 |

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
| 85.09 | hysteria2 | 180.2 | 487.2 | 23.61 | 0.0 | 9.12 | 13.5 | 19.86 | Au1rxx-base64 | 107.175.219.48 |
| 82.43 | vless | 205.3 | 523.9 | 23.02 | 0.0 | 9.26 | 10.29 | 19.86 | Au1rxx-base64 | 172.235.43.210 |
| 80.95 | vless | 267.2 | 694.3 | 21.59 | 0.0 | 9.21 | 10.29 | 19.86 | Au1rxx-base64 | 45.149.172.80 |
| 80.42 | vless | 200.4 | 519.3 | 23.14 | 0.0 | 9.13 | 10.29 | 19.86 | Au1rxx-base64 | 192.3.247.109 |
| 79.81 | vless | 315.9 | 836.9 | 20.47 | 0.0 | 9.19 | 10.29 | 19.86 | Au1rxx-base64 | 15.204.97.216 |
| 78.59 | vless | 209.0 | 466.2 | 22.94 | 0.0 | 10.0 | 10.29 | 19.86 | Au1rxx-base64 | 188.114.97.6 |
| 78.36 | vless | 292.3 | 797.1 | 21.01 | 0.0 | 9.2 | 10.29 | 19.86 | Au1rxx-base64 | 45.149.172.74 |
| 78.17 | vless | 261.9 | 730.4 | 21.72 | 0.0 | 9.3 | 10.29 | 19.86 | Au1rxx-base64 | 198.200.42.129 |
| 77.8 | vless | 193.1 | 501.5 | 23.31 | 0.0 | 9.34 | 10.29 | 19.86 | Au1rxx-base64 | 31.58.50.200 |
| 77.47 | vless | 224.8 | 505.2 | 22.57 | 0.0 | 9.25 | 10.29 | 19.86 | Au1rxx-base64 | 162.159.45.19 |
| 76.71 | shadowsocks | 205.6 | 518.1 | 23.02 | 0.0 | 10.0 | 13.77 | 14.42 | Surfboard-tg-mixed | 5.78.51.123 |
| 76.54 | shadowsocks | 293.2 | 656.3 | 20.99 | 0.0 | 9.28 | 13.77 | 19.86 | Au1rxx-base64 | 156.146.38.168 |
| 76.04 | vless | 266.7 | 430.6 | 21.61 | 0.0 | 9.25 | 10.29 | 19.86 | Au1rxx-base64 | 108.162.198.178 |
| 75.79 | vless | 343.3 | 750.8 | 19.83 | 0.0 | 9.15 | 10.29 | 19.86 | Au1rxx-base64 | 79.141.172.154 |
| 75.61 | shadowsocks | 253.0 | 592.5 | 21.92 | 0.0 | 10.0 | 13.77 | 14.42 | Surfboard-tg-mixed | 108.181.0.177 |
| 75.4 | vless | 506.4 | 1356.5 | 16.06 | 0.0 | 9.19 | 10.29 | 19.86 | Au1rxx-base64 | 51.81.203.63 |
| 75.26 | vless | 174.9 | 474.5 | 23.73 | 0.0 | 10.0 | 10.29 | 12.24 | mheidari-all | 47.251.108.158 |
| 75.1 | hysteria2 | 198.6 | 516.6 | 23.18 | 0.0 | 10.0 | 13.5 | 14.42 | Surfboard-tg-mixed | 45.149.172.74 |
| 75.02 | hysteria2 | 202.1 | 510.3 | 23.1 | 0.0 | 10.0 | 13.5 | 14.42 | Surfboard-tg-mixed | 45.149.172.80 |
| 75.0 | trojan | 200.5 | 530.6 | 23.14 | 0.0 | 9.25 | 5.25 | 19.86 | Au1rxx-base64 | 100.42.228.109 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.879 | 0.818 | 286 | 1584 | prefer |
| Surfboard-tg-mixed | 0.767 | 0.689 | 164 | 7572 | prefer |
| ermaozi | 0.531 | 0.514 | 35 | 425 | observe |
| ermaozi-get_subscribe | 0.384 | 0.625 | 8 | 447 | observe |
| DeltaKronecker-all | 0.322 | 0.25 | 16 | 5972 | observe |
| mheidari-all | 0.309 | 0.228 | 588 | 21540 | observe |
| roosterkid-openproxylist-v2ray | 0.261 | 1.0 | 1 | 150 | observe |
| tg-oneclickvpnkeys | 0.26 | 1.0 | 1 | 120 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4914 | observe |
| Epodonios-all | 0.255 | None | 0 | 8044 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 8754 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 6105 | observe |
| barry-far-vless | 0.255 | None | 0 | 6333 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4099 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 204 |
| geo | ClientOSError | - | 99 |
| speed | TimeoutError | - | 96 |
| cn-block | ClientOSError | - | 65 |
| speed | ClientOSError | - | 59 |
| cn-block | TimeoutError | - | 28 |
| 204 | ProxyError | - | 25 |
| 204 | TimeoutError | - | 12 |
| cn-block | ProxyError | - | 2 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
