# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-06-17 19:18:58 |
| 运行耗时 | 352.7s |
| 订阅源总数 | 44 |
| 健康订阅源 | 44 |
| 原始节点 | 43688 |
| 去重后节点 | 18013 |
| TCP 可达 | 3000 |
| 真实可用 | 987 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 18013 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 3.2 |
| geo | 1.2 |
| tcp | 19.4 |
| probe | 72.5 |
| real_test | 220.7 |
| generate | 35.7 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 22488 |
| shadowsocks | 8351 |
| trojan | 7005 |
| vmess | 5419 |
| hysteria2 | 198 |
| http | 95 |
| shadowsocksr | 87 |
| socks | 38 |
| hysteria | 6 |
| tuic | 1 |

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
| 62.6 | shadowsocks | 237.9 | 635.4 | 22.27 | 0.0 | 10.0 | 11.25 | 8.08 | Au1rxx-base64 | 37.19.198.236 |
| 62.6 | shadowsocks | 238.1 | 643.8 | 22.27 | 0.0 | 10.0 | 11.25 | 8.08 | Au1rxx-base64 | 37.19.198.243 |
| 62.55 | shadowsocks | 240.3 | 641.8 | 22.22 | 0.0 | 10.0 | 11.25 | 8.08 | Au1rxx-base64 | 37.19.198.160 |
| 62.54 | shadowsocks | 240.4 | 642.8 | 22.21 | 0.0 | 10.0 | 11.25 | 8.08 | Au1rxx-base64 | 37.19.198.244 |
| 61.82 | vless | 275.4 | 752.8 | 21.4 | 0.0 | 10.0 | 7.88 | 7.54 | DeltaKronecker-all | 47.253.226.114 |
| 61.66 | vless | 282.4 | 739.4 | 21.24 | 0.0 | 10.0 | 7.88 | 7.54 | DeltaKronecker-all | 152.53.171.40 |
| 61.59 | vless | 273.8 | 638.4 | 21.44 | 0.0 | 10.0 | 7.88 | 7.54 | DeltaKronecker-all | 154.88.3.220 |
| 61.29 | shadowsocks | 249.5 | 649.7 | 22.0 | 0.0 | 10.0 | 11.25 | 7.54 | DeltaKronecker-all | 108.181.57.93 |
| 60.75 | vless | 321.6 | 886.9 | 20.33 | 0.0 | 10.0 | 7.88 | 7.54 | DeltaKronecker-all | 193.202.11.143 |
| 60.74 | vless | 322.0 | 860.0 | 20.32 | 0.0 | 10.0 | 7.88 | 7.54 | DeltaKronecker-all | 147.182.212.232 |
| 59.55 | shadowsocks | 281.7 | 654.8 | 21.26 | 0.0 | 10.0 | 11.25 | 8.08 | Au1rxx-base64 | 156.146.38.169 |
| 59.15 | shadowsocks | 275.9 | 628.9 | 21.39 | 0.0 | 10.0 | 11.25 | 8.08 | Au1rxx-base64 | 156.146.38.167 |
| 58.94 | shadowsocks | 275.0 | 631.3 | 21.41 | 0.0 | 10.0 | 11.25 | 8.08 | Au1rxx-base64 | 156.146.38.170 |
| 58.26 | vless | 304.2 | 681.0 | 20.74 | 0.0 | 10.0 | 7.88 | 7.54 | DeltaKronecker-all | 193.233.202.7 |
| 58.14 | shadowsocks | 311.1 | 741.2 | 20.58 | 0.0 | 10.0 | 11.25 | 8.08 | Au1rxx-base64 | 156.146.38.168 |
| 58.05 | vless | 424.1 | 525.7 | 17.96 | 0.0 | 10.0 | 7.88 | 7.54 | DeltaKronecker-all | 162.218.95.14 |
| 57.79 | vless | 463.6 | 804.3 | 17.05 | 0.0 | 10.0 | 7.88 | 17.68 | snakem982 | 185.229.191.42 |
| 57.72 | vless | 466.0 | 838.2 | 16.99 | 0.0 | 10.0 | 7.88 | 17.68 | snakem982 | 185.229.191.145 |
| 57.53 | vless | 464.3 | 811.3 | 17.03 | 0.0 | 10.0 | 7.88 | 17.68 | snakem982 | 185.229.191.49 |
| 57.53 | vless | 470.6 | 844.6 | 16.89 | 0.0 | 10.0 | 7.88 | 17.68 | snakem982 | 185.229.191.169 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Surfboard-tg-mixed | 0.933 | 0.856 | 236 | 4729 | prefer |
| Au1rxx-base64 | 0.883 | 0.891 | 64 | 108 | prefer |
| snakem982 | 0.88 | 0.891 | 55 | 73 | prefer |
| mheidari-all | 0.872 | 0.818 | 22 | 2000 | prefer |
| DeltaKronecker-all | 0.823 | 0.744 | 886 | 7763 | prefer |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| roosterkid-openproxylist-v2ray | 0.261 | 1.0 | 1 | 150 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 2000 | observe |
| Epodonios-all | 0.255 | None | 0 | 3000 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3000 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 3000 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 3741 | observe |
| barry-far-vless | 0.255 | None | 0 | 2000 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4541 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 147 |
| 204 | TimeoutError | - | 30 |
| 204 | ProxyError | - | 24 |
| cn-block | TimeoutError | - | 21 |
| geo | ClientOSError | - | 13 |
| cn-block | ClientOSError | - | 10 |
| 204 | ClientOSError | - | 8 |
| geo | TimeoutError | - | 7 |
| speed | TimeoutError | - | 7 |
| cn-block | ProxyError | - | 4 |
| geo | ProxyError | - | 4 |
| speed | ProxyError | - | 4 |
| speed | ClientPayloadError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 102 | 300 | - |
| global | False | 112 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
