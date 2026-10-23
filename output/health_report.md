# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-23 17:22:04 |
| 运行耗时 | 302.5s |
| 订阅源总数 | 107 |
| 健康订阅源 | 88 |
| 原始节点 | 95347 |
| 去重后节点 | 26845 |
| TCP 可达 | 3000 |
| 真实可用 | 306 |
| Verified 输出 | 140 |
| Global 输出 | 300 |
| All 输出 | 26845 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 8.1 |
| geo | 1.5 |
| tcp | 82.7 |
| probe | 100.8 |
| real_test | 66.5 |
| china_check | 29.1 |
| generate | 13.6 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 56309 |
| vmess | 17048 |
| shadowsocks | 12201 |
| trojan | 7994 |
| hysteria2 | 1317 |
| http | 220 |
| shadowsocksr | 162 |
| socks | 52 |
| anytls | 21 |
| hysteria | 17 |
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
| 90.58 | vless | 292.1 | 0.6 | 21.02 | 14.98 | 8.88 | 9.62 | 17.18 | Au1rxx-base64 | 144.202.126.147 |
| 88.58 | shadowsocks | 284.3 | 4.5 | 21.2 | 14.83 | 8.9 | 14.03 | 17.18 | Au1rxx-base64 | 149.22.95.183 |
| 88.55 | shadowsocks | 303.0 | 1.0 | 20.76 | 14.96 | 8.51 | 14.03 | 17.18 | Au1rxx-base64 | 156.146.38.169 |
| 88.44 | http | 244.7 | 1.5 | 22.11 | 14.94 | 0.0 | 14.17 | 19.72 | ermaozi | 64.98.50.100 |
| 87.87 | vless | 325.8 | 1.8 | 20.24 | 14.93 | 8.79 | 9.62 | 17.18 | Au1rxx-base64 | 195.123.240.65 |
| 87.75 | vless | 286.0 | 6.0 | 21.16 | 14.77 | 6.35 | 9.62 | 17.18 | Au1rxx-base64 | 172.236.227.60 |
| 87.35 | shadowsocks | 334.0 | 0.8 | 20.05 | 14.97 | 8.69 | 14.03 | 17.18 | Au1rxx-base64 | 37.19.198.236 |
| 86.95 | vless | 334.9 | 1.4 | 20.03 | 14.95 | 8.71 | 9.62 | 17.18 | Au1rxx-base64 | 154.40.55.185 |
| 86.74 | shadowsocks | 340.9 | 2.5 | 19.89 | 14.91 | 8.68 | 14.03 | 17.18 | Au1rxx-base64 | 37.19.198.160 |
| 86.73 | vless | 243.2 | 0.9 | 22.15 | 14.96 | 5.46 | 9.62 | 17.18 | Au1rxx-base64 | 47.251.108.158 |
| 86.52 | shadowsocks | 331.7 | 2.3 | 20.1 | 14.91 | 8.72 | 14.03 | 17.18 | Au1rxx-base64 | 37.19.198.244 |
| 86.46 | vless | 374.1 | 1.2 | 19.12 | 14.95 | 7.55 | 9.62 | 17.18 | Au1rxx-base64 | 45.76.172.197 |
| 86.34 | vless | 253.2 | 2.1 | 21.92 | 14.92 | 7.56 | 9.62 | 17.18 | Au1rxx-base64 | 216.167.126.97 |
| 86.21 | vless | 363.1 | 1.1 | 19.37 | 14.96 | 8.74 | 9.62 | 17.18 | Au1rxx-base64 | 44.248.233.99 |
| 86.14 | shadowsocks | 323.7 | 0.3 | 20.29 | 14.99 | 8.53 | 14.03 | 17.18 | Au1rxx-base64 | 156.146.38.168 |
| 85.85 | hysteria2 | 304.9 | 2.5 | 20.72 | 14.91 | 3.52 | 13.0 | 17.18 | Au1rxx-base64 | 129.213.91.185 |
| 85.63 | shadowsocks | 376.8 | 3.3 | 19.05 | 14.88 | 8.76 | 14.03 | 17.18 | Au1rxx-base64 | 95.215.201.18 |
| 85.19 | trojan | 314.8 | 10.1 | 20.49 | 14.62 | 8.72 | 9.9 | 17.18 | Au1rxx-base64 | 66.23.203.21 |
| 84.84 | shadowsocks | 322.6 | 5.8 | 20.31 | 14.78 | 8.5 | 14.03 | 17.18 | Au1rxx-base64 | 173.244.56.9 |
| 84.61 | shadowsocks | 366.6 | 3.2 | 19.29 | 14.88 | 8.5 | 14.03 | 17.18 | Au1rxx-base64 | 193.151.160.9 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.965 | 0.96 | 50 | 555 | prefer |
| Au1rxx-base64 | 0.875 | 0.814 | 242 | 1588 | prefer |
| mheidari-all | 0.854 | 0.793 | 29 | 23793 | prefer |
| Surfboard-tg-mixed | 0.573 | 0.493 | 67 | 6855 | observe |
| xiaoji235-airport-v2ray-all | 0.335 | 1.0 | 1 | 6752 | observe |
| roosterkid-openproxylist-v2ray | 0.317 | 1.0 | 2 | 150 | observe |
| tg-oneclickvpnkeys | 0.272 | 0.667 | 3 | 98 | observe |
| tg-LonUp_M | 0.262 | 1.0 | 1 | 175 | observe |
| tg-OutlineReleasedKey | 0.257 | 1.0 | 1 | 53 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4911 | observe |
| DeltaKronecker-all | 0.255 | None | 0 | 3871 | observe |
| Epodonios-all | 0.255 | None | 0 | 7353 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5326 | observe |
| barry-far-vless | 0.255 | None | 0 | 5545 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 53 |
| 204 | TimeoutError | - | 8 |
| 204 | ProxyError | - | 8 |
| cn-block | TimeoutError | - | 6 |
| cn-block | ClientOSError | - | 5 |
| 204 | ClientOSError | - | 5 |
| geo | ClientOSError | - | 5 |
| cn-block | ProxyError | - | 2 |
| speed | ClientOSError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | True | 140 | 69 | 0.5 |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
