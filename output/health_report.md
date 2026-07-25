# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-25 19:21:21 |
| 运行耗时 | 318.0s |
| 订阅源总数 | 107 |
| 健康订阅源 | 102 |
| 原始节点 | 80536 |
| 去重后节点 | 22511 |
| TCP 可达 | 3000 |
| 真实可用 | 708 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22511 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.4 |
| geo | 1.3 |
| tcp | 31.1 |
| probe | 68.8 |
| real_test | 169.4 |
| generate | 42.0 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 45402 |
| trojan | 14511 |
| vmess | 10179 |
| shadowsocks | 9756 |
| hysteria2 | 433 |
| http | 81 |
| shadowsocksr | 79 |
| socks | 68 |
| hysteria | 15 |
| tuic | 11 |
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
| 79.48 | shadowsocks | 219.0 | 585.5 | 22.71 | 0.0 | 10.0 | 12.37 | 18.4 | Au1rxx-base64 | 198.98.53.130 |
| 78.93 | shadowsocks | 242.8 | 673.2 | 22.16 | 0.0 | 10.0 | 12.37 | 18.4 | Au1rxx-base64 | 37.19.198.160 |
| 78.9 | shadowsocks | 243.9 | 674.3 | 22.13 | 0.0 | 10.0 | 12.37 | 18.4 | Au1rxx-base64 | 37.19.198.243 |
| 78.89 | shadowsocks | 244.6 | 676.6 | 22.12 | 0.0 | 10.0 | 12.37 | 18.4 | Au1rxx-base64 | 37.19.198.236 |
| 78.82 | shadowsocks | 247.4 | 685.9 | 22.05 | 0.0 | 10.0 | 12.37 | 18.4 | Au1rxx-base64 | 37.19.198.244 |
| 76.24 | trojan | 345.1 | 883.3 | 19.79 | 0.0 | 10.0 | 13.61 | 15.84 | DeltaKronecker-all | 64.74.163.118 |
| 75.71 | shadowsocks | 284.7 | 649.1 | 21.19 | 0.0 | 10.0 | 12.37 | 18.4 | Au1rxx-base64 | 156.146.38.168 |
| 75.53 | shadowsocks | 282.7 | 647.7 | 21.23 | 0.0 | 10.0 | 12.37 | 18.4 | Au1rxx-base64 | 156.146.38.169 |
| 74.99 | hysteria2 | 352.9 | 698.3 | 19.61 | 0.0 | 10.0 | 13.5 | 18.4 | Au1rxx-base64 | 62.210.124.146 |
| 74.62 | shadowsocks | 321.0 | 817.3 | 20.35 | 0.0 | 10.0 | 12.37 | 18.4 | Au1rxx-base64 | 185.196.61.82 |
| 74.46 | shadowsocks | 287.2 | 662.8 | 21.13 | 0.0 | 10.0 | 12.37 | 18.4 | Au1rxx-base64 | 156.146.38.170 |
| 73.87 | hysteria2 | 423.1 | 881.1 | 17.98 | 0.0 | 10.0 | 13.5 | 18.4 | Au1rxx-base64 | 5.255.102.165 |
| 73.8 | trojan | 448.0 | 1143.1 | 17.41 | 0.0 | 10.0 | 13.61 | 18.4 | Au1rxx-base64 | 148.72.168.35 |
| 73.65 | trojan | 567.5 | 1620.9 | 14.64 | 0.0 | 10.0 | 13.61 | 18.4 | Au1rxx-base64 | 153.75.250.171 |
| 73.47 | shadowsocks | 283.7 | 640.7 | 21.21 | 0.0 | 10.0 | 12.37 | 18.4 | Au1rxx-base64 | 156.146.38.167 |
| 71.13 | trojan | 502.4 | 1234.3 | 16.15 | 0.0 | 10.0 | 13.61 | 18.4 | Au1rxx-base64 | 163.245.196.68 |
| 70.38 | trojan | 435.9 | 772.4 | 17.69 | 0.0 | 10.0 | 13.61 | 18.4 | Au1rxx-base64 | 89.39.70.208 |
| 70.17 | trojan | 445.3 | 793.5 | 17.47 | 0.0 | 10.0 | 13.61 | 18.4 | Au1rxx-base64 | 193.169.239.76 |
| 69.97 | trojan | 452.5 | 765.3 | 17.3 | 0.0 | 10.0 | 13.61 | 18.4 | Au1rxx-base64 | 89.39.70.233 |
| 69.93 | trojan | 451.0 | 829.7 | 17.34 | 0.0 | 10.0 | 13.61 | 18.4 | Au1rxx-base64 | 79.133.126.137 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.992 | 1.0 | 76 | 119 | prefer |
| Au1rxx-base64 | 0.908 | 0.862 | 427 | 1199 | prefer |
| mheidari-all | 0.782 | 0.704 | 253 | 17275 | prefer |
| Surfboard-tg-mixed | 0.747 | 0.673 | 49 | 5515 | prefer |
| DeltaKronecker-all | 0.65 | 0.571 | 91 | 5838 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4879 | observe |
| Epodonios-all | 0.255 | None | 0 | 6622 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3972 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6305 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4371 | observe |
| barry-far-vless | 0.255 | None | 0 | 4959 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4980 | observe |
| nscl5-all | 0.255 | None | 0 | 2974 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 59 |
| speed | ClientOSError | - | 32 |
| cn-block | TimeoutError | - | 31 |
| 204 | ProxyError | - | 22 |
| 204 | TimeoutError | - | 18 |
| speed | TimeoutError | - | 8 |
| geo | ClientOSError | - | 6 |
| cn-block | ClientOSError | - | 6 |
| cn-block | ProxyError | - | 4 |
| geo | ProxyError | - | 2 |
| 204 | ClientOSError | - | 2 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
