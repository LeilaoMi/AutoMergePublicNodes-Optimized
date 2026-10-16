# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-16 15:17:41 |
| 运行耗时 | 304.5s |
| 订阅源总数 | 107 |
| 健康订阅源 | 93 |
| 原始节点 | 99232 |
| 去重后节点 | 27717 |
| TCP 可达 | 3000 |
| 真实可用 | 404 |
| Verified 输出 | 77 |
| Global 输出 | 300 |
| All 输出 | 27717 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 10.7 |
| geo | 1.5 |
| tcp | 85.6 |
| probe | 94.8 |
| real_test | 80.9 |
| china_check | 17.0 |
| write_verified | 0.0 |
| generate | 14.0 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 58464 |
| vmess | 16388 |
| shadowsocks | 12056 |
| trojan | 10076 |
| hysteria2 | 1311 |
| http | 662 |
| shadowsocksr | 164 |
| socks | 59 |
| anytls | 29 |
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
| 95.49 | hysteria2 | 238.7 | 1.2 | 22.25 | 14.96 | 10.0 | 13.12 | 16.66 | Au1rxx-base64 | 129.213.91.185 |
| 93.0 | shadowsocks | 258.5 | 1.7 | 21.79 | 14.94 | 10.0 | 13.61 | 16.66 | Au1rxx-base64 | 37.19.198.236 |
| 92.97 | shadowsocks | 258.8 | 2.5 | 21.79 | 14.91 | 10.0 | 13.61 | 16.66 | Au1rxx-base64 | 37.19.198.160 |
| 92.96 | shadowsocks | 259.1 | 2.5 | 21.78 | 14.91 | 10.0 | 13.61 | 16.66 | Au1rxx-base64 | 37.19.198.244 |
| 92.79 | vless | 247.1 | 1.2 | 22.06 | 14.96 | 10.0 | 9.11 | 16.66 | Au1rxx-base64 | 147.45.60.160 |
| 92.39 | shadowsocks | 284.8 | 1.7 | 21.18 | 14.94 | 10.0 | 13.61 | 16.66 | Au1rxx-base64 | 37.19.198.243 |
| 90.38 | vless | 346.8 | 3.7 | 19.75 | 14.86 | 10.0 | 9.11 | 16.66 | Au1rxx-base64 | 185.95.231.156 |
| 89.93 | shadowsocks | 284.5 | 2.2 | 21.19 | 14.92 | 10.0 | 13.61 | 16.66 | Au1rxx-base64 | 156.146.38.167 |
| 89.38 | shadowsocks | 374.7 | 13.1 | 19.1 | 14.51 | 10.0 | 13.61 | 16.66 | Au1rxx-base64 | 15.204.233.41 |
| 89.1 | shadowsocks | 327.4 | 0.0 | 20.2 | 15.0 | 10.0 | 13.61 | 16.66 | Au1rxx-base64 | 156.146.38.170 |
| 89.06 | shadowsocks | 281.7 | 1.7 | 21.26 | 14.94 | 10.0 | 13.61 | 16.66 | Au1rxx-base64 | 156.146.38.168 |
| 88.82 | shadowsocks | 369.1 | 19.1 | 19.23 | 14.29 | 10.0 | 13.61 | 16.66 | Au1rxx-base64 | 51.222.136.236 |
| 88.68 | http | 238.3 | 2.8 | 22.26 | 14.9 | 0.0 | 14.52 | 20.0 | ermaozi | 198.44.135.19 |
| 88.24 | shadowsocks | 283.5 | 1.1 | 21.21 | 14.96 | 10.0 | 13.61 | 16.66 | Au1rxx-base64 | 156.146.38.169 |
| 86.98 | vless | 295.1 | 1.1 | 20.95 | 14.96 | 5.3 | 9.11 | 16.66 | Au1rxx-base64 | 66.70.179.198 |
| 86.23 | hysteria2 | 391.5 | 8.0 | 18.72 | 14.7 | 9.85 | 13.12 | 16.66 | Au1rxx-base64 | 62.210.124.146 |
| 86.14 | shadowsocks | 321.2 | 0.8 | 20.34 | 14.97 | 10.0 | 13.61 | 16.66 | Au1rxx-base64 | 173.244.56.6 |
| 85.83 | vless | 344.3 | 6.7 | 19.81 | 14.75 | 10.0 | 9.11 | 16.66 | Au1rxx-base64 | 104.243.33.154 |
| 85.79 | vless | 315.4 | 7.5 | 20.48 | 14.72 | 10.0 | 9.11 | 16.66 | Au1rxx-base64 | 131.143.180.110 |
| 85.68 | trojan | 420.5 | 7.8 | 18.04 | 14.71 | 7.03 | 12.24 | 16.66 | Au1rxx-base64 | 69.164.240.85 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.991 | 0.982 | 57 | 618 | prefer |
| Au1rxx-base64 | 0.829 | 0.751 | 441 | 1991 | prefer |
| mheidari-all | 0.616 | 0.538 | 26 | 23974 | observe |
| Au1rxx-clash | 0.335 | 1.0 | 1 | 1991 | observe |
| Surfboard-tg-mixed | 0.32 | 0.5 | 4 | 7090 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5024 | observe |
| Epodonios-all | 0.255 | None | 0 | 7602 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 10100 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5572 | observe |
| barry-far-vless | 0.255 | None | 0 | 5822 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4265 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 72 |
| speed | ClientOSError | - | 13 |
| 204 | TimeoutError | - | 13 |
| 204 | ProxyError | - | 10 |
| cn-block | ClientOSError | - | 6 |
| cn-block | TimeoutError | - | 5 |
| 204 | ClientOSError | - | 4 |
| cn-block | ProxyError | - | 2 |
| geo | ClientOSError | - | 2 |
| speed | ClientPayloadError | - | 1 |
| geo | ProxyError | - | 1 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 79 | 77 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
