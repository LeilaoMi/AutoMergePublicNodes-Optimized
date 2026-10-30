# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-30 22:33:40 |
| 运行耗时 | 301.1s |
| 订阅源总数 | 107 |
| 健康订阅源 | 87 |
| 原始节点 | 80795 |
| 去重后节点 | 26300 |
| TCP 可达 | 3000 |
| 真实可用 | 546 |
| Verified 输出 | 107 |
| Global 输出 | 300 |
| All 输出 | 26300 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.0 |
| geo | 1.5 |
| tcp | 77.0 |
| probe | 82.7 |
| real_test | 89.6 |
| china_check | 32.5 |
| write_verified | 0.1 |
| generate | 11.8 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 49012 |
| vmess | 14032 |
| shadowsocks | 8553 |
| trojan | 7350 |
| hysteria2 | 1494 |
| shadowsocksr | 154 |
| http | 111 |
| socks | 51 |
| tuic | 14 |
| anytls | 13 |
| hysteria | 11 |

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
| 96.46 | hysteria2 | 273.2 | 2.4 | 21.45 | 14.91 | 10.0 | 13.0 | 18.6 | Au1rxx-base64 | 129.213.91.185 |
| 94.88 | shadowsocks | 243.9 | 0.7 | 22.13 | 14.97 | 10.0 | 13.18 | 18.6 | Au1rxx-base64 | 156.146.38.168 |
| 93.81 | shadowsocks | 258.8 | 20.1 | 21.79 | 14.24 | 10.0 | 13.18 | 18.6 | Au1rxx-base64 | 156.146.38.170 |
| 93.5 | shadowsocks | 267.6 | 22.8 | 21.58 | 14.14 | 10.0 | 13.18 | 18.6 | Au1rxx-base64 | 156.146.38.167 |
| 93.16 | trojan | 263.3 | 1.1 | 21.68 | 14.96 | 9.55 | 10.87 | 18.6 | Au1rxx-base64 | 66.163.114.132 |
| 92.52 | trojan | 272.0 | 0.6 | 21.48 | 14.98 | 10.0 | 10.87 | 18.6 | Au1rxx-base64 | 66.163.114.45 |
| 92.18 | shadowsocks | 299.1 | 3.3 | 20.85 | 14.87 | 10.0 | 13.18 | 18.6 | Au1rxx-base64 | 37.19.198.160 |
| 91.82 | trojan | 264.0 | 0.7 | 21.67 | 14.97 | 8.26 | 10.87 | 18.6 | Au1rxx-base64 | 66.163.114.166 |
| 91.42 | trojan | 266.8 | 0.2 | 21.6 | 14.99 | 8.38 | 10.87 | 18.6 | Au1rxx-base64 | 66.163.114.245 |
| 91.3 | trojan | 270.4 | 5.7 | 21.52 | 14.79 | 8.26 | 10.87 | 18.6 | Au1rxx-base64 | 66.163.114.106 |
| 91.08 | shadowsocks | 279.9 | 2.6 | 21.3 | 14.9 | 7.1 | 13.18 | 18.6 | Au1rxx-base64 | 156.146.38.169 |
| 90.87 | shadowsocks | 316.7 | 2.1 | 20.45 | 14.92 | 10.0 | 13.18 | 18.6 | Au1rxx-base64 | 185.230.230.18 |
| 90.82 | trojan | 270.0 | 4.5 | 21.53 | 14.83 | 8.26 | 10.87 | 18.6 | Au1rxx-base64 | 66.163.114.114 |
| 90.64 | shadowsocks | 340.0 | 11.0 | 19.91 | 14.59 | 10.0 | 13.18 | 18.6 | Au1rxx-base64 | 37.19.198.243 |
| 90.62 | trojan | 272.2 | 4.2 | 21.48 | 14.84 | 8.24 | 10.87 | 18.6 | Au1rxx-base64 | 66.163.114.126 |
| 90.25 | shadowsocks | 354.6 | 2.4 | 19.57 | 14.91 | 10.0 | 13.18 | 18.6 | Au1rxx-base64 | 37.19.198.236 |
| 89.41 | trojan | 267.3 | 5.2 | 21.59 | 14.81 | 6.04 | 10.87 | 18.6 | Au1rxx-base64 | 216.152.155.54 |
| 89.31 | shadowsocks | 300.9 | 3.7 | 20.81 | 14.86 | 10.0 | 13.18 | 18.6 | Au1rxx-base64 | 37.19.198.244 |
| 89.16 | shadowsocks | 285.6 | 2.1 | 21.17 | 14.92 | 10.0 | 13.18 | 18.6 | Au1rxx-base64 | 95.215.201.18 |
| 88.84 | vless | 291.1 | 5.9 | 21.04 | 14.78 | 10.0 | 8.73 | 18.6 | Au1rxx-base64 | 144.202.126.147 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.957 | 0.966 | 29 | 550 | prefer |
| Au1rxx-base64 | 0.951 | 0.883 | 341 | 1751 | prefer |
| Surfboard-tg-mixed | 0.863 | 0.787 | 164 | 7917 | prefer |
| mheidari-all | 0.813 | 0.737 | 114 | 14611 | prefer |
| xiaoji235-airport-v2ray-all | 0.438 | 1.0 | 3 | 6752 | observe |
| ermaozi-get_subscribe | 0.328 | 1.0 | 2 | 430 | observe |
| ninja-vless | 0.327 | 1.0 | 1 | 1791 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4960 | observe |
| DeltaKronecker-all | 0.255 | None | 0 | 2724 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 10557 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5777 | observe |
| barry-far-vless | 0.255 | None | 0 | 6013 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4459 | observe |
| Au1rxx-clash | 0.245 | None | 0 | 1751 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 55 |
| geo | ClientOSError | - | 16 |
| cn-block | ClientOSError | - | 13 |
| 204 | TimeoutError | - | 6 |
| geo | ProxyError | - | 4 |
| 204 | ProxyError | - | 3 |
| cn-block | TimeoutError | - | 3 |
| speed | ClientOSError | - | 2 |
| cn-block | ProxyError | - | 1 |
| speed | ClientConnectionResetError | - | 1 |
| 204 | ClientOSError | - | 1 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 80 | 107 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
