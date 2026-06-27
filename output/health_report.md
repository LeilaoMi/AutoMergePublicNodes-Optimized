# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-06-27 08:47:54 |
| 运行耗时 | 244.4s |
| 订阅源总数 | 107 |
| 健康订阅源 | 105 |
| 原始节点 | 77212 |
| 去重后节点 | 22994 |
| TCP 可达 | 3000 |
| 真实可用 | 440 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22994 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.3 |
| geo | 1.5 |
| tcp | 30.5 |
| probe | 55.0 |
| real_test | 114.1 |
| generate | 38.0 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 43314 |
| trojan | 12533 |
| vmess | 11339 |
| shadowsocks | 9466 |
| hysteria2 | 248 |
| shadowsocksr | 162 |
| http | 79 |
| socks | 60 |
| hysteria | 8 |
| tuic | 2 |
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
| 74.89 | shadowsocks | 231.4 | 591.8 | 22.42 | 0.0 | 10.0 | 13.21 | 13.26 | Au1rxx-base64 | 156.146.38.167 |
| 74.75 | shadowsocks | 237.5 | 611.4 | 22.28 | 0.0 | 10.0 | 13.21 | 13.26 | Au1rxx-base64 | 156.146.38.169 |
| 74.68 | shadowsocks | 240.3 | 620.9 | 22.21 | 0.0 | 10.0 | 13.21 | 13.26 | Au1rxx-base64 | 156.146.38.170 |
| 74.6 | shadowsocks | 244.2 | 624.4 | 22.13 | 0.0 | 10.0 | 13.21 | 13.26 | Au1rxx-base64 | 156.146.38.168 |
| 72.52 | trojan | 435.2 | 1159.1 | 17.7 | 0.0 | 10.0 | 12.98 | 14.84 | mheidari-all | 64.94.95.118 |
| 71.31 | shadowsocks | 256.3 | 539.2 | 21.84 | 0.0 | 10.0 | 13.21 | 13.26 | Au1rxx-base64 | 173.244.56.9 |
| 69.85 | shadowsocks | 312.0 | 703.3 | 20.56 | 0.0 | 10.0 | 13.21 | 13.26 | Au1rxx-base64 | 173.244.56.6 |
| 69.74 | shadowsocks | 305.9 | 653.9 | 20.7 | 0.0 | 10.0 | 13.21 | 14.84 | mheidari-all | 198.98.53.130 |
| 69.11 | trojan | 366.3 | 627.7 | 19.3 | 0.0 | 10.0 | 12.98 | 18.4 | Surfboard-tg-mixed | 94.140.0.100 |
| 68.89 | shadowsocks | 327.7 | 708.0 | 20.19 | 0.0 | 10.0 | 13.21 | 13.26 | Au1rxx-base64 | 37.19.198.236 |
| 68.7 | trojan | 438.2 | 856.1 | 17.63 | 0.0 | 10.0 | 12.98 | 13.26 | Au1rxx-base64 | 45.61.52.243 |
| 68.65 | shadowsocks | 310.8 | 638.0 | 20.58 | 0.0 | 10.0 | 13.21 | 13.26 | Au1rxx-base64 | 149.22.95.183 |
| 68.58 | shadowsocks | 350.0 | 744.5 | 19.68 | 0.0 | 10.0 | 13.21 | 14.84 | mheidari-all | 108.181.57.93 |
| 68.3 | shadowsocks | 406.5 | 1031.3 | 18.37 | 0.0 | 10.0 | 13.21 | 13.26 | Au1rxx-base64 | 172.234.202.34 |
| 67.95 | trojan | 429.0 | 848.0 | 17.85 | 0.0 | 10.0 | 12.98 | 13.26 | Au1rxx-base64 | 207.126.167.150 |
| 67.92 | vless | 356.1 | 869.8 | 19.53 | 0.0 | 10.0 | 6.66 | 13.26 | Au1rxx-base64 | 15.204.97.214 |
| 67.77 | vless | 360.7 | 884.4 | 19.43 | 0.0 | 10.0 | 6.66 | 13.26 | Au1rxx-base64 | 15.204.97.219 |
| 67.72 | trojan | 449.6 | 546.9 | 17.37 | 0.0 | 10.0 | 12.98 | 18.4 | Surfboard-tg-mixed | 45.131.4.118 |
| 67.39 | shadowsocks | 331.4 | 374.0 | 20.11 | 0.97 | 9.75 | 13.21 | 14.84 | mheidari-all | 149.22.87.240 |
| 67.38 | shadowsocks | 327.7 | 373.9 | 20.19 | 0.98 | 9.71 | 13.21 | 14.84 | mheidari-all | 149.22.87.204 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.89 | 1.0 | 18 | 39 | prefer |
| Surfboard-tg-mixed | 0.797 | 0.718 | 277 | 5179 | prefer |
| Au1rxx-base64 | 0.76 | 0.771 | 35 | 91 | prefer |
| DeltaKronecker-all | 0.75 | 0.674 | 89 | 6822 | prefer |
| mheidari-all | 0.723 | 0.644 | 208 | 16368 | prefer |
| nscl5-all | 0.359 | 1.0 | 2 | 1186 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4579 | observe |
| Epodonios-all | 0.255 | None | 0 | 7844 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3979 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7359 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 3796 | observe |
| barry-far-vless | 0.255 | None | 0 | 4577 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5283 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 72 |
| 204 | TimeoutError | - | 29 |
| geo | TimeoutError | - | 21 |
| 204 | ClientOSError | - | 19 |
| cn-block | TimeoutError | - | 14 |
| 204 | ProxyError | - | 11 |
| speed | TimeoutError | - | 7 |
| geo | ClientOSError | - | 5 |
| cn-block | ProxyError | - | 3 |
| cn-block | ClientOSError | - | 3 |
| geo | ProxyError | - | 3 |
| speed | ProxyError | - | 3 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
