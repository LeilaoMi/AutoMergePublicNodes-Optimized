# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-18 06:59:16 |
| 运行耗时 | 413.2s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 91021 |
| 去重后节点 | 23861 |
| TCP 可达 | 3000 |
| 真实可用 | 1271 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23861 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.8 |
| geo | 1.0 |
| tcp | 36.1 |
| probe | 77.5 |
| real_test | 257.0 |
| generate | 36.7 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 51744 |
| trojan | 17415 |
| shadowsocks | 10460 |
| vmess | 9396 |
| hysteria2 | 1462 |
| http | 186 |
| socks | 148 |
| shadowsocksr | 133 |
| anytls | 44 |
| tuic | 20 |
| hysteria | 13 |

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
| 85.23 | hysteria2 | 221.1 | 524.8 | 22.66 | 0.0 | 10.0 | 14.59 | 18.98 | mheidari-all | 150.241.102.127 |
| 84.66 | trojan | 231.7 | 533.1 | 22.41 | 0.0 | 10.0 | 14.75 | 20.0 | Au1rxx-base64 | 44.243.85.47 |
| 84.55 | trojan | 236.7 | 549.6 | 22.3 | 0.0 | 10.0 | 14.75 | 20.0 | Au1rxx-base64 | 34.217.192.97 |
| 84.38 | trojan | 244.2 | 569.9 | 22.13 | 0.0 | 10.0 | 14.75 | 20.0 | Au1rxx-base64 | 100.22.163.167 |
| 84.33 | trojan | 246.1 | 570.9 | 22.08 | 0.0 | 10.0 | 14.75 | 20.0 | Au1rxx-base64 | 34.221.30.108 |
| 84.26 | trojan | 249.2 | 583.5 | 22.01 | 0.0 | 10.0 | 14.75 | 20.0 | Au1rxx-base64 | 35.88.120.18 |
| 84.2 | trojan | 186.2 | 487.0 | 23.47 | 0.0 | 10.0 | 14.75 | 18.98 | mheidari-all | 14.1.28.76 |
| 83.41 | trojan | 241.9 | 564.0 | 22.18 | 0.0 | 10.0 | 14.75 | 18.98 | mheidari-all | 54.185.164.73 |
| 83.35 | trojan | 288.6 | 701.6 | 21.1 | 0.0 | 10.0 | 14.75 | 20.0 | Au1rxx-base64 | 44.251.158.80 |
| 83.34 | trojan | 244.9 | 569.8 | 22.11 | 0.0 | 10.0 | 14.75 | 18.98 | mheidari-all | 54.188.176.255 |
| 82.95 | trojan | 232.9 | 534.9 | 22.39 | 0.0 | 10.0 | 14.75 | 18.98 | mheidari-all | 54.244.169.225 |
| 82.86 | trojan | 222.4 | 504.4 | 22.63 | 0.0 | 10.0 | 14.75 | 18.98 | mheidari-all | 35.160.249.189 |
| 82.39 | trojan | 241.1 | 557.2 | 22.2 | 0.0 | 10.0 | 14.75 | 18.98 | mheidari-all | 34.220.224.252 |
| 82.31 | trojan | 289.2 | 703.2 | 21.08 | 0.0 | 10.0 | 14.75 | 18.98 | mheidari-all | 54.245.126.186 |
| 82.2 | shadowsocks | 217.5 | 519.3 | 22.74 | 0.0 | 10.0 | 14.48 | 18.98 | mheidari-all | 173.244.56.6 |
| 82.11 | trojan | 298.2 | 689.8 | 20.88 | 0.0 | 10.0 | 14.75 | 18.98 | mheidari-all | 44.247.89.62 |
| 81.75 | trojan | 248.6 | 586.9 | 22.02 | 0.0 | 10.0 | 14.75 | 20.0 | Au1rxx-base64 | 35.92.245.6 |
| 81.14 | shadowsocks | 263.6 | 622.7 | 21.68 | 0.0 | 10.0 | 14.48 | 18.98 | mheidari-all | 173.244.56.9 |
| 80.84 | trojan | 303.7 | 748.5 | 20.75 | 0.0 | 10.0 | 14.75 | 18.98 | mheidari-all | 35.90.27.143 |
| 80.58 | trojan | 274.2 | 662.4 | 21.43 | 0.0 | 10.0 | 14.75 | 18.98 | mheidari-all | 35.91.98.35 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.999 | 1.0 | 127 | 159 | prefer |
| Surfboard-tg-mixed | 0.934 | 0.859 | 135 | 6138 | prefer |
| Au1rxx-base64 | 0.896 | 0.84 | 814 | 1408 | prefer |
| mheidari-all | 0.705 | 0.625 | 539 | 21284 | prefer |
| nscl5-all | 0.4 | 0.75 | 4 | 2992 | observe |
| DeltaKronecker-all | 0.344 | 0.333 | 12 | 5725 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5068 | observe |
| Epodonios-all | 0.255 | None | 0 | 6730 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3986 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6856 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4777 | observe |
| barry-far-vless | 0.255 | None | 0 | 5074 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4045 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.231 | None | 0 | 1408 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 111 |
| speed | TimeoutError | - | 93 |
| geo | ClientOSError | - | 61 |
| 204 | TimeoutError | - | 29 |
| speed | ClientOSError | - | 28 |
| cn-block | TimeoutError | - | 24 |
| 204 | ClientOSError | - | 6 |
| cn-block | ClientOSError | - | 5 |
| cn-block | ProxyError | - | 2 |
| speed | ProxyError | - | 2 |
| 204 | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
