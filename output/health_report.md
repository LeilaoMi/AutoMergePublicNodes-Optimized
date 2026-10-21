# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-21 17:26:59 |
| 运行耗时 | 284.4s |
| 订阅源总数 | 107 |
| 健康订阅源 | 92 |
| 原始节点 | 96402 |
| 去重后节点 | 26917 |
| TCP 可达 | 3000 |
| 真实可用 | 300 |
| Verified 输出 | 75 |
| Global 输出 | 300 |
| All 输出 | 26917 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.3 |
| geo | 1.5 |
| tcp | 81.4 |
| probe | 96.5 |
| real_test | 63.9 |
| china_check | 19.9 |
| write_verified | 0.0 |
| generate | 13.9 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 57260 |
| vmess | 17053 |
| shadowsocks | 11920 |
| trojan | 8545 |
| hysteria2 | 1253 |
| shadowsocksr | 161 |
| http | 110 |
| socks | 56 |
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
| 94.99 | hysteria2 | 237.7 | 6.9 | 22.28 | 14.74 | 9.57 | 13.0 | 16.9 | Au1rxx-base64 | 129.213.91.185 |
| 92.56 | shadowsocks | 232.5 | 2.1 | 22.4 | 14.92 | 9.56 | 13.28 | 16.9 | Au1rxx-base64 | 185.230.230.18 |
| 92.49 | shadowsocks | 237.9 | 0.4 | 22.27 | 14.99 | 9.55 | 13.28 | 16.9 | Au1rxx-base64 | 193.151.163.18 |
| 92.45 | shadowsocks | 256.1 | 2.8 | 21.85 | 14.89 | 9.53 | 13.28 | 16.9 | Au1rxx-base64 | 37.19.198.160 |
| 92.01 | shadowsocks | 279.6 | 0.1 | 21.31 | 15.0 | 9.52 | 13.28 | 16.9 | Au1rxx-base64 | 37.19.198.243 |
| 90.76 | shadowsocks | 267.2 | 0.4 | 21.59 | 14.99 | 9.5 | 13.28 | 16.9 | Au1rxx-base64 | 185.215.132.9 |
| 89.8 | shadowsocks | 299.6 | 7.5 | 20.84 | 14.72 | 9.56 | 13.28 | 16.9 | Au1rxx-base64 | 45.86.51.18 |
| 89.06 | vless | 256.9 | 8.3 | 21.83 | 14.69 | 8.4 | 9.69 | 16.9 | Au1rxx-base64 | 169.40.42.231 |
| 89.05 | shadowsocks | 282.4 | 0.1 | 21.24 | 15.0 | 9.2 | 13.28 | 16.9 | Au1rxx-base64 | 156.146.38.169 |
| 88.89 | shadowsocks | 292.2 | 1.0 | 21.01 | 14.96 | 9.36 | 13.28 | 16.9 | Au1rxx-base64 | 193.151.160.18 |
| 88.65 | shadowsocks | 291.7 | 0.4 | 21.02 | 14.98 | 6.47 | 13.28 | 16.9 | Au1rxx-base64 | 37.19.198.244 |
| 88.51 | vless | 395.2 | 2.9 | 18.63 | 14.89 | 8.4 | 9.69 | 16.9 | Au1rxx-base64 | 169.40.42.35 |
| 88.09 | vless | 272.0 | 1.2 | 21.48 | 14.96 | 5.06 | 9.69 | 16.9 | Au1rxx-base64 | 195.123.235.183 |
| 88.08 | vless | 340.7 | 12.7 | 19.89 | 14.53 | 7.07 | 9.69 | 16.9 | Au1rxx-base64 | 169.40.42.104 |
| 87.98 | vless | 349.2 | 10.2 | 19.69 | 14.62 | 7.08 | 9.69 | 16.9 | Au1rxx-base64 | 169.40.42.74 |
| 87.76 | shadowsocks | 378.9 | 0.1 | 19.01 | 14.99 | 9.37 | 13.28 | 16.9 | Au1rxx-base64 | 193.151.160.9 |
| 87.67 | shadowsocks | 321.1 | 0.5 | 20.35 | 14.98 | 9.21 | 13.28 | 16.9 | Au1rxx-base64 | 156.146.38.170 |
| 87.56 | vless | 340.5 | 2.4 | 19.9 | 14.91 | 6.16 | 9.69 | 16.9 | Au1rxx-base64 | 169.40.42.224 |
| 87.54 | vless | 289.7 | 1.0 | 21.07 | 14.96 | 4.92 | 9.69 | 16.9 | Au1rxx-base64 | 66.70.179.198 |
| 86.85 | http | 247.2 | 3.7 | 22.06 | 14.86 | 0.0 | 14.01 | 18.92 | ermaozi-get_subscribe | 198.44.135.19 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.967 | 1.0 | 27 | 31 | prefer |
| mheidari-all | 0.856 | 0.783 | 83 | 24102 | prefer |
| Au1rxx-base64 | 0.83 | 0.769 | 234 | 1566 | prefer |
| ermaozi-get_subscribe | 0.703 | 1.0 | 12 | 385 | prefer |
| Surfboard-tg-mixed | 0.543 | 0.615 | 13 | 7070 | observe |
| DeltaKronecker-all | 0.352 | 0.364 | 11 | 4067 | observe |
| ninja-vless | 0.327 | 1.0 | 1 | 1791 | observe |
| roosterkid-openproxylist-v2ray | 0.317 | 1.0 | 2 | 150 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4925 | observe |
| Epodonios-all | 0.255 | None | 0 | 7559 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 10000 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5554 | observe |
| barry-far-vless | 0.255 | None | 0 | 5768 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4127 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 43 |
| speed | ClientOSError | - | 15 |
| geo | ClientOSError | - | 8 |
| 204 | ProxyError | - | 7 |
| cn-block | ClientOSError | - | 5 |
| cn-block | TimeoutError | - | 4 |
| 204 | TimeoutError | - | 3 |
| cn-block | ProxyError | - | 2 |
| 204 | ClientOSError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 118 | 75 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
