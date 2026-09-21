# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-21 04:34:48 |
| 运行耗时 | 848.5s |
| 订阅源总数 | 107 |
| 健康订阅源 | 94 |
| 原始节点 | 83915 |
| 去重后节点 | 23652 |
| TCP 可达 | 3000 |
| 真实可用 | 672 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23652 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.5 |
| geo | 1.4 |
| tcp | 39.3 |
| probe | 272.9 |
| real_test | 449.0 |
| generate | 79.4 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 50272 |
| vmess | 13549 |
| shadowsocks | 9781 |
| trojan | 8351 |
| hysteria2 | 1090 |
| http | 647 |
| shadowsocksr | 140 |
| socks | 67 |
| hysteria | 9 |
| anytls | 5 |
| tuic | 4 |

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
| 81.07 | hysteria2 | 253.3 | 556.9 | 21.92 | 0.0 | 10.0 | 12.19 | 19.42 | Au1rxx-base64 | 66.94.121.46 |
| 80.83 | vless | 310.0 | 802.6 | 20.6 | 0.0 | 10.0 | 10.81 | 19.42 | Au1rxx-base64 | 15.204.97.216 |
| 80.61 | vless | 319.6 | 790.4 | 20.38 | 0.0 | 10.0 | 10.81 | 19.42 | Au1rxx-base64 | 15.204.97.209 |
| 80.06 | http | 216.3 | 557.1 | 22.77 | 0.0 | 10.0 | 12.35 | 17.94 | ermaozi | 138.199.35.216 |
| 79.51 | http | 239.9 | 623.3 | 22.22 | 0.0 | 10.0 | 12.35 | 17.94 | ermaozi | 138.199.35.205 |
| 79.38 | http | 245.5 | 641.2 | 22.09 | 0.0 | 10.0 | 12.35 | 17.94 | ermaozi | 138.199.35.198 |
| 78.69 | http | 232.2 | 604.7 | 22.4 | 0.0 | 10.0 | 12.35 | 17.94 | ermaozi | 138.199.35.203 |
| 78.63 | http | 235.1 | 619.4 | 22.34 | 0.0 | 10.0 | 12.35 | 17.94 | ermaozi | 138.199.35.212 |
| 77.36 | vless | 244.0 | 600.6 | 22.13 | 0.0 | 10.0 | 10.81 | 19.42 | Au1rxx-base64 | 195.123.240.65 |
| 76.42 | http | 373.8 | 1027.5 | 19.13 | 0.0 | 10.0 | 12.35 | 17.94 | ermaozi | 138.199.35.213 |
| 76.41 | vless | 246.3 | 573.4 | 22.08 | 0.0 | 10.0 | 10.81 | 18.52 | DeltaKronecker-all | 47.88.107.209 |
| 76.3 | vless | 246.8 | 588.3 | 22.07 | 0.0 | 10.0 | 10.81 | 19.42 | Au1rxx-base64 | 195.26.229.86 |
| 76.0 | shadowsocks | 226.4 | 538.7 | 22.54 | 0.0 | 10.0 | 13.44 | 14.02 | mheidari-all | 149.22.95.183 |
| 75.92 | vless | 300.8 | 728.7 | 20.81 | 0.0 | 10.0 | 10.81 | 18.52 | DeltaKronecker-all | 192.3.20.155 |
| 75.51 | vless | 189.0 | 491.6 | 23.4 | 0.0 | 7.88 | 10.81 | 19.42 | Au1rxx-base64 | us7-2.998998.best |
| 75.27 | shadowsocks | 240.7 | 569.4 | 22.21 | 0.0 | 10.0 | 13.44 | 13.62 | Surfboard-tg-mixed | 173.244.56.9 |
| 75.09 | trojan | 182.8 | 497.9 | 23.55 | 0.0 | 10.0 | 4.62 | 19.42 | Au1rxx-base64 | 100.42.228.109 |
| 74.9 | vless | 228.0 | 614.8 | 22.5 | 0.0 | 10.0 | 10.81 | 19.42 | Au1rxx-base64 | 172.235.43.210 |
| 74.61 | http | 235.6 | 614.7 | 22.32 | 0.0 | 10.0 | 12.35 | 17.94 | ermaozi | 138.199.35.196 |
| 74.47 | vless | 261.6 | 453.8 | 21.72 | 0.0 | 10.0 | 10.81 | 19.42 | Au1rxx-base64 | 212.104.128.217 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.933 | 0.867 | 332 | 1693 | prefer |
| Surfboard-tg-mixed | 0.736 | 0.659 | 123 | 7202 | prefer |
| ermaozi | 0.7 | 0.694 | 49 | 355 | prefer |
| mheidari-all | 0.57 | 0.49 | 100 | 15960 | observe |
| DeltaKronecker-all | 0.551 | 0.471 | 450 | 6092 | observe |
| mahdibland-V2RayAggregator | 0.335 | 1.0 | 1 | 4315 | observe |
| ermaozi-get_subscribe | 0.297 | 0.4 | 10 | 382 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| tg-oneclickvpnkeys | 0.258 | 1.0 | 1 | 74 | observe |
| Epodonios-all | 0.255 | None | 0 | 7661 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 8828 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5800 | observe |
| barry-far-vless | 0.255 | None | 0 | 6015 | observe |
| Au1rxx-clash | 0.243 | None | 0 | 1693 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 168 |
| geo | ClientOSError | - | 71 |
| speed | TimeoutError | - | 54 |
| speed | ClientOSError | - | 46 |
| 204 | ProxyError | - | 25 |
| cn-block | ClientOSError | - | 16 |
| cn-block | TimeoutError | - | 12 |
| cn-block | ProxyError | - | 5 |
| 204 | ClientOSError | - | 5 |
| geo | ProxyError | - | 3 |
| 204 | TimeoutError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
