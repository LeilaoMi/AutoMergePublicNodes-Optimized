# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-03 19:49:37 |
| 运行耗时 | 260.2s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 84754 |
| 去重后节点 | 25181 |
| TCP 可达 | 3000 |
| 真实可用 | 478 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 25181 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.1 |
| geo | 1.7 |
| tcp | 37.5 |
| probe | 56.8 |
| real_test | 126.8 |
| generate | 31.2 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 52045 |
| vmess | 12822 |
| shadowsocks | 10361 |
| trojan | 8535 |
| hysteria2 | 747 |
| http | 76 |
| socks | 74 |
| shadowsocksr | 72 |
| hysteria | 11 |
| tuic | 6 |
| anytls | 5 |

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
| 80.33 | hysteria2 | 258.7 | 652.6 | 21.79 | 0.0 | 10.0 | 13.64 | 16.0 | Au1rxx-base64 | 159.223.157.129 |
| 80.02 | hysteria2 | 276.3 | 712.0 | 21.38 | 0.0 | 10.0 | 13.64 | 16.0 | Au1rxx-base64 | 138.124.68.188 |
| 79.18 | hysteria2 | 274.1 | 702.5 | 21.43 | 0.0 | 9.11 | 13.64 | 16.0 | Au1rxx-base64 | usa1.spectrumproxy.shop |
| 77.04 | shadowsocks | 258.1 | 631.5 | 21.8 | 0.0 | 10.0 | 13.24 | 16.0 | Au1rxx-base64 | 156.146.38.169 |
| 77.02 | trojan | 269.9 | 620.6 | 21.53 | 0.0 | 10.0 | 13.2 | 16.0 | Au1rxx-base64 | 64.94.95.118 |
| 76.77 | shadowsocks | 270.0 | 671.2 | 21.53 | 0.0 | 10.0 | 13.24 | 16.0 | Au1rxx-base64 | 37.19.198.236 |
| 76.63 | trojan | 270.2 | 627.2 | 21.52 | 0.0 | 10.0 | 13.2 | 16.0 | Au1rxx-base64 | 64.94.95.114 |
| 76.6 | shadowsocks | 259.6 | 629.8 | 21.77 | 0.0 | 10.0 | 13.24 | 16.0 | Au1rxx-base64 | 156.146.38.168 |
| 76.56 | trojan | 300.0 | 735.6 | 20.83 | 0.0 | 10.0 | 13.2 | 16.0 | Au1rxx-base64 | 153.75.250.171 |
| 75.88 | shadowsocks | 288.3 | 714.5 | 21.1 | 0.0 | 10.0 | 13.24 | 16.0 | Au1rxx-base64 | 37.19.198.160 |
| 75.72 | shadowsocks | 315.1 | 617.7 | 20.48 | 0.0 | 10.0 | 13.24 | 16.0 | Au1rxx-base64 | 37.19.198.243 |
| 75.66 | trojan | 321.0 | 786.5 | 20.35 | 0.0 | 10.0 | 13.2 | 16.0 | Au1rxx-base64 | 64.94.95.115 |
| 75.5 | shadowsocks | 281.8 | 680.0 | 21.26 | 0.0 | 10.0 | 13.24 | 16.0 | Au1rxx-base64 | 37.19.198.244 |
| 75.3 | shadowsocks | 298.3 | 752.3 | 20.87 | 0.0 | 10.0 | 13.24 | 16.0 | Au1rxx-base64 | 156.146.38.167 |
| 75.02 | trojan | 301.1 | 723.7 | 20.81 | 0.0 | 10.0 | 13.2 | 16.0 | Au1rxx-base64 | 64.94.95.117 |
| 74.67 | shadowsocks | 346.2 | 725.5 | 19.76 | 0.0 | 10.0 | 13.24 | 16.0 | Au1rxx-base64 | 198.98.53.130 |
| 74.4 | vless | 316.5 | 803.5 | 20.45 | 0.0 | 10.0 | 7.95 | 16.0 | Au1rxx-base64 | 88.218.44.4 |
| 74.29 | trojan | 280.0 | 621.2 | 21.3 | 0.0 | 10.0 | 13.2 | 16.0 | Au1rxx-base64 | 163.245.196.68 |
| 74.22 | vless | 261.5 | 681.3 | 21.72 | 0.0 | 10.0 | 7.95 | 16.0 | Au1rxx-base64 | 216.152.147.28 |
| 72.11 | vless | 368.1 | 972.7 | 19.26 | 0.0 | 10.0 | 7.95 | 16.0 | Au1rxx-base64 | 45.138.100.226 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.989 | 1.0 | 67 | 92 | prefer |
| Au1rxx-base64 | 0.782 | 0.714 | 525 | 1718 | prefer |
| Surfboard-tg-mixed | 0.673 | 0.6 | 25 | 5168 | observe |
| mheidari-all | 0.446 | 0.625 | 8 | 18750 | observe |
| xiaoji235-airport-v2ray-all | 0.287 | 0.5 | 2 | 5127 | observe |
| tg-OutlineReleasedKey | 0.257 | 1.0 | 1 | 57 | observe |
| DeltaKronecker-all | 0.256 | 0.169 | 83 | 6205 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5285 | observe |
| Epodonios-all | 0.255 | None | 0 | 5757 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3996 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6825 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4147 | observe |
| barry-far-vless | 0.255 | None | 0 | 4498 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5152 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 118 |
| 204 | TimeoutError | - | 36 |
| speed | TimeoutError | - | 23 |
| geo | ClientOSError | - | 15 |
| 204 | ProxyError | - | 11 |
| cn-block | TimeoutError | - | 9 |
| cn-block | ClientOSError | - | 7 |
| speed | ClientOSError | - | 7 |
| cn-block | ProxyError | - | 3 |
| 204 | ClientOSError | - | 3 |
| geo | parse | TimeoutError | 1 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
