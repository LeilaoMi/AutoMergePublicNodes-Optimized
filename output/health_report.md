# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-11 07:19:39 |
| 运行耗时 | 230.9s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 84663 |
| 去重后节点 | 24209 |
| TCP 可达 | 3000 |
| 真实可用 | 495 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 24209 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.2 |
| geo | 1.3 |
| tcp | 36.6 |
| probe | 51.0 |
| real_test | 106.8 |
| generate | 29.9 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 49256 |
| vmess | 13332 |
| trojan | 10676 |
| shadowsocks | 9835 |
| hysteria2 | 1301 |
| socks | 74 |
| http | 73 |
| shadowsocksr | 65 |
| anytls | 26 |
| hysteria | 13 |
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
| 83.97 | hysteria2 | 243.5 | 671.5 | 22.14 | 0.0 | 10.0 | 14.17 | 18.76 | Au1rxx-base64 | 159.223.157.129 |
| 81.41 | shadowsocks | 226.2 | 624.4 | 22.54 | 0.0 | 10.0 | 14.11 | 18.76 | Au1rxx-base64 | 37.19.198.160 |
| 81.12 | shadowsocks | 239.0 | 664.2 | 22.25 | 0.0 | 10.0 | 14.11 | 18.76 | Au1rxx-base64 | 37.19.198.244 |
| 80.96 | shadowsocks | 245.8 | 682.1 | 22.09 | 0.0 | 10.0 | 14.11 | 18.76 | Au1rxx-base64 | 37.19.198.243 |
| 80.81 | shadowsocks | 252.3 | 702.5 | 21.94 | 0.0 | 10.0 | 14.11 | 18.76 | Au1rxx-base64 | 37.19.198.236 |
| 80.06 | shadowsocks | 262.9 | 683.0 | 21.69 | 0.0 | 10.0 | 14.11 | 18.76 | Au1rxx-base64 | 68.168.222.210 |
| 77.87 | shadowsocks | 282.6 | 649.6 | 21.24 | 0.0 | 10.0 | 14.11 | 18.76 | Au1rxx-base64 | 156.146.38.170 |
| 77.85 | shadowsocks | 274.8 | 631.9 | 21.42 | 0.0 | 10.0 | 14.11 | 18.76 | Au1rxx-base64 | 156.146.38.169 |
| 77.24 | shadowsocks | 282.1 | 655.9 | 21.25 | 0.0 | 10.0 | 14.11 | 18.76 | Au1rxx-base64 | 156.146.38.168 |
| 77.08 | trojan | 293.5 | 636.5 | 20.98 | 0.0 | 10.0 | 13.63 | 18.76 | Au1rxx-base64 | 64.94.95.118 |
| 76.72 | trojan | 294.8 | 646.4 | 20.95 | 0.0 | 10.0 | 13.63 | 18.76 | Au1rxx-base64 | 64.94.95.117 |
| 76.64 | trojan | 294.1 | 642.5 | 20.97 | 0.0 | 10.0 | 13.63 | 18.76 | Au1rxx-base64 | 64.94.95.114 |
| 76.11 | hysteria2 | 355.1 | 691.3 | 19.56 | 0.0 | 10.0 | 14.17 | 18.76 | Au1rxx-base64 | 62.210.124.146 |
| 76.05 | trojan | 298.4 | 650.6 | 20.87 | 0.0 | 10.0 | 13.63 | 18.76 | Au1rxx-base64 | 64.94.95.115 |
| 75.22 | hysteria2 | 385.8 | 739.9 | 18.85 | 0.0 | 10.0 | 14.17 | 18.76 | Au1rxx-base64 | 144.31.207.60 |
| 74.29 | hysteria2 | 425.9 | 870.4 | 17.92 | 0.0 | 9.87 | 14.17 | 18.76 | Au1rxx-base64 | 5.255.102.165 |
| 72.94 | shadowsocks | 277.5 | 638.6 | 21.35 | 0.0 | 10.0 | 14.11 | 18.76 | Au1rxx-base64 | 156.146.38.167 |
| 72.93 | hysteria2 | 470.4 | 906.2 | 16.89 | 0.0 | 9.98 | 14.17 | 18.76 | Au1rxx-base64 | 91.196.32.163 |
| 72.36 | vless | 226.1 | 652.0 | 22.54 | 0.0 | 10.0 | 6.06 | 18.76 | Au1rxx-base64 | usa.anonch.org |
| 72.36 | shadowsocks | 366.8 | 732.0 | 19.29 | 0.0 | 10.0 | 14.11 | 18.76 | Au1rxx-base64 | 173.244.56.6 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.983 | 1.0 | 49 | 67 | prefer |
| Au1rxx-base64 | 0.949 | 0.895 | 380 | 1409 | prefer |
| Surfboard-tg-mixed | 0.792 | 0.716 | 102 | 6265 | prefer |
| DeltaKronecker-all | 0.397 | 0.308 | 39 | 5522 | observe |
| mheidari-all | 0.29 | 0.204 | 103 | 20272 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5419 | observe |
| Epodonios-all | 0.255 | None | 0 | 6871 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7470 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5103 | observe |
| barry-far-vless | 0.255 | None | 0 | 5410 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5209 | observe |
| nscl5-all | 0.239 | None | 0 | 1607 | observe |
| Au1rxx-clash | 0.231 | None | 0 | 1409 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 46 |
| geo | ClientOSError | - | 44 |
| speed | TimeoutError | - | 29 |
| 204 | TimeoutError | - | 18 |
| speed | ClientOSError | - | 17 |
| 204 | ProxyError | - | 11 |
| cn-block | TimeoutError | - | 5 |
| cn-block | ProxyError | - | 4 |
| 204 | ClientOSError | - | 3 |
| cn-block | ClientOSError | - | 3 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
