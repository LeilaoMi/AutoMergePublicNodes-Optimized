# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-30 13:16:36 |
| 运行耗时 | 323.1s |
| 订阅源总数 | 107 |
| 健康订阅源 | 87 |
| 原始节点 | 100257 |
| 去重后节点 | 27804 |
| TCP 可达 | 3000 |
| 真实可用 | 440 |
| Verified 输出 | 80 |
| Global 输出 | 300 |
| All 输出 | 27804 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 8.1 |
| geo | 1.6 |
| tcp | 87.9 |
| probe | 96.9 |
| real_test | 92.5 |
| china_check | 20.8 |
| write_verified | 0.0 |
| generate | 15.3 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 62067 |
| vmess | 14672 |
| shadowsocks | 10844 |
| trojan | 10095 |
| hysteria2 | 2210 |
| shadowsocksr | 166 |
| http | 114 |
| socks | 48 |
| tuic | 17 |
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
| 95.81 | trojan | 263.7 | 3.2 | 21.67 | 14.88 | 10.0 | 13.24 | 18.52 | Au1rxx-base64 | 66.163.114.45 |
| 94.63 | hysteria2 | 325.7 | 45.1 | 20.24 | 13.31 | 10.0 | 14.06 | 18.52 | Au1rxx-base64 | 129.213.91.185 |
| 94.45 | trojan | 263.1 | 2.8 | 21.69 | 14.9 | 8.6 | 13.24 | 18.52 | Au1rxx-base64 | 66.163.114.132 |
| 93.95 | shadowsocks | 260.1 | 3.9 | 21.76 | 14.85 | 10.0 | 12.82 | 18.52 | Au1rxx-base64 | 156.146.38.168 |
| 93.33 | trojan | 261.9 | 0.1 | 21.72 | 15.0 | 7.35 | 13.24 | 18.52 | Au1rxx-base64 | 66.163.114.106 |
| 93.32 | shadowsocks | 257.9 | 22.1 | 21.81 | 14.17 | 10.0 | 12.82 | 18.52 | Au1rxx-base64 | 156.146.38.167 |
| 92.28 | trojan | 269.6 | 0.3 | 21.54 | 14.99 | 7.28 | 13.24 | 18.52 | Au1rxx-base64 | 216.152.155.59 |
| 91.92 | shadowsocks | 306.3 | 29.6 | 20.69 | 13.89 | 10.0 | 12.82 | 18.52 | Au1rxx-base64 | 156.146.38.170 |
| 91.12 | trojan | 267.0 | 20.9 | 21.6 | 14.22 | 7.27 | 13.24 | 18.52 | Au1rxx-base64 | 66.163.114.126 |
| 90.07 | trojan | 317.2 | 1.2 | 20.43 | 14.96 | 7.2 | 13.24 | 18.52 | Au1rxx-base64 | 170.101.101.19 |
| 90.0 | shadowsocks | 384.4 | 19.3 | 18.88 | 14.28 | 10.0 | 12.82 | 18.52 | Au1rxx-base64 | 45.86.51.18 |
| 89.91 | shadowsocks | 314.0 | 4.5 | 20.51 | 14.83 | 10.0 | 12.82 | 18.52 | Au1rxx-base64 | 185.230.230.18 |
| 89.34 | trojan | 318.3 | 0.6 | 20.41 | 14.98 | 7.24 | 13.24 | 18.52 | Au1rxx-base64 | 216.152.156.49 |
| 89.13 | trojan | 316.0 | 4.6 | 20.46 | 14.83 | 9.82 | 13.24 | 18.52 | Au1rxx-base64 | 66.163.112.121 |
| 89.11 | shadowsocks | 244.3 | 1.1 | 22.12 | 14.96 | 4.69 | 12.82 | 18.52 | Au1rxx-base64 | 156.146.38.169 |
| 88.74 | trojan | 315.8 | 2.5 | 20.47 | 14.91 | 8.48 | 13.24 | 18.52 | Au1rxx-base64 | 216.152.147.48 |
| 88.7 | trojan | 304.0 | 3.3 | 20.74 | 14.88 | 7.34 | 13.24 | 18.52 | Au1rxx-base64 | 170.101.101.67 |
| 88.5 | trojan | 314.8 | 3.9 | 20.49 | 14.85 | 7.2 | 13.24 | 18.52 | Au1rxx-base64 | 216.152.156.65 |
| 88.3 | shadowsocks | 313.0 | 1.9 | 20.53 | 14.93 | 10.0 | 12.82 | 18.52 | Au1rxx-base64 | 193.151.163.18 |
| 88.2 | shadowsocks | 299.6 | 0.5 | 20.84 | 14.98 | 10.0 | 12.82 | 18.52 | Au1rxx-base64 | 173.244.56.6 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.955 | 0.964 | 28 | 550 | prefer |
| Au1rxx-base64 | 0.93 | 0.862 | 340 | 1751 | prefer |
| Surfboard-tg-mixed | 0.622 | 0.543 | 140 | 7902 | observe |
| mheidari-all | 0.534 | 0.453 | 95 | 34171 | observe |
| xiaoji235-airport-v2ray-all | 0.391 | 1.0 | 2 | 6752 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4960 | observe |
| DeltaKronecker-all | 0.255 | None | 0 | 2724 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 10521 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5822 | observe |
| barry-far-vless | 0.255 | None | 0 | 5942 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4445 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.245 | None | 0 | 1751 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 91 |
| geo | ClientOSError | - | 22 |
| 204 | TimeoutError | - | 15 |
| 204 | ProxyError | - | 13 |
| cn-block | TimeoutError | - | 7 |
| cn-block | ClientOSError | - | 5 |
| geo | ProxyError | - | 5 |
| 204 | ClientOSError | - | 3 |
| speed | ProxyError | - | 3 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 91 | 80 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
