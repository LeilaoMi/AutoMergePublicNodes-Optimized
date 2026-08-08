# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-08 18:49:03 |
| 运行耗时 | 217.7s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 83469 |
| 去重后节点 | 23607 |
| TCP 可达 | 3000 |
| 真实可用 | 401 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23607 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.0 |
| geo | 1.4 |
| tcp | 35.6 |
| probe | 45.7 |
| real_test | 85.8 |
| generate | 44.3 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 49005 |
| vmess | 13041 |
| trojan | 10099 |
| shadowsocks | 9792 |
| hysteria2 | 1330 |
| shadowsocksr | 74 |
| socks | 70 |
| http | 36 |
| hysteria | 13 |
| tuic | 8 |
| anytls | 1 |

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
| 84.38 | hysteria2 | 239.8 | 648.1 | 22.23 | 0.0 | 10.0 | 13.33 | 19.92 | Au1rxx-base64 | 159.223.157.129 |
| 84.18 | hysteria2 | 252.8 | 692.1 | 21.93 | 0.0 | 10.0 | 13.33 | 19.92 | Au1rxx-base64 | 138.124.68.188 |
| 83.64 | hysteria2 | 246.4 | 671.7 | 22.08 | 0.0 | 9.31 | 13.33 | 19.92 | Au1rxx-base64 | usa1.spectrumproxy.shop |
| 81.39 | shadowsocks | 248.0 | 659.6 | 22.04 | 0.0 | 10.0 | 13.43 | 19.92 | Au1rxx-base64 | 37.19.198.244 |
| 81.35 | shadowsocks | 249.6 | 661.1 | 22.0 | 0.0 | 10.0 | 13.43 | 19.92 | Au1rxx-base64 | 37.19.198.160 |
| 81.0 | shadowsocks | 264.9 | 705.7 | 21.65 | 0.0 | 10.0 | 13.43 | 19.92 | Au1rxx-base64 | 37.19.198.236 |
| 79.41 | shadowsocks | 247.0 | 625.4 | 22.06 | 0.0 | 10.0 | 13.43 | 19.92 | Au1rxx-base64 | 37.19.198.243 |
| 78.58 | shadowsocks | 284.8 | 662.6 | 21.18 | 0.0 | 10.0 | 13.43 | 19.92 | Au1rxx-base64 | 156.146.38.170 |
| 78.14 | trojan | 323.7 | 747.2 | 20.28 | 0.0 | 10.0 | 14.35 | 19.92 | Au1rxx-base64 | 64.94.95.117 |
| 77.89 | shadowsocks | 287.6 | 661.2 | 21.12 | 0.0 | 10.0 | 13.43 | 19.92 | Au1rxx-base64 | 156.146.38.168 |
| 77.81 | trojan | 339.9 | 762.9 | 19.91 | 0.0 | 10.0 | 14.35 | 19.92 | Au1rxx-base64 | 64.94.95.118 |
| 77.8 | trojan | 321.1 | 745.8 | 20.35 | 0.0 | 10.0 | 14.35 | 19.92 | Au1rxx-base64 | 64.94.95.114 |
| 76.95 | trojan | 330.6 | 759.9 | 20.12 | 0.0 | 10.0 | 14.35 | 19.92 | Au1rxx-base64 | 64.94.95.115 |
| 76.71 | shadowsocks | 301.5 | 716.3 | 20.8 | 0.0 | 10.0 | 13.43 | 19.92 | Au1rxx-base64 | 108.181.57.93 |
| 76.25 | hysteria2 | 352.6 | 683.9 | 19.62 | 0.0 | 10.0 | 13.33 | 19.92 | Au1rxx-base64 | 62.210.124.146 |
| 75.0 | hysteria2 | 420.8 | 867.3 | 18.04 | 0.0 | 10.0 | 13.33 | 19.92 | Au1rxx-base64 | 5.255.102.165 |
| 74.3 | shadowsocks | 339.7 | 698.2 | 19.91 | 0.0 | 10.0 | 13.43 | 19.92 | Au1rxx-base64 | 173.244.56.6 |
| 74.27 | shadowsocks | 331.8 | 704.5 | 20.1 | 0.0 | 10.0 | 13.43 | 19.92 | Au1rxx-base64 | 108.181.0.177 |
| 74.16 | hysteria2 | 449.9 | 944.7 | 17.36 | 0.0 | 10.0 | 13.33 | 19.92 | Au1rxx-base64 | 194.180.174.69 |
| 74.08 | vless | 420.7 | 1088.8 | 18.04 | 0.0 | 10.0 | 7.1 | 19.92 | Au1rxx-base64 | 128.254.207.163 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.989 | 0.93 | 341 | 1540 | prefer |
| zhangkai | 0.956 | 1.0 | 20 | 25 | prefer |
| mheidari-all | 0.84 | 0.882 | 17 | 17642 | prefer |
| Surfboard-tg-mixed | 0.68 | 0.603 | 78 | 6620 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5450 | observe |
| DeltaKronecker-all | 0.255 | 0.222 | 9 | 5347 | observe |
| Epodonios-all | 0.255 | None | 0 | 7201 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7604 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5385 | observe |
| barry-far-vless | 0.255 | None | 0 | 5666 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5127 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| nscl5-all | 0.241 | None | 0 | 1643 | observe |
| Au1rxx-clash | 0.237 | None | 0 | 1540 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | TimeoutError | - | 22 |
| cn-block | TimeoutError | - | 14 |
| speed | TimeoutError | - | 8 |
| 204 | ProxyError | - | 7 |
| cn-block | ClientOSError | - | 4 |
| geo | ClientOSError | - | 3 |
| geo | TimeoutError | - | 3 |
| 204 | ClientOSError | - | 2 |
| cn-block | ProxyError | - | 1 |
| speed | ClientOSError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
