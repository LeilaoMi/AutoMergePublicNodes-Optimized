# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-14 08:21:16 |
| 运行耗时 | 195.1s |
| 订阅源总数 | 107 |
| 健康订阅源 | 44 |
| 原始节点 | 78847 |
| 去重后节点 | 23657 |
| TCP 可达 | 3000 |
| 真实可用 | 278 |
| Verified 输出 | 278 |
| Global 输出 | 290 |
| All 输出 | 23657 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.4 |
| geo | 1.3 |
| tcp | 30.6 |
| probe | 45.1 |
| real_test | 85.0 |
| generate | 25.7 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 46644 |
| trojan | 11400 |
| vmess | 10680 |
| shadowsocks | 9352 |
| hysteria2 | 457 |
| http | 135 |
| shadowsocksr | 131 |
| socks | 30 |
| hysteria | 12 |
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
| 73.63 | trojan | 293.2 | 660.7 | 20.99 | 0.0 | 10.0 | 13.46 | 18.64 | Surfboard-tg-mixed | 162.159.252.15 |
| 73.32 | shadowsocks | 321.4 | 872.6 | 20.34 | 0.0 | 10.0 | 14.32 | 13.16 | mheidari-all | 108.181.57.93 |
| 72.53 | shadowsocks | 224.9 | 621.8 | 22.57 | 0.0 | 10.0 | 14.32 | 9.64 | Au1rxx-base64 | 37.19.198.244 |
| 72.42 | trojan | 374.3 | 595.6 | 19.11 | 0.0 | 10.0 | 13.46 | 18.64 | Surfboard-tg-mixed | 199.232.78.140 |
| 72.34 | shadowsocks | 233.0 | 641.9 | 22.38 | 0.0 | 10.0 | 14.32 | 9.64 | Au1rxx-base64 | 37.19.198.243 |
| 72.3 | shadowsocks | 235.1 | 649.3 | 22.34 | 0.0 | 10.0 | 14.32 | 9.64 | Au1rxx-base64 | 37.19.198.160 |
| 71.71 | shadowsocks | 360.0 | 885.4 | 19.45 | 0.0 | 10.0 | 14.32 | 13.16 | mheidari-all | 185.196.61.82 |
| 71.55 | trojan | 448.7 | 782.3 | 17.39 | 0.0 | 10.0 | 13.46 | 18.64 | Surfboard-tg-mixed | 104.17.121.71 |
| 71.44 | trojan | 449.7 | 773.1 | 17.37 | 0.0 | 10.0 | 13.46 | 18.64 | Surfboard-tg-mixed | 104.19.64.105 |
| 70.61 | trojan | 345.0 | 588.8 | 19.79 | 0.0 | 10.0 | 13.46 | 18.64 | Surfboard-tg-mixed | 172.64.53.65 |
| 69.98 | trojan | 350.2 | 628.1 | 19.67 | 0.0 | 10.0 | 13.46 | 15.0 | DeltaKronecker-all | 5.10.215.9 |
| 69.92 | shadowsocks | 414.7 | 743.9 | 18.18 | 0.0 | 10.0 | 14.32 | 18.64 | Surfboard-tg-mixed | 57.129.121.230 |
| 69.8 | trojan | 505.1 | 834.5 | 16.09 | 0.0 | 10.0 | 13.46 | 18.64 | Surfboard-tg-mixed | 45.130.125.162 |
| 69.19 | shadowsocks | 452.2 | 856.7 | 17.31 | 0.0 | 10.0 | 14.32 | 18.64 | Surfboard-tg-mixed | 137.74.119.18 |
| 69.07 | shadowsocks | 436.5 | 682.4 | 17.67 | 0.0 | 10.0 | 14.32 | 18.64 | Surfboard-tg-mixed | 209.46.102.22 |
| 68.99 | shadowsocks | 470.3 | 916.9 | 16.89 | 0.0 | 10.0 | 14.32 | 18.64 | Surfboard-tg-mixed | 82.38.31.29 |
| 68.98 | trojan | 494.3 | 523.9 | 16.34 | 0.0 | 10.0 | 13.46 | 18.64 | Surfboard-tg-mixed | 104.17.122.62 |
| 68.98 | trojan | 523.1 | 841.6 | 15.67 | 0.0 | 10.0 | 13.46 | 18.64 | Surfboard-tg-mixed | 172.64.147.227 |
| 68.95 | trojan | 329.5 | 747.8 | 20.15 | 0.0 | 10.0 | 13.46 | 13.16 | mheidari-all | 64.94.95.118 |
| 68.72 | shadowsocks | 481.7 | 906.8 | 16.63 | 0.0 | 10.0 | 14.32 | 18.64 | Surfboard-tg-mixed | 82.38.31.32 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| Surfboard-tg-mixed | 0.796 | 0.72 | 107 | 5561 | prefer |
| DeltaKronecker-all | 0.733 | 0.655 | 148 | 7942 | prefer |
| mheidari-all | 0.638 | 0.559 | 111 | 18314 | observe |
| Au1rxx-base64 | 0.404 | 1.0 | 4 | 103 | observe |
| xiaoji235-airport-v2ray-all | 0.391 | 1.0 | 2 | 3836 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4019 | observe |
| Epodonios-all | 0.255 | None | 0 | 6471 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3972 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6406 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4279 | observe |
| barry-far-vless | 0.255 | None | 0 | 4826 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5405 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| nscl5-all | 0.231 | None | 0 | 1412 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 51 |
| speed | TimeoutError | - | 17 |
| 204 | TimeoutError | - | 15 |
| speed | ClientOSError | - | 14 |
| geo | ClientOSError | - | 8 |
| cn-block | ClientOSError | - | 8 |
| 204 | ProxyError | - | 5 |
| cn-block | TimeoutError | - | 5 |
| 204 | ClientOSError | - | 5 |
| geo | status | 403 | 1 |
| cn-block | ProxyError | - | 1 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 278 | - |
| global | False | 300 | 290 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
