# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-07 23:03:18 |
| 运行耗时 | 408.3s |
| 订阅源总数 | 107 |
| 健康订阅源 | 94 |
| 原始节点 | 98461 |
| 去重后节点 | 27482 |
| TCP 可达 | 3000 |
| 真实可用 | 428 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 27482 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.5 |
| geo | 1.4 |
| tcp | 46.5 |
| probe | 189.0 |
| real_test | 140.9 |
| generate | 26.1 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 58111 |
| vmess | 15548 |
| shadowsocks | 11720 |
| trojan | 10668 |
| hysteria2 | 1522 |
| http | 561 |
| shadowsocksr | 171 |
| socks | 100 |
| anytls | 34 |
| hysteria | 17 |
| tuic | 9 |

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
| 83.91 | vless | 198.4 | 519.7 | 23.19 | 0.0 | 10.0 | 11.34 | 19.38 | Au1rxx-base64 | 107.173.237.146 |
| 83.59 | vless | 212.1 | 507.3 | 22.87 | 0.0 | 10.0 | 11.34 | 19.38 | Au1rxx-base64 | 137.175.82.40 |
| 83.56 | vless | 213.1 | 500.6 | 22.84 | 0.0 | 10.0 | 11.34 | 19.38 | Au1rxx-base64 | 47.251.108.158 |
| 81.91 | hysteria2 | 241.9 | 238.3 | 22.18 | 6.06 | 9.87 | 12.32 | 19.38 | Au1rxx-base64 | 158.101.148.79 |
| 81.85 | vless | 287.0 | 757.6 | 21.13 | 0.0 | 10.0 | 11.34 | 19.38 | Au1rxx-base64 | 195.123.240.65 |
| 81.83 | vless | 201.6 | 509.3 | 23.11 | 0.0 | 10.0 | 11.34 | 19.38 | Au1rxx-base64 | 144.202.126.147 |
| 80.56 | shadowsocks | 265.3 | 643.3 | 21.64 | 0.0 | 10.0 | 13.54 | 19.38 | Au1rxx-base64 | 156.146.38.168 |
| 80.48 | hysteria2 | 256.0 | 290.6 | 21.85 | 4.1 | 9.9 | 12.32 | 19.38 | Au1rxx-base64 | 132.226.14.77 |
| 79.62 | hysteria2 | 235.2 | 243.8 | 22.33 | 5.86 | 6.94 | 12.32 | 19.38 | Au1rxx-base64 | open.2ml.bid |
| 79.22 | vless | 272.9 | 600.7 | 21.46 | 0.0 | 10.0 | 11.34 | 19.38 | Au1rxx-base64 | 15.204.97.216 |
| 78.92 | vless | 301.5 | 638.8 | 20.8 | 0.0 | 10.0 | 11.34 | 19.38 | Au1rxx-base64 | 51.81.203.63 |
| 78.0 | vless | 378.2 | 953.2 | 19.02 | 0.0 | 10.0 | 11.34 | 19.38 | Au1rxx-base64 | 23.95.222.127 |
| 77.95 | shadowsocks | 295.2 | 734.6 | 20.94 | 0.0 | 10.0 | 13.54 | 19.38 | Au1rxx-base64 | 156.146.38.170 |
| 77.74 | hysteria2 | 251.9 | 305.1 | 21.95 | 3.56 | 7.42 | 12.32 | 19.38 | Au1rxx-base64 | open.w2m.ink |
| 77.41 | hysteria2 | 346.7 | 826.0 | 19.75 | 0.0 | 10.0 | 12.32 | 19.38 | Au1rxx-base64 | 129.213.91.185 |
| 77.21 | vless | 228.5 | 548.0 | 22.49 | 0.0 | 10.0 | 11.34 | 19.38 | Au1rxx-base64 | 104.17.98.5 |
| 76.98 | vless | 304.7 | 584.5 | 20.72 | 0.0 | 10.0 | 11.34 | 19.38 | Au1rxx-base64 | 15.204.97.197 |
| 76.36 | shadowsocks | 292.2 | 637.9 | 21.01 | 0.0 | 10.0 | 13.54 | 19.38 | Au1rxx-base64 | 149.22.95.183 |
| 76.22 | shadowsocks | 267.3 | 575.1 | 21.59 | 0.0 | 10.0 | 13.54 | 19.38 | Au1rxx-base64 | 173.244.56.6 |
| 76.12 | shadowsocks | 263.2 | 643.8 | 21.68 | 0.0 | 10.0 | 13.54 | 19.38 | Au1rxx-base64 | 156.146.38.169 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.94 | 0.869 | 352 | 1824 | prefer |
| mheidari-all | 0.925 | 0.851 | 101 | 23169 | prefer |
| ermaozi | 0.636 | 0.615 | 39 | 664 | observe |
| Surfboard-tg-mixed | 0.529 | 0.857 | 7 | 7189 | observe |
| DeltaKronecker-all | 0.32 | 0.5 | 4 | 5344 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| tg-OutlineReleasedKey | 0.257 | 1.0 | 1 | 50 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5138 | observe |
| Epodonios-all | 0.255 | None | 0 | 7553 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9262 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5706 | observe |
| barry-far-vless | 0.255 | None | 0 | 5859 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4431 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | ProxyError | - | 19 |
| speed | TimeoutError | - | 16 |
| 204 | ClientOSError | - | 9 |
| speed | ClientOSError | - | 9 |
| cn-block | TimeoutError | - | 9 |
| geo | ClientOSError | - | 7 |
| 204 | TimeoutError | - | 6 |
| geo | TimeoutError | - | 5 |
| cn-block | ClientOSError | - | 4 |
| cn-block | ProxyError | - | 2 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
