# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-06-29 11:15:42 |
| 运行耗时 | 269.6s |
| 订阅源总数 | 107 |
| 健康订阅源 | 105 |
| 原始节点 | 76490 |
| 去重后节点 | 23087 |
| TCP 可达 | 3000 |
| 真实可用 | 455 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23087 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.9 |
| geo | 1.3 |
| tcp | 30.6 |
| probe | 59.9 |
| real_test | 123.4 |
| generate | 49.4 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 43028 |
| trojan | 12596 |
| vmess | 10946 |
| shadowsocks | 9347 |
| hysteria2 | 231 |
| shadowsocksr | 153 |
| http | 136 |
| socks | 46 |
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
| 79.64 | shadowsocks | 262.3 | 650.2 | 21.71 | 0.0 | 10.0 | 13.53 | 18.4 | mheidari-all | 198.98.53.130 |
| 77.84 | vless | 301.6 | 768.9 | 20.8 | 0.0 | 10.0 | 8.64 | 18.4 | mheidari-all | 47.253.226.114 |
| 77.79 | shadowsocks | 283.5 | 689.3 | 21.21 | 0.0 | 10.0 | 13.53 | 18.4 | mheidari-all | 108.181.57.93 |
| 74.53 | shadowsocks | 253.7 | 621.5 | 21.9 | 0.0 | 10.0 | 13.53 | 13.1 | Au1rxx-base64 | 156.146.38.168 |
| 74.45 | trojan | 397.6 | 606.7 | 18.58 | 0.0 | 10.0 | 12.0 | 15.92 | Surfboard-tg-mixed | 94.140.0.100 |
| 74.4 | shadowsocks | 259.7 | 636.9 | 21.77 | 0.0 | 10.0 | 13.53 | 13.1 | Au1rxx-base64 | 156.146.38.167 |
| 74.28 | shadowsocks | 264.8 | 663.9 | 21.65 | 0.0 | 10.0 | 13.53 | 13.1 | Au1rxx-base64 | 37.19.198.243 |
| 74.27 | shadowsocks | 265.0 | 659.6 | 21.64 | 0.0 | 10.0 | 13.53 | 13.1 | Au1rxx-base64 | 37.19.198.244 |
| 73.56 | shadowsocks | 295.8 | 750.0 | 20.93 | 0.0 | 10.0 | 13.53 | 13.1 | Au1rxx-base64 | 156.146.38.170 |
| 73.14 | vless | 273.3 | 580.0 | 21.45 | 0.0 | 10.0 | 8.64 | 18.4 | mheidari-all | 173.245.59.35 |
| 73.08 | shadowsocks | 316.4 | 797.2 | 20.45 | 0.0 | 10.0 | 13.53 | 13.1 | Au1rxx-base64 | 37.19.198.236 |
| 73.06 | shadowsocks | 255.9 | 629.2 | 21.85 | 0.0 | 10.0 | 13.53 | 13.1 | Au1rxx-base64 | 156.146.38.169 |
| 70.48 | vless | 475.5 | 1225.2 | 16.77 | 0.0 | 10.0 | 8.64 | 15.92 | Surfboard-tg-mixed | 130.107.73.148 |
| 69.99 | vless | 333.7 | 663.0 | 20.05 | 0.0 | 10.0 | 8.64 | 18.4 | mheidari-all | 38.244.20.164 |
| 69.87 | vless | 402.5 | 564.2 | 18.46 | 0.0 | 10.0 | 8.64 | 18.4 | mheidari-all | 162.159.34.128 |
| 69.29 | shadowsocks | 264.2 | 659.9 | 21.66 | 0.0 | 10.0 | 13.53 | 13.1 | Au1rxx-base64 | 37.19.198.160 |
| 69.28 | vless | 347.9 | 910.2 | 19.72 | 0.0 | 10.0 | 8.64 | 15.92 | Surfboard-tg-mixed | 174.129.45.76 |
| 68.98 | shadowsocks | 300.1 | 623.6 | 20.83 | 0.0 | 10.0 | 13.53 | 13.1 | Au1rxx-base64 | 149.22.95.183 |
| 68.68 | vless | 294.6 | 659.9 | 20.96 | 0.0 | 10.0 | 8.64 | 18.4 | mheidari-all | 162.159.18.241 |
| 68.14 | shadowsocks | 327.9 | 685.2 | 20.19 | 0.0 | 10.0 | 13.53 | 13.1 | Au1rxx-base64 | 173.244.56.6 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| mheidari-all | 0.826 | 0.748 | 282 | 15787 | prefer |
| Au1rxx-base64 | 0.82 | 0.833 | 36 | 95 | prefer |
| Surfboard-tg-mixed | 0.707 | 0.628 | 239 | 5303 | prefer |
| DeltaKronecker-all | 0.571 | 0.491 | 53 | 7004 | observe |
| nscl5-all | 0.302 | 1.0 | 1 | 1166 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4653 | observe |
| Epodonios-all | 0.255 | None | 0 | 7391 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7178 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 3969 | observe |
| barry-far-vless | 0.255 | None | 0 | 4344 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5278 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 70 |
| 204 | ProxyError | - | 22 |
| 204 | ClientOSError | - | 18 |
| 204 | TimeoutError | - | 17 |
| cn-block | TimeoutError | - | 17 |
| geo | TimeoutError | - | 16 |
| speed | TimeoutError | - | 11 |
| cn-block | ClientOSError | - | 8 |
| geo | ClientOSError | - | 7 |
| cn-block | ProxyError | - | 3 |
| speed | ProxyError | - | 3 |
| geo | ProxyError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
