# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-23 01:48:54 |
| 运行耗时 | 324.3s |
| 订阅源总数 | 107 |
| 健康订阅源 | 99 |
| 原始节点 | 83081 |
| 去重后节点 | 23824 |
| TCP 可达 | 3000 |
| 真实可用 | 848 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23824 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 11.7 |
| geo | 1.4 |
| tcp | 41.3 |
| probe | 59.3 |
| real_test | 179.2 |
| generate | 31.4 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 49774 |
| trojan | 10633 |
| shadowsocks | 10372 |
| vmess | 10337 |
| hysteria2 | 1479 |
| shadowsocksr | 174 |
| http | 167 |
| socks | 115 |
| anytls | 16 |
| hysteria | 11 |
| tuic | 3 |

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
| 83.5 | trojan | 247.1 | 606.3 | 22.06 | 0.0 | 10.0 | 14.45 | 20.0 | Au1rxx-base64 | 64.94.95.117 |
| 83.44 | trojan | 250.1 | 603.4 | 21.99 | 0.0 | 10.0 | 14.45 | 20.0 | Au1rxx-base64 | 64.94.95.114 |
| 83.42 | trojan | 250.9 | 610.6 | 21.97 | 0.0 | 10.0 | 14.45 | 20.0 | Au1rxx-base64 | 64.94.95.115 |
| 82.5 | trojan | 247.5 | 605.5 | 22.05 | 0.0 | 10.0 | 14.45 | 20.0 | Au1rxx-base64 | 64.94.95.118 |
| 82.22 | http | 252.9 | 572.9 | 21.92 | 0.0 | 10.0 | 14.87 | 19.94 | zhangkai | 138.199.35.198 |
| 82.16 | shadowsocks | 237.0 | 607.6 | 22.29 | 0.0 | 10.0 | 13.87 | 20.0 | Au1rxx-base64 | 156.146.38.167 |
| 82.16 | shadowsocks | 237.1 | 608.4 | 22.29 | 0.0 | 10.0 | 13.87 | 20.0 | Au1rxx-base64 | 156.146.38.168 |
| 81.99 | vless | 265.7 | 600.5 | 21.63 | 0.0 | 10.0 | 11.54 | 20.0 | Au1rxx-base64 | 15.204.97.216 |
| 81.81 | vless | 267.0 | 603.0 | 21.6 | 0.0 | 10.0 | 11.54 | 20.0 | Au1rxx-base64 | 15.204.97.197 |
| 81.8 | vless | 265.1 | 598.6 | 21.64 | 0.0 | 10.0 | 11.54 | 20.0 | Au1rxx-base64 | 15.204.97.209 |
| 81.53 | http | 240.3 | 534.2 | 22.22 | 0.0 | 10.0 | 14.87 | 19.94 | zhangkai | 138.199.35.216 |
| 81.23 | vless | 347.1 | 892.5 | 19.74 | 0.0 | 10.0 | 11.54 | 20.0 | Au1rxx-base64 | 38.180.242.205 |
| 79.82 | shadowsocks | 273.1 | 653.6 | 21.46 | 0.0 | 10.0 | 13.87 | 20.0 | Au1rxx-base64 | 94.72.127.55 |
| 79.13 | shadowsocks | 283.1 | 579.5 | 21.22 | 0.0 | 9.42 | 13.87 | 20.0 | Au1rxx-base64 | 154.12.242.150 |
| 79.11 | shadowsocks | 266.1 | 620.2 | 21.62 | 0.0 | 10.0 | 13.87 | 20.0 | Au1rxx-base64 | 154.53.60.212 |
| 78.86 | shadowsocks | 271.3 | 623.3 | 21.5 | 0.0 | 9.42 | 13.87 | 20.0 | Au1rxx-base64 | 94.72.127.58 |
| 78.83 | vless | 304.8 | 676.1 | 20.72 | 0.0 | 10.0 | 11.54 | 20.0 | Au1rxx-base64 | 70.39.198.183 |
| 78.8 | trojan | 288.4 | 594.9 | 21.1 | 0.0 | 9.43 | 14.45 | 20.0 | Au1rxx-base64 | 35.160.249.189 |
| 78.77 | trojan | 296.6 | 593.8 | 20.91 | 0.0 | 10.0 | 14.45 | 20.0 | Au1rxx-base64 | 44.251.158.80 |
| 78.76 | trojan | 299.3 | 627.3 | 20.85 | 0.0 | 10.0 | 14.45 | 20.0 | Au1rxx-base64 | 35.92.245.6 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | 0.938 | 513 | 1658 | prefer |
| zhangkai | 0.997 | 1.0 | 113 | 144 | prefer |
| Surfboard-tg-mixed | 0.931 | 0.855 | 173 | 6297 | prefer |
| mheidari-all | 0.619 | 0.54 | 163 | 14498 | observe |
| nscl5-all | 0.355 | 1.0 | 2 | 1082 | observe |
| tg-oneclickvpnkeys | 0.317 | 1.0 | 2 | 146 | observe |
| xiaoji235-airport-v2ray-all | 0.287 | 0.5 | 2 | 5974 | observe |
| Epodonios-all | 0.255 | None | 0 | 6920 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3986 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7010 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5114 | observe |
| barry-far-vless | 0.255 | None | 0 | 5496 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4074 | observe |
| DeltaKronecker-all | 0.243 | 0.155 | 84 | 5015 | downweight |
| Au1rxx-clash | 0.241 | None | 0 | 1660 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 91 |
| speed | TimeoutError | - | 44 |
| geo | ClientOSError | - | 26 |
| cn-block | TimeoutError | - | 18 |
| speed | ClientOSError | - | 15 |
| 204 | TimeoutError | - | 5 |
| cn-block | ClientOSError | - | 3 |
| geo | ProxyError | - | 2 |
| 204 | ClientOSError | - | 2 |
| cn-block | ProxyError | - | 1 |
| speed | ProxyError | - | 1 |
| 204 | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
