# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-11 20:55:29 |
| 运行耗时 | 554.0s |
| 订阅源总数 | 107 |
| 健康订阅源 | 94 |
| 原始节点 | 83905 |
| 去重后节点 | 23390 |
| TCP 可达 | 3000 |
| 真实可用 | 445 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23390 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.3 |
| geo | 1.4 |
| tcp | 40.3 |
| probe | 209.4 |
| real_test | 215.9 |
| generate | 80.6 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 51162 |
| vmess | 12565 |
| shadowsocks | 9764 |
| trojan | 8006 |
| hysteria2 | 1608 |
| http | 599 |
| shadowsocksr | 125 |
| socks | 53 |
| tuic | 12 |
| hysteria | 9 |
| anytls | 2 |

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
| 81.53 | hysteria2 | 266.5 | 677.8 | 21.61 | 0.0 | 10.0 | 13.12 | 17.9 | Au1rxx-base64 | 159.223.157.129 |
| 78.6 | vless | 287.8 | 725.2 | 21.12 | 0.0 | 10.0 | 9.58 | 17.9 | Au1rxx-base64 | 47.253.226.114 |
| 78.02 | shadowsocks | 276.0 | 649.9 | 21.39 | 0.0 | 10.0 | 13.58 | 17.9 | Au1rxx-base64 | 51.222.12.127 |
| 77.87 | shadowsocks | 319.3 | 800.5 | 20.39 | 0.0 | 10.0 | 13.58 | 17.9 | Au1rxx-base64 | 37.19.198.243 |
| 77.81 | shadowsocks | 300.2 | 772.9 | 20.83 | 0.0 | 10.0 | 13.58 | 17.9 | Au1rxx-base64 | 15.204.247.206 |
| 77.71 | vless | 276.0 | 645.2 | 21.39 | 0.0 | 10.0 | 9.58 | 17.9 | Au1rxx-base64 | 195.123.235.177 |
| 77.42 | vless | 338.7 | 893.8 | 19.94 | 0.0 | 10.0 | 9.58 | 17.9 | Au1rxx-base64 | 216.152.147.28 |
| 77.0 | shadowsocks | 325.1 | 808.4 | 20.25 | 0.0 | 9.51 | 13.58 | 17.9 | Au1rxx-base64 | ca225.vpnbook.com |
| 76.99 | vless | 267.2 | 700.3 | 21.59 | 0.0 | 10.0 | 9.58 | 17.9 | Au1rxx-base64 | 79.141.172.154 |
| 76.44 | hysteria2 | 298.4 | 610.2 | 20.87 | 0.0 | 10.0 | 13.12 | 17.9 | Au1rxx-base64 | 66.94.121.46 |
| 76.12 | shadowsocks | 250.5 | 617.3 | 21.98 | 0.0 | 10.0 | 13.58 | 14.56 | Surfboard-tg-mixed | 198.98.53.130 |
| 75.97 | shadowsocks | 257.1 | 625.0 | 21.83 | 0.0 | 10.0 | 13.58 | 14.56 | Surfboard-tg-mixed | 156.146.38.167 |
| 75.91 | vless | 386.5 | 862.3 | 18.83 | 0.0 | 10.0 | 9.58 | 17.9 | Au1rxx-base64 | 169.40.42.202 |
| 75.9 | vless | 292.7 | 690.9 | 21.0 | 0.0 | 10.0 | 9.58 | 17.9 | Au1rxx-base64 | 169.40.42.179 |
| 75.72 | vless | 340.5 | 791.4 | 19.9 | 0.0 | 10.0 | 9.58 | 17.9 | Au1rxx-base64 | 169.40.42.224 |
| 75.57 | shadowsocks | 256.0 | 625.4 | 21.85 | 0.0 | 10.0 | 13.58 | 14.14 | mheidari-all | 156.146.38.169 |
| 75.46 | shadowsocks | 357.0 | 872.7 | 19.51 | 0.0 | 10.0 | 13.58 | 17.9 | Au1rxx-base64 | 38.180.135.156 |
| 75.4 | shadowsocks | 259.9 | 639.8 | 21.76 | 0.0 | 10.0 | 13.58 | 14.14 | mheidari-all | 156.146.38.170 |
| 75.02 | shadowsocks | 279.8 | 696.8 | 21.3 | 0.0 | 10.0 | 13.58 | 14.14 | mheidari-all | 37.19.198.160 |
| 74.93 | vless | 338.1 | 610.4 | 19.95 | 0.0 | 10.0 | 9.58 | 17.9 | Au1rxx-base64 | 169.40.42.225 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.942 | 0.88 | 275 | 1630 | prefer |
| mheidari-all | 0.775 | 0.699 | 93 | 15494 | prefer |
| ermaozi | 0.748 | 0.75 | 28 | 377 | prefer |
| Surfboard-tg-mixed | 0.673 | 0.595 | 148 | 7355 | observe |
| DeltaKronecker-all | 0.658 | 0.581 | 43 | 6070 | observe |
| tg-oneclickvpnkeys | 0.319 | 1.0 | 2 | 194 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4932 | observe |
| Epodonios-all | 0.255 | None | 0 | 7810 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9022 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5993 | observe |
| barry-far-vless | 0.255 | None | 0 | 6209 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4223 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | ClientOSError | - | 58 |
| cn-block | TimeoutError | - | 21 |
| 204 | TimeoutError | - | 20 |
| 204 | ProxyError | - | 15 |
| speed | ClientOSError | - | 12 |
| cn-block | ClientOSError | - | 11 |
| cn-block | ProxyError | - | 5 |
| speed | TimeoutError | - | 4 |
| 204 | ServerDisconnectedError | - | 2 |
| 204 | ClientOSError | - | 2 |
| geo | TimeoutError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
