# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-14 13:17:05 |
| 运行耗时 | 298.5s |
| 订阅源总数 | 107 |
| 健康订阅源 | 93 |
| 原始节点 | 97972 |
| 去重后节点 | 27169 |
| TCP 可达 | 3000 |
| 真实可用 | 66 |
| Verified 输出 | 66 |
| Global 输出 | 72 |
| All 输出 | 27169 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.8 |
| geo | 1.5 |
| tcp | 89.6 |
| probe | 92.0 |
| real_test | 70.0 |
| china_check | 29.6 |
| write_verified | 0.0 |
| generate | 10.1 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 57920 |
| vmess | 16072 |
| shadowsocks | 11794 |
| trojan | 10172 |
| hysteria2 | 1303 |
| http | 410 |
| shadowsocksr | 167 |
| socks | 85 |
| anytls | 25 |
| hysteria | 18 |
| tuic | 6 |

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
| 75.45 | shadowsocks | 266.3 | 643.2 | 21.61 | 0.0 | 9.12 | 12.93 | 17.06 | Au1rxx-base64 | 156.146.38.167 |
| 72.97 | vless | 294.9 | 675.1 | 20.95 | 0.0 | 9.24 | 10.29 | 17.06 | Au1rxx-base64 | 147.45.60.160 |
| 71.26 | hysteria2 | 366.0 | 868.4 | 19.3 | 0.0 | 8.86 | 10.71 | 17.06 | Au1rxx-base64 | 129.213.91.185 |
| 71.0 | vless | 332.9 | 580.3 | 20.07 | 0.0 | 8.34 | 10.29 | 17.06 | Au1rxx-base64 | 45.32.69.110 |
| 70.01 | shadowsocks | 378.6 | 817.1 | 19.01 | 0.0 | 10.0 | 12.93 | 17.06 | Au1rxx-base64 | 37.19.198.244 |
| 69.84 | vless | 356.3 | 701.7 | 19.53 | 0.0 | 8.27 | 10.29 | 17.06 | Au1rxx-base64 | 154.29.145.196 |
| 69.71 | shadowsocks | 390.4 | 870.7 | 18.74 | 0.0 | 10.0 | 12.93 | 17.06 | Au1rxx-base64 | 37.19.198.160 |
| 68.66 | shadowsocks | 385.0 | 788.1 | 18.87 | 0.0 | 10.0 | 12.93 | 17.06 | Au1rxx-base64 | 140.82.63.79 |
| 68.19 | hysteria2 | 482.6 | 1076.0 | 16.61 | 0.0 | 8.6 | 10.71 | 17.06 | Au1rxx-base64 | 66.94.121.46 |
| 67.47 | shadowsocks | 303.6 | 748.5 | 20.75 | 0.0 | 9.9 | 12.93 | 17.06 | Au1rxx-base64 | 156.146.38.168 |
| 67.36 | shadowsocks | 261.8 | 633.8 | 21.72 | 0.0 | 0.0 | 12.93 | 17.06 | Au1rxx-base64 | 156.146.38.169 |
| 65.7 | vless | 354.5 | 652.0 | 19.57 | 0.0 | 4.61 | 10.29 | 17.06 | Au1rxx-base64 | 154.12.38.159 |
| 65.53 | shadowsocks | 399.3 | 762.5 | 18.53 | 0.0 | 9.19 | 12.93 | 17.06 | Au1rxx-base64 | 149.22.95.183 |
| 65.03 | shadowsocks | 264.0 | 646.4 | 21.67 | 0.0 | 0.0 | 12.93 | 15.94 | mheidari-all | 156.146.38.170 |
| 65.01 | http | 334.9 | 591.8 | 20.02 | 0.0 | 0.0 | 14.48 | 18.54 | zhangkai | 138.199.35.198 |
| 64.11 | http | 336.5 | 597.3 | 19.99 | 0.0 | 0.0 | 14.48 | 18.54 | zhangkai | 138.199.35.216 |
| 63.5 | shadowsocks | 470.8 | 1048.2 | 16.88 | 0.0 | 6.86 | 12.93 | 17.06 | Au1rxx-base64 | 15.204.246.132 |
| 62.36 | shadowsocks | 299.9 | 610.8 | 20.84 | 0.0 | 0.0 | 12.93 | 17.06 | Au1rxx-base64 | 173.244.56.6 |
| 62.35 | vless | 306.6 | 614.1 | 20.68 | 0.0 | 0.0 | 10.29 | 15.94 | mheidari-all | 216.227.161.95 |
| 61.83 | vless | 564.3 | 683.1 | 14.71 | 0.0 | 6.97 | 10.29 | 17.06 | Au1rxx-base64 | 185.200.199.75 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.927 | 1.0 | 19 | 144 | prefer |
| Au1rxx-base64 | 0.814 | 0.745 | 200 | 1782 | prefer |
| mheidari-all | 0.78 | 0.705 | 78 | 23983 | prefer |
| Surfboard-tg-mixed | 0.736 | 0.661 | 59 | 7056 | prefer |
| ermaozi-get_subscribe | 0.534 | 1.0 | 7 | 515 | observe |
| 10ium-HighSpeed | 0.289 | 1.0 | 1 | 839 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5125 | observe |
| DeltaKronecker-all | 0.255 | None | 0 | 4803 | observe |
| Epodonios-all | 0.255 | None | 0 | 7542 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9829 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5579 | observe |
| barry-far-vless | 0.255 | None | 0 | 5831 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4216 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 49 |
| speed | ClientOSError | - | 13 |
| 204 | ProxyError | - | 8 |
| geo | ClientOSError | - | 6 |
| cn-block | TimeoutError | - | 5 |
| 204 | TimeoutError | - | 5 |
| 204 | ClientOSError | - | 4 |
| cn-block | ClientOSError | - | 3 |
| cn-block | ProxyError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 80 | 66 | - |
| global | False | 84 | 72 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
