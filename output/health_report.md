# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-11-09 06:56:06 |
| 运行耗时 | 295.6s |
| 订阅源总数 | 107 |
| 健康订阅源 | 87 |
| 原始节点 | 81041 |
| 去重后节点 | 26687 |
| TCP 可达 | 3000 |
| 真实可用 | 440 |
| Verified 输出 | 44 |
| Global 输出 | 300 |
| All 输出 | 26687 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.9 |
| geo | 1.5 |
| tcp | 78.2 |
| probe | 98.5 |
| real_test | 70.2 |
| china_check | 25.8 |
| write_verified | 0.0 |
| generate | 14.6 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 48324 |
| vmess | 14231 |
| shadowsocks | 9134 |
| trojan | 7382 |
| hysteria2 | 1608 |
| shadowsocksr | 150 |
| http | 97 |
| socks | 52 |
| hysteria | 25 |
| tuic | 21 |
| anytls | 17 |

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
| 94.09 | shadowsocks | 253.1 | 3.4 | 21.92 | 14.87 | 10.0 | 13.8 | 17.5 | Au1rxx-base64 | 37.19.198.236 |
| 93.96 | vless | 251.1 | 8.1 | 21.97 | 14.7 | 9.58 | 10.21 | 17.5 | Au1rxx-base64 | 167.17.69.171 |
| 93.91 | shadowsocks | 235.9 | 5.7 | 22.32 | 14.79 | 10.0 | 13.8 | 17.5 | Au1rxx-base64 | 45.86.51.18 |
| 93.82 | vless | 246.2 | 14.2 | 22.08 | 14.47 | 9.56 | 10.21 | 17.5 | Au1rxx-base64 | 159.89.87.21 |
| 93.57 | shadowsocks | 251.7 | 4.7 | 21.95 | 14.82 | 10.0 | 13.8 | 17.5 | Au1rxx-base64 | 185.230.230.18 |
| 92.69 | trojan | 257.8 | 6.5 | 21.81 | 14.76 | 7.92 | 13.2 | 17.5 | Au1rxx-base64 | 216.152.155.59 |
| 92.64 | shadowsocks | 297.5 | 1.3 | 20.89 | 14.95 | 10.0 | 13.8 | 17.5 | Au1rxx-base64 | 193.151.160.9 |
| 92.42 | vless | 317.4 | 1.1 | 20.43 | 14.96 | 9.56 | 10.21 | 17.5 | Au1rxx-base64 | 169.40.42.202 |
| 91.88 | shadowsocks | 331.1 | 0.7 | 20.11 | 14.97 | 10.0 | 13.8 | 17.5 | Au1rxx-base64 | 15.204.247.206 |
| 91.54 | shadowsocks | 287.2 | 1.7 | 21.13 | 14.94 | 8.67 | 13.8 | 17.5 | Au1rxx-base64 | 193.151.160.18 |
| 91.36 | shadowsocks | 250.8 | 1.9 | 21.97 | 14.93 | 10.0 | 13.8 | 17.5 | Au1rxx-base64 | 37.19.198.243 |
| 91.02 | vless | 282.6 | 14.9 | 21.24 | 14.44 | 7.63 | 10.21 | 17.5 | Au1rxx-base64 | 2.24.124.64 |
| 91.02 | shadowsocks | 379.1 | 7.5 | 19.0 | 14.72 | 10.0 | 13.8 | 17.5 | Au1rxx-base64 | 37.19.198.160 |
| 91.02 | trojan | 398.4 | 6.1 | 18.55 | 14.77 | 10.0 | 13.2 | 17.5 | Au1rxx-base64 | 69.164.240.85 |
| 90.76 | shadowsocks | 379.4 | 0.8 | 18.99 | 14.97 | 10.0 | 13.8 | 17.5 | Au1rxx-base64 | 193.151.163.18 |
| 90.63 | vless | 389.8 | 3.5 | 18.75 | 14.87 | 9.58 | 10.21 | 17.5 | Au1rxx-base64 | 169.40.42.168 |
| 90.28 | vless | 289.5 | 26.7 | 21.08 | 14.0 | 9.49 | 10.21 | 17.5 | Au1rxx-base64 | 66.70.179.198 |
| 90.27 | vless | 341.0 | 1.5 | 19.88 | 14.95 | 9.58 | 10.21 | 17.5 | Au1rxx-base64 | 169.40.42.89 |
| 90.22 | shadowsocks | 322.1 | 3.3 | 20.32 | 14.88 | 10.0 | 13.8 | 17.5 | Au1rxx-base64 | 156.146.38.167 |
| 89.93 | vless | 361.3 | 7.3 | 19.42 | 14.73 | 8.07 | 10.21 | 17.5 | Au1rxx-base64 | 209.200.246.148 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.934 | 0.952 | 21 | 519 | prefer |
| Surfboard-tg-mixed | 0.897 | 0.823 | 124 | 8133 | prefer |
| Au1rxx-base64 | 0.888 | 0.821 | 240 | 1751 | prefer |
| mheidari-all | 0.827 | 0.75 | 156 | 13820 | prefer |
| ninja-vless | 0.383 | 1.0 | 2 | 1791 | observe |
| xiaoji235-airport-v2ray-all | 0.349 | 0.667 | 3 | 6752 | observe |
| tg-LonUp_M | 0.262 | 1.0 | 1 | 173 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5035 | observe |
| DeltaKronecker-all | 0.255 | None | 0 | 3024 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 10927 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5838 | observe |
| barry-far-vless | 0.255 | None | 0 | 6048 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4583 | observe |
| Au1rxx-clash | 0.245 | None | 0 | 1751 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 60 |
| 204 | ProxyError | - | 13 |
| cn-block | ProxyError | - | 9 |
| geo | ClientOSError | - | 8 |
| speed | ClientOSError | - | 5 |
| cn-block | TimeoutError | - | 3 |
| geo | ProxyError | - | 2 |
| 204 | TimeoutError | - | 2 |
| speed | ProxyError | - | 1 |
| 204 | ClientOSError | - | 1 |
| cn-block | ClientOSError | - | 1 |
| geo | TimeoutError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 84 | 44 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
