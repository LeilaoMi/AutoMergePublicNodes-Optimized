# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-28 03:02:12 |
| 运行耗时 | 413.0s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 84746 |
| 去重后节点 | 23236 |
| TCP 可达 | 3000 |
| 真实可用 | 1062 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23236 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 22.0 |
| geo | 1.3 |
| tcp | 32.1 |
| probe | 76.6 |
| real_test | 250.6 |
| generate | 30.3 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 47839 |
| trojan | 15646 |
| vmess | 10418 |
| shadowsocks | 10035 |
| hysteria2 | 547 |
| shadowsocksr | 96 |
| socks | 71 |
| http | 63 |
| hysteria | 15 |
| anytls | 10 |
| tuic | 6 |

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
| 83.48 | hysteria2 | 232.5 | 640.9 | 22.39 | 0.0 | 10.0 | 12.69 | 19.5 | Au1rxx-base64 | 159.223.157.129 |
| 82.46 | trojan | 249.6 | 679.7 | 22.0 | 0.0 | 10.0 | 13.96 | 19.5 | Au1rxx-base64 | 153.75.250.171 |
| 79.56 | shadowsocks | 216.1 | 589.1 | 22.78 | 0.0 | 10.0 | 11.28 | 19.5 | Au1rxx-base64 | 198.98.53.130 |
| 79.23 | shadowsocks | 230.0 | 636.1 | 22.45 | 0.0 | 10.0 | 11.28 | 19.5 | Au1rxx-base64 | 37.19.198.160 |
| 79.06 | shadowsocks | 237.5 | 659.5 | 22.28 | 0.0 | 10.0 | 11.28 | 19.5 | Au1rxx-base64 | 37.19.198.244 |
| 77.99 | hysteria2 | 255.4 | 704.7 | 21.87 | 0.0 | 5.93 | 12.69 | 19.5 | Au1rxx-base64 | usa1.spectrumproxy.shop |
| 76.98 | trojan | 340.7 | 768.7 | 19.89 | 0.0 | 10.0 | 13.96 | 19.5 | Au1rxx-base64 | 64.94.95.118 |
| 76.83 | shadowsocks | 247.2 | 686.8 | 22.05 | 0.0 | 10.0 | 11.28 | 19.5 | Au1rxx-base64 | 37.19.198.236 |
| 75.09 | shadowsocks | 359.9 | 896.2 | 19.45 | 0.0 | 10.0 | 11.28 | 19.5 | Au1rxx-base64 | 185.196.61.82 |
| 75.07 | shadowsocks | 283.0 | 656.7 | 21.23 | 0.0 | 10.0 | 11.28 | 19.5 | Au1rxx-base64 | 156.146.38.169 |
| 74.99 | shadowsocks | 278.5 | 639.3 | 21.33 | 0.0 | 10.0 | 11.28 | 19.5 | Au1rxx-base64 | 156.146.38.167 |
| 74.53 | vless | 417.0 | 1090.6 | 18.12 | 0.0 | 10.0 | 6.91 | 19.5 | Au1rxx-base64 | 158.69.112.254 |
| 74.01 | hysteria2 | 407.5 | 650.5 | 18.34 | 0.0 | 10.0 | 12.69 | 19.5 | Au1rxx-base64 | 62.210.124.146 |
| 73.76 | trojan | 433.9 | 1052.3 | 17.73 | 0.0 | 10.0 | 13.96 | 19.5 | Au1rxx-base64 | 64.94.95.115 |
| 73.68 | trojan | 487.8 | 1213.6 | 16.49 | 0.0 | 10.0 | 13.96 | 19.5 | Au1rxx-base64 | 64.94.95.114 |
| 73.66 | trojan | 441.5 | 1050.5 | 17.56 | 0.0 | 10.0 | 13.96 | 19.5 | Au1rxx-base64 | 163.245.196.68 |
| 73.61 | vless | 241.1 | 636.2 | 22.2 | 0.0 | 10.0 | 6.91 | 19.5 | Au1rxx-base64 | us888.bearbeer.digital |
| 73.13 | trojan | 347.5 | 887.2 | 19.73 | 0.0 | 10.0 | 13.96 | 13.44 | DeltaKronecker-all | 64.74.163.118 |
| 72.86 | shadowsocks | 327.9 | 801.3 | 20.19 | 0.0 | 10.0 | 11.28 | 19.5 | Au1rxx-base64 | 68.168.116.6 |
| 72.25 | shadowsocks | 309.3 | 592.9 | 20.62 | 0.0 | 10.0 | 11.28 | 19.5 | Au1rxx-base64 | 173.244.56.9 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | 0.963 | 485 | 1387 | prefer |
| zhangkai | 0.987 | 1.0 | 59 | 74 | prefer |
| mheidari-all | 0.945 | 0.868 | 243 | 18500 | prefer |
| Surfboard-tg-mixed | 0.611 | 0.533 | 30 | 5606 | observe |
| xiaoji235-airport-v2ray-all | 0.438 | 1.0 | 3 | 3959 | observe |
| DeltaKronecker-all | 0.409 | 0.329 | 925 | 5643 | observe |
| Barabama-yudou | 0.318 | 1.0 | 2 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4831 | observe |
| Epodonios-all | 0.255 | None | 0 | 6592 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3971 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6500 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4470 | observe |
| barry-far-vless | 0.255 | None | 0 | 5025 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4997 | observe |
| Au1rxx-clash | 0.23 | None | 0 | 1387 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 313 |
| speed | ClientOSError | - | 170 |
| geo | ClientOSError | - | 90 |
| speed | TimeoutError | - | 47 |
| 204 | ProxyError | - | 35 |
| cn-block | TimeoutError | - | 17 |
| 204 | TimeoutError | - | 11 |
| cn-block | ClientOSError | - | 3 |
| cn-block | ProxyError | - | 2 |
| 204 | ClientOSError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
