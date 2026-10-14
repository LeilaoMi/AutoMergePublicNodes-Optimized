# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-14 13:04:56 |
| 运行耗时 | 312.7s |
| 订阅源总数 | 107 |
| 健康订阅源 | 93 |
| 原始节点 | 97972 |
| 去重后节点 | 27170 |
| TCP 可达 | 3000 |
| 真实可用 | 80 |
| Verified 输出 | 80 |
| Global 输出 | 84 |
| All 输出 | 27170 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 8.1 |
| geo | 1.6 |
| tcp | 85.1 |
| probe | 105.4 |
| real_test | 70.1 |
| china_check | 28.6 |
| write_verified | 0.0 |
| generate | 13.7 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 57921 |
| vmess | 16074 |
| shadowsocks | 11792 |
| trojan | 10170 |
| hysteria2 | 1304 |
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
| 81.66 | hysteria2 | 240.8 | 587.8 | 22.2 | 0.0 | 10.0 | 13.64 | 16.82 | Au1rxx-base64 | 66.94.121.46 |
| 78.53 | shadowsocks | 239.9 | 617.1 | 22.22 | 0.0 | 10.0 | 13.49 | 16.82 | Au1rxx-base64 | 156.146.38.167 |
| 77.22 | vless | 245.5 | 545.5 | 22.09 | 0.0 | 10.0 | 9.29 | 16.82 | Au1rxx-base64 | 45.32.69.110 |
| 76.86 | hysteria2 | 303.1 | 731.3 | 20.76 | 0.0 | 10.0 | 13.64 | 16.82 | Au1rxx-base64 | 129.213.91.185 |
| 73.31 | shadowsocks | 242.7 | 618.8 | 22.16 | 0.0 | 4.84 | 13.49 | 16.82 | Au1rxx-base64 | 156.146.38.169 |
| 73.23 | vless | 293.9 | 596.0 | 20.97 | 0.0 | 10.0 | 9.29 | 16.82 | Au1rxx-base64 | 154.29.145.196 |
| 72.37 | shadowsocks | 334.1 | 767.0 | 20.04 | 0.0 | 10.0 | 13.49 | 16.82 | Au1rxx-base64 | 37.19.198.160 |
| 71.08 | shadowsocks | 275.5 | 589.7 | 21.4 | 0.0 | 6.82 | 13.49 | 16.82 | Au1rxx-base64 | 173.244.56.6 |
| 70.79 | shadowsocks | 400.3 | 955.2 | 18.51 | 0.0 | 10.0 | 13.49 | 16.82 | Au1rxx-base64 | 37.19.198.244 |
| 70.77 | shadowsocks | 368.1 | 815.3 | 19.26 | 0.0 | 9.27 | 13.49 | 16.82 | Au1rxx-base64 | 15.204.233.41 |
| 70.41 | shadowsocks | 340.3 | 770.0 | 19.9 | 0.0 | 7.93 | 13.49 | 16.82 | Au1rxx-base64 | 37.19.198.236 |
| 70.1 | shadowsocks | 377.4 | 686.7 | 19.04 | 0.0 | 10.0 | 13.49 | 16.82 | Au1rxx-base64 | 140.82.63.79 |
| 69.43 | shadowsocks | 318.6 | 652.7 | 20.4 | 0.0 | 10.0 | 13.49 | 16.82 | Au1rxx-base64 | 149.22.95.183 |
| 69.02 | shadowsocks | 240.7 | 619.0 | 22.21 | 0.0 | 0.0 | 13.49 | 17.32 | mheidari-all | 156.146.38.170 |
| 68.37 | shadowsocks | 437.2 | 993.7 | 17.66 | 0.0 | 9.21 | 13.49 | 16.82 | Au1rxx-base64 | 64.74.163.69 |
| 68.07 | vless | 440.4 | 648.3 | 17.58 | 0.0 | 9.7 | 9.29 | 16.82 | Au1rxx-base64 | 154.12.38.159 |
| 67.53 | http | 261.0 | 563.4 | 21.74 | 0.0 | 0.0 | 14.33 | 18.54 | zhangkai | 138.199.35.198 |
| 67.53 | vless | 396.8 | 854.0 | 18.59 | 0.0 | 7.43 | 9.29 | 16.82 | Au1rxx-base64 | 193.233.202.250 |
| 67.49 | shadowsocks | 396.7 | 951.5 | 18.59 | 0.0 | 6.74 | 13.49 | 16.82 | Au1rxx-base64 | 37.19.198.243 |
| 66.15 | vless | 324.5 | 708.0 | 20.27 | 0.0 | 7.48 | 9.29 | 16.82 | Au1rxx-base64 | 69.48.201.136 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.927 | 1.0 | 19 | 144 | prefer |
| Au1rxx-base64 | 0.853 | 0.785 | 209 | 1782 | prefer |
| mheidari-all | 0.797 | 0.722 | 90 | 23983 | prefer |
| Surfboard-tg-mixed | 0.794 | 0.727 | 33 | 7056 | prefer |
| ermaozi-get_subscribe | 0.546 | 0.889 | 9 | 515 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5125 | observe |
| DeltaKronecker-all | 0.255 | None | 0 | 4803 | observe |
| Epodonios-all | 0.255 | None | 0 | 7542 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9836 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5579 | observe |
| barry-far-vless | 0.255 | None | 0 | 5831 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4216 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 52 |
| speed | ClientOSError | - | 11 |
| geo | ClientOSError | - | 4 |
| cn-block | TimeoutError | - | 3 |
| 204 | TimeoutError | - | 2 |
| 204 | ClientOSError | - | 2 |
| cn-block | ClientOSError | - | 2 |
| geo | TimeoutError | - | 1 |
| speed | TimeoutError | - | 1 |
| geo | ProxyError | - | 1 |
| speed | ProxyError | - | 1 |
| 204 | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 88 | 80 | - |
| global | False | 98 | 84 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
