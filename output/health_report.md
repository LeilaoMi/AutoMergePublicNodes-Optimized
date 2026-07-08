# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-08 14:30:48 |
| 运行耗时 | 195.2s |
| 订阅源总数 | 107 |
| 健康订阅源 | 102 |
| 原始节点 | 83404 |
| 去重后节点 | 24825 |
| TCP 可达 | 3000 |
| 真实可用 | 280 |
| Verified 输出 | 280 |
| Global 输出 | 292 |
| All 输出 | 24825 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.1 |
| geo | 1.3 |
| tcp | 32.1 |
| probe | 43.3 |
| real_test | 78.2 |
| generate | 35.2 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 48710 |
| trojan | 13468 |
| vmess | 10480 |
| shadowsocks | 9564 |
| hysteria2 | 846 |
| shadowsocksr | 143 |
| http | 140 |
| socks | 39 |
| hysteria | 8 |
| anytls | 4 |
| tuic | 2 |

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
| 77.88 | trojan | 303.5 | 750.1 | 20.75 | 0.0 | 10.0 | 12.83 | 17.18 | mheidari-all | 149.28.241.235 |
| 77.48 | shadowsocks | 268.4 | 658.2 | 21.57 | 0.0 | 10.0 | 12.99 | 16.92 | Au1rxx-base64 | 156.146.38.168 |
| 77.0 | shadowsocks | 282.0 | 699.9 | 21.25 | 0.0 | 10.0 | 12.99 | 16.92 | Au1rxx-base64 | 156.146.38.170 |
| 76.84 | shadowsocks | 274.6 | 656.4 | 21.42 | 0.0 | 10.0 | 12.99 | 16.92 | Au1rxx-base64 | 37.19.198.244 |
| 76.78 | shadowsocks | 273.7 | 671.2 | 21.44 | 0.0 | 10.0 | 12.99 | 16.92 | Au1rxx-base64 | 37.19.198.236 |
| 76.61 | shadowsocks | 266.7 | 658.3 | 21.6 | 0.0 | 10.0 | 12.99 | 16.92 | Au1rxx-base64 | 37.19.198.243 |
| 76.39 | shadowsocks | 271.8 | 663.2 | 21.49 | 0.0 | 10.0 | 12.99 | 16.92 | Au1rxx-base64 | 108.181.57.93 |
| 76.26 | trojan | 301.9 | 738.7 | 20.79 | 0.0 | 10.0 | 12.83 | 17.18 | mheidari-all | 45.32.195.168 |
| 76.24 | trojan | 352.9 | 880.1 | 19.61 | 0.0 | 10.0 | 12.83 | 16.84 | DeltaKronecker-all | 64.94.95.114 |
| 76.02 | trojan | 306.7 | 747.5 | 20.68 | 0.0 | 10.0 | 12.83 | 16.84 | DeltaKronecker-all | 64.94.95.115 |
| 75.04 | shadowsocks | 351.9 | 929.2 | 19.63 | 0.0 | 10.0 | 12.99 | 16.92 | Au1rxx-base64 | 185.196.61.82 |
| 74.61 | trojan | 300.1 | 721.3 | 20.83 | 0.0 | 10.0 | 12.83 | 15.74 | Surfboard-tg-mixed | 64.94.95.118 |
| 74.34 | trojan | 304.0 | 712.8 | 20.74 | 0.0 | 10.0 | 12.83 | 16.84 | DeltaKronecker-all | 64.94.95.117 |
| 73.99 | shadowsocks | 247.5 | 615.0 | 22.05 | 0.0 | 10.0 | 12.99 | 16.92 | Au1rxx-base64 | 156.146.38.167 |
| 71.85 | shadowsocks | 295.5 | 724.5 | 20.94 | 0.0 | 10.0 | 12.99 | 16.92 | Au1rxx-base64 | 37.19.198.160 |
| 70.95 | shadowsocks | 245.1 | 604.2 | 22.1 | 0.0 | 10.0 | 12.99 | 16.92 | Au1rxx-base64 | 198.98.53.130 |
| 70.89 | shadowsocks | 308.4 | 628.4 | 20.64 | 0.0 | 8.7 | 12.99 | 16.92 | Au1rxx-base64 | 149.22.95.183 |
| 68.89 | shadowsocks | 328.2 | 608.9 | 20.18 | 0.0 | 8.89 | 12.99 | 16.92 | Au1rxx-base64 | 108.181.118.10 |
| 68.49 | shadowsocks | 252.6 | 625.8 | 21.93 | 0.0 | 10.0 | 12.99 | 16.92 | Au1rxx-base64 | 156.146.38.169 |
| 68.42 | shadowsocks | 374.0 | 692.0 | 19.12 | 0.0 | 10.0 | 12.99 | 16.92 | Au1rxx-base64 | 108.181.0.177 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| Au1rxx-base64 | 0.849 | 0.857 | 56 | 116 | prefer |
| Surfboard-tg-mixed | 0.814 | 0.738 | 122 | 5938 | prefer |
| mheidari-all | 0.759 | 0.684 | 76 | 18015 | prefer |
| DeltaKronecker-all | 0.639 | 0.56 | 91 | 8321 | observe |
| xiaoji235-airport-v2ray-all | 0.4 | 0.75 | 4 | 3640 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4408 | observe |
| Epodonios-all | 0.255 | None | 0 | 6852 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3969 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6934 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4397 | observe |
| barry-far-vless | 0.255 | None | 0 | 4939 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5352 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| nscl5-all | 0.237 | None | 0 | 1561 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 22 |
| 204 | ProxyError | - | 19 |
| geo | TimeoutError | - | 14 |
| 204 | TimeoutError | - | 11 |
| speed | ProxyError | - | 10 |
| geo | ClientOSError | - | 7 |
| 204 | ClientOSError | - | 6 |
| cn-block | TimeoutError | - | 6 |
| cn-block | ProxyError | - | 5 |
| cn-block | ClientOSError | - | 4 |
| speed | TimeoutError | - | 2 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 280 | - |
| global | False | 300 | 292 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
