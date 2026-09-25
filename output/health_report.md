# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-25 21:29:31 |
| 运行耗时 | 485.9s |
| 订阅源总数 | 107 |
| 健康订阅源 | 94 |
| 原始节点 | 97258 |
| 去重后节点 | 26464 |
| TCP 可达 | 3000 |
| 真实可用 | 402 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 26464 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.0 |
| geo | 1.4 |
| tcp | 43.7 |
| probe | 186.3 |
| real_test | 158.3 |
| generate | 92.2 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 59655 |
| vmess | 15074 |
| shadowsocks | 11210 |
| trojan | 8873 |
| hysteria2 | 1552 |
| http | 576 |
| shadowsocksr | 169 |
| socks | 96 |
| anytls | 27 |
| hysteria | 15 |
| tuic | 11 |

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
| 79.66 | vless | 261.5 | 634.9 | 21.72 | 0.0 | 9.44 | 9.6 | 18.9 | Au1rxx-base64 | 195.211.98.43 |
| 78.77 | vless | 286.2 | 668.3 | 21.15 | 0.0 | 9.43 | 9.6 | 18.9 | Au1rxx-base64 | 198.251.78.29 |
| 77.47 | shadowsocks | 252.6 | 668.6 | 21.93 | 0.0 | 9.49 | 13.15 | 18.9 | Au1rxx-base64 | 156.146.38.168 |
| 77.15 | shadowsocks | 263.6 | 623.1 | 21.68 | 0.0 | 9.43 | 13.15 | 18.9 | Au1rxx-base64 | 23.150.248.20 |
| 77.01 | shadowsocks | 309.8 | 732.4 | 20.61 | 0.0 | 9.54 | 13.15 | 18.9 | Au1rxx-base64 | 37.19.198.236 |
| 76.6 | shadowsocks | 352.9 | 926.6 | 19.61 | 0.0 | 9.44 | 13.15 | 18.9 | Au1rxx-base64 | 185.156.47.97 |
| 75.6 | shadowsocks | 252.0 | 644.1 | 21.94 | 0.0 | 10.0 | 13.15 | 14.58 | Surfboard-tg-mixed | 156.146.38.167 |
| 74.44 | vless | 290.4 | 593.0 | 21.06 | 0.0 | 9.45 | 9.6 | 18.9 | Au1rxx-base64 | 192.3.247.109 |
| 74.37 | vless | 351.0 | 759.6 | 19.65 | 0.0 | 9.46 | 9.6 | 18.9 | Au1rxx-base64 | 169.40.42.173 |
| 74.09 | vless | 438.2 | 1076.4 | 17.63 | 0.0 | 9.45 | 9.6 | 18.9 | Au1rxx-base64 | 185.95.231.156 |
| 73.7 | vless | 346.8 | 779.9 | 19.75 | 0.0 | 9.43 | 9.6 | 18.9 | Au1rxx-base64 | 66.70.179.198 |
| 73.6 | vless | 387.3 | 912.4 | 18.81 | 0.0 | 9.45 | 9.6 | 18.9 | Au1rxx-base64 | 169.40.42.95 |
| 73.47 | vless | 309.5 | 627.6 | 20.61 | 0.0 | 9.43 | 9.6 | 18.9 | Au1rxx-base64 | 172.235.43.210 |
| 73.47 | vless | 417.1 | 909.9 | 18.12 | 0.0 | 9.48 | 9.6 | 18.9 | Au1rxx-base64 | 169.40.42.223 |
| 73.21 | vless | 364.0 | 813.7 | 19.35 | 0.0 | 9.48 | 9.6 | 18.9 | Au1rxx-base64 | 5.78.159.214 |
| 72.81 | vless | 330.3 | 703.1 | 20.13 | 0.0 | 9.45 | 9.6 | 18.9 | Au1rxx-base64 | 169.40.42.231 |
| 72.66 | shadowsocks | 252.5 | 638.8 | 21.93 | 0.0 | 10.0 | 13.15 | 14.58 | Surfboard-tg-mixed | 156.146.38.169 |
| 72.52 | vless | 394.2 | 899.9 | 18.65 | 0.0 | 9.45 | 9.6 | 18.9 | Au1rxx-base64 | 169.40.42.15 |
| 72.24 | vless | 356.2 | 720.3 | 19.53 | 0.0 | 9.48 | 9.6 | 18.9 | Au1rxx-base64 | 169.40.42.212 |
| 72.11 | vless | 351.8 | 745.5 | 19.63 | 0.0 | 9.46 | 9.6 | 18.9 | Au1rxx-base64 | 169.40.42.225 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.949 | 0.884 | 241 | 1701 | prefer |
| mheidari-all | 0.903 | 0.831 | 77 | 22345 | prefer |
| Surfboard-tg-mixed | 0.901 | 0.826 | 121 | 7370 | prefer |
| ermaozi | 0.689 | 0.688 | 32 | 304 | observe |
| tg-oneclickvpnkeys | 0.314 | 1.0 | 2 | 69 | observe |
| ermaozi-get_subscribe | 0.268 | 1.0 | 1 | 314 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5293 | observe |
| DeltaKronecker-all | 0.255 | None | 0 | 5452 | observe |
| Epodonios-all | 0.255 | None | 0 | 7740 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9253 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5959 | observe |
| barry-far-vless | 0.255 | None | 0 | 6190 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4304 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | TimeoutError | - | 21 |
| cn-block | TimeoutError | - | 17 |
| 204 | ProxyError | - | 15 |
| cn-block | ClientOSError | - | 5 |
| cn-block | ProxyError | - | 3 |
| 204 | ClientOSError | - | 3 |
| speed | ClientOSError | - | 2 |
| geo | ClientOSError | - | 2 |
| speed | ProxyError | - | 2 |
| geo | TimeoutError | - | 2 |
| speed | TimeoutError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
