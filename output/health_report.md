# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-11 13:41:56 |
| 运行耗时 | 172.9s |
| 订阅源总数 | 107 |
| 健康订阅源 | 102 |
| 原始节点 | 76522 |
| 去重后节点 | 24023 |
| TCP 可达 | 3000 |
| 真实可用 | 295 |
| Verified 输出 | 295 |
| Global 输出 | 300 |
| All 输出 | 24023 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.5 |
| geo | 1.4 |
| tcp | 31.7 |
| probe | 45.6 |
| real_test | 62.9 |
| generate | 26.8 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 43762 |
| trojan | 12093 |
| vmess | 10577 |
| shadowsocks | 9426 |
| hysteria2 | 280 |
| shadowsocksr | 150 |
| http | 135 |
| socks | 90 |
| hysteria | 8 |
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
| 79.44 | shadowsocks | 224.1 | 602.9 | 22.59 | 0.0 | 10.0 | 12.63 | 18.22 | mheidari-all | 198.98.53.130 |
| 78.41 | shadowsocks | 246.9 | 647.8 | 22.06 | 0.0 | 10.0 | 12.63 | 18.22 | mheidari-all | 108.181.57.93 |
| 75.3 | trojan | 339.8 | 756.5 | 19.91 | 0.0 | 10.0 | 12.69 | 18.22 | mheidari-all | 45.32.195.168 |
| 74.85 | vmess | 391.2 | 1126.3 | 18.72 | 0.0 | 10.0 | 13.33 | 17.3 | Surfboard-tg-mixed | 67.220.95.3 |
| 74.45 | shadowsocks | 241.7 | 667.8 | 22.18 | 0.0 | 10.0 | 12.63 | 13.64 | Au1rxx-base64 | 37.19.198.244 |
| 74.43 | shadowsocks | 242.6 | 673.4 | 22.16 | 0.0 | 10.0 | 12.63 | 13.64 | Au1rxx-base64 | 37.19.198.236 |
| 74.34 | shadowsocks | 246.8 | 684.9 | 22.07 | 0.0 | 10.0 | 12.63 | 13.64 | Au1rxx-base64 | 37.19.198.243 |
| 73.64 | trojan | 394.3 | 908.0 | 18.65 | 0.0 | 10.0 | 12.69 | 18.22 | mheidari-all | 64.94.95.118 |
| 72.42 | shadowsocks | 231.7 | 627.1 | 22.41 | 0.0 | 10.0 | 12.63 | 18.22 | mheidari-all | 147.90.234.133 |
| 70.99 | trojan | 391.7 | 541.5 | 18.71 | 0.0 | 10.0 | 12.69 | 17.3 | Surfboard-tg-mixed | 104.21.52.100 |
| 70.96 | shadowsocks | 279.7 | 634.3 | 21.3 | 0.0 | 10.0 | 12.63 | 13.64 | Au1rxx-base64 | 156.146.38.169 |
| 70.77 | trojan | 334.1 | 589.7 | 20.05 | 0.0 | 10.0 | 12.69 | 15.18 | DeltaKronecker-all | 104.16.99.215 |
| 70.73 | vmess | 477.7 | 1348.1 | 16.72 | 0.0 | 10.0 | 13.33 | 15.18 | DeltaKronecker-all | 67.220.85.46 |
| 70.57 | shadowsocks | 319.5 | 766.8 | 20.38 | 0.0 | 10.0 | 12.63 | 13.64 | Au1rxx-base64 | 156.146.38.167 |
| 70.48 | trojan | 360.3 | 779.4 | 19.44 | 0.0 | 10.0 | 12.69 | 13.64 | Au1rxx-base64 | 149.28.241.235 |
| 69.73 | trojan | 419.4 | 1007.5 | 18.07 | 0.0 | 10.0 | 12.69 | 15.18 | DeltaKronecker-all | 64.94.95.115 |
| 69.42 | trojan | 391.6 | 928.1 | 18.71 | 0.0 | 10.0 | 12.69 | 15.18 | DeltaKronecker-all | 64.94.95.117 |
| 68.93 | trojan | 428.3 | 1020.2 | 17.86 | 0.0 | 10.0 | 12.69 | 15.18 | DeltaKronecker-all | 64.94.95.114 |
| 68.82 | trojan | 371.7 | 594.5 | 19.17 | 0.0 | 10.0 | 12.69 | 15.18 | DeltaKronecker-all | 104.16.97.215 |
| 68.78 | trojan | 392.6 | 597.4 | 18.69 | 0.0 | 10.0 | 12.69 | 17.3 | Surfboard-tg-mixed | 104.16.71.109 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| Surfboard-tg-mixed | 0.904 | 0.83 | 100 | 5543 | prefer |
| Au1rxx-base64 | 0.804 | 0.821 | 28 | 103 | prefer |
| mheidari-all | 0.802 | 0.727 | 77 | 16510 | prefer |
| DeltaKronecker-all | 0.645 | 0.566 | 166 | 7969 | observe |
| Barabama-yudou | 0.318 | 1.0 | 2 | 166 | observe |
| nscl5-all | 0.303 | 1.0 | 1 | 1207 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 3953 | observe |
| Epodonios-all | 0.255 | None | 0 | 6467 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3968 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6527 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4147 | observe |
| barry-far-vless | 0.255 | None | 0 | 4696 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5423 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | ProxyError | - | 24 |
| geo | TimeoutError | - | 19 |
| speed | ClientOSError | - | 16 |
| cn-block | ProxyError | - | 13 |
| geo | ProxyError | - | 10 |
| geo | ClientOSError | - | 8 |
| cn-block | ClientOSError | - | 7 |
| speed | ProxyError | - | 7 |
| 204 | TimeoutError | - | 4 |
| 204 | ClientOSError | - | 4 |
| cn-block | TimeoutError | - | 3 |
| speed | TimeoutError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 295 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
