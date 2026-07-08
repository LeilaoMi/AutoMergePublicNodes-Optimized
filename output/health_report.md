# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-08 08:40:46 |
| 运行耗时 | 196.2s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 83146 |
| 去重后节点 | 24737 |
| TCP 可达 | 3000 |
| 真实可用 | 356 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 24737 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.3 |
| geo | 1.3 |
| tcp | 31.9 |
| probe | 43.5 |
| real_test | 88.1 |
| generate | 26.0 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 48609 |
| trojan | 13292 |
| vmess | 10475 |
| shadowsocks | 9610 |
| hysteria2 | 824 |
| shadowsocksr | 143 |
| http | 140 |
| socks | 39 |
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
| 77.89 | shadowsocks | 202.9 | 539.8 | 23.08 | 0.0 | 10.0 | 13.91 | 14.9 | Au1rxx-base64 | 149.22.95.183 |
| 75.79 | trojan | 283.2 | 490.0 | 21.22 | 0.0 | 10.0 | 14.03 | 19.68 | Surfboard-tg-mixed | 162.159.38.119 |
| 74.66 | trojan | 344.2 | 332.1 | 19.81 | 2.54 | 9.94 | 14.03 | 19.68 | Surfboard-tg-mixed | 103.106.228.187 |
| 74.04 | trojan | 340.5 | 767.0 | 19.9 | 0.0 | 10.0 | 14.03 | 15.76 | DeltaKronecker-all | 45.32.198.247 |
| 73.26 | shadowsocks | 252.7 | 514.3 | 21.93 | 0.0 | 10.0 | 13.91 | 14.9 | Au1rxx-base64 | 108.181.118.10 |
| 72.42 | trojan | 326.2 | 668.1 | 20.23 | 0.0 | 10.0 | 14.03 | 15.76 | DeltaKronecker-all | 64.94.95.115 |
| 72.41 | trojan | 338.9 | 770.0 | 19.93 | 0.0 | 10.0 | 14.03 | 14.2 | mheidari-all | 149.28.241.235 |
| 72.38 | trojan | 324.4 | 662.8 | 20.27 | 0.0 | 10.0 | 14.03 | 15.76 | DeltaKronecker-all | 64.94.95.117 |
| 72.34 | trojan | 324.0 | 659.7 | 20.28 | 0.0 | 10.0 | 14.03 | 15.76 | DeltaKronecker-all | 64.94.95.114 |
| 72.29 | trojan | 343.0 | 779.7 | 19.84 | 0.0 | 10.0 | 14.03 | 14.2 | mheidari-all | 45.32.195.168 |
| 72.25 | trojan | 488.8 | 1136.7 | 16.46 | 0.0 | 10.0 | 14.03 | 19.68 | Surfboard-tg-mixed | 64.94.95.118 |
| 71.4 | trojan | 439.8 | 477.2 | 17.6 | 0.0 | 10.0 | 14.03 | 19.68 | Surfboard-tg-mixed | 199.232.2.79 |
| 71.13 | shadowsocks | 307.1 | 719.1 | 20.67 | 0.0 | 10.0 | 13.91 | 14.9 | Au1rxx-base64 | 108.181.0.177 |
| 71.06 | shadowsocks | 286.8 | 320.7 | 21.14 | 2.97 | 9.05 | 13.91 | 14.9 | Au1rxx-base64 | 149.22.87.240 |
| 70.67 | shadowsocks | 286.2 | 326.8 | 21.15 | 2.75 | 9.05 | 13.91 | 14.9 | Au1rxx-base64 | 149.22.87.241 |
| 70.19 | shadowsocks | 319.0 | 641.5 | 20.39 | 0.0 | 9.12 | 13.91 | 14.9 | Au1rxx-base64 | 156.146.38.168 |
| 70.08 | shadowsocks | 283.1 | 341.6 | 21.23 | 2.19 | 9.05 | 13.91 | 14.9 | Au1rxx-base64 | 149.22.87.204 |
| 69.89 | shadowsocks | 266.2 | 542.3 | 21.62 | 0.0 | 10.0 | 13.91 | 14.9 | Au1rxx-base64 | 173.244.56.6 |
| 69.57 | shadowsocks | 323.9 | 686.6 | 20.28 | 0.0 | 9.05 | 13.91 | 14.9 | Au1rxx-base64 | 156.146.38.170 |
| 69.44 | shadowsocks | 397.4 | 804.6 | 18.58 | 0.0 | 10.0 | 13.91 | 14.9 | Au1rxx-base64 | 172.245.235.84 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| mheidari-all | 0.859 | 0.786 | 84 | 17974 | prefer |
| Au1rxx-base64 | 0.846 | 0.851 | 67 | 134 | prefer |
| DeltaKronecker-all | 0.842 | 0.766 | 141 | 8321 | prefer |
| Surfboard-tg-mixed | 0.787 | 0.711 | 121 | 5842 | prefer |
| xiaoji235-airport-v2ray-all | 0.349 | 0.667 | 3 | 3640 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4408 | observe |
| Epodonios-all | 0.255 | None | 0 | 6817 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3971 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6807 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4337 | observe |
| barry-far-vless | 0.255 | None | 0 | 4981 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5352 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 29 |
| speed | ClientOSError | - | 20 |
| 204 | ProxyError | - | 10 |
| cn-block | TimeoutError | - | 7 |
| 204 | TimeoutError | - | 7 |
| 204 | ClientOSError | - | 7 |
| geo | ClientOSError | - | 5 |
| speed | TimeoutError | - | 4 |
| cn-block | ProxyError | - | 3 |
| cn-block | ClientOSError | - | 3 |
| geo | ProxyError | - | 2 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
