# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-06 08:49:25 |
| 运行耗时 | 238.2s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 88936 |
| 去重后节点 | 24432 |
| TCP 可达 | 3000 |
| 真实可用 | 450 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 24432 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 18.4 |
| geo | 1.4 |
| tcp | 36.6 |
| probe | 45.4 |
| real_test | 86.9 |
| generate | 49.5 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 51846 |
| vmess | 13334 |
| trojan | 11885 |
| shadowsocks | 10161 |
| hysteria2 | 1453 |
| socks | 89 |
| shadowsocksr | 79 |
| anytls | 30 |
| http | 24 |
| hysteria | 21 |
| tuic | 14 |

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
| 85.77 | hysteria2 | 227.1 | 633.5 | 22.52 | 0.0 | 10.0 | 14.35 | 20.0 | Au1rxx-base64 | 159.223.157.129 |
| 85.42 | hysteria2 | 246.4 | 688.8 | 22.07 | 0.0 | 10.0 | 14.35 | 20.0 | Au1rxx-base64 | usa1.spectrumproxy.shop |
| 81.66 | hysteria2 | 409.2 | 1175.3 | 18.31 | 0.0 | 10.0 | 14.35 | 20.0 | Au1rxx-base64 | 138.124.68.188 |
| 81.46 | shadowsocks | 247.2 | 676.5 | 22.06 | 0.0 | 10.0 | 13.9 | 20.0 | Au1rxx-base64 | 68.168.222.210 |
| 81.09 | shadowsocks | 284.6 | 804.0 | 21.19 | 0.0 | 10.0 | 13.9 | 20.0 | Au1rxx-base64 | 37.19.198.236 |
| 79.66 | trojan | 363.9 | 1022.6 | 19.36 | 0.0 | 10.0 | 13.3 | 20.0 | Au1rxx-base64 | 153.75.250.171 |
| 79.4 | shadowsocks | 280.6 | 651.6 | 21.28 | 0.0 | 10.0 | 13.9 | 20.0 | Au1rxx-base64 | 156.146.38.169 |
| 79.34 | shadowsocks | 279.8 | 651.1 | 21.3 | 0.0 | 10.0 | 13.9 | 20.0 | Au1rxx-base64 | 156.146.38.168 |
| 78.31 | shadowsocks | 404.6 | 1157.2 | 18.41 | 0.0 | 10.0 | 13.9 | 20.0 | Au1rxx-base64 | 37.19.198.244 |
| 78.12 | trojan | 292.2 | 635.1 | 21.01 | 0.0 | 10.0 | 13.3 | 20.0 | Au1rxx-base64 | 64.94.95.114 |
| 78.06 | trojan | 297.3 | 648.0 | 20.9 | 0.0 | 10.0 | 13.3 | 20.0 | Au1rxx-base64 | 64.94.95.118 |
| 77.83 | trojan | 310.8 | 686.7 | 20.58 | 0.0 | 10.0 | 13.3 | 20.0 | Au1rxx-base64 | 64.94.95.117 |
| 77.81 | trojan | 299.7 | 656.0 | 20.84 | 0.0 | 10.0 | 13.3 | 20.0 | Au1rxx-base64 | 64.94.95.115 |
| 77.35 | hysteria2 | 352.8 | 684.4 | 19.61 | 0.0 | 10.0 | 14.35 | 20.0 | Au1rxx-base64 | 62.210.124.146 |
| 77.29 | trojan | 304.9 | 653.4 | 20.72 | 0.0 | 10.0 | 13.3 | 20.0 | Au1rxx-base64 | 163.245.196.68 |
| 77.03 | shadowsocks | 316.3 | 704.1 | 20.46 | 0.0 | 10.0 | 13.9 | 20.0 | Au1rxx-base64 | 108.181.57.93 |
| 76.15 | shadowsocks | 393.5 | 982.8 | 18.67 | 0.0 | 10.0 | 13.9 | 20.0 | Au1rxx-base64 | 156.146.38.167 |
| 75.6 | shadowsocks | 441.7 | 1130.7 | 17.55 | 0.0 | 10.0 | 13.9 | 20.0 | Au1rxx-base64 | 156.146.38.170 |
| 75.08 | shadowsocks | 303.6 | 596.7 | 20.75 | 0.0 | 10.0 | 13.9 | 20.0 | Au1rxx-base64 | 173.244.56.6 |
| 74.47 | shadowsocks | 354.8 | 1015.7 | 19.57 | 0.0 | 10.0 | 13.9 | 20.0 | Au1rxx-base64 | 37.19.198.160 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | 0.949 | 351 | 1409 | prefer |
| zhangkai | 0.956 | 1.0 | 20 | 25 | prefer |
| Surfboard-tg-mixed | 0.653 | 0.574 | 122 | 5873 | observe |
| DeltaKronecker-all | 0.555 | 0.529 | 17 | 5897 | observe |
| mheidari-all | 0.47 | 0.385 | 39 | 20781 | observe |
| nscl5-all | 0.32 | 1.0 | 1 | 1621 | observe |
| xiaoji235-airport-v2ray-all | 0.287 | 0.5 | 2 | 5214 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5219 | observe |
| Epodonios-all | 0.255 | None | 0 | 6505 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7196 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4677 | observe |
| barry-far-vless | 0.255 | None | 0 | 5049 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5212 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 31 |
| geo | ClientOSError | - | 26 |
| cn-block | TimeoutError | - | 10 |
| 204 | ClientOSError | - | 9 |
| 204 | TimeoutError | - | 7 |
| 204 | ProxyError | - | 6 |
| speed | TimeoutError | - | 5 |
| speed | ClientOSError | - | 4 |
| cn-block | ClientOSError | - | 4 |
| cn-block | ProxyError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
