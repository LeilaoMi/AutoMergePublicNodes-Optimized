# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-05 05:14:49 |
| 运行耗时 | 818.4s |
| 订阅源总数 | 107 |
| 健康订阅源 | 94 |
| 原始节点 | 98824 |
| 去重后节点 | 27507 |
| TCP 可达 | 3000 |
| 真实可用 | 548 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 27507 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.9 |
| geo | 1.5 |
| tcp | 46.9 |
| probe | 269.8 |
| real_test | 415.2 |
| generate | 77.1 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 59304 |
| vmess | 15513 |
| shadowsocks | 11390 |
| trojan | 10325 |
| hysteria2 | 1365 |
| http | 623 |
| shadowsocksr | 170 |
| socks | 68 |
| anytls | 30 |
| tuic | 19 |
| hysteria | 17 |

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
| 84.81 | vless | 200.4 | 521.3 | 23.14 | 0.0 | 10.0 | 12.29 | 19.38 | Au1rxx-base64 | 107.173.237.146 |
| 84.5 | vless | 213.8 | 534.0 | 22.83 | 0.0 | 10.0 | 12.29 | 19.38 | Au1rxx-base64 | 195.123.240.65 |
| 84.47 | vless | 215.2 | 504.5 | 22.8 | 0.0 | 10.0 | 12.29 | 19.38 | Au1rxx-base64 | 47.251.108.158 |
| 81.54 | vless | 308.9 | 744.2 | 20.63 | 0.0 | 10.0 | 12.29 | 19.38 | Au1rxx-base64 | 23.95.222.127 |
| 81.0 | hysteria2 | 321.6 | 738.2 | 20.33 | 0.0 | 10.0 | 14.44 | 19.38 | Au1rxx-base64 | 129.213.91.185 |
| 79.67 | vless | 228.2 | 508.4 | 22.5 | 0.0 | 10.0 | 12.29 | 19.38 | Au1rxx-base64 | 104.18.46.46 |
| 78.97 | vless | 258.2 | 466.2 | 21.8 | 0.0 | 10.0 | 12.29 | 19.38 | Au1rxx-base64 | 188.114.97.6 |
| 78.4 | shadowsocks | 306.9 | 782.0 | 20.67 | 0.0 | 10.0 | 13.37 | 19.38 | Au1rxx-base64 | 156.146.38.167 |
| 78.17 | trojan | 217.7 | 481.0 | 22.74 | 0.0 | 10.0 | 13.93 | 17.0 | mheidari-all | 43.173.90.202 |
| 78.0 | shadowsocks | 257.9 | 625.8 | 21.81 | 0.0 | 10.0 | 13.37 | 16.82 | Surfboard-tg-mixed | 156.146.38.169 |
| 77.42 | vless | 285.4 | 429.1 | 21.17 | 0.0 | 10.0 | 12.29 | 19.38 | Au1rxx-base64 | 172.64.32.103 |
| 76.93 | vless | 263.7 | 622.5 | 21.67 | 0.0 | 10.0 | 12.29 | 19.38 | Au1rxx-base64 | 104.18.47.113 |
| 76.91 | vless | 270.3 | 597.7 | 21.52 | 0.0 | 10.0 | 12.29 | 19.38 | Au1rxx-base64 | 15.204.97.216 |
| 76.9 | shadowsocks | 262.1 | 644.0 | 21.71 | 0.0 | 10.0 | 13.37 | 16.82 | Surfboard-tg-mixed | 156.146.38.168 |
| 76.78 | hysteria2 | 306.0 | 429.3 | 20.69 | 0.0 | 9.32 | 14.44 | 19.38 | Au1rxx-base64 | open.w2m.ink |
| 76.27 | hysteria2 | 351.0 | 766.2 | 19.65 | 0.0 | 10.0 | 14.44 | 17.0 | mheidari-all | 159.223.157.129 |
| 76.14 | shadowsocks | 215.7 | 537.9 | 22.79 | 0.0 | 10.0 | 13.37 | 19.38 | Au1rxx-base64 | 173.244.56.6 |
| 76.05 | vless | 212.8 | 500.0 | 22.85 | 0.0 | 10.0 | 12.29 | 19.38 | Au1rxx-base64 | 137.175.82.40 |
| 75.96 | trojan | 282.8 | 589.9 | 21.23 | 0.0 | 10.0 | 13.93 | 19.38 | Au1rxx-base64 | 44.255.123.205 |
| 75.87 | trojan | 367.8 | 674.8 | 19.26 | 0.0 | 9.07 | 13.93 | 19.38 | Au1rxx-base64 | happy-gibbon.rooster465.autos |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.96 | 0.887 | 363 | 1883 | prefer |
| Surfboard-tg-mixed | 0.931 | 0.861 | 72 | 7178 | prefer |
| ermaozi | 0.468 | 0.439 | 57 | 694 | observe |
| mheidari-all | 0.45 | 0.369 | 366 | 23195 | observe |
| DeltaKronecker-all | 0.332 | 0.286 | 14 | 5267 | observe |
| Epodonios-all | 0.255 | None | 0 | 7673 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9258 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5736 | observe |
| barry-far-vless | 0.255 | None | 0 | 6057 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4365 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |
| Au1rxx-clash | 0.25 | None | 0 | 1883 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 128 |
| speed | TimeoutError | - | 59 |
| geo | ClientOSError | - | 39 |
| 204 | ProxyError | - | 33 |
| cn-block | TimeoutError | - | 20 |
| 204 | ProxyConnectionError | - | 19 |
| 204 | TimeoutError | - | 16 |
| speed | ClientOSError | - | 10 |
| 204 | ClientOSError | - | 3 |
| cn-block | ClientOSError | - | 3 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
