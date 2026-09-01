# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-01 11:30:55 |
| 运行耗时 | 322.4s |
| 订阅源总数 | 107 |
| 健康订阅源 | 96 |
| 原始节点 | 83205 |
| 去重后节点 | 24567 |
| TCP 可达 | 3000 |
| 真实可用 | 616 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 24567 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.8 |
| geo | 1.6 |
| tcp | 40.9 |
| probe | 88.6 |
| real_test | 144.9 |
| generate | 40.7 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 52165 |
| vmess | 11425 |
| shadowsocks | 10156 |
| trojan | 7667 |
| hysteria2 | 1413 |
| http | 146 |
| shadowsocksr | 131 |
| socks | 81 |
| hysteria | 9 |
| tuic | 7 |
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
| 81.95 | shadowsocks | 240.3 | 614.6 | 22.21 | 0.0 | 10.0 | 14.56 | 19.18 | Au1rxx-base64 | 156.146.38.167 |
| 81.93 | shadowsocks | 241.3 | 622.7 | 22.19 | 0.0 | 10.0 | 14.56 | 19.18 | Au1rxx-base64 | 156.146.38.170 |
| 81.08 | shadowsocks | 238.4 | 613.5 | 22.26 | 0.0 | 10.0 | 14.56 | 18.26 | mheidari-all | 156.146.38.168 |
| 80.83 | http | 253.0 | 565.9 | 21.92 | 0.0 | 10.0 | 14.4 | 19.32 | zhangkai | 138.199.35.198 |
| 79.9 | shadowsocks | 289.3 | 724.2 | 21.08 | 0.0 | 10.0 | 14.56 | 18.26 | mheidari-all | 156.146.38.169 |
| 78.78 | vless | 269.7 | 572.6 | 21.54 | 0.0 | 10.0 | 11.14 | 19.18 | Au1rxx-base64 | 172.235.38.85 |
| 78.67 | vless | 266.1 | 558.4 | 21.62 | 0.0 | 10.0 | 11.14 | 19.18 | Au1rxx-base64 | 172.236.252.35 |
| 78.66 | vless | 263.5 | 553.4 | 21.68 | 0.0 | 10.0 | 11.14 | 19.18 | Au1rxx-base64 | 172.233.156.123 |
| 78.44 | vless | 360.6 | 874.2 | 19.43 | 0.0 | 10.0 | 11.14 | 19.18 | Au1rxx-base64 | 15.204.97.197 |
| 78.36 | vless | 282.9 | 586.2 | 21.23 | 0.0 | 10.0 | 11.14 | 19.18 | Au1rxx-base64 | 172.235.43.210 |
| 78.35 | vless | 352.9 | 859.8 | 19.61 | 0.0 | 10.0 | 11.14 | 19.18 | Au1rxx-base64 | 15.204.97.216 |
| 78.34 | hysteria2 | 220.5 | 533.5 | 22.67 | 0.0 | 10.0 | 13.5 | 19.18 | Au1rxx-base64 | 66.94.121.46 |
| 78.31 | vless | 270.0 | 570.0 | 21.53 | 0.0 | 10.0 | 11.14 | 19.18 | Au1rxx-base64 | 172.233.139.46 |
| 78.28 | shadowsocks | 265.3 | 634.4 | 21.64 | 0.0 | 10.0 | 14.56 | 16.58 | Surfboard-tg-mixed | 23.150.248.20 |
| 78.11 | vless | 354.5 | 854.9 | 19.57 | 0.0 | 10.0 | 11.14 | 19.18 | Au1rxx-base64 | 15.204.97.206 |
| 78.0 | vless | 299.9 | 661.0 | 20.83 | 0.0 | 10.0 | 11.14 | 19.18 | Au1rxx-base64 | 195.211.99.45 |
| 77.9 | vless | 344.6 | 835.7 | 19.8 | 0.0 | 10.0 | 11.14 | 19.18 | Au1rxx-base64 | 15.204.97.214 |
| 77.68 | vless | 283.5 | 579.5 | 21.21 | 0.0 | 10.0 | 11.14 | 19.18 | Au1rxx-base64 | 173.230.155.55 |
| 77.59 | vless | 281.4 | 570.8 | 21.26 | 0.0 | 10.0 | 11.14 | 19.18 | Au1rxx-base64 | 74.207.245.124 |
| 77.59 | vless | 288.0 | 585.9 | 21.11 | 0.0 | 10.0 | 11.14 | 19.18 | Au1rxx-base64 | 45.33.107.237 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.966 | 1.0 | 23 | 144 | prefer |
| Au1rxx-base64 | 0.918 | 0.852 | 338 | 1711 | prefer |
| Surfboard-tg-mixed | 0.862 | 0.785 | 177 | 6921 | prefer |
| mheidari-all | 0.853 | 0.775 | 209 | 17148 | prefer |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| tg-LonUp_M | 0.262 | 1.0 | 1 | 166 | observe |
| tg-OutlineReleasedKey | 0.257 | 1.0 | 1 | 49 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4708 | observe |
| Epodonios-all | 0.255 | None | 0 | 7334 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7625 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5831 | observe |
| barry-far-vless | 0.255 | None | 0 | 6092 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4013 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | TimeoutError | - | 25 |
| speed | TimeoutError | - | 25 |
| cn-block | TimeoutError | - | 20 |
| geo | ClientOSError | - | 18 |
| cn-block | ClientOSError | - | 17 |
| geo | TimeoutError | - | 14 |
| 204 | ProxyError | - | 13 |
| 204 | ClientOSError | - | 8 |
| cn-block | ProxyError | - | 2 |
| speed | ClientOSError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
