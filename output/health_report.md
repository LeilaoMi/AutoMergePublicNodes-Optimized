# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-06 10:44:32 |
| 运行耗时 | 287.1s |
| 订阅源总数 | 107 |
| 健康订阅源 | 96 |
| 原始节点 | 96057 |
| 去重后节点 | 25365 |
| TCP 可达 | 3000 |
| 真实可用 | 491 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 25365 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.1 |
| geo | 1.4 |
| tcp | 41.2 |
| probe | 89.5 |
| real_test | 115.6 |
| generate | 32.2 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 60557 |
| vmess | 12577 |
| shadowsocks | 11222 |
| trojan | 9271 |
| hysteria2 | 2029 |
| http | 138 |
| shadowsocksr | 125 |
| socks | 61 |
| anytls | 47 |
| hysteria | 18 |
| tuic | 12 |

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
| 83.88 | hysteria2 | 207.7 | 525.9 | 22.97 | 0.0 | 8.84 | 13.89 | 19.18 | Au1rxx-base64 | 66.94.121.46 |
| 78.93 | shadowsocks | 283.6 | 638.3 | 21.21 | 0.0 | 9.07 | 13.47 | 19.18 | Au1rxx-base64 | 173.244.56.9 |
| 78.63 | vless | 185.3 | 465.8 | 23.49 | 0.0 | 8.87 | 7.09 | 19.18 | Au1rxx-base64 | 216.167.94.71 |
| 78.34 | vless | 207.8 | 529.7 | 22.97 | 0.0 | 9.1 | 7.09 | 19.18 | Au1rxx-base64 | 172.235.43.210 |
| 78.22 | vless | 203.1 | 524.2 | 23.08 | 0.0 | 8.87 | 7.09 | 19.18 | Au1rxx-base64 | 172.233.139.46 |
| 78.18 | http | 429.8 | 1203.8 | 17.83 | 0.0 | 10.0 | 14.03 | 19.32 | zhangkai | 138.199.35.198 |
| 77.79 | vless | 221.6 | 534.6 | 22.65 | 0.0 | 8.87 | 7.09 | 19.18 | Au1rxx-base64 | 23.94.227.94 |
| 76.07 | http | 340.7 | 628.2 | 19.89 | 0.0 | 10.0 | 14.03 | 19.32 | zhangkai | 38.28.193.188 |
| 75.92 | shadowsocks | 293.2 | 656.7 | 20.99 | 0.0 | 10.0 | 13.47 | 19.18 | Au1rxx-base64 | 156.146.38.168 |
| 75.79 | shadowsocks | 221.4 | 523.4 | 22.65 | 0.0 | 9.06 | 13.47 | 19.18 | Au1rxx-base64 | 149.22.95.183 |
| 75.26 | vless | 243.5 | 240.7 | 22.14 | 5.97 | 9.81 | 7.09 | 16.42 | Surfboard-tg-mixed | 31.76.91.72 |
| 75.15 | shadowsocks | 200.5 | 485.6 | 23.14 | 0.0 | 8.86 | 13.47 | 19.18 | Au1rxx-base64 | 108.181.0.177 |
| 74.74 | shadowsocks | 342.9 | 801.2 | 19.84 | 0.0 | 9.14 | 13.47 | 19.18 | Au1rxx-base64 | 156.146.38.169 |
| 74.64 | vless | 190.2 | 520.3 | 23.37 | 0.0 | 10.0 | 7.09 | 19.18 | Au1rxx-base64 | 47.251.108.158 |
| 74.57 | http | 426.7 | 1192.2 | 17.9 | 0.0 | 10.0 | 14.03 | 19.32 | zhangkai | 138.199.35.216 |
| 74.51 | http | 177.9 | 482.2 | 23.66 | 0.0 | 0.0 | 14.03 | 19.32 | zhangkai | purposebydesig.club |
| 74.47 | vless | 284.0 | 768.9 | 21.2 | 0.0 | 10.0 | 7.09 | 19.18 | Au1rxx-base64 | 198.44.36.41 |
| 74.44 | vless | 198.5 | 506.4 | 23.18 | 0.0 | 8.87 | 7.09 | 19.18 | Au1rxx-base64 | 38.150.33.232 |
| 74.06 | vless | 225.9 | 516.1 | 22.55 | 0.0 | 10.0 | 7.09 | 16.42 | Surfboard-tg-mixed | 172.67.213.31 |
| 73.79 | shadowsocks | 303.0 | 640.3 | 20.76 | 0.0 | 10.0 | 13.47 | 16.42 | Surfboard-tg-mixed | 156.146.38.170 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.932 | 0.863 | 335 | 1781 | prefer |
| Surfboard-tg-mixed | 0.862 | 0.786 | 145 | 7318 | prefer |
| zhangkai | 0.846 | 0.87 | 23 | 144 | prefer |
| mheidari-all | 0.661 | 0.583 | 103 | 22388 | observe |
| DeltaKronecker-all | 0.48 | 1.0 | 4 | 5856 | observe |
| tg-oneclickvpnkeys | 0.363 | 1.0 | 3 | 133 | observe |
| xiaoji235-airport-v2ray-all | 0.335 | 1.0 | 1 | 6965 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4791 | observe |
| Epodonios-all | 0.255 | None | 0 | 7771 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3996 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 8223 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 6005 | observe |
| barry-far-vless | 0.255 | None | 0 | 6223 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4111 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| cn-block | ClientOSError | - | 42 |
| cn-block | TimeoutError | - | 20 |
| 204 | TimeoutError | - | 19 |
| geo | ClientOSError | - | 13 |
| speed | TimeoutError | - | 10 |
| 204 | ProxyError | - | 6 |
| 204 | ProxyConnectionError | - | 4 |
| geo | TimeoutError | - | 3 |
| speed | ClientOSError | - | 3 |
| 204 | ClientOSError | - | 2 |
| 204 | ServerDisconnectedError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
