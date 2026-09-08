# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-08 21:09:04 |
| 运行耗时 | 652.8s |
| 订阅源总数 | 107 |
| 健康订阅源 | 95 |
| 原始节点 | 84956 |
| 去重后节点 | 22773 |
| TCP 可达 | 3000 |
| 真实可用 | 527 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22773 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.9 |
| geo | 1.4 |
| tcp | 37.4 |
| probe | 236.2 |
| real_test | 283.2 |
| generate | 87.7 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 52481 |
| vmess | 12056 |
| shadowsocks | 9735 |
| trojan | 8295 |
| hysteria2 | 1614 |
| http | 570 |
| shadowsocksr | 128 |
| socks | 54 |
| hysteria | 11 |
| tuic | 8 |
| anytls | 4 |

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
| 84.72 | hysteria2 | 213.0 | 509.2 | 22.85 | 0.0 | 10.0 | 13.57 | 19.3 | Au1rxx-base64 | 66.94.121.46 |
| 81.92 | vless | 210.3 | 487.3 | 22.91 | 0.0 | 10.0 | 9.71 | 19.3 | Au1rxx-base64 | 172.235.43.210 |
| 81.68 | vless | 220.7 | 559.6 | 22.67 | 0.0 | 10.0 | 9.71 | 19.3 | Au1rxx-base64 | 38.244.20.160 |
| 80.61 | vless | 208.3 | 484.4 | 22.96 | 0.0 | 10.0 | 9.71 | 19.3 | Au1rxx-base64 | 172.233.139.46 |
| 80.46 | vless | 230.2 | 593.7 | 22.45 | 0.0 | 10.0 | 9.71 | 19.3 | Au1rxx-base64 | 38.209.125.45 |
| 80.32 | shadowsocks | 241.5 | 555.5 | 22.19 | 0.0 | 10.0 | 12.83 | 19.3 | Au1rxx-base64 | 149.22.95.183 |
| 79.95 | vless | 248.1 | 560.5 | 22.04 | 0.0 | 10.0 | 9.71 | 19.3 | Au1rxx-base64 | 172.235.38.85 |
| 79.61 | shadowsocks | 272.2 | 638.2 | 21.48 | 0.0 | 10.0 | 12.83 | 19.3 | Au1rxx-base64 | 173.244.56.6 |
| 79.48 | vless | 229.5 | 503.2 | 22.47 | 0.0 | 10.0 | 9.71 | 19.3 | Au1rxx-base64 | 31.58.50.200 |
| 79.45 | vless | 316.8 | 823.5 | 20.44 | 0.0 | 10.0 | 9.71 | 19.3 | Au1rxx-base64 | 15.204.97.216 |
| 79.21 | vless | 240.9 | 590.9 | 22.2 | 0.0 | 10.0 | 9.71 | 19.3 | Au1rxx-base64 | 38.246.229.58 |
| 76.5 | vless | 228.5 | 513.5 | 22.49 | 0.0 | 10.0 | 9.71 | 19.3 | Au1rxx-base64 | 5.253.38.67 |
| 75.57 | trojan | 309.0 | 651.3 | 20.62 | 0.0 | 10.0 | 12.14 | 19.3 | Au1rxx-base64 | 64.94.95.118 |
| 75.5 | shadowsocks | 301.9 | 667.2 | 20.79 | 0.0 | 10.0 | 12.83 | 19.3 | Au1rxx-base64 | 156.146.38.168 |
| 75.49 | vless | 261.2 | 605.1 | 21.73 | 0.0 | 10.0 | 9.71 | 19.3 | Au1rxx-base64 | 108.162.198.178 |
| 75.2 | vless | 289.4 | 398.9 | 21.08 | 0.04 | 10.0 | 9.71 | 19.3 | Au1rxx-base64 | 172.64.158.146 |
| 74.66 | vless | 243.1 | 580.2 | 22.15 | 0.0 | 10.0 | 9.71 | 19.3 | Au1rxx-base64 | 172.64.42.85 |
| 74.34 | trojan | 304.3 | 640.9 | 20.73 | 0.0 | 10.0 | 12.14 | 19.3 | Au1rxx-base64 | 64.94.95.117 |
| 73.97 | vless | 272.8 | 413.6 | 21.46 | 0.0 | 10.0 | 9.71 | 19.3 | Au1rxx-base64 | 172.64.229.170 |
| 73.62 | shadowsocks | 225.7 | 538.8 | 22.55 | 0.0 | 10.0 | 12.83 | 14.42 | Surfboard-tg-mixed | 108.181.0.177 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | 0.942 | 291 | 1700 | prefer |
| DeltaKronecker-all | 0.92 | 0.87 | 23 | 6097 | prefer |
| Surfboard-tg-mixed | 0.814 | 0.737 | 167 | 7370 | prefer |
| mheidari-all | 0.811 | 0.735 | 117 | 16416 | prefer |
| ermaozi | 0.702 | 0.697 | 33 | 409 | prefer |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| Epodonios-all | 0.255 | None | 0 | 7999 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 8578 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 6089 | observe |
| barry-far-vless | 0.255 | None | 0 | 6497 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4219 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.243 | None | 0 | 1700 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | TimeoutError | - | 27 |
| geo | ClientOSError | - | 21 |
| 204 | ProxyError | - | 16 |
| cn-block | TimeoutError | - | 14 |
| cn-block | ClientOSError | - | 9 |
| speed | TimeoutError | - | 5 |
| 204 | ClientOSError | - | 4 |
| geo | TimeoutError | - | 4 |
| speed | ClientOSError | - | 4 |
| cn-block | ProxyError | - | 3 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
