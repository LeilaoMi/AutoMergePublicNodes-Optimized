# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-11-21 19:33:07 |
| 运行耗时 | 305.8s |
| 订阅源总数 | 107 |
| 健康订阅源 | 87 |
| 原始节点 | 83259 |
| 去重后节点 | 27850 |
| TCP 可达 | 3000 |
| 真实可用 | 274 |
| Verified 输出 | 36 |
| Global 输出 | 279 |
| All 输出 | 27850 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.7 |
| geo | 1.5 |
| tcp | 78.3 |
| probe | 95.2 |
| real_test | 85.5 |
| china_check | 23.5 |
| write_verified | 0.0 |
| generate | 15.0 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 48974 |
| vmess | 15061 |
| shadowsocks | 10373 |
| trojan | 6902 |
| hysteria2 | 1513 |
| shadowsocksr | 154 |
| http | 121 |
| socks | 108 |
| hysteria | 24 |
| tuic | 17 |
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
| 93.88 | shadowsocks | 241.9 | 4.6 | 22.18 | 14.83 | 10.0 | 13.37 | 17.5 | Au1rxx-base64 | 37.19.198.160 |
| 93.38 | shadowsocks | 253.1 | 11.0 | 21.92 | 14.59 | 10.0 | 13.37 | 17.5 | Au1rxx-base64 | 37.19.198.244 |
| 92.98 | vless | 342.5 | 5.0 | 19.85 | 14.81 | 10.0 | 10.82 | 17.5 | Au1rxx-base64 | 167.17.69.171 |
| 92.9 | vless | 352.7 | 0.7 | 19.61 | 14.97 | 10.0 | 10.82 | 17.5 | Au1rxx-base64 | 169.40.42.202 |
| 91.23 | vless | 328.3 | 2.5 | 20.18 | 14.91 | 10.0 | 10.82 | 17.5 | Au1rxx-base64 | 169.40.42.74 |
| 90.75 | shadowsocks | 340.2 | 13.9 | 19.9 | 14.48 | 10.0 | 13.37 | 17.5 | Au1rxx-base64 | 193.151.163.18 |
| 90.33 | vless | 386.5 | 8.2 | 18.83 | 14.69 | 8.49 | 10.82 | 17.5 | Au1rxx-base64 | 169.40.42.229 |
| 89.35 | shadowsocks | 404.3 | 11.8 | 18.42 | 14.56 | 10.0 | 13.37 | 17.5 | Au1rxx-base64 | 185.230.230.18 |
| 89.16 | shadowsocks | 253.2 | 10.7 | 21.92 | 14.6 | 10.0 | 13.37 | 17.5 | Au1rxx-base64 | 37.19.198.243 |
| 89.07 | shadowsocks | 370.0 | 8.2 | 19.21 | 14.69 | 10.0 | 13.37 | 17.5 | Au1rxx-base64 | 37.19.198.236 |
| 89.0 | shadowsocks | 413.0 | 0.7 | 18.22 | 14.97 | 10.0 | 13.37 | 17.5 | Au1rxx-base64 | 193.151.160.9 |
| 88.21 | shadowsocks | 449.5 | 0.2 | 17.37 | 14.99 | 9.48 | 13.37 | 17.5 | Au1rxx-base64 | 193.151.160.18 |
| 88.18 | shadowsocks | 384.0 | 3.5 | 18.89 | 14.87 | 10.0 | 13.37 | 17.5 | Au1rxx-base64 | 156.146.38.170 |
| 88.15 | http | 265.4 | 0.1 | 21.63 | 15.0 | 0.0 | 14.44 | 19.58 | ermaozi | 172.64.68.89 |
| 87.91 | shadowsocks | 475.3 | 6.3 | 16.78 | 14.76 | 10.0 | 13.37 | 17.5 | Au1rxx-base64 | 45.86.51.18 |
| 87.76 | shadowsocks | 480.6 | 6.9 | 16.65 | 14.74 | 10.0 | 13.37 | 17.5 | Au1rxx-base64 | 15.204.247.206 |
| 87.47 | shadowsocks | 393.2 | 7.8 | 18.68 | 14.71 | 10.0 | 13.37 | 17.5 | Au1rxx-base64 | 156.146.38.168 |
| 86.24 | vless | 332.8 | 6.0 | 20.07 | 14.78 | 10.0 | 10.82 | 17.5 | Au1rxx-base64 | 169.40.42.35 |
| 85.7 | shadowsocks | 390.5 | 1.3 | 18.74 | 14.95 | 10.0 | 13.37 | 17.5 | Au1rxx-base64 | 95.215.201.18 |
| 85.29 | vless | 347.3 | 7.1 | 19.74 | 14.73 | 10.0 | 10.82 | 17.5 | Au1rxx-base64 | 45.138.100.248 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.88 | 0.9 | 20 | 403 | prefer |
| mheidari-all | 0.877 | 0.805 | 77 | 14536 | prefer |
| Surfboard-tg-mixed | 0.707 | 0.628 | 226 | 8779 | prefer |
| Au1rxx-base64 | 0.505 | 0.434 | 136 | 1751 | observe |
| xiaoji235-airport-v2ray-all | 0.287 | 0.5 | 2 | 6752 | observe |
| ermaozi-get_subscribe | 0.267 | 1.0 | 1 | 303 | observe |
| tg-oneclickvpnkeys | 0.261 | 1.0 | 1 | 141 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5030 | observe |
| DeltaKronecker-all | 0.255 | None | 0 | 2989 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 12097 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5784 | observe |
| barry-far-vless | 0.255 | None | 0 | 5966 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4482 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 107 |
| 204 | ProxyError | - | 27 |
| cn-block | ClientOSError | - | 10 |
| cn-block | TimeoutError | - | 8 |
| cn-block | ProxyError | - | 6 |
| 204 | TimeoutError | - | 6 |
| 204 | ClientOSError | - | 5 |
| geo | ProxyError | - | 5 |
| speed | ProxyError | - | 3 |
| speed | TimeoutError | - | 2 |
| speed | ClientOSError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 52 | 36 | - |
| global | False | 300 | 279 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
