# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-13 03:34:47 |
| 运行耗时 | 183.3s |
| 订阅源总数 | 107 |
| 健康订阅源 | 103 |
| 原始节点 | 77721 |
| 去重后节点 | 24189 |
| TCP 可达 | 3000 |
| 真实可用 | 461 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 24189 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.6 |
| geo | 1.3 |
| tcp | 31.7 |
| probe | 42.4 |
| real_test | 82.2 |
| generate | 21.2 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 44920 |
| trojan | 11685 |
| vmess | 10754 |
| shadowsocks | 9662 |
| hysteria2 | 390 |
| shadowsocksr | 137 |
| http | 137 |
| socks | 26 |
| hysteria | 6 |
| tuic | 4 |

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
| 76.85 | shadowsocks | 220.4 | 600.4 | 22.68 | 0.0 | 10.0 | 11.51 | 16.66 | Au1rxx-base64 | 198.98.53.130 |
| 76.63 | shadowsocks | 229.9 | 633.7 | 22.46 | 0.0 | 10.0 | 11.51 | 16.66 | Au1rxx-base64 | 37.19.198.236 |
| 76.45 | shadowsocks | 237.5 | 660.6 | 22.28 | 0.0 | 10.0 | 11.51 | 16.66 | Au1rxx-base64 | 37.19.198.244 |
| 76.37 | shadowsocks | 241.0 | 670.3 | 22.2 | 0.0 | 10.0 | 11.51 | 16.66 | Au1rxx-base64 | 37.19.198.160 |
| 75.71 | shadowsocks | 247.7 | 659.5 | 22.04 | 0.0 | 10.0 | 11.51 | 16.66 | Au1rxx-base64 | 108.181.57.93 |
| 75.29 | shadowsocks | 287.8 | 806.8 | 21.12 | 0.0 | 10.0 | 11.51 | 16.66 | Au1rxx-base64 | 37.19.198.243 |
| 73.8 | vless | 263.1 | 739.7 | 21.69 | 0.0 | 10.0 | 5.45 | 16.66 | Au1rxx-base64 | 47.253.226.114 |
| 73.34 | shadowsocks | 281.2 | 635.1 | 21.27 | 0.0 | 10.0 | 11.51 | 16.66 | Au1rxx-base64 | 156.146.38.169 |
| 72.72 | shadowsocks | 288.8 | 616.6 | 21.09 | 0.0 | 10.0 | 11.51 | 16.66 | Au1rxx-base64 | 156.146.38.167 |
| 72.66 | shadowsocks | 317.6 | 753.0 | 20.43 | 0.0 | 10.0 | 11.51 | 16.66 | Au1rxx-base64 | 156.146.38.168 |
| 70.87 | vmess | 364.8 | 1047.4 | 19.33 | 0.0 | 10.0 | 13.12 | 12.92 | DeltaKronecker-all | 67.220.95.3 |
| 70.25 | trojan | 392.1 | 948.7 | 18.7 | 0.0 | 10.0 | 10.39 | 16.66 | Au1rxx-base64 | 149.28.241.235 |
| 70.06 | trojan | 383.1 | 916.1 | 18.91 | 0.0 | 10.0 | 10.39 | 16.66 | Au1rxx-base64 | 45.32.195.168 |
| 70.01 | trojan | 347.3 | 672.8 | 19.74 | 0.0 | 10.0 | 10.39 | 14.74 | Surfboard-tg-mixed | 104.21.52.100 |
| 68.85 | shadowsocks | 292.9 | 807.5 | 21.0 | 0.0 | 10.0 | 11.51 | 16.66 | Au1rxx-base64 | 147.90.234.133 |
| 68.8 | shadowsocks | 381.3 | 963.1 | 18.95 | 0.0 | 10.0 | 11.51 | 16.66 | Au1rxx-base64 | 185.196.61.82 |
| 68.75 | shadowsocks | 332.7 | 930.7 | 20.08 | 0.0 | 10.0 | 11.51 | 16.66 | Au1rxx-base64 | 68.168.222.210 |
| 68.58 | shadowsocks | 339.9 | 554.9 | 19.91 | 0.0 | 10.0 | 11.51 | 16.66 | Au1rxx-base64 | 173.244.56.6 |
| 68.56 | hysteria2 | 353.3 | 694.1 | 19.6 | 0.0 | 10.0 | 10.0 | 16.66 | Au1rxx-base64 | 62.210.124.146 |
| 68.32 | vmess | 582.1 | 1681.5 | 14.3 | 0.0 | 10.0 | 13.12 | 15.4 | mheidari-all | 67.220.85.46 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Surfboard-tg-mixed | 0.996 | 0.922 | 129 | 5535 | prefer |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| mheidari-all | 0.878 | 0.804 | 92 | 16437 | prefer |
| DeltaKronecker-all | 0.802 | 0.724 | 246 | 8141 | prefer |
| Au1rxx-base64 | 0.745 | 0.746 | 71 | 127 | prefer |
| xiaoji235-airport-v2ray-all | 0.321 | 1.0 | 1 | 1647 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4003 | observe |
| Epodonios-all | 0.255 | None | 0 | 6591 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3970 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6553 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4183 | observe |
| barry-far-vless | 0.255 | None | 0 | 4867 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5438 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| nscl5-all | 0.236 | None | 0 | 1526 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 43 |
| speed | ClientOSError | - | 27 |
| geo | ClientOSError | - | 15 |
| speed | TimeoutError | - | 8 |
| cn-block | ClientOSError | - | 7 |
| cn-block | TimeoutError | - | 6 |
| 204 | TimeoutError | - | 4 |
| 204 | ClientOSError | - | 3 |
| 204 | ProxyError | - | 2 |
| cn-block | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 266 | 300 | - |
| global | False | 294 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
