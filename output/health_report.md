# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-17 08:23:28 |
| 运行耗时 | 261.7s |
| 订阅源总数 | 107 |
| 健康订阅源 | 98 |
| 原始节点 | 79278 |
| 去重后节点 | 24796 |
| TCP 可达 | 3000 |
| 真实可用 | 562 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 24796 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.8 |
| geo | 1.1 |
| tcp | 32.3 |
| probe | 54.5 |
| real_test | 127.5 |
| generate | 41.4 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 45639 |
| trojan | 12547 |
| vmess | 10843 |
| shadowsocks | 9756 |
| hysteria2 | 275 |
| shadowsocksr | 130 |
| http | 51 |
| socks | 27 |
| hysteria | 8 |
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
| 81.15 | shadowsocks | 235.1 | 633.6 | 22.34 | 0.0 | 10.0 | 13.41 | 19.4 | mheidari-all | 147.90.234.133 |
| 79.67 | shadowsocks | 262.7 | 730.4 | 21.7 | 0.0 | 10.0 | 13.41 | 18.56 | Au1rxx-base64 | 37.19.198.236 |
| 79.02 | shadowsocks | 290.5 | 808.6 | 21.05 | 0.0 | 10.0 | 13.41 | 18.56 | Au1rxx-base64 | 37.19.198.243 |
| 77.89 | shadowsocks | 317.9 | 889.4 | 20.42 | 0.0 | 10.0 | 13.41 | 18.56 | Au1rxx-base64 | 68.168.222.210 |
| 76.93 | shadowsocks | 344.6 | 899.2 | 19.8 | 0.0 | 10.0 | 13.41 | 18.56 | Au1rxx-base64 | 50.114.177.235 |
| 76.75 | vmess | 342.7 | 984.2 | 19.85 | 0.0 | 10.0 | 12.0 | 19.4 | mheidari-all | 67.220.95.3 |
| 76.69 | shadowsocks | 282.3 | 647.3 | 21.24 | 0.0 | 10.0 | 13.41 | 18.56 | Au1rxx-base64 | 156.146.38.167 |
| 76.64 | shadowsocks | 280.8 | 631.1 | 21.28 | 0.0 | 10.0 | 13.41 | 18.56 | Au1rxx-base64 | 156.146.38.170 |
| 76.55 | shadowsocks | 248.0 | 664.2 | 22.04 | 0.0 | 10.0 | 13.41 | 18.56 | Au1rxx-base64 | 108.181.57.93 |
| 76.35 | shadowsocks | 286.1 | 645.9 | 21.16 | 0.0 | 10.0 | 13.41 | 18.56 | Au1rxx-base64 | 156.146.38.169 |
| 76.08 | shadowsocks | 290.7 | 652.1 | 21.05 | 0.0 | 10.0 | 13.41 | 18.56 | Au1rxx-base64 | 156.146.38.168 |
| 75.86 | shadowsocks | 353.8 | 881.1 | 19.59 | 0.0 | 10.0 | 13.41 | 18.56 | Au1rxx-base64 | 185.196.61.82 |
| 75.29 | trojan | 431.8 | 1047.2 | 17.78 | 0.0 | 10.0 | 14.5 | 19.4 | mheidari-all | 64.94.95.118 |
| 74.99 | shadowsocks | 232.0 | 640.1 | 22.41 | 0.0 | 10.0 | 13.41 | 18.56 | Au1rxx-base64 | 37.19.198.244 |
| 74.66 | shadowsocks | 224.5 | 596.7 | 22.58 | 0.0 | 10.0 | 13.41 | 19.4 | mheidari-all | 198.98.53.130 |
| 73.21 | trojan | 371.0 | 861.7 | 19.19 | 0.0 | 10.0 | 14.5 | 15.92 | DeltaKronecker-all | 64.94.95.117 |
| 73.15 | trojan | 386.8 | 898.3 | 18.82 | 0.0 | 10.0 | 14.5 | 15.92 | DeltaKronecker-all | 64.94.95.115 |
| 72.98 | trojan | 459.8 | 807.0 | 17.13 | 0.0 | 10.0 | 14.5 | 19.4 | mheidari-all | 104.17.131.88 |
| 72.94 | trojan | 395.1 | 935.1 | 18.63 | 0.0 | 10.0 | 14.5 | 15.92 | DeltaKronecker-all | 64.94.95.114 |
| 72.91 | shadowsocks | 338.6 | 955.5 | 19.94 | 0.0 | 10.0 | 13.41 | 18.56 | Au1rxx-base64 | 37.19.198.160 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.978 | 0.981 | 105 | 149 | prefer |
| zhangkai | 0.976 | 1.0 | 36 | 61 | prefer |
| mheidari-all | 0.964 | 0.89 | 145 | 16487 | prefer |
| Surfboard-tg-mixed | 0.826 | 0.75 | 124 | 5351 | prefer |
| DeltaKronecker-all | 0.674 | 0.595 | 333 | 8967 | observe |
| nscl5-all | 0.328 | 1.0 | 1 | 1821 | observe |
| xiaoji235-airport-v2ray-all | 0.322 | 1.0 | 1 | 1680 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| Epodonios-all | 0.255 | None | 0 | 6542 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6827 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4142 | observe |
| barry-far-vless | 0.255 | None | 0 | 4764 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5208 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 83 |
| speed | ClientOSError | - | 40 |
| 204 | ProxyError | - | 17 |
| speed | TimeoutError | - | 9 |
| cn-block | ClientOSError | - | 8 |
| 204 | ClientOSError | - | 8 |
| cn-block | TimeoutError | - | 7 |
| 204 | TimeoutError | - | 5 |
| cn-block | ProxyError | - | 3 |
| geo | ClientOSError | - | 3 |
| speed | ProxyError | - | 2 |
| geo | ProxyError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
