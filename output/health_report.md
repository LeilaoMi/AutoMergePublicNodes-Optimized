# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-11-28 08:08:09 |
| 运行耗时 | 280.6s |
| 订阅源总数 | 107 |
| 健康订阅源 | 86 |
| 原始节点 | 77832 |
| 去重后节点 | 26998 |
| TCP 可达 | 3000 |
| 真实可用 | 342 |
| Verified 输出 | 49 |
| Global 输出 | 300 |
| All 输出 | 26998 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.9 |
| geo | 1.5 |
| tcp | 81.0 |
| probe | 79.8 |
| real_test | 77.7 |
| china_check | 24.7 |
| write_verified | 0.0 |
| generate | 11.0 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 45487 |
| vmess | 15267 |
| shadowsocks | 9652 |
| trojan | 5372 |
| hysteria2 | 1572 |
| shadowsocksr | 152 |
| http | 148 |
| socks | 101 |
| anytls | 37 |
| hysteria | 32 |
| tuic | 12 |

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
| 92.62 | shadowsocks | 191.0 | 1.4 | 23.36 | 14.95 | 10.0 | 11.53 | 17.28 | Au1rxx-base64 | 95.215.201.18 |
| 92.61 | vless | 233.9 | 1.0 | 22.36 | 14.96 | 7.52 | 10.49 | 17.28 | Au1rxx-base64 | 45.63.53.81 |
| 92.55 | shadowsocks | 214.9 | 1.7 | 22.8 | 14.94 | 10.0 | 11.53 | 17.28 | Au1rxx-base64 | 173.244.56.6 |
| 91.71 | shadowsocks | 252.3 | 1.1 | 21.94 | 14.96 | 10.0 | 11.53 | 17.28 | Au1rxx-base64 | 156.146.38.170 |
| 91.54 | shadowsocks | 257.3 | 1.1 | 21.82 | 14.96 | 10.0 | 11.53 | 17.28 | Au1rxx-base64 | 156.146.38.168 |
| 90.37 | shadowsocks | 209.3 | 0.1 | 22.93 | 15.0 | 10.0 | 11.53 | 17.28 | Au1rxx-base64 | 173.244.56.9 |
| 89.51 | http | 214.6 | 1.4 | 22.81 | 14.95 | 0.0 | 14.67 | 19.58 | ermaozi | 172.64.69.89 |
| 86.88 | vless | 271.4 | 3.0 | 21.5 | 14.89 | 9.6 | 10.49 | 17.28 | Au1rxx-base64 | 15.204.97.214 |
| 86.33 | shadowsocks | 286.0 | 1.8 | 21.16 | 14.93 | 5.43 | 11.53 | 17.28 | Au1rxx-base64 | 156.146.38.169 |
| 85.26 | shadowsocks | 349.4 | 0.1 | 19.69 | 15.0 | 10.0 | 11.53 | 17.28 | Au1rxx-base64 | 193.151.160.9 |
| 85.02 | shadowsocks | 342.4 | 0.4 | 19.85 | 14.99 | 10.0 | 11.53 | 17.28 | Au1rxx-base64 | 37.19.198.236 |
| 85.0 | shadowsocks | 339.1 | 0.7 | 19.93 | 14.97 | 10.0 | 11.53 | 17.28 | Au1rxx-base64 | 37.19.198.243 |
| 84.9 | shadowsocks | 340.9 | 2.0 | 19.89 | 14.93 | 10.0 | 11.53 | 17.28 | Au1rxx-base64 | 37.19.198.244 |
| 84.89 | shadowsocks | 344.7 | 0.5 | 19.8 | 14.98 | 10.0 | 11.53 | 17.28 | Au1rxx-base64 | 185.230.230.18 |
| 84.13 | hysteria2 | 255.6 | 1.1 | 21.86 | 14.96 | 0.0 | 13.75 | 14.66 | mheidari-all | 172.87.24.53 |
| 83.91 | shadowsocks | 338.7 | 0.2 | 19.94 | 14.99 | 10.0 | 11.53 | 17.28 | Au1rxx-base64 | 37.19.198.160 |
| 83.86 | shadowsocks | 349.1 | 0.2 | 19.7 | 14.99 | 10.0 | 11.53 | 17.28 | Au1rxx-base64 | 193.151.163.18 |
| 83.12 | shadowsocks | 352.9 | 5.4 | 19.61 | 14.8 | 8.06 | 11.53 | 17.28 | Au1rxx-base64 | 193.151.160.18 |
| 83.06 | vless | 206.2 | 2.4 | 23.0 | 14.91 | 0.0 | 10.49 | 14.66 | mheidari-all | 172.235.53.103 |
| 82.73 | vless | 429.6 | 1.4 | 17.83 | 14.95 | 8.98 | 10.49 | 17.28 | Au1rxx-base64 | 159.89.87.21 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.973 | 1.0 | 21 | 405 | prefer |
| Surfboard-tg-mixed | 0.847 | 0.77 | 217 | 8437 | prefer |
| Au1rxx-base64 | 0.813 | 0.746 | 134 | 1751 | prefer |
| mheidari-all | 0.705 | 0.628 | 94 | 14211 | prefer |
| xiaoji235-airport-v2ray-all | 0.391 | 1.0 | 2 | 6752 | observe |
| ermaozi-get_subscribe | 0.269 | 1.0 | 1 | 357 | observe |
| tg-LonUp_M | 0.261 | 1.0 | 1 | 157 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4895 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 11621 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5299 | observe |
| barry-far-vless | 0.255 | None | 0 | 5482 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4526 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.245 | None | 0 | 1751 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 82 |
| 204 | ClientOSError | - | 7 |
| cn-block | ClientOSError | - | 6 |
| 204 | ProxyError | - | 6 |
| 204 | TimeoutError | - | 6 |
| speed | ClientOSError | - | 4 |
| cn-block | TimeoutError | - | 4 |
| speed | TimeoutError | - | 4 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 79 | 49 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
