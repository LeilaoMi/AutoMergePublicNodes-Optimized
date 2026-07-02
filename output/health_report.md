# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-02 09:26:32 |
| 运行耗时 | 229.7s |
| 订阅源总数 | 107 |
| 健康订阅源 | 102 |
| 原始节点 | 76108 |
| 去重后节点 | 23111 |
| TCP 可达 | 3000 |
| 真实可用 | 418 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23111 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.8 |
| geo | 1.5 |
| tcp | 30.6 |
| probe | 48.4 |
| real_test | 106.9 |
| generate | 37.4 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 43050 |
| trojan | 12602 |
| vmess | 10449 |
| shadowsocks | 9335 |
| hysteria2 | 235 |
| shadowsocksr | 155 |
| socks | 140 |
| http | 135 |
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
| 77.76 | shadowsocks | 207.9 | 489.9 | 22.96 | 0.0 | 10.0 | 13.0 | 15.8 | Au1rxx-base64 | 173.244.56.9 |
| 77.52 | shadowsocks | 197.1 | 473.8 | 23.22 | 0.0 | 10.0 | 13.0 | 15.8 | Au1rxx-base64 | 108.181.118.10 |
| 77.44 | shadowsocks | 200.5 | 500.0 | 23.14 | 0.0 | 10.0 | 13.0 | 15.8 | Au1rxx-base64 | 108.181.0.177 |
| 76.82 | shadowsocks | 248.8 | 601.9 | 22.02 | 0.0 | 10.0 | 13.0 | 15.8 | Au1rxx-base64 | 156.146.38.170 |
| 76.69 | shadowsocks | 254.4 | 622.9 | 21.89 | 0.0 | 10.0 | 13.0 | 15.8 | Au1rxx-base64 | 156.146.38.168 |
| 76.44 | shadowsocks | 265.2 | 663.7 | 21.64 | 0.0 | 10.0 | 13.0 | 15.8 | Au1rxx-base64 | 173.244.56.6 |
| 74.04 | shadowsocks | 369.0 | 964.2 | 19.24 | 0.0 | 10.0 | 13.0 | 15.8 | Au1rxx-base64 | 156.146.38.167 |
| 73.46 | shadowsocks | 394.1 | 1040.6 | 18.66 | 0.0 | 10.0 | 13.0 | 15.8 | Au1rxx-base64 | 156.146.38.169 |
| 73.13 | vless | 209.9 | 500.1 | 22.92 | 0.0 | 10.0 | 5.59 | 16.62 | Surfboard-tg-mixed | 64.23.143.23 |
| 69.92 | shadowsocks | 303.3 | 353.7 | 20.76 | 1.73 | 9.91 | 13.0 | 15.8 | Au1rxx-base64 | 149.22.87.241 |
| 69.69 | shadowsocks | 350.8 | 716.5 | 19.66 | 0.0 | 10.0 | 13.0 | 15.8 | Au1rxx-base64 | 37.19.198.236 |
| 69.68 | vless | 338.2 | 813.9 | 19.95 | 0.0 | 10.0 | 5.59 | 15.8 | Au1rxx-base64 | 15.204.97.214 |
| 69.6 | shadowsocks | 352.8 | 704.8 | 19.61 | 0.0 | 10.0 | 13.0 | 15.8 | Au1rxx-base64 | 37.19.198.244 |
| 69.54 | shadowsocks | 304.9 | 358.1 | 20.72 | 1.57 | 9.9 | 13.0 | 15.8 | Au1rxx-base64 | 149.22.87.204 |
| 69.28 | shadowsocks | 308.8 | 368.1 | 20.63 | 1.2 | 9.9 | 13.0 | 15.8 | Au1rxx-base64 | 149.22.87.240 |
| 69.24 | shadowsocks | 361.8 | 769.2 | 19.4 | 0.0 | 9.81 | 13.0 | 15.8 | Au1rxx-base64 | tinkered-pennies-puppies.freesocks.work |
| 68.79 | shadowsocks | 393.1 | 856.7 | 18.68 | 0.0 | 10.0 | 13.0 | 15.8 | Au1rxx-base64 | 37.19.198.243 |
| 68.12 | shadowsocks | 438.5 | 1066.4 | 17.63 | 0.0 | 10.0 | 13.0 | 15.8 | Au1rxx-base64 | 172.234.202.34 |
| 67.82 | trojan | 399.1 | 963.6 | 18.54 | 0.0 | 10.0 | 13.3 | 11.2 | mheidari-all | 64.94.95.118 |
| 67.02 | shadowsocks | 426.1 | 916.7 | 17.91 | 0.0 | 10.0 | 13.0 | 15.8 | Au1rxx-base64 | 37.19.198.160 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| Au1rxx-base64 | 0.832 | 0.839 | 56 | 106 | prefer |
| Surfboard-tg-mixed | 0.764 | 0.686 | 261 | 5705 | prefer |
| mheidari-all | 0.705 | 0.629 | 70 | 15877 | prefer |
| DeltaKronecker-all | 0.619 | 0.54 | 202 | 7467 | observe |
| tg-LonUp_M | 0.318 | 1.0 | 2 | 179 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4254 | observe |
| Epodonios-all | 0.255 | None | 0 | 6497 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6729 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4232 | observe |
| barry-far-vless | 0.255 | None | 0 | 4756 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5365 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 91 |
| 204 | ProxyError | - | 36 |
| geo | TimeoutError | - | 30 |
| 204 | TimeoutError | - | 14 |
| geo | ClientOSError | - | 11 |
| cn-block | ProxyError | - | 8 |
| 204 | ClientOSError | - | 7 |
| cn-block | ClientOSError | - | 6 |
| cn-block | TimeoutError | - | 5 |
| speed | TimeoutError | - | 4 |
| geo | ProxyError | - | 1 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
