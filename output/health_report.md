# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-17 20:49:05 |
| 运行耗时 | 287.9s |
| 订阅源总数 | 107 |
| 健康订阅源 | 93 |
| 原始节点 | 99294 |
| 去重后节点 | 27807 |
| TCP 可达 | 3000 |
| 真实可用 | 364 |
| Verified 输出 | 66 |
| Global 输出 | 300 |
| All 输出 | 27807 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.0 |
| geo | 1.4 |
| tcp | 91.4 |
| probe | 74.4 |
| real_test | 78.5 |
| china_check | 30.5 |
| write_verified | 0.0 |
| generate | 7.7 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 58546 |
| vmess | 16710 |
| shadowsocks | 11902 |
| trojan | 9934 |
| hysteria2 | 1321 |
| http | 611 |
| shadowsocksr | 160 |
| socks | 61 |
| anytls | 26 |
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
| 94.42 | vless | 253.7 | 1.5 | 21.9 | 14.94 | 10.0 | 10.16 | 17.42 | Au1rxx-base64 | 147.45.60.160 |
| 93.75 | shadowsocks | 224.9 | 0.0 | 22.57 | 15.0 | 10.0 | 12.76 | 17.42 | Au1rxx-base64 | 156.146.38.169 |
| 93.74 | shadowsocks | 225.5 | 0.1 | 22.56 | 15.0 | 10.0 | 12.76 | 17.42 | Au1rxx-base64 | 156.146.38.167 |
| 93.6 | shadowsocks | 227.4 | 2.3 | 22.51 | 14.91 | 10.0 | 12.76 | 17.42 | Au1rxx-base64 | 156.146.38.170 |
| 91.39 | shadowsocks | 252.9 | 0.2 | 21.92 | 14.99 | 10.0 | 12.76 | 17.42 | Au1rxx-base64 | 173.244.56.9 |
| 90.78 | shadowsocks | 223.7 | 0.1 | 22.6 | 15.0 | 10.0 | 12.76 | 17.42 | Au1rxx-base64 | 156.146.38.168 |
| 89.17 | vless | 287.3 | 8.3 | 21.13 | 14.69 | 8.39 | 10.16 | 17.42 | Au1rxx-base64 | 212.104.141.233 |
| 89.14 | hysteria2 | 293.5 | 2.5 | 20.98 | 14.91 | 5.14 | 12.19 | 17.42 | Au1rxx-base64 | 129.213.91.185 |
| 88.49 | shadowsocks | 326.4 | 0.9 | 20.22 | 14.97 | 10.0 | 12.76 | 17.42 | Au1rxx-base64 | 37.19.198.160 |
| 87.98 | shadowsocks | 331.2 | 2.2 | 20.11 | 14.92 | 10.0 | 12.76 | 17.42 | Au1rxx-base64 | 37.19.198.244 |
| 87.09 | vless | 254.6 | 0.5 | 21.88 | 14.98 | 6.98 | 10.16 | 17.42 | Au1rxx-base64 | 176.122.183.26 |
| 86.64 | shadowsocks | 328.4 | 0.8 | 20.18 | 14.97 | 10.0 | 12.76 | 17.42 | Au1rxx-base64 | 37.19.198.243 |
| 86.58 | vless | 251.3 | 3.1 | 21.96 | 14.88 | 4.89 | 10.16 | 17.42 | Au1rxx-base64 | 45.32.69.110 |
| 86.58 | vless | 352.9 | 0.7 | 19.61 | 14.97 | 9.99 | 10.16 | 17.42 | Au1rxx-base64 | 208.84.100.209 |
| 86.23 | vless | 252.0 | 2.7 | 21.95 | 14.9 | 5.5 | 10.16 | 17.42 | Au1rxx-base64 | 45.63.53.81 |
| 86.13 | shadowsocks | 245.7 | 0.4 | 22.09 | 14.98 | 10.0 | 12.76 | 17.42 | Au1rxx-base64 | 173.244.56.6 |
| 85.62 | vless | 439.2 | 0.2 | 17.61 | 14.99 | 9.25 | 10.16 | 17.42 | Au1rxx-base64 | 185.95.231.156 |
| 85.58 | vless | 444.8 | 0.3 | 17.48 | 14.99 | 10.0 | 10.16 | 17.42 | Au1rxx-base64 | 167.17.69.171 |
| 85.38 | vless | 280.1 | 2.0 | 21.29 | 14.92 | 4.83 | 10.16 | 17.42 | Au1rxx-base64 | 154.9.241.170 |
| 84.99 | vless | 303.7 | 2.0 | 20.75 | 14.93 | 5.4 | 10.16 | 17.42 | Au1rxx-base64 | 195.211.98.43 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.925 | 0.929 | 28 | 623 | prefer |
| Au1rxx-base64 | 0.887 | 0.809 | 393 | 1992 | prefer |
| mheidari-all | 0.674 | 0.6 | 30 | 23876 | observe |
| Surfboard-tg-mixed | 0.438 | 1.0 | 3 | 7109 | observe |
| Surfboard-tg-vless | 0.335 | 1.0 | 1 | 5614 | observe |
| tg-LonUp_M | 0.318 | 1.0 | 2 | 176 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4986 | observe |
| Au1rxx-clash | 0.255 | None | 0 | 1992 | observe |
| Epodonios-all | 0.255 | None | 0 | 7590 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 10112 | observe |
| barry-far-vless | 0.255 | None | 0 | 5860 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 44 |
| speed | ClientOSError | - | 12 |
| 204 | TimeoutError | - | 11 |
| cn-block | ClientOSError | - | 7 |
| 204 | ProxyError | - | 6 |
| cn-block | TimeoutError | - | 5 |
| cn-block | ProxyError | - | 4 |
| 204 | ClientOSError | - | 3 |
| geo | ClientOSError | - | 2 |
| speed | ClientPayloadError | - | 1 |
| speed | ProxyError | - | 1 |
| geo | TimeoutError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 121 | 66 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
