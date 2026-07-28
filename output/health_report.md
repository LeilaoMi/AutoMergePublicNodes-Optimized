# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-28 19:43:21 |
| 运行耗时 | 207.1s |
| 订阅源总数 | 107 |
| 健康订阅源 | 99 |
| 原始节点 | 80840 |
| 去重后节点 | 22955 |
| TCP 可达 | 3000 |
| 真实可用 | 346 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22955 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.7 |
| geo | 1.4 |
| tcp | 32.5 |
| probe | 47.2 |
| real_test | 87.7 |
| generate | 32.4 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 46334 |
| trojan | 13086 |
| vmess | 10417 |
| shadowsocks | 10345 |
| hysteria2 | 516 |
| shadowsocksr | 76 |
| socks | 52 |
| hysteria | 8 |
| tuic | 3 |
| http | 3 |

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
| 81.28 | shadowsocks | 227.6 | 627.8 | 22.51 | 0.0 | 10.0 | 13.47 | 19.3 | Au1rxx-base64 | 37.19.198.243 |
| 81.25 | shadowsocks | 228.9 | 626.1 | 22.48 | 0.0 | 10.0 | 13.47 | 19.3 | Au1rxx-base64 | 37.19.198.160 |
| 81.21 | shadowsocks | 230.6 | 629.2 | 22.44 | 0.0 | 10.0 | 13.47 | 19.3 | Au1rxx-base64 | 37.19.198.244 |
| 81.18 | shadowsocks | 231.8 | 597.9 | 22.41 | 0.0 | 10.0 | 13.47 | 19.3 | Au1rxx-base64 | 198.98.53.130 |
| 80.91 | shadowsocks | 243.4 | 672.6 | 22.14 | 0.0 | 10.0 | 13.47 | 19.3 | Au1rxx-base64 | 37.19.198.236 |
| 80.26 | hysteria2 | 231.6 | 638.7 | 22.42 | 0.0 | 10.0 | 9.64 | 19.3 | Au1rxx-base64 | 159.223.157.129 |
| 79.6 | trojan | 315.6 | 871.0 | 20.47 | 0.0 | 10.0 | 12.83 | 19.3 | Au1rxx-base64 | 153.75.250.171 |
| 77.86 | shadowsocks | 334.2 | 858.8 | 20.04 | 0.0 | 10.0 | 13.47 | 19.3 | Au1rxx-base64 | 185.196.61.82 |
| 77.8 | shadowsocks | 289.6 | 658.1 | 21.07 | 0.0 | 10.0 | 13.47 | 19.3 | Au1rxx-base64 | 156.146.38.167 |
| 77.28 | shadowsocks | 306.4 | 717.0 | 20.68 | 0.0 | 10.0 | 13.47 | 19.3 | Au1rxx-base64 | 156.146.38.169 |
| 77.15 | trojan | 294.9 | 644.7 | 20.95 | 0.0 | 10.0 | 12.83 | 19.3 | Au1rxx-base64 | 64.94.95.115 |
| 76.4 | trojan | 327.1 | 739.3 | 20.21 | 0.0 | 10.0 | 12.83 | 19.3 | Au1rxx-base64 | 64.94.95.118 |
| 76.08 | trojan | 303.1 | 641.1 | 20.76 | 0.0 | 10.0 | 12.83 | 19.3 | Au1rxx-base64 | 163.245.196.68 |
| 75.71 | vless | 305.4 | 685.5 | 20.71 | 0.0 | 10.0 | 8.34 | 18.52 | mheidari-all | 45.206.5.122 |
| 74.87 | vless | 422.1 | 1111.3 | 18.01 | 0.0 | 10.0 | 8.34 | 18.52 | mheidari-all | 158.69.112.254 |
| 74.67 | trojan | 386.8 | 916.6 | 18.82 | 0.0 | 10.0 | 12.83 | 19.3 | Au1rxx-base64 | 64.94.95.114 |
| 74.59 | trojan | 384.5 | 909.5 | 18.88 | 0.0 | 10.0 | 12.83 | 19.3 | Au1rxx-base64 | 64.94.95.117 |
| 74.41 | vless | 259.3 | 669.2 | 21.77 | 0.0 | 10.0 | 8.34 | 19.3 | Au1rxx-base64 | pro-us.emrata.top |
| 73.86 | shadowsocks | 310.7 | 823.5 | 20.59 | 0.0 | 10.0 | 13.47 | 19.3 | Au1rxx-base64 | 185.232.22.28 |
| 73.82 | shadowsocks | 312.2 | 830.9 | 20.55 | 0.0 | 10.0 | 13.47 | 19.3 | Au1rxx-base64 | 185.232.22.18 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.858 | 0.807 | 270 | 1312 | prefer |
| mheidari-all | 0.717 | 0.639 | 133 | 17378 | prefer |
| DeltaKronecker-all | 0.69 | 0.615 | 39 | 5965 | observe |
| Surfboard-tg-mixed | 0.661 | 0.586 | 29 | 5820 | observe |
| 10ium-ScrapeCategorize-Vless | 0.349 | 0.667 | 3 | 4972 | observe |
| Epodonios-all | 0.255 | None | 0 | 6834 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3970 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6507 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4597 | observe |
| barry-far-vless | 0.255 | None | 0 | 5117 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5059 | observe |
| nscl5-all | 0.255 | None | 0 | 3331 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.227 | None | 0 | 1312 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 27 |
| 204 | TimeoutError | - | 23 |
| cn-block | TimeoutError | - | 22 |
| 204 | ProxyError | - | 19 |
| geo | ClientOSError | - | 9 |
| speed | TimeoutError | - | 9 |
| 204 | ClientOSError | - | 6 |
| speed | ClientOSError | - | 4 |
| cn-block | ProxyError | - | 4 |
| cn-block | ClientOSError | - | 4 |
| geo | ProxyError | - | 1 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
