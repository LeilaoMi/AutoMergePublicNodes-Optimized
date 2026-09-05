# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-05 03:58:21 |
| 运行耗时 | 314.9s |
| 订阅源总数 | 107 |
| 健康订阅源 | 96 |
| 原始节点 | 84346 |
| 去重后节点 | 23686 |
| TCP 可达 | 3000 |
| 真实可用 | 647 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23686 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.8 |
| geo | 1.5 |
| tcp | 39.2 |
| probe | 87.9 |
| real_test | 143.4 |
| generate | 37.1 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 53163 |
| vmess | 11482 |
| shadowsocks | 9883 |
| trojan | 8065 |
| hysteria2 | 1401 |
| http | 149 |
| shadowsocksr | 126 |
| socks | 52 |
| tuic | 14 |
| hysteria | 10 |
| anytls | 1 |

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
| 81.04 | http | 248.5 | 561.1 | 22.03 | 0.0 | 10.0 | 14.5 | 19.24 | zhangkai | 138.199.35.198 |
| 80.87 | http | 246.6 | 553.9 | 22.07 | 0.0 | 10.0 | 14.5 | 19.24 | zhangkai | 138.199.35.216 |
| 80.21 | trojan | 244.1 | 596.1 | 22.13 | 0.0 | 10.0 | 12.78 | 18.3 | Au1rxx-base64 | 64.94.95.115 |
| 80.16 | trojan | 246.2 | 599.7 | 22.08 | 0.0 | 10.0 | 12.78 | 18.3 | Au1rxx-base64 | 64.94.95.118 |
| 80.11 | trojan | 248.4 | 599.8 | 22.03 | 0.0 | 10.0 | 12.78 | 18.3 | Au1rxx-base64 | 64.94.95.117 |
| 79.89 | shadowsocks | 232.7 | 585.9 | 22.39 | 0.0 | 10.0 | 13.2 | 18.3 | Au1rxx-base64 | 156.146.38.169 |
| 79.69 | shadowsocks | 241.6 | 618.1 | 22.19 | 0.0 | 10.0 | 13.2 | 18.3 | Au1rxx-base64 | 156.146.38.170 |
| 79.64 | shadowsocks | 243.6 | 614.1 | 22.14 | 0.0 | 10.0 | 13.2 | 18.3 | Au1rxx-base64 | 156.146.38.167 |
| 78.58 | vless | 324.0 | 586.6 | 20.28 | 0.0 | 10.0 | 11.5 | 18.3 | Au1rxx-base64 | 38.180.242.205 |
| 78.43 | vless | 268.5 | 557.7 | 21.56 | 0.0 | 10.0 | 11.5 | 18.3 | Au1rxx-base64 | 172.233.139.46 |
| 77.7 | vless | 273.0 | 561.9 | 21.46 | 0.0 | 10.0 | 11.5 | 18.3 | Au1rxx-base64 | 172.235.38.85 |
| 77.56 | shadowsocks | 242.9 | 622.8 | 22.16 | 0.0 | 10.0 | 13.2 | 16.2 | Surfboard-tg-mixed | 156.146.38.168 |
| 77.08 | shadowsocks | 263.0 | 612.9 | 21.69 | 0.0 | 10.0 | 13.2 | 18.3 | Au1rxx-base64 | 23.150.248.20 |
| 76.71 | vless | 292.9 | 631.0 | 21.0 | 0.0 | 10.0 | 11.5 | 18.3 | Au1rxx-base64 | 38.127.121.44 |
| 75.55 | trojan | 249.2 | 599.8 | 22.01 | 0.0 | 10.0 | 12.78 | 18.3 | Au1rxx-base64 | 64.94.95.114 |
| 75.5 | vless | 340.4 | 718.4 | 19.9 | 0.0 | 10.0 | 11.5 | 18.3 | Au1rxx-base64 | 138.124.60.146 |
| 75.34 | hysteria2 | 453.5 | 1084.1 | 17.28 | 0.0 | 10.0 | 13.12 | 17.64 | mheidari-all | 66.94.121.46 |
| 75.31 | vless | 350.9 | 763.2 | 19.65 | 0.0 | 10.0 | 11.5 | 18.3 | Au1rxx-base64 | 216.152.147.28 |
| 74.72 | vless | 410.4 | 1004.2 | 18.28 | 0.0 | 10.0 | 11.5 | 18.3 | Au1rxx-base64 | 45.138.100.226 |
| 74.59 | vless | 365.7 | 758.9 | 19.31 | 0.0 | 10.0 | 11.5 | 18.3 | Au1rxx-base64 | 23.237.192.18 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.993 | 0.923 | 389 | 1796 | prefer |
| zhangkai | 0.881 | 0.909 | 22 | 144 | prefer |
| Surfboard-tg-mixed | 0.874 | 0.8 | 100 | 7291 | prefer |
| mheidari-all | 0.728 | 0.65 | 217 | 16194 | prefer |
| tg-oneclickvpnkeys | 0.554 | 1.0 | 8 | 135 | observe |
| DeltaKronecker-all | 0.269 | 0.186 | 210 | 7089 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 8350 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 6083 | observe |
| barry-far-vless | 0.255 | None | 0 | 6282 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4095 | observe |
| Au1rxx-clash | 0.247 | None | 0 | 1796 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |
| 10ium-HighSpeed | 0.209 | None | 0 | 839 | observe |
| 10ium-ScrapeCategorize-Vless | 0.207 | 0.0 | 1 | 4810 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 159 |
| geo | ClientOSError | - | 51 |
| speed | TimeoutError | - | 37 |
| speed | ClientOSError | - | 20 |
| 204 | TimeoutError | - | 14 |
| cn-block | ClientOSError | - | 9 |
| cn-block | TimeoutError | - | 7 |
| 204 | ProxyError | - | 4 |
| 204 | ProxyConnectionError | - | 2 |
| cn-block | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
