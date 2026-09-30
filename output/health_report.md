# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-30 12:25:19 |
| 运行耗时 | 576.4s |
| 订阅源总数 | 107 |
| 健康订阅源 | 94 |
| 原始节点 | 96400 |
| 去重后节点 | 26890 |
| TCP 可达 | 3000 |
| 真实可用 | 378 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 26890 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.7 |
| geo | 1.4 |
| tcp | 45.8 |
| probe | 277.0 |
| real_test | 175.2 |
| generate | 72.3 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 58466 |
| vmess | 15245 |
| shadowsocks | 11270 |
| trojan | 9047 |
| hysteria2 | 1430 |
| http | 639 |
| shadowsocksr | 171 |
| socks | 72 |
| anytls | 37 |
| hysteria | 15 |
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
| 82.12 | hysteria2 | 309.3 | 683.7 | 20.62 | 0.0 | 10.0 | 13.85 | 20.0 | Au1rxx-base64 | 192.255.128.123 |
| 81.43 | shadowsocks | 251.6 | 627.8 | 21.95 | 0.0 | 10.0 | 13.48 | 20.0 | Au1rxx-base64 | 156.146.38.167 |
| 80.01 | shadowsocks | 310.1 | 770.5 | 20.6 | 0.0 | 10.0 | 13.48 | 20.0 | Au1rxx-base64 | 37.19.198.236 |
| 79.11 | shadowsocks | 331.6 | 826.4 | 20.1 | 0.0 | 9.53 | 13.48 | 20.0 | Au1rxx-base64 | 37.19.198.160 |
| 78.66 | shadowsocks | 305.2 | 748.9 | 20.71 | 0.0 | 10.0 | 13.48 | 20.0 | Au1rxx-base64 | 37.19.198.243 |
| 77.39 | shadowsocks | 324.3 | 713.3 | 20.27 | 0.0 | 10.0 | 13.48 | 20.0 | Au1rxx-base64 | 140.82.63.79 |
| 77.0 | shadowsocks | 355.9 | 932.9 | 19.54 | 0.0 | 8.48 | 13.48 | 20.0 | Au1rxx-base64 | yyz-ca-01.blncvpn4u.cc |
| 76.79 | shadowsocks | 300.8 | 742.5 | 20.81 | 0.0 | 9.52 | 13.48 | 20.0 | Au1rxx-base64 | 37.19.198.244 |
| 76.7 | shadowsocks | 305.1 | 848.0 | 20.72 | 0.0 | 10.0 | 13.48 | 20.0 | Au1rxx-base64 | 66.23.204.219 |
| 76.43 | shadowsocks | 288.3 | 715.3 | 21.1 | 0.0 | 9.52 | 13.48 | 20.0 | Au1rxx-base64 | 185.156.47.97 |
| 76.35 | shadowsocks | 384.7 | 925.6 | 18.87 | 0.0 | 10.0 | 13.48 | 20.0 | Au1rxx-base64 | 15.204.246.132 |
| 75.36 | hysteria2 | 477.4 | 634.7 | 16.73 | 0.0 | 10.0 | 13.85 | 20.0 | Au1rxx-base64 | 66.94.121.46 |
| 75.32 | shadowsocks | 279.6 | 572.3 | 21.31 | 0.0 | 9.52 | 13.48 | 20.0 | Au1rxx-base64 | 173.244.56.6 |
| 75.26 | shadowsocks | 324.7 | 684.7 | 20.26 | 0.0 | 9.52 | 13.48 | 20.0 | Au1rxx-base64 | 149.22.95.183 |
| 74.83 | shadowsocks | 354.4 | 741.2 | 19.57 | 0.0 | 10.0 | 13.48 | 20.0 | Au1rxx-base64 | 108.181.57.93 |
| 74.7 | shadowsocks | 318.6 | 658.9 | 20.4 | 0.0 | 10.0 | 13.48 | 20.0 | Au1rxx-base64 | 108.181.118.10 |
| 74.25 | vless | 274.7 | 655.3 | 21.42 | 0.0 | 10.0 | 4.65 | 20.0 | Au1rxx-base64 | 195.211.98.43 |
| 74.18 | shadowsocks | 307.6 | 792.5 | 20.66 | 0.0 | 10.0 | 13.48 | 14.04 | Surfboard-tg-mixed | 156.146.38.169 |
| 74.18 | shadowsocks | 405.5 | 898.0 | 18.39 | 0.0 | 10.0 | 13.48 | 20.0 | Au1rxx-base64 | 15.204.233.41 |
| 73.5 | shadowsocks | 296.4 | 543.2 | 20.92 | 0.0 | 10.0 | 13.48 | 20.0 | Au1rxx-base64 | 108.181.0.177 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| mheidari-all | 0.931 | 0.867 | 45 | 22755 | prefer |
| Au1rxx-base64 | 0.842 | 0.774 | 274 | 1752 | prefer |
| ermaozi | 0.835 | 0.833 | 54 | 335 | prefer |
| Surfboard-tg-mixed | 0.587 | 0.507 | 142 | 6952 | observe |
| DeltaKronecker-all | 0.428 | 0.333 | 21 | 5434 | observe |
| tg-oneclickvpnkeys | 0.36 | 1.0 | 3 | 53 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5327 | observe |
| Epodonios-all | 0.255 | None | 0 | 7458 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9148 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5632 | observe |
| barry-far-vless | 0.255 | None | 0 | 5879 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4183 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | TimeoutError | - | 52 |
| speed | ClientOSError | - | 46 |
| 204 | ProxyError | - | 15 |
| cn-block | TimeoutError | - | 15 |
| cn-block | ClientOSError | - | 10 |
| geo | TimeoutError | - | 8 |
| speed | TimeoutError | - | 6 |
| 204 | ClientOSError | - | 6 |
| geo | ClientOSError | - | 2 |
| cn-block | ProxyError | - | 1 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
