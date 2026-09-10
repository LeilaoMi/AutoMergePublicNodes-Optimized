# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-10 16:21:34 |
| 运行耗时 | 696.8s |
| 订阅源总数 | 107 |
| 健康订阅源 | 96 |
| 原始节点 | 91096 |
| 去重后节点 | 24439 |
| TCP 可达 | 3000 |
| 真实可用 | 444 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 24439 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.0 |
| geo | 1.5 |
| tcp | 41.1 |
| probe | 272.2 |
| real_test | 291.7 |
| generate | 83.4 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 55142 |
| vmess | 13254 |
| shadowsocks | 11137 |
| trojan | 8830 |
| hysteria2 | 1907 |
| http | 608 |
| shadowsocksr | 127 |
| socks | 58 |
| hysteria | 15 |
| tuic | 10 |
| anytls | 8 |

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
| 82.21 | vless | 223.3 | 569.8 | 22.61 | 0.0 | 8.85 | 11.29 | 19.46 | Au1rxx-base64 | 38.209.125.45 |
| 81.49 | vless | 205.6 | 491.9 | 23.02 | 0.0 | 8.72 | 11.29 | 19.46 | Au1rxx-base64 | 31.58.50.200 |
| 81.49 | vless | 252.4 | 442.6 | 21.94 | 0.0 | 8.8 | 11.29 | 19.46 | Au1rxx-base64 | 172.235.43.210 |
| 80.79 | vless | 274.5 | 691.5 | 21.42 | 0.0 | 8.62 | 11.29 | 19.46 | Au1rxx-base64 | 172.233.139.46 |
| 80.03 | shadowsocks | 223.1 | 541.1 | 22.61 | 0.0 | 8.57 | 13.89 | 19.46 | Au1rxx-base64 | 108.181.0.177 |
| 79.8 | vless | 317.8 | 838.4 | 20.42 | 0.0 | 8.63 | 11.29 | 19.46 | Au1rxx-base64 | 15.204.97.216 |
| 79.44 | shadowsocks | 202.5 | 501.5 | 23.09 | 0.0 | 10.0 | 13.89 | 16.96 | Surfboard-tg-mixed | 108.181.118.10 |
| 79.24 | shadowsocks | 232.6 | 561.6 | 22.39 | 0.0 | 10.0 | 13.89 | 16.96 | Surfboard-tg-mixed | 173.244.56.9 |
| 78.42 | shadowsocks | 268.4 | 672.1 | 21.57 | 0.0 | 10.0 | 13.89 | 16.96 | Surfboard-tg-mixed | 173.244.56.6 |
| 76.87 | vless | 314.5 | 815.7 | 20.5 | 0.0 | 8.62 | 11.29 | 19.46 | Au1rxx-base64 | 15.204.97.198 |
| 75.73 | hysteria2 | 376.4 | 784.8 | 19.07 | 0.0 | 9.07 | 14.38 | 19.46 | Au1rxx-base64 | 159.223.157.129 |
| 75.22 | vless | 395.8 | 1065.3 | 18.62 | 0.0 | 8.85 | 11.29 | 19.46 | Au1rxx-base64 | 15.204.97.195 |
| 75.07 | hysteria2 | 294.7 | 581.8 | 20.96 | 0.0 | 4.57 | 14.38 | 19.46 | Au1rxx-base64 | starlink-ft.251313.xyz |
| 74.79 | vless | 345.8 | 752.1 | 19.77 | 0.0 | 8.66 | 11.29 | 19.46 | Au1rxx-base64 | 79.141.172.154 |
| 74.74 | shadowsocks | 292.6 | 660.6 | 21.0 | 0.0 | 8.63 | 13.89 | 19.46 | Au1rxx-base64 | 156.146.38.169 |
| 74.7 | shadowsocks | 238.9 | 583.5 | 22.25 | 0.0 | 10.0 | 13.89 | 12.56 | mheidari-all | 149.22.95.183 |
| 74.38 | shadowsocks | 293.3 | 658.3 | 20.99 | 0.0 | 10.0 | 13.89 | 16.96 | Surfboard-tg-mixed | 156.146.38.167 |
| 73.66 | shadowsocks | 326.4 | 331.3 | 20.22 | 2.58 | 8.55 | 13.89 | 19.46 | Au1rxx-base64 | 84.247.155.196 |
| 72.99 | vless | 213.8 | 548.2 | 22.83 | 0.0 | 8.6 | 11.29 | 19.46 | Au1rxx-base64 | 107.173.237.146 |
| 72.7 | vless | 346.2 | 383.8 | 19.76 | 0.61 | 9.03 | 11.29 | 19.46 | Au1rxx-base64 | 130.12.102.62 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.948 | 0.883 | 273 | 1693 | prefer |
| Surfboard-tg-mixed | 0.849 | 0.773 | 132 | 7191 | prefer |
| ermaozi | 0.824 | 0.833 | 24 | 405 | prefer |
| mheidari-all | 0.599 | 0.52 | 152 | 19266 | observe |
| tg-oneclickvpnkeys | 0.264 | 1.0 | 1 | 214 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4995 | observe |
| Epodonios-all | 0.255 | None | 0 | 7902 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3996 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 8955 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5790 | observe |
| barry-far-vless | 0.255 | None | 0 | 6248 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4358 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 3508 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.243 | None | 0 | 1693 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | ClientOSError | - | 46 |
| 204 | TimeoutError | - | 22 |
| cn-block | ClientOSError | - | 19 |
| 204 | ProxyError | - | 15 |
| cn-block | TimeoutError | - | 15 |
| speed | ClientOSError | - | 9 |
| speed | TimeoutError | - | 9 |
| geo | TimeoutError | - | 4 |
| 204 | ProxyConnectionError | - | 2 |
| speed | ProxyError | - | 2 |
| cn-block | ProxyError | - | 1 |
| 204 | ClientOSError | - | 1 |
| geo | ProxyError | - | 1 |
| geo | parse | TimeoutError | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
