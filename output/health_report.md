# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-14 17:00:51 |
| 运行耗时 | 325.2s |
| 订阅源总数 | 107 |
| 健康订阅源 | 93 |
| 原始节点 | 98394 |
| 去重后节点 | 27341 |
| TCP 可达 | 3000 |
| 真实可用 | 63 |
| Verified 输出 | 63 |
| Global 输出 | 73 |
| All 输出 | 27341 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.9 |
| geo | 1.5 |
| tcp | 89.7 |
| probe | 107.7 |
| real_test | 70.5 |
| china_check | 34.6 |
| write_verified | 0.0 |
| generate | 13.3 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 58412 |
| vmess | 16290 |
| shadowsocks | 11771 |
| trojan | 9942 |
| hysteria2 | 1289 |
| http | 410 |
| shadowsocksr | 166 |
| socks | 65 |
| anytls | 25 |
| hysteria | 18 |
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
| 76.51 | hysteria2 | 290.2 | 723.2 | 21.06 | 0.0 | 9.76 | 10.91 | 16.28 | Au1rxx-base64 | 129.213.91.185 |
| 74.03 | vless | 301.1 | 697.4 | 20.81 | 0.0 | 9.38 | 9.14 | 16.28 | Au1rxx-base64 | 45.32.69.110 |
| 73.92 | hysteria2 | 295.9 | 599.6 | 20.93 | 0.0 | 9.55 | 10.91 | 16.28 | Au1rxx-base64 | 66.94.121.46 |
| 72.54 | shadowsocks | 291.7 | 609.4 | 21.02 | 0.0 | 10.0 | 13.04 | 16.28 | Au1rxx-base64 | 173.244.56.9 |
| 72.5 | shadowsocks | 329.4 | 760.2 | 20.15 | 0.0 | 10.0 | 13.04 | 16.28 | Au1rxx-base64 | 37.19.198.244 |
| 72.18 | shadowsocks | 327.6 | 769.8 | 20.19 | 0.0 | 10.0 | 13.04 | 16.28 | Au1rxx-base64 | 37.19.198.236 |
| 72.15 | shadowsocks | 230.5 | 607.3 | 22.44 | 0.0 | 9.39 | 13.04 | 16.28 | Au1rxx-base64 | 156.146.38.168 |
| 70.63 | vless | 371.9 | 841.4 | 19.17 | 0.0 | 9.28 | 9.14 | 16.28 | Au1rxx-base64 | 154.29.145.196 |
| 70.58 | shadowsocks | 329.7 | 759.5 | 20.15 | 0.0 | 9.69 | 13.04 | 16.28 | Au1rxx-base64 | 37.19.198.160 |
| 69.66 | shadowsocks | 353.7 | 697.7 | 19.59 | 0.0 | 10.0 | 13.04 | 16.28 | Au1rxx-base64 | 140.82.63.79 |
| 69.31 | shadowsocks | 405.4 | 977.5 | 18.39 | 0.0 | 10.0 | 13.04 | 16.28 | Au1rxx-base64 | 15.204.233.41 |
| 68.82 | shadowsocks | 338.5 | 662.8 | 19.94 | 0.0 | 10.0 | 13.04 | 16.28 | Au1rxx-base64 | 149.22.95.183 |
| 67.12 | shadowsocks | 229.0 | 613.2 | 22.48 | 0.0 | 0.0 | 13.04 | 15.6 | mheidari-all | 156.146.38.170 |
| 66.54 | vless | 258.1 | 628.5 | 21.8 | 0.0 | 0.0 | 9.14 | 15.6 | mheidari-all | 216.227.161.95 |
| 65.17 | shadowsocks | 517.2 | 1064.6 | 15.81 | 0.0 | 10.0 | 13.04 | 16.28 | Au1rxx-base64 | 51.222.200.165 |
| 64.47 | vless | 393.7 | 879.4 | 18.66 | 0.0 | 4.46 | 9.14 | 16.28 | Au1rxx-base64 | 193.233.202.250 |
| 64.16 | vless | 277.0 | 569.0 | 21.36 | 0.0 | 0.93 | 9.14 | 16.28 | Au1rxx-base64 | 47.251.108.158 |
| 63.79 | shadowsocks | 280.9 | 628.6 | 21.28 | 0.0 | 1.25 | 13.04 | 16.28 | Au1rxx-base64 | 173.244.56.6 |
| 63.56 | shadowsocks | 323.6 | 762.6 | 20.29 | 0.0 | 1.12 | 13.04 | 16.28 | Au1rxx-base64 | 37.19.198.243 |
| 62.98 | vless | 362.0 | 758.9 | 19.4 | 0.0 | 7.64 | 9.14 | 16.28 | Au1rxx-base64 | 69.48.201.136 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.915 | 0.95 | 20 | 144 | prefer |
| mheidari-all | 0.788 | 0.714 | 70 | 23968 | prefer |
| Au1rxx-base64 | 0.766 | 0.697 | 185 | 1780 | prefer |
| Surfboard-tg-mixed | 0.695 | 0.62 | 50 | 7210 | observe |
| ermaozi-get_subscribe | 0.57 | 1.0 | 8 | 515 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5125 | observe |
| DeltaKronecker-all | 0.255 | None | 0 | 4803 | observe |
| Epodonios-all | 0.255 | None | 0 | 7543 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9997 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5726 | observe |
| barry-far-vless | 0.255 | None | 0 | 5831 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4216 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 59 |
| geo | ClientOSError | - | 9 |
| speed | ClientOSError | - | 8 |
| cn-block | TimeoutError | - | 7 |
| 204 | TimeoutError | - | 4 |
| cn-block | ClientOSError | - | 4 |
| cn-block | ProxyError | - | 3 |
| 204 | ClientOSError | - | 2 |
| 204 | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 66 | 63 | - |
| global | False | 72 | 73 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
