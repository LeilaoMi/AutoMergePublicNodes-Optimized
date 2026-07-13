# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-13 09:40:59 |
| 运行耗时 | 183.8s |
| 订阅源总数 | 107 |
| 健康订阅源 | 103 |
| 原始节点 | 76766 |
| 去重后节点 | 23821 |
| TCP 可达 | 3000 |
| 真实可用 | 288 |
| Verified 输出 | 288 |
| Global 输出 | 297 |
| All 输出 | 23821 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.5 |
| geo | 1.4 |
| tcp | 31.8 |
| probe | 47.9 |
| real_test | 76.4 |
| generate | 21.8 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 44018 |
| trojan | 11558 |
| vmess | 10725 |
| shadowsocks | 9758 |
| hysteria2 | 389 |
| shadowsocksr | 146 |
| http | 137 |
| socks | 26 |
| hysteria | 6 |
| tuic | 3 |

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
| 77.28 | trojan | 275.0 | 493.9 | 21.41 | 0.0 | 10.0 | 14.2 | 19.92 | Surfboard-tg-mixed | 162.159.252.15 |
| 74.08 | trojan | 312.7 | 647.7 | 20.54 | 0.0 | 10.0 | 14.2 | 16.04 | DeltaKronecker-all | 64.94.95.114 |
| 73.26 | vless | 195.1 | 471.4 | 23.26 | 0.0 | 10.0 | 4.96 | 16.04 | DeltaKronecker-all | 104.17.90.246 |
| 72.94 | trojan | 281.7 | 437.8 | 21.26 | 0.0 | 10.0 | 14.2 | 19.92 | Surfboard-tg-mixed | 45.131.5.9 |
| 72.29 | trojan | 402.9 | 952.7 | 18.45 | 0.0 | 10.0 | 14.2 | 16.04 | DeltaKronecker-all | 64.94.95.117 |
| 71.98 | trojan | 301.1 | 657.8 | 20.81 | 0.0 | 10.0 | 14.2 | 16.04 | DeltaKronecker-all | 64.94.95.115 |
| 71.07 | trojan | 363.4 | 487.6 | 19.37 | 0.0 | 10.0 | 14.2 | 16.04 | DeltaKronecker-all | 104.16.101.215 |
| 68.59 | trojan | 462.3 | 381.3 | 17.08 | 0.7 | 10.0 | 14.2 | 16.04 | DeltaKronecker-all | 104.21.29.125 |
| 68.5 | trojan | 453.3 | 375.0 | 17.28 | 0.94 | 9.37 | 14.2 | 17.56 | mheidari-all | 119.246.1.143 |
| 68.33 | trojan | 470.5 | 381.5 | 16.89 | 0.69 | 10.0 | 14.2 | 16.04 | DeltaKronecker-all | 172.67.149.1 |
| 67.9 | trojan | 628.7 | 915.3 | 13.22 | 0.0 | 10.0 | 14.2 | 19.92 | Surfboard-tg-mixed | 104.17.121.71 |
| 67.71 | trojan | 639.5 | 932.1 | 12.97 | 0.0 | 10.0 | 14.2 | 19.92 | Surfboard-tg-mixed | 104.19.64.105 |
| 67.67 | trojan | 639.8 | 918.5 | 12.97 | 0.0 | 10.0 | 14.2 | 19.92 | Surfboard-tg-mixed | 45.130.125.75 |
| 67.53 | trojan | 649.2 | 943.3 | 12.75 | 0.0 | 10.0 | 14.2 | 19.92 | Surfboard-tg-mixed | 212.183.88.136 |
| 67.45 | trojan | 198.4 | 478.9 | 23.19 | 0.0 | 0.0 | 14.2 | 17.56 | mheidari-all | jp1.8b1c7c70-ecf1-6891-9fa7-68a86662f902.cheathub.net |
| 67.44 | trojan | 647.3 | 945.5 | 12.79 | 0.0 | 10.0 | 14.2 | 19.92 | Surfboard-tg-mixed | 198.62.62.23 |
| 67.43 | vless | 231.1 | 531.6 | 22.43 | 0.0 | 10.0 | 4.96 | 16.04 | DeltaKronecker-all | 69.46.46.84 |
| 67.37 | trojan | 656.3 | 969.8 | 12.59 | 0.0 | 10.0 | 14.2 | 19.92 | Surfboard-tg-mixed | 188.114.99.0 |
| 67.15 | trojan | 666.3 | 981.4 | 12.35 | 0.0 | 10.0 | 14.2 | 19.92 | Surfboard-tg-mixed | 104.21.40.34 |
| 66.91 | trojan | 349.6 | 347.7 | 19.68 | 1.96 | 9.37 | 14.2 | 14.9 | Au1rxx-base64 | busy-lab.rooster465.autos |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| mheidari-all | 0.815 | 0.742 | 66 | 16468 | prefer |
| DeltaKronecker-all | 0.688 | 0.609 | 207 | 7926 | observe |
| Surfboard-tg-mixed | 0.683 | 0.605 | 114 | 5436 | observe |
| Au1rxx-base64 | 0.413 | 0.667 | 9 | 103 | observe |
| xiaoji235-airport-v2ray-all | 0.321 | 1.0 | 1 | 1647 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 3897 | observe |
| Epodonios-all | 0.255 | None | 0 | 6476 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3979 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6409 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4097 | observe |
| barry-far-vless | 0.255 | None | 0 | 4724 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5412 | observe |
| nscl5-all | 0.236 | None | 0 | 1526 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 51 |
| speed | ClientOSError | - | 30 |
| 204 | TimeoutError | - | 11 |
| geo | ClientOSError | - | 9 |
| speed | TimeoutError | - | 9 |
| 204 | ClientOSError | - | 8 |
| cn-block | ClientOSError | - | 7 |
| 204 | ProxyError | - | 7 |
| cn-block | ProxyError | - | 6 |
| speed | ProxyError | - | 5 |
| geo | ProxyError | - | 5 |
| cn-block | TimeoutError | - | 3 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 288 | - |
| global | False | 300 | 297 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
