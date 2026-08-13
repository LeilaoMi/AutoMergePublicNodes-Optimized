# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-13 13:28:27 |
| 运行耗时 | 316.2s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 79794 |
| 去重后节点 | 22452 |
| TCP 可达 | 3000 |
| 真实可用 | 786 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22452 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 14.7 |
| geo | 0.9 |
| tcp | 32.9 |
| probe | 64.7 |
| real_test | 166.1 |
| generate | 37.0 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 43802 |
| vmess | 13396 |
| trojan | 11264 |
| shadowsocks | 9865 |
| hysteria2 | 1141 |
| http | 160 |
| socks | 77 |
| shadowsocksr | 72 |
| tuic | 8 |
| hysteria | 7 |
| anytls | 2 |

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
| 84.03 | http | 242.1 | 648.2 | 22.17 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.8 |
| 83.95 | http | 245.6 | 660.8 | 22.09 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.10 |
| 83.92 | http | 247.0 | 653.2 | 22.06 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.21 |
| 83.9 | http | 247.9 | 660.5 | 22.04 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.31 |
| 83.9 | http | 248.0 | 663.4 | 22.04 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.5 |
| 83.8 | http | 252.2 | 673.7 | 21.94 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.34 |
| 83.78 | http | 253.1 | 683.6 | 21.92 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.4 |
| 83.78 | http | 253.1 | 677.9 | 21.92 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.15 |
| 83.74 | http | 254.9 | 680.0 | 21.88 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.19 |
| 83.67 | http | 258.0 | 692.1 | 21.81 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.23 |
| 83.62 | http | 259.8 | 692.5 | 21.76 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.9 |
| 83.61 | http | 260.6 | 689.3 | 21.75 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.41 |
| 83.56 | http | 262.4 | 691.0 | 21.7 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.39 |
| 82.56 | http | 305.8 | 831.9 | 20.7 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.33 |
| 82.48 | http | 309.1 | 831.2 | 20.62 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.25 |
| 82.48 | http | 309.4 | 847.9 | 20.62 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.11 |
| 82.37 | http | 314.2 | 856.5 | 20.51 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.27 |
| 82.16 | http | 322.9 | 873.3 | 20.3 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.28 |
| 81.93 | hysteria2 | 323.1 | 890.8 | 20.3 | 0.0 | 10.0 | 12.63 | 20.0 | Au1rxx-base64 | 138.124.68.188 |
| 81.64 | shadowsocks | 234.1 | 634.1 | 22.36 | 0.0 | 10.0 | 13.28 | 20.0 | Au1rxx-base64 | 37.19.198.236 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | 0.961 | 534 | 1591 | prefer |
| zhangkai | 0.999 | 1.0 | 128 | 159 | prefer |
| Surfboard-tg-mixed | 0.828 | 0.752 | 113 | 5967 | prefer |
| mheidari-all | 0.774 | 0.7 | 70 | 17032 | prefer |
| DeltaKronecker-all | 0.503 | 0.417 | 24 | 4878 | observe |
| roosterkid-openproxylist-v2ray | 0.261 | 1.0 | 1 | 150 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5203 | observe |
| Epodonios-all | 0.255 | None | 0 | 6610 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7410 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4695 | observe |
| barry-far-vless | 0.255 | None | 0 | 5031 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5197 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| nscl5-all | 0.241 | None | 0 | 1654 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| cn-block | TimeoutError | - | 15 |
| geo | ClientOSError | - | 14 |
| geo | TimeoutError | - | 14 |
| 204 | TimeoutError | - | 11 |
| 204 | ProxyError | - | 9 |
| speed | ClientOSError | - | 8 |
| speed | TimeoutError | - | 6 |
| 204 | ClientOSError | - | 3 |
| cn-block | ClientOSError | - | 3 |
| cn-block | ProxyError | - | 2 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
