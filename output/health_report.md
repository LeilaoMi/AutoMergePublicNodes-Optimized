# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-03 10:02:03 |
| 运行耗时 | 347.9s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 83372 |
| 去重后节点 | 24502 |
| TCP 可达 | 3000 |
| 真实可用 | 676 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 24502 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.4 |
| geo | 1.4 |
| tcp | 37.2 |
| probe | 67.2 |
| real_test | 194.3 |
| generate | 42.4 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 50617 |
| vmess | 12727 |
| shadowsocks | 10517 |
| trojan | 8428 |
| hysteria2 | 735 |
| http | 176 |
| shadowsocksr | 77 |
| socks | 71 |
| hysteria | 12 |
| anytls | 7 |
| tuic | 5 |

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
| 85.24 | http | 191.9 | 485.5 | 23.34 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.214 |
| 85.2 | http | 193.3 | 492.4 | 23.3 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.212 |
| 85.2 | http | 193.5 | 492.9 | 23.3 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.205 |
| 85.19 | http | 193.7 | 497.8 | 23.29 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.197 |
| 85.13 | http | 196.3 | 491.3 | 23.23 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.204 |
| 85.13 | http | 196.4 | 494.1 | 23.23 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.216 |
| 85.12 | http | 197.0 | 494.3 | 23.22 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.217 |
| 85.11 | http | 197.1 | 498.3 | 23.21 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.215 |
| 85.09 | http | 198.0 | 495.7 | 23.19 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.206 |
| 85.09 | http | 198.4 | 494.2 | 23.19 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.210 |
| 85.08 | http | 198.8 | 494.7 | 23.18 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.218 |
| 85.05 | http | 199.9 | 501.7 | 23.15 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.220 |
| 85.01 | http | 201.7 | 507.4 | 23.11 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.195 |
| 84.98 | http | 203.0 | 517.3 | 23.08 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.209 |
| 84.87 | http | 207.6 | 513.6 | 22.97 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.213 |
| 84.77 | http | 211.9 | 499.5 | 22.87 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.211 |
| 84.55 | http | 221.7 | 568.8 | 22.65 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.200 |
| 84.34 | http | 230.7 | 601.1 | 22.44 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.207 |
| 84.33 | http | 231.2 | 604.3 | 22.43 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.208 |
| 84.16 | http | 238.4 | 631.0 | 22.26 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.202 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 1.0 | 1.0 | 144 | 344 | prefer |
| Au1rxx-base64 | 0.81 | 0.746 | 555 | 1629 | prefer |
| Surfboard-tg-mixed | 0.388 | 0.292 | 24 | 5244 | observe |
| DeltaKronecker-all | 0.379 | 0.298 | 359 | 6205 | observe |
| xiaoji235-airport-v2ray-all | 0.335 | 1.0 | 1 | 3833 | observe |
| tg-OutlineReleasedKey | 0.257 | 1.0 | 1 | 54 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5285 | observe |
| Epodonios-all | 0.255 | None | 0 | 5831 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6567 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4132 | observe |
| barry-far-vless | 0.255 | None | 0 | 4492 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5196 | observe |
| mheidari-all | 0.249 | 0.2 | 10 | 18806 | downweight |
| Au1rxx-clash | 0.24 | None | 0 | 1629 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 157 |
| 204 | ProxyError | - | 83 |
| speed | TimeoutError | - | 48 |
| speed | ClientOSError | - | 32 |
| 204 | TimeoutError | - | 28 |
| cn-block | TimeoutError | - | 27 |
| geo | ClientOSError | - | 25 |
| cn-block | ProxyError | - | 9 |
| 204 | ClientOSError | - | 5 |
| geo | ProxyError | - | 4 |
| speed | ProxyError | - | 3 |
| cn-block | ClientOSError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
