# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-19 06:59:21 |
| 运行耗时 | 403.4s |
| 订阅源总数 | 107 |
| 健康订阅源 | 100 |
| 原始节点 | 82903 |
| 去重后节点 | 22465 |
| TCP 可达 | 3000 |
| 真实可用 | 1336 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22465 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.0 |
| geo | 0.8 |
| tcp | 35.0 |
| probe | 84.3 |
| real_test | 249.3 |
| generate | 28.0 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 44348 |
| trojan | 18415 |
| shadowsocks | 10123 |
| vmess | 8472 |
| hysteria2 | 1129 |
| http | 178 |
| socks | 117 |
| shadowsocksr | 97 |
| tuic | 10 |
| hysteria | 7 |
| anytls | 7 |

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
| 83.86 | http | 249.8 | 648.9 | 22.0 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.4 |
| 83.82 | http | 251.5 | 637.6 | 21.96 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.27 |
| 83.8 | http | 252.1 | 651.5 | 21.94 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.23 |
| 83.8 | http | 252.3 | 648.8 | 21.94 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.15 |
| 83.66 | http | 258.4 | 651.5 | 21.8 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.8 |
| 83.64 | http | 259.3 | 671.6 | 21.78 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.28 |
| 83.56 | http | 262.7 | 683.4 | 21.7 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.25 |
| 83.54 | http | 263.3 | 684.1 | 21.68 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.10 |
| 83.51 | http | 264.5 | 688.9 | 21.65 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.31 |
| 83.51 | http | 264.5 | 688.0 | 21.65 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.33 |
| 83.5 | http | 265.0 | 694.5 | 21.64 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.19 |
| 83.5 | http | 265.2 | 694.6 | 21.64 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.34 |
| 83.48 | http | 266.1 | 691.4 | 21.62 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.21 |
| 83.46 | http | 267.1 | 699.3 | 21.6 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.5 |
| 83.44 | http | 267.6 | 695.8 | 21.58 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.11 |
| 83.43 | http | 268.2 | 686.2 | 21.57 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.9 |
| 83.42 | http | 268.6 | 695.0 | 21.56 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.39 |
| 83.4 | http | 269.4 | 697.5 | 21.54 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.41 |
| 82.8 | shadowsocks | 234.2 | 623.2 | 22.36 | 0.0 | 10.0 | 14.44 | 20.0 | mheidari-all | 37.19.198.160 |
| 82.71 | shadowsocks | 237.7 | 632.9 | 22.27 | 0.0 | 10.0 | 14.44 | 20.0 | mheidari-all | 37.19.198.243 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | 0.984 | 803 | 1924 | prefer |
| zhangkai | 0.999 | 1.0 | 126 | 159 | prefer |
| mheidari-all | 0.887 | 0.809 | 329 | 16809 | prefer |
| Surfboard-tg-mixed | 0.867 | 0.79 | 181 | 6315 | prefer |
| nscl5-all | 0.4 | 0.75 | 4 | 3330 | observe |
| DeltaKronecker-all | 0.323 | 0.229 | 35 | 6390 | observe |
| Epodonios-all | 0.255 | None | 0 | 7030 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3996 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7119 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4850 | observe |
| barry-far-vless | 0.255 | None | 0 | 5173 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 3995 | observe |
| Au1rxx-clash | 0.252 | None | 0 | 1924 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 45 |
| speed | TimeoutError | - | 27 |
| geo | ClientOSError | - | 20 |
| 204 | TimeoutError | - | 14 |
| speed | ClientOSError | - | 13 |
| cn-block | TimeoutError | - | 10 |
| cn-block | ClientOSError | - | 7 |
| 204 | ProxyError | - | 5 |
| 204 | ClientOSError | - | 3 |
| cn-block | ProxyError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
