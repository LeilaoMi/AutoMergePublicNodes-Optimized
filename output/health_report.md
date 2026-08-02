# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-02 19:23:45 |
| 运行耗时 | 326.4s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 81361 |
| 去重后节点 | 22680 |
| TCP 可达 | 3000 |
| 真实可用 | 634 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22680 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 10.6 |
| geo | 1.5 |
| tcp | 34.8 |
| probe | 64.1 |
| real_test | 176.7 |
| generate | 38.6 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 49706 |
| vmess | 12548 |
| shadowsocks | 10285 |
| trojan | 7752 |
| hysteria2 | 738 |
| http | 165 |
| shadowsocksr | 73 |
| socks | 72 |
| hysteria | 10 |
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
| 80.29 | http | 405.7 | 1132.8 | 18.39 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.198 |
| 80.27 | http | 406.2 | 1132.4 | 18.37 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.197 |
| 80.27 | http | 406.3 | 1139.1 | 18.37 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.220 |
| 80.26 | http | 406.7 | 1132.9 | 18.36 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.217 |
| 80.25 | http | 407.2 | 1133.6 | 18.35 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.209 |
| 80.23 | http | 408.3 | 1140.8 | 18.33 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.208 |
| 80.1 | http | 413.5 | 1139.6 | 18.2 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.218 |
| 80.09 | http | 414.4 | 1137.6 | 18.19 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.207 |
| 80.08 | http | 414.8 | 1137.1 | 18.18 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.211 |
| 80.08 | http | 414.8 | 1142.9 | 18.18 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.212 |
| 80.07 | http | 414.9 | 1141.5 | 18.17 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.213 |
| 80.07 | http | 415.1 | 1144.9 | 18.17 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.206 |
| 80.06 | http | 415.7 | 1142.7 | 18.16 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.216 |
| 80.05 | http | 416.1 | 1143.6 | 18.15 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.215 |
| 80.01 | http | 417.6 | 1144.5 | 18.11 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.195 |
| 79.99 | http | 418.7 | 1149.8 | 18.09 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.204 |
| 79.89 | http | 422.9 | 1151.4 | 17.99 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.200 |
| 79.87 | http | 423.5 | 1158.5 | 17.97 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.205 |
| 79.82 | http | 426.1 | 1158.5 | 17.92 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.214 |
| 79.8 | http | 426.6 | 1161.1 | 17.9 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.202 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 1.0 | 1.0 | 143 | 344 | prefer |
| Au1rxx-base64 | 0.774 | 0.709 | 533 | 1651 | prefer |
| DeltaKronecker-all | 0.542 | 0.462 | 117 | 3437 | observe |
| Surfboard-tg-mixed | 0.477 | 0.395 | 129 | 5222 | observe |
| mheidari-all | 0.418 | 0.5 | 10 | 18817 | observe |
| xiaoji235-airport-v2ray-all | 0.335 | 1.0 | 1 | 3833 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| tg-OutlineReleasedKey | 0.257 | 1.0 | 1 | 56 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5486 | observe |
| Epodonios-all | 0.255 | None | 0 | 5783 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3975 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7117 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4122 | observe |
| barry-far-vless | 0.255 | None | 0 | 4490 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5208 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 102 |
| 204 | TimeoutError | - | 48 |
| 204 | ProxyError | - | 43 |
| speed | TimeoutError | - | 29 |
| cn-block | TimeoutError | - | 22 |
| geo | ClientOSError | - | 19 |
| speed | ClientOSError | - | 15 |
| 204 | ClientOSError | - | 8 |
| cn-block | ProxyError | - | 7 |
| geo | ProxyError | - | 4 |
| cn-block | ClientOSError | - | 3 |
| speed | ProxyError | - | 3 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
