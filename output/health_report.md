# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-19 18:48:26 |
| 运行耗时 | 402.8s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 93105 |
| 去重后节点 | 24449 |
| TCP 可达 | 3000 |
| 真实可用 | 1236 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 24449 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.4 |
| geo | 0.5 |
| tcp | 38.2 |
| probe | 80.1 |
| real_test | 232.9 |
| generate | 43.8 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 50809 |
| trojan | 19388 |
| shadowsocks | 11004 |
| vmess | 9600 |
| hysteria2 | 1738 |
| shadowsocksr | 202 |
| http | 165 |
| socks | 136 |
| anytls | 36 |
| hysteria | 15 |
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
| 85.18 | trojan | 193.3 | 497.4 | 23.3 | 0.0 | 10.0 | 14.88 | 20.0 | Au1rxx-base64 | 128.14.181.220 |
| 84.18 | trojan | 189.9 | 491.4 | 23.38 | 0.0 | 10.0 | 14.88 | 18.92 | mheidari-all | 14.1.28.76 |
| 83.2 | trojan | 253.7 | 557.0 | 21.9 | 0.0 | 10.0 | 14.88 | 18.92 | mheidari-all | 44.246.163.102 |
| 82.77 | hysteria2 | 219.8 | 508.9 | 22.69 | 0.0 | 10.0 | 12.0 | 19.08 | Surfboard-tg-mixed | 150.241.102.127 |
| 82.6 | vless | 241.9 | 509.6 | 22.18 | 0.0 | 10.0 | 10.8 | 20.0 | Au1rxx-base64 | 150.241.102.202 |
| 82.37 | vless | 225.1 | 587.4 | 22.57 | 0.0 | 10.0 | 10.8 | 20.0 | Au1rxx-base64 | 38.244.21.216 |
| 82.26 | shadowsocks | 219.3 | 516.3 | 22.7 | 0.0 | 10.0 | 13.56 | 20.0 | Au1rxx-base64 | 149.22.95.183 |
| 82.05 | trojan | 303.6 | 673.3 | 20.75 | 0.0 | 10.0 | 14.88 | 18.92 | mheidari-all | 54.244.169.225 |
| 81.92 | shadowsocks | 234.2 | 510.3 | 22.36 | 0.0 | 10.0 | 13.56 | 20.0 | Au1rxx-base64 | 173.244.56.9 |
| 81.58 | trojan | 268.0 | 567.8 | 21.57 | 0.0 | 10.0 | 14.88 | 20.0 | Au1rxx-base64 | 34.220.224.252 |
| 81.2 | shadowsocks | 196.9 | 483.0 | 23.22 | 0.0 | 10.0 | 13.56 | 18.92 | mheidari-all | 108.181.118.10 |
| 81.06 | trojan | 309.2 | 704.4 | 20.62 | 0.0 | 10.0 | 14.88 | 20.0 | Au1rxx-base64 | 35.92.245.6 |
| 81.04 | trojan | 240.3 | 495.1 | 22.22 | 0.0 | 10.0 | 14.88 | 18.92 | mheidari-all | 44.251.158.80 |
| 80.64 | shadowsocks | 221.0 | 547.6 | 22.66 | 0.0 | 10.0 | 13.56 | 18.92 | mheidari-all | 108.181.0.177 |
| 80.56 | trojan | 325.1 | 746.4 | 20.25 | 0.0 | 10.0 | 14.88 | 20.0 | Au1rxx-base64 | 34.222.243.142 |
| 80.37 | trojan | 331.7 | 775.4 | 20.1 | 0.0 | 10.0 | 14.88 | 20.0 | Au1rxx-base64 | 54.213.46.211 |
| 80.28 | trojan | 314.4 | 736.5 | 20.5 | 0.0 | 10.0 | 14.88 | 20.0 | Au1rxx-base64 | 35.91.138.234 |
| 80.2 | trojan | 192.8 | 492.5 | 23.32 | 0.0 | 10.0 | 14.88 | 20.0 | Au1rxx-base64 | 162.221.197.83 |
| 80.16 | trojan | 270.9 | 600.6 | 21.51 | 0.0 | 10.0 | 14.88 | 20.0 | Au1rxx-base64 | 44.247.89.62 |
| 80.11 | trojan | 284.0 | 613.8 | 21.2 | 0.0 | 10.0 | 14.88 | 18.92 | mheidari-all | 35.88.210.26 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | 0.98 | 691 | 1890 | prefer |
| mheidari-all | 1.0 | 0.945 | 293 | 20423 | prefer |
| zhangkai | 0.988 | 0.991 | 113 | 144 | prefer |
| Surfboard-tg-mixed | 0.866 | 0.789 | 213 | 6336 | prefer |
| nscl5-all | 0.335 | 1.0 | 1 | 3330 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5067 | observe |
| Epodonios-all | 0.255 | None | 0 | 7060 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7318 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5003 | observe |
| barry-far-vless | 0.255 | None | 0 | 5325 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4086 | observe |
| Au1rxx-clash | 0.251 | None | 0 | 1890 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| DeltaKronecker-all | 0.24 | 0.25 | 4 | 6390 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | TimeoutError | - | 20 |
| cn-block | TimeoutError | - | 14 |
| geo | TimeoutError | - | 10 |
| speed | TimeoutError | - | 10 |
| geo | ClientOSError | - | 9 |
| 204 | ProxyError | - | 7 |
| cn-block | ClientOSError | - | 4 |
| speed | ClientOSError | - | 3 |
| 204 | ClientOSError | - | 3 |
| cn-block | ProxyError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
