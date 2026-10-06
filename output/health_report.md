# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-06 06:01:32 |
| 运行耗时 | 770.3s |
| 订阅源总数 | 107 |
| 健康订阅源 | 94 |
| 原始节点 | 98384 |
| 去重后节点 | 27441 |
| TCP 可达 | 3000 |
| 真实可用 | 531 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 27441 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 8.1 |
| geo | 1.5 |
| tcp | 48.1 |
| probe | 282.3 |
| real_test | 355.7 |
| generate | 74.6 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 58265 |
| vmess | 15910 |
| shadowsocks | 11661 |
| trojan | 10225 |
| hysteria2 | 1380 |
| http | 614 |
| shadowsocksr | 165 |
| socks | 107 |
| anytls | 28 |
| hysteria | 17 |
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
| 85.77 | vless | 197.1 | 516.0 | 23.21 | 0.0 | 10.0 | 12.56 | 20.0 | Au1rxx-base64 | 107.173.237.146 |
| 84.51 | vless | 218.7 | 515.6 | 22.72 | 0.0 | 10.0 | 12.56 | 20.0 | Au1rxx-base64 | 47.251.108.158 |
| 84.49 | vless | 211.8 | 494.3 | 22.87 | 0.0 | 10.0 | 12.56 | 20.0 | Au1rxx-base64 | 137.175.82.40 |
| 83.88 | trojan | 240.5 | 596.0 | 22.21 | 0.0 | 10.0 | 14.67 | 20.0 | Au1rxx-base64 | 107.149.159.190 |
| 82.6 | shadowsocks | 255.2 | 621.7 | 21.87 | 0.0 | 10.0 | 14.73 | 20.0 | Au1rxx-base64 | 156.146.38.169 |
| 82.49 | shadowsocks | 259.8 | 634.8 | 21.76 | 0.0 | 10.0 | 14.73 | 20.0 | Au1rxx-base64 | 156.146.38.167 |
| 82.23 | vless | 273.9 | 610.9 | 21.44 | 0.0 | 10.0 | 12.56 | 20.0 | Au1rxx-base64 | 15.204.97.216 |
| 81.24 | shadowsocks | 261.2 | 641.1 | 21.73 | 0.0 | 10.0 | 14.73 | 18.78 | mheidari-all | 156.146.38.168 |
| 81.2 | shadowsocks | 241.4 | 552.9 | 22.19 | 0.0 | 10.0 | 14.73 | 18.78 | mheidari-all | 108.181.118.10 |
| 81.06 | shadowsocks | 259.4 | 629.9 | 21.77 | 0.0 | 10.0 | 14.73 | 20.0 | Au1rxx-base64 | 156.146.38.170 |
| 80.83 | vless | 194.7 | 505.3 | 23.27 | 0.0 | 10.0 | 12.56 | 20.0 | Au1rxx-base64 | 144.202.126.147 |
| 80.82 | shadowsocks | 259.4 | 612.6 | 21.77 | 0.0 | 10.0 | 14.73 | 20.0 | Surfboard-tg-mixed | 5.78.51.123 |
| 80.69 | hysteria2 | 226.8 | 228.7 | 22.53 | 6.42 | 9.91 | 13.7 | 20.0 | Au1rxx-base64 | 45.32.10.7 |
| 80.52 | vless | 325.9 | 785.2 | 20.23 | 0.0 | 10.0 | 12.56 | 20.0 | Au1rxx-base64 | 23.95.222.127 |
| 80.0 | trojan | 291.6 | 626.9 | 21.03 | 0.0 | 10.0 | 14.67 | 20.0 | Au1rxx-base64 | guided-ferret.rooster465.autos |
| 79.57 | vless | 182.7 | 479.7 | 23.55 | 0.0 | 10.0 | 12.56 | 20.0 | Au1rxx-base64 | 154.21.94.246 |
| 79.25 | vless | 284.5 | 441.5 | 21.19 | 0.0 | 10.0 | 12.56 | 20.0 | Au1rxx-base64 | 104.18.47.113 |
| 79.04 | shadowsocks | 257.6 | 674.9 | 21.81 | 0.0 | 10.0 | 14.73 | 20.0 | Au1rxx-base64 | 108.181.0.177 |
| 78.91 | trojan | 332.6 | 750.3 | 20.08 | 0.0 | 9.79 | 14.67 | 20.0 | Au1rxx-base64 | ultimate-jaguar.rooster465.autos |
| 78.84 | vless | 273.1 | 606.9 | 21.46 | 0.0 | 10.0 | 12.56 | 20.0 | Au1rxx-base64 | 15.204.97.197 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | 0.935 | 356 | 1801 | prefer |
| Surfboard-tg-mixed | 0.797 | 0.72 | 143 | 7083 | prefer |
| ermaozi | 0.601 | 0.576 | 59 | 691 | observe |
| mheidari-all | 0.351 | 0.269 | 201 | 23039 | observe |
| DeltaKronecker-all | 0.337 | 0.308 | 13 | 5300 | observe |
| tg-OutlineReleasedKey | 0.257 | 1.0 | 1 | 53 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5111 | observe |
| Epodonios-all | 0.255 | None | 0 | 7631 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3996 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9601 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5600 | observe |
| barry-far-vless | 0.255 | None | 0 | 5876 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4375 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |
| Au1rxx-clash | 0.247 | None | 0 | 1801 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 113 |
| speed | TimeoutError | - | 36 |
| 204 | ProxyError | - | 25 |
| geo | ClientOSError | - | 20 |
| 204 | TimeoutError | - | 14 |
| cn-block | TimeoutError | - | 14 |
| speed | ClientOSError | - | 8 |
| 204 | ProxyConnectionError | - | 7 |
| cn-block | ClientOSError | - | 6 |
| 204 | ClientOSError | - | 4 |
| cn-block | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
