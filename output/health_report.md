# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-11-07 22:03:58 |
| 运行耗时 | 268.4s |
| 订阅源总数 | 107 |
| 健康订阅源 | 87 |
| 原始节点 | 81598 |
| 去重后节点 | 26916 |
| TCP 可达 | 3000 |
| 真实可用 | 338 |
| Verified 输出 | 41 |
| Global 输出 | 300 |
| All 输出 | 26916 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.4 |
| geo | 1.4 |
| tcp | 78.7 |
| probe | 85.4 |
| real_test | 57.3 |
| china_check | 28.8 |
| write_verified | 0.0 |
| generate | 11.4 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 48361 |
| vmess | 14339 |
| shadowsocks | 9500 |
| trojan | 7469 |
| hysteria2 | 1541 |
| shadowsocksr | 151 |
| http | 94 |
| socks | 80 |
| hysteria | 25 |
| anytls | 22 |
| tuic | 16 |

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
| 95.06 | shadowsocks | 236.6 | 0.7 | 22.3 | 14.97 | 10.0 | 14.33 | 17.46 | Au1rxx-base64 | 37.19.198.236 |
| 94.56 | shadowsocks | 253.1 | 3.9 | 21.92 | 14.85 | 10.0 | 14.33 | 17.46 | Au1rxx-base64 | 37.19.198.244 |
| 94.3 | shadowsocks | 248.1 | 0.4 | 22.03 | 14.98 | 10.0 | 14.33 | 17.46 | Au1rxx-base64 | 185.230.230.18 |
| 94.16 | shadowsocks | 243.2 | 7.5 | 22.15 | 14.72 | 10.0 | 14.33 | 17.46 | Au1rxx-base64 | 45.86.51.18 |
| 94.0 | shadowsocks | 260.5 | 1.0 | 21.75 | 14.96 | 10.0 | 14.33 | 17.46 | Au1rxx-base64 | 193.151.163.18 |
| 93.27 | shadowsocks | 309.7 | 3.6 | 20.61 | 14.87 | 10.0 | 14.33 | 17.46 | Au1rxx-base64 | 37.19.198.160 |
| 93.13 | shadowsocks | 296.8 | 0.7 | 20.91 | 14.97 | 10.0 | 14.33 | 17.46 | Au1rxx-base64 | 193.151.160.9 |
| 92.43 | shadowsocks | 275.8 | 2.8 | 21.39 | 14.9 | 10.0 | 14.33 | 17.46 | Au1rxx-base64 | 156.146.38.168 |
| 92.07 | shadowsocks | 292.9 | 0.9 | 21.0 | 14.96 | 8.82 | 14.33 | 17.46 | Au1rxx-base64 | 193.151.160.18 |
| 91.97 | shadowsocks | 345.3 | 2.7 | 19.78 | 14.9 | 10.0 | 14.33 | 17.46 | Au1rxx-base64 | 15.204.247.206 |
| 91.95 | vless | 257.3 | 2.6 | 21.82 | 14.9 | 9.25 | 8.52 | 17.46 | Au1rxx-base64 | 159.89.87.21 |
| 91.76 | shadowsocks | 277.5 | 1.6 | 21.35 | 14.94 | 10.0 | 14.33 | 17.46 | Au1rxx-base64 | 156.146.38.167 |
| 91.61 | vless | 274.6 | 4.2 | 21.42 | 14.84 | 9.37 | 8.52 | 17.46 | Au1rxx-base64 | 167.17.69.171 |
| 91.35 | shadowsocks | 250.3 | 4.7 | 21.98 | 14.82 | 10.0 | 14.33 | 17.46 | Au1rxx-base64 | 37.19.198.243 |
| 91.2 | shadowsocks | 278.7 | 0.2 | 21.33 | 14.99 | 10.0 | 14.33 | 17.46 | Au1rxx-base64 | 156.146.38.170 |
| 90.89 | trojan | 284.2 | 4.8 | 21.2 | 14.82 | 8.38 | 12.86 | 17.46 | Au1rxx-base64 | 170.101.101.67 |
| 90.39 | vless | 250.2 | 3.5 | 21.99 | 14.87 | 8.2 | 8.52 | 17.46 | Au1rxx-base64 | 195.123.235.183 |
| 89.27 | vless | 374.8 | 21.5 | 19.1 | 14.19 | 10.0 | 8.52 | 17.46 | Au1rxx-base64 | 169.40.42.35 |
| 88.59 | vless | 348.6 | 11.1 | 19.71 | 14.58 | 9.34 | 8.52 | 17.46 | Au1rxx-base64 | 169.40.42.202 |
| 88.35 | trojan | 310.8 | 0.7 | 20.58 | 14.97 | 6.75 | 12.86 | 17.46 | Au1rxx-base64 | 169.197.140.218 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.942 | 1.0 | 19 | 515 | prefer |
| mheidari-all | 0.845 | 0.769 | 130 | 14235 | prefer |
| Au1rxx-base64 | 0.844 | 0.776 | 250 | 1751 | prefer |
| Surfboard-tg-mixed | 0.799 | 0.733 | 30 | 8421 | prefer |
| xiaoji235-airport-v2ray-all | 0.391 | 1.0 | 2 | 6752 | observe |
| ninja-vless | 0.383 | 1.0 | 2 | 1791 | observe |
| DeltaKronecker-all | 0.335 | 1.0 | 1 | 2734 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4866 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 11058 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5923 | observe |
| barry-far-vless | 0.255 | None | 0 | 6134 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4529 | observe |
| Au1rxx-clash | 0.245 | None | 0 | 1751 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 54 |
| 204 | ProxyError | - | 13 |
| 204 | TimeoutError | - | 11 |
| speed | TimeoutError | - | 4 |
| cn-block | TimeoutError | - | 4 |
| cn-block | ProxyError | - | 3 |
| speed | ClientOSError | - | 2 |
| speed | ProxyError | - | 1 |
| geo | ProxyError | - | 1 |
| geo | TimeoutError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 68 | 41 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
