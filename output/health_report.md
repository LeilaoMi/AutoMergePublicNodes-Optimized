# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-08 11:03:20 |
| 运行耗时 | 298.3s |
| 订阅源总数 | 107 |
| 健康订阅源 | 96 |
| 原始节点 | 91310 |
| 去重后节点 | 25270 |
| TCP 可达 | 3000 |
| 真实可用 | 563 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 25270 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.9 |
| geo | 1.5 |
| tcp | 41.6 |
| probe | 81.6 |
| real_test | 120.0 |
| generate | 47.6 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 57070 |
| vmess | 12444 |
| shadowsocks | 10287 |
| trojan | 8987 |
| hysteria2 | 1800 |
| http | 502 |
| shadowsocksr | 128 |
| socks | 54 |
| hysteria | 16 |
| tuic | 11 |
| anytls | 11 |

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
| 81.27 | shadowsocks | 215.4 | 579.4 | 22.79 | 0.0 | 10.0 | 14.1 | 18.38 | Surfboard-tg-mixed | 198.98.53.130 |
| 81.09 | hysteria2 | 292.5 | 822.7 | 21.01 | 0.0 | 10.0 | 13.8 | 18.38 | Surfboard-tg-mixed | 159.223.157.129 |
| 80.77 | shadowsocks | 237.0 | 644.8 | 22.29 | 0.0 | 10.0 | 14.1 | 18.38 | Surfboard-tg-mixed | 37.19.198.244 |
| 78.04 | shadowsocks | 302.8 | 841.2 | 20.77 | 0.0 | 7.97 | 14.1 | 19.7 | Au1rxx-base64 | 38.180.135.156 |
| 77.84 | shadowsocks | 342.0 | 894.7 | 19.86 | 0.0 | 10.0 | 14.1 | 18.38 | Surfboard-tg-mixed | 51.79.64.198 |
| 77.77 | vless | 262.8 | 641.8 | 21.69 | 0.0 | 10.0 | 6.38 | 19.7 | Au1rxx-base64 | 169.40.42.74 |
| 77.67 | http | 312.7 | 850.1 | 20.54 | 0.0 | 10.0 | 14.75 | 19.88 | ermaozi | 147.182.216.4 |
| 77.52 | shadowsocks | 369.8 | 1035.9 | 19.22 | 0.0 | 10.0 | 14.1 | 19.7 | Au1rxx-base64 | 15.204.246.108 |
| 77.19 | vless | 244.7 | 641.9 | 22.11 | 0.0 | 10.0 | 6.38 | 19.7 | Au1rxx-base64 | 195.123.235.177 |
| 77.08 | vless | 292.9 | 689.3 | 21.0 | 0.0 | 10.0 | 6.38 | 19.7 | Au1rxx-base64 | 169.40.42.223 |
| 77.01 | hysteria2 | 295.5 | 588.8 | 20.94 | 0.0 | 7.96 | 13.8 | 19.7 | Au1rxx-base64 | 66.94.121.46 |
| 76.99 | vless | 296.5 | 737.3 | 20.91 | 0.0 | 10.0 | 6.38 | 19.7 | Au1rxx-base64 | 169.40.42.90 |
| 76.91 | shadowsocks | 317.3 | 898.3 | 20.43 | 0.0 | 10.0 | 14.1 | 18.38 | Surfboard-tg-mixed | 37.19.198.160 |
| 76.65 | shadowsocks | 393.6 | 946.3 | 18.67 | 0.0 | 10.0 | 14.1 | 18.38 | Surfboard-tg-mixed | 51.222.200.165 |
| 76.49 | vless | 318.2 | 788.6 | 20.41 | 0.0 | 10.0 | 6.38 | 19.7 | Au1rxx-base64 | 169.40.42.16 |
| 76.19 | vless | 331.1 | 890.9 | 20.11 | 0.0 | 10.0 | 6.38 | 19.7 | Au1rxx-base64 | 169.40.42.231 |
| 76.04 | vless | 337.7 | 799.8 | 19.96 | 0.0 | 10.0 | 6.38 | 19.7 | Au1rxx-base64 | 169.40.42.89 |
| 75.96 | vless | 341.2 | 894.3 | 19.88 | 0.0 | 10.0 | 6.38 | 19.7 | Au1rxx-base64 | 169.40.42.212 |
| 75.94 | vless | 342.0 | 816.8 | 19.86 | 0.0 | 10.0 | 6.38 | 19.7 | Au1rxx-base64 | 169.40.42.235 |
| 75.92 | vless | 343.1 | 878.0 | 19.84 | 0.0 | 10.0 | 6.38 | 19.7 | Au1rxx-base64 | 169.40.42.179 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 1.0 | 1.0 | 53 | 450 | prefer |
| Au1rxx-base64 | 0.968 | 0.902 | 325 | 1726 | prefer |
| ermaozi-get_subscribe | 0.94 | 1.0 | 19 | 470 | prefer |
| mheidari-all | 0.852 | 0.779 | 77 | 22334 | prefer |
| Surfboard-tg-mixed | 0.762 | 0.684 | 190 | 7431 | prefer |
| DeltaKronecker-all | 0.461 | 0.545 | 11 | 6097 | observe |
| tg-oneclickvpnkeys | 0.263 | 1.0 | 1 | 212 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4657 | observe |
| Epodonios-all | 0.255 | None | 0 | 7885 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 8811 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 6201 | observe |
| barry-far-vless | 0.255 | None | 0 | 6423 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4209 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| cn-block | TimeoutError | - | 24 |
| 204 | TimeoutError | - | 23 |
| geo | ClientOSError | - | 15 |
| cn-block | ClientOSError | - | 13 |
| speed | TimeoutError | - | 13 |
| 204 | ProxyError | - | 9 |
| speed | ClientOSError | - | 6 |
| 204 | ClientOSError | - | 4 |
| geo | TimeoutError | - | 3 |
| cn-block | ProxyError | - | 3 |
| speed | ProxyError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
