# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-11-10 02:27:08 |
| 运行耗时 | 297.9s |
| 订阅源总数 | 107 |
| 健康订阅源 | 87 |
| 原始节点 | 82150 |
| 去重后节点 | 26759 |
| TCP 可达 | 3000 |
| 真实可用 | 587 |
| Verified 输出 | 127 |
| Global 输出 | 300 |
| All 输出 | 26759 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.8 |
| geo | 1.5 |
| tcp | 77.0 |
| probe | 94.1 |
| real_test | 85.2 |
| china_check | 19.0 |
| write_verified | 0.1 |
| generate | 14.4 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 49821 |
| vmess | 14195 |
| shadowsocks | 9163 |
| trojan | 6894 |
| hysteria2 | 1564 |
| http | 246 |
| shadowsocksr | 149 |
| socks | 52 |
| hysteria | 30 |
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
| 95.76 | trojan | 274.6 | 0.4 | 21.42 | 14.98 | 9.72 | 14.2 | 17.94 | Au1rxx-base64 | 216.152.147.48 |
| 95.56 | trojan | 250.8 | 0.5 | 21.97 | 14.98 | 8.97 | 14.2 | 17.94 | Au1rxx-base64 | 216.152.155.59 |
| 94.83 | trojan | 276.5 | 3.5 | 21.38 | 14.87 | 8.94 | 14.2 | 17.94 | Au1rxx-base64 | 170.101.101.19 |
| 94.72 | trojan | 273.5 | 8.4 | 21.45 | 14.69 | 8.94 | 14.2 | 17.94 | Au1rxx-base64 | 170.101.101.67 |
| 94.71 | shadowsocks | 237.5 | 0.9 | 22.28 | 14.97 | 10.0 | 14.02 | 17.94 | Au1rxx-base64 | 185.230.230.18 |
| 94.47 | shadowsocks | 250.7 | 12.2 | 21.97 | 14.54 | 10.0 | 14.02 | 17.94 | Au1rxx-base64 | 37.19.198.160 |
| 93.86 | trojan | 257.6 | 2.3 | 21.81 | 14.91 | 7.5 | 14.2 | 17.94 | Au1rxx-base64 | 216.152.155.23 |
| 93.81 | shadowsocks | 250.5 | 5.9 | 21.98 | 14.78 | 10.0 | 14.02 | 17.94 | Au1rxx-base64 | 193.151.163.18 |
| 93.76 | shadowsocks | 269.0 | 6.8 | 21.55 | 14.75 | 10.0 | 14.02 | 17.94 | Au1rxx-base64 | 45.86.51.18 |
| 93.55 | shadowsocks | 301.0 | 5.9 | 20.81 | 14.78 | 10.0 | 14.02 | 17.94 | Au1rxx-base64 | 37.19.198.243 |
| 92.95 | shadowsocks | 331.4 | 3.1 | 20.11 | 14.88 | 10.0 | 14.02 | 17.94 | Au1rxx-base64 | 37.19.198.236 |
| 92.72 | trojan | 289.4 | 8.0 | 21.08 | 14.7 | 7.3 | 14.2 | 17.94 | Au1rxx-base64 | 216.152.147.79 |
| 92.64 | shadowsocks | 327.9 | 0.2 | 20.19 | 14.99 | 10.0 | 14.02 | 17.94 | Au1rxx-base64 | 51.222.136.236 |
| 92.6 | trojan | 306.5 | 1.1 | 20.68 | 14.96 | 7.32 | 14.2 | 17.94 | Au1rxx-base64 | 216.152.147.201 |
| 92.52 | shadowsocks | 297.4 | 2.2 | 20.89 | 14.92 | 10.0 | 14.02 | 17.94 | Au1rxx-base64 | 193.151.160.9 |
| 92.41 | trojan | 315.4 | 0.6 | 20.48 | 14.98 | 7.31 | 14.2 | 17.94 | Au1rxx-base64 | 216.152.147.85 |
| 92.13 | shadowsocks | 286.7 | 2.3 | 21.14 | 14.91 | 9.7 | 14.02 | 17.94 | Au1rxx-base64 | 193.151.160.18 |
| 91.92 | vless | 276.3 | 3.1 | 21.38 | 14.88 | 8.89 | 8.83 | 17.94 | Au1rxx-base64 | 195.123.235.183 |
| 91.68 | trojan | 439.3 | 1.8 | 17.61 | 14.93 | 10.0 | 14.2 | 17.94 | Au1rxx-base64 | 69.164.240.85 |
| 91.04 | trojan | 315.4 | 5.5 | 20.48 | 14.79 | 7.25 | 14.2 | 17.94 | Au1rxx-base64 | 169.197.140.214 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 1.0 | 0.989 | 89 | 602 | prefer |
| Surfboard-tg-mixed | 0.927 | 0.85 | 220 | 8250 | prefer |
| Au1rxx-base64 | 0.926 | 0.859 | 234 | 1751 | prefer |
| mheidari-all | 0.774 | 0.696 | 158 | 14061 | prefer |
| xiaoji235-airport-v2ray-all | 0.391 | 1.0 | 2 | 6752 | observe |
| DeltaKronecker-all | 0.287 | 0.5 | 2 | 2754 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 11203 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 6133 | observe |
| barry-far-vless | 0.255 | None | 0 | 6344 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4583 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.245 | None | 0 | 1751 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |
| 10ium-HighSpeed | 0.209 | None | 0 | 839 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 73 |
| speed | ClientOSError | - | 11 |
| cn-block | TimeoutError | - | 8 |
| geo | ClientOSError | - | 8 |
| 204 | ProxyError | - | 7 |
| 204 | TimeoutError | - | 4 |
| cn-block | ClientOSError | - | 2 |
| cn-block | ProxyError | - | 1 |
| geo | TimeoutError | - | 1 |
| cn-block | status | 530 | 1 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 145 | 127 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
