# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-11-17 21:09:39 |
| 运行耗时 | 306.8s |
| 订阅源总数 | 107 |
| 健康订阅源 | 88 |
| 原始节点 | 82265 |
| 去重后节点 | 27554 |
| TCP 可达 | 3000 |
| 真实可用 | 392 |
| Verified 输出 | 48 |
| Global 输出 | 300 |
| All 输出 | 27554 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.2 |
| geo | 1.6 |
| tcp | 81.9 |
| probe | 96.7 |
| real_test | 75.0 |
| china_check | 28.2 |
| write_verified | 0.0 |
| generate | 16.2 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 48906 |
| vmess | 14904 |
| shadowsocks | 9687 |
| trojan | 6837 |
| hysteria2 | 1472 |
| http | 194 |
| shadowsocksr | 152 |
| socks | 70 |
| hysteria | 17 |
| tuic | 14 |
| anytls | 12 |

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
| 92.92 | shadowsocks | 227.0 | 4.6 | 22.52 | 14.83 | 10.0 | 13.43 | 16.64 | Au1rxx-base64 | 95.215.201.18 |
| 92.01 | vless | 209.4 | 4.4 | 22.93 | 14.84 | 6.83 | 10.77 | 16.64 | Au1rxx-base64 | 45.63.53.81 |
| 91.96 | trojan | 244.2 | 2.6 | 22.13 | 14.9 | 10.0 | 10.79 | 16.64 | Au1rxx-base64 | 66.163.112.121 |
| 88.77 | trojan | 246.5 | 3.6 | 22.07 | 14.87 | 8.27 | 10.79 | 16.64 | Au1rxx-base64 | 66.163.112.242 |
| 88.62 | trojan | 174.5 | 1.5 | 23.74 | 14.95 | 10.0 | 10.79 | 16.64 | Au1rxx-base64 | 167.88.61.175 |
| 88.44 | trojan | 295.8 | 2.3 | 20.93 | 14.91 | 7.67 | 10.79 | 16.64 | Au1rxx-base64 | 66.163.112.76 |
| 88.37 | hysteria2 | 224.3 | 8.6 | 22.59 | 14.68 | 3.92 | 11.54 | 16.64 | Au1rxx-base64 | 66.94.121.46 |
| 88.1 | trojan | 301.7 | 8.4 | 20.79 | 14.69 | 7.69 | 10.79 | 16.64 | Au1rxx-base64 | 66.163.112.13 |
| 87.88 | vless | 212.7 | 12.2 | 22.86 | 14.54 | 8.07 | 10.77 | 16.64 | Au1rxx-base64 | 195.123.240.65 |
| 87.61 | trojan | 237.6 | 2.2 | 22.28 | 14.92 | 5.48 | 10.79 | 16.64 | Au1rxx-base64 | 66.163.112.142 |
| 87.52 | trojan | 273.6 | 8.2 | 21.44 | 14.69 | 7.58 | 10.79 | 16.64 | Au1rxx-base64 | 66.163.114.114 |
| 86.82 | trojan | 184.0 | 2.5 | 23.52 | 14.91 | 8.46 | 10.79 | 16.64 | Au1rxx-base64 | 167.88.61.193 |
| 86.7 | vless | 202.6 | 3.2 | 23.09 | 14.88 | 0.0 | 10.77 | 17.96 | Surfboard-tg-mixed | 147.224.54.25 |
| 86.54 | vless | 211.4 | 1.9 | 22.88 | 14.93 | 0.0 | 10.77 | 17.96 | Surfboard-tg-mixed | 143.246.62.191 |
| 86.49 | vless | 213.5 | 2.1 | 22.84 | 14.92 | 0.0 | 10.77 | 17.96 | Surfboard-tg-mixed | 143.246.60.254 |
| 86.49 | vless | 214.1 | 1.5 | 22.82 | 14.94 | 0.0 | 10.77 | 17.96 | Surfboard-tg-mixed | 199.7.140.201 |
| 86.35 | trojan | 186.5 | 13.3 | 23.46 | 14.5 | 8.46 | 10.79 | 16.64 | Au1rxx-base64 | 167.88.61.20 |
| 86.2 | trojan | 247.8 | 4.3 | 22.04 | 14.84 | 4.39 | 10.79 | 16.64 | Au1rxx-base64 | 216.106.186.32 |
| 85.66 | shadowsocks | 166.3 | 4.2 | 23.93 | 14.84 | 0.0 | 13.43 | 17.96 | Surfboard-tg-mixed | 137.184.89.151 |
| 85.63 | shadowsocks | 188.2 | 2.0 | 23.42 | 14.92 | 0.0 | 13.43 | 17.96 | Surfboard-tg-mixed | 38.145.220.193 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.977 | 1.0 | 21 | 517 | prefer |
| mheidari-all | 0.927 | 0.855 | 83 | 14572 | prefer |
| Surfboard-tg-mixed | 0.85 | 0.772 | 224 | 8416 | prefer |
| Au1rxx-base64 | 0.774 | 0.707 | 167 | 1751 | prefer |
| tg-LonUp_M | 0.456 | 0.857 | 7 | 171 | observe |
| DeltaKronecker-all | 0.335 | 1.0 | 1 | 2790 | observe |
| xiaoji235-airport-v2ray-all | 0.335 | 1.0 | 1 | 6752 | observe |
| tg-ShadowsocksM | 0.258 | 1.0 | 1 | 64 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4928 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 11534 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5789 | observe |
| barry-far-vless | 0.255 | None | 0 | 6032 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4601 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 50 |
| 204 | ProxyError | - | 30 |
| cn-block | ProxyError | - | 8 |
| 204 | TimeoutError | - | 8 |
| geo | ProxyError | - | 5 |
| cn-block | ClientOSError | - | 4 |
| cn-block | TimeoutError | - | 2 |
| 204 | ClientOSError | - | 2 |
| speed | ProxyError | - | 2 |
| speed | TimeoutError | - | 1 |
| geo | TimeoutError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 50 | 48 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
