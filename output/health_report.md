# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-21 21:54:29 |
| 运行耗时 | 288.9s |
| 订阅源总数 | 107 |
| 健康订阅源 | 91 |
| 原始节点 | 96046 |
| 去重后节点 | 27003 |
| TCP 可达 | 3000 |
| 真实可用 | 332 |
| Verified 输出 | 74 |
| Global 输出 | 300 |
| All 输出 | 27003 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.2 |
| geo | 1.5 |
| tcp | 85.6 |
| probe | 98.4 |
| real_test | 62.6 |
| china_check | 19.3 |
| write_verified | 0.0 |
| generate | 14.3 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 57043 |
| vmess | 16956 |
| shadowsocks | 11972 |
| trojan | 8422 |
| hysteria2 | 1269 |
| shadowsocksr | 164 |
| http | 121 |
| socks | 55 |
| anytls | 21 |
| hysteria | 17 |
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
| 95.24 | hysteria2 | 229.2 | 0.7 | 22.47 | 14.98 | 8.76 | 13.93 | 16.6 | Au1rxx-base64 | 129.213.91.185 |
| 91.56 | shadowsocks | 293.5 | 1.0 | 20.98 | 14.96 | 10.0 | 13.02 | 16.6 | Au1rxx-base64 | 37.19.198.243 |
| 91.11 | vless | 340.4 | 3.7 | 19.9 | 14.86 | 9.98 | 9.77 | 16.6 | Au1rxx-base64 | 169.40.42.74 |
| 90.66 | vless | 310.1 | 3.6 | 20.6 | 14.87 | 8.82 | 9.77 | 16.6 | Au1rxx-base64 | 169.40.42.104 |
| 90.17 | vless | 358.8 | 0.7 | 19.47 | 14.97 | 9.97 | 9.77 | 16.6 | Au1rxx-base64 | 169.40.42.168 |
| 90.0 | shadowsocks | 361.6 | 0.8 | 19.41 | 14.97 | 10.0 | 13.02 | 16.6 | Au1rxx-base64 | 37.19.198.160 |
| 89.92 | vless | 278.8 | 7.7 | 21.32 | 14.71 | 7.52 | 9.77 | 16.6 | Au1rxx-base64 | 195.123.235.183 |
| 89.59 | vless | 278.8 | 6.3 | 21.32 | 14.76 | 8.7 | 9.77 | 16.6 | Au1rxx-base64 | 169.40.42.163 |
| 89.37 | shadowsocks | 242.0 | 1.6 | 22.18 | 14.94 | 6.63 | 13.02 | 16.6 | Au1rxx-base64 | 37.19.198.244 |
| 89.19 | vless | 346.4 | 6.7 | 19.76 | 14.75 | 8.31 | 9.77 | 16.6 | Au1rxx-base64 | 169.40.42.224 |
| 89.17 | trojan | 428.1 | 3.8 | 17.87 | 14.86 | 9.6 | 13.24 | 16.6 | Au1rxx-base64 | 69.164.240.85 |
| 89.05 | shadowsocks | 280.5 | 0.5 | 21.28 | 14.98 | 10.0 | 13.02 | 16.6 | Au1rxx-base64 | 156.146.38.169 |
| 88.78 | shadowsocks | 393.9 | 0.1 | 18.66 | 15.0 | 10.0 | 13.02 | 16.6 | Au1rxx-base64 | 193.151.163.18 |
| 88.73 | shadowsocks | 370.8 | 2.8 | 19.19 | 14.89 | 10.0 | 13.02 | 16.6 | Au1rxx-base64 | 193.151.160.9 |
| 88.51 | vless | 332.4 | 8.3 | 20.08 | 14.69 | 9.97 | 9.77 | 16.6 | Au1rxx-base64 | 169.40.42.231 |
| 88.24 | hysteria2 | 351.7 | 1.8 | 19.64 | 14.93 | 10.0 | 13.93 | 16.6 | Au1rxx-base64 | 66.94.121.46 |
| 88.12 | vless | 324.8 | 1.1 | 20.26 | 14.96 | 8.3 | 9.77 | 16.6 | Au1rxx-base64 | 169.40.42.235 |
| 88.04 | shadowsocks | 286.6 | 5.1 | 21.14 | 14.81 | 10.0 | 13.02 | 16.6 | Au1rxx-base64 | 156.146.38.170 |
| 87.93 | trojan | 379.5 | 3.2 | 18.99 | 14.88 | 10.0 | 13.24 | 16.6 | Au1rxx-base64 | 66.23.203.21 |
| 87.66 | vless | 320.4 | 5.1 | 20.36 | 14.81 | 9.99 | 9.77 | 16.6 | Au1rxx-base64 | 169.40.42.35 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.932 | 0.963 | 27 | 31 | prefer |
| mheidari-all | 0.899 | 0.825 | 103 | 23903 | prefer |
| Au1rxx-base64 | 0.873 | 0.812 | 255 | 1596 | prefer |
| DeltaKronecker-all | 0.454 | 0.389 | 18 | 4067 | observe |
| ninja-vless | 0.412 | 0.667 | 6 | 1791 | observe |
| Surfboard-tg-mixed | 0.32 | 0.5 | 4 | 7033 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4925 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 10005 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5488 | observe |
| barry-far-vless | 0.255 | None | 0 | 5734 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4164 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |
| Au1rxx-clash | 0.239 | None | 0 | 1596 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 40 |
| speed | ClientOSError | - | 18 |
| 204 | ProxyError | - | 7 |
| 204 | TimeoutError | - | 6 |
| cn-block | ClientOSError | - | 5 |
| speed | ProxyError | - | 4 |
| geo | ClientOSError | - | 4 |
| cn-block | TimeoutError | - | 3 |
| cn-block | ProxyError | - | 1 |
| speed | TimeoutError | - | 1 |
| 204 | ClientOSError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 75 | 74 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
