# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.9.1 |
| 更新时间 | 2026-06-19 05:04:49 |
| 运行耗时 | 368.7s |
| 订阅源总数 | 107 |
| 健康订阅源 | 106 |
| 原始节点 | 71770 |
| 去重后节点 | 22121 |
| TCP 可达 | 866 |
| 真实可用 | 676 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22121 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.7 |
| geo | 1.4 |
| tcp | 64.2 |
| probe | 92.8 |
| real_test | 173.0 |
| generate | 32.6 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 41274 |
| shadowsocks | 10573 |
| trojan | 10110 |
| vmess | 9236 |
| hysteria2 | 223 |
| shadowsocksr | 147 |
| http | 107 |
| socks | 73 |
| anytls | 19 |
| hysteria | 6 |
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
| 80.45 | vless | 247.9 | 673.4 | 22.04 | 0.0 | 10.0 | 12.49 | 18.42 | Surfboard-tg-mixed | 137.184.218.169 |
| 76.36 | vless | 233.6 | 608.6 | 22.37 | 0.0 | 10.0 | 12.49 | 16.5 | mheidari-all | 46.8.98.55 |
| 76.24 | shadowsocks | 237.7 | 643.6 | 22.28 | 0.0 | 10.0 | 12.5 | 17.96 | Au1rxx-base64 | 37.19.198.160 |
| 76.16 | shadowsocks | 241.0 | 652.4 | 22.2 | 0.0 | 10.0 | 12.5 | 17.96 | Au1rxx-base64 | 37.19.198.236 |
| 75.6 | shadowsocks | 265.0 | 747.0 | 21.64 | 0.0 | 10.0 | 12.5 | 17.96 | Au1rxx-base64 | 37.19.198.244 |
| 75.07 | shadowsocks | 225.1 | 594.7 | 22.57 | 0.0 | 10.0 | 12.5 | 16.5 | mheidari-all | 198.98.53.130 |
| 75.03 | vless | 234.8 | 638.5 | 22.34 | 0.0 | 10.0 | 12.49 | 17.96 | Au1rxx-base64 | 159.89.87.21 |
| 73.04 | vless | 349.1 | 844.5 | 19.7 | 0.0 | 10.0 | 12.49 | 17.96 | Au1rxx-base64 | 193.233.202.7 |
| 72.51 | vless | 358.2 | 925.7 | 19.49 | 0.0 | 10.0 | 12.49 | 16.5 | mheidari-all | 185.156.47.96 |
| 72.46 | shadowsocks | 298.4 | 694.7 | 20.87 | 0.0 | 10.0 | 12.5 | 17.96 | Au1rxx-base64 | 156.146.38.170 |
| 72.23 | shadowsocks | 281.2 | 776.2 | 21.27 | 0.0 | 10.0 | 12.5 | 17.96 | Au1rxx-base64 | 37.19.198.243 |
| 71.34 | shadowsocks | 286.7 | 659.2 | 21.14 | 0.0 | 10.0 | 12.5 | 17.96 | Au1rxx-base64 | 156.146.38.167 |
| 71.08 | shadowsocks | 354.1 | 773.2 | 19.58 | 0.0 | 10.0 | 12.5 | 17.96 | Au1rxx-base64 | 156.146.38.169 |
| 71.04 | shadowsocks | 332.6 | 811.2 | 20.08 | 0.0 | 10.0 | 12.5 | 17.96 | Au1rxx-base64 | 107.172.250.161 |
| 70.34 | hysteria2 | 357.4 | 691.3 | 19.51 | 0.0 | 10.0 | 12.0 | 17.96 | Au1rxx-base64 | 62.210.124.146 |
| 70.18 | shadowsocks | 281.3 | 648.2 | 21.27 | 0.0 | 10.0 | 12.5 | 17.96 | Au1rxx-base64 | 156.146.38.168 |
| 70.13 | vless | 460.9 | 589.7 | 17.11 | 0.0 | 10.0 | 12.49 | 18.42 | Surfboard-tg-mixed | 194.87.24.181 |
| 69.94 | vless | 285.4 | 681.1 | 21.17 | 0.0 | 10.0 | 12.49 | 12.78 | DeltaKronecker-all | 173.245.59.35 |
| 69.29 | vless | 358.0 | 944.1 | 19.49 | 0.0 | 10.0 | 12.49 | 18.42 | Surfboard-tg-mixed | 37.1.212.241 |
| 69.15 | vless | 380.2 | 787.0 | 18.98 | 0.0 | 10.0 | 12.49 | 18.42 | Surfboard-tg-mixed | 104.21.74.112 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Surfboard-tg-mixed | 0.988 | 0.91 | 335 | 4851 | prefer |
| snakem982 | 0.966 | 1.0 | 25 | 73 | prefer |
| mheidari-all | 0.848 | 0.77 | 269 | 14638 | prefer |
| Au1rxx-base64 | 0.825 | 0.828 | 87 | 127 | prefer |
| DeltaKronecker-all | 0.53 | 0.449 | 147 | 7112 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4494 | observe |
| Epodonios-all | 0.255 | None | 0 | 6479 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3974 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6447 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 3730 | observe |
| barry-far-vless | 0.255 | None | 0 | 4360 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4615 | observe |
| ninja-vless | 0.251 | 0.333 | 3 | 1791 | observe |
| nscl5-all | 0.229 | None | 0 | 1360 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 72 |
| speed | ClientOSError | - | 51 |
| cn-block | TimeoutError | - | 18 |
| geo | ClientOSError | - | 15 |
| speed | TimeoutError | - | 11 |
| 204 | TimeoutError | - | 9 |
| 204 | ClientOSError | - | 6 |
| 204 | ProxyError | - | 5 |
| speed | ProxyError | - | 1 |
| cn-block | ClientOSError | - | 1 |
| cn-block | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
