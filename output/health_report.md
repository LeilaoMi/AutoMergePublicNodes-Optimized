# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-14 19:29:29 |
| 运行耗时 | 147.3s |
| 订阅源总数 | 107 |
| 健康订阅源 | 103 |
| 原始节点 | 81121 |
| 去重后节点 | 24269 |
| TCP 可达 | 3000 |
| 真实可用 | 165 |
| Verified 输出 | 165 |
| Global 输出 | 173 |
| All 输出 | 24269 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 3.0 |
| geo | 1.3 |
| tcp | 32.7 |
| probe | 44.8 |
| real_test | 49.5 |
| generate | 16.0 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 47823 |
| trojan | 11679 |
| vmess | 11038 |
| shadowsocks | 9841 |
| hysteria2 | 413 |
| http | 138 |
| shadowsocksr | 133 |
| socks | 38 |
| hysteria | 12 |
| anytls | 4 |
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
| 71.74 | trojan | 240.0 | 599.6 | 22.22 | 0.0 | 10.0 | 11.83 | 14.64 | DeltaKronecker-all | 64.94.95.117 |
| 71.12 | trojan | 244.4 | 582.3 | 22.12 | 0.0 | 10.0 | 11.83 | 14.64 | DeltaKronecker-all | 64.94.95.115 |
| 70.85 | shadowsocks | 338.0 | 739.8 | 19.95 | 0.0 | 10.0 | 11.97 | 15.92 | mheidari-all | 108.181.57.93 |
| 70.1 | shadowsocks | 354.4 | 840.9 | 19.57 | 0.0 | 10.0 | 11.97 | 15.92 | mheidari-all | 185.196.61.82 |
| 70.09 | vmess | 431.8 | 1097.4 | 17.78 | 0.0 | 10.0 | 12.86 | 14.64 | DeltaKronecker-all | 67.220.95.3 |
| 68.42 | vmess | 485.7 | 1084.4 | 16.54 | 0.0 | 10.0 | 12.86 | 15.62 | Surfboard-tg-mixed | 67.220.85.46 |
| 67.55 | trojan | 609.3 | 1621.2 | 13.67 | 0.0 | 10.0 | 11.83 | 15.62 | Surfboard-tg-mixed | 64.94.95.118 |
| 67.35 | trojan | 290.0 | 665.8 | 21.07 | 0.0 | 10.0 | 11.83 | 14.64 | DeltaKronecker-all | 64.94.95.114 |
| 67.31 | shadowsocks | 245.1 | 610.6 | 22.1 | 0.0 | 10.0 | 11.97 | 7.24 | Au1rxx-base64 | 156.146.38.168 |
| 67.3 | shadowsocks | 245.6 | 587.8 | 22.09 | 0.0 | 10.0 | 11.97 | 7.24 | Au1rxx-base64 | 156.146.38.167 |
| 66.95 | shadowsocks | 364.7 | 901.1 | 19.34 | 0.0 | 10.0 | 11.97 | 15.92 | mheidari-all | 198.98.53.130 |
| 66.62 | trojan | 346.8 | 644.8 | 19.75 | 0.0 | 10.0 | 11.83 | 15.62 | Surfboard-tg-mixed | 162.159.38.62 |
| 66.28 | shadowsocks | 248.8 | 607.3 | 22.02 | 0.0 | 10.0 | 11.97 | 7.24 | Au1rxx-base64 | 156.146.38.170 |
| 64.09 | shadowsocks | 455.6 | 885.8 | 17.23 | 0.0 | 10.0 | 11.97 | 15.92 | mheidari-all | 172.245.235.84 |
| 64.09 | trojan | 484.6 | 645.3 | 16.56 | 0.0 | 10.0 | 11.83 | 15.62 | Surfboard-tg-mixed | 199.232.78.140 |
| 64.06 | vless | 404.9 | 1097.3 | 18.4 | 0.0 | 10.0 | 1.02 | 14.64 | DeltaKronecker-all | 20.84.155.134 |
| 63.68 | shadowsocks | 300.4 | 696.5 | 20.82 | 0.0 | 10.0 | 11.97 | 7.24 | Au1rxx-base64 | 37.19.198.160 |
| 63.51 | trojan | 422.6 | 402.8 | 18.0 | 0.0 | 9.58 | 11.83 | 14.64 | DeltaKronecker-all | 18.179.120.96 |
| 62.73 | http | 730.8 | 1036.0 | 10.86 | 0.0 | 9.31 | 14.61 | 19.52 | snakem982 | 84.239.49.219 |
| 62.68 | http | 727.7 | 1005.4 | 10.93 | 0.0 | 9.35 | 14.61 | 19.52 | snakem982 | 84.239.49.247 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| DeltaKronecker-all | 0.772 | 0.7 | 50 | 7942 | prefer |
| Surfboard-tg-mixed | 0.665 | 0.588 | 51 | 5623 | observe |
| mheidari-all | 0.653 | 0.574 | 94 | 18091 | observe |
| Au1rxx-base64 | 0.494 | 0.875 | 8 | 139 | observe |
| xiaoji235-airport-v2ray-all | 0.391 | 1.0 | 2 | 3836 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4019 | observe |
| Epodonios-all | 0.255 | None | 0 | 6538 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3971 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6320 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4338 | observe |
| barry-far-vless | 0.255 | None | 0 | 4852 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5187 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 28 |
| speed | ClientOSError | - | 16 |
| 204 | ProxyError | - | 7 |
| 204 | TimeoutError | - | 5 |
| geo | ClientOSError | - | 4 |
| cn-block | ClientOSError | - | 4 |
| cn-block | ProxyError | - | 3 |
| 204 | ClientOSError | - | 3 |
| speed | TimeoutError | - | 3 |
| cn-block | TimeoutError | - | 2 |
| speed | ProxyError | - | 2 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 251 | 165 | - |
| global | False | 261 | 173 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
