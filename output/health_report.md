# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-14 19:05:52 |
| 运行耗时 | 311.5s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 78247 |
| 去重后节点 | 22446 |
| TCP 可达 | 3000 |
| 真实可用 | 837 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22446 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 13.2 |
| geo | 1.3 |
| tcp | 34.2 |
| probe | 59.6 |
| real_test | 165.6 |
| generate | 37.6 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 44279 |
| trojan | 11680 |
| vmess | 10401 |
| shadowsocks | 10228 |
| hysteria2 | 1320 |
| http | 168 |
| socks | 77 |
| shadowsocksr | 75 |
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
| 85.35 | http | 185.1 | 474.3 | 23.49 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.206 |
| 85.35 | http | 185.4 | 480.0 | 23.49 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.211 |
| 85.29 | http | 188.0 | 481.0 | 23.43 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.195 |
| 85.22 | http | 190.9 | 479.6 | 23.36 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.209 |
| 85.18 | http | 192.4 | 492.2 | 23.32 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.210 |
| 85.15 | http | 193.7 | 495.0 | 23.29 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.214 |
| 85.12 | http | 195.0 | 497.9 | 23.26 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.204 |
| 85.03 | http | 198.9 | 503.0 | 23.17 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.199 |
| 85.01 | http | 199.8 | 491.2 | 23.15 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.212 |
| 85.0 | http | 200.4 | 499.2 | 23.14 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.215 |
| 84.97 | http | 201.8 | 501.2 | 23.11 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.208 |
| 84.94 | http | 202.9 | 500.4 | 23.08 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.213 |
| 84.93 | http | 203.6 | 513.7 | 23.07 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.197 |
| 84.92 | http | 203.7 | 500.5 | 23.06 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.220 |
| 84.75 | hysteria2 | 231.6 | 508.3 | 22.42 | 0.0 | 10.0 | 13.33 | 20.0 | Au1rxx-base64 | 150.241.102.127 |
| 84.54 | trojan | 229.6 | 517.8 | 22.46 | 0.0 | 10.0 | 14.58 | 20.0 | Au1rxx-base64 | liked-serval.rooster465.autos |
| 84.51 | trojan | 230.9 | 531.5 | 22.43 | 0.0 | 10.0 | 14.58 | 20.0 | Au1rxx-base64 | 44.246.163.102 |
| 84.46 | trojan | 233.3 | 524.6 | 22.38 | 0.0 | 10.0 | 14.58 | 20.0 | Au1rxx-base64 | 44.243.85.47 |
| 84.4 | trojan | 235.8 | 535.1 | 22.32 | 0.0 | 10.0 | 14.58 | 20.0 | Au1rxx-base64 | 44.244.3.114 |
| 84.29 | trojan | 228.6 | 521.9 | 22.49 | 0.0 | 10.0 | 14.58 | 20.0 | Au1rxx-base64 | 44.242.235.129 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | 0.938 | 673 | 1715 | prefer |
| zhangkai | 0.999 | 1.0 | 127 | 159 | prefer |
| Surfboard-tg-mixed | 0.717 | 0.641 | 78 | 5725 | prefer |
| DeltaKronecker-all | 0.648 | 0.571 | 42 | 5969 | observe |
| mheidari-all | 0.4 | 0.75 | 4 | 15859 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| tg-oneclickvpnkeys | 0.261 | 1.0 | 1 | 160 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5157 | observe |
| Epodonios-all | 0.255 | None | 0 | 6388 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3995 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7685 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4488 | observe |
| barry-far-vless | 0.255 | None | 0 | 4814 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 3992 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | TimeoutError | - | 35 |
| geo | TimeoutError | - | 11 |
| speed | TimeoutError | - | 9 |
| cn-block | TimeoutError | - | 9 |
| geo | ClientOSError | - | 6 |
| 204 | ProxyError | - | 6 |
| speed | ClientOSError | - | 5 |
| 204 | ClientOSError | - | 4 |
| cn-block | ClientOSError | - | 3 |
| cn-block | ProxyError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
