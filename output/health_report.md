# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-25 07:00:27 |
| 运行耗时 | 262.4s |
| 订阅源总数 | 107 |
| 健康订阅源 | 96 |
| 原始节点 | 78337 |
| 去重后节点 | 22287 |
| TCP 可达 | 3000 |
| 真实可用 | 685 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22287 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.1 |
| geo | 1.4 |
| tcp | 35.2 |
| probe | 54.4 |
| real_test | 134.5 |
| generate | 30.8 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 49153 |
| shadowsocks | 10807 |
| vmess | 10380 |
| trojan | 6618 |
| hysteria2 | 1003 |
| http | 164 |
| shadowsocksr | 132 |
| socks | 70 |
| hysteria | 7 |
| tuic | 3 |

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
| 81.38 | shadowsocks | 252.1 | 699.4 | 21.94 | 0.0 | 10.0 | 13.94 | 19.5 | Au1rxx-base64 | 37.19.198.243 |
| 81.26 | shadowsocks | 217.6 | 590.4 | 22.74 | 0.0 | 10.0 | 13.94 | 19.58 | Surfboard-tg-mixed | 198.98.53.130 |
| 80.59 | shadowsocks | 242.3 | 624.8 | 22.17 | 0.0 | 8.98 | 13.94 | 19.5 | Au1rxx-base64 | 155.138.136.240 |
| 80.31 | shadowsocks | 252.1 | 702.0 | 21.94 | 0.0 | 8.93 | 13.94 | 19.5 | Au1rxx-base64 | 37.19.198.244 |
| 79.77 | shadowsocks | 277.3 | 780.8 | 21.36 | 0.0 | 8.97 | 13.94 | 19.5 | Au1rxx-base64 | 37.19.198.160 |
| 79.31 | shadowsocks | 319.8 | 845.5 | 20.37 | 0.0 | 10.0 | 13.94 | 19.5 | Au1rxx-base64 | 140.238.153.81 |
| 79.18 | shadowsocks | 325.7 | 935.0 | 20.24 | 0.0 | 10.0 | 13.94 | 19.5 | Au1rxx-base64 | 15.204.247.175 |
| 78.93 | vless | 252.0 | 690.6 | 21.94 | 0.0 | 10.0 | 7.49 | 19.5 | Au1rxx-base64 | 47.89.186.170 |
| 78.92 | shadowsocks | 336.8 | 965.9 | 19.98 | 0.0 | 10.0 | 13.94 | 19.5 | Au1rxx-base64 | 15.204.246.132 |
| 78.17 | vless | 239.7 | 649.4 | 22.23 | 0.0 | 8.95 | 7.49 | 19.5 | Au1rxx-base64 | 137.184.218.169 |
| 78.13 | vless | 286.8 | 768.6 | 21.14 | 0.0 | 10.0 | 7.49 | 19.5 | Au1rxx-base64 | 169.40.42.173 |
| 77.97 | shadowsocks | 284.4 | 652.8 | 21.2 | 0.0 | 10.0 | 13.94 | 19.5 | Au1rxx-base64 | 156.146.38.167 |
| 77.93 | vless | 295.4 | 795.2 | 20.94 | 0.0 | 10.0 | 7.49 | 19.5 | Au1rxx-base64 | 185.95.231.156 |
| 77.83 | vless | 256.3 | 699.5 | 21.84 | 0.0 | 9.0 | 7.49 | 19.5 | Au1rxx-base64 | 79.127.243.217 |
| 77.36 | vless | 276.8 | 676.3 | 21.37 | 0.0 | 9.0 | 7.49 | 19.5 | Au1rxx-base64 | 169.40.42.104 |
| 77.23 | vless | 280.2 | 698.8 | 21.29 | 0.0 | 8.95 | 7.49 | 19.5 | Au1rxx-base64 | 66.70.179.198 |
| 77.2 | hysteria2 | 354.5 | 687.1 | 19.57 | 0.0 | 10.0 | 14.4 | 19.58 | Surfboard-tg-mixed | 89.125.156.80 |
| 77.16 | vless | 285.3 | 760.0 | 21.17 | 0.0 | 9.0 | 7.49 | 19.5 | Au1rxx-base64 | 169.40.42.133 |
| 77.12 | vless | 290.1 | 635.5 | 21.06 | 0.0 | 10.0 | 7.49 | 19.5 | Au1rxx-base64 | 198.251.78.29 |
| 76.96 | vless | 298.0 | 735.9 | 20.88 | 0.0 | 10.0 | 7.49 | 19.5 | Au1rxx-base64 | 158.69.112.254 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.967 | 1.0 | 24 | 144 | prefer |
| Au1rxx-base64 | 0.925 | 0.858 | 508 | 1700 | prefer |
| Surfboard-tg-mixed | 0.824 | 0.747 | 154 | 6465 | prefer |
| mheidari-all | 0.803 | 0.73 | 63 | 14480 | prefer |
| DeltaKronecker-all | 0.651 | 0.573 | 110 | 6340 | observe |
| 10ium-ScrapeCategorize-Vless | 0.287 | 0.5 | 2 | 4912 | observe |
| Epodonios-all | 0.255 | None | 0 | 6925 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3989 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6957 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5306 | observe |
| barry-far-vless | 0.255 | None | 0 | 5525 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4119 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.243 | None | 0 | 1705 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 54 |
| 204 | TimeoutError | - | 23 |
| speed | TimeoutError | - | 21 |
| speed | ClientOSError | - | 20 |
| cn-block | TimeoutError | - | 19 |
| geo | ClientOSError | - | 16 |
| 204 | ClientOSError | - | 9 |
| cn-block | ClientOSError | - | 7 |
| 204 | ProxyError | - | 4 |
| cn-block | ProxyError | - | 2 |
| speed | ProxyError | - | 2 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
