# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-11-22 07:09:37 |
| 运行耗时 | 272.0s |
| 订阅源总数 | 107 |
| 健康订阅源 | 88 |
| 原始节点 | 83494 |
| 去重后节点 | 28090 |
| TCP 可达 | 3000 |
| 真实可用 | 282 |
| Verified 输出 | 52 |
| Global 输出 | 284 |
| All 输出 | 28090 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.5 |
| geo | 1.6 |
| tcp | 77.4 |
| probe | 85.9 |
| real_test | 65.8 |
| china_check | 24.4 |
| write_verified | 0.0 |
| generate | 11.5 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 49465 |
| vmess | 15069 |
| shadowsocks | 10229 |
| trojan | 6786 |
| hysteria2 | 1501 |
| shadowsocksr | 163 |
| http | 110 |
| socks | 108 |
| hysteria | 31 |
| tuic | 18 |
| anytls | 14 |

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
| 85.63 | hysteria2 | 325.2 | 2.5 | 20.25 | 14.91 | 0.0 | 13.93 | 17.54 | mheidari-all | 34.24.25.1 |
| 83.76 | http | 299.8 | 1.0 | 20.84 | 14.96 | 0.0 | 12.86 | 17.6 | ermaozi | 172.64.68.89 |
| 82.73 | shadowsocks | 248.7 | 1.9 | 22.02 | 14.93 | 10.0 | 9.68 | 10.1 | Au1rxx-base64 | 156.146.38.168 |
| 82.44 | vless | 304.6 | 0.9 | 20.73 | 14.97 | 9.93 | 8.81 | 10.1 | Au1rxx-base64 | 167.17.69.171 |
| 81.97 | vless | 265.1 | 0.4 | 21.64 | 14.98 | 0.0 | 8.81 | 17.54 | mheidari-all | 216.227.161.95 |
| 81.93 | shadowsocks | 286.4 | 0.1 | 21.15 | 15.0 | 10.0 | 9.68 | 10.1 | Au1rxx-base64 | 37.19.198.236 |
| 81.64 | vless | 399.8 | 3.5 | 18.52 | 14.87 | 9.98 | 8.81 | 10.1 | Au1rxx-base64 | 169.40.42.89 |
| 81.19 | shadowsocks | 290.8 | 3.6 | 21.05 | 14.86 | 10.0 | 9.68 | 10.1 | Au1rxx-base64 | 45.86.51.18 |
| 81.17 | shadowsocks | 287.2 | 6.4 | 21.13 | 14.76 | 10.0 | 9.68 | 10.1 | Au1rxx-base64 | 185.230.230.18 |
| 81.14 | shadowsocks | 313.2 | 4.6 | 20.53 | 14.83 | 10.0 | 9.68 | 10.1 | Au1rxx-base64 | 156.146.38.170 |
| 80.8 | shadowsocks | 285.5 | 0.9 | 21.17 | 14.97 | 9.38 | 9.68 | 10.1 | Au1rxx-base64 | 193.151.160.18 |
| 80.78 | vless | 343.2 | 2.3 | 19.83 | 14.91 | 9.97 | 8.81 | 10.1 | Au1rxx-base64 | 169.40.42.202 |
| 80.74 | shadowsocks | 291.4 | 0.8 | 21.03 | 14.97 | 10.0 | 9.68 | 10.1 | Au1rxx-base64 | 37.19.198.160 |
| 80.57 | vless | 414.2 | 0.4 | 18.19 | 14.99 | 9.98 | 8.81 | 10.1 | Au1rxx-base64 | 169.40.42.90 |
| 79.89 | http | 336.5 | 1.5 | 19.99 | 14.94 | 0.0 | 12.86 | 17.6 | ermaozi | 172.64.69.89 |
| 79.87 | shadowsocks | 263.4 | 0.6 | 21.68 | 14.98 | 10.0 | 9.68 | 10.1 | Au1rxx-base64 | 37.19.198.243 |
| 79.49 | vless | 415.9 | 3.7 | 18.15 | 14.86 | 8.42 | 8.81 | 10.1 | Au1rxx-base64 | 169.40.42.229 |
| 79.1 | shadowsocks | 272.6 | 2.4 | 21.47 | 14.91 | 0.0 | 9.68 | 17.54 | mheidari-all | 38.91.107.57 |
| 78.54 | vless | 261.6 | 2.5 | 21.72 | 14.91 | 0.0 | 8.81 | 17.54 | mheidari-all | 69.17.3.150 |
| 78.48 | hysteria2 | 371.2 | 8.0 | 19.19 | 14.7 | 0.0 | 13.93 | 17.54 | mheidari-all | 62.210.124.146 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.881 | 0.816 | 125 | 1751 | prefer |
| ermaozi | 0.823 | 0.941 | 17 | 399 | prefer |
| mheidari-all | 0.735 | 0.656 | 224 | 14453 | prefer |
| zhangkai | 0.688 | 1.0 | 12 | 27 | observe |
| Surfboard-tg-mixed | 0.606 | 0.889 | 9 | 8778 | observe |
| xiaoji235-airport-v2ray-all | 0.335 | 1.0 | 1 | 6752 | observe |
| ermaozi-get_subscribe | 0.282 | 0.667 | 3 | 327 | observe |
| tg-oneclickvpnkeys | 0.261 | 1.0 | 1 | 146 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5030 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 12093 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5942 | observe |
| barry-far-vless | 0.255 | None | 0 | 6124 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4512 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 45 |
| 204 | ProxyError | - | 16 |
| cn-block | ClientOSError | - | 14 |
| cn-block | ProxyError | - | 7 |
| speed | ProxyError | - | 6 |
| 204 | TimeoutError | - | 5 |
| geo | ProxyError | - | 4 |
| geo | ClientOSError | - | 2 |
| speed | TimeoutError | - | 2 |
| cn-block | TimeoutError | - | 2 |
| speed | ClientOSError | - | 1 |
| 204 | ClientOSError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 36 | 52 | - |
| global | False | 279 | 284 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
