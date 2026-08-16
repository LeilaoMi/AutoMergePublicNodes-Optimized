# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-16 06:54:35 |
| 运行耗时 | 358.3s |
| 订阅源总数 | 107 |
| 健康订阅源 | 99 |
| 原始节点 | 78586 |
| 去重后节点 | 21819 |
| TCP 可达 | 3000 |
| 真实可用 | 1129 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 21819 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.3 |
| geo | 0.7 |
| tcp | 32.6 |
| probe | 76.5 |
| real_test | 215.3 |
| generate | 27.0 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 43153 |
| trojan | 13543 |
| vmess | 10729 |
| shadowsocks | 9803 |
| hysteria2 | 1023 |
| http | 170 |
| shadowsocksr | 74 |
| socks | 72 |
| tuic | 10 |
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
| 84.2 | http | 234.9 | 627.0 | 22.34 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.8 |
| 84.17 | http | 236.3 | 626.7 | 22.31 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.21 |
| 84.08 | http | 240.0 | 642.0 | 22.22 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.28 |
| 83.91 | http | 247.2 | 671.6 | 22.05 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.10 |
| 83.85 | http | 249.8 | 670.1 | 21.99 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.41 |
| 83.82 | http | 251.4 | 665.1 | 21.96 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.5 |
| 83.82 | http | 251.5 | 672.7 | 21.96 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.15 |
| 83.78 | http | 253.0 | 691.3 | 21.92 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.27 |
| 83.76 | http | 253.9 | 671.7 | 21.9 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.19 |
| 83.74 | http | 255.0 | 672.4 | 21.88 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.9 |
| 83.69 | http | 256.8 | 689.5 | 21.83 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.25 |
| 83.68 | http | 257.5 | 682.9 | 21.82 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.39 |
| 83.67 | http | 257.7 | 695.7 | 21.81 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.31 |
| 83.62 | http | 259.9 | 696.2 | 21.76 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.34 |
| 83.55 | http | 262.8 | 714.7 | 21.69 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.11 |
| 83.55 | http | 263.1 | 713.5 | 21.69 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.23 |
| 83.37 | http | 271.0 | 725.4 | 21.51 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.4 |
| 82.27 | http | 318.4 | 872.9 | 20.41 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.33 |
| 82.23 | shadowsocks | 235.5 | 657.5 | 22.33 | 0.0 | 9.6 | 14.3 | 20.0 | Au1rxx-base64 | 37.19.198.243 |
| 81.04 | hysteria2 | 280.2 | 574.5 | 21.29 | 0.0 | 9.35 | 14.0 | 20.0 | Au1rxx-base64 | 150.241.102.127 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | 0.966 | 799 | 1997 | prefer |
| zhangkai | 0.999 | 1.0 | 127 | 159 | prefer |
| Surfboard-tg-mixed | 0.754 | 0.675 | 191 | 5641 | prefer |
| mheidari-all | 0.691 | 0.613 | 142 | 16464 | observe |
| nscl5-all | 0.349 | 0.667 | 3 | 2601 | observe |
| 10ium-ScrapeCategorize-Vless | 0.335 | 1.0 | 1 | 4990 | observe |
| DeltaKronecker-all | 0.315 | 0.224 | 49 | 5092 | observe |
| Au1rxx-clash | 0.255 | None | 0 | 1997 | observe |
| Epodonios-all | 0.255 | None | 0 | 6328 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3986 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7355 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4360 | observe |
| barry-far-vless | 0.255 | None | 0 | 4736 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 3950 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 60 |
| speed | TimeoutError | - | 45 |
| geo | ClientOSError | - | 25 |
| speed | ClientOSError | - | 16 |
| 204 | TimeoutError | - | 16 |
| cn-block | ClientOSError | - | 8 |
| cn-block | TimeoutError | - | 6 |
| 204 | ClientOSError | - | 4 |
| 204 | ProxyError | - | 4 |
| cn-block | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
