# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-03 03:51:54 |
| 运行耗时 | 232.7s |
| 订阅源总数 | 107 |
| 健康订阅源 | 103 |
| 原始节点 | 77844 |
| 去重后节点 | 23404 |
| TCP 可达 | 3000 |
| 真实可用 | 512 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23404 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.5 |
| geo | 1.4 |
| tcp | 30.8 |
| probe | 50.4 |
| real_test | 108.8 |
| generate | 36.8 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 45001 |
| trojan | 12568 |
| vmess | 10472 |
| shadowsocks | 9143 |
| hysteria2 | 220 |
| socks | 155 |
| shadowsocksr | 143 |
| http | 135 |
| hysteria | 6 |
| tuic | 1 |

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
| 75.16 | vless | 257.4 | 728.0 | 21.82 | 0.0 | 10.0 | 8.4 | 14.94 | mheidari-all | 47.253.226.114 |
| 75.11 | shadowsocks | 227.8 | 621.8 | 22.51 | 0.0 | 10.0 | 10.92 | 15.68 | Au1rxx-base64 | 37.19.198.243 |
| 74.99 | shadowsocks | 232.6 | 646.5 | 22.39 | 0.0 | 10.0 | 10.92 | 15.68 | Au1rxx-base64 | 37.19.198.244 |
| 74.44 | shadowsocks | 256.6 | 715.1 | 21.84 | 0.0 | 10.0 | 10.92 | 15.68 | Au1rxx-base64 | 37.19.198.236 |
| 74.31 | shadowsocks | 262.1 | 726.9 | 21.71 | 0.0 | 10.0 | 10.92 | 15.68 | Au1rxx-base64 | 37.19.198.160 |
| 73.23 | shadowsocks | 276.9 | 767.2 | 21.37 | 0.0 | 10.0 | 10.92 | 14.94 | mheidari-all | 198.98.53.130 |
| 72.95 | vless | 298.4 | 813.2 | 20.87 | 0.0 | 10.0 | 8.4 | 15.68 | Au1rxx-base64 | 159.89.87.21 |
| 71.83 | shadowsocks | 315.6 | 859.5 | 20.47 | 0.0 | 10.0 | 10.92 | 14.94 | mheidari-all | 108.181.57.93 |
| 71.67 | vless | 262.1 | 656.1 | 21.71 | 0.0 | 10.0 | 8.4 | 12.56 | DeltaKronecker-all | 198.41.209.87 |
| 71.38 | shadowsocks | 281.8 | 637.2 | 21.25 | 0.0 | 10.0 | 10.92 | 15.68 | Au1rxx-base64 | 156.146.38.170 |
| 71.03 | socks | 264.2 | 662.7 | 21.66 | 0.0 | 10.0 | 10.71 | 13.16 | Surfboard-tg-mixed | 134.122.1.61 |
| 71.02 | shadowsocks | 286.5 | 656.1 | 21.15 | 0.0 | 10.0 | 10.92 | 15.68 | Au1rxx-base64 | 156.146.38.169 |
| 70.94 | vless | 263.0 | 659.4 | 21.69 | 0.0 | 10.0 | 8.4 | 12.56 | DeltaKronecker-all | 104.19.142.226 |
| 70.83 | shadowsocks | 276.3 | 629.2 | 21.38 | 0.0 | 10.0 | 10.92 | 15.68 | Au1rxx-base64 | 156.146.38.167 |
| 70.67 | socks | 236.8 | 640.1 | 22.3 | 0.0 | 10.0 | 10.71 | 13.16 | Surfboard-tg-mixed | 204.48.29.137 |
| 70.67 | vless | 261.0 | 644.6 | 21.74 | 0.0 | 10.0 | 8.4 | 12.56 | DeltaKronecker-all | 104.17.238.33 |
| 70.29 | socks | 252.9 | 719.8 | 21.92 | 0.0 | 10.0 | 10.71 | 13.16 | Surfboard-tg-mixed | 47.253.211.16 |
| 70.04 | shadowsocks | 244.0 | 657.6 | 22.13 | 0.0 | 10.0 | 10.92 | 15.68 | Au1rxx-base64 | 147.90.234.133 |
| 67.27 | vless | 348.4 | 886.4 | 19.71 | 0.0 | 10.0 | 8.4 | 13.16 | Surfboard-tg-mixed | 104.16.75.234 |
| 66.76 | vless | 348.5 | 634.3 | 19.71 | 0.0 | 10.0 | 8.4 | 14.94 | mheidari-all | 107.173.237.146 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| Surfboard-tg-mixed | 0.813 | 0.735 | 324 | 6047 | prefer |
| Au1rxx-base64 | 0.725 | 0.735 | 34 | 73 | prefer |
| mheidari-all | 0.649 | 0.57 | 230 | 16051 | observe |
| DeltaKronecker-all | 0.409 | 0.328 | 244 | 7467 | observe |
| nscl5-all | 0.3 | 1.0 | 1 | 1114 | observe |
| 10ium-HighSpeed | 0.289 | 1.0 | 1 | 839 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4254 | observe |
| Epodonios-all | 0.255 | None | 0 | 7006 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3976 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6800 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4559 | observe |
| barry-far-vless | 0.255 | None | 0 | 5102 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5372 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 149 |
| geo | TimeoutError | - | 115 |
| geo | ClientOSError | - | 52 |
| speed | TimeoutError | - | 14 |
| cn-block | ClientOSError | - | 8 |
| cn-block | TimeoutError | - | 7 |
| 204 | ClientOSError | - | 5 |
| 204 | ProxyError | - | 4 |
| 204 | TimeoutError | - | 4 |
| cn-block | ProxyError | - | 3 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
