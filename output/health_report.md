# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-07 09:55:28 |
| 运行耗时 | 198.6s |
| 订阅源总数 | 107 |
| 健康订阅源 | 102 |
| 原始节点 | 84945 |
| 去重后节点 | 24815 |
| TCP 可达 | 3000 |
| 真实可用 | 326 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 24815 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.7 |
| geo | 1.4 |
| tcp | 31.9 |
| probe | 49.4 |
| real_test | 88.9 |
| generate | 22.4 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 50777 |
| trojan | 13033 |
| vmess | 10576 |
| shadowsocks | 9507 |
| hysteria2 | 702 |
| shadowsocksr | 140 |
| http | 140 |
| socks | 54 |
| hysteria | 8 |
| tuic | 4 |
| anytls | 4 |

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
| 83.53 | trojan | 219.0 | 471.6 | 22.71 | 0.0 | 10.0 | 13.78 | 19.06 | Surfboard-tg-mixed | 89.116.250.135 |
| 79.03 | shadowsocks | 199.6 | 490.5 | 23.16 | 0.0 | 10.0 | 13.45 | 16.92 | Au1rxx-base64 | 108.181.0.177 |
| 79.01 | shadowsocks | 221.8 | 485.2 | 22.64 | 0.0 | 10.0 | 13.45 | 16.92 | Au1rxx-base64 | 173.244.56.6 |
| 78.83 | shadowsocks | 208.0 | 494.3 | 22.96 | 0.0 | 10.0 | 13.45 | 16.92 | Au1rxx-base64 | 108.181.118.10 |
| 78.31 | shadowsocks | 252.2 | 613.4 | 21.94 | 0.0 | 10.0 | 13.45 | 16.92 | Au1rxx-base64 | 156.146.38.170 |
| 78.21 | shadowsocks | 256.3 | 625.1 | 21.84 | 0.0 | 10.0 | 13.45 | 16.92 | Au1rxx-base64 | 156.146.38.169 |
| 78.12 | shadowsocks | 260.6 | 639.3 | 21.75 | 0.0 | 10.0 | 13.45 | 16.92 | Au1rxx-base64 | 156.146.38.168 |
| 77.75 | shadowsocks | 253.6 | 609.3 | 21.91 | 0.0 | 10.0 | 13.45 | 16.92 | Au1rxx-base64 | 156.146.38.167 |
| 76.5 | trojan | 316.5 | 772.0 | 20.45 | 0.0 | 10.0 | 13.78 | 15.44 | mheidari-all | 149.28.241.235 |
| 76.09 | trojan | 318.4 | 772.9 | 20.41 | 0.0 | 10.0 | 13.78 | 14.82 | DeltaKronecker-all | 45.32.198.247 |
| 75.94 | shadowsocks | 224.9 | 493.7 | 22.57 | 0.0 | 10.0 | 13.45 | 16.92 | Au1rxx-base64 | 173.244.56.9 |
| 74.58 | trojan | 310.2 | 753.2 | 20.6 | 0.0 | 10.0 | 13.78 | 14.82 | DeltaKronecker-all | 45.32.195.168 |
| 73.88 | trojan | 352.5 | 830.4 | 19.62 | 0.0 | 10.0 | 13.78 | 19.06 | Surfboard-tg-mixed | 64.94.95.118 |
| 73.87 | trojan | 318.1 | 740.7 | 20.41 | 0.0 | 10.0 | 13.78 | 14.82 | DeltaKronecker-all | 64.94.95.114 |
| 73.83 | shadowsocks | 281.2 | 286.9 | 21.27 | 4.24 | 9.22 | 13.45 | 16.92 | Au1rxx-base64 | 149.22.87.241 |
| 73.83 | trojan | 323.6 | 751.5 | 20.29 | 0.0 | 10.0 | 13.78 | 14.82 | DeltaKronecker-all | 64.94.95.115 |
| 73.3 | trojan | 321.6 | 738.2 | 20.33 | 0.0 | 10.0 | 13.78 | 14.82 | DeltaKronecker-all | 64.94.95.117 |
| 73.28 | shadowsocks | 284.7 | 609.4 | 21.19 | 0.0 | 9.23 | 13.45 | 16.92 | Au1rxx-base64 | 149.22.95.183 |
| 72.63 | trojan | 366.9 | 366.5 | 19.28 | 1.26 | 9.89 | 13.78 | 19.06 | Surfboard-tg-mixed | 103.106.228.187 |
| 71.12 | trojan | 422.7 | 470.0 | 17.99 | 0.0 | 10.0 | 13.78 | 19.06 | Surfboard-tg-mixed | 199.232.237.250 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| Au1rxx-base64 | 0.846 | 0.857 | 42 | 118 | prefer |
| mheidari-all | 0.812 | 0.737 | 95 | 18158 | prefer |
| Surfboard-tg-mixed | 0.781 | 0.704 | 125 | 6102 | prefer |
| DeltaKronecker-all | 0.664 | 0.585 | 159 | 8472 | observe |
| xiaoji235-airport-v2ray-all | 0.4 | 0.75 | 4 | 3626 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4700 | observe |
| Epodonios-all | 0.255 | None | 0 | 7013 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3972 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7353 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4575 | observe |
| barry-far-vless | 0.255 | None | 0 | 5256 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5338 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| nscl5-all | 0.234 | None | 0 | 1478 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 63 |
| geo | TimeoutError | - | 20 |
| geo | ClientOSError | - | 11 |
| 204 | ProxyError | - | 11 |
| 204 | TimeoutError | - | 8 |
| 204 | ClientOSError | - | 8 |
| geo | ProxyError | - | 4 |
| cn-block | ClientOSError | - | 4 |
| cn-block | ProxyError | - | 3 |
| speed | TimeoutError | - | 3 |
| cn-block | TimeoutError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
