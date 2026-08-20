# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-20 13:04:34 |
| 运行耗时 | 358.5s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 94317 |
| 去重后节点 | 25202 |
| TCP 可达 | 3000 |
| 真实可用 | 1105 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 25202 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.7 |
| geo | 0.6 |
| tcp | 37.0 |
| probe | 62.8 |
| real_test | 211.9 |
| generate | 38.5 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 52876 |
| trojan | 18383 |
| shadowsocks | 10619 |
| vmess | 10198 |
| hysteria2 | 1682 |
| shadowsocksr | 202 |
| http | 164 |
| socks | 134 |
| anytls | 32 |
| hysteria | 15 |
| tuic | 12 |

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
| 84.62 | trojan | 233.8 | 535.0 | 22.37 | 0.0 | 10.0 | 14.75 | 20.0 | Au1rxx-base64 | 35.88.120.18 |
| 84.59 | trojan | 234.9 | 538.1 | 22.34 | 0.0 | 10.0 | 14.75 | 20.0 | Au1rxx-base64 | 54.213.46.211 |
| 84.58 | trojan | 235.4 | 534.8 | 22.33 | 0.0 | 10.0 | 14.75 | 20.0 | Au1rxx-base64 | 35.160.249.189 |
| 84.57 | trojan | 235.6 | 545.6 | 22.32 | 0.0 | 10.0 | 14.75 | 20.0 | Au1rxx-base64 | 35.92.245.6 |
| 84.53 | trojan | 237.5 | 550.7 | 22.28 | 0.0 | 10.0 | 14.75 | 20.0 | Au1rxx-base64 | 34.210.213.17 |
| 84.45 | trojan | 240.8 | 557.5 | 22.2 | 0.0 | 10.0 | 14.75 | 20.0 | Au1rxx-base64 | 34.220.224.252 |
| 84.2 | trojan | 197.5 | 511.1 | 23.21 | 0.0 | 10.0 | 14.75 | 19.24 | mheidari-all | 14.1.28.76 |
| 84.04 | http | 196.4 | 506.9 | 23.23 | 0.0 | 10.0 | 14.87 | 19.94 | zhangkai | 138.199.35.216 |
| 83.97 | trojan | 261.6 | 622.2 | 21.72 | 0.0 | 10.0 | 14.75 | 20.0 | Au1rxx-base64 | 44.247.89.62 |
| 83.94 | http | 201.0 | 522.5 | 23.13 | 0.0 | 10.0 | 14.87 | 19.94 | zhangkai | 138.199.35.198 |
| 83.84 | trojan | 267.4 | 642.1 | 21.59 | 0.0 | 10.0 | 14.75 | 20.0 | Au1rxx-base64 | 35.91.138.234 |
| 83.56 | trojan | 246.6 | 569.2 | 22.07 | 0.0 | 10.0 | 14.75 | 19.24 | mheidari-all | 35.90.27.143 |
| 83.53 | trojan | 247.8 | 577.1 | 22.04 | 0.0 | 10.0 | 14.75 | 19.24 | mheidari-all | 54.188.176.255 |
| 83.29 | trojan | 243.4 | 560.6 | 22.14 | 0.0 | 10.0 | 14.75 | 19.24 | mheidari-all | 35.91.98.35 |
| 83.15 | trojan | 296.1 | 724.9 | 20.92 | 0.0 | 10.0 | 14.75 | 20.0 | Au1rxx-base64 | 34.221.30.108 |
| 83.04 | trojan | 290.8 | 709.5 | 21.05 | 0.0 | 10.0 | 14.75 | 20.0 | Au1rxx-base64 | 100.22.163.167 |
| 82.97 | trojan | 243.4 | 546.4 | 22.14 | 0.0 | 10.0 | 14.75 | 19.24 | mheidari-all | 54.244.169.225 |
| 82.8 | trojan | 238.8 | 552.7 | 22.25 | 0.0 | 10.0 | 14.75 | 19.24 | mheidari-all | 35.88.210.26 |
| 82.52 | trojan | 251.5 | 591.0 | 21.96 | 0.0 | 10.0 | 14.75 | 19.24 | mheidari-all | 44.246.163.102 |
| 82.39 | hysteria2 | 249.3 | 604.6 | 22.01 | 0.0 | 10.0 | 12.14 | 19.24 | mheidari-all | 150.241.102.127 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | 0.973 | 565 | 1789 | prefer |
| zhangkai | 0.988 | 0.991 | 112 | 144 | prefer |
| Surfboard-tg-mixed | 0.957 | 0.886 | 79 | 6453 | prefer |
| mheidari-all | 0.871 | 0.792 | 471 | 21209 | prefer |
| DeltaKronecker-all | 0.287 | 0.5 | 2 | 6781 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4958 | observe |
| Epodonios-all | 0.255 | None | 0 | 7150 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3987 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7279 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5135 | observe |
| barry-far-vless | 0.255 | None | 0 | 5460 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4586 | observe |
| nscl5-all | 0.255 | None | 0 | 2418 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 5974 | observe |
| Au1rxx-clash | 0.247 | None | 0 | 1789 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | ClientOSError | - | 40 |
| geo | TimeoutError | - | 23 |
| 204 | TimeoutError | - | 18 |
| cn-block | TimeoutError | - | 14 |
| speed | TimeoutError | - | 9 |
| cn-block | ClientOSError | - | 8 |
| speed | ClientOSError | - | 5 |
| 204 | ProxyError | - | 3 |
| 204 | ClientOSError | - | 3 |
| cn-block | ProxyError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
