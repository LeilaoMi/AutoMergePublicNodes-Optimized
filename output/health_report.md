# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-23 11:54:52 |
| 运行耗时 | 296.5s |
| 订阅源总数 | 107 |
| 健康订阅源 | 92 |
| 原始节点 | 96151 |
| 去重后节点 | 26910 |
| TCP 可达 | 3000 |
| 真实可用 | 414 |
| Verified 输出 | 140 |
| Global 输出 | 300 |
| All 输出 | 26910 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.2 |
| geo | 1.6 |
| tcp | 80.5 |
| probe | 93.8 |
| real_test | 75.0 |
| china_check | 24.5 |
| write_verified | 0.1 |
| generate | 13.9 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 56763 |
| vmess | 17202 |
| shadowsocks | 12230 |
| trojan | 8008 |
| hysteria2 | 1351 |
| http | 328 |
| shadowsocksr | 165 |
| socks | 56 |
| anytls | 25 |
| hysteria | 17 |
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
| 96.68 | hysteria2 | 232.9 | 9.1 | 22.39 | 14.66 | 9.57 | 14.0 | 17.56 | Au1rxx-base64 | 129.213.91.185 |
| 94.93 | shadowsocks | 241.9 | 1.4 | 22.18 | 14.95 | 10.0 | 14.24 | 17.56 | Au1rxx-base64 | 37.19.198.236 |
| 94.58 | shadowsocks | 235.5 | 1.3 | 22.33 | 14.95 | 10.0 | 14.24 | 17.56 | Au1rxx-base64 | 185.230.230.18 |
| 94.44 | shadowsocks | 255.1 | 6.2 | 21.87 | 14.77 | 10.0 | 14.24 | 17.56 | Au1rxx-base64 | 37.19.198.244 |
| 92.96 | trojan | 355.5 | 5.7 | 19.55 | 14.79 | 10.0 | 14.06 | 17.56 | Au1rxx-base64 | 69.164.240.85 |
| 92.18 | shadowsocks | 338.5 | 1.7 | 19.94 | 14.94 | 10.0 | 14.24 | 17.56 | Au1rxx-base64 | 15.204.233.41 |
| 91.42 | shadowsocks | 276.4 | 0.1 | 21.38 | 15.0 | 10.0 | 14.24 | 17.56 | Au1rxx-base64 | 156.146.38.167 |
| 91.19 | shadowsocks | 378.1 | 3.6 | 19.03 | 14.86 | 10.0 | 14.24 | 17.56 | Au1rxx-base64 | 193.151.160.9 |
| 91.08 | shadowsocks | 275.8 | 1.2 | 21.39 | 14.95 | 9.18 | 14.24 | 17.56 | Au1rxx-base64 | 156.146.38.170 |
| 90.83 | shadowsocks | 288.0 | 0.1 | 21.11 | 15.0 | 10.0 | 14.24 | 17.56 | Au1rxx-base64 | 156.146.38.168 |
| 90.82 | shadowsocks | 366.1 | 3.3 | 19.3 | 14.88 | 10.0 | 14.24 | 17.56 | Au1rxx-base64 | 193.151.160.18 |
| 90.79 | shadowsocks | 393.3 | 4.9 | 18.67 | 14.82 | 10.0 | 14.24 | 17.56 | Au1rxx-base64 | 45.86.51.18 |
| 89.62 | vless | 280.2 | 1.6 | 21.29 | 14.94 | 9.52 | 8.15 | 17.56 | Au1rxx-base64 | 169.40.42.224 |
| 88.8 | vless | 330.2 | 0.6 | 20.13 | 14.98 | 7.98 | 8.15 | 17.56 | Au1rxx-base64 | 169.40.42.104 |
| 88.25 | vless | 344.7 | 5.1 | 19.8 | 14.81 | 7.93 | 8.15 | 17.56 | Au1rxx-base64 | 169.40.42.168 |
| 88.06 | trojan | 433.5 | 7.8 | 17.74 | 14.71 | 10.0 | 14.06 | 17.56 | Au1rxx-base64 | 66.23.203.21 |
| 87.68 | vless | 292.5 | 4.1 | 21.01 | 14.84 | 6.12 | 8.15 | 17.56 | Au1rxx-base64 | 195.123.235.183 |
| 87.47 | http | 268.2 | 2.9 | 21.57 | 14.89 | 0.0 | 14.29 | 19.72 | ermaozi | 198.44.138.27 |
| 87.42 | vless | 334.3 | 0.5 | 20.04 | 14.98 | 6.69 | 8.15 | 17.56 | Au1rxx-base64 | 169.40.42.229 |
| 87.37 | vless | 367.7 | 14.3 | 19.27 | 14.47 | 7.92 | 8.15 | 17.56 | Au1rxx-base64 | 185.95.231.156 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.986 | 0.971 | 103 | 609 | prefer |
| Au1rxx-base64 | 0.859 | 0.8 | 250 | 1538 | prefer |
| Surfboard-tg-mixed | 0.812 | 0.737 | 95 | 6855 | prefer |
| mheidari-all | 0.802 | 0.731 | 52 | 23755 | prefer |
| DeltaKronecker-all | 0.401 | 0.571 | 7 | 3871 | observe |
| ninja-vless | 0.327 | 1.0 | 1 | 1791 | observe |
| tg-LonUp_M | 0.262 | 1.0 | 1 | 164 | observe |
| zhangkai | 0.256 | 1.0 | 1 | 24 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4911 | observe |
| Epodonios-all | 0.255 | None | 0 | 7492 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 10293 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5326 | observe |
| barry-far-vless | 0.255 | None | 0 | 5662 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4230 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 57 |
| 204 | ProxyError | - | 10 |
| geo | ClientOSError | - | 8 |
| 204 | TimeoutError | - | 7 |
| cn-block | TimeoutError | - | 7 |
| cn-block | ClientOSError | - | 5 |
| speed | ClientOSError | - | 3 |
| geo | TimeoutError | - | 2 |
| 204 | ClientOSError | - | 2 |
| cn-block | ProxyError | - | 1 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 175 | 140 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
