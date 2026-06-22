# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-06-22 20:59:59 |
| 运行耗时 | 274.4s |
| 订阅源总数 | 107 |
| 健康订阅源 | 105 |
| 原始节点 | 78026 |
| 去重后节点 | 22898 |
| TCP 可达 | 3000 |
| 真实可用 | 723 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22898 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.6 |
| geo | 1.3 |
| tcp | 31.2 |
| probe | 58.1 |
| real_test | 147.7 |
| generate | 30.6 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 47027 |
| trojan | 10535 |
| vmess | 10018 |
| shadowsocks | 9782 |
| hysteria2 | 264 |
| http | 170 |
| shadowsocksr | 166 |
| socks | 56 |
| hysteria | 6 |
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
| 82.44 | vless | 266.3 | 758.4 | 21.61 | 0.0 | 10.0 | 12.41 | 18.42 | mheidari-all | 47.253.226.114 |
| 80.05 | shadowsocks | 224.7 | 621.4 | 22.58 | 0.0 | 10.0 | 13.27 | 18.2 | Au1rxx-base64 | 37.19.198.236 |
| 79.97 | shadowsocks | 228.2 | 631.5 | 22.5 | 0.0 | 10.0 | 13.27 | 18.2 | Au1rxx-base64 | 37.19.198.160 |
| 79.87 | shadowsocks | 232.4 | 582.2 | 22.4 | 0.0 | 10.0 | 13.27 | 18.2 | Au1rxx-base64 | 198.98.53.130 |
| 78.86 | shadowsocks | 275.8 | 775.3 | 21.39 | 0.0 | 10.0 | 13.27 | 18.2 | Au1rxx-base64 | 37.19.198.244 |
| 78.78 | shadowsocks | 279.5 | 785.5 | 21.31 | 0.0 | 10.0 | 13.27 | 18.2 | Au1rxx-base64 | 37.19.198.243 |
| 76.85 | vless | 366.4 | 893.8 | 19.3 | 0.0 | 10.0 | 12.41 | 18.2 | Au1rxx-base64 | 15.223.121.250 |
| 76.51 | shadowsocks | 279.6 | 632.0 | 21.3 | 0.0 | 10.0 | 13.27 | 18.2 | Au1rxx-base64 | 156.146.38.170 |
| 75.46 | shadowsocks | 290.0 | 666.5 | 21.06 | 0.0 | 10.0 | 13.27 | 18.2 | Au1rxx-base64 | 156.146.38.169 |
| 74.88 | shadowsocks | 282.9 | 655.7 | 21.23 | 0.0 | 10.0 | 13.27 | 18.2 | Au1rxx-base64 | 156.146.38.168 |
| 74.68 | vless | 301.2 | 785.4 | 20.81 | 0.0 | 10.0 | 12.41 | 13.46 | DeltaKronecker-all | 152.53.171.40 |
| 74.59 | shadowsocks | 290.6 | 805.1 | 21.05 | 0.0 | 10.0 | 13.27 | 18.2 | Au1rxx-base64 | tinkered-pennies-puppies.freesocks.work |
| 74.58 | vless | 365.3 | 928.5 | 19.32 | 0.0 | 10.0 | 12.41 | 18.42 | mheidari-all | 185.156.47.96 |
| 74.32 | shadowsocks | 245.9 | 666.2 | 22.09 | 0.0 | 10.0 | 13.27 | 13.46 | DeltaKronecker-all | 108.181.57.93 |
| 73.25 | shadowsocks | 232.0 | 628.4 | 22.41 | 0.0 | 10.0 | 13.27 | 18.2 | Au1rxx-base64 | 147.90.234.133 |
| 72.71 | vless | 384.2 | 926.6 | 18.88 | 0.0 | 10.0 | 12.41 | 13.46 | DeltaKronecker-all | 193.233.202.7 |
| 72.22 | hysteria2 | 374.1 | 686.8 | 19.12 | 0.0 | 9.99 | 12.0 | 18.2 | Au1rxx-base64 | 62.210.124.146 |
| 72.04 | vless | 285.5 | 767.6 | 21.17 | 0.0 | 10.0 | 12.41 | 13.46 | DeltaKronecker-all | 162.217.248.229 |
| 71.69 | shadowsocks | 321.2 | 606.0 | 20.34 | 0.0 | 10.0 | 13.27 | 18.2 | Au1rxx-base64 | 173.244.56.9 |
| 71.41 | shadowsocks | 351.7 | 557.3 | 19.64 | 0.0 | 10.0 | 13.27 | 18.2 | Au1rxx-base64 | 173.244.56.6 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.987 | 1.0 | 58 | 95 | prefer |
| mheidari-all | 0.919 | 0.841 | 345 | 15541 | prefer |
| Au1rxx-base64 | 0.862 | 0.863 | 102 | 150 | prefer |
| DeltaKronecker-all | 0.762 | 0.683 | 413 | 7452 | prefer |
| Surfboard-tg-mixed | 0.4 | 0.75 | 4 | 5285 | observe |
| Barabama-yudou | 0.318 | 1.0 | 2 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4466 | observe |
| Epodonios-all | 0.255 | None | 0 | 8275 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3980 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7495 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4112 | observe |
| barry-far-vless | 0.255 | None | 0 | 5141 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4547 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| nscl5-all | 0.23 | None | 0 | 1364 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 85 |
| 204 | TimeoutError | - | 32 |
| cn-block | TimeoutError | - | 18 |
| geo | ClientOSError | - | 12 |
| geo | TimeoutError | - | 11 |
| speed | TimeoutError | - | 11 |
| 204 | ProxyError | - | 9 |
| 204 | ClientOSError | - | 7 |
| geo | ProxyError | - | 4 |
| cn-block | ClientOSError | - | 4 |
| cn-block | ProxyError | - | 4 |
| speed | ProxyError | - | 4 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
