# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-13 14:50:38 |
| 运行耗时 | 225.2s |
| 订阅源总数 | 107 |
| 健康订阅源 | 103 |
| 原始节点 | 77707 |
| 去重后节点 | 23895 |
| TCP 可达 | 3000 |
| 真实可用 | 208 |
| Verified 输出 | 208 |
| Global 输出 | 222 |
| All 输出 | 23895 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 3.1 |
| geo | 1.3 |
| tcp | 32.2 |
| probe | 44.3 |
| real_test | 97.1 |
| generate | 47.3 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 45162 |
| trojan | 11424 |
| vmess | 10707 |
| shadowsocks | 9708 |
| hysteria2 | 388 |
| shadowsocksr | 146 |
| http | 138 |
| socks | 26 |
| hysteria | 6 |
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
| 70.62 | vless | 201.7 | 480.7 | 23.11 | 0.0 | 10.0 | 2.21 | 16.3 | mheidari-all | 104.16.9.20 |
| 70.33 | vless | 214.0 | 502.5 | 22.82 | 0.0 | 10.0 | 2.21 | 16.3 | mheidari-all | 104.25.161.29 |
| 69.59 | vless | 202.9 | 476.1 | 23.08 | 0.0 | 10.0 | 2.21 | 16.3 | mheidari-all | 172.67.209.126 |
| 69.2 | shadowsocks | 199.6 | 487.3 | 23.16 | 0.0 | 10.0 | 11.55 | 16.3 | mheidari-all | 216.105.168.18 |
| 69.0 | trojan | 281.0 | 625.3 | 21.27 | 0.0 | 10.0 | 11.73 | 13.76 | DeltaKronecker-all | 64.94.95.115 |
| 68.73 | trojan | 279.5 | 631.6 | 21.31 | 0.0 | 10.0 | 11.73 | 13.76 | DeltaKronecker-all | 64.94.95.117 |
| 68.37 | trojan | 290.7 | 653.6 | 21.05 | 0.0 | 10.0 | 11.73 | 13.76 | DeltaKronecker-all | 64.94.95.114 |
| 63.85 | vless | 278.1 | 685.5 | 21.34 | 0.0 | 10.0 | 2.21 | 16.3 | mheidari-all | 69.46.46.39 |
| 62.89 | trojan | 439.4 | 365.2 | 17.61 | 1.31 | 9.37 | 11.73 | 13.66 | Surfboard-tg-mixed | 119.246.1.143 |
| 62.68 | vless | 328.6 | 835.4 | 20.17 | 0.0 | 10.0 | 2.21 | 16.3 | mheidari-all | 69.46.46.84 |
| 62.6 | trojan | 482.1 | 414.7 | 16.62 | 0.0 | 10.0 | 11.73 | 13.76 | DeltaKronecker-all | 172.67.149.1 |
| 62.59 | vless | 319.0 | 768.1 | 20.39 | 0.0 | 10.0 | 2.21 | 16.3 | mheidari-all | 69.46.46.109 |
| 62.55 | vless | 328.2 | 793.5 | 20.18 | 0.0 | 10.0 | 2.21 | 16.3 | mheidari-all | 69.46.46.9 |
| 62.38 | vless | 231.8 | 528.4 | 22.41 | 0.0 | 10.0 | 2.21 | 13.76 | DeltaKronecker-all | 69.46.46.97 |
| 62.13 | trojan | 500.4 | 446.6 | 16.19 | 0.0 | 10.0 | 11.73 | 13.76 | DeltaKronecker-all | 104.21.29.125 |
| 61.74 | http | 764.1 | 1049.6 | 10.09 | 0.0 | 9.25 | 14.61 | 19.52 | snakem982 | 193.176.84.31 |
| 61.58 | trojan | 689.2 | 1835.9 | 11.82 | 0.0 | 10.0 | 11.73 | 16.3 | mheidari-all | 64.94.95.118 |
| 61.1 | trojan | 663.8 | 989.8 | 12.41 | 0.0 | 10.0 | 11.73 | 16.3 | mheidari-all | 104.17.121.43 |
| 61.04 | vmess | 574.0 | 1394.6 | 14.49 | 0.0 | 10.0 | 12.86 | 13.76 | DeltaKronecker-all | 67.220.85.46 |
| 60.98 | trojan | 663.6 | 963.6 | 12.42 | 0.0 | 10.0 | 11.73 | 16.3 | mheidari-all | 45.130.125.76 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| Surfboard-tg-mixed | 0.708 | 0.632 | 76 | 5596 | prefer |
| mheidari-all | 0.637 | 0.558 | 86 | 16239 | observe |
| DeltaKronecker-all | 0.545 | 0.465 | 155 | 7926 | observe |
| Au1rxx-base64 | 0.317 | 1.0 | 2 | 134 | observe |
| xiaoji235-airport-v2ray-all | 0.273 | 0.5 | 2 | 1647 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 3897 | observe |
| Epodonios-all | 0.255 | None | 0 | 6473 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6904 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4341 | observe |
| barry-far-vless | 0.255 | None | 0 | 4964 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5412 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 45 |
| speed | ClientOSError | - | 25 |
| 204 | ProxyError | - | 19 |
| 204 | TimeoutError | - | 16 |
| cn-block | TimeoutError | - | 13 |
| cn-block | ProxyError | - | 6 |
| speed | TimeoutError | - | 6 |
| cn-block | ClientOSError | - | 6 |
| geo | ProxyError | - | 6 |
| speed | ProxyError | - | 5 |
| 204 | ClientOSError | - | 3 |
| geo | ClientOSError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 288 | 208 | - |
| global | False | 297 | 222 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
