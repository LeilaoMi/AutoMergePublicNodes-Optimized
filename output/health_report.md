# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-16 01:47:53 |
| 运行耗时 | 387.1s |
| 订阅源总数 | 107 |
| 健康订阅源 | 99 |
| 原始节点 | 79337 |
| 去重后节点 | 22383 |
| TCP 可达 | 3000 |
| 真实可用 | 1147 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22383 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.7 |
| geo | 0.5 |
| tcp | 33.2 |
| probe | 74.7 |
| real_test | 238.1 |
| generate | 34.9 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 43312 |
| trojan | 14077 |
| vmess | 10719 |
| shadowsocks | 9827 |
| hysteria2 | 1032 |
| http | 182 |
| socks | 89 |
| shadowsocksr | 80 |
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
| 84.14 | http | 237.7 | 642.6 | 22.28 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.10 |
| 84.01 | vless | 243.7 | 663.3 | 22.14 | 0.0 | 10.0 | 11.87 | 20.0 | Au1rxx-base64 | 137.184.218.169 |
| 83.84 | http | 250.3 | 677.1 | 21.98 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.19 |
| 83.83 | http | 250.8 | 675.3 | 21.97 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.39 |
| 83.83 | http | 250.9 | 679.3 | 21.97 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.25 |
| 83.81 | http | 251.9 | 682.2 | 21.95 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.41 |
| 83.8 | http | 252.0 | 674.7 | 21.94 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.11 |
| 83.8 | http | 252.1 | 674.5 | 21.94 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.4 |
| 83.74 | http | 254.9 | 692.9 | 21.88 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.34 |
| 83.74 | http | 254.9 | 690.0 | 21.88 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.15 |
| 83.71 | http | 256.2 | 682.2 | 21.85 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.31 |
| 83.7 | vless | 242.3 | 652.4 | 22.17 | 0.0 | 9.66 | 11.87 | 20.0 | Au1rxx-base64 | 204.48.20.223 |
| 83.65 | http | 258.5 | 702.3 | 21.79 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.33 |
| 83.57 | http | 262.0 | 711.6 | 21.71 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.8 |
| 83.55 | vless | 263.4 | 691.4 | 21.68 | 0.0 | 10.0 | 11.87 | 20.0 | Au1rxx-base64 | 169.40.42.133 |
| 83.51 | hysteria2 | 249.1 | 680.1 | 22.01 | 0.0 | 10.0 | 12.5 | 20.0 | Au1rxx-base64 | 138.124.68.188 |
| 83.49 | hysteria2 | 245.8 | 675.0 | 22.09 | 0.0 | 10.0 | 12.5 | 20.0 | Au1rxx-base64 | 159.223.157.129 |
| 83.49 | http | 265.8 | 719.4 | 21.63 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.9 |
| 83.48 | http | 265.8 | 726.3 | 21.62 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.21 |
| 83.45 | http | 267.5 | 715.8 | 21.59 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.28 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | 0.978 | 787 | 1995 | prefer |
| zhangkai | 0.999 | 1.0 | 127 | 159 | prefer |
| Surfboard-tg-mixed | 0.802 | 0.724 | 156 | 5707 | prefer |
| mheidari-all | 0.568 | 0.488 | 252 | 16315 | observe |
| nscl5-all | 0.391 | 1.0 | 2 | 2601 | observe |
| tg-oneclickvpnkeys | 0.261 | 1.0 | 1 | 145 | observe |
| Au1rxx-clash | 0.255 | None | 0 | 1995 | observe |
| Epodonios-all | 0.255 | None | 0 | 6340 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3984 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7329 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4387 | observe |
| barry-far-vless | 0.255 | None | 0 | 4782 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 3935 | observe |
| DeltaKronecker-all | 0.249 | 0.159 | 69 | 5773 | downweight |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 94 |
| speed | TimeoutError | - | 64 |
| cn-block | TimeoutError | - | 30 |
| geo | ClientOSError | - | 28 |
| speed | ClientOSError | - | 14 |
| 204 | TimeoutError | - | 9 |
| 204 | ClientOSError | - | 4 |
| cn-block | ClientOSError | - | 3 |
| 204 | ProxyError | - | 2 |
| cn-block | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
