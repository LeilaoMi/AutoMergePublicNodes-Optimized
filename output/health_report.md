# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-07 04:03:14 |
| 运行耗时 | 372.8s |
| 订阅源总数 | 107 |
| 健康订阅源 | 96 |
| 原始节点 | 94333 |
| 去重后节点 | 24798 |
| TCP 可达 | 3000 |
| 真实可用 | 609 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 24798 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.9 |
| geo | 1.5 |
| tcp | 42.0 |
| probe | 95.2 |
| real_test | 182.9 |
| generate | 44.3 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 58832 |
| vmess | 12750 |
| shadowsocks | 11271 |
| trojan | 9045 |
| hysteria2 | 2051 |
| http | 137 |
| shadowsocksr | 123 |
| socks | 60 |
| anytls | 29 |
| hysteria | 19 |
| tuic | 16 |

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
| 79.53 | hysteria2 | 231.7 | 530.3 | 22.42 | 0.0 | 9.13 | 13.7 | 19.5 | Au1rxx-base64 | 66.94.121.46 |
| 78.22 | vless | 273.7 | 570.4 | 21.44 | 0.0 | 9.17 | 10.52 | 19.5 | Au1rxx-base64 | 172.233.139.46 |
| 77.68 | vless | 280.4 | 578.7 | 21.29 | 0.0 | 9.2 | 10.52 | 19.5 | Au1rxx-base64 | 38.150.33.232 |
| 77.58 | vless | 350.2 | 848.9 | 19.67 | 0.0 | 9.4 | 10.52 | 19.5 | Au1rxx-base64 | 15.204.97.216 |
| 77.37 | vless | 270.8 | 565.7 | 21.51 | 0.0 | 9.31 | 10.52 | 19.5 | Au1rxx-base64 | 172.235.43.210 |
| 76.11 | trojan | 370.3 | 966.7 | 19.21 | 0.0 | 9.26 | 11.14 | 19.5 | Au1rxx-base64 | 64.94.95.117 |
| 75.48 | vless | 271.6 | 623.9 | 21.49 | 0.0 | 9.39 | 10.52 | 19.5 | Au1rxx-base64 | 38.180.242.205 |
| 75.3 | vless | 367.1 | 736.6 | 19.28 | 0.0 | 9.16 | 10.52 | 19.5 | Au1rxx-base64 | 216.167.94.71 |
| 74.63 | trojan | 434.1 | 1139.1 | 17.73 | 0.0 | 9.26 | 11.14 | 19.5 | Au1rxx-base64 | 64.94.95.115 |
| 74.56 | shadowsocks | 239.5 | 615.6 | 22.23 | 0.0 | 9.37 | 13.51 | 19.5 | Au1rxx-base64 | 156.146.38.169 |
| 74.19 | shadowsocks | 307.6 | 637.9 | 20.66 | 0.0 | 9.24 | 13.51 | 19.5 | Au1rxx-base64 | 149.22.95.183 |
| 73.8 | http | 518.8 | 1118.0 | 15.77 | 0.0 | 10.0 | 14.38 | 19.2 | zhangkai | 138.199.35.216 |
| 73.71 | vless | 283.1 | 566.7 | 21.23 | 0.0 | 9.2 | 10.52 | 19.5 | Au1rxx-base64 | 172.235.38.85 |
| 73.68 | vless | 293.2 | 325.0 | 20.99 | 2.81 | 9.66 | 10.52 | 16.52 | Surfboard-tg-mixed | 31.76.91.72 |
| 73.38 | vless | 411.6 | 948.3 | 18.25 | 0.0 | 9.33 | 10.52 | 19.5 | Au1rxx-base64 | 216.152.147.28 |
| 73.37 | vless | 414.8 | 1021.4 | 18.18 | 0.0 | 9.21 | 10.52 | 19.5 | Au1rxx-base64 | 45.138.100.226 |
| 73.25 | vless | 386.5 | 826.2 | 18.83 | 0.0 | 9.22 | 10.52 | 19.5 | Au1rxx-base64 | 66.70.179.198 |
| 73.06 | vless | 377.6 | 749.0 | 19.04 | 0.0 | 9.32 | 10.52 | 19.5 | Au1rxx-base64 | 169.40.42.231 |
| 72.74 | shadowsocks | 316.8 | 664.5 | 20.44 | 0.0 | 10.0 | 13.51 | 16.52 | Surfboard-tg-mixed | 173.244.56.6 |
| 72.61 | vless | 317.0 | 619.6 | 20.44 | 0.0 | 10.0 | 10.52 | 19.5 | Au1rxx-base64 | 38.244.20.160 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.992 | 0.921 | 328 | 1835 | prefer |
| zhangkai | 0.813 | 0.833 | 24 | 144 | prefer |
| Surfboard-tg-mixed | 0.782 | 0.704 | 216 | 7284 | prefer |
| mheidari-all | 0.405 | 0.324 | 395 | 21249 | observe |
| xiaoji235-airport-v2ray-all | 0.391 | 1.0 | 2 | 5750 | observe |
| 10ium-ScrapeCategorize-Vless | 0.335 | 1.0 | 1 | 4791 | observe |
| tg-oneclickvpnkeys | 0.316 | 1.0 | 2 | 121 | observe |
| tg-LonUp_M | 0.262 | 1.0 | 1 | 177 | observe |
| Epodonios-all | 0.255 | None | 0 | 7766 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3996 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 8622 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 6082 | observe |
| barry-far-vless | 0.255 | None | 0 | 6301 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4138 | observe |
| Au1rxx-clash | 0.248 | None | 0 | 1835 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 113 |
| geo | ClientOSError | - | 72 |
| speed | TimeoutError | - | 62 |
| 204 | TimeoutError | - | 34 |
| speed | ClientOSError | - | 27 |
| cn-block | ClientOSError | - | 27 |
| cn-block | TimeoutError | - | 21 |
| 204 | ProxyConnectionError | - | 11 |
| 204 | ProxyError | - | 4 |
| cn-block | ProxyError | - | 2 |
| 204 | ServerDisconnectedError | - | 1 |
| geo | ProxyError | - | 1 |
| 204 | ClientOSError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
