# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-18 16:04:07 |
| 运行耗时 | 307.1s |
| 订阅源总数 | 107 |
| 健康订阅源 | 93 |
| 原始节点 | 98093 |
| 去重后节点 | 27755 |
| TCP 可达 | 3000 |
| 真实可用 | 362 |
| Verified 输出 | 143 |
| Global 输出 | 300 |
| All 输出 | 27755 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.4 |
| geo | 1.6 |
| tcp | 82.5 |
| probe | 102.9 |
| real_test | 73.5 |
| china_check | 24.9 |
| generate | 14.2 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 57811 |
| vmess | 16733 |
| shadowsocks | 11746 |
| trojan | 9602 |
| hysteria2 | 1308 |
| http | 613 |
| shadowsocksr | 167 |
| socks | 67 |
| anytls | 22 |
| hysteria | 17 |
| tuic | 7 |

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
| 93.29 | vless | 268.5 | 1.5 | 21.56 | 14.94 | 10.0 | 9.21 | 17.58 | Au1rxx-base64 | 147.45.60.160 |
| 93.19 | shadowsocks | 251.1 | 4.0 | 21.97 | 14.85 | 10.0 | 12.79 | 17.58 | Au1rxx-base64 | 156.146.38.170 |
| 92.98 | shadowsocks | 260.9 | 3.6 | 21.74 | 14.87 | 10.0 | 12.79 | 17.58 | Au1rxx-base64 | 156.146.38.168 |
| 92.85 | shadowsocks | 256.0 | 10.0 | 21.85 | 14.63 | 10.0 | 12.79 | 17.58 | Au1rxx-base64 | 156.146.38.169 |
| 92.43 | shadowsocks | 285.3 | 2.9 | 21.17 | 14.89 | 10.0 | 12.79 | 17.58 | Au1rxx-base64 | 37.19.198.244 |
| 92.38 | shadowsocks | 285.7 | 4.1 | 21.16 | 14.85 | 10.0 | 12.79 | 17.58 | Au1rxx-base64 | 37.19.198.160 |
| 92.0 | shadowsocks | 294.4 | 8.8 | 20.96 | 14.67 | 10.0 | 12.79 | 17.58 | Au1rxx-base64 | 156.146.38.167 |
| 91.5 | vless | 273.6 | 1.0 | 21.44 | 14.96 | 8.31 | 9.21 | 17.58 | Au1rxx-base64 | 208.84.100.209 |
| 91.22 | vless | 342.3 | 3.1 | 19.85 | 14.89 | 9.73 | 9.21 | 17.58 | Au1rxx-base64 | 169.40.42.15 |
| 91.05 | vless | 340.8 | 4.3 | 19.89 | 14.84 | 9.73 | 9.21 | 17.58 | Au1rxx-base64 | 169.40.42.16 |
| 90.84 | vless | 318.2 | 29.1 | 20.41 | 13.91 | 9.73 | 9.21 | 17.58 | Au1rxx-base64 | 169.40.42.74 |
| 90.75 | vless | 346.0 | 13.0 | 19.77 | 14.51 | 9.74 | 9.21 | 17.58 | Au1rxx-base64 | 169.40.42.224 |
| 90.55 | vless | 385.8 | 1.9 | 18.85 | 14.93 | 10.0 | 9.21 | 17.58 | Au1rxx-base64 | 185.95.231.156 |
| 90.27 | hysteria2 | 276.2 | 27.8 | 21.39 | 13.96 | 8.04 | 10.8 | 17.58 | Au1rxx-base64 | 129.213.91.185 |
| 90.23 | vless | 317.8 | 1.1 | 20.42 | 14.96 | 8.06 | 9.21 | 17.58 | Au1rxx-base64 | 169.40.42.231 |
| 88.75 | vless | 382.2 | 0.4 | 18.93 | 14.98 | 8.05 | 9.21 | 17.58 | Au1rxx-base64 | 169.40.42.229 |
| 88.66 | vless | 262.3 | 9.1 | 21.71 | 14.66 | 10.0 | 9.21 | 17.58 | Au1rxx-base64 | 69.48.201.136 |
| 88.16 | vless | 321.8 | 45.9 | 20.33 | 13.28 | 10.0 | 9.21 | 17.58 | Au1rxx-base64 | 169.40.42.90 |
| 87.5 | vless | 285.7 | 12.0 | 21.16 | 14.55 | 10.0 | 9.21 | 17.58 | Au1rxx-base64 | 162.35.126.130 |
| 87.35 | vless | 374.4 | 0.2 | 19.11 | 14.99 | 10.0 | 9.21 | 17.58 | Au1rxx-base64 | 169.40.42.104 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.919 | 0.852 | 311 | 1729 | prefer |
| mheidari-all | 0.908 | 0.852 | 27 | 23775 | prefer |
| ermaozi | 0.863 | 0.857 | 35 | 639 | prefer |
| Surfboard-tg-mixed | 0.599 | 0.519 | 79 | 7095 | observe |
| tg-LonUp_M | 0.262 | 1.0 | 1 | 175 | observe |
| peasoft-NoMoreWalls | 0.26 | 1.0 | 1 | 123 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4983 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 10058 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5602 | observe |
| barry-far-vless | 0.255 | None | 0 | 5815 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4246 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.244 | None | 0 | 1729 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 50 |
| geo | ClientOSError | - | 22 |
| 204 | TimeoutError | - | 17 |
| speed | ClientOSError | - | 11 |
| 204 | ProxyError | - | 6 |
| cn-block | ProxyError | - | 5 |
| cn-block | ClientOSError | - | 4 |
| cn-block | TimeoutError | - | 4 |
| geo | ProxyError | - | 2 |
| 204 | ClientOSError | - | 2 |
| speed | TimeoutError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | True | 143 | 45 | 0.5 |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
