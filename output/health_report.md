# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-06-27 13:58:27 |
| 运行耗时 | 216.4s |
| 订阅源总数 | 107 |
| 健康订阅源 | 105 |
| 原始节点 | 77289 |
| 去重后节点 | 23018 |
| TCP 可达 | 3000 |
| 真实可用 | 296 |
| Verified 输出 | 296 |
| Global 输出 | 300 |
| All 输出 | 23018 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.5 |
| geo | 1.4 |
| tcp | 30.6 |
| probe | 48.8 |
| real_test | 94.7 |
| generate | 36.5 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 43300 |
| trojan | 12808 |
| vmess | 11239 |
| shadowsocks | 9398 |
| hysteria2 | 245 |
| shadowsocksr | 152 |
| http | 79 |
| socks | 59 |
| hysteria | 6 |
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
| 75.92 | shadowsocks | 240.0 | 623.1 | 22.22 | 0.0 | 10.0 | 12.5 | 15.2 | Au1rxx-base64 | 156.146.38.168 |
| 75.87 | shadowsocks | 242.0 | 626.4 | 22.17 | 0.0 | 10.0 | 12.5 | 15.2 | Au1rxx-base64 | 156.146.38.170 |
| 75.85 | shadowsocks | 243.1 | 627.4 | 22.15 | 0.0 | 10.0 | 12.5 | 15.2 | Au1rxx-base64 | 156.146.38.167 |
| 71.59 | trojan | 292.5 | 731.7 | 21.01 | 0.0 | 10.0 | 10.58 | 15.0 | DeltaKronecker-all | 64.94.95.117 |
| 71.24 | trojan | 307.7 | 789.8 | 20.66 | 0.0 | 10.0 | 10.58 | 15.0 | DeltaKronecker-all | 64.94.95.114 |
| 69.96 | shadowsocks | 307.7 | 673.4 | 20.66 | 0.0 | 10.0 | 12.5 | 15.2 | Au1rxx-base64 | 173.244.56.6 |
| 69.76 | trojan | 240.3 | 584.5 | 22.22 | 0.0 | 10.0 | 10.58 | 15.0 | DeltaKronecker-all | 64.94.95.115 |
| 69.68 | shadowsocks | 305.7 | 621.1 | 20.7 | 0.0 | 10.0 | 12.5 | 15.2 | Au1rxx-base64 | 149.22.95.183 |
| 69.47 | shadowsocks | 335.6 | 735.3 | 20.01 | 0.0 | 10.0 | 12.5 | 15.2 | Au1rxx-base64 | 37.19.198.243 |
| 69.46 | shadowsocks | 321.6 | 698.7 | 20.33 | 0.0 | 10.0 | 12.5 | 15.2 | Au1rxx-base64 | 37.19.198.160 |
| 69.46 | shadowsocks | 323.1 | 705.1 | 20.3 | 0.0 | 10.0 | 12.5 | 15.2 | Au1rxx-base64 | 37.19.198.236 |
| 69.42 | shadowsocks | 367.2 | 847.4 | 19.28 | 0.0 | 10.0 | 12.5 | 15.2 | Au1rxx-base64 | 173.244.56.9 |
| 69.01 | shadowsocks | 414.6 | 1022.1 | 18.18 | 0.0 | 10.0 | 12.5 | 15.2 | Au1rxx-base64 | 172.234.202.34 |
| 68.65 | vless | 270.0 | 578.9 | 21.53 | 0.0 | 10.0 | 9.11 | 15.94 | Surfboard-tg-mixed | 38.244.20.69 |
| 68.51 | vless | 385.3 | 805.8 | 18.86 | 0.0 | 10.0 | 9.11 | 15.94 | Surfboard-tg-mixed | 15.223.121.250 |
| 68.25 | vless | 320.2 | 746.4 | 20.37 | 0.0 | 10.0 | 9.11 | 15.94 | Surfboard-tg-mixed | 141.193.154.182 |
| 68.05 | trojan | 359.1 | 735.4 | 19.47 | 0.0 | 10.0 | 10.58 | 15.0 | DeltaKronecker-all | 104.17.148.22 |
| 67.6 | shadowsocks | 266.7 | 565.6 | 21.6 | 0.0 | 10.0 | 12.5 | 15.2 | Au1rxx-base64 | 216.105.168.18 |
| 66.96 | shadowsocks | 364.2 | 755.0 | 19.35 | 0.0 | 10.0 | 12.5 | 14.46 | mheidari-all | 108.181.57.93 |
| 66.59 | shadowsocks | 329.8 | 728.0 | 20.14 | 0.0 | 10.0 | 12.5 | 15.2 | Au1rxx-base64 | 37.19.198.244 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.913 | 0.95 | 20 | 93 | prefer |
| snakem982 | 0.89 | 1.0 | 18 | 39 | prefer |
| mheidari-all | 0.864 | 0.796 | 49 | 16363 | prefer |
| Surfboard-tg-mixed | 0.768 | 0.69 | 229 | 5186 | prefer |
| DeltaKronecker-all | 0.428 | 0.347 | 176 | 6822 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4579 | observe |
| Epodonios-all | 0.255 | None | 0 | 7866 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3978 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7361 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 3808 | observe |
| barry-far-vless | 0.255 | None | 0 | 4584 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5283 | observe |
| nscl5-all | 0.255 | 0.5 | 2 | 1186 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 103 |
| 204 | ProxyError | - | 20 |
| 204 | TimeoutError | - | 19 |
| 204 | ClientOSError | - | 15 |
| geo | ClientOSError | - | 9 |
| cn-block | TimeoutError | - | 9 |
| speed | TimeoutError | - | 6 |
| cn-block | ProxyError | - | 4 |
| cn-block | ClientOSError | - | 4 |
| geo | TimeoutError | - | 4 |
| speed | ProxyError | - | 4 |
| geo | ProxyError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 296 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
