# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-10 11:10:46 |
| 运行耗时 | 675.1s |
| 订阅源总数 | 107 |
| 健康订阅源 | 96 |
| 原始节点 | 91201 |
| 去重后节点 | 24193 |
| TCP 可达 | 3000 |
| 真实可用 | 451 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 24193 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.9 |
| geo | 1.4 |
| tcp | 40.4 |
| probe | 272.2 |
| real_test | 266.2 |
| generate | 88.0 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 55435 |
| vmess | 13056 |
| shadowsocks | 10980 |
| trojan | 8869 |
| hysteria2 | 1964 |
| http | 685 |
| shadowsocksr | 124 |
| socks | 56 |
| hysteria | 15 |
| tuic | 10 |
| anytls | 7 |

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
| 81.36 | shadowsocks | 249.3 | 696.1 | 22.01 | 0.0 | 10.0 | 13.67 | 19.68 | Au1rxx-base64 | 37.19.198.160 |
| 80.92 | vless | 235.3 | 618.3 | 22.33 | 0.0 | 10.0 | 8.91 | 19.68 | Au1rxx-base64 | 195.123.235.177 |
| 80.63 | vless | 247.9 | 701.6 | 22.04 | 0.0 | 10.0 | 8.91 | 19.68 | Au1rxx-base64 | 47.253.226.114 |
| 79.89 | vless | 280.0 | 703.8 | 21.3 | 0.0 | 10.0 | 8.91 | 19.68 | Au1rxx-base64 | 66.70.179.198 |
| 79.55 | shadowsocks | 289.6 | 808.6 | 21.07 | 0.0 | 9.13 | 13.67 | 19.68 | Au1rxx-base64 | 37.19.198.244 |
| 79.34 | shadowsocks | 300.9 | 850.1 | 20.81 | 0.0 | 9.18 | 13.67 | 19.68 | Au1rxx-base64 | 37.19.198.243 |
| 79.03 | vless | 280.8 | 753.2 | 21.28 | 0.0 | 9.16 | 8.91 | 19.68 | Au1rxx-base64 | 169.40.42.89 |
| 78.84 | shadowsocks | 301.2 | 831.7 | 20.81 | 0.0 | 9.18 | 13.67 | 19.68 | Au1rxx-base64 | 38.180.135.156 |
| 78.79 | vless | 245.6 | 703.3 | 22.09 | 0.0 | 9.11 | 8.91 | 19.68 | Au1rxx-base64 | 79.141.172.154 |
| 78.61 | vless | 299.1 | 708.8 | 20.86 | 0.0 | 9.16 | 8.91 | 19.68 | Au1rxx-base64 | 216.152.147.28 |
| 78.52 | vless | 259.7 | 625.6 | 21.77 | 0.0 | 9.16 | 8.91 | 19.68 | Au1rxx-base64 | 169.40.42.52 |
| 78.48 | vless | 340.9 | 807.8 | 19.89 | 0.0 | 10.0 | 8.91 | 19.68 | Au1rxx-base64 | 169.40.42.163 |
| 78.31 | vless | 312.1 | 723.5 | 20.55 | 0.0 | 9.17 | 8.91 | 19.68 | Au1rxx-base64 | 169.40.42.90 |
| 78.24 | vless | 281.3 | 636.2 | 21.27 | 0.0 | 10.0 | 8.91 | 19.68 | Au1rxx-base64 | 169.40.42.168 |
| 78.24 | vless | 351.2 | 985.0 | 19.65 | 0.0 | 10.0 | 8.91 | 19.68 | Au1rxx-base64 | 185.95.231.156 |
| 78.17 | vless | 251.8 | 663.0 | 21.95 | 0.0 | 9.21 | 8.91 | 19.68 | Au1rxx-base64 | 169.40.42.184 |
| 78.15 | shadowsocks | 366.4 | 989.1 | 19.3 | 0.0 | 10.0 | 13.67 | 19.68 | Au1rxx-base64 | 15.204.246.132 |
| 78.14 | vless | 320.3 | 854.7 | 20.36 | 0.0 | 9.19 | 8.91 | 19.68 | Au1rxx-base64 | 169.40.42.133 |
| 78.11 | shadowsocks | 292.0 | 666.4 | 21.02 | 0.0 | 10.0 | 13.67 | 19.68 | Au1rxx-base64 | 156.146.38.167 |
| 77.93 | shadowsocks | 297.8 | 770.1 | 20.88 | 0.0 | 10.0 | 13.67 | 17.88 | Surfboard-tg-mixed | 51.222.141.125 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.973 | 0.91 | 268 | 1628 | prefer |
| Surfboard-tg-mixed | 0.848 | 0.771 | 166 | 7439 | prefer |
| mheidari-all | 0.628 | 0.549 | 71 | 19290 | observe |
| ermaozi | 0.618 | 0.604 | 53 | 449 | observe |
| DeltaKronecker-all | 0.372 | 0.273 | 22 | 5853 | observe |
| ermaozi-get_subscribe | 0.274 | 1.0 | 1 | 469 | observe |
| tg-oneclickvpnkeys | 0.264 | 1.0 | 1 | 214 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4995 | observe |
| Epodonios-all | 0.255 | None | 0 | 7808 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 8703 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 6025 | observe |
| barry-far-vless | 0.255 | None | 0 | 6215 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4358 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 3508 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | ClientOSError | - | 26 |
| 204 | TimeoutError | - | 26 |
| 204 | ProxyError | - | 19 |
| geo | TimeoutError | - | 13 |
| 204 | ProxyConnectionError | - | 12 |
| cn-block | TimeoutError | - | 10 |
| speed | ClientOSError | - | 10 |
| cn-block | ClientOSError | - | 8 |
| speed | TimeoutError | - | 4 |
| 204 | ClientOSError | - | 3 |
| cn-block | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
