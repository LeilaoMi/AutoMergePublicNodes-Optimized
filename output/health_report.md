# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-09 13:05:47 |
| 运行耗时 | 236.0s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 85362 |
| 去重后节点 | 23924 |
| TCP 可达 | 3000 |
| 真实可用 | 483 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23924 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.0 |
| geo | 1.4 |
| tcp | 36.0 |
| probe | 51.3 |
| real_test | 112.5 |
| generate | 28.8 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 51086 |
| vmess | 13124 |
| trojan | 9934 |
| shadowsocks | 9540 |
| hysteria2 | 1440 |
| socks | 75 |
| shadowsocksr | 70 |
| http | 39 |
| anytls | 26 |
| hysteria | 16 |
| tuic | 12 |

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
| 83.67 | trojan | 212.8 | 517.3 | 22.85 | 0.0 | 9.11 | 14.55 | 19.66 | Au1rxx-base64 | 44.244.3.114 |
| 83.48 | trojan | 220.0 | 525.3 | 22.68 | 0.0 | 9.09 | 14.55 | 19.66 | Au1rxx-base64 | 44.242.235.129 |
| 82.62 | trojan | 258.0 | 653.9 | 21.81 | 0.0 | 9.1 | 14.55 | 19.66 | Au1rxx-base64 | 44.246.163.102 |
| 81.85 | trojan | 310.2 | 810.0 | 20.6 | 0.0 | 9.54 | 14.55 | 19.66 | Au1rxx-base64 | 35.86.90.51 |
| 81.66 | shadowsocks | 208.7 | 565.7 | 22.95 | 0.0 | 9.31 | 13.74 | 19.66 | Au1rxx-base64 | 149.22.95.183 |
| 81.44 | trojan | 201.0 | 479.9 | 23.13 | 0.0 | 8.79 | 14.55 | 19.66 | Au1rxx-base64 | devoted-tapir.rooster465.autos |
| 79.22 | http | 263.4 | 561.7 | 21.68 | 0.0 | 10.0 | 14.38 | 19.12 | zhangkai | 138.199.35.214 |
| 79.21 | vless | 248.3 | 523.9 | 22.03 | 0.0 | 10.0 | 9.13 | 19.66 | Au1rxx-base64 | 186.241.106.97 |
| 78.8 | shadowsocks | 256.2 | 265.7 | 21.85 | 5.04 | 9.48 | 13.74 | 19.66 | Au1rxx-base64 | 149.22.87.204 |
| 78.47 | vless | 241.8 | 525.1 | 22.18 | 0.0 | 10.0 | 9.13 | 19.66 | Au1rxx-base64 | 179.255.148.66 |
| 78.21 | trojan | 196.6 | 472.0 | 23.23 | 0.0 | 3.27 | 14.55 | 19.66 | Au1rxx-base64 | natural-collie.rooster465.autos |
| 78.19 | trojan | 198.0 | 471.1 | 23.2 | 0.0 | 3.28 | 14.55 | 19.66 | Au1rxx-base64 | pet-ghost.rooster465.autos |
| 78.17 | trojan | 200.0 | 475.2 | 23.15 | 0.0 | 3.31 | 14.55 | 19.66 | Au1rxx-base64 | fleet-bonefish.rooster465.autos |
| 78.16 | trojan | 308.9 | 312.7 | 20.63 | 3.27 | 9.96 | 14.55 | 19.66 | Au1rxx-base64 | 18.181.164.216 |
| 78.06 | vless | 248.5 | 538.6 | 22.03 | 0.0 | 10.0 | 9.13 | 19.66 | Au1rxx-base64 | 179.253.240.24 |
| 78.0 | http | 264.1 | 568.8 | 21.67 | 0.0 | 10.0 | 14.38 | 19.12 | zhangkai | 138.199.35.199 |
| 77.87 | vless | 268.1 | 602.3 | 21.57 | 0.0 | 9.1 | 9.13 | 19.66 | Au1rxx-base64 | 107.173.237.146 |
| 77.71 | trojan | 315.7 | 321.0 | 20.47 | 2.96 | 9.97 | 14.55 | 19.66 | Au1rxx-base64 | 43.207.155.134 |
| 77.65 | hysteria2 | 341.2 | 714.3 | 19.88 | 0.0 | 9.12 | 13.89 | 19.66 | Au1rxx-base64 | 159.223.157.129 |
| 77.58 | http | 265.6 | 571.4 | 21.63 | 0.0 | 10.0 | 14.38 | 19.12 | zhangkai | 138.199.35.217 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.989 | 0.923 | 403 | 1704 | prefer |
| zhangkai | 0.956 | 1.0 | 20 | 25 | prefer |
| Surfboard-tg-mixed | 0.778 | 0.702 | 104 | 6480 | prefer |
| mheidari-all | 0.33 | 0.243 | 70 | 20170 | observe |
| tg-oneclickvpnkeys | 0.258 | 1.0 | 1 | 77 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5505 | observe |
| Epodonios-all | 0.255 | None | 0 | 7128 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7369 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5320 | observe |
| barry-far-vless | 0.255 | None | 0 | 5659 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5130 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.243 | None | 0 | 1704 | observe |
| nscl5-all | 0.235 | None | 0 | 1506 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | ClientOSError | - | 25 |
| 204 | TimeoutError | - | 21 |
| speed | TimeoutError | - | 17 |
| 204 | ProxyError | - | 15 |
| cn-block | TimeoutError | - | 13 |
| speed | ClientOSError | - | 11 |
| geo | TimeoutError | - | 8 |
| cn-block | ClientOSError | - | 4 |
| cn-block | ProxyError | - | 1 |
| speed | ProxyError | - | 1 |
| 204 | ClientOSError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
