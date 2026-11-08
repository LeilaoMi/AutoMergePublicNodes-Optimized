# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-11-08 13:42:58 |
| 运行耗时 | 295.1s |
| 订阅源总数 | 107 |
| 健康订阅源 | 87 |
| 原始节点 | 81840 |
| 去重后节点 | 26970 |
| TCP 可达 | 3000 |
| 真实可用 | 447 |
| Verified 输出 | 68 |
| Global 输出 | 300 |
| All 输出 | 26970 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.7 |
| geo | 1.5 |
| tcp | 76.3 |
| probe | 97.5 |
| real_test | 73.2 |
| china_check | 25.5 |
| write_verified | 0.0 |
| generate | 14.5 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 48816 |
| vmess | 14245 |
| shadowsocks | 9261 |
| trojan | 7386 |
| hysteria2 | 1609 |
| http | 252 |
| shadowsocksr | 157 |
| socks | 55 |
| hysteria | 24 |
| anytls | 20 |
| tuic | 15 |

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
| 94.93 | shadowsocks | 249.2 | 2.3 | 22.01 | 14.91 | 10.0 | 13.95 | 18.06 | Au1rxx-base64 | 37.19.198.243 |
| 94.61 | shadowsocks | 263.2 | 2.5 | 21.69 | 14.91 | 10.0 | 13.95 | 18.06 | Au1rxx-base64 | 37.19.198.236 |
| 94.38 | shadowsocks | 231.2 | 14.8 | 22.43 | 14.44 | 10.0 | 13.95 | 18.06 | Au1rxx-base64 | 45.86.51.18 |
| 94.21 | shadowsocks | 247.6 | 9.3 | 22.05 | 14.65 | 10.0 | 13.95 | 18.06 | Au1rxx-base64 | 185.230.230.18 |
| 94.1 | shadowsocks | 264.0 | 15.5 | 21.67 | 14.42 | 10.0 | 13.95 | 18.06 | Au1rxx-base64 | 37.19.198.160 |
| 92.64 | shadowsocks | 305.1 | 15.8 | 20.72 | 14.41 | 10.0 | 13.95 | 18.06 | Au1rxx-base64 | 193.151.163.18 |
| 92.48 | shadowsocks | 292.0 | 1.5 | 21.02 | 14.94 | 9.01 | 13.95 | 18.06 | Au1rxx-base64 | 193.151.160.18 |
| 92.34 | shadowsocks | 289.7 | 6.5 | 21.07 | 14.76 | 10.0 | 13.95 | 18.06 | Au1rxx-base64 | 193.151.160.9 |
| 91.48 | trojan | 284.0 | 5.4 | 21.2 | 14.8 | 6.68 | 13.24 | 18.06 | Au1rxx-base64 | 170.101.101.67 |
| 91.31 | vless | 306.6 | 2.3 | 20.68 | 14.91 | 9.42 | 8.24 | 18.06 | Au1rxx-base64 | 169.40.42.90 |
| 91.15 | shadowsocks | 290.6 | 2.4 | 21.05 | 14.91 | 10.0 | 13.95 | 18.06 | Au1rxx-base64 | 156.146.38.167 |
| 91.07 | vless | 339.0 | 4.1 | 19.93 | 14.84 | 10.0 | 8.24 | 18.06 | Au1rxx-base64 | 169.40.42.35 |
| 91.02 | trojan | 410.1 | 15.0 | 18.28 | 14.44 | 10.0 | 13.24 | 18.06 | Au1rxx-base64 | 69.164.240.85 |
| 90.59 | trojan | 312.5 | 0.6 | 20.54 | 14.98 | 10.0 | 13.24 | 18.06 | Au1rxx-base64 | 66.163.114.45 |
| 90.58 | trojan | 278.9 | 5.9 | 21.32 | 14.78 | 6.68 | 13.24 | 18.06 | Au1rxx-base64 | 170.101.101.19 |
| 89.91 | shadowsocks | 243.6 | 6.3 | 22.14 | 14.76 | 10.0 | 13.95 | 18.06 | Au1rxx-base64 | 37.19.198.244 |
| 89.24 | trojan | 311.3 | 1.3 | 20.57 | 14.95 | 8.85 | 13.24 | 18.06 | Au1rxx-base64 | 66.163.114.132 |
| 89.0 | vless | 286.7 | 0.4 | 21.14 | 14.98 | 6.58 | 8.24 | 18.06 | Au1rxx-base64 | 195.123.235.183 |
| 89.0 | vless | 360.3 | 1.0 | 19.44 | 14.96 | 9.36 | 8.24 | 18.06 | Au1rxx-base64 | 169.40.42.202 |
| 88.8 | trojan | 349.2 | 1.5 | 19.7 | 14.94 | 10.0 | 13.24 | 18.06 | Au1rxx-base64 | 216.238.80.100 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 1.0 | 1.0 | 55 | 586 | prefer |
| Au1rxx-base64 | 0.903 | 0.836 | 219 | 1751 | prefer |
| Surfboard-tg-mixed | 0.89 | 0.814 | 172 | 8136 | prefer |
| mheidari-all | 0.871 | 0.798 | 84 | 14420 | prefer |
| xiaoji235-airport-v2ray-all | 0.335 | 1.0 | 1 | 6752 | observe |
| DeltaKronecker-all | 0.287 | 0.5 | 2 | 3024 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5035 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 10990 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5786 | observe |
| barry-far-vless | 0.255 | None | 0 | 5999 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4635 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.245 | None | 0 | 1751 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 45 |
| 204 | ProxyError | - | 16 |
| cn-block | ProxyError | - | 6 |
| cn-block | TimeoutError | - | 5 |
| 204 | TimeoutError | - | 4 |
| geo | ProxyError | - | 3 |
| speed | TimeoutError | - | 2 |
| 204 | ClientOSError | - | 2 |
| speed | ClientOSError | - | 1 |
| speed | ProxyError | - | 1 |
| cn-block | ClientOSError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 59 | 68 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
