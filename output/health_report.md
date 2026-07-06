# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-06 10:52:32 |
| 运行耗时 | 197.4s |
| 订阅源总数 | 107 |
| 健康订阅源 | 102 |
| 原始节点 | 79147 |
| 去重后节点 | 24406 |
| TCP 可达 | 3000 |
| 真实可用 | 338 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 24406 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.2 |
| geo | 1.3 |
| tcp | 31.1 |
| probe | 43.3 |
| real_test | 81.8 |
| generate | 35.7 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 45506 |
| trojan | 12944 |
| vmess | 10452 |
| shadowsocks | 9451 |
| hysteria2 | 447 |
| shadowsocksr | 148 |
| http | 139 |
| socks | 44 |
| tuic | 10 |
| hysteria | 6 |

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
| 78.8 | shadowsocks | 278.4 | 678.5 | 21.33 | 0.0 | 10.0 | 14.08 | 19.38 | mheidari-all | 108.181.57.93 |
| 78.65 | shadowsocks | 347.1 | 906.0 | 19.74 | 0.0 | 10.0 | 14.08 | 19.38 | mheidari-all | 185.196.61.82 |
| 78.54 | shadowsocks | 256.6 | 633.7 | 21.84 | 0.0 | 10.0 | 14.08 | 16.62 | Au1rxx-base64 | 156.146.38.169 |
| 78.45 | shadowsocks | 260.5 | 613.6 | 21.75 | 0.0 | 10.0 | 14.08 | 16.62 | Au1rxx-base64 | 156.146.38.168 |
| 78.42 | shadowsocks | 259.0 | 650.0 | 21.78 | 0.0 | 10.0 | 14.08 | 16.62 | Au1rxx-base64 | 156.146.38.167 |
| 77.63 | shadowsocks | 295.7 | 755.3 | 20.93 | 0.0 | 10.0 | 14.08 | 16.62 | Au1rxx-base64 | 37.19.198.236 |
| 77.55 | shadowsocks | 293.3 | 741.5 | 20.99 | 0.0 | 10.0 | 14.08 | 16.62 | Au1rxx-base64 | 37.19.198.244 |
| 77.48 | shadowsocks | 268.9 | 679.5 | 21.55 | 0.0 | 10.0 | 14.08 | 16.62 | Au1rxx-base64 | 37.19.198.243 |
| 77.45 | trojan | 300.9 | 739.0 | 20.81 | 0.0 | 10.0 | 13.74 | 15.4 | DeltaKronecker-all | 149.28.241.235 |
| 77.43 | shadowsocks | 304.5 | 768.4 | 20.73 | 0.0 | 10.0 | 14.08 | 16.62 | Au1rxx-base64 | 37.19.198.160 |
| 77.3 | trojan | 305.6 | 746.0 | 20.7 | 0.0 | 10.0 | 13.74 | 15.4 | DeltaKronecker-all | 45.32.195.168 |
| 77.0 | trojan | 298.8 | 724.4 | 20.86 | 0.0 | 10.0 | 13.74 | 15.4 | DeltaKronecker-all | 64.94.95.117 |
| 76.81 | trojan | 307.0 | 739.6 | 20.67 | 0.0 | 10.0 | 13.74 | 15.4 | DeltaKronecker-all | 64.94.95.114 |
| 75.83 | trojan | 313.2 | 774.0 | 20.53 | 0.0 | 10.0 | 13.74 | 15.4 | DeltaKronecker-all | 64.94.95.115 |
| 74.27 | shadowsocks | 254.8 | 631.2 | 21.88 | 0.0 | 10.0 | 14.08 | 19.38 | mheidari-all | 198.98.53.130 |
| 73.79 | shadowsocks | 335.7 | 841.9 | 20.01 | 0.0 | 10.0 | 14.08 | 19.38 | mheidari-all | 147.90.234.133 |
| 73.79 | shadowsocks | 476.3 | 1187.1 | 16.75 | 0.0 | 10.0 | 14.08 | 19.38 | mheidari-all | 130.51.22.8 |
| 73.45 | shadowsocks | 260.5 | 649.4 | 21.75 | 0.0 | 10.0 | 14.08 | 16.62 | Au1rxx-base64 | 156.146.38.170 |
| 73.25 | shadowsocks | 301.3 | 604.3 | 20.8 | 0.0 | 10.0 | 14.08 | 16.62 | Au1rxx-base64 | 149.22.95.183 |
| 72.81 | shadowsocks | 420.0 | 915.1 | 18.06 | 0.0 | 10.0 | 14.08 | 19.38 | mheidari-all | 172.245.235.84 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| mheidari-all | 0.911 | 0.839 | 87 | 16255 | prefer |
| Au1rxx-base64 | 0.849 | 0.867 | 30 | 120 | prefer |
| Surfboard-tg-mixed | 0.841 | 0.765 | 115 | 5925 | prefer |
| DeltaKronecker-all | 0.792 | 0.715 | 158 | 8330 | prefer |
| nscl5-all | 0.321 | 1.0 | 1 | 1651 | observe |
| ermaozi | 0.256 | 1.0 | 1 | 27 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4358 | observe |
| Epodonios-all | 0.255 | None | 0 | 6980 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6861 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4334 | observe |
| barry-far-vless | 0.255 | None | 0 | 5043 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5349 | observe |
| xiaoji235-airport-v2ray-all | 0.226 | None | 0 | 1268 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 26 |
| geo | TimeoutError | - | 23 |
| 204 | ClientOSError | - | 12 |
| geo | ClientOSError | - | 6 |
| 204 | TimeoutError | - | 6 |
| cn-block | TimeoutError | - | 6 |
| speed | TimeoutError | - | 5 |
| 204 | ProxyError | - | 3 |
| cn-block | ClientOSError | - | 3 |
| geo | ProxyError | - | 2 |
| cn-block | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
