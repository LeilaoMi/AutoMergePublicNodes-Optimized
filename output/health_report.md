# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-09 15:25:01 |
| 运行耗时 | 160.6s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 79415 |
| 去重后节点 | 23963 |
| TCP 可达 | 3000 |
| 真实可用 | 242 |
| Verified 输出 | 242 |
| Global 输出 | 248 |
| All 输出 | 23963 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.3 |
| geo | 1.3 |
| tcp | 31.8 |
| probe | 45.0 |
| real_test | 58.4 |
| generate | 19.8 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 45338 |
| trojan | 12790 |
| vmess | 10515 |
| shadowsocks | 9491 |
| hysteria2 | 903 |
| shadowsocksr | 135 |
| http | 135 |
| socks | 91 |
| hysteria | 10 |
| anytls | 5 |
| tuic | 2 |

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
| 75.31 | shadowsocks | 243.2 | 646.8 | 22.15 | 0.0 | 10.0 | 12.3 | 14.86 | Au1rxx-base64 | 37.19.198.236 |
| 74.48 | shadowsocks | 257.2 | 663.1 | 21.82 | 0.0 | 10.0 | 12.3 | 14.86 | Au1rxx-base64 | 108.181.57.93 |
| 74.1 | shadowsocks | 295.3 | 808.9 | 20.94 | 0.0 | 10.0 | 12.3 | 14.86 | Au1rxx-base64 | 37.19.198.160 |
| 72.43 | shadowsocks | 231.9 | 609.4 | 22.41 | 0.0 | 10.0 | 12.3 | 11.72 | mheidari-all | 198.98.53.130 |
| 71.39 | shadowsocks | 281.1 | 642.2 | 21.27 | 0.0 | 10.0 | 12.3 | 14.86 | Au1rxx-base64 | 156.146.38.170 |
| 71.23 | vless | 321.8 | 849.0 | 20.33 | 0.0 | 10.0 | 6.04 | 14.86 | Au1rxx-base64 | 159.89.87.21 |
| 70.93 | shadowsocks | 243.5 | 653.2 | 22.14 | 0.0 | 10.0 | 12.3 | 14.86 | Au1rxx-base64 | 37.19.198.244 |
| 70.79 | shadowsocks | 284.7 | 648.9 | 21.19 | 0.0 | 10.0 | 12.3 | 14.86 | Au1rxx-base64 | 156.146.38.168 |
| 70.76 | shadowsocks | 280.9 | 635.2 | 21.28 | 0.0 | 10.0 | 12.3 | 14.86 | Au1rxx-base64 | 156.146.38.169 |
| 70.13 | shadowsocks | 250.8 | 669.3 | 21.97 | 0.0 | 10.0 | 12.3 | 14.86 | Au1rxx-base64 | 37.19.198.243 |
| 69.96 | vmess | 392.2 | 1067.7 | 18.7 | 0.0 | 10.0 | 12.86 | 12.9 | DeltaKronecker-all | 67.220.85.46 |
| 68.73 | hysteria2 | 355.1 | 686.9 | 19.56 | 0.0 | 10.0 | 12.5 | 14.86 | Au1rxx-base64 | 62.210.124.146 |
| 68.23 | trojan | 319.9 | 755.9 | 20.37 | 0.0 | 10.0 | 7.58 | 14.86 | Au1rxx-base64 | 149.28.241.235 |
| 67.95 | shadowsocks | 323.4 | 582.7 | 20.29 | 0.0 | 10.0 | 12.3 | 14.86 | Au1rxx-base64 | 173.244.56.6 |
| 67.87 | shadowsocks | 304.7 | 571.1 | 20.73 | 0.0 | 10.0 | 12.3 | 14.86 | Au1rxx-base64 | 108.181.118.10 |
| 66.89 | shadowsocks | 325.6 | 595.6 | 20.24 | 0.0 | 10.0 | 12.3 | 14.86 | Au1rxx-base64 | 173.244.56.9 |
| 66.78 | shadowsocks | 320.0 | 745.7 | 20.37 | 0.0 | 10.0 | 12.3 | 14.86 | Au1rxx-base64 | 156.146.38.167 |
| 66.78 | shadowsocks | 356.6 | 659.6 | 19.52 | 0.0 | 10.0 | 12.3 | 14.86 | Au1rxx-base64 | 108.181.0.177 |
| 66.4 | shadowsocks | 373.3 | 927.2 | 19.14 | 0.0 | 10.0 | 12.3 | 11.72 | mheidari-all | 185.196.61.82 |
| 66.2 | shadowsocks | 361.2 | 679.0 | 19.42 | 0.0 | 10.0 | 12.3 | 14.86 | Au1rxx-base64 | 149.22.95.183 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| Surfboard-tg-mixed | 0.891 | 0.824 | 51 | 5805 | prefer |
| mheidari-all | 0.791 | 0.722 | 36 | 16991 | prefer |
| Au1rxx-base64 | 0.765 | 0.767 | 73 | 119 | prefer |
| DeltaKronecker-all | 0.492 | 0.411 | 192 | 7533 | observe |
| xiaoji235-airport-v2ray-all | 0.391 | 1.0 | 2 | 2703 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4306 | observe |
| Epodonios-all | 0.255 | None | 0 | 6648 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3977 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6653 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4318 | observe |
| barry-far-vless | 0.255 | None | 0 | 4797 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5440 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| nscl5-all | 0.228 | None | 0 | 1319 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 83 |
| geo | TimeoutError | - | 28 |
| 204 | ClientOSError | - | 9 |
| cn-block | ClientOSError | - | 7 |
| geo | ClientOSError | - | 7 |
| 204 | TimeoutError | - | 5 |
| speed | TimeoutError | - | 4 |
| cn-block | ProxyError | - | 3 |
| cn-block | TimeoutError | - | 2 |
| 204 | ProxyError | - | 1 |
| geo | ProxyError | - | 1 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 242 | - |
| global | False | 300 | 248 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
