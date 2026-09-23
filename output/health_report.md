# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-23 16:43:19 |
| 运行耗时 | 585.8s |
| 订阅源总数 | 107 |
| 健康订阅源 | 96 |
| 原始节点 | 97200 |
| 去重后节点 | 26542 |
| TCP 可达 | 3000 |
| 真实可用 | 436 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 26542 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.4 |
| geo | 1.6 |
| tcp | 43.1 |
| probe | 267.0 |
| real_test | 184.2 |
| generate | 84.4 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 60136 |
| vmess | 14763 |
| shadowsocks | 11172 |
| trojan | 8774 |
| hysteria2 | 1497 |
| http | 562 |
| shadowsocksr | 171 |
| socks | 74 |
| anytls | 25 |
| hysteria | 18 |
| tuic | 8 |

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
| 82.34 | vless | 202.8 | 528.1 | 23.08 | 0.0 | 8.96 | 10.44 | 19.86 | Au1rxx-base64 | 172.235.43.210 |
| 80.91 | shadowsocks | 261.9 | 633.5 | 21.72 | 0.0 | 10.0 | 14.18 | 19.86 | Au1rxx-base64 | 156.146.38.170 |
| 80.34 | shadowsocks | 258.2 | 712.1 | 21.8 | 0.0 | 10.0 | 14.18 | 19.86 | Au1rxx-base64 | 129.146.124.141 |
| 79.78 | shadowsocks | 346.4 | 886.6 | 19.76 | 0.0 | 10.0 | 14.18 | 19.86 | Au1rxx-base64 | 156.146.38.169 |
| 79.56 | vless | 321.0 | 786.2 | 20.35 | 0.0 | 8.96 | 10.44 | 19.86 | Au1rxx-base64 | 195.123.240.65 |
| 78.91 | vless | 275.6 | 599.1 | 21.4 | 0.0 | 10.0 | 10.44 | 19.86 | Au1rxx-base64 | 15.204.97.216 |
| 78.57 | vless | 216.2 | 498.3 | 22.77 | 0.0 | 10.0 | 10.44 | 19.86 | Au1rxx-base64 | 104.18.39.218 |
| 78.48 | vless | 198.5 | 524.8 | 23.18 | 0.0 | 10.0 | 10.44 | 19.86 | Au1rxx-base64 | 192.3.247.109 |
| 78.37 | shadowsocks | 200.6 | 539.6 | 23.13 | 0.0 | 10.0 | 14.18 | 15.56 | mheidari-all | 192.3.247.109 |
| 78.33 | vless | 201.5 | 525.3 | 23.11 | 0.0 | 10.0 | 10.44 | 14.78 | Surfboard-tg-mixed | 172.235.38.85 |
| 77.92 | shadowsocks | 311.4 | 634.5 | 20.57 | 0.0 | 10.0 | 14.18 | 19.86 | Au1rxx-base64 | 23.150.248.20 |
| 77.84 | vless | 248.1 | 494.9 | 22.04 | 0.0 | 10.0 | 10.44 | 19.86 | Au1rxx-base64 | 172.64.229.2 |
| 77.36 | shadowsocks | 232.2 | 554.9 | 22.4 | 0.0 | 10.0 | 14.18 | 14.78 | Surfboard-tg-mixed | 173.244.56.9 |
| 76.99 | vless | 206.9 | 522.1 | 22.99 | 0.0 | 10.0 | 10.44 | 15.56 | mheidari-all | 172.233.139.46 |
| 76.44 | shadowsocks | 275.4 | 673.4 | 21.4 | 0.0 | 10.0 | 14.18 | 15.56 | mheidari-all | 156.146.38.168 |
| 76.24 | shadowsocks | 424.5 | 1122.5 | 17.95 | 0.0 | 10.0 | 14.18 | 19.86 | Au1rxx-base64 | 156.146.38.167 |
| 76.16 | shadowsocks | 296.4 | 766.5 | 20.92 | 0.0 | 10.0 | 14.18 | 15.56 | mheidari-all | 108.181.118.10 |
| 75.39 | hysteria2 | 451.2 | 891.4 | 17.33 | 0.0 | 10.0 | 14.32 | 19.86 | Au1rxx-base64 | 66.94.121.46 |
| 75.35 | shadowsocks | 297.4 | 775.6 | 20.89 | 0.0 | 10.0 | 14.18 | 14.78 | Surfboard-tg-mixed | 108.181.0.177 |
| 74.66 | shadowsocks | 568.3 | 1599.6 | 14.62 | 0.0 | 10.0 | 14.18 | 19.86 | Au1rxx-base64 | 173.244.56.6 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.99 | 0.927 | 273 | 1665 | prefer |
| ermaozi | 0.793 | 0.8 | 30 | 291 | prefer |
| Surfboard-tg-mixed | 0.604 | 0.525 | 61 | 7138 | observe |
| mheidari-all | 0.599 | 0.519 | 237 | 22163 | observe |
| DeltaKronecker-all | 0.335 | 1.0 | 1 | 6471 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| tg-oneclickvpnkeys | 0.259 | 1.0 | 1 | 88 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5131 | observe |
| Epodonios-all | 0.255 | None | 0 | 7512 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9407 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5827 | observe |
| barry-far-vless | 0.255 | None | 0 | 6042 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4187 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| cn-block | ClientOSError | - | 48 |
| geo | ClientOSError | - | 37 |
| 204 | TimeoutError | - | 30 |
| cn-block | TimeoutError | - | 22 |
| 204 | ProxyError | - | 18 |
| speed | TimeoutError | - | 9 |
| 204 | ClientOSError | - | 4 |
| geo | ProxyError | - | 3 |
| speed | ClientOSError | - | 2 |
| geo | TimeoutError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
