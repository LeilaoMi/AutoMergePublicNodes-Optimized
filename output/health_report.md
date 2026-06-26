# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-06-26 20:02:05 |
| 运行耗时 | 203.6s |
| 订阅源总数 | 107 |
| 健康订阅源 | 105 |
| 原始节点 | 75726 |
| 去重后节点 | 22770 |
| TCP 可达 | 3000 |
| 真实可用 | 293 |
| Verified 输出 | 293 |
| Global 输出 | 300 |
| All 输出 | 22770 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.7 |
| geo | 1.4 |
| tcp | 30.3 |
| probe | 53.9 |
| real_test | 83.5 |
| generate | 29.8 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 42645 |
| trojan | 11643 |
| vmess | 11376 |
| shadowsocks | 9502 |
| hysteria2 | 253 |
| shadowsocksr | 154 |
| http | 80 |
| socks | 63 |
| hysteria | 8 |
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
| 79.09 | shadowsocks | 234.2 | 640.3 | 22.36 | 0.0 | 10.0 | 12.91 | 17.82 | Au1rxx-base64 | 37.19.198.160 |
| 79.07 | shadowsocks | 234.9 | 646.4 | 22.34 | 0.0 | 10.0 | 12.91 | 17.82 | Au1rxx-base64 | 37.19.198.236 |
| 78.94 | shadowsocks | 240.4 | 654.9 | 22.21 | 0.0 | 10.0 | 12.91 | 17.82 | Au1rxx-base64 | 37.19.198.243 |
| 76.52 | vless | 258.3 | 711.7 | 21.8 | 0.0 | 10.0 | 9.02 | 15.7 | mheidari-all | 47.253.226.114 |
| 76.18 | shadowsocks | 246.4 | 660.2 | 22.07 | 0.0 | 10.0 | 12.91 | 15.7 | mheidari-all | 108.181.57.93 |
| 75.75 | shadowsocks | 308.5 | 856.9 | 20.64 | 0.0 | 10.0 | 12.91 | 17.82 | Au1rxx-base64 | tinkered-pennies-puppies.freesocks.work |
| 75.16 | shadowsocks | 283.5 | 658.8 | 21.21 | 0.0 | 10.0 | 12.91 | 17.82 | Au1rxx-base64 | 156.146.38.168 |
| 74.21 | shadowsocks | 295.5 | 645.6 | 20.94 | 0.0 | 10.0 | 12.91 | 17.82 | Au1rxx-base64 | 156.146.38.167 |
| 74.18 | shadowsocks | 294.7 | 660.1 | 20.95 | 0.0 | 10.0 | 12.91 | 17.82 | Au1rxx-base64 | 156.146.38.170 |
| 72.47 | shadowsocks | 328.2 | 782.9 | 20.18 | 0.0 | 10.0 | 12.91 | 17.82 | Au1rxx-base64 | 156.146.38.169 |
| 71.48 | vless | 384.4 | 925.7 | 18.88 | 0.0 | 10.0 | 9.02 | 16.46 | Surfboard-tg-mixed | 15.223.121.250 |
| 70.86 | shadowsocks | 341.0 | 645.3 | 19.89 | 0.0 | 10.0 | 12.91 | 17.82 | Au1rxx-base64 | 149.22.95.183 |
| 70.52 | shadowsocks | 327.1 | 608.3 | 20.21 | 0.0 | 10.0 | 12.91 | 17.82 | Au1rxx-base64 | 173.244.56.9 |
| 69.95 | shadowsocks | 376.4 | 758.1 | 19.06 | 0.0 | 10.0 | 12.91 | 17.82 | Au1rxx-base64 | 173.244.56.6 |
| 69.91 | shadowsocks | 363.2 | 744.1 | 19.37 | 0.0 | 10.0 | 12.91 | 17.82 | Au1rxx-base64 | 108.181.0.177 |
| 69.52 | shadowsocks | 369.8 | 714.0 | 19.22 | 0.0 | 10.0 | 12.91 | 17.82 | Au1rxx-base64 | 108.181.118.10 |
| 69.03 | vless | 330.4 | 610.6 | 20.13 | 0.0 | 10.0 | 9.02 | 17.82 | Au1rxx-base64 | 144.34.235.155 |
| 67.62 | vless | 461.5 | 930.1 | 17.1 | 0.0 | 10.0 | 9.02 | 17.82 | Au1rxx-base64 | 15.204.97.214 |
| 67.29 | vless | 476.7 | 974.8 | 16.74 | 0.0 | 10.0 | 9.02 | 17.82 | Au1rxx-base64 | 15.204.97.219 |
| 66.8 | shadowsocks | 673.2 | 1914.5 | 12.19 | 0.0 | 10.0 | 12.91 | 15.7 | mheidari-all | 198.98.53.130 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.89 | 1.0 | 18 | 39 | prefer |
| Au1rxx-base64 | 0.824 | 0.838 | 37 | 86 | prefer |
| mheidari-all | 0.741 | 0.664 | 125 | 16147 | prefer |
| Surfboard-tg-mixed | 0.732 | 0.653 | 196 | 5075 | prefer |
| DeltaKronecker-all | 0.58 | 0.5 | 62 | 6283 | observe |
| roosterkid-openproxylist-v2ray | 0.261 | 1.0 | 1 | 150 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4567 | observe |
| Epodonios-all | 0.255 | None | 0 | 7688 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3981 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7108 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 3761 | observe |
| barry-far-vless | 0.255 | None | 0 | 4543 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5248 | observe |
| nscl5-all | 0.255 | 0.5 | 2 | 1175 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 34 |
| 204 | TimeoutError | - | 26 |
| 204 | ClientOSError | - | 21 |
| 204 | ProxyError | - | 20 |
| cn-block | TimeoutError | - | 17 |
| geo | TimeoutError | - | 13 |
| cn-block | ClientOSError | - | 5 |
| speed | TimeoutError | - | 5 |
| geo | ClientOSError | - | 4 |
| geo | ProxyError | - | 3 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 293 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
