# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-04 12:16:04 |
| 运行耗时 | 631.1s |
| 订阅源总数 | 107 |
| 健康订阅源 | 94 |
| 原始节点 | 99561 |
| 去重后节点 | 27370 |
| TCP 可达 | 3000 |
| 真实可用 | 406 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 27370 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.9 |
| geo | 1.6 |
| tcp | 47.0 |
| probe | 231.7 |
| real_test | 191.5 |
| generate | 152.3 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 59731 |
| vmess | 15756 |
| shadowsocks | 11573 |
| trojan | 10122 |
| hysteria2 | 1566 |
| http | 521 |
| shadowsocksr | 172 |
| socks | 70 |
| anytls | 27 |
| hysteria | 17 |
| tuic | 6 |

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
| 83.63 | hysteria2 | 254.8 | 614.7 | 21.88 | 0.0 | 10.0 | 13.64 | 19.54 | Au1rxx-base64 | 66.94.121.46 |
| 82.17 | hysteria2 | 262.6 | 255.7 | 21.7 | 5.41 | 9.35 | 13.64 | 19.54 | Au1rxx-base64 | open.w2m.ink |
| 81.46 | shadowsocks | 235.1 | 605.7 | 22.33 | 0.0 | 10.0 | 13.59 | 19.54 | Au1rxx-base64 | 156.146.38.167 |
| 79.94 | shadowsocks | 256.2 | 603.4 | 21.85 | 0.0 | 10.0 | 13.59 | 19.54 | Au1rxx-base64 | 5.78.51.123 |
| 78.33 | shadowsocks | 241.1 | 617.8 | 22.2 | 0.0 | 10.0 | 13.59 | 19.54 | Au1rxx-base64 | 156.146.38.168 |
| 77.18 | shadowsocks | 272.7 | 582.4 | 21.46 | 0.0 | 10.0 | 13.59 | 19.54 | Au1rxx-base64 | 173.244.56.9 |
| 76.08 | shadowsocks | 241.3 | 624.7 | 22.19 | 0.0 | 10.0 | 13.59 | 14.3 | Surfboard-tg-mixed | 156.146.38.169 |
| 75.38 | shadowsocks | 340.6 | 774.6 | 19.89 | 0.0 | 10.0 | 13.59 | 19.54 | Au1rxx-base64 | 37.19.198.236 |
| 74.35 | hysteria2 | 426.4 | 1101.1 | 17.91 | 0.0 | 10.0 | 13.64 | 14.3 | Surfboard-tg-mixed | 129.213.91.185 |
| 74.3 | vless | 288.2 | 555.6 | 21.11 | 0.0 | 10.0 | 6.24 | 19.54 | Au1rxx-base64 | 195.123.240.65 |
| 74.16 | vless | 269.8 | 597.0 | 21.53 | 0.0 | 10.0 | 6.24 | 19.54 | Au1rxx-base64 | 15.204.97.216 |
| 73.58 | shadowsocks | 264.8 | 520.1 | 21.65 | 0.0 | 10.0 | 13.59 | 19.54 | Au1rxx-base64 | 108.181.118.10 |
| 73.54 | shadowsocks | 431.8 | 1044.5 | 17.78 | 0.0 | 10.0 | 13.59 | 19.54 | Au1rxx-base64 | 185.156.47.97 |
| 73.4 | http | 252.3 | 570.2 | 21.94 | 0.0 | 10.0 | 10.96 | 14.6 | ermaozi | 138.199.35.198 |
| 73.28 | shadowsocks | 421.9 | 987.0 | 18.01 | 0.0 | 10.0 | 13.59 | 19.54 | Au1rxx-base64 | 15.204.233.41 |
| 73.0 | shadowsocks | 338.0 | 771.5 | 19.95 | 0.0 | 10.0 | 13.59 | 19.54 | Au1rxx-base64 | 37.19.198.244 |
| 72.62 | shadowsocks | 382.8 | 722.7 | 18.92 | 0.0 | 10.0 | 13.59 | 19.54 | Au1rxx-base64 | 108.181.57.93 |
| 72.39 | shadowsocks | 300.3 | 637.5 | 20.83 | 0.0 | 10.0 | 13.59 | 19.54 | Au1rxx-base64 | 198.98.53.130 |
| 72.02 | vless | 320.2 | 655.3 | 20.37 | 0.0 | 10.0 | 6.24 | 19.54 | Au1rxx-base64 | 172.235.43.210 |
| 71.87 | vless | 244.6 | 546.9 | 22.12 | 0.0 | 10.0 | 6.24 | 19.54 | Au1rxx-base64 | 45.32.69.110 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.949 | 0.879 | 297 | 1816 | prefer |
| ermaozi | 0.949 | 0.958 | 24 | 646 | prefer |
| mheidari-all | 0.863 | 0.795 | 44 | 23332 | prefer |
| Surfboard-tg-mixed | 0.855 | 0.78 | 109 | 7269 | prefer |
| ermaozi-get_subscribe | 0.289 | 0.667 | 3 | 505 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5173 | observe |
| Epodonios-all | 0.255 | None | 0 | 7796 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3996 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9804 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5821 | observe |
| barry-far-vless | 0.255 | None | 0 | 6148 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4338 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |
| Au1rxx-clash | 0.248 | None | 0 | 1816 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| cn-block | TimeoutError | - | 30 |
| 204 | TimeoutError | - | 13 |
| geo | TimeoutError | - | 10 |
| 204 | ProxyError | - | 5 |
| cn-block | ClientOSError | - | 5 |
| speed | TimeoutError | - | 5 |
| geo | ClientOSError | - | 3 |
| cn-block | ProxyError | - | 2 |
| speed | ClientOSError | - | 2 |
| 204 | ProxyConnectionError | - | 1 |
| 204 | ClientOSError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
