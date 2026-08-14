# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-14 07:44:35 |
| 运行耗时 | 314.2s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 81257 |
| 去重后节点 | 23189 |
| TCP 可达 | 3000 |
| 真实可用 | 847 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23189 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.6 |
| geo | 1.3 |
| tcp | 34.9 |
| probe | 66.9 |
| real_test | 172.5 |
| generate | 33.0 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 44342 |
| vmess | 13420 |
| trojan | 11669 |
| shadowsocks | 10068 |
| hysteria2 | 1444 |
| http | 149 |
| socks | 79 |
| shadowsocksr | 70 |
| tuic | 8 |
| hysteria | 7 |
| anytls | 1 |

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
| 84.1 | http | 239.0 | 623.7 | 22.24 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.5 |
| 84.07 | http | 240.5 | 625.2 | 22.21 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.21 |
| 84.06 | http | 240.8 | 639.9 | 22.2 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.39 |
| 84.06 | http | 240.9 | 641.6 | 22.2 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.8 |
| 83.96 | http | 245.3 | 644.6 | 22.1 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.23 |
| 83.96 | http | 245.3 | 639.1 | 22.1 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.33 |
| 83.92 | http | 247.2 | 668.9 | 22.06 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.28 |
| 83.87 | http | 249.1 | 670.2 | 22.01 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.9 |
| 83.85 | http | 250.2 | 669.2 | 21.99 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.41 |
| 83.78 | hysteria2 | 238.9 | 651.8 | 22.25 | 0.0 | 10.0 | 12.63 | 20.0 | Au1rxx-base64 | 159.223.157.129 |
| 83.66 | http | 258.1 | 665.0 | 21.8 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.15 |
| 83.63 | http | 259.6 | 679.7 | 21.77 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.11 |
| 83.61 | http | 260.5 | 667.4 | 21.75 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.34 |
| 83.58 | http | 261.7 | 664.9 | 21.72 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.27 |
| 83.57 | http | 262.2 | 676.9 | 21.71 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.25 |
| 83.53 | http | 264.0 | 684.2 | 21.67 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.4 |
| 83.48 | http | 266.0 | 687.5 | 21.62 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.10 |
| 83.48 | http | 266.1 | 703.3 | 21.62 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.19 |
| 83.42 | http | 268.7 | 714.2 | 21.56 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.31 |
| 83.21 | hysteria2 | 267.7 | 727.5 | 21.58 | 0.0 | 10.0 | 12.63 | 20.0 | Au1rxx-base64 | 138.124.68.188 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | 0.939 | 652 | 1671 | prefer |
| zhangkai | 0.999 | 1.0 | 128 | 159 | prefer |
| Surfboard-tg-mixed | 0.705 | 0.627 | 102 | 5896 | prefer |
| DeltaKronecker-all | 0.471 | 0.389 | 90 | 5969 | observe |
| mheidari-all | 0.432 | 0.429 | 14 | 16991 | observe |
| nscl5-all | 0.326 | 1.0 | 1 | 1768 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5157 | observe |
| Epodonios-all | 0.255 | None | 0 | 6568 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7698 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4633 | observe |
| barry-far-vless | 0.255 | None | 0 | 4969 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5332 | observe |
| Au1rxx-clash | 0.242 | None | 0 | 1671 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 57 |
| geo | ClientOSError | - | 21 |
| speed | ClientOSError | - | 20 |
| speed | TimeoutError | - | 16 |
| cn-block | TimeoutError | - | 11 |
| 204 | TimeoutError | - | 9 |
| 204 | ProxyError | - | 6 |
| cn-block | ProxyError | - | 2 |
| geo | ProxyError | - | 1 |
| 204 | ClientOSError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
