# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-29 13:24:10 |
| 运行耗时 | 302.1s |
| 订阅源总数 | 107 |
| 健康订阅源 | 87 |
| 原始节点 | 99866 |
| 去重后节点 | 28371 |
| TCP 可达 | 3000 |
| 真实可用 | 402 |
| Verified 输出 | 71 |
| Global 输出 | 300 |
| All 输出 | 28371 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.4 |
| geo | 1.6 |
| tcp | 92.2 |
| probe | 73.3 |
| real_test | 87.0 |
| china_check | 33.8 |
| write_verified | 0.0 |
| generate | 9.7 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 62902 |
| vmess | 14279 |
| shadowsocks | 10795 |
| trojan | 9142 |
| hysteria2 | 2327 |
| shadowsocksr | 177 |
| http | 148 |
| socks | 56 |
| tuic | 16 |
| anytls | 13 |
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
| 94.94 | shadowsocks | 279.8 | 0.2 | 21.3 | 14.99 | 10.0 | 14.13 | 18.52 | Au1rxx-base64 | 156.146.38.168 |
| 94.92 | trojan | 260.6 | 0.9 | 21.75 | 14.97 | 9.56 | 12.62 | 18.52 | Au1rxx-base64 | 66.163.114.245 |
| 94.31 | shadowsocks | 304.9 | 1.7 | 20.72 | 14.94 | 10.0 | 14.13 | 18.52 | Au1rxx-base64 | 156.146.38.167 |
| 93.55 | shadowsocks | 285.6 | 0.9 | 21.17 | 14.97 | 10.0 | 14.13 | 18.52 | Au1rxx-base64 | 37.19.198.244 |
| 93.32 | shadowsocks | 330.5 | 1.0 | 20.13 | 14.96 | 9.58 | 14.13 | 18.52 | Au1rxx-base64 | 156.146.38.169 |
| 92.0 | trojan | 261.7 | 0.3 | 21.72 | 14.99 | 6.65 | 12.62 | 18.52 | Au1rxx-base64 | 66.163.114.132 |
| 91.56 | trojan | 263.8 | 0.1 | 21.67 | 15.0 | 6.65 | 12.62 | 18.52 | Au1rxx-base64 | 66.163.114.114 |
| 90.86 | shadowsocks | 346.0 | 0.1 | 19.77 | 14.99 | 10.0 | 14.13 | 18.52 | Au1rxx-base64 | 37.19.198.160 |
| 90.83 | trojan | 266.6 | 1.5 | 21.61 | 14.94 | 6.65 | 12.62 | 18.52 | Au1rxx-base64 | 66.163.114.166 |
| 90.45 | shadowsocks | 287.8 | 3.1 | 21.12 | 14.88 | 5.98 | 14.13 | 18.52 | Au1rxx-base64 | 156.146.38.170 |
| 90.1 | trojan | 262.9 | 1.6 | 21.69 | 14.94 | 5.02 | 12.62 | 18.52 | Au1rxx-base64 | 66.163.114.126 |
| 89.91 | shadowsocks | 309.5 | 2.6 | 20.61 | 14.9 | 10.0 | 14.13 | 18.52 | Au1rxx-base64 | 193.151.163.18 |
| 89.61 | trojan | 289.7 | 4.6 | 21.07 | 14.83 | 5.07 | 12.62 | 18.52 | Au1rxx-base64 | 216.152.155.131 |
| 89.4 | shadowsocks | 293.0 | 1.1 | 21.0 | 14.96 | 10.0 | 14.13 | 18.52 | Au1rxx-base64 | 37.19.198.236 |
| 88.97 | trojan | 263.9 | 0.1 | 21.67 | 15.0 | 4.57 | 12.62 | 18.52 | Au1rxx-base64 | 66.163.114.45 |
| 88.78 | trojan | 270.1 | 1.6 | 21.52 | 14.94 | 4.98 | 12.62 | 18.52 | Au1rxx-base64 | 66.163.114.106 |
| 88.11 | shadowsocks | 345.5 | 2.2 | 19.78 | 14.92 | 9.11 | 14.13 | 18.52 | Au1rxx-base64 | 149.22.95.183 |
| 88.08 | shadowsocks | 355.3 | 0.2 | 19.55 | 14.99 | 10.0 | 14.13 | 18.52 | Au1rxx-base64 | 173.244.56.6 |
| 88.0 | shadowsocks | 293.7 | 0.4 | 20.98 | 14.99 | 10.0 | 14.13 | 18.52 | Au1rxx-base64 | 173.244.56.9 |
| 87.77 | trojan | 358.8 | 0.2 | 19.47 | 14.99 | 9.24 | 12.62 | 18.52 | Au1rxx-base64 | 216.238.80.100 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.87 | 0.803 | 310 | 1723 | prefer |
| ermaozi | 0.739 | 0.733 | 30 | 510 | prefer |
| mheidari-all | 0.738 | 0.662 | 71 | 34088 | prefer |
| Surfboard-tg-mixed | 0.705 | 0.627 | 134 | 7779 | prefer |
| DeltaKronecker-all | 0.335 | 1.0 | 1 | 2709 | observe |
| xiaoji235-airport-v2ray-all | 0.335 | 1.0 | 1 | 6752 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5005 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 10415 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5820 | observe |
| barry-far-vless | 0.255 | None | 0 | 6035 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4444 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.244 | None | 0 | 1723 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 82 |
| geo | ClientOSError | - | 19 |
| 204 | TimeoutError | - | 11 |
| 204 | ProxyError | - | 10 |
| cn-block | ClientOSError | - | 8 |
| cn-block | TimeoutError | - | 6 |
| 204 | ClientOSError | - | 2 |
| geo | ProxyError | - | 2 |
| speed | ClientOSError | - | 1 |
| speed | ProxyError | - | 1 |
| geo | TimeoutError | - | 1 |
| cn-block | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 84 | 71 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
