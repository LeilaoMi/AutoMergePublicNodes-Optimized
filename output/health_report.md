# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-05 04:01:57 |
| 运行耗时 | 192.5s |
| 订阅源总数 | 107 |
| 健康订阅源 | 103 |
| 原始节点 | 78644 |
| 去重后节点 | 23862 |
| TCP 可达 | 3000 |
| 真实可用 | 451 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23862 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.7 |
| geo | 1.6 |
| tcp | 31.0 |
| probe | 43.3 |
| real_test | 87.4 |
| generate | 24.6 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 45180 |
| trojan | 12697 |
| vmess | 10449 |
| shadowsocks | 9505 |
| hysteria2 | 477 |
| shadowsocksr | 144 |
| http | 135 |
| socks | 48 |
| hysteria | 6 |
| tuic | 3 |

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
| 76.28 | shadowsocks | 251.5 | 614.2 | 21.96 | 0.0 | 10.0 | 11.28 | 17.04 | Au1rxx-base64 | 156.146.38.170 |
| 76.21 | shadowsocks | 254.4 | 632.9 | 21.89 | 0.0 | 10.0 | 11.28 | 17.04 | Au1rxx-base64 | 156.146.38.167 |
| 76.1 | shadowsocks | 259.2 | 636.0 | 21.78 | 0.0 | 10.0 | 11.28 | 17.04 | Au1rxx-base64 | 156.146.38.169 |
| 75.94 | shadowsocks | 266.0 | 661.9 | 21.62 | 0.0 | 10.0 | 11.28 | 17.04 | Au1rxx-base64 | 37.19.198.236 |
| 75.88 | shadowsocks | 268.5 | 671.1 | 21.56 | 0.0 | 10.0 | 11.28 | 17.04 | Au1rxx-base64 | 37.19.198.160 |
| 75.79 | shadowsocks | 254.1 | 626.3 | 21.9 | 0.0 | 10.0 | 11.28 | 17.04 | Au1rxx-base64 | 156.146.38.168 |
| 75.6 | shadowsocks | 271.6 | 679.6 | 21.49 | 0.0 | 10.0 | 11.28 | 17.04 | Au1rxx-base64 | 37.19.198.244 |
| 72.91 | shadowsocks | 267.2 | 672.0 | 21.59 | 0.0 | 10.0 | 11.28 | 17.04 | Au1rxx-base64 | 37.19.198.243 |
| 71.45 | shadowsocks | 280.7 | 686.2 | 21.28 | 0.0 | 10.0 | 11.28 | 13.94 | Surfboard-tg-mixed | 108.181.57.93 |
| 70.9 | hysteria2 | 384.3 | 714.9 | 18.88 | 0.0 | 9.9 | 12.5 | 17.04 | Au1rxx-base64 | 62.210.124.146 |
| 70.56 | shadowsocks | 307.6 | 617.7 | 20.66 | 0.0 | 10.0 | 11.28 | 17.04 | Au1rxx-base64 | 149.22.95.183 |
| 70.19 | vless | 302.8 | 770.5 | 20.77 | 0.0 | 10.0 | 2.42 | 17.04 | Au1rxx-base64 | 47.253.226.114 |
| 70.08 | shadowsocks | 338.6 | 874.0 | 19.94 | 0.0 | 10.0 | 11.28 | 13.34 | mheidari-all | 147.90.234.133 |
| 68.86 | shadowsocks | 335.8 | 877.9 | 20.0 | 0.0 | 10.0 | 11.28 | 12.08 | DeltaKronecker-all | 185.196.61.82 |
| 68.31 | vmess | 427.9 | 1144.3 | 17.87 | 0.0 | 10.0 | 12.86 | 12.08 | DeltaKronecker-all | 67.220.85.46 |
| 68.0 | shadowsocks | 342.3 | 614.8 | 19.85 | 0.0 | 10.0 | 11.28 | 17.04 | Au1rxx-base64 | 173.244.56.9 |
| 67.62 | trojan | 263.8 | 615.4 | 21.67 | 0.0 | 10.0 | 8.24 | 12.08 | DeltaKronecker-all | 64.94.95.114 |
| 67.3 | shadowsocks | 361.8 | 345.7 | 19.4 | 2.04 | 9.51 | 11.28 | 17.04 | Au1rxx-base64 | 149.22.87.240 |
| 67.27 | shadowsocks | 382.9 | 747.1 | 18.92 | 0.0 | 10.0 | 11.28 | 17.04 | Au1rxx-base64 | 173.244.56.6 |
| 67.0 | vless | 375.2 | 862.5 | 19.09 | 0.0 | 10.0 | 2.42 | 17.04 | Au1rxx-base64 | 159.89.87.21 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| mheidari-all | 0.954 | 0.882 | 85 | 16452 | prefer |
| Surfboard-tg-mixed | 0.872 | 0.796 | 157 | 5979 | prefer |
| Au1rxx-base64 | 0.805 | 0.81 | 58 | 125 | prefer |
| DeltaKronecker-all | 0.798 | 0.72 | 232 | 7309 | prefer |
| nscl5-all | 0.308 | 1.0 | 1 | 1323 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4579 | observe |
| Epodonios-all | 0.255 | None | 0 | 6981 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3983 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6984 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4424 | observe |
| barry-far-vless | 0.255 | None | 0 | 5089 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5366 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| xiaoji235-airport-v2ray-all | 0.227 | None | 0 | 1288 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 45 |
| speed | ClientOSError | - | 35 |
| 204 | ClientOSError | - | 8 |
| geo | ClientOSError | - | 7 |
| cn-block | TimeoutError | - | 7 |
| speed | TimeoutError | - | 6 |
| cn-block | ClientOSError | - | 4 |
| 204 | TimeoutError | - | 3 |
| 204 | ProxyError | - | 2 |
| cn-block | ProxyError | - | 1 |
| sing-box exited 1 |  [31mFATAL[0m[0000] start service: start inbound/socks[socks-in]: listen tcp 127.0.0.1:34986: bind: address already in use | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 202 | 300 | - |
| global | False | 208 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
