# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-23 14:20:47 |
| 运行耗时 | 353.2s |
| 订阅源总数 | 107 |
| 健康订阅源 | 102 |
| 原始节点 | 83515 |
| 去重后节点 | 22818 |
| TCP 可达 | 3000 |
| 真实可用 | 840 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22818 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.5 |
| geo | 1.1 |
| tcp | 32.5 |
| probe | 69.2 |
| real_test | 216.3 |
| generate | 29.6 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 48322 |
| trojan | 14126 |
| shadowsocks | 10286 |
| vmess | 10138 |
| hysteria2 | 429 |
| shadowsocksr | 73 |
| socks | 57 |
| http | 50 |
| tuic | 17 |
| hysteria | 14 |
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
| 77.73 | trojan | 355.0 | 867.6 | 19.56 | 0.0 | 10.0 | 13.45 | 18.04 | DeltaKronecker-all | 64.74.163.118 |
| 76.55 | shadowsocks | 248.6 | 612.8 | 22.02 | 0.0 | 10.0 | 12.69 | 15.84 | Au1rxx-base64 | 198.98.53.130 |
| 76.5 | trojan | 304.8 | 732.9 | 20.72 | 0.0 | 10.0 | 13.45 | 15.84 | Au1rxx-base64 | 64.94.95.115 |
| 76.46 | shadowsocks | 252.5 | 619.9 | 21.93 | 0.0 | 10.0 | 12.69 | 15.84 | Au1rxx-base64 | 156.146.38.168 |
| 76.38 | shadowsocks | 256.3 | 631.3 | 21.85 | 0.0 | 10.0 | 12.69 | 15.84 | Au1rxx-base64 | 156.146.38.170 |
| 76.37 | shadowsocks | 256.4 | 632.6 | 21.84 | 0.0 | 10.0 | 12.69 | 15.84 | Au1rxx-base64 | 156.146.38.167 |
| 75.99 | shadowsocks | 272.8 | 688.0 | 21.46 | 0.0 | 10.0 | 12.69 | 15.84 | Au1rxx-base64 | 37.19.198.244 |
| 75.88 | shadowsocks | 277.5 | 677.3 | 21.35 | 0.0 | 10.0 | 12.69 | 15.84 | Au1rxx-base64 | 37.19.198.243 |
| 75.78 | trojan | 341.9 | 823.7 | 19.86 | 0.0 | 10.0 | 13.45 | 15.84 | Au1rxx-base64 | 64.94.95.118 |
| 74.85 | trojan | 355.7 | 888.5 | 19.54 | 0.0 | 10.0 | 13.45 | 15.84 | Au1rxx-base64 | 64.94.95.117 |
| 73.39 | trojan | 510.4 | 1362.9 | 15.96 | 0.0 | 10.0 | 13.45 | 18.04 | DeltaKronecker-all | 153.75.250.171 |
| 72.22 | shadowsocks | 369.1 | 936.9 | 19.23 | 0.0 | 10.0 | 12.69 | 15.84 | Au1rxx-base64 | 68.168.222.210 |
| 71.45 | vmess | 373.4 | 1010.3 | 19.13 | 0.0 | 10.0 | 10.0 | 16.82 | Surfboard-tg-mixed | 67.220.95.3 |
| 71.32 | shadowsocks | 258.7 | 636.0 | 21.79 | 0.0 | 10.0 | 12.69 | 15.84 | Au1rxx-base64 | 156.146.38.169 |
| 70.97 | shadowsocks | 298.4 | 614.8 | 20.87 | 0.0 | 10.0 | 12.69 | 15.84 | Au1rxx-base64 | 149.22.95.183 |
| 70.73 | shadowsocks | 297.9 | 566.2 | 20.88 | 0.0 | 10.0 | 12.69 | 15.84 | Au1rxx-base64 | 173.244.56.9 |
| 70.5 | shadowsocks | 323.5 | 712.1 | 20.29 | 0.0 | 10.0 | 12.69 | 15.84 | Au1rxx-base64 | 108.181.57.93 |
| 69.68 | trojan | 377.5 | 681.0 | 19.04 | 0.0 | 10.0 | 13.45 | 15.84 | Au1rxx-base64 | 35.95.97.145 |
| 69.59 | trojan | 376.7 | 669.3 | 19.06 | 0.0 | 10.0 | 13.45 | 15.84 | Au1rxx-base64 | 44.243.31.46 |
| 69.57 | shadowsocks | 337.9 | 688.3 | 19.96 | 0.0 | 10.0 | 12.69 | 15.84 | Au1rxx-base64 | 108.181.0.177 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.976 | 1.0 | 36 | 61 | prefer |
| mheidari-all | 0.928 | 0.85 | 353 | 19424 | prefer |
| Surfboard-tg-mixed | 0.793 | 0.718 | 85 | 5390 | prefer |
| Au1rxx-base64 | 0.79 | 0.776 | 196 | 432 | prefer |
| DeltaKronecker-all | 0.586 | 0.506 | 569 | 5572 | observe |
| xiaoji235-airport-v2ray-all | 0.391 | 1.0 | 2 | 4399 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4757 | observe |
| Epodonios-all | 0.255 | None | 0 | 6487 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3971 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7332 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4196 | observe |
| barry-far-vless | 0.255 | None | 0 | 4823 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4954 | observe |
| nscl5-all | 0.255 | None | 0 | 2435 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 104 |
| geo | TimeoutError | - | 80 |
| cn-block | TimeoutError | - | 69 |
| geo | ClientOSError | - | 43 |
| 204 | ProxyError | - | 40 |
| 204 | TimeoutError | - | 28 |
| speed | TimeoutError | - | 12 |
| cn-block | ProxyError | - | 10 |
| cn-block | ClientOSError | - | 7 |
| 204 | ClientOSError | - | 6 |
| geo | ProxyError | - | 4 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
