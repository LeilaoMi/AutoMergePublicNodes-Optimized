# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-31 21:48:49 |
| 运行耗时 | 304.5s |
| 订阅源总数 | 107 |
| 健康订阅源 | 88 |
| 原始节点 | 80795 |
| 去重后节点 | 26337 |
| TCP 可达 | 3000 |
| 真实可用 | 509 |
| Verified 输出 | 99 |
| Global 输出 | 300 |
| All 输出 | 26337 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 8.7 |
| geo | 1.6 |
| tcp | 75.6 |
| probe | 94.4 |
| real_test | 84.2 |
| china_check | 27.7 |
| write_verified | 0.1 |
| generate | 12.4 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 47542 |
| vmess | 13806 |
| trojan | 8980 |
| shadowsocks | 8616 |
| hysteria2 | 1444 |
| shadowsocksr | 163 |
| http | 162 |
| socks | 48 |
| tuic | 12 |
| hysteria | 11 |
| anytls | 11 |

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
| 96.36 | hysteria2 | 258.4 | 2.2 | 21.8 | 14.92 | 10.0 | 13.12 | 18.02 | Au1rxx-base64 | 129.213.91.185 |
| 93.84 | shadowsocks | 264.4 | 4.2 | 21.66 | 14.84 | 10.0 | 13.48 | 18.02 | Au1rxx-base64 | 156.146.38.167 |
| 93.16 | shadowsocks | 271.9 | 8.5 | 21.48 | 14.68 | 10.0 | 13.48 | 18.02 | Au1rxx-base64 | 193.151.160.18 |
| 93.14 | shadowsocks | 286.3 | 0.1 | 21.15 | 14.99 | 10.0 | 13.48 | 18.02 | Au1rxx-base64 | 45.86.51.18 |
| 93.04 | shadowsocks | 299.5 | 8.1 | 20.84 | 14.7 | 10.0 | 13.48 | 18.02 | Au1rxx-base64 | 37.19.198.243 |
| 92.75 | shadowsocks | 317.8 | 4.5 | 20.42 | 14.83 | 10.0 | 13.48 | 18.02 | Au1rxx-base64 | 156.146.38.170 |
| 92.48 | shadowsocks | 312.8 | 5.0 | 20.54 | 14.81 | 10.0 | 13.48 | 18.02 | Au1rxx-base64 | 156.146.38.168 |
| 92.43 | shadowsocks | 317.1 | 0.2 | 20.44 | 14.99 | 10.0 | 13.48 | 18.02 | Au1rxx-base64 | 193.151.160.9 |
| 92.3 | trojan | 275.0 | 14.6 | 21.41 | 14.45 | 8.98 | 11.94 | 18.02 | Au1rxx-base64 | 216.152.156.49 |
| 92.13 | shadowsocks | 317.3 | 8.1 | 20.43 | 14.7 | 10.0 | 13.48 | 18.02 | Au1rxx-base64 | 185.230.230.18 |
| 92.06 | trojan | 281.8 | 5.6 | 21.25 | 14.79 | 8.98 | 11.94 | 18.02 | Au1rxx-base64 | 216.152.156.65 |
| 91.44 | vless | 301.0 | 5.6 | 20.81 | 14.79 | 10.0 | 8.36 | 18.02 | Au1rxx-base64 | 167.17.69.171 |
| 91.36 | vless | 281.0 | 1.4 | 21.27 | 14.95 | 8.76 | 8.36 | 18.02 | Au1rxx-base64 | 5.34.178.120 |
| 91.17 | shadowsocks | 300.8 | 2.9 | 20.81 | 14.89 | 10.0 | 13.48 | 18.02 | Au1rxx-base64 | 193.151.163.18 |
| 91.05 | trojan | 336.8 | 23.8 | 19.98 | 14.11 | 10.0 | 11.94 | 18.02 | Au1rxx-base64 | 66.23.203.21 |
| 90.78 | trojan | 273.0 | 0.6 | 21.46 | 14.98 | 6.88 | 11.94 | 18.02 | Au1rxx-base64 | 216.152.156.81 |
| 90.75 | vless | 271.8 | 2.7 | 21.49 | 14.9 | 8.68 | 8.36 | 18.02 | Au1rxx-base64 | 195.123.235.183 |
| 90.68 | trojan | 274.2 | 3.6 | 21.43 | 14.87 | 6.92 | 11.94 | 18.02 | Au1rxx-base64 | 169.197.140.245 |
| 90.56 | trojan | 277.3 | 5.1 | 21.36 | 14.81 | 6.93 | 11.94 | 18.02 | Au1rxx-base64 | 169.197.140.169 |
| 90.53 | trojan | 280.0 | 4.0 | 21.3 | 14.85 | 6.92 | 11.94 | 18.02 | Au1rxx-base64 | 169.197.140.218 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| mheidari-all | 0.959 | 0.887 | 97 | 14850 | prefer |
| Au1rxx-base64 | 0.931 | 0.864 | 330 | 1751 | prefer |
| zhangkai | 0.877 | 0.947 | 19 | 43 | prefer |
| Surfboard-tg-mixed | 0.754 | 0.676 | 170 | 7936 | prefer |
| DeltaKronecker-all | 0.391 | 1.0 | 2 | 2848 | observe |
| ermaozi-get_subscribe | 0.328 | 1.0 | 2 | 412 | observe |
| xiaoji235-airport-v2ray-all | 0.287 | 0.5 | 2 | 6752 | observe |
| peasoft-NoMoreWalls | 0.264 | 1.0 | 1 | 227 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4970 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 10505 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5636 | observe |
| barry-far-vless | 0.255 | None | 0 | 5849 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4635 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 41 |
| geo | ClientOSError | - | 39 |
| 204 | ProxyError | - | 7 |
| cn-block | ClientOSError | - | 6 |
| 204 | ClientOSError | - | 5 |
| cn-block | TimeoutError | - | 5 |
| 204 | TimeoutError | - | 4 |
| speed | ClientOSError | - | 2 |
| cn-block | ProxyError | - | 1 |
| geo | ProxyError | - | 1 |
| speed | ProxyError | - | 1 |
| speed | TimeoutError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 146 | 99 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
