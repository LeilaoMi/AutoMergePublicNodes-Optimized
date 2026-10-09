# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-09 22:39:51 |
| 运行耗时 | 678.1s |
| 订阅源总数 | 107 |
| 健康订阅源 | 94 |
| 原始节点 | 97854 |
| 去重后节点 | 27601 |
| TCP 可达 | 3000 |
| 真实可用 | 441 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 27601 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 8.0 |
| geo | 1.5 |
| tcp | 46.8 |
| probe | 251.9 |
| real_test | 293.2 |
| generate | 76.7 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 57405 |
| vmess | 15656 |
| shadowsocks | 11874 |
| trojan | 10602 |
| hysteria2 | 1499 |
| http | 506 |
| shadowsocksr | 173 |
| socks | 79 |
| anytls | 30 |
| hysteria | 17 |
| tuic | 13 |

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
| 80.09 | hysteria2 | 279.1 | 715.9 | 21.32 | 0.0 | 10.0 | 10.59 | 19.68 | Au1rxx-base64 | 129.213.91.185 |
| 79.48 | shadowsocks | 255.2 | 631.8 | 21.87 | 0.0 | 10.0 | 11.93 | 19.68 | Au1rxx-base64 | 156.146.38.167 |
| 79.39 | shadowsocks | 259.3 | 638.4 | 21.78 | 0.0 | 10.0 | 11.93 | 19.68 | Au1rxx-base64 | 156.146.38.168 |
| 76.93 | vless | 292.5 | 579.9 | 21.01 | 0.0 | 10.0 | 10.12 | 19.68 | Au1rxx-base64 | 107.173.237.146 |
| 76.88 | vless | 272.5 | 556.1 | 21.47 | 0.0 | 10.0 | 10.12 | 19.68 | Au1rxx-base64 | 47.251.108.158 |
| 76.78 | vless | 328.6 | 770.4 | 20.17 | 0.0 | 10.0 | 10.12 | 19.68 | Au1rxx-base64 | 167.17.69.171 |
| 76.7 | hysteria2 | 302.2 | 295.3 | 20.78 | 3.93 | 9.6 | 10.59 | 19.68 | Au1rxx-base64 | 158.101.148.79 |
| 76.59 | vless | 356.3 | 740.0 | 19.53 | 0.0 | 10.0 | 10.12 | 19.68 | Au1rxx-base64 | 169.40.42.184 |
| 76.51 | vless | 323.7 | 734.6 | 20.28 | 0.0 | 10.0 | 10.12 | 19.68 | Au1rxx-base64 | 66.70.179.198 |
| 76.27 | vless | 359.2 | 668.6 | 19.46 | 0.0 | 10.0 | 10.12 | 19.68 | Au1rxx-base64 | 169.40.42.89 |
| 75.91 | shadowsocks | 309.9 | 757.4 | 20.6 | 0.0 | 10.0 | 11.93 | 19.68 | Au1rxx-base64 | 37.19.198.243 |
| 75.88 | shadowsocks | 308.4 | 758.0 | 20.64 | 0.0 | 10.0 | 11.93 | 19.68 | Au1rxx-base64 | 37.19.198.160 |
| 75.83 | shadowsocks | 302.1 | 690.0 | 20.79 | 0.0 | 10.0 | 11.93 | 19.68 | Au1rxx-base64 | 140.82.63.79 |
| 75.67 | vless | 391.5 | 933.6 | 18.71 | 0.0 | 10.0 | 10.12 | 19.68 | Au1rxx-base64 | 169.40.42.231 |
| 75.47 | vless | 329.9 | 708.4 | 20.14 | 0.0 | 10.0 | 10.12 | 19.68 | Au1rxx-base64 | 144.202.126.147 |
| 75.47 | vless | 399.8 | 886.9 | 18.52 | 0.0 | 10.0 | 10.12 | 19.68 | Au1rxx-base64 | 169.40.42.90 |
| 75.32 | vless | 352.3 | 811.8 | 19.62 | 0.0 | 10.0 | 10.12 | 19.68 | Au1rxx-base64 | 169.40.42.202 |
| 75.23 | vless | 317.5 | 625.3 | 20.43 | 0.0 | 10.0 | 10.12 | 19.68 | Au1rxx-base64 | 195.123.240.65 |
| 75.22 | vless | 387.6 | 827.3 | 18.81 | 0.0 | 10.0 | 10.12 | 19.68 | Au1rxx-base64 | 169.40.42.182 |
| 75.19 | vless | 333.8 | 660.8 | 20.05 | 0.0 | 10.0 | 10.12 | 19.68 | Au1rxx-base64 | 15.204.97.216 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.983 | 0.913 | 367 | 1805 | prefer |
| zhangkai | 0.962 | 1.0 | 21 | 144 | prefer |
| mheidari-all | 0.88 | 0.809 | 68 | 23076 | prefer |
| Surfboard-tg-mixed | 0.783 | 0.714 | 35 | 7025 | prefer |
| DeltaKronecker-all | 0.259 | 0.333 | 3 | 5154 | observe |
| tg-OutlineReleasedKey | 0.257 | 1.0 | 1 | 52 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4984 | observe |
| Epodonios-all | 0.255 | None | 0 | 7582 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9986 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5553 | observe |
| barry-far-vless | 0.255 | None | 0 | 5812 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4346 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |
| Au1rxx-clash | 0.247 | None | 0 | 1805 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| cn-block | TimeoutError | - | 20 |
| speed | ClientOSError | - | 10 |
| 204 | ProxyError | - | 9 |
| geo | TimeoutError | - | 7 |
| 204 | TimeoutError | - | 7 |
| speed | TimeoutError | - | 5 |
| cn-block | ClientOSError | - | 4 |
| geo | ClientOSError | - | 3 |
| cn-block | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
