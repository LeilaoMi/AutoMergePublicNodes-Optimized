# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-14 02:56:35 |
| 运行耗时 | 170.3s |
| 订阅源总数 | 107 |
| 健康订阅源 | 44 |
| 原始节点 | 77090 |
| 去重后节点 | 23680 |
| TCP 可达 | 3000 |
| 真实可用 | 359 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23680 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.2 |
| geo | 1.4 |
| tcp | 31.5 |
| probe | 40.5 |
| real_test | 74.9 |
| generate | 15.7 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 44879 |
| trojan | 11356 |
| vmess | 10715 |
| shadowsocks | 9361 |
| hysteria2 | 456 |
| shadowsocksr | 141 |
| http | 135 |
| socks | 29 |
| hysteria | 12 |
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
| 71.23 | shadowsocks | 376.1 | 877.1 | 19.07 | 0.0 | 10.0 | 12.29 | 15.42 | mheidari-all | 185.196.61.82 |
| 70.91 | trojan | 288.9 | 698.4 | 21.09 | 0.0 | 10.0 | 9.92 | 14.46 | DeltaKronecker-all | 64.94.95.115 |
| 70.33 | shadowsocks | 306.6 | 696.3 | 20.68 | 0.0 | 10.0 | 12.29 | 15.42 | mheidari-all | 108.181.57.93 |
| 69.42 | shadowsocks | 376.1 | 928.8 | 19.07 | 0.0 | 10.0 | 12.29 | 15.42 | mheidari-all | 198.98.53.130 |
| 69.41 | vless | 298.2 | 803.4 | 20.88 | 0.0 | 10.0 | 4.07 | 14.46 | DeltaKronecker-all | 20.84.155.134 |
| 67.74 | trojan | 362.1 | 928.4 | 19.4 | 0.0 | 10.0 | 9.92 | 15.42 | mheidari-all | 64.94.95.118 |
| 65.51 | shadowsocks | 247.8 | 609.6 | 22.04 | 0.0 | 10.0 | 12.29 | 5.18 | Au1rxx-base64 | 156.146.38.169 |
| 65.49 | shadowsocks | 248.9 | 628.5 | 22.02 | 0.0 | 10.0 | 12.29 | 5.18 | Au1rxx-base64 | 156.146.38.170 |
| 65.35 | shadowsocks | 254.8 | 617.8 | 21.88 | 0.0 | 10.0 | 12.29 | 5.18 | Au1rxx-base64 | 156.146.38.167 |
| 65.0 | trojan | 611.8 | 1713.2 | 13.62 | 0.0 | 10.0 | 9.92 | 14.46 | DeltaKronecker-all | 64.94.95.117 |
| 64.42 | shadowsocks | 375.0 | 898.0 | 19.1 | 0.0 | 10.0 | 12.29 | 15.42 | mheidari-all | 147.90.234.133 |
| 64.4 | http | 674.4 | 970.6 | 12.17 | 0.0 | 9.59 | 14.61 | 19.52 | snakem982 | 193.176.84.37 |
| 64.37 | shadowsocks | 297.1 | 743.3 | 20.9 | 0.0 | 10.0 | 12.29 | 5.18 | Au1rxx-base64 | 156.146.38.168 |
| 64.32 | http | 678.0 | 994.0 | 12.08 | 0.0 | 9.56 | 14.61 | 19.52 | snakem982 | 193.176.84.31 |
| 64.25 | http | 675.7 | 967.1 | 12.14 | 0.0 | 9.53 | 14.61 | 19.52 | snakem982 | 193.176.84.32 |
| 63.55 | http | 704.4 | 1014.8 | 11.47 | 0.0 | 9.49 | 14.61 | 19.52 | snakem982 | 84.239.14.160 |
| 63.33 | trojan | 363.9 | 655.4 | 19.35 | 0.0 | 10.0 | 9.92 | 14.46 | DeltaKronecker-all | 104.16.97.215 |
| 63.32 | http | 710.6 | 1008.1 | 11.33 | 0.0 | 9.44 | 14.61 | 19.52 | snakem982 | 84.239.49.239 |
| 63.27 | http | 712.8 | 1026.3 | 11.28 | 0.0 | 9.52 | 14.61 | 19.52 | snakem982 | 84.239.49.234 |
| 63.25 | http | 715.1 | 1024.9 | 11.23 | 0.0 | 9.51 | 14.61 | 19.52 | snakem982 | 84.239.49.204 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| Surfboard-tg-mixed | 0.932 | 0.858 | 113 | 5561 | prefer |
| DeltaKronecker-all | 0.75 | 0.671 | 228 | 7926 | prefer |
| mheidari-all | 0.658 | 0.579 | 114 | 16374 | observe |
| Au1rxx-base64 | 0.482 | 1.0 | 6 | 119 | observe |
| xiaoji235-airport-v2ray-all | 0.335 | 1.0 | 1 | 3836 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 3897 | observe |
| Epodonios-all | 0.255 | None | 0 | 6563 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3978 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6467 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4279 | observe |
| barry-far-vless | 0.255 | None | 0 | 4885 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5454 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |
| 10ium-HighSpeed | 0.209 | None | 0 | 839 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 72 |
| speed | ClientOSError | - | 35 |
| speed | TimeoutError | - | 16 |
| geo | ClientOSError | - | 15 |
| cn-block | ClientOSError | - | 2 |
| 204 | ClientOSError | - | 2 |
| cn-block | TimeoutError | - | 2 |
| cn-block | ProxyError | - | 1 |
| 204 | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 205 | 300 | - |
| global | False | 214 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
