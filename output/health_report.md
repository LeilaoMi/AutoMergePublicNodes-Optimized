# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-16 19:24:22 |
| 运行耗时 | 223.4s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 79788 |
| 去重后节点 | 24632 |
| TCP 可达 | 3000 |
| 真实可用 | 411 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 24632 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.8 |
| geo | 0.9 |
| tcp | 33.2 |
| probe | 48.8 |
| real_test | 93.3 |
| generate | 42.4 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 46496 |
| trojan | 12184 |
| vmess | 10857 |
| shadowsocks | 9698 |
| hysteria2 | 275 |
| shadowsocksr | 127 |
| http | 97 |
| socks | 40 |
| hysteria | 10 |
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
| 80.1 | shadowsocks | 226.9 | 614.4 | 22.53 | 0.0 | 10.0 | 13.09 | 18.48 | mheidari-all | 147.90.234.133 |
| 79.75 | shadowsocks | 226.1 | 623.8 | 22.54 | 0.0 | 10.0 | 13.09 | 18.12 | Au1rxx-base64 | 37.19.198.160 |
| 79.58 | shadowsocks | 233.4 | 639.7 | 22.37 | 0.0 | 10.0 | 13.09 | 18.12 | Au1rxx-base64 | 37.19.198.236 |
| 78.8 | shadowsocks | 245.8 | 660.5 | 22.09 | 0.0 | 10.0 | 13.09 | 18.12 | Au1rxx-base64 | 108.181.57.93 |
| 78.63 | shadowsocks | 274.8 | 765.8 | 21.42 | 0.0 | 10.0 | 13.09 | 18.12 | Au1rxx-base64 | 37.19.198.243 |
| 76.27 | shadowsocks | 291.8 | 696.5 | 21.02 | 0.0 | 10.0 | 13.09 | 18.12 | Au1rxx-base64 | 185.196.61.82 |
| 75.55 | shadowsocks | 343.1 | 898.1 | 19.84 | 0.0 | 10.0 | 13.09 | 18.12 | Au1rxx-base64 | 50.114.177.235 |
| 75.47 | vmess | 379.6 | 1086.4 | 18.99 | 0.0 | 10.0 | 12.5 | 18.48 | mheidari-all | 67.220.95.3 |
| 75.03 | shadowsocks | 408.5 | 1103.7 | 18.32 | 0.0 | 10.0 | 13.09 | 18.12 | Au1rxx-base64 | 68.168.222.210 |
| 74.85 | trojan | 385.2 | 905.4 | 18.86 | 0.0 | 10.0 | 13.75 | 18.48 | mheidari-all | 64.94.95.118 |
| 73.63 | shadowsocks | 274.5 | 755.7 | 21.42 | 0.0 | 10.0 | 13.09 | 18.12 | Au1rxx-base64 | 37.19.198.244 |
| 71.94 | shadowsocks | 316.5 | 578.7 | 20.45 | 0.0 | 10.0 | 13.09 | 18.12 | Au1rxx-base64 | 173.244.56.9 |
| 71.81 | shadowsocks | 320.8 | 565.9 | 20.35 | 0.0 | 10.0 | 13.09 | 18.12 | Au1rxx-base64 | 173.244.56.6 |
| 71.68 | shadowsocks | 225.7 | 604.1 | 22.55 | 0.0 | 10.0 | 13.09 | 18.48 | mheidari-all | 198.98.53.130 |
| 71.57 | shadowsocks | 325.1 | 572.7 | 20.25 | 0.0 | 10.0 | 13.09 | 18.12 | Au1rxx-base64 | 108.181.0.177 |
| 71.3 | shadowsocks | 286.7 | 660.7 | 21.14 | 0.0 | 10.0 | 13.09 | 18.12 | Au1rxx-base64 | 156.146.38.168 |
| 70.94 | trojan | 401.5 | 554.0 | 18.48 | 0.0 | 10.0 | 13.75 | 17.98 | Surfboard-tg-mixed | 104.21.48.168 |
| 70.93 | trojan | 405.7 | 603.9 | 18.39 | 0.0 | 10.0 | 13.75 | 17.98 | Surfboard-tg-mixed | 104.16.71.48 |
| 70.84 | shadowsocks | 338.4 | 602.2 | 19.94 | 0.0 | 10.0 | 13.09 | 18.12 | Au1rxx-base64 | 108.181.118.10 |
| 70.76 | shadowsocks | 295.2 | 674.8 | 20.94 | 0.0 | 10.0 | 13.09 | 18.12 | Au1rxx-base64 | 156.146.38.170 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| Au1rxx-base64 | 0.925 | 0.928 | 97 | 149 | prefer |
| mheidari-all | 0.863 | 0.787 | 127 | 16694 | prefer |
| Surfboard-tg-mixed | 0.771 | 0.696 | 92 | 5554 | prefer |
| DeltaKronecker-all | 0.668 | 0.589 | 202 | 8462 | observe |
| xiaoji235-airport-v2ray-all | 0.325 | 1.0 | 1 | 1757 | observe |
| nscl5-all | 0.316 | 1.0 | 1 | 1519 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4470 | observe |
| Epodonios-all | 0.255 | None | 0 | 6586 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3974 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7013 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4319 | observe |
| barry-far-vless | 0.255 | None | 0 | 4954 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5260 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | TimeoutError | - | 37 |
| geo | TimeoutError | - | 35 |
| speed | ClientOSError | - | 20 |
| cn-block | TimeoutError | - | 19 |
| 204 | ProxyError | - | 10 |
| 204 | ClientOSError | - | 7 |
| cn-block | ClientOSError | - | 5 |
| cn-block | ProxyError | - | 4 |
| speed | TimeoutError | - | 4 |
| speed | ProxyError | - | 4 |
| geo | ClientOSError | - | 1 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
