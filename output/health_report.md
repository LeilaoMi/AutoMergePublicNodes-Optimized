# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-16 12:55:05 |
| 运行耗时 | 364.2s |
| 订阅源总数 | 107 |
| 健康订阅源 | 99 |
| 原始节点 | 79021 |
| 去重后节点 | 21933 |
| TCP 可达 | 3000 |
| 真实可用 | 1100 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 21933 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.5 |
| geo | 1.2 |
| tcp | 34.0 |
| probe | 62.6 |
| real_test | 227.3 |
| generate | 33.5 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 43551 |
| trojan | 13256 |
| vmess | 10803 |
| shadowsocks | 10021 |
| hysteria2 | 1056 |
| http | 166 |
| socks | 75 |
| shadowsocksr | 74 |
| tuic | 10 |
| hysteria | 7 |
| anytls | 2 |

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
| 84.77 | hysteria2 | 259.3 | 562.8 | 21.78 | 0.0 | 9.99 | 14.21 | 20.0 | Au1rxx-base64 | 150.241.102.127 |
| 82.96 | hysteria2 | 309.2 | 721.1 | 20.62 | 0.0 | 10.0 | 14.21 | 20.0 | Au1rxx-base64 | 159.223.157.129 |
| 82.56 | shadowsocks | 217.6 | 584.8 | 22.74 | 0.0 | 9.88 | 13.94 | 20.0 | Au1rxx-base64 | 156.146.38.168 |
| 82.41 | shadowsocks | 229.2 | 602.8 | 22.47 | 0.0 | 10.0 | 13.94 | 20.0 | Au1rxx-base64 | 156.146.38.167 |
| 81.69 | trojan | 253.1 | 559.5 | 21.92 | 0.0 | 10.0 | 14.66 | 20.0 | Au1rxx-base64 | 14.1.28.76 |
| 81.51 | shadowsocks | 246.7 | 599.3 | 22.07 | 0.0 | 10.0 | 13.94 | 20.0 | Au1rxx-base64 | 23.150.248.20 |
| 79.43 | shadowsocks | 267.2 | 537.2 | 21.59 | 0.0 | 10.0 | 13.94 | 20.0 | Au1rxx-base64 | 173.244.56.6 |
| 78.22 | shadowsocks | 294.0 | 658.8 | 20.97 | 0.0 | 10.0 | 13.94 | 20.0 | Au1rxx-base64 | 173.244.56.9 |
| 78.2 | shadowsocks | 257.6 | 512.3 | 21.81 | 0.0 | 9.88 | 13.94 | 20.0 | Au1rxx-base64 | 108.181.118.10 |
| 77.92 | vless | 242.4 | 511.0 | 22.17 | 0.0 | 9.98 | 8.99 | 20.0 | Au1rxx-base64 | 70.39.197.13 |
| 77.86 | vless | 403.0 | 162.9 | 18.45 | 8.89 | 9.2 | 8.99 | 20.0 | Au1rxx-base64 | 95.40.100.129 |
| 77.82 | hysteria2 | 302.1 | 725.0 | 20.79 | 0.0 | 10.0 | 14.21 | 13.82 | mheidari-all | 138.124.68.188 |
| 77.8 | trojan | 301.3 | 561.4 | 20.8 | 0.0 | 10.0 | 14.66 | 20.0 | Au1rxx-base64 | 44.247.89.62 |
| 77.78 | shadowsocks | 295.8 | 678.2 | 20.93 | 0.0 | 10.0 | 13.94 | 20.0 | Au1rxx-base64 | 37.19.198.243 |
| 77.63 | trojan | 310.1 | 588.1 | 20.6 | 0.0 | 10.0 | 14.66 | 20.0 | Au1rxx-base64 | 44.244.3.114 |
| 77.6 | shadowsocks | 216.5 | 575.4 | 22.77 | 0.0 | 9.89 | 13.94 | 20.0 | Au1rxx-base64 | 156.146.38.169 |
| 77.42 | trojan | 322.7 | 623.4 | 20.31 | 0.0 | 10.0 | 14.66 | 20.0 | Au1rxx-base64 | 34.210.213.17 |
| 77.42 | http | 337.4 | 703.9 | 19.97 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.33 |
| 77.38 | shadowsocks | 273.8 | 554.7 | 21.44 | 0.0 | 9.88 | 13.94 | 20.0 | Au1rxx-base64 | 108.181.0.177 |
| 77.35 | shadowsocks | 321.5 | 729.2 | 20.34 | 0.0 | 10.0 | 13.94 | 20.0 | Au1rxx-base64 | 37.19.198.244 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | 0.963 | 807 | 1994 | prefer |
| zhangkai | 0.999 | 1.0 | 127 | 159 | prefer |
| mheidari-all | 0.971 | 0.899 | 99 | 16375 | prefer |
| Surfboard-tg-mixed | 0.794 | 0.717 | 145 | 5800 | prefer |
| 10ium-ScrapeCategorize-Vless | 0.335 | 1.0 | 1 | 4990 | observe |
| nscl5-all | 0.335 | 1.0 | 1 | 2601 | observe |
| Au1rxx-clash | 0.255 | None | 0 | 1994 | observe |
| Epodonios-all | 0.255 | None | 0 | 6483 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3989 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7383 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4502 | observe |
| barry-far-vless | 0.255 | None | 0 | 4839 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 3950 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |
| 10ium-HighSpeed | 0.209 | None | 0 | 839 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | TimeoutError | - | 24 |
| geo | TimeoutError | - | 23 |
| geo | ClientOSError | - | 17 |
| speed | TimeoutError | - | 16 |
| 204 | ClientOSError | - | 6 |
| cn-block | TimeoutError | - | 6 |
| speed | ClientOSError | - | 5 |
| cn-block | ClientOSError | - | 5 |
| 204 | ProxyError | - | 4 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
