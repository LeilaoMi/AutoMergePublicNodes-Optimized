# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-11-27 21:31:53 |
| 运行耗时 | 279.3s |
| 订阅源总数 | 107 |
| 健康订阅源 | 86 |
| 原始节点 | 78578 |
| 去重后节点 | 27356 |
| TCP 可达 | 3000 |
| 真实可用 | 382 |
| Verified 输出 | 79 |
| Global 输出 | 300 |
| All 输出 | 27356 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.8 |
| geo | 1.4 |
| tcp | 80.8 |
| probe | 81.7 |
| real_test | 79.0 |
| china_check | 20.8 |
| write_verified | 0.0 |
| generate | 10.8 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 46023 |
| vmess | 15159 |
| shadowsocks | 9723 |
| trojan | 5500 |
| hysteria2 | 1612 |
| http | 208 |
| shadowsocksr | 156 |
| socks | 110 |
| anytls | 45 |
| hysteria | 30 |
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
| 88.57 | http | 271.8 | 1.6 | 21.49 | 14.94 | 0.0 | 14.66 | 19.98 | ermaozi | 172.64.69.89 |
| 87.7 | shadowsocks | 294.3 | 0.5 | 20.97 | 14.98 | 10.0 | 11.97 | 13.78 | Au1rxx-base64 | 37.19.198.244 |
| 87.68 | shadowsocks | 295.0 | 0.5 | 20.95 | 14.98 | 10.0 | 11.97 | 13.78 | Au1rxx-base64 | 37.19.198.160 |
| 87.54 | http | 280.0 | 10.8 | 21.3 | 14.6 | 0.0 | 14.66 | 19.98 | ermaozi | 198.44.138.27 |
| 86.96 | shadowsocks | 309.6 | 10.6 | 20.61 | 14.6 | 10.0 | 11.97 | 13.78 | Au1rxx-base64 | 37.19.198.243 |
| 86.79 | shadowsocks | 292.7 | 0.3 | 21.0 | 14.99 | 10.0 | 11.97 | 13.78 | Au1rxx-base64 | 185.230.230.18 |
| 85.15 | vless | 378.2 | 0.8 | 19.02 | 14.97 | 10.0 | 9.6 | 13.78 | Au1rxx-base64 | 169.40.42.74 |
| 84.71 | shadowsocks | 348.7 | 1.4 | 19.71 | 14.95 | 10.0 | 11.97 | 13.78 | Au1rxx-base64 | 193.151.160.9 |
| 84.7 | vless | 395.9 | 0.6 | 18.61 | 14.98 | 9.25 | 9.6 | 13.78 | Au1rxx-base64 | 169.40.42.90 |
| 84.34 | shadowsocks | 418.5 | 0.1 | 18.09 | 15.0 | 10.0 | 11.97 | 13.78 | Au1rxx-base64 | 45.86.51.18 |
| 82.79 | shadowsocks | 297.6 | 2.0 | 20.89 | 14.93 | 10.0 | 11.97 | 13.78 | Au1rxx-base64 | 173.244.56.9 |
| 82.78 | shadowsocks | 348.2 | 0.9 | 19.72 | 14.97 | 8.73 | 11.97 | 13.78 | Au1rxx-base64 | 193.151.160.18 |
| 82.64 | vless | 366.9 | 1.1 | 19.28 | 14.96 | 9.24 | 9.6 | 13.78 | Au1rxx-base64 | 169.40.42.202 |
| 82.41 | shadowsocks | 281.7 | 0.0 | 21.26 | 15.0 | 5.48 | 11.97 | 13.78 | Au1rxx-base64 | 156.146.38.169 |
| 82.34 | shadowsocks | 332.1 | 1.3 | 20.09 | 14.95 | 10.0 | 11.97 | 13.78 | Au1rxx-base64 | 95.215.201.18 |
| 81.77 | http | 321.3 | 1.8 | 20.34 | 14.93 | 0.0 | 14.66 | 19.98 | ermaozi | 38.95.111.226 |
| 81.7 | shadowsocks | 343.5 | 3.8 | 19.83 | 14.86 | 10.0 | 11.97 | 13.78 | Au1rxx-base64 | 173.244.56.6 |
| 81.45 | shadowsocks | 204.9 | 2.0 | 23.04 | 14.92 | 0.0 | 11.97 | 16.02 | Surfboard-tg-mixed | 216.106.178.169 |
| 81.37 | shadowsocks | 208.7 | 1.9 | 22.95 | 14.93 | 0.0 | 11.97 | 16.02 | Surfboard-tg-mixed | 67.220.73.178 |
| 81.35 | shadowsocks | 248.9 | 4.5 | 22.02 | 14.83 | 10.0 | 11.97 | 13.78 | Au1rxx-base64 | 156.146.38.170 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.979 | 0.979 | 48 | 466 | prefer |
| Au1rxx-base64 | 0.864 | 0.799 | 134 | 1751 | prefer |
| Surfboard-tg-mixed | 0.843 | 0.766 | 222 | 8496 | prefer |
| mheidari-all | 0.733 | 0.656 | 93 | 14418 | prefer |
| tg-LonUp_M | 0.52 | 1.0 | 7 | 174 | observe |
| mahdibland-V2RayAggregator | 0.335 | 1.0 | 1 | 4459 | observe |
| xiaoji235-airport-v2ray-all | 0.335 | 1.0 | 1 | 6752 | observe |
| ermaozi-get_subscribe | 0.272 | 1.0 | 1 | 417 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4895 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 11762 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5391 | observe |
| barry-far-vless | 0.255 | None | 0 | 5607 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.245 | None | 0 | 1751 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 75 |
| speed | TimeoutError | - | 6 |
| 204 | TimeoutError | - | 6 |
| 204 | ProxyError | - | 5 |
| cn-block | ClientOSError | - | 5 |
| speed | ClientOSError | - | 4 |
| geo | ClientOSError | - | 3 |
| speed | ProxyError | - | 2 |
| geo | TimeoutError | - | 2 |
| geo | ProxyError | - | 1 |
| 204 | ClientOSError | - | 1 |
| cn-block | ProxyError | - | 1 |
| cn-block | TimeoutError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 51 | 79 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
