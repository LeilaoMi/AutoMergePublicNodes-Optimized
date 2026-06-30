# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-06-30 14:35:10 |
| 运行耗时 | 257.5s |
| 订阅源总数 | 107 |
| 健康订阅源 | 103 |
| 原始节点 | 75035 |
| 去重后节点 | 23114 |
| TCP 可达 | 3000 |
| 真实可用 | 485 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23114 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 3.8 |
| geo | 1.4 |
| tcp | 30.7 |
| probe | 58.7 |
| real_test | 131.6 |
| generate | 31.3 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 41852 |
| trojan | 12988 |
| vmess | 10292 |
| shadowsocks | 9277 |
| hysteria2 | 275 |
| shadowsocksr | 146 |
| http | 135 |
| socks | 63 |
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
| 75.06 | shadowsocks | 234.1 | 599.0 | 22.36 | 0.0 | 10.0 | 11.62 | 15.08 | Au1rxx-base64 | 156.146.38.169 |
| 75.01 | shadowsocks | 236.1 | 607.2 | 22.31 | 0.0 | 10.0 | 11.62 | 15.08 | Au1rxx-base64 | 156.146.38.167 |
| 74.89 | shadowsocks | 241.5 | 620.6 | 22.19 | 0.0 | 10.0 | 11.62 | 15.08 | Au1rxx-base64 | 156.146.38.168 |
| 74.83 | shadowsocks | 243.8 | 630.8 | 22.13 | 0.0 | 10.0 | 11.62 | 15.08 | Au1rxx-base64 | 156.146.38.170 |
| 73.65 | vless | 234.8 | 535.2 | 22.34 | 0.0 | 10.0 | 7.82 | 14.26 | Surfboard-tg-mixed | 64.23.143.23 |
| 69.7 | shadowsocks | 301.3 | 670.5 | 20.8 | 0.0 | 10.0 | 11.62 | 15.08 | Au1rxx-base64 | 173.244.56.6 |
| 69.28 | shadowsocks | 301.9 | 632.4 | 20.79 | 0.0 | 10.0 | 11.62 | 15.08 | Au1rxx-base64 | 108.181.118.10 |
| 69.04 | shadowsocks | 287.0 | 567.1 | 21.13 | 0.0 | 10.0 | 11.62 | 15.08 | Au1rxx-base64 | 149.22.95.183 |
| 68.87 | shadowsocks | 271.9 | 549.4 | 21.48 | 0.0 | 10.0 | 11.62 | 15.08 | Au1rxx-base64 | 173.244.56.9 |
| 68.84 | vless | 319.5 | 664.3 | 20.38 | 0.0 | 10.0 | 7.82 | 14.26 | Surfboard-tg-mixed | 162.159.38.119 |
| 68.79 | shadowsocks | 322.9 | 696.9 | 20.3 | 0.0 | 10.0 | 11.62 | 15.08 | Au1rxx-base64 | 37.19.198.160 |
| 68.45 | shadowsocks | 332.0 | 728.8 | 20.09 | 0.0 | 10.0 | 11.62 | 15.08 | Au1rxx-base64 | 37.19.198.236 |
| 68.41 | shadowsocks | 327.9 | 717.4 | 20.19 | 0.0 | 10.0 | 11.62 | 15.08 | Au1rxx-base64 | 37.19.198.244 |
| 67.76 | shadowsocks | 336.9 | 742.7 | 19.98 | 0.0 | 10.0 | 11.62 | 15.08 | Au1rxx-base64 | 108.181.0.177 |
| 66.27 | shadowsocks | 327.4 | 371.3 | 20.2 | 1.07 | 9.79 | 11.62 | 15.08 | Au1rxx-base64 | 149.22.87.241 |
| 65.99 | vless | 420.2 | 921.4 | 18.05 | 0.0 | 10.0 | 7.82 | 15.08 | Au1rxx-base64 | 15.204.97.214 |
| 65.65 | shadowsocks | 330.9 | 385.5 | 20.12 | 0.55 | 9.79 | 11.62 | 15.08 | Au1rxx-base64 | 149.22.87.240 |
| 65.56 | shadowsocks | 331.6 | 385.2 | 20.1 | 0.55 | 9.79 | 11.62 | 15.08 | Au1rxx-base64 | 149.22.87.204 |
| 65.17 | hysteria2 | 451.7 | 704.4 | 17.32 | 0.0 | 9.64 | 11.25 | 15.08 | Au1rxx-base64 | 62.210.124.146 |
| 65.05 | shadowsocks | 327.3 | 657.0 | 20.2 | 0.0 | 10.0 | 11.62 | 12.4 | mheidari-all | 198.98.53.130 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| DeltaKronecker-all | 0.751 | 0.675 | 77 | 7352 | prefer |
| Surfboard-tg-mixed | 0.73 | 0.651 | 312 | 5637 | prefer |
| mheidari-all | 0.713 | 0.635 | 249 | 15693 | prefer |
| Au1rxx-base64 | 0.658 | 0.66 | 50 | 103 | observe |
| Barabama-yudou | 0.318 | 1.0 | 2 | 166 | observe |
| xiaoji235-airport-v2ray-all | 0.303 | 1.0 | 1 | 1204 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4139 | observe |
| Epodonios-all | 0.255 | None | 0 | 6322 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3977 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6506 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4204 | observe |
| barry-far-vless | 0.255 | None | 0 | 4531 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5353 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 128 |
| 204 | TimeoutError | - | 24 |
| geo | TimeoutError | - | 17 |
| 204 | ClientOSError | - | 16 |
| 204 | ProxyError | - | 13 |
| geo | ClientOSError | - | 13 |
| cn-block | TimeoutError | - | 12 |
| speed | TimeoutError | - | 11 |
| cn-block | ClientOSError | - | 5 |
| cn-block | ProxyError | - | 4 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
