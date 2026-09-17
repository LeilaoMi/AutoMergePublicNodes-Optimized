# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-17 04:42:18 |
| 运行耗时 | 1159.3s |
| 订阅源总数 | 107 |
| 健康订阅源 | 96 |
| 原始节点 | 89183 |
| 去重后节点 | 24536 |
| TCP 可达 | 3000 |
| 真实可用 | 537 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 24536 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.3 |
| geo | 1.6 |
| tcp | 42.2 |
| probe | 429.1 |
| real_test | 610.6 |
| generate | 70.5 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 52802 |
| vmess | 14151 |
| shadowsocks | 10863 |
| trojan | 9055 |
| hysteria2 | 1422 |
| http | 676 |
| shadowsocksr | 125 |
| socks | 77 |
| hysteria | 8 |
| tuic | 2 |
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
| 80.36 | vless | 284.3 | 723.4 | 21.2 | 0.0 | 10.0 | 11.36 | 17.8 | Au1rxx-base64 | 79.141.172.154 |
| 80.06 | hysteria2 | 308.3 | 732.4 | 20.64 | 0.0 | 10.0 | 13.42 | 18.08 | mheidari-all | 159.223.157.129 |
| 79.78 | shadowsocks | 230.8 | 596.4 | 22.43 | 0.0 | 10.0 | 13.62 | 18.08 | mheidari-all | 156.146.38.170 |
| 79.08 | shadowsocks | 238.6 | 607.8 | 22.25 | 0.0 | 10.0 | 13.62 | 17.8 | Au1rxx-base64 | 156.146.38.168 |
| 78.67 | shadowsocks | 281.8 | 680.3 | 21.25 | 0.0 | 10.0 | 13.62 | 17.8 | Au1rxx-base64 | 37.19.198.236 |
| 78.65 | hysteria2 | 282.3 | 538.2 | 21.24 | 0.0 | 10.0 | 13.42 | 17.8 | Au1rxx-base64 | 66.94.121.46 |
| 78.29 | shadowsocks | 279.4 | 674.6 | 21.31 | 0.0 | 10.0 | 13.62 | 17.8 | Au1rxx-base64 | 37.19.198.243 |
| 77.32 | vless | 225.6 | 605.4 | 22.56 | 0.0 | 10.0 | 11.36 | 16.4 | DeltaKronecker-all | 88.216.57.128 |
| 76.28 | vless | 300.8 | 662.1 | 20.82 | 0.0 | 10.0 | 11.36 | 17.8 | Au1rxx-base64 | 195.123.235.177 |
| 76.12 | shadowsocks | 276.1 | 674.0 | 21.39 | 0.0 | 10.0 | 13.62 | 18.08 | mheidari-all | 37.19.198.160 |
| 75.71 | vless | 286.5 | 560.6 | 21.15 | 0.0 | 10.0 | 11.36 | 17.8 | Au1rxx-base64 | 172.235.43.210 |
| 75.57 | vless | 410.2 | 949.2 | 18.28 | 0.0 | 10.0 | 11.36 | 17.8 | Au1rxx-base64 | 169.40.42.225 |
| 75.38 | shadowsocks | 356.0 | 911.1 | 19.54 | 0.0 | 10.0 | 13.62 | 17.8 | Au1rxx-base64 | 37.19.198.244 |
| 75.25 | vless | 303.0 | 559.5 | 20.76 | 0.0 | 10.0 | 11.36 | 17.8 | Au1rxx-base64 | 144.172.104.26 |
| 75.04 | vless | 355.1 | 786.5 | 19.56 | 0.0 | 10.0 | 11.36 | 17.8 | Au1rxx-base64 | 169.40.42.212 |
| 75.02 | vless | 388.4 | 915.9 | 18.79 | 0.0 | 10.0 | 11.36 | 17.8 | Au1rxx-base64 | 137.184.218.169 |
| 74.79 | trojan | 308.9 | 581.9 | 20.63 | 0.0 | 10.0 | 13.5 | 17.8 | Au1rxx-base64 | 100.42.228.109 |
| 74.71 | vless | 399.4 | 970.9 | 18.53 | 0.0 | 10.0 | 11.36 | 17.8 | Au1rxx-base64 | 169.40.42.235 |
| 74.68 | hysteria2 | 316.1 | 782.5 | 20.46 | 0.0 | 10.0 | 13.42 | 17.8 | Au1rxx-base64 | 108.59.244.158 |
| 74.59 | shadowsocks | 398.4 | 990.7 | 18.56 | 0.0 | 10.0 | 13.62 | 18.08 | mheidari-all | 15.204.247.206 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.939 | 0.878 | 279 | 1590 | prefer |
| Surfboard-tg-mixed | 0.83 | 0.773 | 22 | 7408 | prefer |
| ermaozi | 0.774 | 0.778 | 27 | 396 | prefer |
| mheidari-all | 0.577 | 0.497 | 165 | 17792 | observe |
| DeltaKronecker-all | 0.411 | 0.33 | 497 | 6081 | observe |
| ermaozi-get_subscribe | 0.398 | 0.545 | 11 | 431 | observe |
| tg-oneclickvpnkeys | 0.26 | 1.0 | 1 | 130 | observe |
| Epodonios-all | 0.255 | None | 0 | 7930 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9115 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5925 | observe |
| barry-far-vless | 0.255 | None | 0 | 6194 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4234 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 2484 | observe |
| ninja-vless | 0.251 | 0.333 | 3 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 255 |
| geo | ClientOSError | - | 70 |
| speed | TimeoutError | - | 55 |
| speed | ClientOSError | - | 44 |
| 204 | ProxyError | - | 22 |
| cn-block | TimeoutError | - | 10 |
| 204 | TimeoutError | - | 6 |
| cn-block | ClientOSError | - | 5 |
| 204 | ClientOSError | - | 1 |
| cn-block | ProxyError | - | 1 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
