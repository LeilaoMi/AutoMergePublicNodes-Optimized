# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-13 02:29:18 |
| 运行耗时 | 291.6s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 79753 |
| 去重后节点 | 22383 |
| TCP 可达 | 3000 |
| 真实可用 | 669 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22383 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.1 |
| geo | 1.4 |
| tcp | 32.6 |
| probe | 60.4 |
| real_test | 167.7 |
| generate | 23.5 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 45223 |
| vmess | 13438 |
| trojan | 9819 |
| shadowsocks | 9740 |
| hysteria2 | 1201 |
| http | 160 |
| socks | 77 |
| shadowsocksr | 74 |
| tuic | 11 |
| hysteria | 7 |
| anytls | 3 |

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
| 84.21 | http | 234.6 | 630.7 | 22.35 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.31 |
| 84.18 | http | 235.8 | 636.8 | 22.32 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.25 |
| 84.1 | hysteria2 | 234.4 | 631.1 | 22.35 | 0.0 | 10.0 | 14.29 | 18.56 | Au1rxx-base64 | 159.223.157.129 |
| 84.06 | http | 241.0 | 643.0 | 22.2 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.39 |
| 84.02 | hysteria2 | 242.2 | 669.8 | 22.17 | 0.0 | 10.0 | 14.29 | 18.56 | Au1rxx-base64 | 138.124.68.188 |
| 83.94 | http | 246.3 | 669.7 | 22.08 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.28 |
| 83.9 | http | 248.0 | 661.3 | 22.04 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.34 |
| 83.87 | http | 249.0 | 666.4 | 22.01 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.5 |
| 83.86 | http | 249.4 | 672.1 | 22.0 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.41 |
| 83.83 | http | 250.8 | 681.0 | 21.97 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.21 |
| 83.79 | http | 252.7 | 685.3 | 21.93 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.19 |
| 83.76 | http | 254.0 | 675.6 | 21.9 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.11 |
| 83.67 | http | 257.9 | 683.8 | 21.81 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.33 |
| 83.65 | http | 239.0 | 636.0 | 22.25 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.9 |
| 83.64 | http | 259.3 | 701.1 | 21.78 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.10 |
| 83.63 | http | 259.6 | 706.8 | 21.77 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.15 |
| 83.61 | http | 260.4 | 698.1 | 21.75 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.4 |
| 83.6 | http | 260.8 | 712.7 | 21.74 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.27 |
| 83.54 | http | 263.5 | 693.0 | 21.68 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.23 |
| 83.46 | http | 267.1 | 727.6 | 21.6 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.8 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.999 | 1.0 | 128 | 159 | prefer |
| Au1rxx-base64 | 0.934 | 0.876 | 403 | 1489 | prefer |
| Surfboard-tg-mixed | 0.71 | 0.632 | 163 | 5894 | prefer |
| mheidari-all | 0.432 | 0.429 | 14 | 16809 | observe |
| DeltaKronecker-all | 0.262 | 0.18 | 438 | 4975 | observe |
| Epodonios-all | 0.255 | None | 0 | 6571 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7660 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4734 | observe |
| barry-far-vless | 0.255 | None | 0 | 5066 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5209 | observe |
| nscl5-all | 0.241 | None | 0 | 1654 | observe |
| Au1rxx-clash | 0.235 | None | 0 | 1489 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |
| 10ium-HighSpeed | 0.209 | None | 0 | 839 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 237 |
| geo | ClientOSError | - | 93 |
| speed | TimeoutError | - | 71 |
| speed | ClientOSError | - | 42 |
| cn-block | TimeoutError | - | 15 |
| 204 | TimeoutError | - | 8 |
| cn-block | ClientOSError | - | 6 |
| 204 | ProxyError | - | 5 |
| 204 | ClientOSError | - | 3 |
| cn-block | ProxyError | - | 2 |
| speed | ProxyError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
