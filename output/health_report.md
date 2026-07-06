# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-06 20:09:02 |
| 运行耗时 | 193.0s |
| 订阅源总数 | 107 |
| 健康订阅源 | 102 |
| 原始节点 | 80258 |
| 去重后节点 | 24589 |
| TCP 可达 | 3000 |
| 真实可用 | 284 |
| Verified 输出 | 284 |
| Global 输出 | 300 |
| All 输出 | 24589 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.8 |
| geo | 1.3 |
| tcp | 31.4 |
| probe | 48.2 |
| real_test | 72.9 |
| generate | 34.3 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 46889 |
| trojan | 12481 |
| vmess | 10502 |
| shadowsocks | 9552 |
| hysteria2 | 479 |
| shadowsocksr | 152 |
| http | 139 |
| socks | 50 |
| tuic | 8 |
| hysteria | 6 |

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
| 75.38 | socks | 243.8 | 628.2 | 22.14 | 0.0 | 10.0 | 10.0 | 17.74 | Surfboard-tg-mixed | 134.122.1.61 |
| 75.03 | shadowsocks | 250.7 | 682.8 | 21.97 | 0.0 | 10.0 | 12.0 | 15.06 | Au1rxx-base64 | 37.19.198.160 |
| 74.25 | trojan | 329.3 | 754.5 | 20.15 | 0.0 | 10.0 | 12.8 | 17.04 | DeltaKronecker-all | 45.32.198.247 |
| 73.79 | trojan | 331.6 | 766.2 | 20.1 | 0.0 | 10.0 | 12.8 | 17.04 | DeltaKronecker-all | 149.28.241.235 |
| 73.75 | shadowsocks | 306.2 | 854.8 | 20.69 | 0.0 | 10.0 | 12.0 | 15.06 | Au1rxx-base64 | 37.19.198.243 |
| 73.28 | shadowsocks | 302.7 | 832.7 | 20.77 | 0.0 | 10.0 | 12.0 | 15.06 | Au1rxx-base64 | tinkered-pennies-puppies.freesocks.work |
| 72.77 | trojan | 338.5 | 781.6 | 19.94 | 0.0 | 10.0 | 12.8 | 17.04 | DeltaKronecker-all | 45.32.195.168 |
| 72.72 | shadowsocks | 329.1 | 883.4 | 20.16 | 0.0 | 10.0 | 12.0 | 15.06 | Au1rxx-base64 | 108.181.57.93 |
| 71.66 | shadowsocks | 288.7 | 661.1 | 21.1 | 0.0 | 10.0 | 12.0 | 15.06 | Au1rxx-base64 | 156.146.38.168 |
| 70.99 | shadowsocks | 283.8 | 650.0 | 21.21 | 0.0 | 10.0 | 12.0 | 15.06 | Au1rxx-base64 | 156.146.38.169 |
| 70.65 | shadowsocks | 355.2 | 877.2 | 19.56 | 0.0 | 10.0 | 12.0 | 15.06 | Au1rxx-base64 | 185.196.61.82 |
| 70.37 | shadowsocks | 236.3 | 634.4 | 22.31 | 0.0 | 10.0 | 12.0 | 15.06 | Au1rxx-base64 | 37.19.198.244 |
| 70.14 | shadowsocks | 245.9 | 679.4 | 22.08 | 0.0 | 10.0 | 12.0 | 15.06 | Au1rxx-base64 | 37.19.198.236 |
| 70.1 | shadowsocks | 314.9 | 742.9 | 20.49 | 0.0 | 10.0 | 12.0 | 15.06 | Au1rxx-base64 | 156.146.38.167 |
| 69.93 | hysteria2 | 370.5 | 699.8 | 19.2 | 0.0 | 9.94 | 12.86 | 15.06 | Au1rxx-base64 | 62.210.124.146 |
| 69.83 | trojan | 405.2 | 589.4 | 18.4 | 0.0 | 10.0 | 12.8 | 17.74 | Surfboard-tg-mixed | 104.18.37.237 |
| 69.47 | trojan | 425.7 | 600.1 | 17.92 | 0.0 | 10.0 | 12.8 | 17.74 | Surfboard-tg-mixed | 199.232.237.250 |
| 69.44 | vmess | 608.1 | 1761.3 | 13.7 | 0.0 | 10.0 | 12.5 | 17.74 | Surfboard-tg-mixed | 67.220.95.3 |
| 69.42 | shadowsocks | 311.0 | 731.8 | 20.58 | 0.0 | 10.0 | 12.0 | 15.06 | Au1rxx-base64 | 156.146.38.170 |
| 69.31 | shadowsocks | 335.5 | 585.3 | 20.01 | 0.0 | 10.0 | 12.0 | 17.04 | DeltaKronecker-all | 107.172.219.230 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| Au1rxx-base64 | 0.805 | 0.81 | 58 | 121 | prefer |
| Surfboard-tg-mixed | 0.794 | 0.718 | 110 | 6111 | prefer |
| DeltaKronecker-all | 0.793 | 0.717 | 120 | 8330 | prefer |
| mheidari-all | 0.661 | 0.583 | 60 | 16332 | observe |
| nscl5-all | 0.321 | 1.0 | 1 | 1651 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4358 | observe |
| Epodonios-all | 0.255 | None | 0 | 7090 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7234 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4506 | observe |
| barry-far-vless | 0.255 | None | 0 | 5174 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5338 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| xiaoji235-airport-v2ray-all | 0.226 | None | 0 | 1268 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 30 |
| 204 | ClientOSError | - | 13 |
| 204 | TimeoutError | - | 12 |
| cn-block | TimeoutError | - | 10 |
| 204 | ProxyError | - | 9 |
| cn-block | ClientOSError | - | 9 |
| geo | TimeoutError | - | 7 |
| cn-block | ProxyError | - | 4 |
| speed | ProxyError | - | 3 |
| speed | TimeoutError | - | 2 |
| geo | ProxyError | - | 2 |
| geo | ClientOSError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 284 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
