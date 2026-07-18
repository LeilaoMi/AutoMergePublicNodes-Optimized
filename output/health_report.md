# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-18 19:18:07 |
| 运行耗时 | 374.2s |
| 订阅源总数 | 107 |
| 健康订阅源 | 99 |
| 原始节点 | 88346 |
| 去重后节点 | 23115 |
| TCP 可达 | 3000 |
| 真实可用 | 839 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23115 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.3 |
| geo | 0.8 |
| tcp | 32.6 |
| probe | 74.2 |
| real_test | 221.9 |
| generate | 37.4 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 52162 |
| trojan | 14267 |
| vmess | 10780 |
| shadowsocks | 10547 |
| hysteria2 | 322 |
| shadowsocksr | 126 |
| socks | 64 |
| http | 55 |
| hysteria | 14 |
| tuic | 7 |
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
| 78.51 | shadowsocks | 242.1 | 652.0 | 22.17 | 0.0 | 10.0 | 13.18 | 17.66 | mheidari-all | 108.181.57.93 |
| 78.29 | shadowsocks | 251.6 | 660.0 | 21.95 | 0.0 | 10.0 | 13.18 | 17.66 | mheidari-all | 68.168.222.210 |
| 76.63 | shadowsocks | 233.1 | 637.4 | 22.38 | 0.0 | 8.39 | 13.18 | 16.68 | Au1rxx-base64 | 37.19.198.160 |
| 76.58 | shadowsocks | 235.5 | 645.7 | 22.33 | 0.0 | 8.39 | 13.18 | 16.68 | Au1rxx-base64 | 37.19.198.243 |
| 76.56 | shadowsocks | 237.1 | 654.7 | 22.29 | 0.0 | 8.41 | 13.18 | 16.68 | Au1rxx-base64 | 37.19.198.244 |
| 75.7 | shadowsocks | 350.0 | 913.1 | 19.67 | 0.0 | 10.0 | 13.18 | 17.66 | mheidari-all | 50.114.177.235 |
| 75.18 | shadowsocks | 338.5 | 839.7 | 19.94 | 0.0 | 10.0 | 13.18 | 17.66 | mheidari-all | 185.196.61.82 |
| 73.08 | shadowsocks | 280.8 | 642.6 | 21.28 | 0.0 | 8.36 | 13.18 | 16.68 | Au1rxx-base64 | 156.146.38.167 |
| 72.79 | shadowsocks | 284.1 | 655.0 | 21.2 | 0.0 | 8.35 | 13.18 | 16.68 | Au1rxx-base64 | 156.146.38.170 |
| 72.28 | shadowsocks | 286.1 | 659.7 | 21.16 | 0.0 | 8.36 | 13.18 | 16.68 | Au1rxx-base64 | 156.146.38.169 |
| 72.07 | shadowsocks | 229.2 | 616.3 | 22.47 | 0.0 | 10.0 | 13.18 | 17.66 | mheidari-all | 147.90.234.133 |
| 71.37 | shadowsocks | 330.8 | 793.8 | 20.12 | 0.0 | 8.35 | 13.18 | 16.68 | Au1rxx-base64 | 156.146.38.168 |
| 70.4 | trojan | 444.5 | 791.7 | 17.49 | 0.0 | 10.0 | 13.22 | 17.66 | mheidari-all | 45.130.125.76 |
| 70.16 | shadowsocks | 231.1 | 596.5 | 22.43 | 0.0 | 10.0 | 13.18 | 17.66 | mheidari-all | 198.98.53.130 |
| 69.5 | trojan | 457.8 | 755.1 | 17.18 | 0.0 | 10.0 | 13.22 | 17.66 | mheidari-all | 212.183.88.136 |
| 69.06 | hysteria2 | 402.8 | 832.8 | 18.45 | 0.0 | 8.41 | 12.0 | 16.68 | Au1rxx-base64 | 62.210.124.146 |
| 69.03 | shadowsocks | 319.4 | 561.4 | 20.39 | 0.0 | 8.35 | 13.18 | 16.68 | Au1rxx-base64 | 173.244.56.6 |
| 68.92 | shadowsocks | 315.1 | 560.3 | 20.48 | 0.0 | 8.34 | 13.18 | 16.68 | Au1rxx-base64 | 108.181.0.177 |
| 68.89 | trojan | 445.3 | 1079.9 | 17.47 | 0.0 | 10.0 | 13.22 | 14.6 | DeltaKronecker-all | 64.94.95.117 |
| 68.86 | vless | 250.2 | 689.8 | 21.99 | 0.0 | 10.0 | 4.21 | 17.66 | mheidari-all | 47.89.186.170 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.976 | 1.0 | 36 | 61 | prefer |
| Au1rxx-base64 | 0.917 | 0.917 | 121 | 150 | prefer |
| Surfboard-tg-mixed | 0.869 | 0.793 | 140 | 5696 | prefer |
| mheidari-all | 0.743 | 0.664 | 776 | 19946 | prefer |
| DeltaKronecker-all | 0.44 | 0.358 | 173 | 9946 | observe |
| xiaoji235-airport-v2ray-all | 0.349 | 0.667 | 3 | 4321 | observe |
| Barabama-yudou | 0.318 | 1.0 | 2 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4371 | observe |
| Epodonios-all | 0.255 | None | 0 | 6883 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3975 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7250 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4374 | observe |
| barry-far-vless | 0.255 | None | 0 | 4962 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5340 | observe |
| nscl5-all | 0.254 | None | 0 | 1976 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 180 |
| speed | ClientOSError | - | 101 |
| geo | ClientOSError | - | 53 |
| cn-block | TimeoutError | - | 34 |
| 204 | TimeoutError | - | 21 |
| cn-block | ClientOSError | - | 8 |
| speed | TimeoutError | - | 6 |
| 204 | ClientOSError | - | 4 |
| cn-block | ProxyError | - | 3 |
| 204 | ProxyError | - | 3 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
