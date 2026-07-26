# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-26 03:35:50 |
| 运行耗时 | 318.4s |
| 订阅源总数 | 107 |
| 健康订阅源 | 102 |
| 原始节点 | 80527 |
| 去重后节点 | 22461 |
| TCP 可达 | 3000 |
| 真实可用 | 913 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22461 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 3.9 |
| geo | 1.5 |
| tcp | 31.1 |
| probe | 69.1 |
| real_test | 192.8 |
| generate | 20.1 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 45075 |
| trojan | 14615 |
| vmess | 10121 |
| shadowsocks | 9979 |
| hysteria2 | 475 |
| http | 81 |
| shadowsocksr | 79 |
| socks | 77 |
| hysteria | 13 |
| tuic | 11 |
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
| 77.9 | shadowsocks | 195.1 | 480.4 | 23.26 | 0.0 | 10.0 | 10.98 | 18.16 | Au1rxx-base64 | 108.181.118.10 |
| 77.76 | shadowsocks | 201.3 | 487.8 | 23.12 | 0.0 | 10.0 | 10.98 | 18.16 | Au1rxx-base64 | 108.181.0.177 |
| 76.22 | shadowsocks | 246.1 | 597.8 | 22.08 | 0.0 | 10.0 | 10.98 | 18.16 | Au1rxx-base64 | 149.22.95.183 |
| 74.82 | shadowsocks | 207.0 | 527.2 | 22.99 | 0.0 | 10.0 | 10.98 | 18.16 | Au1rxx-base64 | 173.244.56.6 |
| 74.81 | trojan | 328.5 | 325.3 | 20.17 | 2.8 | 9.95 | 13.64 | 18.16 | Au1rxx-base64 | 95.85.94.199 |
| 74.67 | trojan | 325.1 | 331.8 | 20.25 | 2.56 | 9.95 | 13.64 | 18.16 | Au1rxx-base64 | 31.223.184.164 |
| 74.5 | trojan | 327.1 | 331.6 | 20.21 | 2.56 | 9.87 | 13.64 | 18.16 | Au1rxx-base64 | 95.85.94.96 |
| 74.5 | trojan | 330.6 | 333.4 | 20.13 | 2.5 | 9.95 | 13.64 | 18.16 | Au1rxx-base64 | 95.85.94.148 |
| 74.49 | trojan | 325.6 | 336.0 | 20.24 | 2.4 | 9.94 | 13.64 | 18.16 | Au1rxx-base64 | 95.85.94.165 |
| 74.39 | trojan | 328.4 | 335.7 | 20.18 | 2.41 | 9.94 | 13.64 | 18.16 | Au1rxx-base64 | 95.85.94.90 |
| 74.29 | trojan | 325.7 | 333.4 | 20.24 | 2.5 | 9.66 | 13.64 | 18.16 | Au1rxx-base64 | moved-osprey.rooster465.autos |
| 74.21 | trojan | 329.0 | 340.7 | 20.16 | 2.22 | 9.95 | 13.64 | 18.16 | Au1rxx-base64 | 31.223.184.238 |
| 74.19 | trojan | 325.8 | 332.5 | 20.24 | 2.53 | 9.65 | 13.64 | 18.16 | Au1rxx-base64 | wise-longhorn.rooster465.autos |
| 74.07 | trojan | 336.2 | 674.0 | 19.99 | 0.0 | 10.0 | 13.64 | 18.16 | Au1rxx-base64 | 163.245.196.68 |
| 73.74 | shadowsocks | 180.4 | 472.0 | 23.6 | 0.0 | 10.0 | 10.98 | 18.16 | Au1rxx-base64 | 216.105.168.19 |
| 73.6 | trojan | 325.4 | 329.8 | 20.25 | 2.63 | 9.85 | 13.64 | 18.16 | Au1rxx-base64 | 95.85.94.185 |
| 73.55 | shadowsocks | 291.8 | 661.6 | 21.02 | 0.0 | 10.0 | 10.98 | 18.16 | Au1rxx-base64 | 156.146.38.170 |
| 73.43 | trojan | 335.9 | 355.2 | 20.0 | 1.68 | 9.93 | 13.64 | 18.16 | Au1rxx-base64 | 31.223.184.172 |
| 73.23 | shadowsocks | 289.5 | 642.7 | 21.08 | 0.0 | 10.0 | 10.98 | 18.16 | Au1rxx-base64 | 156.146.38.168 |
| 73.11 | shadowsocks | 207.6 | 524.0 | 22.97 | 0.0 | 10.0 | 10.98 | 18.16 | Au1rxx-base64 | 173.244.56.9 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.992 | 1.0 | 76 | 119 | prefer |
| Au1rxx-base64 | 0.94 | 0.888 | 489 | 1341 | prefer |
| Surfboard-tg-mixed | 0.899 | 0.829 | 70 | 5462 | prefer |
| DeltaKronecker-all | 0.714 | 0.635 | 230 | 5838 | prefer |
| mheidari-all | 0.604 | 0.524 | 376 | 17224 | observe |
| xiaoji235-airport-v2ray-all | 0.272 | 0.5 | 2 | 1624 | observe |
| tg-ConfigV2rayNG | 0.263 | 1.0 | 1 | 200 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4879 | observe |
| Epodonios-all | 0.255 | None | 0 | 6569 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3970 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6505 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4196 | observe |
| barry-far-vless | 0.255 | None | 0 | 4852 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4980 | observe |
| nscl5-all | 0.255 | None | 0 | 2896 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 101 |
| speed | ClientOSError | - | 100 |
| speed | TimeoutError | - | 39 |
| cn-block | TimeoutError | - | 38 |
| geo | ClientOSError | - | 27 |
| 204 | ProxyError | - | 9 |
| 204 | TimeoutError | - | 7 |
| cn-block | ClientOSError | - | 7 |
| 204 | ClientOSError | - | 6 |
| cn-block | ProxyError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
