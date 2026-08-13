# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-13 07:46:43 |
| 运行耗时 | 278.0s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 79301 |
| 去重后节点 | 22373 |
| TCP 可达 | 3000 |
| 真实可用 | 687 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22373 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.0 |
| geo | 1.1 |
| tcp | 33.3 |
| probe | 62.4 |
| real_test | 146.9 |
| generate | 28.4 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 44303 |
| vmess | 13367 |
| trojan | 10432 |
| shadowsocks | 9733 |
| hysteria2 | 1136 |
| http | 160 |
| socks | 77 |
| shadowsocksr | 74 |
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
| 85.26 | http | 189.0 | 485.2 | 23.4 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.206 |
| 85.21 | http | 191.3 | 496.6 | 23.35 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.209 |
| 85.18 | http | 192.4 | 489.6 | 23.32 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.220 |
| 85.15 | http | 193.9 | 498.8 | 23.29 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.204 |
| 85.14 | http | 194.4 | 501.5 | 23.28 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.208 |
| 85.06 | http | 197.6 | 511.6 | 23.2 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.215 |
| 85.06 | http | 197.9 | 506.5 | 23.2 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.214 |
| 85.03 | http | 199.1 | 508.8 | 23.17 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.195 |
| 84.98 | http | 201.0 | 512.7 | 23.12 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.212 |
| 84.95 | http | 202.4 | 508.5 | 23.09 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.197 |
| 84.95 | http | 202.5 | 510.5 | 23.09 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.211 |
| 84.95 | http | 202.6 | 525.5 | 23.09 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.199 |
| 84.93 | http | 203.4 | 526.6 | 23.07 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.213 |
| 84.93 | http | 203.6 | 516.7 | 23.07 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.210 |
| 81.52 | shadowsocks | 193.9 | 478.4 | 23.29 | 0.0 | 10.0 | 14.05 | 18.68 | Au1rxx-base64 | 108.181.0.177 |
| 81.18 | shadowsocks | 230.0 | 548.2 | 22.45 | 0.0 | 10.0 | 14.05 | 18.68 | Au1rxx-base64 | 149.22.95.183 |
| 80.8 | shadowsocks | 224.9 | 607.5 | 22.57 | 0.0 | 10.0 | 14.05 | 18.68 | Au1rxx-base64 | 70.39.178.204 |
| 80.54 | shadowsocks | 236.2 | 589.9 | 22.31 | 0.0 | 10.0 | 14.05 | 18.68 | Au1rxx-base64 | 108.181.118.10 |
| 80.11 | shadowsocks | 276.3 | 645.6 | 21.38 | 0.0 | 10.0 | 14.05 | 18.68 | Au1rxx-base64 | 173.244.56.9 |
| 80.11 | shadowsocks | 276.5 | 640.0 | 21.38 | 0.0 | 10.0 | 14.05 | 18.68 | Au1rxx-base64 | 173.244.56.6 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | 0.948 | 464 | 1501 | prefer |
| zhangkai | 0.999 | 1.0 | 128 | 159 | prefer |
| Surfboard-tg-mixed | 0.744 | 0.667 | 135 | 5801 | prefer |
| mheidari-all | 0.616 | 0.538 | 26 | 16910 | observe |
| DeltaKronecker-all | 0.4 | 0.312 | 48 | 4975 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5203 | observe |
| Epodonios-all | 0.255 | None | 0 | 6457 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3996 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7624 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4621 | observe |
| barry-far-vless | 0.255 | None | 0 | 4989 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5197 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| nscl5-all | 0.241 | None | 0 | 1654 | observe |
| Au1rxx-clash | 0.235 | None | 0 | 1501 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 31 |
| cn-block | TimeoutError | - | 20 |
| geo | ClientOSError | - | 16 |
| 204 | TimeoutError | - | 14 |
| speed | TimeoutError | - | 8 |
| 204 | ProxyError | - | 7 |
| speed | ClientOSError | - | 4 |
| geo | ProxyError | - | 4 |
| cn-block | ClientOSError | - | 4 |
| 204 | ClientOSError | - | 3 |
| cn-block | ProxyError | - | 3 |
| geo | parse | TimeoutError | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
