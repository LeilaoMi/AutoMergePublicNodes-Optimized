# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-25 13:51:48 |
| 运行耗时 | 320.0s |
| 订阅源总数 | 107 |
| 健康订阅源 | 102 |
| 原始节点 | 78946 |
| 去重后节点 | 22525 |
| TCP 可达 | 3000 |
| 真实可用 | 821 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22525 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.2 |
| geo | 1.1 |
| tcp | 31.3 |
| probe | 65.2 |
| real_test | 180.3 |
| generate | 36.9 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 44190 |
| trojan | 14069 |
| vmess | 10127 |
| shadowsocks | 9877 |
| hysteria2 | 432 |
| http | 81 |
| shadowsocksr | 76 |
| socks | 67 |
| hysteria | 15 |
| tuic | 11 |
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
| 78.62 | trojan | 291.6 | 804.1 | 21.03 | 0.0 | 9.63 | 13.74 | 17.22 | Au1rxx-base64 | 153.75.250.171 |
| 77.78 | shadowsocks | 227.7 | 633.9 | 22.51 | 0.0 | 10.0 | 12.37 | 16.9 | mheidari-all | 37.19.198.236 |
| 77.6 | shadowsocks | 226.8 | 632.1 | 22.53 | 0.0 | 9.48 | 12.37 | 17.22 | Au1rxx-base64 | 37.19.198.243 |
| 77.45 | shadowsocks | 232.9 | 646.5 | 22.39 | 0.0 | 9.47 | 12.37 | 17.22 | Au1rxx-base64 | 37.19.198.160 |
| 76.54 | shadowsocks | 272.5 | 762.7 | 21.47 | 0.0 | 9.48 | 12.37 | 17.22 | Au1rxx-base64 | 37.19.198.244 |
| 74.33 | shadowsocks | 299.2 | 698.9 | 20.85 | 0.0 | 9.46 | 12.37 | 17.22 | Au1rxx-base64 | 156.146.38.170 |
| 73.84 | trojan | 336.6 | 611.5 | 19.99 | 0.0 | 9.6 | 13.74 | 17.22 | Au1rxx-base64 | 163.245.196.68 |
| 73.65 | shadowsocks | 321.4 | 739.7 | 20.34 | 0.0 | 9.47 | 12.37 | 17.22 | Au1rxx-base64 | 108.181.57.93 |
| 73.49 | shadowsocks | 280.5 | 651.7 | 21.28 | 0.0 | 9.46 | 12.37 | 17.22 | Au1rxx-base64 | 156.146.38.168 |
| 72.65 | trojan | 439.7 | 1168.8 | 17.6 | 0.0 | 10.0 | 13.74 | 15.58 | DeltaKronecker-all | 64.74.163.118 |
| 72.07 | shadowsocks | 336.5 | 818.4 | 19.99 | 0.0 | 9.47 | 12.37 | 17.22 | Au1rxx-base64 | 156.146.38.169 |
| 71.5 | shadowsocks | 339.3 | 875.6 | 19.92 | 0.0 | 9.49 | 12.37 | 17.22 | Au1rxx-base64 | 185.196.61.82 |
| 70.75 | hysteria2 | 370.2 | 704.7 | 19.21 | 0.0 | 9.42 | 12.0 | 17.22 | Au1rxx-base64 | 62.210.124.146 |
| 70.71 | trojan | 428.5 | 757.2 | 17.86 | 0.0 | 10.0 | 13.74 | 16.9 | mheidari-all | 8.6.112.6 |
| 70.14 | shadowsocks | 302.0 | 699.6 | 20.79 | 0.0 | 9.47 | 12.37 | 17.22 | Au1rxx-base64 | 156.146.38.167 |
| 69.82 | vless | 444.1 | 1285.4 | 17.5 | 0.0 | 10.0 | 5.42 | 16.9 | mheidari-all | 47.89.186.170 |
| 69.55 | trojan | 425.6 | 761.3 | 17.93 | 0.0 | 10.0 | 13.74 | 15.58 | DeltaKronecker-all | 5.10.214.34 |
| 69.51 | trojan | 466.3 | 808.7 | 16.98 | 0.0 | 10.0 | 13.74 | 16.9 | mheidari-all | 104.18.152.208 |
| 69.4 | trojan | 428.8 | 750.6 | 17.85 | 0.0 | 10.0 | 13.74 | 15.58 | DeltaKronecker-all | 172.64.229.75 |
| 69.3 | trojan | 430.3 | 758.8 | 17.82 | 0.0 | 10.0 | 13.74 | 15.58 | DeltaKronecker-all | 8.6.112.139 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.992 | 1.0 | 76 | 119 | prefer |
| Au1rxx-base64 | 0.92 | 0.891 | 293 | 803 | prefer |
| mheidari-all | 0.858 | 0.779 | 399 | 17158 | prefer |
| DeltaKronecker-all | 0.792 | 0.714 | 182 | 5838 | prefer |
| Surfboard-tg-mixed | 0.775 | 0.702 | 57 | 5379 | prefer |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| tg-LonUp_M | 0.262 | 1.0 | 1 | 180 | observe |
| roosterkid-openproxylist-v2ray | 0.261 | 1.0 | 1 | 150 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4879 | observe |
| Epodonios-all | 0.255 | None | 0 | 6540 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3969 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6338 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4058 | observe |
| barry-far-vless | 0.255 | None | 0 | 4746 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5009 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 57 |
| speed | ClientOSError | - | 40 |
| cn-block | TimeoutError | - | 27 |
| 204 | ProxyError | - | 20 |
| 204 | TimeoutError | - | 15 |
| geo | ClientOSError | - | 8 |
| cn-block | ClientOSError | - | 8 |
| cn-block | ProxyError | - | 6 |
| speed | TimeoutError | - | 4 |
| 204 | ClientOSError | - | 4 |
| geo | ProxyError | - | 2 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
