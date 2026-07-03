# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-03 09:31:44 |
| 运行耗时 | 242.0s |
| 订阅源总数 | 107 |
| 健康订阅源 | 103 |
| 原始节点 | 77356 |
| 去重后节点 | 22732 |
| TCP 可达 | 3000 |
| 真实可用 | 437 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22732 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.4 |
| geo | 1.4 |
| tcp | 30.5 |
| probe | 51.4 |
| real_test | 106.8 |
| generate | 47.5 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 44806 |
| trojan | 12310 |
| vmess | 10399 |
| shadowsocks | 9216 |
| hysteria2 | 218 |
| shadowsocksr | 150 |
| http | 135 |
| socks | 115 |
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
| 77.19 | shadowsocks | 220.6 | 609.6 | 22.67 | 0.0 | 10.0 | 14.02 | 14.5 | Au1rxx-base64 | 37.19.198.243 |
| 77.06 | shadowsocks | 226.1 | 626.8 | 22.54 | 0.0 | 10.0 | 14.02 | 14.5 | Au1rxx-base64 | 37.19.198.160 |
| 76.98 | shadowsocks | 229.7 | 631.8 | 22.46 | 0.0 | 10.0 | 14.02 | 14.5 | Au1rxx-base64 | 37.19.198.244 |
| 75.56 | socks | 267.6 | 698.2 | 21.58 | 0.0 | 10.0 | 12.22 | 16.26 | Surfboard-tg-mixed | 134.122.1.61 |
| 75.24 | shadowsocks | 305.1 | 865.7 | 20.72 | 0.0 | 10.0 | 14.02 | 14.5 | Au1rxx-base64 | 37.19.198.236 |
| 74.96 | socks | 293.7 | 700.2 | 20.98 | 0.0 | 10.0 | 12.22 | 16.26 | Surfboard-tg-mixed | 47.253.211.16 |
| 74.87 | shadowsocks | 225.5 | 598.3 | 22.56 | 0.0 | 10.0 | 14.02 | 12.98 | mheidari-all | 198.98.53.130 |
| 74.74 | socks | 238.3 | 642.3 | 22.26 | 0.0 | 10.0 | 12.22 | 16.26 | Surfboard-tg-mixed | 204.48.29.137 |
| 72.81 | shadowsocks | 324.7 | 775.0 | 20.26 | 0.0 | 10.0 | 14.02 | 14.5 | Au1rxx-base64 | 156.146.38.169 |
| 71.36 | shadowsocks | 403.2 | 1010.6 | 18.45 | 0.0 | 10.0 | 14.02 | 14.5 | Au1rxx-base64 | 156.146.38.167 |
| 70.83 | shadowsocks | 389.2 | 959.7 | 18.77 | 0.0 | 10.0 | 14.02 | 14.5 | Au1rxx-base64 | 156.146.38.170 |
| 70.74 | socks | 323.8 | 668.2 | 20.28 | 0.0 | 10.0 | 12.22 | 16.26 | Surfboard-tg-mixed | 142.248.80.110 |
| 70.46 | vless | 258.3 | 728.5 | 21.8 | 0.0 | 10.0 | 5.68 | 12.98 | mheidari-all | 47.253.226.114 |
| 70.4 | shadowsocks | 237.7 | 639.1 | 22.27 | 0.0 | 10.0 | 14.02 | 14.5 | Au1rxx-base64 | 147.90.234.133 |
| 70.28 | trojan | 314.5 | 747.2 | 20.5 | 0.0 | 10.0 | 13.7 | 16.26 | Surfboard-tg-mixed | 94.140.0.40 |
| 69.63 | shadowsocks | 317.0 | 576.2 | 20.44 | 0.0 | 10.0 | 14.02 | 14.5 | Au1rxx-base64 | 173.244.56.9 |
| 69.29 | trojan | 389.4 | 546.5 | 18.76 | 0.0 | 10.0 | 13.7 | 16.26 | Surfboard-tg-mixed | 91.193.58.201 |
| 69.18 | vless | 270.2 | 666.3 | 21.52 | 0.0 | 10.0 | 5.68 | 12.98 | mheidari-all | 104.25.161.29 |
| 69.15 | shadowsocks | 321.9 | 602.3 | 20.33 | 0.0 | 10.0 | 14.02 | 14.5 | Au1rxx-base64 | 149.22.95.183 |
| 69.14 | trojan | 450.8 | 769.8 | 17.34 | 0.0 | 10.0 | 13.7 | 16.26 | Surfboard-tg-mixed | 165.215.250.14 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| DeltaKronecker-all | 0.766 | 0.689 | 103 | 6997 | prefer |
| Au1rxx-base64 | 0.741 | 0.75 | 40 | 80 | prefer |
| Surfboard-tg-mixed | 0.74 | 0.661 | 283 | 6013 | prefer |
| mheidari-all | 0.537 | 0.457 | 243 | 16051 | observe |
| nscl5-all | 0.356 | 1.0 | 2 | 1114 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4368 | observe |
| Epodonios-all | 0.255 | None | 0 | 6902 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3977 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6954 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4518 | observe |
| barry-far-vless | 0.255 | None | 0 | 5055 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5372 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| xiaoji235-airport-v2ray-all | 0.227 | None | 0 | 1289 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 121 |
| geo | TimeoutError | - | 62 |
| 204 | TimeoutError | - | 16 |
| geo | ClientOSError | - | 15 |
| 204 | ProxyError | - | 14 |
| cn-block | TimeoutError | - | 14 |
| cn-block | ClientOSError | - | 9 |
| speed | TimeoutError | - | 7 |
| 204 | ClientOSError | - | 6 |
| cn-block | ProxyError | - | 3 |
| geo | ProxyError | - | 2 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
