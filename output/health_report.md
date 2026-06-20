# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.9.1 |
| 更新时间 | 2026-06-20 04:18:50 |
| 运行耗时 | 406.7s |
| 订阅源总数 | 107 |
| 健康订阅源 | 105 |
| 原始节点 | 73021 |
| 去重后节点 | 22102 |
| TCP 可达 | 935 |
| 真实可用 | 710 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22102 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.1 |
| geo | 1.3 |
| tcp | 65.4 |
| probe | 97.0 |
| real_test | 202.7 |
| generate | 36.3 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 41612 |
| shadowsocks | 10771 |
| trojan | 10147 |
| vmess | 9876 |
| hysteria2 | 247 |
| shadowsocksr | 154 |
| http | 107 |
| socks | 99 |
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
| 75.52 | shadowsocks | 252.3 | 653.2 | 21.94 | 0.0 | 10.0 | 13.6 | 16.48 | mheidari-all | 198.98.53.130 |
| 73.89 | vless | 385.3 | 876.7 | 18.86 | 0.0 | 10.0 | 9.99 | 18.48 | Surfboard-tg-mixed | 193.233.202.1 |
| 73.79 | shadowsocks | 283.6 | 757.2 | 21.21 | 0.0 | 10.0 | 13.6 | 18.48 | Surfboard-tg-mixed | 69.164.240.83 |
| 72.8 | shadowsocks | 237.4 | 635.3 | 22.28 | 0.0 | 10.0 | 13.6 | 13.42 | Au1rxx-base64 | 37.19.198.160 |
| 72.72 | shadowsocks | 241.1 | 646.6 | 22.2 | 0.0 | 10.0 | 13.6 | 13.42 | Au1rxx-base64 | 37.19.198.244 |
| 72.57 | shadowsocks | 247.5 | 651.9 | 22.05 | 0.0 | 10.0 | 13.6 | 13.42 | Au1rxx-base64 | 37.19.198.236 |
| 72.11 | shadowsocks | 245.6 | 652.8 | 22.09 | 0.0 | 10.0 | 13.6 | 13.42 | Au1rxx-base64 | 37.19.198.243 |
| 71.6 | shadowsocks | 292.0 | 784.7 | 21.02 | 0.0 | 10.0 | 13.6 | 16.48 | mheidari-all | 69.164.240.86 |
| 69.84 | shadowsocks | 277.1 | 641.3 | 21.36 | 0.0 | 10.0 | 13.6 | 13.42 | Au1rxx-base64 | 156.146.38.170 |
| 69.38 | shadowsocks | 274.9 | 639.1 | 21.41 | 0.0 | 10.0 | 13.6 | 13.42 | Au1rxx-base64 | 156.146.38.168 |
| 69.27 | shadowsocks | 414.0 | 1146.2 | 18.19 | 0.0 | 10.0 | 13.6 | 16.48 | mheidari-all | 161.129.71.148 |
| 69.26 | shadowsocks | 281.8 | 652.4 | 21.25 | 0.0 | 10.0 | 13.6 | 13.42 | Au1rxx-base64 | 156.146.38.169 |
| 69.24 | shadowsocks | 276.1 | 634.7 | 21.39 | 0.0 | 10.0 | 13.6 | 13.42 | Au1rxx-base64 | 156.146.38.167 |
| 69.24 | vless | 329.3 | 612.2 | 20.15 | 0.0 | 10.0 | 9.99 | 18.48 | Surfboard-tg-mixed | 67.230.170.34 |
| 67.86 | shadowsocks | 318.3 | 773.1 | 20.41 | 0.0 | 10.0 | 13.6 | 13.42 | Au1rxx-base64 | 107.172.250.161 |
| 67.59 | vless | 433.8 | 797.3 | 17.74 | 0.0 | 10.0 | 9.99 | 18.48 | Surfboard-tg-mixed | 3.8.160.120 |
| 67.47 | trojan | 297.1 | 623.7 | 20.9 | 0.0 | 10.0 | 11.77 | 16.48 | mheidari-all | 64.94.95.118 |
| 67.2 | trojan | 414.9 | 585.0 | 18.17 | 0.0 | 10.0 | 11.77 | 18.48 | Surfboard-tg-mixed | 151.101.110.219 |
| 67.15 | shadowsocks | 415.6 | 762.1 | 18.16 | 0.0 | 10.0 | 13.6 | 18.48 | Surfboard-tg-mixed | 162.19.254.232 |
| 67.11 | trojan | 450.5 | 776.8 | 17.35 | 0.0 | 10.0 | 11.77 | 18.48 | Surfboard-tg-mixed | 212.183.88.136 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.966 | 1.0 | 25 | 73 | prefer |
| Au1rxx-base64 | 0.958 | 1.0 | 20 | 98 | prefer |
| Surfboard-tg-mixed | 0.913 | 0.834 | 429 | 5022 | prefer |
| mheidari-all | 0.854 | 0.776 | 335 | 14629 | prefer |
| DeltaKronecker-all | 0.48 | 0.398 | 108 | 6989 | observe |
| xiaoji235-airport-v2ray-all | 0.292 | 1.0 | 1 | 913 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| roosterkid-openproxylist-v2ray | 0.261 | 1.0 | 1 | 150 | observe |
| Epodonios-all | 0.255 | None | 0 | 7454 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3978 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6672 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 3739 | observe |
| barry-far-vless | 0.255 | None | 0 | 4406 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4527 | observe |
| nscl5-all | 0.253 | 0.5 | 2 | 1126 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 82 |
| speed | ClientOSError | - | 59 |
| geo | ClientOSError | - | 16 |
| 204 | ClientOSError | - | 16 |
| cn-block | TimeoutError | - | 15 |
| 204 | TimeoutError | - | 11 |
| speed | TimeoutError | - | 9 |
| 204 | ProxyError | - | 8 |
| cn-block | ClientOSError | - | 5 |
| geo | ProxyError | - | 2 |
| speed | ProxyError | - | 1 |
| cn-block | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
