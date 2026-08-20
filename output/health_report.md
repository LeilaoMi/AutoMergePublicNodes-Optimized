# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-20 18:53:22 |
| 运行耗时 | 340.3s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 95001 |
| 去重后节点 | 25247 |
| TCP 可达 | 3000 |
| 真实可用 | 1089 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 25247 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.5 |
| geo | 0.9 |
| tcp | 40.9 |
| probe | 67.0 |
| real_test | 194.9 |
| generate | 31.1 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 53036 |
| trojan | 18758 |
| shadowsocks | 10564 |
| vmess | 10414 |
| hysteria2 | 1673 |
| shadowsocksr | 202 |
| http | 164 |
| socks | 131 |
| anytls | 32 |
| hysteria | 15 |
| tuic | 12 |

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
| 82.99 | hysteria2 | 260.0 | 257.4 | 21.76 | 5.35 | 9.77 | 13.57 | 20.0 | Au1rxx-base64 | 45.32.252.144 |
| 81.5 | hysteria2 | 269.1 | 566.7 | 21.55 | 0.0 | 10.0 | 13.57 | 17.42 | mheidari-all | 150.241.102.127 |
| 80.69 | trojan | 282.2 | 677.9 | 21.25 | 0.0 | 10.0 | 14.77 | 19.14 | Surfboard-tg-mixed | 128.14.181.220 |
| 80.39 | shadowsocks | 260.5 | 612.6 | 21.75 | 0.0 | 10.0 | 14.0 | 19.14 | Surfboard-tg-mixed | 23.150.248.20 |
| 80.12 | shadowsocks | 217.0 | 497.2 | 22.75 | 0.0 | 10.0 | 14.0 | 20.0 | Au1rxx-base64 | 209.38.142.23 |
| 79.76 | trojan | 280.7 | 564.6 | 21.28 | 0.0 | 10.0 | 14.77 | 20.0 | Au1rxx-base64 | 44.247.89.62 |
| 79.65 | trojan | 289.8 | 591.4 | 21.07 | 0.0 | 10.0 | 14.77 | 20.0 | Au1rxx-base64 | 34.221.30.108 |
| 79.61 | trojan | 285.4 | 585.1 | 21.17 | 0.0 | 10.0 | 14.77 | 20.0 | Au1rxx-base64 | 100.22.163.167 |
| 79.61 | trojan | 290.5 | 592.9 | 21.05 | 0.0 | 10.0 | 14.77 | 20.0 | Au1rxx-base64 | 35.88.120.18 |
| 79.4 | trojan | 291.4 | 602.9 | 21.03 | 0.0 | 10.0 | 14.77 | 20.0 | Au1rxx-base64 | 35.92.245.6 |
| 79.15 | trojan | 292.8 | 605.9 | 21.0 | 0.0 | 10.0 | 14.77 | 20.0 | Au1rxx-base64 | 34.210.213.17 |
| 79.02 | trojan | 291.9 | 597.3 | 21.02 | 0.0 | 10.0 | 14.77 | 20.0 | Au1rxx-base64 | 34.220.224.252 |
| 78.8 | trojan | 283.0 | 572.7 | 21.23 | 0.0 | 10.0 | 14.77 | 19.14 | Surfboard-tg-mixed | 54.244.169.225 |
| 78.76 | shadowsocks | 276.4 | 576.6 | 21.38 | 0.0 | 10.0 | 14.0 | 20.0 | Au1rxx-base64 | 154.12.242.150 |
| 78.74 | trojan | 291.9 | 598.0 | 21.02 | 0.0 | 10.0 | 14.77 | 19.14 | Surfboard-tg-mixed | 35.90.27.143 |
| 78.58 | trojan | 291.4 | 586.8 | 21.03 | 0.0 | 10.0 | 14.77 | 19.14 | Surfboard-tg-mixed | 54.188.176.255 |
| 78.53 | trojan | 333.0 | 724.4 | 20.07 | 0.0 | 10.0 | 14.77 | 20.0 | Au1rxx-base64 | 35.160.249.189 |
| 78.36 | trojan | 296.6 | 599.1 | 20.91 | 0.0 | 10.0 | 14.77 | 19.14 | Surfboard-tg-mixed | 54.245.126.186 |
| 78.34 | shadowsocks | 260.3 | 616.7 | 21.75 | 0.0 | 10.0 | 14.0 | 20.0 | Au1rxx-base64 | 154.53.60.212 |
| 78.34 | trojan | 288.5 | 585.5 | 21.1 | 0.0 | 10.0 | 14.77 | 20.0 | Au1rxx-base64 | 34.223.2.163 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | 0.953 | 571 | 1789 | prefer |
| mheidari-all | 1.0 | 0.936 | 251 | 22064 | prefer |
| zhangkai | 0.988 | 0.991 | 112 | 144 | prefer |
| Surfboard-tg-mixed | 0.911 | 0.833 | 234 | 6440 | prefer |
| DeltaKronecker-all | 0.372 | 0.444 | 9 | 6781 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4958 | observe |
| Epodonios-all | 0.255 | None | 0 | 7181 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7349 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5117 | observe |
| barry-far-vless | 0.255 | None | 0 | 5501 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4586 | observe |
| nscl5-all | 0.255 | None | 0 | 2418 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 5974 | observe |
| Au1rxx-clash | 0.247 | None | 0 | 1789 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| cn-block | TimeoutError | - | 19 |
| 204 | TimeoutError | - | 18 |
| geo | TimeoutError | - | 16 |
| geo | ClientOSError | - | 11 |
| 204 | ProxyError | - | 6 |
| speed | TimeoutError | - | 6 |
| 204 | ClientOSError | - | 4 |
| cn-block | ClientOSError | - | 4 |
| speed | ClientOSError | - | 4 |
| cn-block | ProxyError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
