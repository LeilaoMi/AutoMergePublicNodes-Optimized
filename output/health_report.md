# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-24 17:02:28 |
| 运行耗时 | 554.2s |
| 订阅源总数 | 107 |
| 健康订阅源 | 95 |
| 原始节点 | 97092 |
| 去重后节点 | 26416 |
| TCP 可达 | 3000 |
| 真实可用 | 405 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 26416 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.6 |
| geo | 1.4 |
| tcp | 43.7 |
| probe | 220.4 |
| real_test | 202.3 |
| generate | 80.8 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 59649 |
| vmess | 14751 |
| shadowsocks | 11245 |
| trojan | 9033 |
| hysteria2 | 1569 |
| http | 551 |
| shadowsocksr | 173 |
| socks | 74 |
| anytls | 22 |
| hysteria | 18 |
| tuic | 7 |

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
| 80.86 | shadowsocks | 218.3 | 544.4 | 22.72 | 0.0 | 10.0 | 13.7 | 18.44 | Surfboard-tg-mixed | 173.244.56.6 |
| 80.2 | vless | 226.5 | 573.1 | 22.54 | 0.0 | 10.0 | 9.22 | 18.44 | Surfboard-tg-mixed | 172.235.38.85 |
| 79.48 | shadowsocks | 260.4 | 632.6 | 21.75 | 0.0 | 10.0 | 13.7 | 18.32 | Au1rxx-base64 | 156.146.38.167 |
| 79.46 | shadowsocks | 265.7 | 646.7 | 21.63 | 0.0 | 10.0 | 13.7 | 18.44 | Surfboard-tg-mixed | 156.146.38.169 |
| 79.44 | vless | 201.4 | 526.8 | 23.12 | 0.0 | 8.78 | 9.22 | 18.32 | Au1rxx-base64 | 172.235.43.210 |
| 78.63 | shadowsocks | 314.6 | 826.6 | 20.49 | 0.0 | 10.0 | 13.7 | 18.44 | Surfboard-tg-mixed | 173.244.56.9 |
| 77.74 | vless | 197.7 | 517.9 | 23.2 | 0.0 | 10.0 | 9.22 | 18.32 | Au1rxx-base64 | 192.3.247.109 |
| 77.0 | hysteria2 | 368.4 | 851.9 | 19.25 | 0.0 | 10.0 | 14.25 | 18.32 | Au1rxx-base64 | 66.94.121.46 |
| 75.54 | vless | 323.5 | 763.8 | 20.29 | 0.0 | 10.0 | 9.22 | 18.44 | Surfboard-tg-mixed | 5.78.159.214 |
| 74.91 | shadowsocks | 190.3 | 506.3 | 23.37 | 0.0 | 10.0 | 13.7 | 12.34 | mheidari-all | 192.3.247.109 |
| 74.34 | vless | 215.8 | 569.4 | 22.78 | 0.0 | 10.0 | 9.22 | 12.34 | mheidari-all | 172.233.139.46 |
| 73.76 | shadowsocks | 299.5 | 335.2 | 20.84 | 2.43 | 9.9 | 13.7 | 18.32 | Au1rxx-base64 | 149.22.87.241 |
| 73.58 | shadowsocks | 259.5 | 623.6 | 21.77 | 0.0 | 10.0 | 13.7 | 12.34 | mheidari-all | 156.146.38.168 |
| 73.21 | shadowsocks | 256.0 | 620.6 | 21.85 | 0.0 | 10.0 | 13.7 | 12.34 | mheidari-all | 156.146.38.170 |
| 73.15 | hysteria2 | 434.9 | 898.6 | 17.71 | 0.0 | 10.0 | 14.25 | 18.32 | Au1rxx-base64 | 159.223.157.129 |
| 73.01 | shadowsocks | 272.4 | 709.7 | 21.47 | 0.0 | 10.0 | 13.7 | 12.34 | mheidari-all | 108.181.118.10 |
| 72.8 | shadowsocks | 544.9 | 1508.3 | 15.16 | 0.0 | 10.0 | 13.7 | 18.44 | Surfboard-tg-mixed | 108.181.0.177 |
| 72.14 | vless | 288.5 | 592.7 | 21.1 | 0.0 | 10.0 | 9.22 | 18.32 | Au1rxx-base64 | 104.18.39.218 |
| 71.61 | shadowsocks | 344.4 | 641.1 | 19.8 | 0.0 | 8.77 | 13.7 | 18.32 | Au1rxx-base64 | 198.98.53.130 |
| 71.29 | vless | 248.1 | 591.3 | 22.03 | 0.0 | 10.0 | 9.22 | 18.32 | Au1rxx-base64 | 172.64.32.103 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.988 | 0.924 | 262 | 1697 | prefer |
| mheidari-all | 0.95 | 0.881 | 67 | 22258 | prefer |
| Surfboard-tg-mixed | 0.793 | 0.717 | 106 | 7421 | prefer |
| ermaozi | 0.669 | 0.667 | 33 | 298 | observe |
| DeltaKronecker-all | 0.438 | 1.0 | 3 | 5845 | observe |
| roosterkid-openproxylist-v2ray | 0.261 | 1.0 | 1 | 149 | observe |
| tg-oneclickvpnkeys | 0.258 | 1.0 | 1 | 85 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5307 | observe |
| Epodonios-all | 0.255 | None | 0 | 7498 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9120 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5991 | observe |
| barry-far-vless | 0.255 | None | 0 | 5901 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4305 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | ProxyError | - | 18 |
| 204 | TimeoutError | - | 15 |
| cn-block | TimeoutError | - | 10 |
| speed | TimeoutError | - | 7 |
| cn-block | ProxyError | - | 6 |
| geo | TimeoutError | - | 6 |
| cn-block | ClientOSError | - | 4 |
| speed | ClientOSError | - | 3 |
| geo | ProxyError | - | 2 |
| 204 | ClientOSError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
