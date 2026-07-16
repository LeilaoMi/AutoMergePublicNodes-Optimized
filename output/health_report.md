# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-16 08:27:07 |
| 运行耗时 | 255.8s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 78890 |
| 去重后节点 | 24434 |
| TCP 可达 | 3000 |
| 真实可用 | 440 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 24434 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.7 |
| geo | 0.8 |
| tcp | 32.9 |
| probe | 52.5 |
| real_test | 132.7 |
| generate | 32.2 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 45657 |
| trojan | 12333 |
| vmess | 10824 |
| shadowsocks | 9496 |
| hysteria2 | 297 |
| shadowsocksr | 134 |
| http | 97 |
| socks | 38 |
| hysteria | 10 |
| tuic | 4 |

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
| 81.58 | shadowsocks | 227.1 | 626.1 | 22.52 | 0.0 | 10.0 | 13.84 | 19.22 | Au1rxx-base64 | 37.19.198.160 |
| 81.52 | shadowsocks | 229.7 | 638.0 | 22.46 | 0.0 | 10.0 | 13.84 | 19.22 | Au1rxx-base64 | 37.19.198.236 |
| 81.5 | shadowsocks | 230.5 | 640.6 | 22.44 | 0.0 | 10.0 | 13.84 | 19.22 | Au1rxx-base64 | 37.19.198.243 |
| 80.57 | shadowsocks | 249.3 | 667.3 | 22.01 | 0.0 | 10.0 | 13.84 | 19.22 | Au1rxx-base64 | 108.181.57.93 |
| 78.51 | shadowsocks | 285.9 | 661.9 | 21.16 | 0.0 | 10.0 | 13.84 | 19.22 | Au1rxx-base64 | 156.146.38.168 |
| 78.31 | shadowsocks | 279.3 | 642.1 | 21.31 | 0.0 | 10.0 | 13.84 | 19.22 | Au1rxx-base64 | 156.146.38.170 |
| 78.0 | shadowsocks | 221.0 | 589.8 | 22.66 | 0.0 | 10.0 | 13.84 | 17.9 | mheidari-all | 198.98.53.130 |
| 77.68 | shadowsocks | 272.5 | 627.7 | 21.47 | 0.0 | 10.0 | 13.84 | 19.22 | Au1rxx-base64 | 156.146.38.169 |
| 77.52 | shadowsocks | 242.0 | 657.8 | 22.18 | 0.0 | 10.0 | 13.84 | 16.0 | DeltaKronecker-all | 68.168.222.210 |
| 76.96 | trojan | 293.8 | 636.8 | 20.98 | 0.0 | 10.0 | 13.99 | 17.9 | mheidari-all | 64.94.95.118 |
| 76.87 | vmess | 309.8 | 866.9 | 20.61 | 0.0 | 10.0 | 12.86 | 17.9 | mheidari-all | 67.220.95.3 |
| 76.63 | shadowsocks | 224.8 | 615.6 | 22.57 | 0.0 | 10.0 | 13.84 | 19.22 | Au1rxx-base64 | 37.19.198.244 |
| 75.48 | vmess | 369.6 | 1029.2 | 19.22 | 0.0 | 10.0 | 12.86 | 17.9 | mheidari-all | 67.220.85.46 |
| 74.41 | shadowsocks | 331.1 | 856.0 | 20.11 | 0.0 | 10.0 | 13.84 | 19.22 | Au1rxx-base64 | 50.114.177.235 |
| 74.3 | shadowsocks | 321.7 | 575.9 | 20.33 | 0.0 | 10.0 | 13.84 | 19.22 | Au1rxx-base64 | 173.244.56.9 |
| 73.78 | shadowsocks | 371.2 | 927.6 | 19.18 | 0.0 | 10.0 | 13.84 | 16.0 | DeltaKronecker-all | 185.196.61.82 |
| 73.77 | shadowsocks | 330.4 | 604.4 | 20.13 | 0.0 | 10.0 | 13.84 | 19.22 | Au1rxx-base64 | 173.244.56.6 |
| 73.21 | trojan | 370.7 | 865.6 | 19.2 | 0.0 | 10.0 | 13.99 | 16.0 | DeltaKronecker-all | 64.94.95.115 |
| 73.16 | trojan | 368.8 | 854.9 | 19.24 | 0.0 | 10.0 | 13.99 | 16.0 | DeltaKronecker-all | 64.94.95.114 |
| 73.06 | hysteria2 | 403.9 | 833.7 | 18.43 | 0.0 | 10.0 | 12.0 | 19.22 | Au1rxx-base64 | 62.210.124.146 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.976 | 0.98 | 99 | 149 | prefer |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| mheidari-all | 0.814 | 0.738 | 122 | 16602 | prefer |
| Surfboard-tg-mixed | 0.665 | 0.59 | 39 | 5419 | observe |
| DeltaKronecker-all | 0.649 | 0.57 | 337 | 8462 | observe |
| xiaoji235-airport-v2ray-all | 0.325 | 1.0 | 1 | 1757 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4470 | observe |
| Epodonios-all | 0.255 | None | 0 | 6507 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3971 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6810 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4150 | observe |
| barry-far-vless | 0.255 | None | 0 | 4742 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5262 | observe |
| nscl5-all | 0.236 | None | 0 | 1519 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 70 |
| 204 | TimeoutError | - | 35 |
| speed | ClientOSError | - | 25 |
| cn-block | TimeoutError | - | 18 |
| 204 | ProxyError | - | 12 |
| speed | TimeoutError | - | 10 |
| geo | ClientOSError | - | 9 |
| cn-block | ClientOSError | - | 7 |
| 204 | ClientOSError | - | 6 |
| cn-block | ProxyError | - | 5 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
