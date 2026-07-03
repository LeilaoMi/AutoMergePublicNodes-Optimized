# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-03 19:41:17 |
| 运行耗时 | 196.4s |
| 订阅源总数 | 107 |
| 健康订阅源 | 103 |
| 原始节点 | 77772 |
| 去重后节点 | 23173 |
| TCP 可达 | 3000 |
| 真实可用 | 267 |
| Verified 输出 | 267 |
| Global 输出 | 274 |
| All 输出 | 23173 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.4 |
| geo | 1.4 |
| tcp | 30.9 |
| probe | 49.4 |
| real_test | 72.9 |
| generate | 37.5 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 45269 |
| trojan | 12318 |
| vmess | 10445 |
| shadowsocks | 9095 |
| hysteria2 | 285 |
| shadowsocksr | 148 |
| http | 135 |
| socks | 70 |
| hysteria | 6 |
| tuic | 1 |

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
| 78.31 | shadowsocks | 201.1 | 497.4 | 23.12 | 0.0 | 10.0 | 12.33 | 16.86 | Au1rxx-base64 | 173.244.56.9 |
| 77.25 | shadowsocks | 246.9 | 598.5 | 22.06 | 0.0 | 10.0 | 12.33 | 16.86 | Au1rxx-base64 | 173.244.56.6 |
| 76.93 | shadowsocks | 253.3 | 612.6 | 21.92 | 0.0 | 10.0 | 12.33 | 16.86 | Au1rxx-base64 | 156.146.38.169 |
| 76.33 | shadowsocks | 264.4 | 650.7 | 21.66 | 0.0 | 10.0 | 12.33 | 16.86 | Au1rxx-base64 | 156.146.38.167 |
| 76.33 | shadowsocks | 265.0 | 692.3 | 21.64 | 0.0 | 10.0 | 12.33 | 16.86 | Au1rxx-base64 | 108.181.0.177 |
| 76.11 | shadowsocks | 274.7 | 709.6 | 21.42 | 0.0 | 10.0 | 12.33 | 16.86 | Au1rxx-base64 | 108.181.118.10 |
| 75.85 | shadowsocks | 295.8 | 745.9 | 20.93 | 0.0 | 10.0 | 12.33 | 16.86 | Au1rxx-base64 | 156.146.38.170 |
| 73.82 | shadowsocks | 250.1 | 611.0 | 21.99 | 0.0 | 10.0 | 12.33 | 16.86 | Au1rxx-base64 | 156.146.38.168 |
| 73.8 | shadowsocks | 278.4 | 275.2 | 21.33 | 4.68 | 9.86 | 12.33 | 16.86 | Au1rxx-base64 | 149.22.87.204 |
| 73.28 | shadowsocks | 281.2 | 288.7 | 21.27 | 4.18 | 9.87 | 12.33 | 16.86 | Au1rxx-base64 | 149.22.87.241 |
| 72.71 | shadowsocks | 284.0 | 610.8 | 21.2 | 0.0 | 10.0 | 12.33 | 16.86 | Au1rxx-base64 | 149.22.95.183 |
| 70.66 | trojan | 315.9 | 457.2 | 20.46 | 0.0 | 10.0 | 11.15 | 15.34 | Surfboard-tg-mixed | 94.140.0.40 |
| 70.1 | shadowsocks | 304.9 | 357.0 | 20.72 | 1.61 | 9.9 | 12.33 | 16.86 | Au1rxx-base64 | 149.22.87.240 |
| 69.9 | shadowsocks | 214.5 | 497.7 | 22.81 | 0.0 | 10.0 | 12.33 | 11.86 | DeltaKronecker-all | 107.172.219.230 |
| 69.43 | shadowsocks | 363.7 | 731.9 | 19.36 | 0.0 | 10.0 | 12.33 | 16.86 | Au1rxx-base64 | 37.19.198.236 |
| 69.21 | shadowsocks | 357.5 | 725.5 | 19.5 | 0.0 | 10.0 | 12.33 | 16.86 | Au1rxx-base64 | 37.19.198.243 |
| 69.16 | shadowsocks | 359.5 | 709.8 | 19.46 | 0.0 | 10.0 | 12.33 | 16.86 | Au1rxx-base64 | 37.19.198.160 |
| 68.33 | vless | 346.9 | 834.4 | 19.75 | 0.0 | 10.0 | 3.5 | 16.86 | Au1rxx-base64 | 15.204.97.214 |
| 68.06 | trojan | 289.8 | 581.3 | 21.07 | 0.0 | 10.0 | 11.15 | 16.86 | Au1rxx-base64 | pro-tortoise.rooster465.autos |
| 65.33 | shadowsocks | 371.4 | 760.3 | 19.18 | 0.0 | 10.0 | 12.33 | 16.86 | Au1rxx-base64 | tinkered-pennies-puppies.freesocks.work |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| Surfboard-tg-mixed | 0.791 | 0.716 | 95 | 6062 | prefer |
| Au1rxx-base64 | 0.717 | 0.727 | 33 | 79 | prefer |
| DeltaKronecker-all | 0.715 | 0.637 | 113 | 6997 | prefer |
| mheidari-all | 0.711 | 0.634 | 101 | 16169 | prefer |
| nscl5-all | 0.356 | 1.0 | 2 | 1114 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4368 | observe |
| Epodonios-all | 0.255 | None | 0 | 7138 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6834 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4562 | observe |
| barry-far-vless | 0.255 | None | 0 | 5164 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5333 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| xiaoji235-airport-v2ray-all | 0.227 | None | 0 | 1289 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | ProxyError | - | 36 |
| speed | ClientOSError | - | 18 |
| geo | TimeoutError | - | 18 |
| 204 | TimeoutError | - | 8 |
| 204 | ClientOSError | - | 8 |
| cn-block | ProxyError | - | 7 |
| cn-block | ClientOSError | - | 7 |
| cn-block | TimeoutError | - | 5 |
| geo | ClientOSError | - | 3 |
| geo | ProxyError | - | 3 |
| speed | ProxyError | - | 2 |
| speed | TimeoutError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 295 | 267 | - |
| global | False | 300 | 274 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
