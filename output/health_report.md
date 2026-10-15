# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-15 16:47:13 |
| 运行耗时 | 322.4s |
| 订阅源总数 | 107 |
| 健康订阅源 | 93 |
| 原始节点 | 100051 |
| 去重后节点 | 27919 |
| TCP 可达 | 3000 |
| 真实可用 | 89 |
| Verified 输出 | 89 |
| Global 输出 | 94 |
| All 输出 | 27919 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.8 |
| geo | 1.5 |
| tcp | 84.3 |
| probe | 113.3 |
| real_test | 72.7 |
| china_check | 28.7 |
| write_verified | 0.0 |
| generate | 14.2 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 59032 |
| vmess | 16500 |
| shadowsocks | 12001 |
| trojan | 10372 |
| hysteria2 | 1209 |
| http | 660 |
| shadowsocksr | 170 |
| socks | 57 |
| anytls | 27 |
| hysteria | 17 |
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
| 74.73 | vless | 269.8 | 562.6 | 21.53 | 0.0 | 10.0 | 9.47 | 16.42 | Au1rxx-base64 | 216.227.161.95 |
| 74.56 | shadowsocks | 274.2 | 527.3 | 21.43 | 0.0 | 10.0 | 12.74 | 16.42 | Au1rxx-base64 | 173.244.56.6 |
| 74.35 | http | 170.6 | 460.6 | 23.83 | 0.0 | 0.0 | 13.9 | 19.12 | ermaozi | fan.365747.xyz |
| 73.75 | http | 196.5 | 549.4 | 23.23 | 0.0 | 0.0 | 13.9 | 19.12 | ermaozi | voteshirleysew.club |
| 73.15 | shadowsocks | 292.3 | 653.6 | 21.01 | 0.0 | 10.0 | 12.74 | 16.42 | Au1rxx-base64 | 156.146.38.170 |
| 73.14 | shadowsocks | 269.0 | 503.6 | 21.55 | 0.0 | 10.0 | 12.74 | 16.42 | Au1rxx-base64 | 173.244.56.9 |
| 72.73 | shadowsocks | 203.6 | 548.0 | 23.07 | 0.0 | 10.0 | 12.74 | 16.42 | Au1rxx-base64 | 64.110.25.6 |
| 72.49 | shadowsocks | 291.5 | 658.6 | 21.03 | 0.0 | 10.0 | 12.74 | 16.42 | Au1rxx-base64 | 156.146.38.168 |
| 72.22 | vless | 210.3 | 545.2 | 22.91 | 0.0 | 8.42 | 9.47 | 16.42 | Au1rxx-base64 | 154.29.159.211 |
| 71.95 | http | 187.7 | 496.0 | 23.43 | 0.0 | 0.0 | 13.9 | 19.12 | ermaozi | 167.88.60.242 |
| 71.09 | http | 203.2 | 511.3 | 23.07 | 0.0 | 0.0 | 13.9 | 19.12 | ermaozi | 38.95.111.226 |
| 70.91 | shadowsocks | 294.9 | 663.2 | 20.95 | 0.0 | 10.0 | 12.74 | 16.42 | Au1rxx-base64 | 156.146.38.167 |
| 70.84 | shadowsocks | 298.3 | 474.7 | 20.87 | 0.0 | 10.0 | 12.74 | 16.42 | Au1rxx-base64 | 103.11.76.248 |
| 70.66 | http | 221.9 | 508.5 | 22.64 | 0.0 | 0.0 | 13.9 | 19.12 | ermaozi | 138.199.35.216 |
| 68.09 | shadowsocks | 373.4 | 896.6 | 19.14 | 0.0 | 10.0 | 12.74 | 16.42 | Au1rxx-base64 | 156.146.38.169 |
| 68.04 | shadowsocks | 386.2 | 811.5 | 18.84 | 0.0 | 10.0 | 12.74 | 16.42 | Au1rxx-base64 | 37.19.198.244 |
| 66.4 | vless | 347.8 | 686.1 | 19.73 | 0.0 | 6.22 | 9.47 | 16.42 | Au1rxx-base64 | 195.211.98.43 |
| 65.07 | hysteria2 | 304.1 | 694.2 | 20.74 | 0.0 | 0.0 | 10.91 | 16.42 | Au1rxx-base64 | starlink-ft.251313.xyz |
| 64.74 | vless | 169.6 | 463.5 | 23.85 | 0.0 | 0.0 | 9.47 | 16.42 | Au1rxx-base64 | 47.251.25.74 |
| 64.68 | vless | 382.6 | 739.5 | 18.92 | 0.0 | 10.0 | 9.47 | 16.42 | Au1rxx-base64 | 69.48.201.136 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.984 | 0.971 | 69 | 659 | prefer |
| Au1rxx-base64 | 0.709 | 0.64 | 308 | 1767 | prefer |
| mheidari-all | 0.633 | 0.714 | 14 | 24080 | observe |
| Surfboard-tg-mixed | 0.391 | 1.0 | 2 | 7281 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5089 | observe |
| DeltaKronecker-all | 0.255 | None | 0 | 5147 | observe |
| Epodonios-all | 0.255 | None | 0 | 7794 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 10074 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5707 | observe |
| barry-far-vless | 0.255 | None | 0 | 5961 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4338 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 80 |
| speed | ClientOSError | - | 11 |
| 204 | ProxyError | - | 7 |
| 204 | TimeoutError | - | 5 |
| cn-block | ProxyError | - | 3 |
| cn-block | ClientOSError | - | 3 |
| 204 | ClientOSError | - | 2 |
| geo | ClientOSError | - | 2 |
| geo | ProxyError | - | 2 |
| cn-block | TimeoutError | - | 2 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 100 | 89 | - |
| global | False | 104 | 94 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
