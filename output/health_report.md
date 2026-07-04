# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-04 08:48:19 |
| 运行耗时 | 200.1s |
| 订阅源总数 | 107 |
| 健康订阅源 | 103 |
| 原始节点 | 78924 |
| 去重后节点 | 23515 |
| TCP 可达 | 3000 |
| 真实可用 | 350 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23515 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.8 |
| geo | 1.4 |
| tcp | 30.9 |
| probe | 44.8 |
| real_test | 88.5 |
| generate | 29.7 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 45836 |
| trojan | 12741 |
| vmess | 10499 |
| shadowsocks | 9178 |
| hysteria2 | 285 |
| shadowsocksr | 151 |
| http | 135 |
| socks | 91 |
| hysteria | 6 |
| tuic | 1 |
| anytls | 1 |

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
| 78.92 | trojan | 251.3 | 629.9 | 21.96 | 0.0 | 10.0 | 13.58 | 16.38 | DeltaKronecker-all | 64.94.95.117 |
| 78.78 | shadowsocks | 228.4 | 603.3 | 22.49 | 0.0 | 10.0 | 13.31 | 16.98 | Au1rxx-base64 | 156.146.38.169 |
| 78.66 | trojan | 252.1 | 572.8 | 21.94 | 0.0 | 10.0 | 13.58 | 17.28 | mheidari-all | 64.94.95.118 |
| 78.53 | trojan | 268.3 | 649.3 | 21.57 | 0.0 | 10.0 | 13.58 | 16.38 | DeltaKronecker-all | 64.94.95.115 |
| 78.49 | shadowsocks | 241.0 | 592.9 | 22.2 | 0.0 | 10.0 | 13.31 | 16.98 | Au1rxx-base64 | 156.146.38.170 |
| 78.37 | shadowsocks | 246.0 | 605.8 | 22.08 | 0.0 | 10.0 | 13.31 | 16.98 | Au1rxx-base64 | 156.146.38.167 |
| 78.16 | trojan | 284.2 | 552.6 | 21.2 | 0.0 | 10.0 | 13.58 | 16.38 | DeltaKronecker-all | 64.94.95.114 |
| 76.43 | shadowsocks | 286.7 | 722.6 | 21.14 | 0.0 | 10.0 | 13.31 | 16.98 | Au1rxx-base64 | 156.146.38.168 |
| 76.24 | shadowsocks | 280.4 | 680.5 | 21.29 | 0.0 | 10.0 | 13.31 | 16.98 | Au1rxx-base64 | 37.19.198.236 |
| 74.33 | shadowsocks | 336.7 | 830.1 | 19.98 | 0.0 | 10.0 | 13.31 | 16.98 | Au1rxx-base64 | 37.19.198.160 |
| 73.94 | trojan | 272.2 | 718.9 | 21.48 | 0.0 | 10.0 | 13.58 | 16.38 | DeltaKronecker-all | 149.28.241.235 |
| 73.87 | trojan | 275.2 | 722.0 | 21.41 | 0.0 | 10.0 | 13.58 | 16.38 | DeltaKronecker-all | 45.32.195.168 |
| 73.82 | shadowsocks | 302.8 | 662.8 | 20.77 | 0.0 | 10.0 | 13.31 | 17.28 | mheidari-all | 198.98.53.130 |
| 73.21 | shadowsocks | 380.1 | 935.5 | 18.98 | 0.0 | 10.0 | 13.31 | 17.28 | mheidari-all | 108.181.57.93 |
| 72.81 | shadowsocks | 283.5 | 676.7 | 21.21 | 0.0 | 10.0 | 13.31 | 16.98 | Au1rxx-base64 | 37.19.198.244 |
| 72.29 | trojan | 343.4 | 929.8 | 19.83 | 0.0 | 10.0 | 13.58 | 16.38 | DeltaKronecker-all | 45.32.198.247 |
| 71.57 | shadowsocks | 279.3 | 614.1 | 21.31 | 0.0 | 10.0 | 13.31 | 16.98 | Au1rxx-base64 | 173.244.56.9 |
| 71.15 | shadowsocks | 324.6 | 653.5 | 20.26 | 0.0 | 10.0 | 13.31 | 16.98 | Au1rxx-base64 | 108.181.0.177 |
| 71.12 | shadowsocks | 306.1 | 631.6 | 20.69 | 0.0 | 10.0 | 13.31 | 16.98 | Au1rxx-base64 | 149.22.95.183 |
| 70.2 | shadowsocks | 366.3 | 803.5 | 19.3 | 0.0 | 10.0 | 13.31 | 16.98 | Au1rxx-base64 | 108.181.118.10 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| Au1rxx-base64 | 0.836 | 0.864 | 22 | 77 | prefer |
| Surfboard-tg-mixed | 0.83 | 0.754 | 114 | 6152 | prefer |
| DeltaKronecker-all | 0.804 | 0.726 | 201 | 7309 | prefer |
| mheidari-all | 0.747 | 0.67 | 88 | 16136 | prefer |
| nscl5-all | 0.359 | 1.0 | 2 | 1189 | observe |
| Surfboard-tg-vless | 0.335 | 1.0 | 1 | 4573 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4579 | observe |
| Epodonios-all | 0.255 | None | 0 | 7154 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3973 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7126 | observe |
| barry-far-vless | 0.255 | None | 0 | 5278 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5333 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| xiaoji235-airport-v2ray-all | 0.226 | None | 0 | 1263 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | ProxyError | - | 36 |
| geo | TimeoutError | - | 17 |
| 204 | ClientOSError | - | 14 |
| speed | ClientOSError | - | 11 |
| speed | ProxyError | - | 8 |
| cn-block | ClientOSError | - | 7 |
| cn-block | ProxyError | - | 6 |
| 204 | TimeoutError | - | 6 |
| cn-block | TimeoutError | - | 4 |
| geo | ClientOSError | - | 4 |
| geo | ProxyError | - | 3 |
| speed | TimeoutError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
