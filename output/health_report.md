# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-03 03:36:42 |
| 运行耗时 | 354.5s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 81081 |
| 去重后节点 | 22634 |
| TCP 可达 | 3000 |
| 真实可用 | 876 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22634 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.0 |
| geo | 1.5 |
| tcp | 34.9 |
| probe | 64.0 |
| real_test | 200.2 |
| generate | 46.9 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 49583 |
| vmess | 12591 |
| shadowsocks | 10281 |
| trojan | 7554 |
| hysteria2 | 727 |
| http | 176 |
| shadowsocksr | 76 |
| socks | 69 |
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
| 84.99 | http | 202.5 | 504.2 | 23.09 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.204 |
| 80.27 | http | 406.4 | 1133.4 | 18.37 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.197 |
| 80.16 | http | 411.2 | 1148.6 | 18.26 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.208 |
| 80.1 | http | 413.7 | 1150.5 | 18.2 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.206 |
| 80.1 | http | 414.0 | 1150.4 | 18.2 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.220 |
| 80.03 | http | 416.7 | 1144.4 | 18.13 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.214 |
| 80.03 | http | 416.7 | 1148.4 | 18.13 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.215 |
| 79.98 | http | 418.9 | 1159.0 | 18.08 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.209 |
| 79.98 | http | 419.0 | 1155.4 | 18.08 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.217 |
| 79.95 | http | 420.3 | 1148.6 | 18.05 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.216 |
| 79.95 | http | 420.4 | 1154.2 | 18.05 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.211 |
| 79.94 | http | 420.9 | 1163.2 | 18.04 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.205 |
| 79.91 | http | 422.1 | 1158.4 | 18.01 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.195 |
| 79.88 | http | 423.4 | 1165.6 | 17.98 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.213 |
| 79.86 | http | 424.3 | 1169.3 | 17.96 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.212 |
| 79.53 | http | 438.6 | 1185.9 | 17.63 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.218 |
| 79.4 | http | 444.0 | 1243.4 | 17.5 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.202 |
| 79.1 | http | 456.8 | 1283.2 | 17.2 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.207 |
| 79.09 | http | 457.4 | 1287.6 | 17.19 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.198 |
| 78.79 | http | 411.0 | 1124.7 | 18.26 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.210 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 1.0 | 1.0 | 143 | 344 | prefer |
| Au1rxx-base64 | 0.939 | 0.875 | 586 | 1632 | prefer |
| DeltaKronecker-all | 0.629 | 0.549 | 284 | 3437 | observe |
| Surfboard-tg-mixed | 0.623 | 0.544 | 90 | 5182 | observe |
| mheidari-all | 0.349 | 0.26 | 50 | 18808 | observe |
| xiaoji235-airport-v2ray-all | 0.335 | 1.0 | 1 | 3833 | observe |
| tg-OutlineReleasedKey | 0.257 | 1.0 | 1 | 56 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5486 | observe |
| Epodonios-all | 0.255 | None | 0 | 5849 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6871 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4109 | observe |
| barry-far-vless | 0.255 | None | 0 | 4560 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5208 | observe |
| Au1rxx-clash | 0.24 | None | 0 | 1632 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| cn-block | TimeoutError | - | 87 |
| geo | TimeoutError | - | 70 |
| speed | TimeoutError | - | 41 |
| speed | ClientOSError | - | 31 |
| geo | ClientOSError | - | 21 |
| 204 | TimeoutError | - | 19 |
| 204 | ClientOSError | - | 7 |
| 204 | ProxyError | - | 6 |
| geo | ProxyError | - | 2 |
| cn-block | ClientOSError | - | 2 |
| cn-block | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
