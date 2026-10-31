# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-31 12:51:42 |
| 运行耗时 | 291.2s |
| 订阅源总数 | 107 |
| 健康订阅源 | 88 |
| 原始节点 | 80647 |
| 去重后节点 | 26392 |
| TCP 可达 | 3000 |
| 真实可用 | 399 |
| Verified 输出 | 146 |
| Global 输出 | 300 |
| All 输出 | 26392 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.2 |
| geo | 1.5 |
| tcp | 72.9 |
| probe | 91.7 |
| real_test | 81.1 |
| china_check | 22.2 |
| generate | 14.6 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 48255 |
| vmess | 13586 |
| shadowsocks | 8534 |
| trojan | 8409 |
| hysteria2 | 1456 |
| shadowsocksr | 163 |
| http | 159 |
| socks | 49 |
| tuic | 14 |
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
| 96.72 | hysteria2 | 224.4 | 1.8 | 22.58 | 14.93 | 10.0 | 12.19 | 18.52 | Au1rxx-base64 | 129.213.91.185 |
| 94.31 | shadowsocks | 255.4 | 0.4 | 21.86 | 14.98 | 10.0 | 12.95 | 18.52 | Au1rxx-base64 | 37.19.198.243 |
| 94.25 | shadowsocks | 233.5 | 2.5 | 22.37 | 14.91 | 10.0 | 12.95 | 18.52 | Au1rxx-base64 | 45.86.51.18 |
| 94.24 | vless | 253.6 | 12.1 | 21.91 | 14.55 | 10.0 | 9.26 | 18.52 | Au1rxx-base64 | 159.89.87.21 |
| 94.09 | vless | 273.8 | 3.5 | 21.44 | 14.87 | 10.0 | 9.26 | 18.52 | Au1rxx-base64 | 167.17.69.171 |
| 94.07 | vless | 278.1 | 1.4 | 21.34 | 14.95 | 10.0 | 9.26 | 18.52 | Au1rxx-base64 | 66.70.179.198 |
| 94.06 | shadowsocks | 238.4 | 4.5 | 22.26 | 14.83 | 10.0 | 12.95 | 18.52 | Au1rxx-base64 | 185.230.230.18 |
| 93.77 | vless | 232.3 | 0.3 | 22.4 | 14.99 | 8.6 | 9.26 | 18.52 | Au1rxx-base64 | 195.123.235.183 |
| 93.72 | shadowsocks | 259.3 | 0.7 | 21.78 | 14.97 | 10.0 | 12.95 | 18.52 | Au1rxx-base64 | 193.151.163.18 |
| 93.21 | trojan | 262.0 | 1.8 | 21.71 | 14.93 | 6.54 | 14.01 | 18.52 | Au1rxx-base64 | 216.152.155.54 |
| 92.36 | vless | 351.1 | 1.9 | 19.65 | 14.93 | 10.0 | 9.26 | 18.52 | Au1rxx-base64 | 169.40.42.202 |
| 92.35 | trojan | 260.5 | 2.8 | 21.75 | 14.9 | 5.67 | 14.01 | 18.52 | Au1rxx-base64 | 216.152.155.176 |
| 92.33 | shadowsocks | 288.5 | 3.9 | 21.1 | 14.85 | 9.41 | 12.95 | 18.52 | Au1rxx-base64 | 193.151.160.18 |
| 92.26 | trojan | 327.3 | 3.9 | 20.2 | 14.85 | 7.18 | 14.01 | 18.52 | Au1rxx-base64 | 216.152.155.23 |
| 92.07 | vless | 364.7 | 1.0 | 19.33 | 14.96 | 10.0 | 9.26 | 18.52 | Au1rxx-base64 | 169.40.42.90 |
| 92.03 | shadowsocks | 274.3 | 0.0 | 21.43 | 15.0 | 10.0 | 12.95 | 18.52 | Au1rxx-base64 | 156.146.38.167 |
| 92.0 | shadowsocks | 301.6 | 20.5 | 20.8 | 14.23 | 10.0 | 12.95 | 18.52 | Au1rxx-base64 | 193.151.160.9 |
| 91.93 | trojan | 431.2 | 10.5 | 17.8 | 14.6 | 10.0 | 14.01 | 18.52 | Au1rxx-base64 | 69.164.240.85 |
| 91.71 | trojan | 285.3 | 5.7 | 21.17 | 14.79 | 5.72 | 14.01 | 18.52 | Au1rxx-base64 | 170.101.101.131 |
| 91.63 | shadowsocks | 290.3 | 0.8 | 21.06 | 14.97 | 10.0 | 12.95 | 18.52 | Au1rxx-base64 | 156.146.38.170 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.901 | 0.833 | 324 | 1751 | prefer |
| zhangkai | 0.877 | 0.947 | 19 | 43 | prefer |
| Surfboard-tg-mixed | 0.738 | 0.667 | 36 | 7861 | prefer |
| DeltaKronecker-all | 0.622 | 0.667 | 15 | 2848 | observe |
| mheidari-all | 0.587 | 0.507 | 146 | 14723 | observe |
| mahdibland-V2RayAggregator | 0.287 | 0.5 | 2 | 4635 | observe |
| ermaozi-get_subscribe | 0.271 | 1.0 | 1 | 412 | observe |
| xiaoji235-airport-v2ray-all | 0.259 | 0.333 | 3 | 6752 | observe |
| ermaozi | 0.258 | 1.0 | 1 | 79 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4970 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 10576 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5698 | observe |
| barry-far-vless | 0.255 | None | 0 | 5912 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 90 |
| geo | ClientOSError | - | 16 |
| 204 | ProxyError | - | 9 |
| 204 | TimeoutError | - | 8 |
| cn-block | ProxyError | - | 7 |
| cn-block | TimeoutError | - | 6 |
| geo | TimeoutError | - | 3 |
| 204 | ClientOSError | - | 2 |
| geo | ProxyError | - | 2 |
| speed | ClientOSError | - | 2 |
| cn-block | ClientOSError | - | 2 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | True | 146 | 68 | 0.5 |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
