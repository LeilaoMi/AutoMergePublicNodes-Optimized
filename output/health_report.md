# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-14 12:10:32 |
| 运行耗时 | 362.1s |
| 订阅源总数 | 107 |
| 健康订阅源 | 93 |
| 原始节点 | 98048 |
| 去重后节点 | 27228 |
| TCP 可达 | 3000 |
| 真实可用 | 88 |
| Verified 输出 | 88 |
| Global 输出 | 97 |
| All 输出 | 27228 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 8.0 |
| geo | 1.5 |
| tcp | 114.5 |
| probe | 108.3 |
| real_test | 75.6 |
| generate | 54.3 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 57916 |
| vmess | 16104 |
| shadowsocks | 11784 |
| trojan | 10156 |
| hysteria2 | 1303 |
| http | 483 |
| shadowsocksr | 167 |
| socks | 86 |
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
| 77.21 | shadowsocks | 251.5 | 696.6 | 21.96 | 0.0 | 10.0 | 12.81 | 16.44 | Au1rxx-base64 | 37.19.198.244 |
| 77.01 | shadowsocks | 259.8 | 716.8 | 21.76 | 0.0 | 10.0 | 12.81 | 16.44 | Au1rxx-base64 | 37.19.198.160 |
| 76.58 | shadowsocks | 257.0 | 661.0 | 21.83 | 0.0 | 10.0 | 12.81 | 16.44 | Au1rxx-base64 | 140.82.63.79 |
| 75.53 | vless | 279.4 | 703.4 | 21.31 | 0.0 | 8.76 | 9.02 | 16.44 | Au1rxx-base64 | 66.70.179.198 |
| 75.44 | hysteria2 | 238.8 | 680.7 | 22.25 | 0.0 | 10.0 | 11.25 | 16.44 | Au1rxx-base64 | 129.213.91.185 |
| 74.61 | shadowsocks | 279.9 | 789.2 | 21.3 | 0.0 | 8.06 | 12.81 | 16.44 | Au1rxx-base64 | 37.19.198.243 |
| 73.46 | shadowsocks | 331.2 | 953.5 | 20.11 | 0.0 | 9.6 | 12.81 | 16.44 | Au1rxx-base64 | 15.204.233.41 |
| 73.45 | shadowsocks | 315.6 | 852.0 | 20.47 | 0.0 | 8.73 | 12.81 | 16.44 | Au1rxx-base64 | 37.19.198.236 |
| 73.16 | vless | 257.8 | 711.0 | 21.81 | 0.0 | 8.89 | 9.02 | 16.44 | Au1rxx-base64 | 216.9.226.22 |
| 73.15 | hysteria2 | 318.4 | 637.2 | 20.41 | 0.0 | 10.0 | 11.25 | 16.44 | Au1rxx-base64 | 66.94.121.46 |
| 71.28 | vless | 320.9 | 659.8 | 20.35 | 0.0 | 7.17 | 9.02 | 16.44 | Au1rxx-base64 | 136.107.170.196 |
| 70.81 | shadowsocks | 311.0 | 739.2 | 20.58 | 0.0 | 10.0 | 12.81 | 16.44 | Au1rxx-base64 | 156.146.38.168 |
| 70.67 | vless | 412.5 | 934.6 | 18.23 | 0.0 | 9.98 | 9.02 | 16.44 | Au1rxx-base64 | 209.200.246.148 |
| 69.8 | http | 258.0 | 685.4 | 21.81 | 0.0 | 0.0 | 13.99 | 18.5 | ermaozi-get_subscribe | 147.182.216.4 |
| 69.77 | shadowsocks | 323.0 | 928.4 | 20.3 | 0.0 | 4.72 | 12.81 | 16.44 | Au1rxx-base64 | 15.204.247.206 |
| 69.64 | shadowsocks | 279.6 | 652.6 | 21.31 | 0.0 | 6.1 | 12.81 | 16.44 | Au1rxx-base64 | 156.146.38.169 |
| 69.6 | shadowsocks | 327.3 | 632.3 | 20.2 | 0.0 | 10.0 | 12.81 | 16.44 | Au1rxx-base64 | 173.244.56.6 |
| 68.71 | vless | 375.1 | 709.7 | 19.1 | 0.0 | 9.97 | 9.02 | 16.44 | Au1rxx-base64 | 45.32.69.110 |
| 68.61 | vless | 368.8 | 790.9 | 19.24 | 0.0 | 8.19 | 9.02 | 16.44 | Au1rxx-base64 | 51.79.31.36 |
| 68.43 | shadowsocks | 569.7 | 1184.2 | 14.59 | 0.0 | 10.0 | 12.81 | 16.44 | Au1rxx-base64 | 15.204.246.132 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.927 | 1.0 | 19 | 144 | prefer |
| ermaozi-get_subscribe | 0.925 | 0.913 | 69 | 598 | prefer |
| mheidari-all | 0.877 | 0.806 | 72 | 23983 | prefer |
| Au1rxx-base64 | 0.855 | 0.787 | 211 | 1778 | prefer |
| Surfboard-tg-mixed | 0.616 | 0.537 | 82 | 7056 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5125 | observe |
| DeltaKronecker-all | 0.255 | None | 0 | 4803 | observe |
| Epodonios-all | 0.255 | None | 0 | 7542 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9834 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5579 | observe |
| barry-far-vless | 0.255 | None | 0 | 5831 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4216 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 60 |
| speed | ClientOSError | - | 9 |
| geo | ClientOSError | - | 8 |
| cn-block | TimeoutError | - | 6 |
| cn-block | ProxyError | - | 5 |
| cn-block | ClientOSError | - | 5 |
| 204 | TimeoutError | - | 3 |
| 204 | ClientOSError | - | 3 |
| 204 | ProxyError | - | 2 |
| speed | ProxyError | - | 2 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 84 | 88 | - |
| global | False | 91 | 97 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
