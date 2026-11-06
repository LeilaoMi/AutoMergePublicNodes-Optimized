# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-11-06 19:36:22 |
| 运行耗时 | 254.3s |
| 订阅源总数 | 107 |
| 健康订阅源 | 87 |
| 原始节点 | 82563 |
| 去重后节点 | 26734 |
| TCP 可达 | 3000 |
| 真实可用 | 279 |
| Verified 输出 | 123 |
| Global 输出 | 282 |
| All 输出 | 26734 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.8 |
| geo | 1.4 |
| tcp | 77.7 |
| probe | 79.6 |
| real_test | 57.5 |
| china_check | 22.2 |
| generate | 11.1 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 49407 |
| vmess | 14682 |
| shadowsocks | 9103 |
| trojan | 7289 |
| hysteria2 | 1577 |
| http | 202 |
| shadowsocksr | 155 |
| socks | 79 |
| hysteria | 34 |
| anytls | 20 |
| tuic | 15 |

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
| 94.15 | shadowsocks | 242.2 | 7.7 | 22.17 | 14.71 | 10.0 | 14.11 | 17.16 | Au1rxx-base64 | 37.19.198.244 |
| 94.0 | shadowsocks | 239.0 | 0.5 | 22.25 | 14.98 | 10.0 | 14.11 | 17.16 | Au1rxx-base64 | 45.86.51.18 |
| 93.53 | shadowsocks | 273.2 | 5.1 | 21.45 | 14.81 | 10.0 | 14.11 | 17.16 | Au1rxx-base64 | 37.19.198.243 |
| 93.29 | shadowsocks | 266.3 | 2.4 | 21.61 | 14.91 | 10.0 | 14.11 | 17.16 | Au1rxx-base64 | 193.151.163.18 |
| 92.05 | shadowsocks | 254.1 | 3.3 | 21.9 | 14.88 | 10.0 | 14.11 | 17.16 | Au1rxx-base64 | 37.19.198.236 |
| 91.58 | vless | 269.8 | 3.4 | 21.53 | 14.87 | 8.71 | 9.31 | 17.16 | Au1rxx-base64 | 167.17.69.171 |
| 91.4 | vless | 336.3 | 1.5 | 19.99 | 14.94 | 10.0 | 9.31 | 17.16 | Au1rxx-base64 | 169.40.42.35 |
| 91.37 | shadowsocks | 372.5 | 1.3 | 19.15 | 14.95 | 10.0 | 14.11 | 17.16 | Au1rxx-base64 | 37.19.198.160 |
| 90.99 | vless | 345.4 | 7.0 | 19.78 | 14.74 | 10.0 | 9.31 | 17.16 | Au1rxx-base64 | 169.40.42.74 |
| 89.97 | vless | 340.5 | 3.4 | 19.9 | 14.87 | 8.73 | 9.31 | 17.16 | Au1rxx-base64 | 169.40.42.202 |
| 89.83 | shadowsocks | 280.2 | 2.6 | 21.29 | 14.9 | 6.37 | 14.11 | 17.16 | Au1rxx-base64 | 198.98.53.130 |
| 89.76 | shadowsocks | 412.2 | 6.6 | 18.24 | 14.75 | 10.0 | 14.11 | 17.16 | Au1rxx-base64 | 185.230.230.18 |
| 89.04 | vless | 312.1 | 4.6 | 20.55 | 14.83 | 8.74 | 9.31 | 17.16 | Au1rxx-base64 | 169.40.42.168 |
| 88.69 | vless | 389.2 | 6.6 | 18.77 | 14.75 | 8.7 | 9.31 | 17.16 | Au1rxx-base64 | 159.89.87.21 |
| 88.38 | shadowsocks | 280.4 | 4.6 | 21.29 | 14.83 | 10.0 | 14.11 | 17.16 | Au1rxx-base64 | 156.146.38.168 |
| 88.21 | shadowsocks | 411.8 | 0.3 | 18.24 | 14.99 | 8.46 | 14.11 | 17.16 | Au1rxx-base64 | 193.151.160.18 |
| 88.06 | vless | 315.0 | 4.9 | 20.49 | 14.82 | 7.35 | 9.31 | 17.16 | Au1rxx-base64 | 2.24.124.64 |
| 87.89 | vless | 298.0 | 3.3 | 20.88 | 14.88 | 8.66 | 9.31 | 17.16 | Au1rxx-base64 | 66.70.179.198 |
| 86.97 | shadowsocks | 313.6 | 0.1 | 20.52 | 15.0 | 10.0 | 14.11 | 17.16 | Au1rxx-base64 | 173.244.56.6 |
| 86.91 | trojan | 348.6 | 0.1 | 19.71 | 14.99 | 10.0 | 13.27 | 17.16 | Au1rxx-base64 | 66.163.112.121 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.992 | 1.0 | 33 | 513 | prefer |
| mheidari-all | 0.861 | 0.786 | 103 | 14184 | prefer |
| Au1rxx-base64 | 0.853 | 0.785 | 205 | 1751 | prefer |
| xiaoji235-airport-v2ray-all | 0.335 | 1.0 | 1 | 6752 | observe |
| DeltaKronecker-all | 0.287 | 0.5 | 2 | 2768 | observe |
| tg-LonUp_M | 0.262 | 1.0 | 1 | 179 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4934 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 10962 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 6135 | observe |
| barry-far-vless | 0.255 | None | 0 | 6479 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4703 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.245 | None | 0 | 1751 | observe |
| Surfboard-tg-mixed | 0.239 | 0.167 | 12 | 8758 | downweight |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 31 |
| 204 | ProxyError | - | 29 |
| cn-block | ProxyError | - | 5 |
| 204 | TimeoutError | - | 4 |
| geo | ProxyError | - | 3 |
| 204 | ClientOSError | - | 2 |
| cn-block | TimeoutError | - | 1 |
| speed | TimeoutError | - | 1 |
| geo | TimeoutError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | True | 123 | 42 | 0.5 |
| global | False | 300 | 282 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
