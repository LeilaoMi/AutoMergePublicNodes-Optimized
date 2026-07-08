# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-08 03:25:39 |
| 运行耗时 | 197.9s |
| 订阅源总数 | 107 |
| 健康订阅源 | 102 |
| 原始节点 | 83948 |
| 去重后节点 | 24959 |
| TCP 可达 | 3000 |
| 真实可用 | 398 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 24959 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.3 |
| geo | 1.3 |
| tcp | 32.1 |
| probe | 41.8 |
| real_test | 71.4 |
| generate | 46.9 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 49737 |
| trojan | 13083 |
| vmess | 10523 |
| shadowsocks | 9424 |
| hysteria2 | 837 |
| shadowsocksr | 148 |
| http | 140 |
| socks | 42 |
| hysteria | 8 |
| anytls | 4 |
| tuic | 2 |

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
| 76.69 | shadowsocks | 244.0 | 651.0 | 22.13 | 0.0 | 10.0 | 11.68 | 16.88 | Au1rxx-base64 | 37.19.198.236 |
| 76.49 | shadowsocks | 252.8 | 672.3 | 21.93 | 0.0 | 10.0 | 11.68 | 16.88 | Au1rxx-base64 | 37.19.198.244 |
| 76.48 | shadowsocks | 252.9 | 668.3 | 21.92 | 0.0 | 10.0 | 11.68 | 16.88 | Au1rxx-base64 | 37.19.198.243 |
| 76.09 | shadowsocks | 248.2 | 631.5 | 22.03 | 0.0 | 10.0 | 11.68 | 16.88 | Au1rxx-base64 | 108.181.57.93 |
| 73.55 | shadowsocks | 277.9 | 642.3 | 21.35 | 0.0 | 10.0 | 11.68 | 16.88 | Au1rxx-base64 | 156.146.38.170 |
| 73.0 | shadowsocks | 283.5 | 658.2 | 21.21 | 0.0 | 10.0 | 11.68 | 16.88 | Au1rxx-base64 | 156.146.38.168 |
| 72.9 | shadowsocks | 244.6 | 639.6 | 22.12 | 0.0 | 10.0 | 11.68 | 13.1 | mheidari-all | 147.90.234.133 |
| 72.87 | shadowsocks | 279.7 | 641.6 | 21.3 | 0.0 | 10.0 | 11.68 | 16.88 | Au1rxx-base64 | 156.146.38.169 |
| 71.62 | shadowsocks | 356.4 | 872.5 | 19.53 | 0.0 | 10.0 | 11.68 | 16.88 | Au1rxx-base64 | 185.196.61.82 |
| 70.36 | shadowsocks | 278.5 | 750.5 | 21.33 | 0.0 | 10.0 | 11.68 | 16.88 | Au1rxx-base64 | 198.98.53.130 |
| 69.51 | vless | 312.4 | 836.8 | 20.55 | 0.0 | 10.0 | 2.08 | 16.88 | Au1rxx-base64 | 159.89.87.21 |
| 69.01 | shadowsocks | 318.2 | 603.7 | 20.41 | 0.0 | 10.0 | 11.68 | 16.88 | Au1rxx-base64 | 108.181.0.177 |
| 68.72 | shadowsocks | 280.6 | 649.1 | 21.28 | 0.0 | 10.0 | 11.68 | 16.88 | Au1rxx-base64 | 156.146.38.167 |
| 68.57 | shadowsocks | 320.7 | 556.8 | 20.36 | 0.0 | 10.0 | 11.68 | 16.88 | Au1rxx-base64 | 108.181.118.10 |
| 68.5 | vmess | 424.3 | 1160.7 | 17.96 | 0.0 | 10.0 | 13.12 | 12.92 | Surfboard-tg-mixed | 67.220.85.46 |
| 68.39 | hysteria2 | 453.4 | 985.4 | 17.28 | 0.0 | 10.0 | 10.71 | 16.88 | Au1rxx-base64 | 62.210.124.146 |
| 68.31 | shadowsocks | 351.0 | 603.5 | 19.65 | 0.0 | 10.0 | 11.68 | 16.88 | Au1rxx-base64 | 149.22.95.183 |
| 68.12 | shadowsocks | 281.4 | 754.8 | 21.26 | 0.0 | 10.0 | 11.68 | 16.88 | Au1rxx-base64 | tinkered-pennies-puppies.freesocks.work |
| 66.65 | hysteria2 | 519.8 | 1143.9 | 15.75 | 0.0 | 10.0 | 10.71 | 16.88 | Au1rxx-base64 | 5.255.102.165 |
| 66.12 | socks | 265.0 | 659.9 | 21.64 | 0.0 | 10.0 | 12.0 | 6.98 | xiaoji235-airport-v2ray-all | 134.122.1.61 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Surfboard-tg-mixed | 0.984 | 0.912 | 102 | 5768 | prefer |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| DeltaKronecker-all | 0.788 | 0.711 | 166 | 8472 | prefer |
| Au1rxx-base64 | 0.745 | 0.747 | 75 | 125 | prefer |
| mheidari-all | 0.71 | 0.632 | 144 | 18232 | prefer |
| xiaoji235-airport-v2ray-all | 0.32 | 0.5 | 4 | 3640 | observe |
| tg-LonUp_M | 0.318 | 1.0 | 2 | 170 | observe |
| Epodonios-all | 0.255 | None | 0 | 6908 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3973 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6977 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4340 | observe |
| barry-far-vless | 0.255 | None | 0 | 5099 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5339 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| nscl5-all | 0.237 | None | 0 | 1561 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 59 |
| speed | ClientOSError | - | 31 |
| speed | TimeoutError | - | 18 |
| geo | ClientOSError | - | 10 |
| 204 | ClientOSError | - | 6 |
| 204 | TimeoutError | - | 3 |
| cn-block | ClientOSError | - | 3 |
| cn-block | TimeoutError | - | 2 |
| 204 | ProxyError | - | 1 |
| cn-block | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 209 | 300 | - |
| global | False | 217 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
