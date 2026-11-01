# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-11-01 06:29:05 |
| 运行耗时 | 305.1s |
| 订阅源总数 | 107 |
| 健康订阅源 | 88 |
| 原始节点 | 80495 |
| 去重后节点 | 26309 |
| TCP 可达 | 3000 |
| 真实可用 | 617 |
| Verified 输出 | 98 |
| Global 输出 | 300 |
| All 输出 | 26309 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.1 |
| geo | 1.4 |
| tcp | 76.8 |
| probe | 79.4 |
| real_test | 105.9 |
| china_check | 25.3 |
| write_verified | 0.1 |
| generate | 11.2 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 47598 |
| vmess | 13770 |
| trojan | 8791 |
| shadowsocks | 8436 |
| hysteria2 | 1499 |
| http | 158 |
| shadowsocksr | 154 |
| socks | 50 |
| anytls | 16 |
| tuic | 12 |
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
| 94.77 | shadowsocks | 240.2 | 2.6 | 22.22 | 14.9 | 10.0 | 13.53 | 18.62 | Au1rxx-base64 | 185.230.230.18 |
| 94.69 | shadowsocks | 238.5 | 6.0 | 22.26 | 14.78 | 10.0 | 13.53 | 18.62 | Au1rxx-base64 | 45.86.51.18 |
| 94.49 | vless | 256.1 | 5.9 | 21.85 | 14.78 | 9.78 | 9.46 | 18.62 | Au1rxx-base64 | 159.89.87.21 |
| 94.39 | hysteria2 | 249.1 | 79.5 | 22.01 | 12.02 | 10.0 | 13.24 | 18.62 | Au1rxx-base64 | 129.213.91.185 |
| 94.32 | shadowsocks | 258.5 | 16.4 | 21.79 | 14.38 | 10.0 | 13.53 | 18.62 | Au1rxx-base64 | 37.19.198.243 |
| 93.98 | trojan | 284.2 | 0.6 | 21.2 | 14.98 | 7.55 | 14.13 | 18.62 | Au1rxx-base64 | 170.101.101.67 |
| 93.97 | vless | 278.8 | 3.1 | 21.32 | 14.88 | 9.69 | 9.46 | 18.62 | Au1rxx-base64 | 66.70.179.198 |
| 93.43 | vless | 306.8 | 2.9 | 20.68 | 14.89 | 9.78 | 9.46 | 18.62 | Au1rxx-base64 | 167.17.69.171 |
| 93.17 | vless | 320.3 | 1.4 | 20.36 | 14.95 | 9.78 | 9.46 | 18.62 | Au1rxx-base64 | 169.40.42.168 |
| 92.89 | trojan | 257.3 | 1.7 | 21.82 | 14.94 | 5.88 | 14.13 | 18.62 | Au1rxx-base64 | 216.152.155.23 |
| 92.85 | vless | 344.6 | 0.7 | 19.8 | 14.97 | 10.0 | 9.46 | 18.62 | Au1rxx-base64 | 169.40.42.74 |
| 92.84 | shadowsocks | 293.8 | 0.5 | 20.98 | 14.98 | 9.23 | 13.53 | 18.62 | Au1rxx-base64 | 193.151.160.18 |
| 92.51 | vless | 349.5 | 1.0 | 19.69 | 14.96 | 9.78 | 9.46 | 18.62 | Au1rxx-base64 | 169.40.42.90 |
| 92.47 | trojan | 430.4 | 2.5 | 17.81 | 14.91 | 10.0 | 14.13 | 18.62 | Au1rxx-base64 | 69.164.240.85 |
| 92.35 | vless | 355.9 | 1.7 | 19.54 | 14.94 | 9.79 | 9.46 | 18.62 | Au1rxx-base64 | 169.40.42.104 |
| 92.24 | shadowsocks | 277.8 | 3.8 | 21.35 | 14.86 | 10.0 | 13.53 | 18.62 | Au1rxx-base64 | 156.146.38.170 |
| 92.02 | trojan | 304.7 | 2.2 | 20.72 | 14.92 | 10.0 | 14.13 | 18.62 | Au1rxx-base64 | 66.163.114.45 |
| 91.97 | shadowsocks | 279.3 | 4.4 | 21.31 | 14.84 | 10.0 | 13.53 | 18.62 | Au1rxx-base64 | 156.146.38.167 |
| 91.86 | shadowsocks | 257.8 | 2.8 | 21.81 | 14.9 | 10.0 | 13.53 | 18.62 | Au1rxx-base64 | 37.19.198.160 |
| 91.86 | vless | 378.8 | 0.7 | 19.01 | 14.98 | 9.79 | 9.46 | 18.62 | Au1rxx-base64 | 169.40.42.89 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi-get_subscribe | 0.993 | 0.985 | 66 | 558 | prefer |
| Au1rxx-base64 | 0.939 | 0.871 | 319 | 1751 | prefer |
| zhangkai | 0.923 | 1.0 | 19 | 43 | prefer |
| Surfboard-tg-mixed | 0.757 | 0.812 | 16 | 7809 | prefer |
| mheidari-all | 0.648 | 0.568 | 424 | 14747 | observe |
| tg-LonUp_M | 0.262 | 1.0 | 1 | 178 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4970 | observe |
| DeltaKronecker-all | 0.255 | None | 0 | 2848 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 10495 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5637 | observe |
| barry-far-vless | 0.255 | None | 0 | 5805 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4680 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.245 | None | 0 | 1751 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 128 |
| geo | ClientOSError | - | 63 |
| speed | ClientOSError | - | 14 |
| 204 | TimeoutError | - | 10 |
| 204 | ProxyError | - | 8 |
| 204 | ClientOSError | - | 5 |
| cn-block | ClientOSError | - | 4 |
| cn-block | TimeoutError | - | 2 |
| geo | ProxyError | - | 1 |
| cn-block | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 99 | 98 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
