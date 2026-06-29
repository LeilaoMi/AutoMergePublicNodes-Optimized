# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-06-29 04:31:37 |
| 运行耗时 | 255.3s |
| 订阅源总数 | 107 |
| 健康订阅源 | 105 |
| 原始节点 | 75950 |
| 去重后节点 | 22966 |
| TCP 可达 | 3000 |
| 真实可用 | 660 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22966 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.3 |
| geo | 1.4 |
| tcp | 30.6 |
| probe | 54.1 |
| real_test | 140.1 |
| generate | 24.8 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 42540 |
| trojan | 12490 |
| vmess | 10958 |
| shadowsocks | 9395 |
| hysteria2 | 223 |
| shadowsocksr | 157 |
| http | 136 |
| socks | 44 |
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
| 79.23 | vless | 270.7 | 743.5 | 21.51 | 0.0 | 10.0 | 10.84 | 16.88 | mheidari-all | 47.253.226.114 |
| 77.38 | shadowsocks | 230.3 | 608.4 | 22.45 | 0.0 | 10.0 | 12.05 | 16.88 | mheidari-all | 198.98.53.130 |
| 77.1 | vless | 297.5 | 720.7 | 20.89 | 0.0 | 10.0 | 10.84 | 16.88 | mheidari-all | 162.159.18.241 |
| 76.77 | shadowsocks | 236.7 | 636.6 | 22.3 | 0.0 | 10.0 | 12.05 | 16.42 | Au1rxx-base64 | 37.19.198.243 |
| 76.69 | shadowsocks | 240.1 | 646.5 | 22.22 | 0.0 | 10.0 | 12.05 | 16.42 | Au1rxx-base64 | 37.19.198.244 |
| 76.67 | shadowsocks | 241.2 | 652.0 | 22.2 | 0.0 | 10.0 | 12.05 | 16.42 | Au1rxx-base64 | 37.19.198.236 |
| 76.57 | vless | 342.7 | 648.4 | 19.85 | 0.0 | 10.0 | 10.84 | 16.88 | mheidari-all | 173.245.59.35 |
| 76.31 | shadowsocks | 255.0 | 668.1 | 21.88 | 0.0 | 10.0 | 12.05 | 16.88 | mheidari-all | 108.181.57.93 |
| 75.24 | shadowsocks | 302.7 | 818.8 | 20.77 | 0.0 | 10.0 | 12.05 | 16.42 | Au1rxx-base64 | tinkered-pennies-puppies.freesocks.work |
| 74.56 | vless | 319.7 | 856.0 | 20.38 | 0.0 | 10.0 | 10.84 | 14.34 | Surfboard-tg-mixed | 137.184.218.169 |
| 74.39 | vless | 272.3 | 664.7 | 21.47 | 0.0 | 10.0 | 10.84 | 13.08 | DeltaKronecker-all | 104.25.161.29 |
| 74.37 | vless | 273.4 | 674.0 | 21.45 | 0.0 | 10.0 | 10.84 | 13.08 | DeltaKronecker-all | 162.159.252.15 |
| 73.99 | vless | 275.8 | 676.1 | 21.39 | 0.0 | 10.0 | 10.84 | 13.08 | DeltaKronecker-all | 104.17.90.246 |
| 73.63 | shadowsocks | 281.4 | 646.9 | 21.26 | 0.0 | 10.0 | 12.05 | 16.42 | Au1rxx-base64 | 156.146.38.169 |
| 73.51 | vless | 271.4 | 652.5 | 21.49 | 0.0 | 10.0 | 10.84 | 13.08 | DeltaKronecker-all | 198.41.209.87 |
| 73.5 | shadowsocks | 282.3 | 659.1 | 21.24 | 0.0 | 10.0 | 12.05 | 16.42 | Au1rxx-base64 | 156.146.38.168 |
| 73.47 | shadowsocks | 276.8 | 639.3 | 21.37 | 0.0 | 10.0 | 12.05 | 16.42 | Au1rxx-base64 | 156.146.38.167 |
| 72.83 | shadowsocks | 321.3 | 767.5 | 20.34 | 0.0 | 10.0 | 12.05 | 16.42 | Au1rxx-base64 | 156.146.38.170 |
| 72.68 | vless | 271.2 | 661.3 | 21.5 | 0.0 | 10.0 | 10.84 | 13.08 | DeltaKronecker-all | 104.19.142.226 |
| 71.21 | vless | 271.6 | 667.4 | 21.49 | 0.0 | 10.0 | 10.84 | 13.08 | DeltaKronecker-all | 104.17.238.33 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| mheidari-all | 0.92 | 0.842 | 367 | 16006 | prefer |
| Surfboard-tg-mixed | 0.796 | 0.718 | 262 | 5165 | prefer |
| Au1rxx-base64 | 0.655 | 0.659 | 41 | 86 | observe |
| DeltaKronecker-all | 0.413 | 0.332 | 292 | 6788 | observe |
| nscl5-all | 0.358 | 1.0 | 2 | 1166 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4327 | observe |
| Epodonios-all | 0.255 | None | 0 | 7662 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6991 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 3804 | observe |
| barry-far-vless | 0.255 | None | 0 | 4390 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5325 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 134 |
| speed | ClientOSError | - | 112 |
| geo | ClientOSError | - | 47 |
| speed | TimeoutError | - | 15 |
| cn-block | TimeoutError | - | 15 |
| 204 | ProxyError | - | 7 |
| 204 | ClientOSError | - | 4 |
| cn-block | ClientOSError | - | 3 |
| 204 | TimeoutError | - | 3 |
| cn-block | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
