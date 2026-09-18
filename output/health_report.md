# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-18 04:23:27 |
| 运行耗时 | 979.5s |
| 订阅源总数 | 107 |
| 健康订阅源 | 95 |
| 原始节点 | 84088 |
| 去重后节点 | 23179 |
| TCP 可达 | 3000 |
| 真实可用 | 607 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23179 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.6 |
| geo | 1.5 |
| tcp | 39.1 |
| probe | 354.4 |
| real_test | 544.8 |
| generate | 33.1 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 50378 |
| vmess | 13169 |
| shadowsocks | 10189 |
| trojan | 8181 |
| hysteria2 | 1294 |
| http | 662 |
| shadowsocksr | 130 |
| socks | 71 |
| hysteria | 8 |
| anytls | 4 |
| tuic | 2 |

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
| 83.49 | hysteria2 | 279.4 | 684.3 | 21.31 | 0.0 | 10.0 | 13.5 | 19.78 | mheidari-all | 159.223.157.129 |
| 83.21 | vless | 291.8 | 690.8 | 21.02 | 0.0 | 10.0 | 12.73 | 19.72 | Au1rxx-base64 | 198.251.78.29 |
| 82.77 | vless | 309.4 | 704.1 | 20.62 | 0.0 | 10.0 | 12.73 | 19.72 | Au1rxx-base64 | 216.152.147.28 |
| 82.74 | hysteria2 | 249.3 | 554.2 | 22.01 | 0.0 | 10.0 | 13.5 | 19.72 | Au1rxx-base64 | 66.94.121.46 |
| 81.97 | vless | 354.6 | 878.9 | 19.57 | 0.0 | 10.0 | 12.73 | 19.72 | Au1rxx-base64 | 38.180.242.205 |
| 81.55 | shadowsocks | 241.6 | 578.2 | 22.18 | 0.0 | 10.0 | 13.7 | 19.78 | mheidari-all | 156.146.38.168 |
| 81.37 | shadowsocks | 254.5 | 632.5 | 21.89 | 0.0 | 10.0 | 13.7 | 19.78 | mheidari-all | 156.146.38.170 |
| 80.02 | shadowsocks | 290.9 | 788.0 | 21.04 | 0.0 | 10.0 | 13.7 | 19.72 | Au1rxx-base64 | 156.146.38.167 |
| 79.58 | shadowsocks | 242.6 | 619.8 | 22.16 | 0.0 | 10.0 | 13.7 | 17.72 | Surfboard-tg-mixed | 156.146.38.169 |
| 79.02 | vless | 316.4 | 759.9 | 20.45 | 0.0 | 10.0 | 12.73 | 19.72 | Au1rxx-base64 | 47.253.226.114 |
| 78.72 | vless | 353.5 | 697.8 | 19.6 | 0.0 | 10.0 | 12.73 | 19.72 | Au1rxx-base64 | 169.40.42.90 |
| 78.67 | vless | 336.9 | 783.9 | 19.98 | 0.0 | 10.0 | 12.73 | 19.72 | Au1rxx-base64 | 169.40.42.89 |
| 78.62 | vless | 382.4 | 903.9 | 18.93 | 0.0 | 10.0 | 12.73 | 19.72 | Au1rxx-base64 | 137.184.218.169 |
| 78.35 | vless | 385.3 | 907.8 | 18.86 | 0.0 | 10.0 | 12.73 | 19.72 | Au1rxx-base64 | 169.40.42.15 |
| 78.21 | vless | 396.5 | 885.9 | 18.6 | 0.0 | 10.0 | 12.73 | 19.72 | Au1rxx-base64 | 169.40.42.95 |
| 78.13 | shadowsocks | 293.8 | 706.7 | 20.98 | 0.0 | 10.0 | 13.7 | 19.72 | Au1rxx-base64 | 37.19.198.243 |
| 77.49 | vless | 420.3 | 1020.0 | 18.05 | 0.0 | 10.0 | 12.73 | 19.72 | Au1rxx-base64 | 185.95.231.156 |
| 77.21 | vless | 349.5 | 820.6 | 19.69 | 0.0 | 10.0 | 12.73 | 19.72 | Au1rxx-base64 | 66.70.179.198 |
| 77.08 | vless | 393.2 | 840.9 | 18.68 | 0.0 | 10.0 | 12.73 | 19.72 | Au1rxx-base64 | 169.40.42.224 |
| 76.98 | vless | 317.1 | 710.8 | 20.44 | 0.0 | 10.0 | 12.73 | 19.72 | Au1rxx-base64 | 169.40.42.231 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.947 | 0.885 | 286 | 1618 | prefer |
| Surfboard-tg-mixed | 0.834 | 0.758 | 120 | 7282 | prefer |
| ermaozi | 0.765 | 0.769 | 26 | 378 | prefer |
| mheidari-all | 0.517 | 0.436 | 110 | 15863 | observe |
| DeltaKronecker-all | 0.455 | 0.374 | 513 | 5931 | observe |
| mahdibland-V2RayAggregator | 0.335 | 1.0 | 1 | 4261 | observe |
| ermaozi-get_subscribe | 0.285 | 0.667 | 3 | 402 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5093 | observe |
| Epodonios-all | 0.255 | None | 0 | 7966 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9011 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5769 | observe |
| barry-far-vless | 0.255 | None | 0 | 6180 | observe |
| Au1rxx-clash | 0.24 | None | 0 | 1618 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 211 |
| speed | ClientOSError | - | 78 |
| geo | ClientOSError | - | 68 |
| speed | TimeoutError | - | 53 |
| cn-block | TimeoutError | - | 18 |
| 204 | ProxyError | - | 13 |
| cn-block | ClientOSError | - | 7 |
| 204 | TimeoutError | - | 3 |
| 204 | ClientOSError | - | 2 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
