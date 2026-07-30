# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-30 19:46:12 |
| 运行耗时 | 294.3s |
| 订阅源总数 | 107 |
| 健康订阅源 | 102 |
| 原始节点 | 78433 |
| 去重后节点 | 23046 |
| TCP 可达 | 3000 |
| 真实可用 | 511 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23046 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.1 |
| geo | 1.3 |
| tcp | 34.2 |
| probe | 70.1 |
| real_test | 148.8 |
| generate | 33.8 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 45636 |
| vmess | 11424 |
| shadowsocks | 10249 |
| trojan | 10213 |
| hysteria2 | 606 |
| http | 116 |
| shadowsocksr | 73 |
| socks | 56 |
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
| 83.92 | http | 201.0 | 477.0 | 23.13 | 0.0 | 10.0 | 14.87 | 19.92 | zhangkai | 138.199.35.196 |
| 82.16 | http | 190.6 | 480.3 | 23.37 | 0.0 | 10.0 | 14.87 | 19.92 | zhangkai | 138.199.35.210 |
| 82.09 | http | 193.5 | 491.7 | 23.3 | 0.0 | 10.0 | 14.87 | 19.92 | zhangkai | 138.199.35.212 |
| 82.03 | http | 196.1 | 484.6 | 23.24 | 0.0 | 10.0 | 14.87 | 19.92 | zhangkai | 138.199.35.213 |
| 81.88 | http | 202.5 | 487.7 | 23.09 | 0.0 | 10.0 | 14.87 | 19.92 | zhangkai | 138.199.35.207 |
| 81.87 | http | 202.8 | 498.9 | 23.08 | 0.0 | 10.0 | 14.87 | 19.92 | zhangkai | 138.199.35.200 |
| 81.85 | http | 203.6 | 490.8 | 23.06 | 0.0 | 10.0 | 14.87 | 19.92 | zhangkai | 138.199.35.202 |
| 81.82 | http | 205.0 | 515.5 | 23.03 | 0.0 | 10.0 | 14.87 | 19.92 | zhangkai | 138.199.35.205 |
| 81.81 | http | 205.4 | 502.8 | 23.02 | 0.0 | 10.0 | 14.87 | 19.92 | zhangkai | 138.199.35.209 |
| 81.8 | http | 206.1 | 510.7 | 23.01 | 0.0 | 10.0 | 14.87 | 19.92 | zhangkai | 138.199.35.216 |
| 81.75 | http | 208.3 | 512.1 | 22.96 | 0.0 | 10.0 | 14.87 | 19.92 | zhangkai | 138.199.35.218 |
| 81.74 | http | 208.4 | 502.9 | 22.95 | 0.0 | 10.0 | 14.87 | 19.92 | zhangkai | 138.199.35.206 |
| 81.68 | http | 211.2 | 503.6 | 22.89 | 0.0 | 10.0 | 14.87 | 19.92 | zhangkai | 138.199.35.214 |
| 81.68 | http | 211.2 | 504.9 | 22.89 | 0.0 | 10.0 | 14.87 | 19.92 | zhangkai | 138.199.35.217 |
| 81.67 | http | 211.4 | 512.1 | 22.88 | 0.0 | 10.0 | 14.87 | 19.92 | zhangkai | 138.199.35.204 |
| 81.67 | http | 211.5 | 504.4 | 22.88 | 0.0 | 10.0 | 14.87 | 19.92 | zhangkai | 138.199.35.215 |
| 81.66 | http | 212.1 | 504.7 | 22.87 | 0.0 | 10.0 | 14.87 | 19.92 | zhangkai | 138.199.35.208 |
| 81.63 | http | 213.3 | 532.3 | 22.84 | 0.0 | 10.0 | 14.87 | 19.92 | zhangkai | 138.199.35.199 |
| 81.62 | http | 213.8 | 529.3 | 22.83 | 0.0 | 10.0 | 14.87 | 19.92 | zhangkai | 138.199.35.198 |
| 80.07 | http | 194.5 | 498.7 | 23.28 | 0.0 | 10.0 | 14.87 | 19.92 | zhangkai | 138.199.35.195 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.996 | 1.0 | 113 | 129 | prefer |
| Au1rxx-base64 | 0.866 | 0.811 | 265 | 1430 | prefer |
| Surfboard-tg-mixed | 0.535 | 0.45 | 20 | 5387 | observe |
| DeltaKronecker-all | 0.519 | 0.438 | 381 | 5759 | observe |
| ninja-vless | 0.457 | 0.714 | 7 | 1791 | observe |
| Epodonios-all | 0.335 | 1.0 | 1 | 6090 | observe |
| mheidari-all | 0.259 | 0.333 | 3 | 16222 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5342 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3973 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6594 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4264 | observe |
| barry-far-vless | 0.255 | None | 0 | 4589 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5047 | observe |
| Au1rxx-clash | 0.232 | None | 0 | 1430 | observe |
| nscl5-all | 0.232 | None | 0 | 1413 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | ProxyError | - | 75 |
| cn-block | TimeoutError | - | 55 |
| geo | TimeoutError | - | 42 |
| 204 | TimeoutError | - | 24 |
| speed | TimeoutError | - | 19 |
| geo | ClientOSError | - | 19 |
| cn-block | ProxyError | - | 19 |
| geo | ProxyError | - | 9 |
| speed | ClientOSError | - | 7 |
| 204 | ClientOSError | - | 5 |
| speed | ProxyError | - | 5 |
| cn-block | ClientOSError | - | 2 |
| geo | parse | TimeoutError | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
