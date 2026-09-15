# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-15 16:50:29 |
| 运行耗时 | 601.1s |
| 订阅源总数 | 107 |
| 健康订阅源 | 95 |
| 原始节点 | 91321 |
| 去重后节点 | 25727 |
| TCP 可达 | 3000 |
| 真实可用 | 424 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 25727 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.0 |
| geo | 1.4 |
| tcp | 42.9 |
| probe | 261.7 |
| real_test | 212.7 |
| generate | 77.4 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 56339 |
| vmess | 13498 |
| shadowsocks | 10067 |
| trojan | 8806 |
| hysteria2 | 1774 |
| http | 624 |
| shadowsocksr | 131 |
| socks | 54 |
| hysteria | 14 |
| anytls | 8 |
| tuic | 6 |

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
| 80.98 | hysteria2 | 279.5 | 666.5 | 21.31 | 0.0 | 10.0 | 12.75 | 18.02 | mheidari-all | 159.223.157.129 |
| 79.99 | shadowsocks | 253.5 | 653.0 | 21.91 | 0.0 | 10.0 | 14.04 | 18.04 | Au1rxx-base64 | 156.146.38.168 |
| 79.64 | shadowsocks | 243.2 | 603.7 | 22.15 | 0.0 | 9.41 | 14.04 | 18.04 | Au1rxx-base64 | 156.146.38.170 |
| 78.51 | shadowsocks | 253.6 | 644.1 | 21.91 | 0.0 | 9.42 | 14.04 | 18.04 | Au1rxx-base64 | 156.146.38.169 |
| 78.48 | hysteria2 | 257.8 | 558.9 | 21.81 | 0.0 | 9.27 | 12.75 | 18.04 | Au1rxx-base64 | 66.94.121.46 |
| 77.88 | vless | 297.8 | 724.6 | 20.88 | 0.0 | 10.0 | 10.73 | 18.04 | Au1rxx-base64 | 79.141.172.154 |
| 75.71 | vless | 349.4 | 830.0 | 19.69 | 0.0 | 10.0 | 10.73 | 18.02 | mheidari-all | 67.220.73.204 |
| 75.65 | shadowsocks | 252.8 | 615.3 | 21.93 | 0.0 | 10.0 | 14.04 | 13.68 | Surfboard-tg-mixed | 156.146.38.167 |
| 75.61 | shadowsocks | 291.5 | 680.2 | 21.03 | 0.0 | 9.42 | 14.04 | 18.04 | Au1rxx-base64 | 38.180.135.156 |
| 75.47 | vless | 277.7 | 552.7 | 21.35 | 0.0 | 10.0 | 10.73 | 18.02 | mheidari-all | 47.251.108.158 |
| 75.42 | shadowsocks | 347.9 | 842.3 | 19.72 | 0.0 | 10.0 | 14.04 | 18.02 | mheidari-all | 37.19.198.243 |
| 75.12 | vless | 290.2 | 604.2 | 21.06 | 0.0 | 9.16 | 10.73 | 18.04 | Au1rxx-base64 | 192.3.247.109 |
| 74.85 | vless | 308.3 | 669.0 | 20.64 | 0.0 | 9.26 | 10.73 | 18.04 | Au1rxx-base64 | 195.123.235.177 |
| 74.52 | shadowsocks | 297.7 | 621.6 | 20.89 | 0.0 | 9.42 | 14.04 | 18.04 | Au1rxx-base64 | 173.244.56.6 |
| 74.49 | vless | 335.7 | 709.8 | 20.01 | 0.0 | 10.0 | 10.73 | 18.04 | Au1rxx-base64 | 169.40.42.74 |
| 74.3 | shadowsocks | 328.1 | 730.9 | 20.18 | 0.0 | 10.0 | 14.04 | 18.02 | mheidari-all | 108.181.57.93 |
| 74.23 | vless | 309.2 | 621.5 | 20.62 | 0.0 | 9.36 | 10.73 | 18.04 | Au1rxx-base64 | 172.235.43.210 |
| 74.17 | vless | 324.8 | 719.5 | 20.26 | 0.0 | 9.15 | 10.73 | 18.04 | Au1rxx-base64 | 137.184.218.169 |
| 74.14 | vless | 393.2 | 877.8 | 18.68 | 0.0 | 10.0 | 10.73 | 18.04 | Au1rxx-base64 | 169.40.42.75 |
| 73.91 | shadowsocks | 290.3 | 687.3 | 21.06 | 0.0 | 10.0 | 14.04 | 18.02 | mheidari-all | 37.19.198.244 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.928 | 0.869 | 312 | 1553 | prefer |
| Surfboard-tg-mixed | 0.783 | 0.708 | 72 | 7516 | prefer |
| ermaozi | 0.712 | 0.714 | 21 | 406 | prefer |
| mheidari-all | 0.538 | 0.458 | 177 | 21913 | observe |
| DeltaKronecker-all | 0.349 | 0.667 | 3 | 5932 | observe |
| ermaozi-get_subscribe | 0.328 | 1.0 | 2 | 422 | observe |
| tg-oneclickvpnkeys | 0.317 | 1.0 | 2 | 149 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5015 | observe |
| Epodonios-all | 0.255 | None | 0 | 8076 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9411 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 6065 | observe |
| barry-far-vless | 0.255 | None | 0 | 6401 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4258 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| cn-block | ClientOSError | - | 45 |
| 204 | TimeoutError | - | 33 |
| geo | ClientOSError | - | 32 |
| cn-block | TimeoutError | - | 15 |
| speed | ClientOSError | - | 13 |
| 204 | ProxyError | - | 12 |
| speed | TimeoutError | - | 6 |
| geo | TimeoutError | - | 5 |
| 204 | ClientOSError | - | 2 |
| cn-block | ProxyError | - | 1 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
