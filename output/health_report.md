# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-16 21:16:32 |
| 运行耗时 | 556.3s |
| 订阅源总数 | 107 |
| 健康订阅源 | 96 |
| 原始节点 | 89335 |
| 去重后节点 | 24603 |
| TCP 可达 | 3000 |
| 真实可用 | 377 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 24603 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.1 |
| geo | 1.5 |
| tcp | 41.1 |
| probe | 215.5 |
| real_test | 206.3 |
| generate | 84.8 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 52838 |
| vmess | 14367 |
| shadowsocks | 10782 |
| trojan | 9065 |
| hysteria2 | 1477 |
| http | 592 |
| shadowsocksr | 129 |
| socks | 73 |
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
| 81.3 | hysteria2 | 173.6 | 465.4 | 23.76 | 0.0 | 10.0 | 11.88 | 16.66 | mheidari-all | 45.149.172.74 |
| 80.43 | vless | 199.6 | 482.1 | 23.16 | 0.0 | 10.0 | 9.87 | 17.4 | Au1rxx-base64 | 45.149.172.74 |
| 80.18 | vless | 210.3 | 526.1 | 22.91 | 0.0 | 10.0 | 9.87 | 17.4 | Au1rxx-base64 | 172.235.43.210 |
| 80.1 | vless | 213.8 | 597.2 | 22.83 | 0.0 | 10.0 | 9.87 | 17.4 | Au1rxx-base64 | 198.200.42.129 |
| 79.33 | http | 193.6 | 497.0 | 23.3 | 0.0 | 10.0 | 12.19 | 16.84 | ermaozi | 138.199.35.213 |
| 79.1 | vless | 247.3 | 522.6 | 22.05 | 0.0 | 10.0 | 9.87 | 17.4 | Au1rxx-base64 | 150.241.102.181 |
| 78.96 | shadowsocks | 210.0 | 532.9 | 22.92 | 0.0 | 10.0 | 13.14 | 17.4 | Au1rxx-base64 | 5.78.51.123 |
| 78.95 | shadowsocks | 231.7 | 546.0 | 22.41 | 0.0 | 10.0 | 13.14 | 17.4 | Au1rxx-base64 | 149.22.95.183 |
| 78.5 | hysteria2 | 192.0 | 491.0 | 23.33 | 0.0 | 10.0 | 11.88 | 16.66 | mheidari-all | 45.149.172.80 |
| 78.47 | vless | 190.2 | 493.0 | 23.38 | 0.0 | 10.0 | 9.87 | 15.22 | DeltaKronecker-all | 47.251.108.158 |
| 78.21 | shadowsocks | 231.9 | 554.6 | 22.41 | 0.0 | 10.0 | 13.14 | 16.66 | mheidari-all | 173.244.56.6 |
| 78.04 | shadowsocks | 217.8 | 529.1 | 22.74 | 0.0 | 10.0 | 13.14 | 16.66 | mheidari-all | 108.181.118.10 |
| 77.77 | vless | 184.9 | 485.7 | 23.5 | 0.0 | 10.0 | 9.87 | 17.4 | Au1rxx-base64 | 45.149.172.80 |
| 77.63 | vless | 320.2 | 825.8 | 20.36 | 0.0 | 10.0 | 9.87 | 17.4 | Au1rxx-base64 | 15.204.97.216 |
| 77.33 | http | 206.3 | 510.6 | 23.0 | 0.0 | 10.0 | 12.19 | 16.84 | ermaozi | 138.199.35.198 |
| 77.15 | trojan | 177.0 | 470.4 | 23.68 | 0.0 | 10.0 | 8.57 | 17.4 | Au1rxx-base64 | 100.42.228.109 |
| 77.12 | vless | 253.2 | 520.9 | 21.92 | 0.0 | 10.0 | 9.87 | 17.4 | Au1rxx-base64 | 144.172.104.26 |
| 76.88 | shadowsocks | 289.2 | 676.6 | 21.08 | 0.0 | 10.0 | 13.14 | 16.66 | mheidari-all | 173.244.56.9 |
| 75.03 | vless | 216.9 | 522.9 | 22.76 | 0.0 | 10.0 | 9.87 | 17.4 | Au1rxx-base64 | 31.58.50.200 |
| 74.05 | shadowsocks | 287.7 | 649.2 | 21.12 | 0.0 | 10.0 | 13.14 | 17.4 | Au1rxx-base64 | 156.146.38.169 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| mheidari-all | 0.904 | 0.833 | 72 | 17985 | prefer |
| Au1rxx-base64 | 0.89 | 0.827 | 254 | 1651 | prefer |
| DeltaKronecker-all | 0.82 | 0.745 | 102 | 6081 | prefer |
| ermaozi | 0.781 | 0.786 | 28 | 353 | prefer |
| Surfboard-tg-mixed | 0.519 | 1.0 | 5 | 7483 | observe |
| tg-oneclickvpnkeys | 0.364 | 1.0 | 3 | 140 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5115 | observe |
| Epodonios-all | 0.255 | None | 0 | 7934 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 8999 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5919 | observe |
| barry-far-vless | 0.255 | None | 0 | 6197 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 2484 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.241 | None | 0 | 1651 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | ClientOSError | - | 15 |
| cn-block | TimeoutError | - | 15 |
| 204 | TimeoutError | - | 13 |
| 204 | ProxyError | - | 12 |
| geo | TimeoutError | - | 10 |
| speed | ClientOSError | - | 9 |
| speed | TimeoutError | - | 9 |
| 204 | ProxyConnectionError | - | 5 |
| cn-block | ProxyError | - | 2 |
| 204 | ClientOSError | - | 2 |
| cn-block | ClientOSError | - | 1 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
