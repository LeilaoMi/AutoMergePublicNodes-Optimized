# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-23 18:41:17 |
| 运行耗时 | 300.3s |
| 订阅源总数 | 107 |
| 健康订阅源 | 97 |
| 原始节点 | 77715 |
| 去重后节点 | 21484 |
| TCP 可达 | 3000 |
| 真实可用 | 644 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 21484 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 17.3 |
| geo | 1.2 |
| tcp | 34.7 |
| probe | 58.1 |
| real_test | 142.6 |
| generate | 46.3 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 47971 |
| shadowsocks | 10225 |
| vmess | 10110 |
| trojan | 7824 |
| hysteria2 | 1182 |
| http | 165 |
| shadowsocksr | 129 |
| socks | 100 |
| hysteria | 7 |
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
| 85.0 | http | 198.2 | 517.1 | 23.19 | 0.0 | 10.0 | 14.87 | 19.94 | zhangkai | 138.199.35.198 |
| 84.98 | http | 198.9 | 510.3 | 23.17 | 0.0 | 10.0 | 14.87 | 19.94 | zhangkai | 138.199.35.216 |
| 84.46 | vless | 233.2 | 582.2 | 22.38 | 0.0 | 10.0 | 12.36 | 19.72 | Au1rxx-base64 | 15.204.97.209 |
| 82.8 | vless | 304.9 | 805.4 | 20.72 | 0.0 | 10.0 | 12.36 | 19.72 | Au1rxx-base64 | 15.204.97.216 |
| 82.59 | vless | 314.1 | 829.4 | 20.51 | 0.0 | 10.0 | 12.36 | 19.72 | Au1rxx-base64 | 15.204.97.197 |
| 82.44 | vless | 320.3 | 845.9 | 20.36 | 0.0 | 10.0 | 12.36 | 19.72 | Au1rxx-base64 | 15.204.97.214 |
| 82.37 | vless | 266.3 | 549.4 | 21.61 | 0.0 | 10.0 | 12.36 | 19.72 | Au1rxx-base64 | 150.241.82.19 |
| 82.35 | shadowsocks | 216.0 | 527.2 | 22.78 | 0.0 | 10.0 | 13.85 | 19.72 | Au1rxx-base64 | 94.72.127.55 |
| 81.82 | shadowsocks | 217.3 | 538.6 | 22.75 | 0.0 | 10.0 | 13.85 | 19.72 | Au1rxx-base64 | 108.181.0.177 |
| 81.75 | shadowsocks | 230.9 | 567.9 | 22.43 | 0.0 | 10.0 | 13.85 | 19.72 | Au1rxx-base64 | 154.12.240.141 |
| 81.65 | trojan | 231.1 | 518.6 | 22.43 | 0.0 | 10.0 | 12.0 | 19.72 | Au1rxx-base64 | 44.251.158.80 |
| 81.57 | vless | 228.6 | 596.1 | 22.49 | 0.0 | 10.0 | 12.36 | 19.72 | Au1rxx-base64 | 38.244.21.147 |
| 81.51 | vless | 360.7 | 969.1 | 19.43 | 0.0 | 10.0 | 12.36 | 19.72 | Au1rxx-base64 | 15.204.97.195 |
| 81.49 | trojan | 238.1 | 551.7 | 22.27 | 0.0 | 10.0 | 12.0 | 19.72 | Au1rxx-base64 | 35.91.251.124 |
| 81.37 | shadowsocks | 194.4 | 471.8 | 23.28 | 0.0 | 10.0 | 13.85 | 18.74 | mheidari-all | 108.181.118.10 |
| 80.49 | vless | 188.6 | 492.6 | 23.41 | 0.0 | 10.0 | 12.36 | 19.72 | Au1rxx-base64 | 154.17.224.207 |
| 80.49 | vless | 188.8 | 489.2 | 23.41 | 0.0 | 10.0 | 12.36 | 19.72 | Au1rxx-base64 | 192.220.55.133 |
| 80.18 | vless | 202.2 | 531.2 | 23.1 | 0.0 | 10.0 | 12.36 | 19.72 | Au1rxx-base64 | 154.23.242.116 |
| 80.16 | vless | 203.1 | 533.5 | 23.08 | 0.0 | 10.0 | 12.36 | 19.72 | Au1rxx-base64 | 154.23.242.96 |
| 80.09 | trojan | 231.2 | 521.8 | 22.43 | 0.0 | 8.44 | 12.0 | 19.72 | Au1rxx-base64 | neutral-quail.rooster465.autos |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.997 | 1.0 | 112 | 144 | prefer |
| Au1rxx-base64 | 0.979 | 0.912 | 398 | 1729 | prefer |
| Surfboard-tg-mixed | 0.817 | 0.74 | 131 | 6307 | prefer |
| mheidari-all | 0.77 | 0.696 | 69 | 14516 | prefer |
| DeltaKronecker-all | 0.498 | 0.415 | 53 | 5415 | observe |
| nscl5-all | 0.298 | 1.0 | 1 | 1082 | observe |
| tg-LonUp_M | 0.262 | 1.0 | 1 | 177 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4989 | observe |
| Epodonios-all | 0.255 | None | 0 | 6871 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3988 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6995 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5215 | observe |
| barry-far-vless | 0.255 | None | 0 | 5492 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4085 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 22 |
| 204 | TimeoutError | - | 21 |
| geo | ClientOSError | - | 17 |
| cn-block | TimeoutError | - | 17 |
| speed | TimeoutError | - | 15 |
| 204 | ProxyError | - | 10 |
| speed | ClientOSError | - | 7 |
| cn-block | ClientOSError | - | 6 |
| 204 | ClientOSError | - | 3 |
| cn-block | ProxyError | - | 3 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
