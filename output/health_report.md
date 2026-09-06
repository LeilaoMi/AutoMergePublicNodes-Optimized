# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-06 04:02:28 |
| 运行耗时 | 277.6s |
| 订阅源总数 | 107 |
| 健康订阅源 | 96 |
| 原始节点 | 97417 |
| 去重后节点 | 25569 |
| TCP 可达 | 3000 |
| 真实可用 | 577 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 25569 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.3 |
| geo | 1.4 |
| tcp | 42.7 |
| probe | 67.2 |
| real_test | 139.3 |
| generate | 22.8 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 62163 |
| vmess | 12654 |
| shadowsocks | 11036 |
| trojan | 9207 |
| hysteria2 | 1953 |
| http | 144 |
| shadowsocksr | 125 |
| socks | 65 |
| anytls | 38 |
| hysteria | 18 |
| tuic | 14 |

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
| 80.27 | shadowsocks | 270.1 | 717.3 | 21.52 | 0.0 | 10.0 | 13.79 | 18.96 | Au1rxx-base64 | 156.146.38.167 |
| 79.05 | shadowsocks | 294.6 | 714.6 | 20.96 | 0.0 | 10.0 | 13.79 | 18.96 | Au1rxx-base64 | 37.19.198.244 |
| 78.72 | hysteria2 | 275.2 | 591.2 | 21.41 | 0.0 | 10.0 | 13.27 | 18.96 | Au1rxx-base64 | 66.94.121.46 |
| 78.54 | trojan | 284.2 | 675.1 | 21.2 | 0.0 | 10.0 | 11.38 | 18.96 | Au1rxx-base64 | 64.94.95.114 |
| 78.2 | shadowsocks | 257.7 | 666.9 | 21.81 | 0.0 | 10.0 | 13.79 | 16.6 | Surfboard-tg-mixed | 156.146.38.170 |
| 78.12 | shadowsocks | 261.1 | 643.1 | 21.73 | 0.0 | 10.0 | 13.79 | 16.6 | Surfboard-tg-mixed | 156.146.38.168 |
| 78.07 | shadowsocks | 283.0 | 686.4 | 21.23 | 0.0 | 10.0 | 13.79 | 18.96 | Au1rxx-base64 | 37.19.198.160 |
| 76.78 | vless | 342.5 | 733.9 | 19.85 | 0.0 | 10.0 | 10.61 | 18.96 | Au1rxx-base64 | 169.40.42.225 |
| 76.56 | vless | 296.3 | 597.7 | 20.92 | 0.0 | 10.0 | 10.61 | 18.96 | Au1rxx-base64 | 172.233.139.46 |
| 76.27 | vless | 279.4 | 262.8 | 21.31 | 5.14 | 9.59 | 10.61 | 16.6 | Surfboard-tg-mixed | 31.76.91.72 |
| 76.26 | vless | 408.5 | 827.2 | 18.32 | 0.0 | 10.0 | 10.61 | 18.96 | Au1rxx-base64 | 169.40.42.223 |
| 75.91 | vless | 413.2 | 983.7 | 18.21 | 0.0 | 10.0 | 10.61 | 18.96 | Au1rxx-base64 | 169.40.42.15 |
| 75.85 | shadowsocks | 265.2 | 697.3 | 21.64 | 0.0 | 10.0 | 13.79 | 18.96 | Au1rxx-base64 | 156.146.38.169 |
| 75.73 | vless | 454.2 | 1197.9 | 17.26 | 0.0 | 10.0 | 10.61 | 18.96 | Au1rxx-base64 | 45.138.100.226 |
| 75.72 | trojan | 301.5 | 752.5 | 20.8 | 0.0 | 10.0 | 11.38 | 18.96 | Au1rxx-base64 | 64.94.95.118 |
| 75.55 | vless | 343.2 | 669.5 | 19.83 | 0.0 | 10.0 | 10.61 | 18.96 | Au1rxx-base64 | 169.40.42.231 |
| 75.51 | vless | 432.1 | 1086.9 | 17.77 | 0.0 | 10.0 | 10.61 | 18.96 | Au1rxx-base64 | 185.95.231.156 |
| 75.49 | vless | 439.7 | 963.9 | 17.6 | 0.0 | 10.0 | 10.61 | 18.96 | Au1rxx-base64 | 169.40.42.163 |
| 75.21 | shadowsocks | 370.6 | 906.4 | 19.2 | 0.0 | 10.0 | 13.79 | 18.96 | Au1rxx-base64 | 38.180.135.156 |
| 74.99 | trojan | 345.6 | 905.2 | 19.78 | 0.0 | 10.0 | 11.38 | 18.96 | Au1rxx-base64 | 64.94.95.117 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.966 | 1.0 | 23 | 144 | prefer |
| Au1rxx-base64 | 0.959 | 0.889 | 314 | 1827 | prefer |
| Surfboard-tg-mixed | 0.821 | 0.744 | 199 | 7381 | prefer |
| tg-oneclickvpnkeys | 0.414 | 0.833 | 6 | 132 | observe |
| mheidari-all | 0.363 | 0.282 | 425 | 22409 | observe |
| xiaoji235-airport-v2ray-all | 0.287 | 0.5 | 2 | 6965 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4887 | observe |
| DeltaKronecker-all | 0.255 | None | 0 | 6212 | observe |
| Epodonios-all | 0.255 | None | 0 | 7876 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 8608 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 6075 | observe |
| barry-far-vless | 0.255 | None | 0 | 6398 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4087 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 158 |
| geo | ClientOSError | - | 77 |
| speed | TimeoutError | - | 48 |
| speed | ClientOSError | - | 32 |
| cn-block | ClientOSError | - | 31 |
| 204 | TimeoutError | - | 19 |
| cn-block | TimeoutError | - | 12 |
| 204 | ProxyError | - | 9 |
| speed | ClientPayloadError | - | 4 |
| 204 | ClientOSError | - | 2 |
| cn-block | ProxyError | - | 1 |
| speed | ProxyError | - | 1 |
| 204 | ServerDisconnectedError | - | 1 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
