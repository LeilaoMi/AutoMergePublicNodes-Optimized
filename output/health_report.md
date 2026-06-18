# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.9.1 |
| 更新时间 | 2026-06-18 10:45:19 |
| 运行耗时 | 366.8s |
| 订阅源总数 | 107 |
| 健康订阅源 | 107 |
| 原始节点 | 70128 |
| 去重后节点 | 21724 |
| TCP 可达 | 690 |
| 真实可用 | 543 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 21724 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 3.3 |
| geo | 1.2 |
| tcp | 59.6 |
| probe | 104.8 |
| real_test | 169.2 |
| generate | 28.8 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 38824 |
| trojan | 10973 |
| shadowsocks | 10361 |
| vmess | 9432 |
| hysteria2 | 225 |
| shadowsocksr | 153 |
| http | 107 |
| socks | 45 |
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
| 77.79 | shadowsocks | 248.9 | 610.0 | 22.02 | 0.0 | 10.0 | 14.55 | 17.32 | Au1rxx-base64 | 156.146.38.169 |
| 77.54 | shadowsocks | 253.3 | 625.4 | 21.91 | 0.0 | 10.0 | 14.55 | 17.32 | Au1rxx-base64 | 156.146.38.167 |
| 77.44 | shadowsocks | 263.7 | 660.8 | 21.67 | 0.0 | 10.0 | 14.55 | 17.32 | Au1rxx-base64 | 37.19.198.160 |
| 77.36 | shadowsocks | 267.5 | 657.9 | 21.59 | 0.0 | 10.0 | 14.55 | 17.32 | Au1rxx-base64 | 37.19.198.236 |
| 77.35 | shadowsocks | 259.1 | 651.7 | 21.78 | 0.0 | 10.0 | 14.55 | 17.12 | mheidari-all | 198.98.53.130 |
| 77.18 | shadowsocks | 256.0 | 625.9 | 21.85 | 0.0 | 10.0 | 14.55 | 17.32 | Au1rxx-base64 | 156.146.38.170 |
| 76.8 | shadowsocks | 291.3 | 723.9 | 21.03 | 0.0 | 10.0 | 14.55 | 17.32 | Au1rxx-base64 | 149.28.255.6 |
| 76.27 | shadowsocks | 314.5 | 811.2 | 20.5 | 0.0 | 10.0 | 14.55 | 17.32 | Au1rxx-base64 | 37.19.198.244 |
| 75.9 | shadowsocks | 287.2 | 729.8 | 21.13 | 0.0 | 10.0 | 14.55 | 17.32 | Au1rxx-base64 | 156.146.38.168 |
| 73.72 | vless | 328.7 | 905.4 | 20.17 | 0.0 | 10.0 | 11.13 | 17.12 | mheidari-all | 185.156.47.96 |
| 73.59 | vmess | 330.5 | 849.4 | 20.13 | 0.0 | 10.0 | 12.86 | 19.7 | Surfboard-tg-mixed | 67.220.85.46 |
| 72.32 | shadowsocks | 285.9 | 568.0 | 21.16 | 0.0 | 10.0 | 14.55 | 17.32 | Au1rxx-base64 | 173.244.56.9 |
| 71.36 | shadowsocks | 286.1 | 685.9 | 21.15 | 0.0 | 10.0 | 14.55 | 12.16 | DeltaKronecker-all | 108.181.57.93 |
| 71.23 | shadowsocks | 325.2 | 687.7 | 20.25 | 0.0 | 10.0 | 14.55 | 17.32 | Au1rxx-base64 | 173.244.56.6 |
| 70.44 | shadowsocks | 318.3 | 623.0 | 20.41 | 0.0 | 10.0 | 14.55 | 17.32 | Au1rxx-base64 | 149.22.95.183 |
| 70.06 | vless | 415.3 | 915.1 | 18.16 | 0.0 | 10.0 | 11.13 | 17.32 | Au1rxx-base64 | 15.204.97.214 |
| 68.32 | vless | 427.4 | 454.4 | 17.88 | 0.0 | 9.63 | 11.13 | 19.7 | Surfboard-tg-mixed | 31.76.91.26 |
| 68.08 | vless | 436.4 | 456.4 | 17.68 | 0.0 | 9.61 | 11.13 | 19.7 | Surfboard-tg-mixed | 31.76.91.24 |
| 67.51 | vless | 502.5 | 843.2 | 16.15 | 0.0 | 9.99 | 11.13 | 19.7 | Surfboard-tg-mixed | 89.23.107.137 |
| 67.44 | trojan | 349.8 | 507.6 | 19.68 | 0.0 | 10.0 | 12.48 | 19.7 | Surfboard-tg-mixed | 104.19.199.34 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.966 | 1.0 | 25 | 73 | prefer |
| Surfboard-tg-mixed | 0.894 | 0.816 | 326 | 4615 | prefer |
| Au1rxx-base64 | 0.887 | 0.897 | 58 | 96 | prefer |
| mheidari-all | 0.816 | 0.738 | 225 | 14164 | prefer |
| DeltaKronecker-all | 0.673 | 0.596 | 52 | 7112 | observe |
| Barabama-yudou | 0.318 | 1.0 | 2 | 166 | observe |
| nscl5-all | 0.297 | 1.0 | 1 | 1044 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4494 | observe |
| Epodonios-all | 0.255 | None | 0 | 6424 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3985 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6163 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 3599 | observe |
| barry-far-vless | 0.255 | None | 0 | 4217 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4615 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | TimeoutError | - | 37 |
| speed | ClientOSError | - | 31 |
| cn-block | TimeoutError | - | 25 |
| geo | TimeoutError | - | 15 |
| speed | TimeoutError | - | 10 |
| geo | ClientOSError | - | 9 |
| 204 | ClientOSError | - | 6 |
| 204 | ProxyError | - | 5 |
| cn-block | ClientOSError | - | 5 |
| geo | ProxyError | - | 3 |
| cn-block | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
