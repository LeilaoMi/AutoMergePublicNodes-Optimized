# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-29 22:56:27 |
| 运行耗时 | 306.4s |
| 订阅源总数 | 107 |
| 健康订阅源 | 86 |
| 原始节点 | 99203 |
| 去重后节点 | 27795 |
| TCP 可达 | 3000 |
| 真实可用 | 519 |
| Verified 输出 | 84 |
| Global 输出 | 300 |
| All 输出 | 27795 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.7 |
| geo | 1.6 |
| tcp | 86.4 |
| probe | 80.1 |
| real_test | 85.2 |
| china_check | 35.5 |
| write_verified | 0.0 |
| generate | 11.9 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 61552 |
| vmess | 15109 |
| shadowsocks | 10814 |
| trojan | 9092 |
| hysteria2 | 2227 |
| shadowsocksr | 171 |
| http | 149 |
| socks | 49 |
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
| 94.36 | trojan | 198.2 | 0.3 | 23.19 | 14.99 | 9.51 | 11.77 | 17.4 | Au1rxx-base64 | 66.163.112.13 |
| 94.31 | trojan | 199.6 | 0.9 | 23.16 | 14.97 | 9.51 | 11.77 | 17.4 | Au1rxx-base64 | 66.163.112.142 |
| 94.0 | vless | 199.1 | 0.7 | 23.17 | 14.97 | 10.0 | 8.46 | 17.4 | Au1rxx-base64 | 144.202.126.147 |
| 93.93 | trojan | 197.2 | 0.4 | 23.21 | 14.99 | 9.06 | 11.77 | 17.4 | Au1rxx-base64 | 66.163.112.121 |
| 93.79 | shadowsocks | 222.5 | 7.8 | 22.63 | 14.71 | 10.0 | 13.05 | 17.4 | Au1rxx-base64 | 173.244.56.6 |
| 93.73 | trojan | 204.4 | 1.2 | 23.05 | 14.95 | 9.06 | 11.77 | 17.4 | Au1rxx-base64 | 66.163.112.171 |
| 93.31 | shadowsocks | 226.4 | 18.1 | 22.54 | 14.32 | 10.0 | 13.05 | 17.4 | Au1rxx-base64 | 173.244.56.9 |
| 93.25 | vless | 223.7 | 5.5 | 22.6 | 14.79 | 10.0 | 8.46 | 17.4 | Au1rxx-base64 | 195.123.240.65 |
| 93.24 | trojan | 246.3 | 0.5 | 22.08 | 14.98 | 9.51 | 11.77 | 17.4 | Au1rxx-base64 | 66.163.112.76 |
| 92.88 | shadowsocks | 261.5 | 7.9 | 21.73 | 14.7 | 10.0 | 13.05 | 17.4 | Au1rxx-base64 | 156.146.38.168 |
| 92.78 | shadowsocks | 257.2 | 13.0 | 21.82 | 14.51 | 10.0 | 13.05 | 17.4 | Au1rxx-base64 | 156.146.38.170 |
| 92.49 | shadowsocks | 254.4 | 3.7 | 21.89 | 14.86 | 9.85 | 13.05 | 17.4 | Au1rxx-base64 | 156.146.38.169 |
| 92.46 | trojan | 197.9 | 1.0 | 23.2 | 14.96 | 7.63 | 11.77 | 17.4 | Au1rxx-base64 | 66.163.112.31 |
| 92.31 | shadowsocks | 261.7 | 3.6 | 21.72 | 14.87 | 10.0 | 13.05 | 17.4 | Au1rxx-base64 | 156.146.38.167 |
| 92.07 | shadowsocks | 277.8 | 6.2 | 21.35 | 14.77 | 10.0 | 13.05 | 17.4 | Au1rxx-base64 | 95.215.201.18 |
| 91.54 | trojan | 278.0 | 0.0 | 21.34 | 15.0 | 9.81 | 11.77 | 17.4 | Au1rxx-base64 | 66.163.114.114 |
| 91.27 | trojan | 277.4 | 2.1 | 21.36 | 14.92 | 9.65 | 11.77 | 17.4 | Au1rxx-base64 | 66.163.114.126 |
| 91.05 | trojan | 274.3 | 1.7 | 21.43 | 14.94 | 9.64 | 11.77 | 17.4 | Au1rxx-base64 | 66.163.114.132 |
| 90.71 | trojan | 281.2 | 1.5 | 21.27 | 14.95 | 9.66 | 11.77 | 17.4 | Au1rxx-base64 | 66.163.114.245 |
| 90.49 | trojan | 277.7 | 1.6 | 21.35 | 14.94 | 9.2 | 11.77 | 17.4 | Au1rxx-base64 | 66.163.114.45 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.979 | 1.0 | 22 | 510 | prefer |
| Surfboard-tg-mixed | 0.953 | 0.88 | 100 | 7758 | prefer |
| Au1rxx-base64 | 0.902 | 0.835 | 345 | 1725 | prefer |
| mheidari-all | 0.752 | 0.674 | 175 | 33474 | prefer |
| xiaoji235-airport-v2ray-all | 0.349 | 0.667 | 3 | 6752 | observe |
| ninja-vless | 0.327 | 1.0 | 1 | 1791 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5005 | observe |
| DeltaKronecker-all | 0.255 | None | 0 | 2709 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 10379 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5789 | observe |
| barry-far-vless | 0.255 | None | 0 | 6033 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4444 | observe |
| Au1rxx-clash | 0.244 | None | 0 | 1725 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 75 |
| geo | ClientOSError | - | 16 |
| cn-block | TimeoutError | - | 9 |
| cn-block | ClientOSError | - | 8 |
| 204 | ProxyError | - | 6 |
| 204 | ClientOSError | - | 5 |
| 204 | TimeoutError | - | 4 |
| speed | ClientOSError | - | 2 |
| speed | ProxyError | - | 1 |
| cn-block | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 71 | 84 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
