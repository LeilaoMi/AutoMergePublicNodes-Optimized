# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-14 12:31:22 |
| 运行耗时 | 582.2s |
| 订阅源总数 | 107 |
| 健康订阅源 | 94 |
| 原始节点 | 84799 |
| 去重后节点 | 23007 |
| TCP 可达 | 3000 |
| 真实可用 | 447 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23007 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.8 |
| geo | 1.4 |
| tcp | 37.7 |
| probe | 209.4 |
| real_test | 241.4 |
| generate | 86.5 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 51960 |
| vmess | 12817 |
| shadowsocks | 9695 |
| trojan | 7960 |
| hysteria2 | 1522 |
| http | 638 |
| shadowsocksr | 126 |
| socks | 53 |
| tuic | 14 |
| hysteria | 11 |
| anytls | 3 |

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
| 81.52 | hysteria2 | 246.5 | 621.3 | 22.07 | 0.0 | 10.0 | 13.27 | 17.18 | Au1rxx-base64 | 107.175.219.48 |
| 79.53 | shadowsocks | 206.8 | 541.7 | 22.99 | 0.0 | 10.0 | 13.86 | 17.18 | Au1rxx-base64 | 192.3.247.109 |
| 79.25 | shadowsocks | 219.0 | 550.4 | 22.71 | 0.0 | 10.0 | 13.86 | 17.18 | Au1rxx-base64 | 108.181.118.10 |
| 78.75 | shadowsocks | 262.0 | 646.5 | 21.71 | 0.0 | 10.0 | 13.86 | 17.18 | Au1rxx-base64 | 156.146.38.167 |
| 78.28 | shadowsocks | 282.6 | 700.3 | 21.24 | 0.0 | 10.0 | 13.86 | 17.18 | Au1rxx-base64 | 156.146.38.170 |
| 78.01 | shadowsocks | 282.9 | 705.0 | 21.23 | 0.0 | 10.0 | 13.86 | 17.18 | Au1rxx-base64 | 156.146.38.168 |
| 76.35 | vless | 233.5 | 506.4 | 22.37 | 0.0 | 10.0 | 6.8 | 17.18 | Au1rxx-base64 | 150.241.102.181 |
| 76.21 | vless | 239.7 | 578.6 | 22.23 | 0.0 | 10.0 | 6.8 | 17.18 | Au1rxx-base64 | 172.235.43.210 |
| 76.02 | shadowsocks | 280.6 | 683.9 | 21.28 | 0.0 | 10.0 | 13.86 | 17.18 | Au1rxx-base64 | 23.150.248.20 |
| 75.19 | shadowsocks | 243.1 | 550.6 | 22.15 | 0.0 | 10.0 | 13.86 | 15.94 | Surfboard-tg-mixed | 5.78.51.123 |
| 74.31 | vless | 254.7 | 546.0 | 21.88 | 0.0 | 10.0 | 6.8 | 17.18 | Au1rxx-base64 | 144.172.104.26 |
| 74.06 | shadowsocks | 205.5 | 491.2 | 23.02 | 0.0 | 10.0 | 13.86 | 11.68 | mheidari-all | 108.181.0.177 |
| 73.78 | shadowsocks | 239.2 | 566.4 | 22.24 | 0.0 | 10.0 | 13.86 | 11.68 | mheidari-all | 173.244.56.6 |
| 73.72 | vless | 217.4 | 561.6 | 22.74 | 0.0 | 10.0 | 6.8 | 17.18 | Au1rxx-base64 | 192.3.247.109 |
| 72.94 | shadowsocks | 275.7 | 750.5 | 21.4 | 0.0 | 10.0 | 13.86 | 17.18 | Au1rxx-base64 | 129.146.118.11 |
| 72.63 | shadowsocks | 288.8 | 717.1 | 21.09 | 0.0 | 10.0 | 13.86 | 11.68 | mheidari-all | 156.146.38.169 |
| 72.15 | shadowsocks | 338.6 | 716.2 | 19.94 | 0.0 | 10.0 | 13.86 | 17.18 | Au1rxx-base64 | 37.19.198.160 |
| 72.04 | vless | 203.7 | 519.8 | 23.06 | 0.0 | 10.0 | 6.8 | 17.18 | Au1rxx-base64 | 38.244.20.41 |
| 71.81 | vless | 341.6 | 819.1 | 19.87 | 0.0 | 10.0 | 6.8 | 17.18 | Au1rxx-base64 | 15.204.97.216 |
| 71.69 | vless | 218.7 | 534.7 | 22.71 | 0.0 | 10.0 | 6.8 | 17.18 | Au1rxx-base64 | 38.244.20.149 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.927 | 0.863 | 299 | 1668 | prefer |
| mheidari-all | 0.844 | 0.774 | 53 | 15903 | prefer |
| Surfboard-tg-mixed | 0.793 | 0.717 | 127 | 7478 | prefer |
| ermaozi | 0.715 | 0.706 | 51 | 417 | prefer |
| ermaozi-get_subscribe | 0.617 | 0.632 | 19 | 444 | observe |
| DeltaKronecker-all | 0.515 | 0.5 | 16 | 5972 | observe |
| tg-oneclickvpnkeys | 0.26 | 1.0 | 1 | 131 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4914 | observe |
| Epodonios-all | 0.255 | None | 0 | 7910 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9127 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 6074 | observe |
| barry-far-vless | 0.255 | None | 0 | 6310 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4176 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | ClientOSError | - | 27 |
| 204 | ProxyError | - | 24 |
| cn-block | TimeoutError | - | 22 |
| speed | ClientOSError | - | 16 |
| 204 | TimeoutError | - | 9 |
| cn-block | ClientOSError | - | 8 |
| geo | TimeoutError | - | 6 |
| speed | TimeoutError | - | 4 |
| 204 | ClientOSError | - | 2 |
| cn-block | ProxyError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
