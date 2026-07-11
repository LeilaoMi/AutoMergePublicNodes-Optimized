# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-11 19:15:20 |
| 运行耗时 | 202.5s |
| 订阅源总数 | 107 |
| 健康订阅源 | 102 |
| 原始节点 | 75703 |
| 去重后节点 | 24094 |
| TCP 可达 | 3000 |
| 真实可用 | 280 |
| Verified 输出 | 280 |
| Global 输出 | 296 |
| All 输出 | 24094 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.0 |
| geo | 1.4 |
| tcp | 31.6 |
| probe | 51.5 |
| real_test | 76.7 |
| generate | 36.3 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 43257 |
| trojan | 11935 |
| vmess | 10624 |
| shadowsocks | 9294 |
| hysteria2 | 264 |
| shadowsocksr | 148 |
| http | 135 |
| socks | 37 |
| hysteria | 8 |
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
| 79.43 | shadowsocks | 240.4 | 644.2 | 22.21 | 0.0 | 10.0 | 13.64 | 18.08 | Surfboard-tg-mixed | 108.181.57.93 |
| 78.35 | shadowsocks | 222.4 | 595.4 | 22.63 | 0.0 | 10.0 | 13.64 | 16.08 | Au1rxx-base64 | 198.98.53.130 |
| 78.12 | shadowsocks | 232.3 | 630.0 | 22.4 | 0.0 | 10.0 | 13.64 | 16.08 | Au1rxx-base64 | 37.19.198.236 |
| 78.08 | shadowsocks | 233.9 | 648.4 | 22.36 | 0.0 | 10.0 | 13.64 | 16.08 | Au1rxx-base64 | 37.19.198.244 |
| 77.88 | shadowsocks | 242.6 | 669.4 | 22.16 | 0.0 | 10.0 | 13.64 | 16.08 | Au1rxx-base64 | 37.19.198.243 |
| 77.01 | socks | 259.8 | 666.0 | 21.76 | 0.0 | 10.0 | 11.67 | 18.08 | Surfboard-tg-mixed | 134.122.1.61 |
| 74.22 | shadowsocks | 281.8 | 642.7 | 21.25 | 0.0 | 10.0 | 13.64 | 16.08 | Au1rxx-base64 | 156.146.38.167 |
| 74.05 | shadowsocks | 286.1 | 657.0 | 21.16 | 0.0 | 10.0 | 13.64 | 16.08 | Au1rxx-base64 | 156.146.38.169 |
| 73.89 | shadowsocks | 285.3 | 804.2 | 21.17 | 0.0 | 10.0 | 13.64 | 16.08 | Au1rxx-base64 | 37.19.198.160 |
| 73.53 | shadowsocks | 323.4 | 758.2 | 20.29 | 0.0 | 10.0 | 13.64 | 16.08 | Au1rxx-base64 | 156.146.38.168 |
| 73.22 | vmess | 316.4 | 861.7 | 20.45 | 0.0 | 10.0 | 13.33 | 18.08 | Surfboard-tg-mixed | 67.220.85.46 |
| 71.75 | shadowsocks | 240.0 | 651.3 | 22.22 | 0.0 | 10.0 | 13.64 | 16.08 | Au1rxx-base64 | tinkered-pennies-puppies.freesocks.work |
| 71.22 | vless | 270.4 | 762.7 | 21.52 | 0.0 | 10.0 | 1.62 | 18.08 | Surfboard-tg-mixed | 47.253.226.114 |
| 71.13 | shadowsocks | 317.7 | 570.9 | 20.42 | 0.0 | 10.0 | 13.64 | 16.08 | Au1rxx-base64 | 173.244.56.6 |
| 70.5 | shadowsocks | 312.1 | 549.7 | 20.55 | 0.0 | 10.0 | 13.64 | 16.08 | Au1rxx-base64 | 108.181.118.10 |
| 70.1 | shadowsocks | 588.6 | 1598.5 | 14.15 | 0.0 | 10.0 | 13.64 | 18.08 | Surfboard-tg-mixed | 185.196.61.82 |
| 69.89 | shadowsocks | 366.9 | 712.9 | 19.28 | 0.0 | 10.0 | 13.64 | 16.08 | Au1rxx-base64 | 108.181.0.177 |
| 69.53 | shadowsocks | 292.3 | 801.2 | 21.01 | 0.0 | 10.0 | 13.64 | 16.08 | Au1rxx-base64 | 147.90.234.133 |
| 69.46 | trojan | 366.4 | 846.6 | 19.3 | 0.0 | 10.0 | 9.84 | 18.08 | Surfboard-tg-mixed | 64.94.95.118 |
| 68.92 | shadowsocks | 345.4 | 653.7 | 19.78 | 0.0 | 10.0 | 13.64 | 16.08 | Au1rxx-base64 | 149.22.95.183 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| Au1rxx-base64 | 0.89 | 0.909 | 33 | 96 | prefer |
| mheidari-all | 0.739 | 0.662 | 80 | 16311 | prefer |
| Surfboard-tg-mixed | 0.58 | 0.5 | 234 | 5315 | observe |
| DeltaKronecker-all | 0.5 | 0.418 | 98 | 7969 | observe |
| nscl5-all | 0.36 | 1.0 | 2 | 1207 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 3953 | observe |
| Epodonios-all | 0.255 | None | 0 | 6185 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3970 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6553 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4082 | observe |
| barry-far-vless | 0.255 | None | 0 | 4681 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5416 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| xiaoji235-airport-v2ray-all | 0.229 | None | 0 | 1340 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 76 |
| 204 | ProxyError | - | 32 |
| 204 | TimeoutError | - | 24 |
| cn-block | ClientOSError | - | 16 |
| geo | TimeoutError | - | 15 |
| cn-block | ProxyError | - | 13 |
| geo | ClientOSError | - | 7 |
| speed | ProxyError | - | 6 |
| 204 | ClientOSError | - | 5 |
| cn-block | TimeoutError | - | 5 |
| geo | ProxyError | - | 4 |
| speed | TimeoutError | - | 3 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 295 | 280 | - |
| global | False | 300 | 296 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
