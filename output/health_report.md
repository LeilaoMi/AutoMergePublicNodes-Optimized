# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-29 19:28:40 |
| 运行耗时 | 244.6s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 79381 |
| 去重后节点 | 22734 |
| TCP 可达 | 3000 |
| 真实可用 | 431 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22734 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.6 |
| geo | 1.3 |
| tcp | 31.4 |
| probe | 54.0 |
| real_test | 111.4 |
| generate | 40.9 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 46492 |
| vmess | 10968 |
| trojan | 10595 |
| shadowsocks | 10571 |
| hysteria2 | 514 |
| shadowsocksr | 75 |
| http | 73 |
| socks | 52 |
| anytls | 26 |
| hysteria | 12 |
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
| 81.16 | hysteria2 | 227.6 | 630.4 | 22.51 | 0.0 | 10.0 | 12.35 | 17.4 | Au1rxx-base64 | 159.223.157.129 |
| 78.72 | shadowsocks | 239.7 | 656.2 | 22.23 | 0.0 | 10.0 | 13.09 | 17.4 | Au1rxx-base64 | 37.19.198.243 |
| 78.57 | shadowsocks | 246.0 | 681.0 | 22.08 | 0.0 | 10.0 | 13.09 | 17.4 | Au1rxx-base64 | 37.19.198.236 |
| 78.47 | trojan | 260.4 | 702.0 | 21.75 | 0.0 | 10.0 | 12.32 | 17.4 | Au1rxx-base64 | 153.75.250.171 |
| 75.67 | shadowsocks | 349.6 | 964.8 | 19.68 | 0.0 | 10.0 | 13.09 | 17.4 | Au1rxx-base64 | 68.168.222.210 |
| 75.54 | shadowsocks | 355.4 | 931.6 | 19.55 | 0.0 | 10.0 | 13.09 | 17.4 | Au1rxx-base64 | 146.70.34.226 |
| 75.1 | vless | 244.3 | 656.9 | 22.12 | 0.0 | 10.0 | 8.58 | 17.4 | Au1rxx-base64 | 167.99.48.117 |
| 74.84 | vless | 337.9 | 916.7 | 19.96 | 0.0 | 10.0 | 8.58 | 17.4 | Au1rxx-base64 | 45.138.100.226 |
| 74.69 | trojan | 296.0 | 645.8 | 20.93 | 0.0 | 10.0 | 12.32 | 17.4 | Au1rxx-base64 | 64.94.95.118 |
| 74.62 | trojan | 297.6 | 648.4 | 20.89 | 0.0 | 10.0 | 12.32 | 17.4 | Au1rxx-base64 | 64.94.95.115 |
| 74.42 | shadowsocks | 300.9 | 735.1 | 20.81 | 0.0 | 10.0 | 13.09 | 17.4 | Au1rxx-base64 | 68.168.114.226 |
| 74.39 | trojan | 305.9 | 638.8 | 20.7 | 0.0 | 10.0 | 12.32 | 17.4 | Au1rxx-base64 | 64.94.95.117 |
| 74.25 | trojan | 297.1 | 646.2 | 20.9 | 0.0 | 10.0 | 12.32 | 17.4 | Au1rxx-base64 | 64.94.95.114 |
| 73.82 | vless | 213.5 | 580.3 | 22.84 | 0.0 | 10.0 | 8.58 | 17.4 | Au1rxx-base64 | 88.218.44.4 |
| 73.74 | shadowsocks | 239.0 | 659.8 | 22.25 | 0.0 | 10.0 | 13.09 | 17.4 | Au1rxx-base64 | 37.19.198.160 |
| 73.45 | trojan | 394.5 | 984.7 | 18.64 | 0.0 | 10.0 | 12.32 | 17.4 | Au1rxx-base64 | 148.72.168.35 |
| 73.34 | trojan | 303.4 | 730.0 | 20.76 | 0.0 | 10.0 | 12.32 | 13.4 | DeltaKronecker-all | 64.74.163.118 |
| 72.81 | trojan | 315.3 | 657.9 | 20.48 | 0.0 | 10.0 | 12.32 | 17.4 | Au1rxx-base64 | 163.245.196.68 |
| 72.21 | hysteria2 | 359.7 | 688.2 | 19.45 | 0.0 | 10.0 | 12.35 | 17.4 | Au1rxx-base64 | 62.210.124.146 |
| 71.97 | shadowsocks | 227.7 | 614.8 | 22.51 | 0.0 | 10.0 | 13.09 | 17.4 | Au1rxx-base64 | 198.98.53.130 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.989 | 1.0 | 70 | 84 | prefer |
| Au1rxx-base64 | 0.815 | 0.761 | 289 | 1384 | prefer |
| Surfboard-tg-mixed | 0.722 | 0.644 | 118 | 5853 | prefer |
| DeltaKronecker-all | 0.712 | 0.635 | 85 | 5519 | prefer |
| mheidari-all | 0.679 | 0.909 | 11 | 16105 | observe |
| xiaoji235-airport-v2ray-all | 0.329 | 1.0 | 1 | 1861 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5118 | observe |
| Epodonios-all | 0.255 | None | 0 | 6489 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3973 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6586 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4561 | observe |
| barry-far-vless | 0.255 | None | 0 | 4922 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5076 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| nscl5-all | 0.246 | None | 0 | 1774 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 36 |
| 204 | TimeoutError | - | 33 |
| cn-block | TimeoutError | - | 30 |
| speed | TimeoutError | - | 16 |
| 204 | ProxyError | - | 6 |
| cn-block | ClientOSError | - | 6 |
| speed | ClientOSError | - | 6 |
| geo | ClientOSError | - | 5 |
| 204 | ClientOSError | - | 4 |
| cn-block | ProxyError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
