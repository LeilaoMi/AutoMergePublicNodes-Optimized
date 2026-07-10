# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-10 19:43:40 |
| 运行耗时 | 183.1s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 76205 |
| 去重后节点 | 23865 |
| TCP 可达 | 3000 |
| 真实可用 | 280 |
| Verified 输出 | 280 |
| Global 输出 | 294 |
| All 输出 | 23865 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.1 |
| geo | 1.3 |
| tcp | 32.1 |
| probe | 46.0 |
| real_test | 70.4 |
| generate | 29.3 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 43304 |
| trojan | 12280 |
| vmess | 10666 |
| shadowsocks | 9293 |
| hysteria2 | 289 |
| shadowsocksr | 136 |
| http | 135 |
| socks | 88 |
| hysteria | 8 |
| anytls | 5 |
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
| 77.18 | shadowsocks | 234.7 | 633.3 | 22.34 | 0.0 | 10.0 | 13.14 | 15.7 | Au1rxx-base64 | 37.19.198.160 |
| 76.91 | shadowsocks | 246.6 | 681.4 | 22.07 | 0.0 | 10.0 | 13.14 | 15.7 | Au1rxx-base64 | 37.19.198.244 |
| 76.9 | shadowsocks | 247.0 | 675.6 | 22.06 | 0.0 | 10.0 | 13.14 | 15.7 | Au1rxx-base64 | 37.19.198.236 |
| 76.89 | shadowsocks | 247.6 | 683.3 | 22.05 | 0.0 | 10.0 | 13.14 | 15.7 | Au1rxx-base64 | 37.19.198.243 |
| 76.52 | shadowsocks | 242.0 | 637.2 | 22.18 | 0.0 | 10.0 | 13.14 | 15.7 | Au1rxx-base64 | 108.181.57.93 |
| 76.23 | shadowsocks | 232.8 | 622.7 | 22.39 | 0.0 | 10.0 | 13.14 | 15.7 | Au1rxx-base64 | tinkered-pennies-puppies.freesocks.work |
| 73.29 | shadowsocks | 290.0 | 655.4 | 21.07 | 0.0 | 10.0 | 13.14 | 15.7 | Au1rxx-base64 | 156.146.38.167 |
| 73.11 | shadowsocks | 282.8 | 645.2 | 21.23 | 0.0 | 10.0 | 13.14 | 15.7 | Au1rxx-base64 | 156.146.38.168 |
| 72.76 | shadowsocks | 354.5 | 888.8 | 19.57 | 0.0 | 10.0 | 13.14 | 14.58 | mheidari-all | 185.196.61.82 |
| 72.43 | shadowsocks | 286.1 | 660.6 | 21.16 | 0.0 | 10.0 | 13.14 | 15.7 | Au1rxx-base64 | 156.146.38.169 |
| 72.41 | shadowsocks | 289.8 | 663.7 | 21.07 | 0.0 | 10.0 | 13.14 | 15.7 | Au1rxx-base64 | 156.146.38.170 |
| 71.75 | vmess | 335.7 | 903.6 | 20.01 | 0.0 | 10.0 | 12.86 | 13.38 | Surfboard-tg-mixed | 67.220.85.46 |
| 70.96 | vmess | 369.6 | 1048.5 | 19.22 | 0.0 | 10.0 | 12.86 | 13.38 | Surfboard-tg-mixed | 67.220.95.3 |
| 69.93 | hysteria2 | 356.7 | 695.4 | 19.52 | 0.0 | 10.0 | 11.25 | 15.7 | Au1rxx-base64 | 62.210.124.146 |
| 69.63 | shadowsocks | 314.9 | 555.2 | 20.49 | 0.0 | 10.0 | 13.14 | 15.7 | Au1rxx-base64 | 108.181.118.10 |
| 69.28 | shadowsocks | 338.4 | 595.0 | 19.94 | 0.0 | 10.0 | 13.14 | 15.7 | Au1rxx-base64 | 173.244.56.9 |
| 69.25 | shadowsocks | 319.2 | 604.1 | 20.39 | 0.0 | 10.0 | 13.14 | 15.7 | Au1rxx-base64 | 108.181.0.177 |
| 68.8 | shadowsocks | 341.8 | 600.1 | 19.87 | 0.0 | 10.0 | 13.14 | 15.7 | Au1rxx-base64 | 173.244.56.6 |
| 68.22 | shadowsocks | 309.0 | 837.7 | 20.62 | 0.0 | 10.0 | 13.14 | 14.58 | mheidari-all | 147.90.234.133 |
| 67.61 | trojan | 345.4 | 795.9 | 19.78 | 0.0 | 10.0 | 8.43 | 15.7 | Au1rxx-base64 | 149.28.241.235 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| Au1rxx-base64 | 0.895 | 0.901 | 71 | 123 | prefer |
| Surfboard-tg-mixed | 0.806 | 0.732 | 82 | 5583 | prefer |
| DeltaKronecker-all | 0.585 | 0.505 | 107 | 7600 | observe |
| mheidari-all | 0.552 | 0.471 | 140 | 16338 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4165 | observe |
| Epodonios-all | 0.255 | None | 0 | 6378 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3974 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6475 | observe |
| barry-far-vless | 0.255 | None | 0 | 4674 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5415 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| xiaoji235-airport-v2ray-all | 0.228 | None | 0 | 1319 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |
| nscl5-all | 0.221 | None | 0 | 1148 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 52 |
| 204 | ProxyError | - | 29 |
| 204 | TimeoutError | - | 16 |
| geo | TimeoutError | - | 13 |
| cn-block | ProxyError | - | 11 |
| 204 | ClientOSError | - | 10 |
| cn-block | ClientOSError | - | 7 |
| cn-block | TimeoutError | - | 6 |
| geo | ProxyError | - | 6 |
| speed | ProxyError | - | 4 |
| geo | ClientOSError | - | 4 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 280 | - |
| global | False | 300 | 294 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
