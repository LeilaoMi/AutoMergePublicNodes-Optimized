# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-11-14 18:21:44 |
| 运行耗时 | 263.8s |
| 订阅源总数 | 107 |
| 健康订阅源 | 87 |
| 原始节点 | 83318 |
| 去重后节点 | 27127 |
| TCP 可达 | 3000 |
| 真实可用 | 314 |
| Verified 输出 | 89 |
| Global 输出 | 300 |
| All 输出 | 27127 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.1 |
| geo | 1.5 |
| tcp | 75.4 |
| probe | 78.7 |
| real_test | 59.5 |
| china_check | 32.9 |
| generate | 10.6 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 50015 |
| vmess | 14593 |
| shadowsocks | 9755 |
| trojan | 6942 |
| hysteria2 | 1522 |
| http | 182 |
| shadowsocksr | 157 |
| socks | 73 |
| anytls | 33 |
| hysteria | 27 |
| tuic | 19 |

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
| 93.54 | shadowsocks | 259.6 | 2.7 | 21.77 | 14.9 | 10.0 | 13.65 | 17.76 | Au1rxx-base64 | 156.146.38.168 |
| 92.05 | shadowsocks | 259.7 | 3.6 | 21.77 | 14.87 | 10.0 | 13.65 | 17.76 | Au1rxx-base64 | 156.146.38.170 |
| 90.89 | trojan | 339.8 | 3.0 | 19.91 | 14.89 | 10.0 | 13.33 | 17.76 | Au1rxx-base64 | 66.23.203.21 |
| 90.63 | shadowsocks | 274.3 | 9.3 | 21.43 | 14.65 | 10.0 | 13.65 | 17.76 | Au1rxx-base64 | 95.215.201.18 |
| 89.98 | shadowsocks | 304.4 | 1.9 | 20.73 | 14.93 | 7.22 | 13.65 | 17.76 | Au1rxx-base64 | 156.146.38.169 |
| 89.43 | vless | 246.4 | 1.8 | 22.07 | 14.93 | 8.07 | 8.02 | 17.76 | Au1rxx-base64 | 45.63.53.81 |
| 89.42 | shadowsocks | 248.7 | 1.6 | 22.02 | 14.94 | 10.0 | 13.65 | 17.76 | Au1rxx-base64 | 156.146.38.167 |
| 88.38 | shadowsocks | 325.2 | 1.0 | 20.25 | 14.96 | 10.0 | 13.65 | 17.76 | Au1rxx-base64 | 193.151.163.18 |
| 88.27 | shadowsocks | 344.2 | 1.1 | 19.81 | 14.96 | 10.0 | 13.65 | 17.76 | Au1rxx-base64 | 45.86.51.18 |
| 88.04 | shadowsocks | 323.5 | 0.3 | 20.29 | 14.99 | 10.0 | 13.65 | 17.76 | Au1rxx-base64 | 185.230.230.18 |
| 88.0 | shadowsocks | 334.6 | 2.9 | 20.03 | 14.89 | 10.0 | 13.65 | 17.76 | Au1rxx-base64 | 193.151.160.9 |
| 87.56 | vless | 248.9 | 1.0 | 22.02 | 14.96 | 8.08 | 8.02 | 17.76 | Au1rxx-base64 | 47.251.108.158 |
| 87.26 | shadowsocks | 330.3 | 0.6 | 20.13 | 14.98 | 8.93 | 13.65 | 17.76 | Au1rxx-base64 | 193.151.160.18 |
| 86.15 | http | 302.0 | 1.1 | 20.79 | 14.96 | 0.0 | 14.18 | 19.16 | ermaozi | 38.247.141.135 |
| 84.98 | http | 353.4 | 5.1 | 19.6 | 14.81 | 0.0 | 14.18 | 19.16 | ermaozi | 172.64.69.89 |
| 84.9 | vless | 272.8 | 1.2 | 21.46 | 14.96 | 9.95 | 8.02 | 17.76 | Au1rxx-base64 | 15.204.97.214 |
| 84.86 | vless | 371.6 | 0.2 | 19.18 | 14.99 | 9.65 | 8.02 | 17.76 | Au1rxx-base64 | 66.70.179.198 |
| 84.54 | trojan | 500.0 | 4.8 | 16.2 | 14.82 | 9.77 | 13.33 | 17.76 | Au1rxx-base64 | 69.164.240.85 |
| 83.2 | vless | 441.4 | 5.0 | 17.56 | 14.81 | 10.0 | 8.02 | 17.76 | Au1rxx-base64 | 169.40.42.74 |
| 82.37 | http | 310.4 | 1.0 | 20.59 | 14.96 | 0.0 | 14.18 | 19.16 | ermaozi | 44.248.167.117 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.947 | 0.96 | 25 | 527 | prefer |
| Surfboard-tg-mixed | 0.899 | 0.824 | 136 | 8883 | prefer |
| mheidari-all | 0.855 | 0.782 | 87 | 14109 | prefer |
| Au1rxx-base64 | 0.761 | 0.693 | 150 | 1751 | prefer |
| xiaoji235-airport-v2ray-all | 0.391 | 1.0 | 2 | 6752 | observe |
| DeltaKronecker-all | 0.335 | 1.0 | 1 | 2652 | observe |
| ermaozi-get_subscribe | 0.271 | 1.0 | 1 | 405 | observe |
| tg-LonUp_M | 0.262 | 1.0 | 1 | 179 | observe |
| roosterkid-openproxylist-v2ray | 0.261 | 1.0 | 1 | 150 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4966 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3996 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 11700 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 6276 | observe |
| barry-far-vless | 0.255 | None | 0 | 6457 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | ProxyError | - | 32 |
| test_one_timeout | 15.0s | - | 25 |
| cn-block | ProxyError | - | 11 |
| 204 | TimeoutError | - | 7 |
| cn-block | TimeoutError | - | 5 |
| geo | ProxyError | - | 5 |
| speed | ProxyError | - | 2 |
| 204 | ClientOSError | - | 2 |
| cn-block | ClientOSError | - | 1 |
| speed | ClientOSError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | True | 89 | 25 | 0.5 |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
