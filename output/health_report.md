# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-08 16:35:05 |
| 运行耗时 | 694.8s |
| 订阅源总数 | 107 |
| 健康订阅源 | 96 |
| 原始节点 | 90488 |
| 去重后节点 | 25021 |
| TCP 可达 | 3000 |
| 真实可用 | 458 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 25021 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.9 |
| geo | 1.4 |
| tcp | 42.8 |
| probe | 285.3 |
| real_test | 269.2 |
| generate | 90.2 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 56378 |
| vmess | 12339 |
| shadowsocks | 10206 |
| trojan | 8935 |
| hysteria2 | 1971 |
| http | 437 |
| shadowsocksr | 129 |
| socks | 54 |
| hysteria | 16 |
| tuic | 13 |
| anytls | 10 |

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
| 80.04 | vless | 297.0 | 661.2 | 20.9 | 0.0 | 9.01 | 11.51 | 19.36 | Au1rxx-base64 | 169.40.42.179 |
| 79.62 | vless | 317.4 | 777.1 | 20.43 | 0.0 | 8.96 | 11.51 | 19.36 | Au1rxx-base64 | 169.40.42.224 |
| 79.49 | vless | 346.8 | 921.4 | 19.75 | 0.0 | 9.04 | 11.51 | 19.36 | Au1rxx-base64 | 216.152.147.28 |
| 79.17 | vless | 330.9 | 810.2 | 20.12 | 0.0 | 9.08 | 11.51 | 19.36 | Au1rxx-base64 | 169.40.42.89 |
| 78.7 | vless | 376.5 | 712.2 | 19.06 | 0.0 | 9.08 | 11.51 | 19.36 | Au1rxx-base64 | 169.40.42.235 |
| 78.46 | shadowsocks | 253.9 | 603.1 | 21.9 | 0.0 | 9.02 | 13.59 | 19.36 | Au1rxx-base64 | 156.146.38.169 |
| 78.35 | shadowsocks | 261.8 | 656.7 | 21.72 | 0.0 | 10.0 | 13.59 | 17.04 | mheidari-all | 37.19.198.244 |
| 77.96 | shadowsocks | 288.6 | 725.4 | 21.1 | 0.0 | 9.01 | 13.59 | 19.36 | Au1rxx-base64 | 37.19.198.236 |
| 77.95 | vless | 335.0 | 802.8 | 20.02 | 0.0 | 9.07 | 11.51 | 19.36 | Au1rxx-base64 | 195.123.235.177 |
| 77.79 | vless | 252.2 | 629.0 | 21.94 | 0.0 | 9.08 | 11.51 | 19.36 | Au1rxx-base64 | 130.94.115.231 |
| 77.58 | vless | 374.9 | 837.5 | 19.1 | 0.0 | 9.01 | 11.51 | 19.36 | Au1rxx-base64 | 169.40.42.184 |
| 77.52 | vless | 317.5 | 710.2 | 20.43 | 0.0 | 9.08 | 11.51 | 19.36 | Au1rxx-base64 | 169.40.42.90 |
| 77.47 | vless | 416.6 | 992.9 | 18.13 | 0.0 | 9.19 | 11.51 | 19.36 | Au1rxx-base64 | 169.40.42.74 |
| 77.37 | vless | 308.2 | 693.2 | 20.64 | 0.0 | 9.04 | 11.51 | 19.36 | Au1rxx-base64 | 169.40.42.182 |
| 77.37 | vless | 379.2 | 966.2 | 19.0 | 0.0 | 9.0 | 11.51 | 19.36 | Au1rxx-base64 | 185.95.231.156 |
| 77.36 | vless | 346.3 | 842.2 | 19.76 | 0.0 | 9.0 | 11.51 | 19.36 | Au1rxx-base64 | 66.70.179.198 |
| 77.22 | shadowsocks | 267.4 | 667.2 | 21.59 | 0.0 | 10.0 | 13.59 | 17.04 | mheidari-all | 37.19.198.160 |
| 76.82 | vless | 398.7 | 898.0 | 18.55 | 0.0 | 9.17 | 11.51 | 19.36 | Au1rxx-base64 | 169.40.42.212 |
| 76.71 | hysteria2 | 295.8 | 566.0 | 20.93 | 0.0 | 9.2 | 12.22 | 19.36 | Au1rxx-base64 | 66.94.121.46 |
| 76.56 | vless | 305.2 | 684.8 | 20.71 | 0.0 | 9.01 | 11.51 | 19.36 | Au1rxx-base64 | 169.40.42.15 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.965 | 0.902 | 305 | 1658 | prefer |
| Surfboard-tg-mixed | 0.721 | 0.644 | 90 | 7484 | prefer |
| ermaozi | 0.674 | 0.667 | 33 | 409 | observe |
| mheidari-all | 0.573 | 0.493 | 205 | 21582 | observe |
| tg-oneclickvpnkeys | 0.263 | 1.0 | 1 | 212 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4657 | observe |
| DeltaKronecker-all | 0.255 | None | 0 | 6097 | observe |
| Epodonios-all | 0.255 | None | 0 | 7932 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 8703 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 6283 | observe |
| barry-far-vless | 0.255 | None | 0 | 6501 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4209 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| cn-block | ClientOSError | - | 45 |
| geo | ClientOSError | - | 40 |
| 204 | ProxyError | - | 27 |
| 204 | TimeoutError | - | 20 |
| cn-block | TimeoutError | - | 18 |
| speed | ClientOSError | - | 10 |
| 204 | ClientOSError | - | 10 |
| speed | TimeoutError | - | 5 |
| geo | TimeoutError | - | 4 |
| cn-block | ProxyError | - | 2 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
