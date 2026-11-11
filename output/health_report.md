# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-11-11 06:49:33 |
| 运行耗时 | 293.8s |
| 订阅源总数 | 107 |
| 健康订阅源 | 87 |
| 原始节点 | 82378 |
| 去重后节点 | 26936 |
| TCP 可达 | 3000 |
| 真实可用 | 464 |
| Verified 输出 | 92 |
| Global 输出 | 300 |
| All 输出 | 26936 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.9 |
| geo | 1.5 |
| tcp | 83.9 |
| probe | 85.9 |
| real_test | 76.5 |
| china_check | 28.2 |
| write_verified | 0.0 |
| generate | 11.9 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 49991 |
| vmess | 14200 |
| shadowsocks | 9227 |
| trojan | 6840 |
| hysteria2 | 1543 |
| http | 307 |
| shadowsocksr | 145 |
| socks | 60 |
| hysteria | 32 |
| tuic | 17 |
| anytls | 16 |

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
| 91.59 | shadowsocks | 240.4 | 1.4 | 22.21 | 14.95 | 10.0 | 13.29 | 15.64 | Au1rxx-base64 | 185.230.230.18 |
| 91.05 | shadowsocks | 264.5 | 0.8 | 21.65 | 14.97 | 10.0 | 13.29 | 15.64 | Au1rxx-base64 | 193.151.163.18 |
| 89.75 | vless | 253.7 | 0.7 | 21.91 | 14.97 | 8.75 | 8.48 | 15.64 | Au1rxx-base64 | 167.17.69.171 |
| 88.65 | shadowsocks | 288.5 | 3.5 | 21.1 | 14.87 | 8.25 | 13.29 | 15.64 | Au1rxx-base64 | 193.151.160.18 |
| 88.54 | shadowsocks | 316.4 | 3.8 | 20.45 | 14.86 | 10.0 | 13.29 | 15.64 | Au1rxx-base64 | 156.146.38.168 |
| 88.31 | vless | 295.3 | 6.5 | 20.94 | 14.76 | 8.66 | 8.48 | 15.64 | Au1rxx-base64 | 66.70.179.198 |
| 87.94 | vless | 324.5 | 4.5 | 20.27 | 14.83 | 8.72 | 8.48 | 15.64 | Au1rxx-base64 | 159.89.87.21 |
| 87.87 | shadowsocks | 277.8 | 11.0 | 21.35 | 14.59 | 10.0 | 13.29 | 15.64 | Au1rxx-base64 | 156.146.38.167 |
| 87.67 | vless | 348.4 | 0.8 | 19.71 | 14.97 | 10.0 | 8.48 | 15.64 | Au1rxx-base64 | 169.40.42.35 |
| 87.65 | vless | 346.0 | 0.3 | 19.77 | 14.99 | 8.77 | 8.48 | 15.64 | Au1rxx-base64 | 169.40.42.202 |
| 87.32 | shadowsocks | 359.2 | 0.5 | 19.46 | 14.98 | 10.0 | 13.29 | 15.64 | Au1rxx-base64 | 156.146.38.170 |
| 87.19 | http | 275.7 | 0.0 | 21.4 | 15.0 | 0.0 | 14.17 | 19.12 | ermaozi | 172.64.69.89 |
| 86.38 | vless | 346.3 | 0.6 | 19.76 | 14.98 | 8.74 | 8.48 | 15.64 | Au1rxx-base64 | 169.40.42.89 |
| 86.2 | shadowsocks | 442.4 | 20.5 | 17.54 | 14.23 | 10.0 | 13.29 | 15.64 | Au1rxx-base64 | 15.204.247.206 |
| 86.13 | shadowsocks | 246.1 | 0.8 | 22.08 | 14.97 | 10.0 | 13.29 | 15.64 | Au1rxx-base64 | 45.86.51.18 |
| 84.62 | shadowsocks | 327.8 | 0.1 | 20.19 | 15.0 | 6.23 | 13.29 | 15.64 | Au1rxx-base64 | 156.146.38.169 |
| 84.36 | http | 286.5 | 13.3 | 21.15 | 14.5 | 0.0 | 14.17 | 19.12 | ermaozi | 198.44.157.27 |
| 84.36 | vless | 358.2 | 2.2 | 19.49 | 14.92 | 8.77 | 8.48 | 15.64 | Au1rxx-base64 | 169.40.42.168 |
| 84.11 | shadowsocks | 302.5 | 2.4 | 20.77 | 14.91 | 10.0 | 13.29 | 15.64 | Au1rxx-base64 | 95.215.201.18 |
| 83.99 | hysteria2 | 343.7 | 3.0 | 19.82 | 14.89 | 0.0 | 13.12 | 17.16 | mheidari-all | 34.24.25.1 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.99 | 0.976 | 85 | 601 | prefer |
| Surfboard-tg-mixed | 0.93 | 0.856 | 125 | 8415 | prefer |
| Au1rxx-base64 | 0.847 | 0.779 | 222 | 1751 | prefer |
| mheidari-all | 0.78 | 0.703 | 138 | 13964 | prefer |
| ninja-vless | 0.43 | 1.0 | 3 | 1791 | observe |
| barry-far-vless | 0.335 | 1.0 | 1 | 6562 | observe |
| xiaoji235-airport-v2ray-all | 0.287 | 0.5 | 2 | 6752 | observe |
| roosterkid-openproxylist-v2ray | 0.261 | 1.0 | 1 | 150 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4955 | observe |
| DeltaKronecker-all | 0.255 | None | 0 | 2620 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 11127 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 6298 | observe |
| Au1rxx-clash | 0.245 | None | 0 | 1751 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 69 |
| speed | ClientOSError | - | 12 |
| 204 | ProxyError | - | 9 |
| cn-block | TimeoutError | - | 5 |
| cn-block | ClientOSError | - | 4 |
| cn-block | ProxyError | - | 3 |
| 204 | ClientOSError | - | 3 |
| 204 | TimeoutError | - | 3 |
| geo | ClientOSError | - | 2 |
| speed | ProxyError | - | 1 |
| speed | TimeoutError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 93 | 92 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
