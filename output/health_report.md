# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-21 12:38:52 |
| 运行耗时 | 589.8s |
| 订阅源总数 | 107 |
| 健康订阅源 | 94 |
| 原始节点 | 84528 |
| 去重后节点 | 23451 |
| TCP 可达 | 3000 |
| 真实可用 | 455 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23451 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.5 |
| geo | 1.5 |
| tcp | 38.2 |
| probe | 219.6 |
| real_test | 233.8 |
| generate | 90.1 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 51126 |
| vmess | 13408 |
| shadowsocks | 9641 |
| trojan | 8381 |
| hysteria2 | 1107 |
| http | 632 |
| shadowsocksr | 140 |
| socks | 75 |
| hysteria | 10 |
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
| 82.42 | hysteria2 | 268.4 | 616.5 | 21.56 | 0.0 | 10.0 | 14.21 | 18.66 | Au1rxx-base64 | 66.94.121.46 |
| 77.41 | shadowsocks | 231.9 | 532.4 | 22.41 | 0.0 | 10.0 | 14.28 | 14.72 | Surfboard-tg-mixed | 173.244.56.9 |
| 76.28 | vless | 247.3 | 556.3 | 22.05 | 0.0 | 10.0 | 7.93 | 18.66 | Au1rxx-base64 | 192.3.20.155 |
| 75.86 | vless | 273.6 | 608.1 | 21.44 | 0.0 | 10.0 | 7.93 | 18.66 | Au1rxx-base64 | 15.204.97.216 |
| 75.57 | shadowsocks | 351.2 | 576.7 | 19.65 | 0.0 | 10.0 | 14.28 | 18.66 | Au1rxx-base64 | 23.150.248.20 |
| 74.68 | shadowsocks | 220.2 | 529.8 | 22.68 | 0.0 | 10.0 | 14.28 | 14.72 | Surfboard-tg-mixed | 173.244.56.6 |
| 74.51 | vless | 209.8 | 532.5 | 22.92 | 0.0 | 10.0 | 7.93 | 18.66 | Au1rxx-base64 | 195.123.240.65 |
| 74.46 | vless | 278.8 | 615.5 | 21.32 | 0.0 | 10.0 | 7.93 | 18.66 | Au1rxx-base64 | 15.204.97.209 |
| 74.01 | http | 225.3 | 574.4 | 22.56 | 0.0 | 10.0 | 10.45 | 14.0 | ermaozi | 138.199.35.198 |
| 73.87 | vless | 333.5 | 762.7 | 20.06 | 0.0 | 10.0 | 7.93 | 18.66 | Au1rxx-base64 | 79.141.172.154 |
| 73.8 | http | 234.5 | 601.2 | 22.35 | 0.0 | 10.0 | 10.45 | 14.0 | ermaozi | 138.199.35.206 |
| 73.71 | http | 238.5 | 586.7 | 22.26 | 0.0 | 10.0 | 10.45 | 14.0 | ermaozi | 138.199.35.212 |
| 73.67 | http | 240.3 | 593.0 | 22.22 | 0.0 | 10.0 | 10.45 | 14.0 | ermaozi | 138.199.35.200 |
| 73.66 | http | 240.6 | 599.8 | 22.21 | 0.0 | 10.0 | 10.45 | 14.0 | ermaozi | 138.199.35.218 |
| 73.61 | http | 242.7 | 597.6 | 22.16 | 0.0 | 10.0 | 10.45 | 14.0 | ermaozi | 138.199.35.216 |
| 73.55 | http | 245.5 | 597.9 | 22.1 | 0.0 | 10.0 | 10.45 | 14.0 | ermaozi | 138.199.35.203 |
| 73.48 | shadowsocks | 258.3 | 628.7 | 21.8 | 0.0 | 10.0 | 14.28 | 11.4 | mheidari-all | 156.146.38.170 |
| 73.38 | shadowsocks | 262.5 | 638.9 | 21.7 | 0.0 | 10.0 | 14.28 | 11.4 | mheidari-all | 156.146.38.168 |
| 71.35 | shadowsocks | 328.5 | 853.2 | 20.17 | 0.0 | 10.0 | 14.28 | 11.4 | mheidari-all | 108.181.118.10 |
| 71.28 | hysteria2 | 444.1 | 763.7 | 17.5 | 0.0 | 9.53 | 14.21 | 18.66 | Au1rxx-base64 | 62.210.124.146 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| mheidari-all | 0.945 | 0.886 | 35 | 16192 | prefer |
| Au1rxx-base64 | 0.919 | 0.856 | 271 | 1649 | prefer |
| DeltaKronecker-all | 0.767 | 0.696 | 46 | 6181 | prefer |
| Surfboard-tg-mixed | 0.661 | 0.582 | 208 | 7246 | observe |
| ermaozi | 0.544 | 0.531 | 64 | 350 | observe |
| Au1rxx-clash | 0.377 | 1.0 | 2 | 1638 | observe |
| tg-oneclickvpnkeys | 0.316 | 1.0 | 2 | 123 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| Epodonios-all | 0.255 | None | 0 | 7697 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3996 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 8900 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5845 | observe |
| barry-far-vless | 0.255 | None | 0 | 6062 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4358 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | ClientOSError | - | 33 |
| 204 | ProxyError | - | 30 |
| geo | TimeoutError | - | 28 |
| speed | ClientOSError | - | 23 |
| cn-block | TimeoutError | - | 20 |
| 204 | TimeoutError | - | 19 |
| speed | TimeoutError | - | 15 |
| cn-block | ClientOSError | - | 9 |
| 204 | ClientOSError | - | 3 |
| geo | ProxyError | - | 3 |
| speed | ProxyError | - | 2 |
| cn-block | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
