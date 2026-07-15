# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-15 02:55:28 |
| 运行耗时 | 195.1s |
| 订阅源总数 | 107 |
| 健康订阅源 | 103 |
| 原始节点 | 76515 |
| 去重后节点 | 23743 |
| TCP 可达 | 3000 |
| 真实可用 | 285 |
| Verified 输出 | 285 |
| Global 输出 | 293 |
| All 输出 | 23743 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.7 |
| geo | 1.5 |
| tcp | 33.2 |
| probe | 43.2 |
| real_test | 82.5 |
| generate | 30.2 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 43611 |
| trojan | 11286 |
| vmess | 11134 |
| shadowsocks | 9817 |
| hysteria2 | 349 |
| http | 137 |
| shadowsocksr | 131 |
| socks | 32 |
| hysteria | 10 |
| anytls | 5 |
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
| 72.26 | trojan | 285.8 | 444.0 | 21.16 | 0.0 | 10.0 | 11.34 | 15.44 | DeltaKronecker-all | 104.16.100.215 |
| 69.1 | hysteria2 | 192.5 | 495.9 | 23.32 | 0.0 | 10.0 | 12.0 | 9.88 | Au1rxx-base64 | 38.148.249.252 |
| 68.48 | trojan | 330.2 | 361.6 | 20.13 | 1.44 | 10.0 | 11.34 | 15.44 | DeltaKronecker-all | 104.16.99.215 |
| 68.24 | trojan | 292.9 | 634.6 | 21.0 | 0.0 | 10.0 | 11.34 | 15.44 | DeltaKronecker-all | 64.94.95.117 |
| 68.14 | trojan | 346.2 | 346.1 | 19.76 | 2.02 | 9.89 | 11.34 | 15.44 | DeltaKronecker-all | 52.68.90.114 |
| 68.05 | trojan | 287.3 | 636.7 | 21.13 | 0.0 | 10.0 | 11.34 | 15.44 | DeltaKronecker-all | 64.94.95.115 |
| 67.81 | trojan | 351.7 | 357.3 | 19.64 | 1.6 | 9.87 | 11.34 | 15.44 | DeltaKronecker-all | 18.179.120.96 |
| 66.59 | trojan | 343.6 | 602.6 | 19.82 | 0.0 | 10.0 | 11.34 | 15.44 | DeltaKronecker-all | 5.10.215.9 |
| 66.07 | trojan | 283.9 | 627.1 | 21.21 | 0.0 | 10.0 | 11.34 | 15.44 | DeltaKronecker-all | 64.94.95.114 |
| 65.93 | trojan | 367.5 | 407.3 | 19.27 | 0.0 | 9.9 | 11.34 | 15.44 | DeltaKronecker-all | 52.194.192.245 |
| 65.86 | trojan | 369.2 | 413.0 | 19.23 | 0.0 | 9.89 | 11.34 | 15.44 | DeltaKronecker-all | 43.207.192.70 |
| 65.48 | trojan | 375.1 | 894.8 | 19.09 | 0.0 | 10.0 | 11.34 | 13.06 | mheidari-all | 64.94.95.118 |
| 64.61 | vmess | 425.5 | 939.5 | 17.93 | 0.0 | 10.0 | 13.12 | 13.3 | Surfboard-tg-mixed | 67.220.95.3 |
| 64.33 | vless | 296.3 | 745.1 | 20.92 | 0.0 | 10.0 | 3.56 | 15.44 | DeltaKronecker-all | 129.146.65.178 |
| 64.2 | trojan | 490.2 | 679.8 | 16.43 | 0.0 | 10.0 | 11.34 | 13.3 | Surfboard-tg-mixed | 162.159.38.62 |
| 62.68 | trojan | 431.0 | 447.2 | 17.8 | 0.0 | 10.0 | 11.34 | 13.3 | Surfboard-tg-mixed | 199.232.78.140 |
| 62.54 | vmess | 504.1 | 1163.9 | 16.11 | 0.0 | 10.0 | 13.12 | 13.3 | Surfboard-tg-mixed | 67.220.85.46 |
| 62.22 | vless | 262.1 | 581.9 | 21.71 | 0.0 | 10.0 | 3.56 | 15.44 | DeltaKronecker-all | 172.64.53.219 |
| 62.16 | vless | 318.3 | 428.9 | 20.41 | 0.0 | 10.0 | 3.56 | 15.44 | DeltaKronecker-all | 162.159.45.241 |
| 61.52 | shadowsocks | 381.2 | 288.4 | 18.95 | 4.18 | 9.36 | 11.25 | 15.44 | DeltaKronecker-all | 103.149.182.105 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| Surfboard-tg-mixed | 0.806 | 0.732 | 82 | 5500 | prefer |
| mheidari-all | 0.741 | 0.664 | 110 | 18109 | prefer |
| DeltaKronecker-all | 0.46 | 0.379 | 298 | 6421 | observe |
| Au1rxx-base64 | 0.317 | 1.0 | 2 | 149 | observe |
| nscl5-all | 0.26 | 0.5 | 2 | 1300 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4019 | observe |
| Epodonios-all | 0.255 | None | 0 | 6322 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3968 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6061 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4205 | observe |
| barry-far-vless | 0.255 | None | 0 | 4653 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5187 | observe |
| xiaoji235-airport-v2ray-all | 0.245 | None | 0 | 1741 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 134 |
| geo | TimeoutError | - | 57 |
| geo | ClientOSError | - | 36 |
| speed | TimeoutError | - | 6 |
| cn-block | TimeoutError | - | 5 |
| 204 | ClientOSError | - | 3 |
| cn-block | ProxyError | - | 2 |
| cn-block | ClientOSError | - | 2 |
| 204 | ProxyError | - | 1 |
| 204 | TimeoutError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 165 | 285 | - |
| global | False | 173 | 293 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
