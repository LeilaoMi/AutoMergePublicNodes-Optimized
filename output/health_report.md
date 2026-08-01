# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-01 13:44:27 |
| 运行耗时 | 292.2s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 78943 |
| 去重后节点 | 23426 |
| TCP 可达 | 3000 |
| 真实可用 | 626 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23426 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.9 |
| geo | 1.4 |
| tcp | 35.1 |
| probe | 59.5 |
| real_test | 148.7 |
| generate | 40.5 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 47480 |
| vmess | 12385 |
| shadowsocks | 10145 |
| trojan | 7979 |
| hysteria2 | 609 |
| http | 157 |
| shadowsocksr | 74 |
| socks | 66 |
| anytls | 26 |
| hysteria | 14 |
| tuic | 8 |

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
| 85.04 | http | 200.8 | 504.1 | 23.13 | 0.0 | 10.0 | 14.91 | 20.0 | zhangkai | 138.199.35.220 |
| 85.04 | http | 200.9 | 504.4 | 23.13 | 0.0 | 10.0 | 14.91 | 20.0 | zhangkai | 138.199.35.199 |
| 85.03 | http | 201.0 | 508.9 | 23.12 | 0.0 | 10.0 | 14.91 | 20.0 | zhangkai | 138.199.35.217 |
| 85.01 | http | 202.1 | 506.1 | 23.1 | 0.0 | 10.0 | 14.91 | 20.0 | zhangkai | 138.199.35.208 |
| 85.01 | http | 202.2 | 504.5 | 23.1 | 0.0 | 10.0 | 14.91 | 20.0 | zhangkai | 138.199.35.213 |
| 85.0 | http | 202.4 | 509.2 | 23.09 | 0.0 | 10.0 | 14.91 | 20.0 | zhangkai | 138.199.35.218 |
| 84.99 | http | 202.9 | 507.6 | 23.08 | 0.0 | 10.0 | 14.91 | 20.0 | zhangkai | 138.199.35.215 |
| 84.94 | http | 205.1 | 519.1 | 23.03 | 0.0 | 10.0 | 14.91 | 20.0 | zhangkai | 138.199.35.205 |
| 84.94 | http | 205.2 | 517.6 | 23.03 | 0.0 | 10.0 | 14.91 | 20.0 | zhangkai | 138.199.35.214 |
| 84.9 | http | 206.7 | 518.3 | 22.99 | 0.0 | 10.0 | 14.91 | 20.0 | zhangkai | 138.199.35.197 |
| 84.9 | http | 206.7 | 522.7 | 22.99 | 0.0 | 10.0 | 14.91 | 20.0 | zhangkai | 138.199.35.216 |
| 84.86 | http | 208.7 | 514.9 | 22.95 | 0.0 | 10.0 | 14.91 | 20.0 | zhangkai | 138.199.35.207 |
| 84.85 | http | 209.2 | 526.9 | 22.94 | 0.0 | 10.0 | 14.91 | 20.0 | zhangkai | 138.199.35.198 |
| 84.82 | http | 210.5 | 521.2 | 22.91 | 0.0 | 10.0 | 14.91 | 20.0 | zhangkai | 138.199.35.212 |
| 84.79 | http | 211.5 | 524.2 | 22.88 | 0.0 | 10.0 | 14.91 | 20.0 | zhangkai | 138.199.35.206 |
| 84.77 | http | 212.2 | 529.5 | 22.86 | 0.0 | 10.0 | 14.91 | 20.0 | zhangkai | 138.199.35.210 |
| 84.07 | http | 199.4 | 505.7 | 23.16 | 0.0 | 10.0 | 14.91 | 20.0 | zhangkai | 138.199.35.195 |
| 83.98 | http | 203.2 | 513.7 | 23.07 | 0.0 | 10.0 | 14.91 | 20.0 | zhangkai | 138.199.35.211 |
| 83.85 | http | 252.4 | 666.0 | 21.94 | 0.0 | 10.0 | 14.91 | 20.0 | zhangkai | 138.199.35.196 |
| 83.83 | http | 253.3 | 668.4 | 21.92 | 0.0 | 10.0 | 14.91 | 20.0 | zhangkai | 138.199.35.209 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.994 | 0.993 | 148 | 194 | prefer |
| Au1rxx-base64 | 0.828 | 0.761 | 498 | 1689 | prefer |
| Surfboard-tg-mixed | 0.727 | 0.65 | 100 | 5351 | prefer |
| DeltaKronecker-all | 0.712 | 0.639 | 36 | 5502 | prefer |
| mheidari-all | 0.515 | 0.636 | 11 | 16460 | observe |
| Epodonios-all | 0.335 | 1.0 | 1 | 5964 | observe |
| SoliSpirit-all | 0.335 | 1.0 | 1 | 6948 | observe |
| xiaoji235-airport-v2ray-all | 0.329 | 1.0 | 1 | 1861 | observe |
| roosterkid-openproxylist-v2ray | 0.261 | 1.0 | 1 | 150 | observe |
| tg-OutlineReleasedKey | 0.257 | 1.0 | 1 | 53 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5391 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4224 | observe |
| barry-far-vless | 0.255 | None | 0 | 4602 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5039 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 46 |
| speed | TimeoutError | - | 32 |
| 204 | TimeoutError | - | 20 |
| 204 | ProxyError | - | 19 |
| speed | ClientOSError | - | 15 |
| geo | ClientOSError | - | 14 |
| 204 | ClientOSError | - | 13 |
| cn-block | TimeoutError | - | 9 |
| cn-block | ProxyError | - | 2 |
| cn-block | ClientOSError | - | 2 |
| speed | ClientPayloadError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
