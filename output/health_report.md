# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-07 00:11:56 |
| 运行耗时 | 300.5s |
| 订阅源总数 | 107 |
| 健康订阅源 | 102 |
| 原始节点 | 88824 |
| 去重后节点 | 24625 |
| TCP 可达 | 3000 |
| 真实可用 | 499 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 24625 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.0 |
| geo | 1.3 |
| tcp | 37.2 |
| probe | 60.7 |
| real_test | 142.5 |
| generate | 52.8 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 51651 |
| vmess | 13327 |
| trojan | 11854 |
| shadowsocks | 10223 |
| hysteria2 | 1478 |
| socks | 129 |
| shadowsocksr | 72 |
| anytls | 30 |
| http | 25 |
| hysteria | 21 |
| tuic | 14 |

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
| 84.46 | trojan | 218.1 | 486.5 | 22.73 | 0.0 | 10.0 | 14.63 | 20.0 | Au1rxx-base64 | 35.91.251.124 |
| 84.04 | trojan | 232.5 | 525.8 | 22.4 | 0.0 | 9.51 | 14.63 | 20.0 | Au1rxx-base64 | fleet-bonefish.rooster465.autos |
| 83.75 | http | 192.8 | 495.7 | 23.31 | 0.0 | 10.0 | 14.32 | 19.12 | zhangkai | 138.199.35.214 |
| 83.73 | trojan | 223.3 | 504.4 | 22.61 | 0.0 | 9.4 | 14.63 | 20.0 | Au1rxx-base64 | sincere-gelding.rooster465.autos |
| 83.7 | http | 195.2 | 499.5 | 23.26 | 0.0 | 10.0 | 14.32 | 19.12 | zhangkai | 138.199.35.217 |
| 83.68 | http | 196.0 | 502.8 | 23.24 | 0.0 | 10.0 | 14.32 | 19.12 | zhangkai | 138.199.35.207 |
| 83.51 | http | 203.2 | 467.2 | 23.07 | 0.0 | 10.0 | 14.32 | 19.12 | zhangkai | 138.199.35.199 |
| 83.4 | trojan | 237.7 | 549.1 | 22.27 | 0.0 | 10.0 | 14.63 | 20.0 | Au1rxx-base64 | 35.86.90.51 |
| 83.3 | trojan | 234.2 | 533.1 | 22.36 | 0.0 | 9.27 | 14.63 | 20.0 | Au1rxx-base64 | natural-collie.rooster465.autos |
| 82.98 | trojan | 227.6 | 477.3 | 22.51 | 0.0 | 10.0 | 14.63 | 20.0 | Au1rxx-base64 | devoted-tapir.rooster465.autos |
| 82.93 | trojan | 233.9 | 525.9 | 22.36 | 0.0 | 9.71 | 14.63 | 20.0 | Au1rxx-base64 | pet-ghost.rooster465.autos |
| 82.81 | trojan | 278.1 | 668.8 | 21.34 | 0.0 | 10.0 | 14.63 | 20.0 | Au1rxx-base64 | 44.244.3.114 |
| 82.8 | trojan | 280.5 | 671.5 | 21.28 | 0.0 | 10.0 | 14.63 | 20.0 | Au1rxx-base64 | 44.246.163.102 |
| 81.77 | trojan | 320.6 | 790.3 | 20.36 | 0.0 | 10.0 | 14.63 | 20.0 | Au1rxx-base64 | 44.242.235.129 |
| 81.71 | shadowsocks | 218.4 | 531.7 | 22.72 | 0.0 | 10.0 | 13.49 | 20.0 | Au1rxx-base64 | 108.181.0.177 |
| 81.56 | shadowsocks | 246.7 | 603.3 | 22.07 | 0.0 | 10.0 | 13.49 | 20.0 | Au1rxx-base64 | 149.22.95.183 |
| 81.43 | shadowsocks | 230.6 | 582.5 | 22.44 | 0.0 | 10.0 | 13.49 | 20.0 | Au1rxx-base64 | 108.181.118.10 |
| 81.05 | shadowsocks | 268.4 | 638.6 | 21.56 | 0.0 | 10.0 | 13.49 | 20.0 | Au1rxx-base64 | 173.244.56.6 |
| 79.07 | shadowsocks | 267.8 | 634.5 | 21.58 | 0.0 | 10.0 | 13.49 | 20.0 | Au1rxx-base64 | 173.244.56.9 |
| 78.49 | trojan | 314.3 | 688.8 | 20.5 | 0.0 | 10.0 | 14.63 | 20.0 | Au1rxx-base64 | 64.94.95.118 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.986 | 0.936 | 328 | 1327 | prefer |
| zhangkai | 0.958 | 1.0 | 21 | 25 | prefer |
| Surfboard-tg-mixed | 0.541 | 0.46 | 202 | 5904 | observe |
| xiaoji235-airport-v2ray-all | 0.349 | 0.667 | 3 | 5184 | observe |
| nscl5-all | 0.32 | 1.0 | 1 | 1621 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| DeltaKronecker-all | 0.259 | 0.162 | 37 | 5897 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5219 | observe |
| Epodonios-all | 0.255 | None | 0 | 6481 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3996 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7217 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4729 | observe |
| barry-far-vless | 0.255 | None | 0 | 5041 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5225 | observe |
| mheidari-all | 0.254 | 0.173 | 394 | 20787 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 225 |
| geo | ClientOSError | - | 82 |
| speed | TimeoutError | - | 70 |
| speed | ClientOSError | - | 59 |
| cn-block | TimeoutError | - | 16 |
| 204 | TimeoutError | - | 13 |
| cn-block | ProxyError | - | 9 |
| geo | ProxyError | - | 4 |
| 204 | ProxyError | - | 4 |
| 204 | ClientOSError | - | 2 |
| cn-block | ClientOSError | - | 2 |
| speed | ProxyError | - | 2 |
| speed | ClientPayloadError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
