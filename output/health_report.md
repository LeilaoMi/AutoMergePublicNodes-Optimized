# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-29 12:40:39 |
| 运行耗时 | 606.3s |
| 订阅源总数 | 107 |
| 健康订阅源 | 94 |
| 原始节点 | 96889 |
| 去重后节点 | 26969 |
| TCP 可达 | 3000 |
| 真实可用 | 449 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 26969 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.6 |
| geo | 1.4 |
| tcp | 45.0 |
| probe | 281.4 |
| real_test | 198.0 |
| generate | 75.8 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 59092 |
| vmess | 14821 |
| shadowsocks | 11452 |
| trojan | 9245 |
| hysteria2 | 1405 |
| http | 583 |
| shadowsocksr | 165 |
| socks | 79 |
| anytls | 24 |
| hysteria | 15 |
| tuic | 8 |

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
| 82.28 | hysteria2 | 190.3 | 512.1 | 23.37 | 0.0 | 10.0 | 12.93 | 16.98 | Au1rxx-base64 | 192.255.128.123 |
| 78.37 | shadowsocks | 250.2 | 680.0 | 21.99 | 0.0 | 10.0 | 13.4 | 16.98 | Au1rxx-base64 | 173.244.56.9 |
| 76.94 | shadowsocks | 202.0 | 492.4 | 23.1 | 0.0 | 10.0 | 13.4 | 14.94 | Surfboard-tg-mixed | 108.181.0.177 |
| 76.43 | vless | 200.6 | 523.1 | 23.13 | 0.0 | 10.0 | 6.32 | 16.98 | Au1rxx-base64 | 172.235.38.85 |
| 76.43 | vless | 200.9 | 521.0 | 23.13 | 0.0 | 10.0 | 6.32 | 16.98 | Au1rxx-base64 | 172.233.139.46 |
| 76.33 | hysteria2 | 269.3 | 233.6 | 21.54 | 6.24 | 6.81 | 12.93 | 16.98 | Au1rxx-base64 | open.2ml.bid |
| 76.18 | vless | 211.5 | 534.3 | 22.88 | 0.0 | 10.0 | 6.32 | 16.98 | Au1rxx-base64 | 195.123.240.65 |
| 75.23 | shadowsocks | 239.8 | 546.8 | 22.23 | 0.0 | 10.0 | 13.4 | 14.94 | Surfboard-tg-mixed | 5.78.51.123 |
| 75.15 | shadowsocks | 262.9 | 634.6 | 21.69 | 0.0 | 10.0 | 13.4 | 14.94 | Surfboard-tg-mixed | 156.146.38.167 |
| 74.58 | shadowsocks | 257.8 | 624.7 | 21.81 | 0.0 | 10.0 | 13.4 | 14.94 | Surfboard-tg-mixed | 156.146.38.169 |
| 72.62 | shadowsocks | 184.1 | 496.6 | 23.52 | 0.0 | 8.22 | 13.4 | 16.98 | Au1rxx-base64 | 64.110.26.99 |
| 72.56 | trojan | 209.4 | 532.7 | 22.93 | 0.0 | 8.11 | 8.04 | 16.98 | Au1rxx-base64 | 192.236.151.43 |
| 72.14 | shadowsocks | 300.0 | 337.0 | 20.83 | 2.36 | 9.89 | 13.4 | 16.98 | Au1rxx-base64 | 149.22.87.204 |
| 71.75 | vless | 244.4 | 549.9 | 22.12 | 0.0 | 8.18 | 6.32 | 16.98 | Au1rxx-base64 | 23.95.222.127 |
| 70.51 | shadowsocks | 204.1 | 536.0 | 23.05 | 0.0 | 10.0 | 13.4 | 8.06 | mheidari-all | 173.244.56.6 |
| 70.34 | hysteria2 | 461.7 | 956.3 | 17.09 | 0.0 | 10.0 | 12.93 | 16.98 | Au1rxx-base64 | 66.94.121.46 |
| 70.33 | shadowsocks | 190.2 | 511.8 | 23.37 | 0.0 | 10.0 | 13.4 | 8.06 | mheidari-all | 192.3.247.109 |
| 69.95 | http | 319.7 | 874.9 | 20.38 | 0.0 | 10.0 | 9.75 | 13.82 | ermaozi | 138.199.35.198 |
| 69.94 | vless | 223.4 | 525.7 | 22.61 | 0.0 | 8.28 | 6.32 | 16.98 | Au1rxx-base64 | 104.18.47.113 |
| 69.65 | shadowsocks | 329.4 | 673.7 | 20.15 | 0.0 | 10.0 | 13.4 | 14.94 | Surfboard-tg-mixed | 198.98.53.130 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.893 | 0.831 | 331 | 1598 | prefer |
| mheidari-all | 0.886 | 0.815 | 65 | 22883 | prefer |
| ermaozi | 0.795 | 0.8 | 35 | 291 | prefer |
| Surfboard-tg-mixed | 0.707 | 0.629 | 140 | 7053 | prefer |
| ermaozi-get_subscribe | 0.323 | 1.0 | 2 | 293 | observe |
| DeltaKronecker-all | 0.32 | 0.5 | 4 | 5528 | observe |
| roosterkid-openproxylist-v2ray | 0.261 | 1.0 | 1 | 150 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5314 | observe |
| Epodonios-all | 0.255 | None | 0 | 7502 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9548 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5690 | observe |
| barry-far-vless | 0.255 | None | 0 | 5869 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4338 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 30 |
| 204 | TimeoutError | - | 28 |
| cn-block | TimeoutError | - | 19 |
| 204 | ProxyError | - | 15 |
| speed | TimeoutError | - | 11 |
| cn-block | ClientOSError | - | 9 |
| geo | TimeoutError | - | 9 |
| geo | ClientOSError | - | 5 |
| cn-block | ProxyError | - | 3 |
| speed | ProxyError | - | 1 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
