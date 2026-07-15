# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-15 13:56:52 |
| 运行耗时 | 212.0s |
| 订阅源总数 | 107 |
| 健康订阅源 | 104 |
| 原始节点 | 76174 |
| 去重后节点 | 22913 |
| TCP 可达 | 3000 |
| 真实可用 | 279 |
| Verified 输出 | 279 |
| Global 输出 | 290 |
| All 输出 | 22913 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.7 |
| geo | 1.3 |
| tcp | 31.9 |
| probe | 46.7 |
| real_test | 82.9 |
| generate | 44.5 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 43553 |
| trojan | 11599 |
| vmess | 10879 |
| shadowsocks | 9509 |
| hysteria2 | 322 |
| http | 138 |
| shadowsocksr | 126 |
| socks | 29 |
| hysteria | 9 |
| tuic | 5 |
| anytls | 5 |

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
| 75.11 | vmess | 303.7 | 878.7 | 20.75 | 0.0 | 10.0 | 12.5 | 16.36 | mheidari-all | 67.220.95.3 |
| 74.71 | shadowsocks | 253.1 | 668.1 | 21.92 | 0.0 | 10.0 | 10.98 | 16.36 | mheidari-all | 108.181.57.93 |
| 71.54 | trojan | 418.9 | 1013.3 | 18.08 | 0.0 | 10.0 | 13.01 | 16.36 | mheidari-all | 64.94.95.118 |
| 70.62 | vmess | 413.9 | 1164.9 | 18.2 | 0.0 | 10.0 | 12.5 | 14.42 | DeltaKronecker-all | 67.220.85.46 |
| 69.54 | shadowsocks | 362.1 | 902.6 | 19.4 | 0.0 | 10.0 | 10.98 | 14.42 | DeltaKronecker-all | 185.196.61.82 |
| 67.99 | trojan | 474.4 | 1178.5 | 16.8 | 0.0 | 10.0 | 13.01 | 14.42 | DeltaKronecker-all | 64.94.95.117 |
| 66.56 | trojan | 454.4 | 1122.4 | 17.26 | 0.0 | 10.0 | 13.01 | 14.42 | DeltaKronecker-all | 64.94.95.115 |
| 66.36 | http | 614.3 | 930.5 | 13.56 | 0.0 | 9.8 | 14.61 | 19.52 | snakem982 | 193.176.84.37 |
| 66.29 | http | 611.7 | 941.5 | 13.62 | 0.0 | 9.81 | 14.61 | 19.52 | snakem982 | 193.176.84.31 |
| 65.94 | trojan | 465.0 | 1154.1 | 17.01 | 0.0 | 10.0 | 13.01 | 14.42 | DeltaKronecker-all | 64.94.95.114 |
| 65.8 | http | 631.4 | 945.1 | 13.16 | 0.0 | 9.75 | 14.61 | 19.52 | snakem982 | 84.239.49.159 |
| 65.59 | http | 638.6 | 968.6 | 13.0 | 0.0 | 9.74 | 14.61 | 19.52 | snakem982 | 84.239.49.202 |
| 65.58 | http | 638.0 | 953.5 | 13.01 | 0.0 | 9.69 | 14.61 | 19.52 | snakem982 | 84.239.49.160 |
| 65.5 | http | 643.9 | 963.1 | 12.87 | 0.0 | 9.71 | 14.61 | 19.52 | snakem982 | 84.239.14.160 |
| 65.46 | http | 643.8 | 978.5 | 12.87 | 0.0 | 9.71 | 14.61 | 19.52 | snakem982 | 84.239.49.239 |
| 65.45 | http | 644.4 | 940.6 | 12.86 | 0.0 | 9.71 | 14.61 | 19.52 | snakem982 | 84.239.49.204 |
| 65.44 | http | 643.4 | 951.7 | 12.88 | 0.0 | 9.77 | 14.61 | 19.52 | snakem982 | 84.239.49.175 |
| 65.4 | http | 646.4 | 934.7 | 12.82 | 0.0 | 9.72 | 14.61 | 19.52 | snakem982 | 84.239.49.253 |
| 65.4 | http | 647.2 | 974.8 | 12.8 | 0.0 | 9.76 | 14.61 | 19.52 | snakem982 | 84.239.49.225 |
| 65.39 | http | 645.1 | 966.7 | 12.85 | 0.0 | 9.72 | 14.61 | 19.52 | snakem982 | 84.239.49.39 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| mheidari-all | 0.853 | 0.776 | 170 | 16029 | prefer |
| Surfboard-tg-mixed | 0.801 | 0.729 | 59 | 5463 | prefer |
| DeltaKronecker-all | 0.622 | 0.543 | 116 | 6421 | observe |
| nscl5-all | 0.321 | 0.667 | 3 | 1300 | observe |
| Au1rxx-base64 | 0.317 | 1.0 | 2 | 149 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| Epodonios-all | 0.255 | None | 0 | 6619 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3979 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7237 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4283 | observe |
| barry-far-vless | 0.255 | None | 0 | 4859 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5187 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| xiaoji235-airport-v2ray-all | 0.245 | None | 0 | 1741 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 43 |
| speed | ClientOSError | - | 20 |
| 204 | TimeoutError | - | 14 |
| speed | TimeoutError | - | 8 |
| cn-block | TimeoutError | - | 7 |
| 204 | ProxyError | - | 6 |
| cn-block | ProxyError | - | 4 |
| geo | ClientOSError | - | 3 |
| cn-block | ClientOSError | - | 3 |
| 204 | ClientOSError | - | 2 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 292 | 279 | - |
| global | False | 300 | 290 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
