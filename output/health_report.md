# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-06-22 12:19:04 |
| 运行耗时 | 208.2s |
| 订阅源总数 | 107 |
| 健康订阅源 | 104 |
| 原始节点 | 75883 |
| 去重后节点 | 22484 |
| TCP 可达 | 3000 |
| 真实可用 | 509 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22484 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.1 |
| geo | 1.3 |
| tcp | 30.4 |
| probe | 50.6 |
| real_test | 98.5 |
| generate | 22.2 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 45069 |
| trojan | 10378 |
| shadowsocks | 9956 |
| vmess | 9817 |
| hysteria2 | 250 |
| http | 182 |
| shadowsocksr | 166 |
| socks | 57 |
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
| 78.95 | vless | 254.3 | 721.3 | 21.89 | 0.0 | 10.0 | 9.76 | 17.3 | mheidari-all | 47.253.226.114 |
| 78.71 | shadowsocks | 227.0 | 631.0 | 22.52 | 0.0 | 10.0 | 14.25 | 15.94 | Au1rxx-base64 | 37.19.198.243 |
| 78.7 | shadowsocks | 227.5 | 632.4 | 22.51 | 0.0 | 10.0 | 14.25 | 15.94 | Au1rxx-base64 | 37.19.198.236 |
| 78.64 | shadowsocks | 230.1 | 635.6 | 22.45 | 0.0 | 10.0 | 14.25 | 15.94 | Au1rxx-base64 | 37.19.198.244 |
| 77.82 | shadowsocks | 265.4 | 742.3 | 21.63 | 0.0 | 10.0 | 14.25 | 15.94 | Au1rxx-base64 | 37.19.198.160 |
| 76.64 | shadowsocks | 233.8 | 660.9 | 22.37 | 0.0 | 10.0 | 14.25 | 14.52 | DeltaKronecker-all | 108.181.57.93 |
| 75.33 | shadowsocks | 290.3 | 814.7 | 21.06 | 0.0 | 10.0 | 14.25 | 14.52 | DeltaKronecker-all | 142.93.183.235 |
| 74.75 | shadowsocks | 282.3 | 653.8 | 21.24 | 0.0 | 10.0 | 14.25 | 15.94 | Au1rxx-base64 | 156.146.38.170 |
| 74.35 | shadowsocks | 282.9 | 653.4 | 21.23 | 0.0 | 10.0 | 14.25 | 15.94 | Au1rxx-base64 | 156.146.38.169 |
| 73.73 | shadowsocks | 420.7 | 1198.3 | 18.04 | 0.0 | 10.0 | 14.25 | 15.94 | Au1rxx-base64 | 205.209.104.91 |
| 73.69 | vless | 309.9 | 740.5 | 20.6 | 0.0 | 10.0 | 9.76 | 15.94 | Au1rxx-base64 | 15.223.121.250 |
| 73.47 | shadowsocks | 278.2 | 640.8 | 21.34 | 0.0 | 10.0 | 14.25 | 15.94 | Au1rxx-base64 | 156.146.38.168 |
| 73.21 | vless | 358.8 | 893.4 | 19.47 | 0.0 | 10.0 | 9.76 | 17.3 | mheidari-all | 185.156.47.96 |
| 72.31 | shadowsocks | 332.7 | 797.8 | 20.08 | 0.0 | 10.0 | 14.25 | 15.94 | Au1rxx-base64 | 107.172.250.161 |
| 72.02 | shadowsocks | 433.2 | 1247.6 | 17.75 | 0.0 | 10.0 | 14.25 | 14.52 | DeltaKronecker-all | 173.225.106.117 |
| 71.74 | trojan | 370.0 | 852.6 | 19.21 | 0.0 | 10.0 | 12.04 | 17.3 | mheidari-all | 64.94.95.118 |
| 71.03 | shadowsocks | 234.9 | 633.2 | 22.34 | 0.0 | 10.0 | 14.25 | 17.3 | mheidari-all | 198.98.53.130 |
| 71.0 | shadowsocks | 309.7 | 561.9 | 20.61 | 0.0 | 10.0 | 14.25 | 15.94 | Au1rxx-base64 | 173.244.56.9 |
| 70.18 | shadowsocks | 358.5 | 745.0 | 19.48 | 0.0 | 10.0 | 14.25 | 15.94 | Au1rxx-base64 | 173.244.56.6 |
| 69.75 | hysteria2 | 366.3 | 704.5 | 19.3 | 0.0 | 10.0 | 11.25 | 15.94 | Au1rxx-base64 | 62.210.124.146 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.991 | 1.0 | 69 | 131 | prefer |
| mheidari-all | 0.921 | 0.843 | 293 | 14984 | prefer |
| Au1rxx-base64 | 0.91 | 0.915 | 82 | 136 | prefer |
| DeltaKronecker-all | 0.673 | 0.594 | 187 | 7452 | observe |
| Surfboard-tg-mixed | 0.401 | 0.571 | 7 | 5168 | observe |
| Epodonios-all | 0.391 | 1.0 | 2 | 7787 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4466 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3982 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7031 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 3984 | observe |
| barry-far-vless | 0.255 | None | 0 | 4897 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4559 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| nscl5-all | 0.23 | None | 0 | 1364 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 51 |
| 204 | ProxyError | - | 23 |
| 204 | TimeoutError | - | 16 |
| geo | TimeoutError | - | 11 |
| cn-block | ProxyError | - | 7 |
| cn-block | TimeoutError | - | 7 |
| speed | TimeoutError | - | 5 |
| 204 | ClientOSError | - | 3 |
| geo | ClientOSError | - | 3 |
| speed | ProxyError | - | 3 |
| cn-block | ClientOSError | - | 2 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
