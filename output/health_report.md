# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-05 19:29:26 |
| 运行耗时 | 210.6s |
| 订阅源总数 | 107 |
| 健康订阅源 | 102 |
| 原始节点 | 78323 |
| 去重后节点 | 24054 |
| TCP 可达 | 3000 |
| 真实可用 | 278 |
| Verified 输出 | 278 |
| Global 输出 | 292 |
| All 输出 | 24054 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.8 |
| geo | 1.3 |
| tcp | 31.0 |
| probe | 48.5 |
| real_test | 81.0 |
| generate | 44.1 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 45125 |
| trojan | 12653 |
| vmess | 10395 |
| shadowsocks | 9334 |
| hysteria2 | 477 |
| shadowsocksr | 148 |
| http | 135 |
| socks | 43 |
| tuic | 7 |
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
| 78.33 | shadowsocks | 228.5 | 633.1 | 22.49 | 0.0 | 10.0 | 12.98 | 16.86 | Au1rxx-base64 | 37.19.198.160 |
| 78.17 | shadowsocks | 235.5 | 653.0 | 22.33 | 0.0 | 10.0 | 12.98 | 16.86 | Au1rxx-base64 | 37.19.198.243 |
| 78.1 | shadowsocks | 238.2 | 663.9 | 22.26 | 0.0 | 10.0 | 12.98 | 16.86 | Au1rxx-base64 | 37.19.198.236 |
| 77.84 | shadowsocks | 250.4 | 661.1 | 21.98 | 0.0 | 10.0 | 12.98 | 17.38 | mheidari-all | 108.181.57.93 |
| 77.4 | shadowsocks | 268.6 | 747.8 | 21.56 | 0.0 | 10.0 | 12.98 | 16.86 | Au1rxx-base64 | 37.19.198.244 |
| 77.28 | shadowsocks | 296.3 | 825.3 | 20.92 | 0.0 | 10.0 | 12.98 | 17.38 | mheidari-all | 147.90.234.133 |
| 76.72 | shadowsocks | 297.9 | 818.2 | 20.88 | 0.0 | 10.0 | 12.98 | 16.86 | Au1rxx-base64 | tinkered-pennies-puppies.freesocks.work |
| 74.62 | trojan | 339.4 | 752.9 | 19.92 | 0.0 | 10.0 | 12.7 | 17.24 | DeltaKronecker-all | 45.32.195.168 |
| 74.54 | shadowsocks | 281.5 | 652.2 | 21.26 | 0.0 | 10.0 | 12.98 | 16.86 | Au1rxx-base64 | 156.146.38.169 |
| 74.5 | shadowsocks | 286.4 | 660.9 | 21.15 | 0.0 | 10.0 | 12.98 | 16.86 | Au1rxx-base64 | 156.146.38.168 |
| 73.93 | vmess | 389.1 | 1097.7 | 18.77 | 0.0 | 10.0 | 12.5 | 17.16 | Surfboard-tg-mixed | 67.220.95.3 |
| 73.67 | shadowsocks | 348.4 | 876.5 | 19.71 | 0.0 | 10.0 | 12.98 | 17.38 | mheidari-all | 185.196.61.82 |
| 73.51 | trojan | 362.9 | 746.5 | 19.38 | 0.0 | 10.0 | 12.7 | 17.24 | DeltaKronecker-all | 149.28.241.235 |
| 73.29 | shadowsocks | 329.6 | 793.7 | 20.15 | 0.0 | 10.0 | 12.98 | 16.86 | Au1rxx-base64 | 156.146.38.167 |
| 71.08 | shadowsocks | 313.8 | 582.1 | 20.51 | 0.0 | 10.0 | 12.98 | 16.86 | Au1rxx-base64 | 173.244.56.9 |
| 71.06 | vless | 267.7 | 663.5 | 21.58 | 0.0 | 10.0 | 3.24 | 17.24 | DeltaKronecker-all | 162.159.252.15 |
| 70.6 | trojan | 317.6 | 733.8 | 20.43 | 0.0 | 10.0 | 12.7 | 17.24 | DeltaKronecker-all | 64.94.95.115 |
| 70.49 | shadowsocks | 327.8 | 628.3 | 20.19 | 0.0 | 10.0 | 12.98 | 16.86 | Au1rxx-base64 | 149.22.95.183 |
| 70.27 | trojan | 320.1 | 740.0 | 20.37 | 0.0 | 10.0 | 12.7 | 17.24 | DeltaKronecker-all | 64.94.95.117 |
| 70.25 | shadowsocks | 321.3 | 577.2 | 20.34 | 0.0 | 10.0 | 12.98 | 16.86 | Au1rxx-base64 | 108.181.0.177 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| Surfboard-tg-mixed | 0.842 | 0.768 | 82 | 5733 | prefer |
| Au1rxx-base64 | 0.825 | 0.846 | 26 | 91 | prefer |
| mheidari-all | 0.787 | 0.711 | 97 | 16129 | prefer |
| DeltaKronecker-all | 0.771 | 0.694 | 121 | 7739 | prefer |
| nscl5-all | 0.411 | 1.0 | 3 | 1323 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4662 | observe |
| Epodonios-all | 0.255 | None | 0 | 7047 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6940 | observe |
| barry-far-vless | 0.255 | None | 0 | 4982 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5372 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| xiaoji235-airport-v2ray-all | 0.227 | None | 0 | 1288 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 19 |
| 204 | ProxyError | - | 16 |
| geo | TimeoutError | - | 11 |
| 204 | ClientOSError | - | 10 |
| cn-block | ClientOSError | - | 7 |
| cn-block | TimeoutError | - | 7 |
| geo | ClientOSError | - | 5 |
| 204 | TimeoutError | - | 4 |
| speed | TimeoutError | - | 3 |
| geo | ProxyError | - | 3 |
| speed | ProxyError | - | 3 |
| cn-block | ProxyError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 278 | - |
| global | False | 300 | 292 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
