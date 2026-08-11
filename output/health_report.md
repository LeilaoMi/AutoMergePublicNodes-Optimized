# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-11 19:13:32 |
| 运行耗时 | 257.6s |
| 订阅源总数 | 107 |
| 健康订阅源 | 102 |
| 原始节点 | 81101 |
| 去重后节点 | 23129 |
| TCP 可达 | 3000 |
| 真实可用 | 563 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23129 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 13.3 |
| geo | 1.3 |
| tcp | 35.1 |
| probe | 51.9 |
| real_test | 117.8 |
| generate | 38.2 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 46357 |
| vmess | 13218 |
| trojan | 10268 |
| shadowsocks | 9696 |
| hysteria2 | 1238 |
| http | 159 |
| shadowsocksr | 75 |
| socks | 66 |
| tuic | 14 |
| hysteria | 10 |

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
| 83.54 | hysteria2 | 239.6 | 638.5 | 22.23 | 0.0 | 10.0 | 14.17 | 18.24 | Au1rxx-base64 | 159.223.157.129 |
| 83.4 | hysteria2 | 249.9 | 662.0 | 21.99 | 0.0 | 10.0 | 14.17 | 18.24 | Au1rxx-base64 | 138.124.68.188 |
| 80.96 | http | 374.7 | 1041.7 | 19.1 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.41 |
| 80.57 | http | 391.7 | 1083.2 | 18.71 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.33 |
| 79.76 | hysteria2 | 246.0 | 669.9 | 22.08 | 0.0 | 6.27 | 14.17 | 18.24 | Au1rxx-base64 | usa1.spectrumproxy.shop |
| 79.51 | shadowsocks | 243.9 | 662.6 | 22.13 | 0.0 | 10.0 | 13.14 | 18.24 | Au1rxx-base64 | 37.19.198.244 |
| 79.47 | shadowsocks | 245.8 | 661.7 | 22.09 | 0.0 | 10.0 | 13.14 | 18.24 | Au1rxx-base64 | 37.19.198.160 |
| 79.36 | shadowsocks | 250.6 | 648.8 | 21.98 | 0.0 | 10.0 | 13.14 | 18.24 | Au1rxx-base64 | 37.19.198.236 |
| 79.29 | shadowsocks | 253.3 | 687.0 | 21.91 | 0.0 | 10.0 | 13.14 | 18.24 | Au1rxx-base64 | 37.19.198.243 |
| 78.98 | http | 244.4 | 651.2 | 22.12 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.11 |
| 78.95 | http | 245.7 | 661.1 | 22.09 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.28 |
| 78.79 | http | 252.6 | 671.4 | 21.93 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.4 |
| 77.52 | http | 523.7 | 1489.7 | 15.66 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.5 |
| 77.4 | http | 528.5 | 1494.5 | 15.54 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.8 |
| 77.27 | http | 534.3 | 1518.5 | 15.41 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.23 |
| 77.15 | http | 539.5 | 1523.9 | 15.29 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.25 |
| 76.94 | http | 548.6 | 1545.9 | 15.08 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.21 |
| 76.08 | http | 369.8 | 1031.5 | 19.22 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.34 |
| 75.98 | http | 373.9 | 1039.7 | 19.12 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.27 |
| 75.86 | shadowsocks | 280.5 | 636.6 | 21.29 | 0.0 | 10.0 | 13.14 | 18.24 | Au1rxx-base64 | 156.146.38.169 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.998 | 1.0 | 125 | 159 | prefer |
| Au1rxx-base64 | 0.933 | 0.875 | 375 | 1503 | prefer |
| Surfboard-tg-mixed | 0.822 | 0.747 | 95 | 6169 | prefer |
| mheidari-all | 0.792 | 0.72 | 50 | 16649 | prefer |
| DeltaKronecker-all | 0.3 | 0.4 | 5 | 5522 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5419 | observe |
| Epodonios-all | 0.255 | None | 0 | 6745 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7634 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5045 | observe |
| barry-far-vless | 0.255 | None | 0 | 5313 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5196 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| nscl5-all | 0.239 | None | 0 | 1607 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | ProxyError | - | 20 |
| 204 | TimeoutError | - | 15 |
| cn-block | TimeoutError | - | 12 |
| speed | TimeoutError | - | 11 |
| geo | ClientOSError | - | 9 |
| 204 | ClientOSError | - | 7 |
| geo | TimeoutError | - | 6 |
| speed | ClientOSError | - | 5 |
| cn-block | ProxyError | - | 2 |
| cn-block | ClientOSError | - | 1 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
