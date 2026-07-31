# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-31 03:34:53 |
| 运行耗时 | 298.0s |
| 订阅源总数 | 107 |
| 健康订阅源 | 102 |
| 原始节点 | 78323 |
| 去重后节点 | 23088 |
| TCP 可达 | 3000 |
| 真实可用 | 582 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23088 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.3 |
| geo | 1.4 |
| tcp | 33.6 |
| probe | 65.2 |
| real_test | 160.4 |
| generate | 33.2 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 45463 |
| vmess | 11410 |
| shadowsocks | 10269 |
| trojan | 10263 |
| hysteria2 | 599 |
| http | 127 |
| shadowsocksr | 75 |
| socks | 57 |
| anytls | 26 |
| tuic | 20 |
| hysteria | 14 |

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
| 84.98 | http | 198.2 | 509.5 | 23.19 | 0.0 | 10.0 | 14.87 | 19.92 | zhangkai | 138.199.35.196 |
| 83.17 | http | 189.8 | 489.3 | 23.38 | 0.0 | 10.0 | 14.87 | 19.92 | zhangkai | 138.199.35.217 |
| 83.17 | http | 189.9 | 489.0 | 23.38 | 0.0 | 10.0 | 14.87 | 19.92 | zhangkai | 138.199.35.205 |
| 83.06 | http | 194.8 | 500.0 | 23.27 | 0.0 | 10.0 | 14.87 | 19.92 | zhangkai | 138.199.35.206 |
| 83.06 | http | 194.9 | 491.2 | 23.27 | 0.0 | 10.0 | 14.87 | 19.92 | zhangkai | 138.199.35.214 |
| 83.05 | http | 195.4 | 501.7 | 23.26 | 0.0 | 10.0 | 14.87 | 19.92 | zhangkai | 138.199.35.218 |
| 83.04 | http | 195.7 | 499.7 | 23.25 | 0.0 | 10.0 | 14.87 | 19.92 | zhangkai | 138.199.35.202 |
| 83.03 | http | 196.2 | 502.2 | 23.24 | 0.0 | 10.0 | 14.87 | 19.92 | zhangkai | 138.199.35.209 |
| 83.01 | http | 196.9 | 512.1 | 23.22 | 0.0 | 10.0 | 14.87 | 19.92 | zhangkai | 138.199.35.212 |
| 83.01 | http | 197.0 | 508.6 | 23.22 | 0.0 | 10.0 | 14.87 | 19.92 | zhangkai | 138.199.35.199 |
| 83.0 | http | 197.1 | 505.3 | 23.21 | 0.0 | 10.0 | 14.87 | 19.92 | zhangkai | 138.199.35.215 |
| 82.98 | http | 198.1 | 504.8 | 23.19 | 0.0 | 10.0 | 14.87 | 19.92 | zhangkai | 138.199.35.210 |
| 82.95 | http | 199.7 | 527.5 | 23.16 | 0.0 | 10.0 | 14.87 | 19.92 | zhangkai | 138.199.35.204 |
| 82.92 | http | 200.9 | 521.6 | 23.13 | 0.0 | 10.0 | 14.87 | 19.92 | zhangkai | 138.199.35.208 |
| 82.9 | http | 201.5 | 512.2 | 23.11 | 0.0 | 10.0 | 14.87 | 19.92 | zhangkai | 138.199.35.198 |
| 82.88 | http | 202.4 | 516.4 | 23.09 | 0.0 | 10.0 | 14.87 | 19.92 | zhangkai | 138.199.35.213 |
| 82.88 | http | 202.5 | 507.9 | 23.09 | 0.0 | 10.0 | 14.87 | 19.92 | zhangkai | 138.199.35.200 |
| 82.86 | http | 203.3 | 525.1 | 23.07 | 0.0 | 10.0 | 14.87 | 19.92 | zhangkai | 138.199.35.207 |
| 82.83 | http | 204.9 | 523.7 | 23.04 | 0.0 | 10.0 | 14.87 | 19.92 | zhangkai | 138.199.35.216 |
| 82.1 | http | 193.1 | 494.1 | 23.31 | 0.0 | 10.0 | 14.87 | 19.92 | zhangkai | 138.199.35.197 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.996 | 1.0 | 113 | 129 | prefer |
| Au1rxx-base64 | 0.968 | 0.921 | 240 | 1272 | prefer |
| Surfboard-tg-mixed | 0.753 | 0.676 | 148 | 5223 | prefer |
| mheidari-all | 0.418 | 0.5 | 10 | 16264 | observe |
| ninja-vless | 0.381 | 0.385 | 13 | 1791 | observe |
| DeltaKronecker-all | 0.365 | 0.284 | 483 | 5759 | observe |
| tg-OutlineReleasedKey | 0.257 | 1.0 | 1 | 43 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5342 | observe |
| Epodonios-all | 0.255 | None | 0 | 6141 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7041 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4144 | observe |
| barry-far-vless | 0.255 | None | 0 | 4647 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5047 | observe |
| xiaoji235-airport-v2ray-all | 0.249 | None | 0 | 1861 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 250 |
| speed | ClientOSError | - | 51 |
| geo | ClientOSError | - | 50 |
| speed | TimeoutError | - | 40 |
| 204 | TimeoutError | - | 12 |
| cn-block | TimeoutError | - | 12 |
| 204 | ProxyError | - | 5 |
| cn-block | ClientOSError | - | 4 |
| geo | ProxyError | - | 1 |
| cn-block | ProxyError | - | 1 |
| 204 | ClientOSError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
