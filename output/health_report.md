# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-30 06:05:47 |
| 运行耗时 | 317.6s |
| 订阅源总数 | 107 |
| 健康订阅源 | 86 |
| 原始节点 | 99789 |
| 去重后节点 | 27982 |
| TCP 可达 | 3000 |
| 真实可用 | 499 |
| Verified 输出 | 91 |
| Global 输出 | 300 |
| All 输出 | 27982 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.8 |
| geo | 1.5 |
| tcp | 86.4 |
| probe | 91.7 |
| real_test | 91.8 |
| china_check | 26.5 |
| write_verified | 0.0 |
| generate | 12.9 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 62544 |
| vmess | 14318 |
| shadowsocks | 10831 |
| trojan | 9451 |
| hysteria2 | 2245 |
| shadowsocksr | 165 |
| http | 143 |
| socks | 50 |
| tuic | 16 |
| anytls | 15 |
| hysteria | 11 |

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
| 96.42 | trojan | 270.3 | 1.9 | 21.52 | 14.93 | 9.96 | 14.47 | 18.04 | Au1rxx-base64 | 216.152.155.131 |
| 95.18 | hysteria2 | 259.4 | 16.8 | 21.77 | 14.37 | 10.0 | 12.5 | 18.04 | Au1rxx-base64 | 129.213.91.185 |
| 94.28 | shadowsocks | 247.4 | 2.8 | 22.05 | 14.89 | 10.0 | 13.3 | 18.04 | Au1rxx-base64 | 156.146.38.170 |
| 94.2 | trojan | 336.0 | 8.3 | 20.0 | 14.69 | 10.0 | 14.47 | 18.04 | Au1rxx-base64 | 66.23.203.21 |
| 94.14 | shadowsocks | 251.7 | 3.9 | 21.95 | 14.85 | 10.0 | 13.3 | 18.04 | Au1rxx-base64 | 156.146.38.169 |
| 93.81 | shadowsocks | 259.5 | 7.9 | 21.77 | 14.7 | 10.0 | 13.3 | 18.04 | Au1rxx-base64 | 156.146.38.168 |
| 93.7 | trojan | 275.4 | 1.1 | 21.4 | 14.96 | 7.33 | 14.47 | 18.04 | Au1rxx-base64 | 169.197.140.169 |
| 93.62 | shadowsocks | 275.8 | 2.8 | 21.39 | 14.89 | 10.0 | 13.3 | 18.04 | Au1rxx-base64 | 37.19.198.243 |
| 93.59 | trojan | 274.4 | 3.1 | 21.43 | 14.88 | 7.27 | 14.47 | 18.04 | Au1rxx-base64 | 216.152.156.49 |
| 93.56 | trojan | 268.4 | 7.6 | 21.57 | 14.71 | 7.27 | 14.47 | 18.04 | Au1rxx-base64 | 216.152.156.212 |
| 93.49 | trojan | 267.8 | 0.4 | 21.58 | 14.99 | 6.91 | 14.47 | 18.04 | Au1rxx-base64 | 216.152.155.54 |
| 93.42 | shadowsocks | 282.1 | 4.5 | 21.25 | 14.83 | 10.0 | 13.3 | 18.04 | Au1rxx-base64 | 37.19.198.160 |
| 93.22 | trojan | 281.8 | 8.6 | 21.26 | 14.68 | 7.27 | 14.47 | 18.04 | Au1rxx-base64 | 216.152.156.42 |
| 92.66 | shadowsocks | 277.8 | 0.8 | 21.35 | 14.97 | 10.0 | 13.3 | 18.04 | Au1rxx-base64 | 37.19.198.236 |
| 92.53 | trojan | 299.7 | 3.2 | 20.84 | 14.88 | 10.0 | 14.47 | 18.04 | Au1rxx-base64 | 66.163.114.132 |
| 92.3 | trojan | 308.9 | 10.7 | 20.63 | 14.6 | 9.99 | 14.47 | 18.04 | Au1rxx-base64 | 66.163.114.114 |
| 92.08 | shadowsocks | 339.2 | 5.0 | 19.93 | 14.81 | 10.0 | 13.3 | 18.04 | Au1rxx-base64 | 37.19.198.244 |
| 92.06 | trojan | 271.8 | 4.2 | 21.49 | 14.84 | 5.72 | 14.47 | 18.04 | Au1rxx-base64 | 169.197.140.214 |
| 91.97 | shadowsocks | 286.7 | 9.7 | 21.14 | 14.64 | 10.0 | 13.3 | 18.04 | Au1rxx-base64 | 193.151.163.18 |
| 91.96 | trojan | 309.0 | 4.6 | 20.62 | 14.83 | 10.0 | 14.47 | 18.04 | Au1rxx-base64 | 66.163.114.245 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.934 | 0.952 | 21 | 515 | prefer |
| Au1rxx-base64 | 0.926 | 0.858 | 332 | 1735 | prefer |
| Surfboard-tg-mixed | 0.708 | 0.63 | 146 | 7756 | prefer |
| mheidari-all | 0.612 | 0.532 | 188 | 34034 | observe |
| DeltaKronecker-all | 0.335 | 1.0 | 1 | 2709 | observe |
| xiaoji235-airport-v2ray-all | 0.3 | 0.4 | 5 | 6752 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5005 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 10500 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5729 | observe |
| barry-far-vless | 0.255 | None | 0 | 5941 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4444 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.244 | None | 0 | 1735 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 122 |
| geo | ClientOSError | - | 31 |
| 204 | ProxyError | - | 10 |
| 204 | TimeoutError | - | 6 |
| cn-block | ClientOSError | - | 6 |
| speed | ClientOSError | - | 6 |
| cn-block | ProxyError | - | 4 |
| cn-block | TimeoutError | - | 3 |
| 204 | ClientOSError | - | 3 |
| geo | ProxyError | - | 1 |
| geo | TimeoutError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 84 | 91 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
