# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.9.1 |
| 更新时间 | 2026-06-20 09:34:31 |
| 运行耗时 | 414.6s |
| 订阅源总数 | 107 |
| 健康订阅源 | 105 |
| 原始节点 | 73485 |
| 去重后节点 | 21780 |
| TCP 可达 | 800 |
| 真实可用 | 608 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 21780 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.2 |
| geo | 1.4 |
| tcp | 66.2 |
| probe | 109.7 |
| real_test | 198.4 |
| generate | 34.8 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 42376 |
| trojan | 10359 |
| shadowsocks | 10318 |
| vmess | 9833 |
| hysteria2 | 238 |
| shadowsocksr | 161 |
| socks | 96 |
| http | 96 |
| hysteria | 6 |
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
| 79.98 | shadowsocks | 200.0 | 532.7 | 23.15 | 0.0 | 10.0 | 14.17 | 19.16 | Au1rxx-base64 | 149.22.95.183 |
| 78.47 | vless | 301.1 | 834.1 | 20.81 | 0.0 | 10.0 | 10.5 | 19.16 | Au1rxx-base64 | 15.204.97.214 |
| 76.87 | vless | 283.8 | 780.1 | 21.21 | 0.0 | 10.0 | 10.5 | 19.16 | Au1rxx-base64 | 15.204.97.219 |
| 74.4 | shadowsocks | 302.4 | 670.7 | 20.78 | 0.0 | 10.0 | 14.17 | 19.16 | Au1rxx-base64 | 173.244.56.6 |
| 73.72 | shadowsocks | 278.0 | 330.2 | 21.34 | 2.62 | 10.0 | 14.17 | 19.16 | Au1rxx-base64 | 149.22.87.241 |
| 73.36 | shadowsocks | 283.5 | 340.4 | 21.22 | 2.23 | 10.0 | 14.17 | 19.16 | Au1rxx-base64 | 149.22.87.204 |
| 73.14 | shadowsocks | 317.2 | 686.9 | 20.44 | 0.0 | 10.0 | 14.17 | 19.16 | Au1rxx-base64 | 156.146.38.169 |
| 73.08 | shadowsocks | 324.3 | 693.0 | 20.27 | 0.0 | 10.0 | 14.17 | 19.16 | Au1rxx-base64 | 156.146.38.170 |
| 73.01 | shadowsocks | 325.7 | 319.0 | 20.24 | 3.04 | 10.0 | 14.17 | 19.16 | Au1rxx-base64 | 103.106.228.175 |
| 72.91 | shadowsocks | 319.2 | 670.0 | 20.39 | 0.0 | 10.0 | 14.17 | 19.16 | Au1rxx-base64 | 156.146.38.167 |
| 72.88 | shadowsocks | 284.9 | 350.2 | 21.18 | 1.87 | 10.0 | 14.17 | 19.16 | Au1rxx-base64 | 149.22.87.240 |
| 72.33 | shadowsocks | 325.7 | 695.8 | 20.24 | 0.0 | 10.0 | 14.17 | 19.16 | Au1rxx-base64 | 156.146.38.168 |
| 72.22 | vless | 208.1 | 496.3 | 22.96 | 0.0 | 10.0 | 10.5 | 18.26 | Surfboard-tg-mixed | 64.118.155.66 |
| 72.2 | shadowsocks | 271.3 | 541.8 | 21.5 | 0.0 | 10.0 | 14.17 | 19.16 | Au1rxx-base64 | 173.244.56.9 |
| 71.7 | vless | 312.0 | 361.9 | 20.56 | 1.43 | 10.0 | 10.5 | 18.26 | Surfboard-tg-mixed | 31.76.91.24 |
| 71.41 | vless | 311.2 | 366.7 | 20.57 | 1.25 | 10.0 | 10.5 | 18.26 | Surfboard-tg-mixed | 31.76.91.18 |
| 70.47 | vless | 311.6 | 363.6 | 20.56 | 1.36 | 10.0 | 10.5 | 17.08 | mheidari-all | 31.76.91.26 |
| 70.46 | shadowsocks | 368.1 | 749.9 | 19.26 | 0.0 | 10.0 | 14.17 | 19.16 | Au1rxx-base64 | 37.19.198.244 |
| 70.44 | shadowsocks | 368.2 | 749.9 | 19.25 | 0.0 | 10.0 | 14.17 | 19.16 | Au1rxx-base64 | 37.19.198.243 |
| 70.36 | shadowsocks | 370.2 | 752.6 | 19.21 | 0.0 | 10.0 | 14.17 | 19.16 | Au1rxx-base64 | 37.19.198.160 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.966 | 1.0 | 25 | 73 | prefer |
| mheidari-all | 0.885 | 0.807 | 264 | 14813 | prefer |
| Surfboard-tg-mixed | 0.863 | 0.785 | 395 | 5054 | prefer |
| Au1rxx-base64 | 0.815 | 0.829 | 35 | 93 | prefer |
| DeltaKronecker-all | 0.46 | 0.377 | 77 | 6810 | observe |
| nscl5-all | 0.3 | 1.0 | 1 | 1126 | observe |
| tg-LonUp_M | 0.262 | 1.0 | 1 | 177 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4507 | observe |
| Epodonios-all | 0.255 | None | 0 | 7491 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3976 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6983 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 3744 | observe |
| barry-far-vless | 0.255 | None | 0 | 4443 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4516 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 49 |
| geo | TimeoutError | - | 29 |
| cn-block | TimeoutError | - | 26 |
| 204 | ProxyError | - | 17 |
| speed | TimeoutError | - | 15 |
| 204 | TimeoutError | - | 14 |
| geo | ClientOSError | - | 12 |
| cn-block | ClientOSError | - | 11 |
| 204 | ClientOSError | - | 11 |
| speed | ProxyError | - | 4 |
| cn-block | ProxyError | - | 3 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
