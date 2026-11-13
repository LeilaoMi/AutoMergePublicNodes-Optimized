# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-11-13 07:01:01 |
| 运行耗时 | 275.4s |
| 订阅源总数 | 107 |
| 健康订阅源 | 86 |
| 原始节点 | 82620 |
| 去重后节点 | 26689 |
| TCP 可达 | 3000 |
| 真实可用 | 487 |
| Verified 输出 | 92 |
| Global 输出 | 300 |
| All 输出 | 26689 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.9 |
| geo | 1.4 |
| tcp | 74.6 |
| probe | 77.9 |
| real_test | 83.5 |
| china_check | 22.7 |
| write_verified | 0.0 |
| generate | 10.4 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 49515 |
| vmess | 14755 |
| shadowsocks | 9505 |
| trojan | 6786 |
| hysteria2 | 1497 |
| http | 284 |
| shadowsocksr | 153 |
| socks | 54 |
| hysteria | 35 |
| tuic | 21 |
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
| 93.91 | shadowsocks | 252.1 | 3.0 | 21.94 | 14.89 | 10.0 | 13.56 | 17.52 | Au1rxx-base64 | 156.146.38.168 |
| 93.84 | shadowsocks | 256.1 | 2.5 | 21.85 | 14.91 | 10.0 | 13.56 | 17.52 | Au1rxx-base64 | 156.146.38.170 |
| 93.09 | shadowsocks | 269.7 | 0.9 | 21.54 | 14.97 | 10.0 | 13.56 | 17.52 | Au1rxx-base64 | 193.151.163.18 |
| 91.64 | shadowsocks | 325.9 | 4.5 | 20.23 | 14.83 | 10.0 | 13.56 | 17.52 | Au1rxx-base64 | 45.86.51.18 |
| 90.67 | shadowsocks | 245.2 | 1.8 | 22.1 | 14.93 | 6.56 | 13.56 | 17.52 | Au1rxx-base64 | 156.146.38.169 |
| 89.98 | vless | 388.2 | 1.7 | 18.79 | 14.94 | 9.96 | 9.34 | 17.52 | Au1rxx-base64 | 169.40.42.89 |
| 89.91 | shadowsocks | 253.4 | 1.9 | 21.91 | 14.93 | 10.0 | 13.56 | 17.52 | Au1rxx-base64 | 156.146.38.167 |
| 89.91 | vless | 305.8 | 2.7 | 20.7 | 14.9 | 10.0 | 9.34 | 17.52 | Au1rxx-base64 | 169.40.42.74 |
| 89.35 | shadowsocks | 310.0 | 2.4 | 20.6 | 14.91 | 9.29 | 13.56 | 17.52 | Au1rxx-base64 | 193.151.160.18 |
| 88.76 | shadowsocks | 340.0 | 3.2 | 19.91 | 14.88 | 10.0 | 13.56 | 17.52 | Au1rxx-base64 | 193.151.160.9 |
| 88.64 | shadowsocks | 296.2 | 3.8 | 20.92 | 14.86 | 10.0 | 13.56 | 17.52 | Au1rxx-base64 | 95.215.201.18 |
| 88.02 | shadowsocks | 278.9 | 1.0 | 21.32 | 14.96 | 10.0 | 13.56 | 17.52 | Au1rxx-base64 | 185.230.230.18 |
| 86.23 | vless | 384.9 | 0.8 | 18.87 | 14.97 | 10.0 | 9.34 | 17.52 | Au1rxx-base64 | 169.40.42.35 |
| 85.9 | http | 287.6 | 0.3 | 21.12 | 14.99 | 0.0 | 14.21 | 19.08 | ermaozi | 172.64.68.89 |
| 85.66 | http | 271.0 | 2.5 | 21.5 | 14.91 | 0.0 | 14.21 | 19.08 | ermaozi | 206.223.183.21 |
| 85.36 | http | 332.7 | 0.3 | 20.08 | 14.99 | 0.0 | 14.21 | 19.08 | ermaozi | 149.88.98.81 |
| 85.16 | vless | 393.0 | 2.9 | 18.68 | 14.89 | 8.59 | 9.34 | 17.52 | Au1rxx-base64 | 169.40.42.229 |
| 85.01 | vless | 367.0 | 0.1 | 19.28 | 15.0 | 9.96 | 9.34 | 17.52 | Au1rxx-base64 | 169.40.42.168 |
| 84.79 | vless | 364.4 | 138.3 | 19.34 | 9.81 | 9.9 | 9.34 | 17.52 | Au1rxx-base64 | 66.70.179.198 |
| 84.71 | trojan | 257.8 | 0.6 | 21.81 | 14.98 | 9.54 | 8.36 | 17.52 | Au1rxx-base64 | 216.152.147.48 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.997 | 0.986 | 72 | 594 | prefer |
| Au1rxx-base64 | 0.868 | 0.801 | 211 | 1751 | prefer |
| mheidari-all | 0.822 | 0.75 | 64 | 13793 | prefer |
| Surfboard-tg-mixed | 0.809 | 0.731 | 271 | 8675 | prefer |
| xiaoji235-airport-v2ray-all | 0.287 | 0.5 | 2 | 6752 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4998 | observe |
| DeltaKronecker-all | 0.255 | None | 0 | 2737 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 11327 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 6119 | observe |
| barry-far-vless | 0.255 | None | 0 | 6543 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4624 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.245 | None | 0 | 1751 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 61 |
| speed | ClientOSError | - | 34 |
| 204 | ProxyError | - | 10 |
| 204 | TimeoutError | - | 8 |
| cn-block | TimeoutError | - | 6 |
| geo | ProxyError | - | 4 |
| cn-block | ProxyError | - | 3 |
| geo | ClientOSError | - | 2 |
| cn-block | ClientOSError | - | 2 |
| speed | TimeoutError | - | 1 |
| 204 | ClientOSError | - | 1 |
| geo | TimeoutError | - | 1 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 61 | 92 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
