# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-18 13:32:58 |
| 运行耗时 | 343.5s |
| 订阅源总数 | 107 |
| 健康订阅源 | 99 |
| 原始节点 | 81014 |
| 去重后节点 | 22082 |
| TCP 可达 | 3000 |
| 真实可用 | 860 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22082 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.2 |
| geo | 0.8 |
| tcp | 31.5 |
| probe | 68.3 |
| real_test | 204.0 |
| generate | 33.7 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 47667 |
| trojan | 11844 |
| vmess | 10663 |
| shadowsocks | 10230 |
| hysteria2 | 332 |
| shadowsocksr | 124 |
| socks | 76 |
| http | 55 |
| hysteria | 14 |
| tuic | 7 |
| anytls | 2 |

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
| 78.81 | shadowsocks | 227.0 | 628.0 | 22.52 | 0.0 | 10.0 | 12.55 | 17.74 | Au1rxx-base64 | 37.19.198.243 |
| 78.71 | shadowsocks | 231.4 | 630.7 | 22.42 | 0.0 | 10.0 | 12.55 | 17.74 | Au1rxx-base64 | 37.19.198.236 |
| 78.59 | shadowsocks | 236.5 | 649.9 | 22.3 | 0.0 | 10.0 | 12.55 | 17.74 | Au1rxx-base64 | 37.19.198.244 |
| 78.56 | shadowsocks | 237.7 | 646.1 | 22.27 | 0.0 | 10.0 | 12.55 | 17.74 | Au1rxx-base64 | 37.19.198.160 |
| 75.4 | shadowsocks | 282.7 | 646.3 | 21.23 | 0.0 | 10.0 | 12.55 | 17.74 | Au1rxx-base64 | 156.146.38.169 |
| 74.65 | shadowsocks | 290.7 | 661.2 | 21.05 | 0.0 | 10.0 | 12.55 | 17.74 | Au1rxx-base64 | 156.146.38.167 |
| 73.47 | shadowsocks | 322.0 | 768.9 | 20.32 | 0.0 | 10.0 | 12.55 | 17.74 | Au1rxx-base64 | 156.146.38.168 |
| 73.05 | shadowsocks | 246.9 | 659.6 | 22.06 | 0.0 | 10.0 | 12.55 | 12.94 | mheidari-all | 108.181.57.93 |
| 72.76 | shadowsocks | 372.8 | 918.9 | 19.15 | 0.0 | 10.0 | 12.55 | 17.74 | Au1rxx-base64 | 156.146.38.170 |
| 72.01 | trojan | 379.6 | 636.3 | 18.99 | 0.0 | 10.0 | 14.09 | 18.18 | Surfboard-tg-mixed | 104.17.148.22 |
| 71.97 | shadowsocks | 305.9 | 571.1 | 20.7 | 0.0 | 10.0 | 12.55 | 17.74 | Au1rxx-base64 | 173.244.56.6 |
| 71.05 | shadowsocks | 333.2 | 921.6 | 20.06 | 0.0 | 10.0 | 12.55 | 12.94 | mheidari-all | 68.168.222.210 |
| 70.97 | trojan | 473.2 | 801.3 | 16.82 | 0.0 | 10.0 | 14.09 | 18.18 | Surfboard-tg-mixed | 198.62.62.23 |
| 70.96 | trojan | 463.1 | 776.8 | 17.06 | 0.0 | 10.0 | 14.09 | 18.18 | Surfboard-tg-mixed | 165.215.250.14 |
| 70.63 | shadowsocks | 329.7 | 604.3 | 20.15 | 0.0 | 10.0 | 12.55 | 17.74 | Au1rxx-base64 | 108.181.0.177 |
| 70.55 | trojan | 478.6 | 789.0 | 16.7 | 0.0 | 10.0 | 14.09 | 18.18 | Surfboard-tg-mixed | 45.130.125.75 |
| 70.3 | vless | 309.4 | 850.2 | 20.62 | 0.0 | 10.0 | 3.94 | 17.74 | Au1rxx-base64 | 159.89.87.21 |
| 70.3 | trojan | 392.0 | 604.7 | 18.7 | 0.0 | 10.0 | 14.09 | 18.18 | Surfboard-tg-mixed | 188.114.98.0 |
| 70.23 | trojan | 442.7 | 745.4 | 17.53 | 0.0 | 10.0 | 14.09 | 18.18 | Surfboard-tg-mixed | 3.67.171.41 |
| 70.01 | shadowsocks | 345.5 | 519.5 | 19.78 | 0.0 | 10.0 | 12.55 | 17.74 | Au1rxx-base64 | 108.181.118.10 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.976 | 1.0 | 36 | 61 | prefer |
| mheidari-all | 0.883 | 0.804 | 449 | 19072 | prefer |
| nscl5-all | 0.862 | 0.81 | 21 | 1976 | prefer |
| Au1rxx-base64 | 0.834 | 0.833 | 132 | 150 | prefer |
| DeltaKronecker-all | 0.73 | 0.652 | 224 | 4096 | prefer |
| Surfboard-tg-mixed | 0.662 | 0.583 | 321 | 5677 | observe |
| xiaoji235-airport-v2ray-all | 0.438 | 1.0 | 3 | 4321 | observe |
| Epodonios-all | 0.255 | None | 0 | 6767 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3971 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7013 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4291 | observe |
| barry-far-vless | 0.255 | None | 0 | 4927 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5334 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 134 |
| speed | ClientOSError | - | 60 |
| 204 | TimeoutError | - | 39 |
| cn-block | TimeoutError | - | 32 |
| geo | ClientOSError | - | 27 |
| 204 | ProxyError | - | 13 |
| speed | TimeoutError | - | 9 |
| 204 | ClientOSError | - | 5 |
| geo | ProxyError | - | 3 |
| cn-block | ClientOSError | - | 3 |
| cn-block | ProxyError | - | 2 |
| speed | ProxyError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
