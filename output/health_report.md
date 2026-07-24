# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-24 08:39:43 |
| 运行耗时 | 319.9s |
| 订阅源总数 | 107 |
| 健康订阅源 | 102 |
| 原始节点 | 83120 |
| 去重后节点 | 22640 |
| TCP 可达 | 3000 |
| 真实可用 | 856 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22640 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.8 |
| geo | 1.3 |
| tcp | 32.0 |
| probe | 62.5 |
| real_test | 185.6 |
| generate | 33.7 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 46948 |
| trojan | 15481 |
| vmess | 10140 |
| shadowsocks | 9929 |
| hysteria2 | 411 |
| shadowsocksr | 79 |
| socks | 58 |
| http | 51 |
| hysteria | 17 |
| tuic | 4 |
| anytls | 2 |

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
| 77.47 | shadowsocks | 234.3 | 651.6 | 22.35 | 0.0 | 10.0 | 13.94 | 15.18 | Au1rxx-base64 | 37.19.198.244 |
| 77.43 | shadowsocks | 236.2 | 647.5 | 22.31 | 0.0 | 10.0 | 13.94 | 15.18 | Au1rxx-base64 | 198.98.53.130 |
| 77.17 | shadowsocks | 247.4 | 686.3 | 22.05 | 0.0 | 10.0 | 13.94 | 15.18 | Au1rxx-base64 | 37.19.198.243 |
| 76.43 | shadowsocks | 236.3 | 658.7 | 22.31 | 0.0 | 10.0 | 13.94 | 15.18 | Au1rxx-base64 | 37.19.198.160 |
| 74.65 | shadowsocks | 334.8 | 845.9 | 20.03 | 0.0 | 10.0 | 13.94 | 15.18 | Au1rxx-base64 | 185.196.61.82 |
| 74.63 | trojan | 343.8 | 853.2 | 19.82 | 0.0 | 10.0 | 12.73 | 16.44 | DeltaKronecker-all | 64.74.163.118 |
| 74.55 | vmess | 300.9 | 862.7 | 20.81 | 0.0 | 10.0 | 10.0 | 18.24 | Surfboard-tg-mixed | 67.220.95.3 |
| 73.74 | shadowsocks | 278.5 | 647.9 | 21.33 | 0.0 | 10.0 | 13.94 | 15.18 | Au1rxx-base64 | 156.146.38.170 |
| 73.36 | shadowsocks | 282.3 | 789.3 | 21.24 | 0.0 | 10.0 | 13.94 | 15.18 | Au1rxx-base64 | 37.19.198.236 |
| 73.16 | shadowsocks | 317.0 | 760.5 | 20.44 | 0.0 | 10.0 | 13.94 | 15.18 | Au1rxx-base64 | 156.146.38.167 |
| 72.8 | shadowsocks | 414.7 | 1100.1 | 18.18 | 0.0 | 10.0 | 13.94 | 15.18 | Au1rxx-base64 | 68.168.222.210 |
| 72.54 | shadowsocks | 341.8 | 922.7 | 19.86 | 0.0 | 10.0 | 13.94 | 18.24 | Surfboard-tg-mixed | 50.114.177.134 |
| 72.15 | shadowsocks | 314.8 | 689.9 | 20.49 | 0.0 | 10.0 | 13.94 | 15.18 | Au1rxx-base64 | 108.181.57.93 |
| 71.13 | trojan | 369.0 | 870.6 | 19.24 | 0.0 | 10.0 | 12.73 | 15.18 | Au1rxx-base64 | 64.94.95.115 |
| 71.07 | trojan | 371.5 | 874.7 | 19.18 | 0.0 | 10.0 | 12.73 | 15.18 | Au1rxx-base64 | 64.94.95.118 |
| 70.22 | shadowsocks | 312.3 | 583.2 | 20.55 | 0.0 | 10.0 | 13.94 | 15.18 | Au1rxx-base64 | 149.22.95.183 |
| 70.22 | hysteria2 | 355.8 | 693.6 | 19.54 | 0.0 | 10.0 | 12.5 | 15.18 | Au1rxx-base64 | 62.210.124.146 |
| 69.75 | trojan | 466.6 | 811.7 | 16.98 | 0.0 | 10.0 | 12.73 | 18.24 | Surfboard-tg-mixed | 198.62.62.23 |
| 69.7 | trojan | 474.8 | 814.3 | 16.79 | 0.0 | 10.0 | 12.73 | 18.24 | Surfboard-tg-mixed | 104.21.40.34 |
| 69.69 | trojan | 475.9 | 770.7 | 16.76 | 0.0 | 10.0 | 12.73 | 18.24 | Surfboard-tg-mixed | 172.64.146.198 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.976 | 1.0 | 36 | 61 | prefer |
| mheidari-all | 0.96 | 0.882 | 457 | 19618 | prefer |
| Au1rxx-base64 | 0.909 | 0.897 | 136 | 432 | prefer |
| Surfboard-tg-mixed | 0.662 | 0.582 | 194 | 5319 | observe |
| DeltaKronecker-all | 0.591 | 0.511 | 354 | 5559 | observe |
| xiaoji235-airport-v2ray-all | 0.287 | 0.5 | 2 | 3847 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4588 | observe |
| Epodonios-all | 0.255 | None | 0 | 6546 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3974 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6796 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4227 | observe |
| barry-far-vless | 0.255 | None | 0 | 4836 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5027 | observe |
| nscl5-all | 0.255 | None | 0 | 3124 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 133 |
| geo | ClientOSError | - | 41 |
| speed | ClientOSError | - | 38 |
| cn-block | TimeoutError | - | 37 |
| 204 | ProxyError | - | 30 |
| speed | TimeoutError | - | 23 |
| 204 | TimeoutError | - | 8 |
| 204 | ClientOSError | - | 5 |
| cn-block | ClientOSError | - | 4 |
| geo | ProxyError | - | 3 |
| speed | ProxyError | - | 3 |
| cn-block | ProxyError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
