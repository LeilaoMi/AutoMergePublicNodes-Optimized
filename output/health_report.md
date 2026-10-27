# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-27 12:31:08 |
| 运行耗时 | 306.6s |
| 订阅源总数 | 107 |
| 健康订阅源 | 88 |
| 原始节点 | 96776 |
| 去重后节点 | 26731 |
| TCP 可达 | 3000 |
| 真实可用 | 483 |
| Verified 输出 | 143 |
| Global 输出 | 300 |
| All 输出 | 26731 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.3 |
| geo | 1.6 |
| tcp | 84.1 |
| probe | 84.9 |
| real_test | 91.6 |
| china_check | 28.4 |
| write_verified | 0.0 |
| generate | 10.8 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 56498 |
| vmess | 17807 |
| shadowsocks | 12655 |
| trojan | 7818 |
| hysteria2 | 1383 |
| http | 324 |
| shadowsocksr | 168 |
| socks | 74 |
| anytls | 25 |
| hysteria | 18 |
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
| 91.72 | vless | 189.0 | 5.4 | 23.4 | 14.8 | 9.1 | 8.22 | 16.2 | Au1rxx-base64 | 45.32.69.110 |
| 90.99 | shadowsocks | 247.8 | 0.0 | 22.04 | 15.0 | 10.0 | 11.75 | 16.2 | Au1rxx-base64 | 156.146.38.169 |
| 90.45 | vless | 199.6 | 1.0 | 23.16 | 14.96 | 8.91 | 8.22 | 16.2 | Au1rxx-base64 | 144.202.126.147 |
| 90.34 | hysteria2 | 301.2 | 26.4 | 20.81 | 14.01 | 8.47 | 14.17 | 16.2 | Au1rxx-base64 | 66.94.121.46 |
| 89.74 | shadowsocks | 262.9 | 0.9 | 21.69 | 14.96 | 9.14 | 11.75 | 16.2 | Au1rxx-base64 | 156.146.38.167 |
| 89.71 | shadowsocks | 253.3 | 1.3 | 21.92 | 14.95 | 9.39 | 11.75 | 16.2 | Au1rxx-base64 | 95.215.201.18 |
| 89.24 | vless | 209.8 | 2.1 | 22.92 | 14.92 | 6.98 | 8.22 | 16.2 | Au1rxx-base64 | 195.123.240.65 |
| 89.16 | vless | 298.6 | 0.5 | 20.86 | 14.98 | 8.9 | 8.22 | 16.2 | Au1rxx-base64 | 172.236.227.60 |
| 87.94 | shadowsocks | 244.9 | 0.9 | 22.11 | 14.97 | 9.3 | 11.75 | 16.2 | Au1rxx-base64 | 173.244.56.9 |
| 87.67 | hysteria2 | 449.4 | 1.7 | 17.37 | 14.94 | 8.88 | 14.17 | 16.2 | Au1rxx-base64 | 129.213.91.185 |
| 85.67 | shadowsocks | 261.3 | 0.7 | 21.73 | 14.97 | 5.7 | 11.75 | 16.2 | Au1rxx-base64 | 156.146.38.170 |
| 85.59 | trojan | 195.1 | 0.5 | 23.26 | 14.98 | 5.64 | 13.01 | 16.2 | Au1rxx-base64 | 66.163.112.76 |
| 85.53 | trojan | 195.9 | 1.6 | 23.24 | 14.94 | 5.64 | 13.01 | 16.2 | Au1rxx-base64 | 66.163.112.13 |
| 85.09 | trojan | 196.0 | 0.6 | 23.24 | 14.98 | 5.16 | 13.01 | 16.2 | Au1rxx-base64 | 66.163.112.142 |
| 84.53 | shadowsocks | 247.8 | 1.0 | 22.04 | 14.96 | 7.27 | 11.75 | 16.2 | Au1rxx-base64 | 173.244.56.6 |
| 84.16 | trojan | 272.0 | 0.9 | 21.48 | 14.97 | 7.26 | 13.01 | 16.2 | Au1rxx-base64 | 66.163.114.166 |
| 84.13 | trojan | 451.4 | 3.4 | 17.33 | 14.87 | 8.86 | 13.01 | 16.2 | Au1rxx-base64 | 66.23.203.21 |
| 84.1 | trojan | 275.5 | 1.2 | 21.4 | 14.96 | 7.26 | 13.01 | 16.2 | Au1rxx-base64 | 66.163.114.245 |
| 83.4 | vless | 367.1 | 1.1 | 19.28 | 14.96 | 9.25 | 8.22 | 16.2 | Au1rxx-base64 | 44.248.233.99 |
| 83.1 | trojan | 282.9 | 0.1 | 21.23 | 15.0 | 5.16 | 13.01 | 16.2 | Au1rxx-base64 | 66.163.112.147 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.991 | 0.978 | 89 | 603 | prefer |
| Au1rxx-base64 | 0.838 | 0.768 | 345 | 1774 | prefer |
| mheidari-all | 0.805 | 0.735 | 49 | 24516 | prefer |
| Surfboard-tg-mixed | 0.741 | 0.664 | 110 | 7059 | prefer |
| DeltaKronecker-all | 0.466 | 0.381 | 42 | 3052 | observe |
| roosterkid-openproxylist-v2ray | 0.455 | 0.857 | 7 | 150 | observe |
| ninja-vless | 0.327 | 1.0 | 1 | 1791 | observe |
| tg-OutlineReleasedKey | 0.257 | 1.0 | 1 | 52 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4988 | observe |
| Epodonios-all | 0.255 | None | 0 | 7509 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5319 | observe |
| barry-far-vless | 0.255 | None | 0 | 5497 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4573 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 70 |
| speed | ClientOSError | - | 31 |
| geo | ClientOSError | - | 28 |
| 204 | ProxyError | - | 10 |
| cn-block | ClientOSError | - | 7 |
| cn-block | TimeoutError | - | 5 |
| 204 | TimeoutError | - | 4 |
| speed | TimeoutError | - | 2 |
| geo | ProxyError | - | 2 |
| 204 | ClientOSError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 129 | 143 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
