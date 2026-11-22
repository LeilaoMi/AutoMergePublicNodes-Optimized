# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-11-22 19:55:04 |
| 运行耗时 | 296.0s |
| 订阅源总数 | 107 |
| 健康订阅源 | 88 |
| 原始节点 | 82521 |
| 去重后节点 | 28181 |
| TCP 可达 | 3000 |
| 真实可用 | 322 |
| Verified 输出 | 41 |
| Global 输出 | 300 |
| All 输出 | 28181 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.9 |
| geo | 1.6 |
| tcp | 82.0 |
| probe | 96.5 |
| real_test | 61.8 |
| china_check | 32.4 |
| write_verified | 0.0 |
| generate | 14.9 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 48518 |
| vmess | 15118 |
| shadowsocks | 10327 |
| trojan | 6585 |
| hysteria2 | 1519 |
| shadowsocksr | 150 |
| http | 140 |
| socks | 100 |
| hysteria | 32 |
| tuic | 17 |
| anytls | 15 |

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
| 92.33 | vless | 191.5 | 4.8 | 23.35 | 14.82 | 7.72 | 8.82 | 17.62 | Au1rxx-base64 | 45.63.53.81 |
| 91.29 | shadowsocks | 235.8 | 5.6 | 22.32 | 14.79 | 10.0 | 13.92 | 17.62 | Au1rxx-base64 | 95.215.201.18 |
| 90.41 | shadowsocks | 231.2 | 3.3 | 22.43 | 14.88 | 10.0 | 13.92 | 17.62 | Au1rxx-base64 | 173.244.56.9 |
| 90.04 | shadowsocks | 250.8 | 2.0 | 21.97 | 14.93 | 10.0 | 13.92 | 17.62 | Au1rxx-base64 | 149.22.95.183 |
| 89.12 | shadowsocks | 317.3 | 3.5 | 20.43 | 14.87 | 10.0 | 13.92 | 17.62 | Au1rxx-base64 | 156.146.38.168 |
| 88.72 | trojan | 317.2 | 1.3 | 20.43 | 14.95 | 10.0 | 11.45 | 17.62 | Au1rxx-base64 | 66.23.203.21 |
| 88.09 | shadowsocks | 237.9 | 0.9 | 22.27 | 14.96 | 10.0 | 13.92 | 17.62 | Au1rxx-base64 | 173.244.56.6 |
| 87.82 | hysteria2 | 228.0 | 1.2 | 22.5 | 14.95 | 4.63 | 13.64 | 17.62 | Au1rxx-base64 | 66.94.121.46 |
| 86.69 | shadowsocks | 360.1 | 0.1 | 19.44 | 15.0 | 10.0 | 13.92 | 17.62 | Au1rxx-base64 | 37.19.198.244 |
| 86.41 | shadowsocks | 365.9 | 0.5 | 19.31 | 14.98 | 10.0 | 13.92 | 17.62 | Au1rxx-base64 | 37.19.198.236 |
| 85.6 | shadowsocks | 317.5 | 0.5 | 20.43 | 14.98 | 9.77 | 13.92 | 17.62 | Au1rxx-base64 | 149.22.87.240 |
| 85.28 | shadowsocks | 394.5 | 3.9 | 18.64 | 14.85 | 10.0 | 13.92 | 17.62 | Au1rxx-base64 | 45.86.51.18 |
| 85.26 | shadowsocks | 397.8 | 7.6 | 18.57 | 14.72 | 10.0 | 13.92 | 17.62 | Au1rxx-base64 | 185.230.230.18 |
| 85.14 | shadowsocks | 375.7 | 4.6 | 19.08 | 14.83 | 10.0 | 13.92 | 17.62 | Au1rxx-base64 | 193.151.163.18 |
| 85.08 | http | 200.1 | 1.7 | 23.15 | 14.94 | 0.0 | 14.03 | 16.46 | ermaozi | 172.64.68.89 |
| 85.07 | shadowsocks | 340.9 | 1.8 | 19.89 | 14.93 | 5.67 | 13.92 | 17.62 | Au1rxx-base64 | 156.146.38.169 |
| 84.96 | shadowsocks | 405.3 | 1.1 | 18.4 | 14.96 | 10.0 | 13.92 | 17.62 | Au1rxx-base64 | 37.19.198.160 |
| 84.92 | shadowsocks | 406.1 | 12.5 | 18.38 | 14.53 | 10.0 | 13.92 | 17.62 | Au1rxx-base64 | 37.19.198.243 |
| 84.4 | hysteria2 | 275.0 | 0.2 | 21.41 | 14.99 | 6.99 | 13.64 | 17.62 | Au1rxx-base64 | 8.209.247.109 |
| 84.11 | http | 199.3 | 1.1 | 23.16 | 14.96 | 0.0 | 14.03 | 16.46 | ermaozi | 172.64.69.89 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.977 | 1.0 | 23 | 415 | prefer |
| Surfboard-tg-mixed | 0.847 | 0.77 | 161 | 8739 | prefer |
| mheidari-all | 0.787 | 0.711 | 121 | 14491 | prefer |
| Au1rxx-base64 | 0.734 | 0.667 | 129 | 1751 | prefer |
| xiaoji235-airport-v2ray-all | 0.391 | 1.0 | 2 | 6752 | observe |
| ermaozi-get_subscribe | 0.371 | 1.0 | 3 | 318 | observe |
| DeltaKronecker-all | 0.335 | 1.0 | 1 | 2671 | observe |
| tg-LonUp_M | 0.275 | 0.667 | 3 | 167 | observe |
| tg-oneclickvpnkeys | 0.259 | 1.0 | 1 | 109 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5069 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 12183 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5664 | observe |
| barry-far-vless | 0.255 | None | 0 | 5881 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4512 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 55 |
| 204 | ProxyError | - | 27 |
| cn-block | ClientOSError | - | 10 |
| 204 | TimeoutError | - | 6 |
| cn-block | TimeoutError | - | 5 |
| speed | TimeoutError | - | 4 |
| 204 | ClientOSError | - | 3 |
| geo | ProxyError | - | 2 |
| cn-block | ProxyError | - | 1 |
| geo | ClientOSError | - | 1 |
| speed | ProxyError | - | 1 |
| geo | TimeoutError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 52 | 41 | - |
| global | False | 284 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
