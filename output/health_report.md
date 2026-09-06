# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-06 15:20:20 |
| 运行耗时 | 268.5s |
| 订阅源总数 | 107 |
| 健康订阅源 | 96 |
| 原始节点 | 94591 |
| 去重后节点 | 24561 |
| TCP 可达 | 3000 |
| 真实可用 | 515 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 24561 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.3 |
| geo | 1.3 |
| tcp | 41.1 |
| probe | 67.4 |
| real_test | 116.6 |
| generate | 37.6 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 59022 |
| vmess | 12855 |
| shadowsocks | 11277 |
| trojan | 9058 |
| hysteria2 | 2001 |
| http | 138 |
| shadowsocksr | 127 |
| socks | 62 |
| hysteria | 19 |
| anytls | 18 |
| tuic | 14 |

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
| 81.22 | shadowsocks | 243.2 | 581.8 | 22.15 | 0.0 | 10.0 | 14.43 | 18.64 | Au1rxx-base64 | 156.146.38.167 |
| 79.84 | trojan | 245.5 | 587.0 | 22.09 | 0.0 | 10.0 | 12.58 | 18.64 | Au1rxx-base64 | 64.94.95.118 |
| 79.13 | shadowsocks | 251.4 | 613.2 | 21.96 | 0.0 | 10.0 | 14.43 | 17.24 | Surfboard-tg-mixed | 23.150.248.20 |
| 78.83 | trojan | 265.7 | 581.1 | 21.63 | 0.0 | 10.0 | 12.58 | 18.64 | Au1rxx-base64 | 64.94.95.115 |
| 78.38 | shadowsocks | 316.3 | 757.9 | 20.46 | 0.0 | 10.0 | 14.43 | 18.64 | Au1rxx-base64 | 37.19.198.160 |
| 78.32 | shadowsocks | 308.1 | 808.0 | 20.65 | 0.0 | 10.0 | 14.43 | 17.24 | Surfboard-tg-mixed | 156.146.38.168 |
| 78.09 | shadowsocks | 317.7 | 848.8 | 20.42 | 0.0 | 10.0 | 14.43 | 17.24 | Surfboard-tg-mixed | 156.146.38.170 |
| 77.28 | shadowsocks | 322.8 | 800.5 | 20.31 | 0.0 | 10.0 | 14.43 | 18.64 | Au1rxx-base64 | 37.19.198.243 |
| 77.26 | shadowsocks | 292.8 | 700.6 | 21.0 | 0.0 | 9.92 | 14.43 | 18.64 | Au1rxx-base64 | 37.19.198.236 |
| 76.36 | vless | 386.6 | 1012.0 | 18.83 | 0.0 | 9.87 | 10.65 | 18.64 | Au1rxx-base64 | 45.138.100.226 |
| 76.24 | hysteria2 | 261.8 | 554.8 | 21.72 | 0.0 | 9.91 | 13.57 | 18.64 | Au1rxx-base64 | 66.94.121.46 |
| 76.13 | shadowsocks | 296.1 | 700.7 | 20.92 | 0.0 | 9.88 | 14.43 | 18.64 | Au1rxx-base64 | 37.19.198.244 |
| 75.73 | vless | 318.3 | 641.1 | 20.41 | 0.0 | 9.86 | 10.65 | 18.64 | Au1rxx-base64 | 38.150.33.232 |
| 75.38 | shadowsocks | 286.7 | 552.5 | 21.14 | 0.0 | 10.0 | 14.43 | 18.64 | Au1rxx-base64 | 149.22.95.183 |
| 75.29 | vless | 360.7 | 735.5 | 19.43 | 0.0 | 9.87 | 10.65 | 18.64 | Au1rxx-base64 | 169.40.42.179 |
| 75.26 | trojan | 246.3 | 578.4 | 22.08 | 0.0 | 10.0 | 12.58 | 18.64 | Au1rxx-base64 | 64.94.95.117 |
| 75.15 | vless | 396.4 | 906.1 | 18.6 | 0.0 | 9.91 | 10.65 | 18.64 | Au1rxx-base64 | 169.40.42.104 |
| 74.97 | trojan | 254.2 | 576.2 | 21.89 | 0.0 | 10.0 | 12.58 | 18.64 | Au1rxx-base64 | 64.94.95.114 |
| 74.97 | vless | 344.0 | 623.1 | 19.81 | 0.0 | 9.84 | 10.65 | 18.64 | Au1rxx-base64 | 38.209.125.45 |
| 74.86 | vless | 371.1 | 832.0 | 19.19 | 0.0 | 9.9 | 10.65 | 18.64 | Au1rxx-base64 | 66.70.179.198 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.974 | 0.902 | 346 | 1876 | prefer |
| zhangkai | 0.964 | 1.0 | 22 | 144 | prefer |
| Surfboard-tg-mixed | 0.804 | 0.727 | 161 | 7393 | prefer |
| mheidari-all | 0.512 | 0.431 | 137 | 21148 | observe |
| xiaoji235-airport-v2ray-all | 0.391 | 1.0 | 2 | 5750 | observe |
| tg-oneclickvpnkeys | 0.363 | 1.0 | 3 | 133 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4791 | observe |
| Epodonios-all | 0.255 | None | 0 | 7776 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 8812 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 6147 | observe |
| barry-far-vless | 0.255 | None | 0 | 6226 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4111 | observe |
| Au1rxx-clash | 0.25 | None | 0 | 1876 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| cn-block | ClientOSError | - | 42 |
| geo | ClientOSError | - | 36 |
| 204 | TimeoutError | - | 29 |
| cn-block | TimeoutError | - | 18 |
| 204 | ProxyError | - | 10 |
| speed | TimeoutError | - | 9 |
| cn-block | ProxyError | - | 6 |
| speed | ClientOSError | - | 3 |
| 204 | ClientOSError | - | 2 |
| geo | TimeoutError | - | 2 |
| 204 | ServerDisconnectedError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
