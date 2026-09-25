# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-25 17:05:07 |
| 运行耗时 | 506.5s |
| 订阅源总数 | 107 |
| 健康订阅源 | 94 |
| 原始节点 | 97420 |
| 去重后节点 | 26475 |
| TCP 可达 | 3000 |
| 真实可用 | 330 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 26475 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.4 |
| geo | 1.5 |
| tcp | 43.2 |
| probe | 213.4 |
| real_test | 159.2 |
| generate | 81.9 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 59595 |
| vmess | 15139 |
| shadowsocks | 11280 |
| trojan | 8912 |
| hysteria2 | 1600 |
| http | 599 |
| shadowsocksr | 170 |
| socks | 76 |
| anytls | 27 |
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
| 80.98 | vless | 249.1 | 687.7 | 22.01 | 0.0 | 8.79 | 11.68 | 18.5 | Au1rxx-base64 | 79.141.172.154 |
| 80.8 | vless | 259.3 | 677.4 | 21.78 | 0.0 | 8.84 | 11.68 | 18.5 | Au1rxx-base64 | 169.40.42.90 |
| 79.99 | vless | 263.0 | 635.7 | 21.69 | 0.0 | 8.79 | 11.68 | 18.5 | Au1rxx-base64 | 195.211.98.43 |
| 79.75 | vless | 304.6 | 684.0 | 20.73 | 0.0 | 8.84 | 11.68 | 18.5 | Au1rxx-base64 | 169.40.42.173 |
| 79.59 | vless | 307.3 | 828.7 | 20.66 | 0.0 | 8.75 | 11.68 | 18.5 | Au1rxx-base64 | 169.40.42.75 |
| 79.23 | shadowsocks | 257.7 | 705.3 | 21.81 | 0.0 | 10.0 | 13.7 | 17.72 | mheidari-all | 37.19.198.244 |
| 78.9 | shadowsocks | 272.1 | 721.4 | 21.48 | 0.0 | 10.0 | 13.7 | 17.72 | mheidari-all | 37.19.198.236 |
| 78.8 | shadowsocks | 254.6 | 663.0 | 21.88 | 0.0 | 10.0 | 13.7 | 17.72 | mheidari-all | 140.82.63.79 |
| 78.69 | vless | 353.3 | 973.0 | 19.6 | 0.0 | 8.91 | 11.68 | 18.5 | Au1rxx-base64 | 185.95.231.233 |
| 78.54 | vless | 356.6 | 974.5 | 19.52 | 0.0 | 8.84 | 11.68 | 18.5 | Au1rxx-base64 | 169.40.42.16 |
| 78.52 | vless | 355.7 | 952.5 | 19.54 | 0.0 | 8.8 | 11.68 | 18.5 | Au1rxx-base64 | 185.95.231.156 |
| 78.5 | vless | 358.5 | 858.8 | 19.48 | 0.0 | 8.84 | 11.68 | 18.5 | Au1rxx-base64 | 169.40.42.15 |
| 78.48 | vless | 247.1 | 695.7 | 22.06 | 0.0 | 10.0 | 11.68 | 14.74 | Surfboard-tg-mixed | 47.253.226.114 |
| 77.93 | vless | 276.0 | 739.6 | 21.39 | 0.0 | 8.9 | 11.68 | 18.5 | Au1rxx-base64 | 169.40.42.179 |
| 77.64 | vless | 292.0 | 708.0 | 21.02 | 0.0 | 8.76 | 11.68 | 18.5 | Au1rxx-base64 | 169.40.42.163 |
| 77.54 | vless | 310.4 | 703.0 | 20.59 | 0.0 | 8.74 | 11.68 | 18.5 | Au1rxx-base64 | 198.251.78.29 |
| 77.42 | vless | 351.1 | 907.7 | 19.65 | 0.0 | 10.0 | 11.68 | 18.5 | Au1rxx-base64 | 169.40.42.202 |
| 77.39 | vless | 318.4 | 690.6 | 20.41 | 0.0 | 8.8 | 11.68 | 18.5 | Au1rxx-base64 | 169.40.42.104 |
| 77.08 | vless | 289.7 | 769.3 | 21.07 | 0.0 | 8.79 | 11.68 | 18.5 | Au1rxx-base64 | 169.40.42.231 |
| 76.99 | vless | 337.9 | 908.7 | 19.96 | 0.0 | 8.91 | 11.68 | 18.5 | Au1rxx-base64 | 169.40.42.184 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.945 | 0.88 | 258 | 1699 | prefer |
| Surfboard-tg-mixed | 0.729 | 0.657 | 35 | 7258 | prefer |
| mheidari-all | 0.557 | 0.476 | 147 | 22782 | observe |
| ermaozi | 0.386 | 0.389 | 18 | 304 | observe |
| DeltaKronecker-all | 0.32 | 0.5 | 4 | 5452 | observe |
| tg-oneclickvpnkeys | 0.258 | 1.0 | 1 | 67 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5293 | observe |
| Epodonios-all | 0.255 | None | 0 | 7757 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9237 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5857 | observe |
| barry-far-vless | 0.255 | None | 0 | 6083 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4324 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| cn-block | ClientOSError | - | 44 |
| 204 | TimeoutError | - | 25 |
| 204 | ProxyError | - | 21 |
| cn-block | TimeoutError | - | 21 |
| 204 | ProxyConnectionError | - | 10 |
| speed | TimeoutError | - | 7 |
| geo | TimeoutError | - | 4 |
| 204 | ClientOSError | - | 2 |
| speed | ClientOSError | - | 2 |
| geo | ClientOSError | - | 1 |
| speed | ProxyError | - | 1 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 290 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
