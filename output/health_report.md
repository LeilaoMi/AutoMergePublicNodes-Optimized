# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-29 06:04:47 |
| 运行耗时 | 320.9s |
| 订阅源总数 | 107 |
| 健康订阅源 | 87 |
| 原始节点 | 99478 |
| 去重后节点 | 27953 |
| TCP 可达 | 3000 |
| 真实可用 | 542 |
| Verified 输出 | 84 |
| Global 输出 | 300 |
| All 输出 | 27953 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.7 |
| geo | 1.7 |
| tcp | 86.5 |
| probe | 96.6 |
| real_test | 89.4 |
| china_check | 24.0 |
| write_verified | 0.0 |
| generate | 15.0 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 62926 |
| vmess | 14209 |
| shadowsocks | 10723 |
| trojan | 8811 |
| hysteria2 | 2349 |
| http | 203 |
| shadowsocksr | 168 |
| socks | 48 |
| tuic | 16 |
| anytls | 14 |
| hysteria | 11 |

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
| 97.37 | hysteria2 | 237.7 | 5.3 | 22.28 | 14.8 | 9.91 | 12.86 | 19.02 | Au1rxx-base64 | 129.213.91.185 |
| 96.04 | shadowsocks | 247.1 | 0.5 | 22.06 | 14.98 | 10.0 | 13.98 | 19.02 | Au1rxx-base64 | 37.19.198.244 |
| 96.02 | shadowsocks | 245.6 | 1.9 | 22.09 | 14.93 | 10.0 | 13.98 | 19.02 | Au1rxx-base64 | 37.19.198.160 |
| 95.73 | vless | 260.7 | 2.7 | 21.74 | 14.9 | 9.9 | 10.17 | 19.02 | Au1rxx-base64 | 167.17.69.171 |
| 95.32 | trojan | 267.0 | 3.2 | 21.6 | 14.88 | 8.43 | 13.89 | 19.02 | Au1rxx-base64 | 216.152.155.54 |
| 95.22 | shadowsocks | 252.7 | 5.5 | 21.93 | 14.79 | 10.0 | 13.98 | 19.02 | Au1rxx-base64 | 193.151.163.18 |
| 95.2 | shadowsocks | 252.7 | 6.2 | 21.93 | 14.77 | 10.0 | 13.98 | 19.02 | Au1rxx-base64 | 185.230.230.18 |
| 94.94 | vless | 274.1 | 3.2 | 21.43 | 14.88 | 9.44 | 10.17 | 19.02 | Au1rxx-base64 | 195.123.235.183 |
| 94.87 | shadowsocks | 293.0 | 3.4 | 21.0 | 14.87 | 10.0 | 13.98 | 19.02 | Au1rxx-base64 | 37.19.198.243 |
| 94.79 | vless | 288.8 | 0.1 | 21.09 | 15.0 | 9.51 | 10.17 | 19.02 | Au1rxx-base64 | 66.70.179.198 |
| 93.91 | trojan | 266.9 | 0.5 | 21.6 | 14.98 | 7.52 | 13.89 | 19.02 | Au1rxx-base64 | 216.152.155.158 |
| 93.8 | vless | 337.4 | 5.3 | 19.97 | 14.8 | 9.84 | 10.17 | 19.02 | Au1rxx-base64 | 169.40.42.104 |
| 93.74 | vless | 348.6 | 1.4 | 19.71 | 14.95 | 9.89 | 10.17 | 19.02 | Au1rxx-base64 | 169.40.42.231 |
| 93.67 | vless | 346.2 | 4.5 | 19.76 | 14.83 | 9.89 | 10.17 | 19.02 | Au1rxx-base64 | 169.40.42.235 |
| 93.54 | trojan | 273.1 | 7.4 | 21.46 | 14.72 | 7.22 | 13.89 | 19.02 | Au1rxx-base64 | 216.152.155.59 |
| 93.26 | trojan | 273.8 | 7.2 | 21.44 | 14.73 | 7.22 | 13.89 | 19.02 | Au1rxx-base64 | 216.152.155.131 |
| 93.12 | trojan | 286.8 | 0.6 | 21.14 | 14.98 | 10.0 | 13.89 | 19.02 | Au1rxx-base64 | 66.23.203.21 |
| 93.07 | shadowsocks | 350.7 | 2.5 | 19.66 | 14.91 | 10.0 | 13.98 | 19.02 | Au1rxx-base64 | 193.151.160.9 |
| 93.07 | vless | 377.7 | 1.1 | 19.04 | 14.96 | 9.88 | 10.17 | 19.02 | Au1rxx-base64 | 169.40.42.224 |
| 92.93 | vless | 358.3 | 4.7 | 19.48 | 14.82 | 9.44 | 10.17 | 19.02 | Au1rxx-base64 | 185.95.231.156 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.995 | 0.986 | 71 | 560 | prefer |
| Au1rxx-base64 | 0.926 | 0.861 | 331 | 1681 | prefer |
| Surfboard-tg-mixed | 0.742 | 0.664 | 143 | 7653 | prefer |
| mheidari-all | 0.633 | 0.554 | 157 | 34088 | observe |
| xiaoji235-airport-v2ray-all | 0.446 | 0.8 | 5 | 6752 | observe |
| ninja-vless | 0.327 | 1.0 | 1 | 1791 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5004 | observe |
| DeltaKronecker-all | 0.255 | None | 0 | 2801 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 10416 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5723 | observe |
| barry-far-vless | 0.255 | None | 0 | 5902 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4323 | observe |
| Au1rxx-clash | 0.242 | None | 0 | 1681 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 93 |
| geo | ClientOSError | - | 26 |
| 204 | ProxyError | - | 10 |
| 204 | TimeoutError | - | 10 |
| cn-block | ClientOSError | - | 8 |
| geo | ProxyError | - | 5 |
| speed | ClientOSError | - | 5 |
| cn-block | TimeoutError | - | 3 |
| cn-block | ProxyError | - | 2 |
| speed | TimeoutError | - | 2 |
| speed | ProxyError | - | 1 |
| 204 | ClientOSError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 76 | 84 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
