# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-06-30 04:11:27 |
| 运行耗时 | 276.4s |
| 订阅源总数 | 107 |
| 健康订阅源 | 104 |
| 原始节点 | 75411 |
| 去重后节点 | 23011 |
| TCP 可达 | 3000 |
| 真实可用 | 602 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23011 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.5 |
| geo | 1.4 |
| tcp | 31.0 |
| probe | 55.6 |
| real_test | 143.3 |
| generate | 40.7 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 42196 |
| trojan | 12868 |
| vmess | 10343 |
| shadowsocks | 9374 |
| hysteria2 | 264 |
| shadowsocksr | 156 |
| http | 135 |
| socks | 68 |
| hysteria | 6 |
| tuic | 1 |

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
| 76.09 | shadowsocks | 225.0 | 622.8 | 22.57 | 0.0 | 10.0 | 11.46 | 16.06 | Au1rxx-base64 | 37.19.198.244 |
| 75.48 | shadowsocks | 226.5 | 627.4 | 22.54 | 0.0 | 10.0 | 11.46 | 16.06 | Au1rxx-base64 | 37.19.198.243 |
| 75.23 | shadowsocks | 226.1 | 600.4 | 22.55 | 0.0 | 10.0 | 11.46 | 15.22 | mheidari-all | 198.98.53.130 |
| 75.0 | vless | 356.4 | 1021.3 | 19.53 | 0.0 | 10.0 | 10.25 | 15.22 | mheidari-all | 47.253.226.114 |
| 74.73 | shadowsocks | 283.8 | 803.9 | 21.21 | 0.0 | 10.0 | 11.46 | 16.06 | Au1rxx-base64 | 37.19.198.236 |
| 74.52 | vless | 329.6 | 869.8 | 20.15 | 0.0 | 10.0 | 10.25 | 15.22 | mheidari-all | 162.159.34.128 |
| 74.02 | shadowsocks | 227.9 | 632.2 | 22.5 | 0.0 | 10.0 | 11.46 | 16.06 | Au1rxx-base64 | 37.19.198.160 |
| 73.62 | vless | 252.8 | 653.0 | 21.93 | 0.0 | 10.0 | 10.25 | 14.44 | Surfboard-tg-mixed | 137.184.218.169 |
| 72.56 | shadowsocks | 285.0 | 661.6 | 21.18 | 0.0 | 10.0 | 11.46 | 16.06 | Au1rxx-base64 | 156.146.38.167 |
| 72.53 | shadowsocks | 281.8 | 654.1 | 21.25 | 0.0 | 10.0 | 11.46 | 16.06 | Au1rxx-base64 | 156.146.38.168 |
| 72.38 | shadowsocks | 327.6 | 882.5 | 20.2 | 0.0 | 10.0 | 11.46 | 15.22 | mheidari-all | 108.181.57.93 |
| 72.16 | shadowsocks | 278.0 | 631.9 | 21.34 | 0.0 | 10.0 | 11.46 | 16.06 | Au1rxx-base64 | 156.146.38.169 |
| 72.02 | shadowsocks | 275.8 | 633.5 | 21.39 | 0.0 | 10.0 | 11.46 | 16.06 | Au1rxx-base64 | 156.146.38.170 |
| 71.47 | vless | 335.9 | 601.4 | 20.0 | 0.0 | 10.0 | 10.25 | 15.22 | mheidari-all | 104.24.9.6 |
| 70.95 | vless | 496.4 | 1281.4 | 16.29 | 0.0 | 10.0 | 10.25 | 15.22 | mheidari-all | 130.107.73.148 |
| 70.69 | vless | 269.6 | 658.9 | 21.54 | 0.0 | 10.0 | 10.25 | 9.9 | DeltaKronecker-all | 104.17.90.246 |
| 70.65 | vless | 271.4 | 673.7 | 21.5 | 0.0 | 10.0 | 10.25 | 9.9 | DeltaKronecker-all | 162.159.252.15 |
| 70.5 | vless | 281.9 | 654.2 | 21.25 | 0.0 | 10.0 | 10.25 | 15.22 | mheidari-all | 162.159.43.131 |
| 69.99 | vless | 338.1 | 611.9 | 19.95 | 0.0 | 10.0 | 10.25 | 15.22 | mheidari-all | 173.245.59.35 |
| 69.56 | vless | 275.1 | 688.8 | 21.41 | 0.0 | 10.0 | 10.25 | 9.9 | DeltaKronecker-all | 104.17.238.33 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| Surfboard-tg-mixed | 0.789 | 0.71 | 324 | 5456 | prefer |
| mheidari-all | 0.775 | 0.696 | 336 | 15873 | prefer |
| Au1rxx-base64 | 0.671 | 0.673 | 55 | 101 | observe |
| DeltaKronecker-all | 0.312 | 0.23 | 278 | 7004 | observe |
| xiaoji235-airport-v2ray-all | 0.303 | 1.0 | 1 | 1204 | observe |
| Epodonios-all | 0.255 | None | 0 | 6395 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3976 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6638 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4008 | observe |
| barry-far-vless | 0.255 | None | 0 | 4588 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5353 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |
| nscl5-all | 0.22 | None | 0 | 1136 | observe |
| 10ium-HighSpeed | 0.209 | None | 0 | 839 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 139 |
| speed | ClientOSError | - | 130 |
| geo | ClientOSError | - | 45 |
| speed | TimeoutError | - | 42 |
| cn-block | TimeoutError | - | 30 |
| 204 | ProxyError | - | 23 |
| 204 | ClientOSError | - | 9 |
| 204 | TimeoutError | - | 5 |
| cn-block | ClientOSError | - | 4 |
| cn-block | ProxyError | - | 3 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
