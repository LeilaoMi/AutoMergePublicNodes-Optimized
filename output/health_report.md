# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-14 14:00:12 |
| 运行耗时 | 183.0s |
| 订阅源总数 | 107 |
| 健康订阅源 | 103 |
| 原始节点 | 80389 |
| 去重后节点 | 23994 |
| TCP 可达 | 3000 |
| 真实可用 | 251 |
| Verified 输出 | 251 |
| Global 输出 | 261 |
| All 输出 | 23994 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.5 |
| geo | 1.3 |
| tcp | 32.6 |
| probe | 44.1 |
| real_test | 69.6 |
| generate | 30.9 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 47722 |
| trojan | 11701 |
| vmess | 10593 |
| shadowsocks | 9579 |
| hysteria2 | 477 |
| http | 138 |
| shadowsocksr | 122 |
| socks | 39 |
| hysteria | 12 |
| anytls | 4 |
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
| 72.65 | shadowsocks | 222.0 | 597.9 | 22.64 | 0.0 | 10.0 | 11.25 | 12.76 | mheidari-all | 198.98.53.130 |
| 70.54 | vmess | 345.3 | 935.3 | 19.78 | 0.0 | 10.0 | 12.5 | 12.76 | mheidari-all | 67.220.85.46 |
| 69.38 | trojan | 375.0 | 885.5 | 19.1 | 0.0 | 10.0 | 11.89 | 14.66 | DeltaKronecker-all | 64.94.95.115 |
| 68.96 | trojan | 299.2 | 647.3 | 20.85 | 0.0 | 10.0 | 11.89 | 12.76 | mheidari-all | 64.94.95.118 |
| 68.72 | trojan | 412.5 | 987.8 | 18.23 | 0.0 | 10.0 | 11.89 | 14.66 | DeltaKronecker-all | 64.94.95.117 |
| 68.21 | shadowsocks | 348.1 | 869.8 | 19.72 | 0.0 | 10.0 | 11.25 | 12.76 | mheidari-all | 185.196.61.82 |
| 67.27 | trojan | 402.2 | 545.2 | 18.47 | 0.0 | 10.0 | 11.89 | 15.92 | Surfboard-tg-mixed | 104.17.122.62 |
| 67.19 | shadowsocks | 255.5 | 703.5 | 21.86 | 0.0 | 10.0 | 11.25 | 8.08 | Au1rxx-base64 | 37.19.198.243 |
| 66.81 | shadowsocks | 272.2 | 760.1 | 21.48 | 0.0 | 10.0 | 11.25 | 8.08 | Au1rxx-base64 | 37.19.198.244 |
| 66.76 | trojan | 441.5 | 580.9 | 17.56 | 0.0 | 10.0 | 11.89 | 15.92 | Surfboard-tg-mixed | 199.232.78.140 |
| 66.62 | http | 602.9 | 935.9 | 13.82 | 0.0 | 9.84 | 14.61 | 19.52 | snakem982 | 193.176.84.31 |
| 66.46 | http | 610.4 | 940.0 | 13.65 | 0.0 | 9.83 | 14.61 | 19.52 | snakem982 | 193.176.84.37 |
| 66.38 | shadowsocks | 245.7 | 655.3 | 22.09 | 0.0 | 10.0 | 11.25 | 12.76 | mheidari-all | 108.181.57.93 |
| 66.27 | http | 619.0 | 934.9 | 13.45 | 0.0 | 9.83 | 14.61 | 19.52 | snakem982 | 193.176.84.32 |
| 65.69 | http | 636.4 | 946.6 | 13.05 | 0.0 | 9.76 | 14.61 | 19.52 | snakem982 | 84.239.49.159 |
| 65.69 | http | 637.3 | 935.3 | 13.03 | 0.0 | 9.76 | 14.61 | 19.52 | snakem982 | 84.239.49.185 |
| 65.65 | http | 636.1 | 939.6 | 13.05 | 0.0 | 9.76 | 14.61 | 19.52 | snakem982 | 84.239.14.159 |
| 65.65 | http | 636.5 | 940.9 | 13.04 | 0.0 | 9.76 | 14.61 | 19.52 | snakem982 | 84.239.49.245 |
| 65.63 | http | 637.5 | 964.3 | 13.02 | 0.0 | 9.76 | 14.61 | 19.52 | snakem982 | 84.239.49.219 |
| 65.62 | http | 635.5 | 954.2 | 13.07 | 0.0 | 9.75 | 14.61 | 19.52 | snakem982 | 84.239.49.187 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| mheidari-all | 0.796 | 0.72 | 100 | 17504 | prefer |
| Surfboard-tg-mixed | 0.781 | 0.704 | 115 | 5621 | prefer |
| DeltaKronecker-all | 0.732 | 0.655 | 87 | 7942 | prefer |
| xiaoji235-airport-v2ray-all | 0.391 | 1.0 | 2 | 3836 | observe |
| Au1rxx-base64 | 0.362 | 1.0 | 3 | 97 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4019 | observe |
| Epodonios-all | 0.255 | None | 0 | 6477 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6376 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4172 | observe |
| barry-far-vless | 0.255 | None | 0 | 4832 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5405 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| nscl5-all | 0.231 | None | 0 | 1412 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 32 |
| speed | ClientOSError | - | 16 |
| cn-block | ClientOSError | - | 10 |
| 204 | TimeoutError | - | 7 |
| 204 | ClientOSError | - | 7 |
| speed | TimeoutError | - | 7 |
| 204 | ProxyError | - | 5 |
| geo | ClientOSError | - | 3 |
| cn-block | TimeoutError | - | 3 |
| cn-block | ProxyError | - | 2 |
| geo | ProxyError | - | 1 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 278 | 251 | - |
| global | False | 290 | 261 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
