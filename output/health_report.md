# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-14 03:43:42 |
| 运行耗时 | 974.1s |
| 订阅源总数 | 107 |
| 健康订阅源 | 93 |
| 原始节点 | 98590 |
| 去重后节点 | 27432 |
| TCP 可达 | 3000 |
| 真实可用 | 55 |
| Verified 输出 | 55 |
| Global 输出 | 70 |
| All 输出 | 27432 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.3 |
| geo | 1.5 |
| tcp | 96.3 |
| probe | 322.3 |
| real_test | 443.3 |
| generate | 104.5 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 58028 |
| vmess | 16108 |
| shadowsocks | 11886 |
| trojan | 10483 |
| hysteria2 | 1310 |
| http | 485 |
| shadowsocksr | 171 |
| socks | 70 |
| anytls | 25 |
| hysteria | 18 |
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
| 82.49 | vless | 321.2 | 698.3 | 20.34 | 0.0 | 9.73 | 12.9 | 19.52 | Au1rxx-base64 | 147.45.60.160 |
| 81.08 | hysteria2 | 312.0 | 689.3 | 20.56 | 0.0 | 10.0 | 12.5 | 19.52 | Au1rxx-base64 | 129.213.91.185 |
| 80.68 | shadowsocks | 244.8 | 601.9 | 22.11 | 0.0 | 10.0 | 13.05 | 19.52 | Au1rxx-base64 | 156.146.38.170 |
| 80.13 | vless | 324.4 | 720.0 | 20.27 | 0.0 | 9.52 | 12.9 | 19.52 | Au1rxx-base64 | 159.89.87.21 |
| 79.12 | hysteria2 | 307.7 | 687.5 | 20.66 | 0.0 | 9.38 | 12.5 | 19.52 | Au1rxx-base64 | 66.94.121.46 |
| 78.39 | vless | 329.0 | 762.5 | 20.16 | 0.0 | 8.51 | 12.9 | 19.52 | Au1rxx-base64 | 169.40.42.90 |
| 78.19 | vless | 355.6 | 767.7 | 19.55 | 0.0 | 8.54 | 12.9 | 19.52 | Au1rxx-base64 | 167.17.69.171 |
| 77.51 | vless | 333.9 | 761.7 | 20.05 | 0.0 | 8.93 | 12.9 | 19.52 | Au1rxx-base64 | 66.70.179.198 |
| 77.28 | vless | 383.9 | 924.1 | 18.89 | 0.0 | 8.94 | 12.9 | 19.52 | Au1rxx-base64 | 137.184.218.169 |
| 77.05 | vless | 315.2 | 599.9 | 20.48 | 0.0 | 8.17 | 12.9 | 19.52 | Au1rxx-base64 | 144.202.126.147 |
| 76.81 | vless | 315.5 | 634.0 | 20.47 | 0.0 | 8.45 | 12.9 | 19.52 | Au1rxx-base64 | 195.123.240.65 |
| 76.64 | vless | 335.4 | 811.8 | 20.01 | 0.0 | 8.71 | 12.9 | 19.52 | Au1rxx-base64 | 69.48.201.136 |
| 76.56 | shadowsocks | 370.7 | 941.5 | 19.2 | 0.0 | 10.0 | 13.05 | 19.52 | Au1rxx-base64 | 37.19.198.160 |
| 76.51 | vless | 305.3 | 602.2 | 20.71 | 0.0 | 8.19 | 12.9 | 19.52 | Au1rxx-base64 | 45.32.69.110 |
| 76.14 | vless | 424.2 | 1054.5 | 17.96 | 0.0 | 8.98 | 12.9 | 19.52 | Au1rxx-base64 | 185.95.231.156 |
| 75.97 | vless | 331.1 | 851.0 | 20.11 | 0.0 | 8.44 | 12.9 | 19.52 | Au1rxx-base64 | 38.180.137.143 |
| 75.91 | vless | 414.0 | 998.9 | 18.19 | 0.0 | 8.23 | 12.9 | 19.52 | Au1rxx-base64 | 169.40.42.182 |
| 75.83 | vless | 442.4 | 1092.5 | 17.54 | 0.0 | 9.48 | 12.9 | 19.52 | Au1rxx-base64 | 169.40.42.173 |
| 75.8 | vless | 352.1 | 706.1 | 19.63 | 0.0 | 8.35 | 12.9 | 19.52 | Au1rxx-base64 | 169.40.42.16 |
| 75.56 | vless | 412.9 | 932.6 | 18.22 | 0.0 | 8.8 | 12.9 | 19.52 | Au1rxx-base64 | 169.40.42.179 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Surfboard-tg-mixed | 1.0 | 0.944 | 72 | 7113 | prefer |
| Au1rxx-base64 | 0.961 | 0.893 | 345 | 1771 | prefer |
| ermaozi-get_subscribe | 0.468 | 0.443 | 61 | 598 | observe |
| mheidari-all | 0.461 | 0.38 | 300 | 24076 | observe |
| zhangkai | 0.261 | 1.0 | 1 | 144 | observe |
| DeltaKronecker-all | 0.255 | None | 0 | 5076 | observe |
| Epodonios-all | 0.255 | None | 0 | 7613 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9824 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5621 | observe |
| barry-far-vless | 0.255 | None | 0 | 5866 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4216 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.246 | None | 0 | 1771 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 110 |
| 204 | ProxyError | - | 41 |
| geo | ClientOSError | - | 36 |
| speed | ClientOSError | - | 33 |
| speed | TimeoutError | - | 15 |
| cn-block | TimeoutError | - | 10 |
| 204 | TimeoutError | - | 8 |
| cn-block | ClientOSError | - | 7 |
| 204 | ClientOSError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 55 | - |
| global | False | 300 | 70 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
