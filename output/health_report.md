# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-11-03 07:03:30 |
| 运行耗时 | 290.0s |
| 订阅源总数 | 107 |
| 健康订阅源 | 88 |
| 原始节点 | 81802 |
| 去重后节点 | 26687 |
| TCP 可达 | 3000 |
| 真实可用 | 392 |
| Verified 输出 | 34 |
| Global 输出 | 300 |
| All 输出 | 26687 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.2 |
| geo | 1.5 |
| tcp | 78.1 |
| probe | 98.1 |
| real_test | 67.8 |
| china_check | 22.2 |
| write_verified | 0.0 |
| generate | 15.1 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 48949 |
| vmess | 14031 |
| shadowsocks | 8636 |
| trojan | 8216 |
| hysteria2 | 1565 |
| shadowsocksr | 157 |
| http | 100 |
| socks | 71 |
| anytls | 35 |
| hysteria | 28 |
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
| 98.22 | hysteria2 | 224.1 | 5.1 | 22.59 | 14.81 | 10.0 | 14.12 | 18.2 | Au1rxx-base64 | 129.213.91.185 |
| 95.29 | shadowsocks | 234.3 | 1.5 | 22.35 | 14.94 | 10.0 | 13.8 | 18.2 | Au1rxx-base64 | 37.19.198.244 |
| 94.87 | trojan | 275.4 | 5.1 | 21.4 | 14.81 | 8.47 | 14.49 | 18.2 | Au1rxx-base64 | 170.101.101.67 |
| 94.59 | shadowsocks | 245.5 | 0.3 | 22.1 | 14.99 | 10.0 | 13.8 | 18.2 | Au1rxx-base64 | 185.230.230.18 |
| 93.85 | trojan | 291.7 | 6.6 | 21.03 | 14.75 | 9.88 | 14.49 | 18.2 | Au1rxx-base64 | 216.152.147.48 |
| 93.61 | shadowsocks | 305.8 | 2.5 | 20.7 | 14.91 | 10.0 | 13.8 | 18.2 | Au1rxx-base64 | 37.19.198.243 |
| 93.08 | shadowsocks | 299.3 | 7.3 | 20.85 | 14.73 | 10.0 | 13.8 | 18.2 | Au1rxx-base64 | 45.86.51.18 |
| 93.07 | shadowsocks | 293.4 | 7.1 | 20.99 | 14.74 | 9.84 | 13.8 | 18.2 | Au1rxx-base64 | 193.151.160.18 |
| 93.0 | shadowsocks | 302.2 | 7.4 | 20.78 | 14.72 | 10.0 | 13.8 | 18.2 | Au1rxx-base64 | 193.151.160.9 |
| 92.76 | trojan | 274.9 | 8.9 | 21.41 | 14.66 | 8.5 | 14.49 | 18.2 | Au1rxx-base64 | 216.152.155.59 |
| 92.49 | trojan | 285.5 | 4.7 | 21.17 | 14.82 | 6.31 | 14.49 | 18.2 | Au1rxx-base64 | 170.101.101.112 |
| 92.34 | trojan | 298.0 | 6.7 | 20.88 | 14.75 | 8.48 | 14.49 | 18.2 | Au1rxx-base64 | 216.152.147.93 |
| 92.19 | trojan | 281.6 | 14.3 | 21.26 | 14.46 | 6.28 | 14.49 | 18.2 | Au1rxx-base64 | 170.101.101.211 |
| 92.18 | shadowsocks | 232.5 | 3.5 | 22.4 | 14.87 | 10.0 | 13.8 | 18.2 | Au1rxx-base64 | 37.19.198.160 |
| 92.07 | trojan | 266.7 | 1.5 | 21.6 | 14.94 | 5.34 | 14.49 | 18.2 | Au1rxx-base64 | 170.101.101.131 |
| 91.81 | trojan | 449.3 | 6.9 | 17.38 | 14.74 | 10.0 | 14.49 | 18.2 | Au1rxx-base64 | 69.164.240.85 |
| 91.7 | trojan | 306.3 | 0.9 | 20.69 | 14.97 | 8.37 | 14.49 | 18.2 | Au1rxx-base64 | 216.152.156.49 |
| 91.64 | trojan | 313.3 | 2.1 | 20.53 | 14.92 | 8.36 | 14.49 | 18.2 | Au1rxx-base64 | 216.152.156.65 |
| 91.56 | trojan | 310.3 | 6.2 | 20.59 | 14.77 | 6.62 | 14.49 | 18.2 | Au1rxx-base64 | 169.197.140.245 |
| 91.42 | vless | 262.7 | 4.6 | 21.7 | 14.83 | 10.0 | 6.69 | 18.2 | Au1rxx-base64 | 167.17.69.171 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.923 | 1.0 | 19 | 43 | prefer |
| Au1rxx-base64 | 0.909 | 0.841 | 283 | 1751 | prefer |
| mheidari-all | 0.887 | 0.818 | 55 | 14871 | prefer |
| Surfboard-tg-mixed | 0.694 | 0.616 | 138 | 8355 | observe |
| ninja-vless | 0.383 | 1.0 | 2 | 1791 | observe |
| xiaoji235-airport-v2ray-all | 0.349 | 0.667 | 3 | 6752 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4941 | observe |
| DeltaKronecker-all | 0.255 | None | 0 | 2726 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 10703 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5917 | observe |
| barry-far-vless | 0.255 | None | 0 | 6133 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4734 | observe |
| Au1rxx-clash | 0.245 | None | 0 | 1751 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 79 |
| geo | ClientOSError | - | 28 |
| 204 | ProxyError | - | 17 |
| 204 | TimeoutError | - | 5 |
| 204 | ClientOSError | - | 3 |
| cn-block | ProxyError | - | 3 |
| cn-block | TimeoutError | - | 2 |
| speed | ProxyError | - | 2 |
| cn-block | ClientOSError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 55 | 34 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
