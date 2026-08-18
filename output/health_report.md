# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-18 13:02:21 |
| 运行耗时 | 399.4s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 91956 |
| 去重后节点 | 24183 |
| TCP 可达 | 3000 |
| 真实可用 | 1245 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 24183 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.3 |
| geo | 1.4 |
| tcp | 38.2 |
| probe | 71.6 |
| real_test | 245.8 |
| generate | 36.2 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 52693 |
| trojan | 16401 |
| shadowsocks | 10453 |
| vmess | 9580 |
| hysteria2 | 2296 |
| http | 183 |
| socks | 144 |
| shadowsocksr | 131 |
| anytls | 43 |
| tuic | 19 |
| hysteria | 13 |

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
| 83.81 | http | 251.9 | 649.4 | 21.95 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.4 |
| 83.74 | http | 254.7 | 659.4 | 21.88 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.8 |
| 83.69 | http | 257.0 | 657.4 | 21.83 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.25 |
| 83.68 | http | 257.6 | 645.8 | 21.82 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.39 |
| 83.6 | http | 260.8 | 658.8 | 21.74 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.31 |
| 83.57 | http | 262.2 | 675.4 | 21.71 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.23 |
| 83.57 | http | 262.3 | 662.9 | 21.71 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.21 |
| 83.55 | http | 262.9 | 683.0 | 21.69 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.15 |
| 83.54 | http | 263.5 | 674.0 | 21.68 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.11 |
| 83.53 | http | 264.1 | 689.6 | 21.67 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.41 |
| 83.48 | http | 266.1 | 680.5 | 21.62 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.33 |
| 83.45 | http | 267.4 | 681.6 | 21.59 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.34 |
| 83.41 | http | 269.0 | 686.6 | 21.55 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.5 |
| 83.39 | http | 269.8 | 681.1 | 21.53 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.10 |
| 83.38 | http | 270.4 | 688.4 | 21.52 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.27 |
| 83.37 | http | 270.8 | 687.8 | 21.51 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.9 |
| 80.4 | shadowsocks | 236.8 | 624.2 | 22.3 | 0.0 | 10.0 | 13.42 | 18.68 | Surfboard-tg-mixed | 37.19.198.236 |
| 79.9 | shadowsocks | 258.2 | 672.9 | 21.8 | 0.0 | 10.0 | 13.42 | 18.68 | Surfboard-tg-mixed | 37.19.198.160 |
| 79.61 | http | 270.0 | 689.8 | 21.53 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.19 |
| 78.99 | http | 253.3 | 652.6 | 21.92 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.28 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | 0.931 | 563 | 1759 | prefer |
| mheidari-all | 1.0 | 0.96 | 447 | 21086 | prefer |
| zhangkai | 0.999 | 1.0 | 127 | 159 | prefer |
| Surfboard-tg-mixed | 0.86 | 0.783 | 207 | 6253 | prefer |
| nscl5-all | 0.335 | 1.0 | 1 | 2992 | observe |
| DeltaKronecker-all | 0.272 | 0.286 | 7 | 5725 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5068 | observe |
| Epodonios-all | 0.255 | None | 0 | 6795 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3984 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6898 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4907 | observe |
| barry-far-vless | 0.255 | None | 0 | 5206 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4045 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6329 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | TimeoutError | - | 23 |
| cn-block | TimeoutError | - | 21 |
| geo | TimeoutError | - | 18 |
| geo | ClientOSError | - | 13 |
| speed | TimeoutError | - | 9 |
| speed | ClientOSError | - | 8 |
| 204 | ProxyError | - | 7 |
| 204 | ClientOSError | - | 4 |
| cn-block | ClientOSError | - | 4 |
| cn-block | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
