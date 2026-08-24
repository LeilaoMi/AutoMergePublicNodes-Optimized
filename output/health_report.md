# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-24 01:45:31 |
| 运行耗时 | 269.2s |
| 订阅源总数 | 107 |
| 健康订阅源 | 97 |
| 原始节点 | 78233 |
| 去重后节点 | 21555 |
| TCP 可达 | 3000 |
| 真实可用 | 747 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 21555 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.8 |
| geo | 1.5 |
| tcp | 35.2 |
| probe | 55.8 |
| real_test | 144.5 |
| generate | 26.3 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 48506 |
| shadowsocks | 10397 |
| vmess | 9918 |
| trojan | 7826 |
| hysteria2 | 1182 |
| http | 165 |
| shadowsocksr | 128 |
| socks | 102 |
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
| 81.44 | shadowsocks | 226.4 | 599.5 | 22.54 | 0.0 | 10.0 | 13.32 | 19.58 | Au1rxx-base64 | 156.146.38.170 |
| 80.74 | http | 254.7 | 568.7 | 21.88 | 0.0 | 10.0 | 14.87 | 19.94 | zhangkai | 138.199.35.198 |
| 79.99 | trojan | 326.8 | 871.8 | 20.21 | 0.0 | 10.0 | 13.2 | 19.58 | Au1rxx-base64 | 64.94.95.118 |
| 79.52 | trojan | 347.3 | 891.7 | 19.74 | 0.0 | 10.0 | 13.2 | 19.58 | Au1rxx-base64 | 64.94.95.114 |
| 79.48 | shadowsocks | 289.2 | 740.7 | 21.08 | 0.0 | 10.0 | 13.32 | 19.58 | Au1rxx-base64 | 23.150.248.20 |
| 79.1 | http | 252.0 | 562.3 | 21.94 | 0.0 | 10.0 | 14.87 | 19.94 | zhangkai | 138.199.35.216 |
| 78.84 | vless | 296.3 | 651.9 | 20.92 | 0.0 | 10.0 | 11.49 | 19.58 | Au1rxx-base64 | 38.244.20.113 |
| 78.27 | shadowsocks | 223.4 | 601.7 | 22.61 | 0.0 | 10.0 | 13.32 | 16.34 | Surfboard-tg-mixed | 156.146.38.167 |
| 77.9 | shadowsocks | 259.7 | 548.7 | 21.77 | 0.0 | 10.0 | 13.32 | 19.58 | Au1rxx-base64 | 173.244.56.9 |
| 77.65 | vless | 325.7 | 717.0 | 20.24 | 0.0 | 10.0 | 11.49 | 19.58 | Au1rxx-base64 | 137.184.218.169 |
| 77.63 | shadowsocks | 261.3 | 507.5 | 21.73 | 0.0 | 10.0 | 13.32 | 19.58 | Au1rxx-base64 | 108.181.118.10 |
| 77.14 | shadowsocks | 231.3 | 619.8 | 22.42 | 0.0 | 10.0 | 13.32 | 15.4 | mheidari-all | 156.146.38.169 |
| 76.69 | trojan | 264.3 | 538.0 | 21.66 | 0.0 | 10.0 | 13.2 | 19.58 | Au1rxx-base64 | 14.1.28.76 |
| 76.61 | vless | 305.1 | 632.0 | 20.72 | 0.0 | 10.0 | 11.49 | 19.58 | Au1rxx-base64 | 38.244.21.147 |
| 76.49 | shadowsocks | 318.5 | 681.8 | 20.41 | 0.0 | 10.0 | 13.32 | 19.58 | Au1rxx-base64 | 173.244.56.6 |
| 76.48 | shadowsocks | 327.5 | 775.3 | 20.2 | 0.0 | 10.0 | 13.32 | 19.58 | Au1rxx-base64 | 37.19.198.236 |
| 76.28 | vless | 273.2 | 592.0 | 21.45 | 0.0 | 10.0 | 11.49 | 19.58 | Au1rxx-base64 | 192.220.54.83 |
| 76.0 | shadowsocks | 285.3 | 588.2 | 21.17 | 0.0 | 10.0 | 13.32 | 19.58 | Au1rxx-base64 | 94.72.127.55 |
| 75.97 | vless | 347.4 | 744.0 | 19.74 | 0.0 | 10.0 | 11.49 | 19.58 | Au1rxx-base64 | 167.17.69.171 |
| 75.83 | hysteria2 | 293.8 | 682.6 | 20.98 | 0.0 | 10.0 | 14.25 | 15.4 | mheidari-all | 159.223.157.129 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.997 | 1.0 | 113 | 144 | prefer |
| Au1rxx-base64 | 0.983 | 0.917 | 448 | 1688 | prefer |
| Surfboard-tg-mixed | 0.867 | 0.791 | 158 | 6383 | prefer |
| DeltaKronecker-all | 0.574 | 0.494 | 77 | 5415 | observe |
| mheidari-all | 0.487 | 0.406 | 143 | 14677 | observe |
| nscl5-all | 0.352 | 1.0 | 2 | 1008 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4989 | observe |
| Epodonios-all | 0.255 | None | 0 | 6993 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3989 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7072 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5292 | observe |
| barry-far-vless | 0.255 | None | 0 | 5618 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4085 | observe |
| Au1rxx-clash | 0.243 | None | 0 | 1689 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 71 |
| speed | TimeoutError | - | 42 |
| geo | ClientOSError | - | 20 |
| speed | ClientOSError | - | 19 |
| cn-block | TimeoutError | - | 15 |
| cn-block | ClientOSError | - | 10 |
| 204 | ProxyError | - | 9 |
| 204 | TimeoutError | - | 8 |
| cn-block | ProxyError | - | 2 |
| 204 | ClientOSError | - | 1 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
