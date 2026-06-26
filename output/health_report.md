# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-06-26 14:39:56 |
| 运行耗时 | 220.4s |
| 订阅源总数 | 107 |
| 健康订阅源 | 104 |
| 原始节点 | 76363 |
| 去重后节点 | 22728 |
| TCP 可达 | 3000 |
| 真实可用 | 402 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22728 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.8 |
| geo | 1.4 |
| tcp | 30.4 |
| probe | 54.5 |
| real_test | 89.1 |
| generate | 40.2 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 43580 |
| trojan | 11517 |
| vmess | 11120 |
| shadowsocks | 9536 |
| hysteria2 | 262 |
| shadowsocksr | 157 |
| http | 110 |
| socks | 71 |
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
| 78.95 | shadowsocks | 231.2 | 588.6 | 22.42 | 0.0 | 10.0 | 12.73 | 17.8 | Au1rxx-base64 | 156.146.38.167 |
| 78.67 | shadowsocks | 243.4 | 622.5 | 22.14 | 0.0 | 10.0 | 12.73 | 17.8 | Au1rxx-base64 | 156.146.38.168 |
| 76.78 | shadowsocks | 239.0 | 614.9 | 22.25 | 0.0 | 10.0 | 12.73 | 17.8 | Au1rxx-base64 | 156.146.38.170 |
| 75.63 | shadowsocks | 245.3 | 629.4 | 22.1 | 0.0 | 10.0 | 12.73 | 17.8 | Au1rxx-base64 | 156.146.38.169 |
| 75.16 | vless | 343.6 | 829.3 | 19.82 | 0.0 | 10.0 | 9.23 | 17.8 | Au1rxx-base64 | 15.204.97.219 |
| 74.64 | vless | 363.9 | 887.7 | 19.35 | 0.0 | 10.0 | 9.23 | 17.8 | Au1rxx-base64 | 15.204.97.214 |
| 74.47 | shadowsocks | 265.3 | 530.3 | 21.64 | 0.0 | 10.0 | 12.73 | 17.8 | Au1rxx-base64 | 173.244.56.9 |
| 73.65 | shadowsocks | 297.6 | 611.6 | 20.89 | 0.0 | 10.0 | 12.73 | 17.8 | Au1rxx-base64 | 108.181.118.10 |
| 73.56 | shadowsocks | 304.7 | 687.0 | 20.72 | 0.0 | 10.0 | 12.73 | 17.8 | Au1rxx-base64 | 173.244.56.6 |
| 72.94 | shadowsocks | 293.2 | 579.2 | 20.99 | 0.0 | 10.0 | 12.73 | 17.8 | Au1rxx-base64 | 149.22.95.183 |
| 72.76 | shadowsocks | 324.4 | 706.4 | 20.27 | 0.0 | 10.0 | 12.73 | 17.8 | Au1rxx-base64 | 37.19.198.243 |
| 72.54 | shadowsocks | 304.8 | 643.9 | 20.72 | 0.0 | 10.0 | 12.73 | 17.8 | Au1rxx-base64 | 108.181.0.177 |
| 72.49 | shadowsocks | 327.3 | 716.3 | 20.2 | 0.0 | 10.0 | 12.73 | 17.8 | Au1rxx-base64 | 37.19.198.236 |
| 72.19 | shadowsocks | 325.9 | 710.7 | 20.23 | 0.0 | 10.0 | 12.73 | 17.8 | Au1rxx-base64 | 37.19.198.160 |
| 71.63 | shadowsocks | 332.5 | 726.4 | 20.08 | 0.0 | 10.0 | 12.73 | 17.8 | Au1rxx-base64 | 37.19.198.244 |
| 70.72 | shadowsocks | 404.1 | 1029.8 | 18.42 | 0.0 | 10.0 | 12.73 | 17.8 | Au1rxx-base64 | 172.234.202.34 |
| 70.36 | shadowsocks | 359.6 | 341.8 | 19.45 | 2.18 | 9.8 | 12.73 | 17.8 | Au1rxx-base64 | 149.22.87.240 |
| 69.21 | shadowsocks | 312.1 | 661.9 | 20.55 | 0.0 | 10.0 | 12.73 | 14.58 | mheidari-all | 198.98.53.130 |
| 68.6 | vless | 373.8 | 826.3 | 19.12 | 0.0 | 10.0 | 9.23 | 14.58 | mheidari-all | 47.253.226.114 |
| 68.53 | hysteria2 | 426.2 | 739.9 | 17.91 | 0.0 | 9.69 | 11.25 | 17.8 | Au1rxx-base64 | 62.210.124.146 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.977 | 1.0 | 36 | 82 | prefer |
| Au1rxx-base64 | 0.891 | 0.902 | 51 | 108 | prefer |
| Surfboard-tg-mixed | 0.823 | 0.745 | 165 | 5176 | prefer |
| mheidari-all | 0.785 | 0.706 | 218 | 16250 | prefer |
| DeltaKronecker-all | 0.413 | 0.331 | 121 | 6283 | observe |
| Barabama-yudou | 0.318 | 1.0 | 2 | 166 | observe |
| nscl5-all | 0.302 | 1.0 | 1 | 1175 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4567 | observe |
| Epodonios-all | 0.255 | None | 0 | 7885 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3981 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7254 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 3834 | observe |
| barry-far-vless | 0.255 | None | 0 | 4612 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5185 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 101 |
| 204 | TimeoutError | - | 15 |
| 204 | ClientOSError | - | 13 |
| geo | TimeoutError | - | 12 |
| cn-block | TimeoutError | - | 12 |
| 204 | ProxyError | - | 11 |
| geo | ClientOSError | - | 9 |
| speed | TimeoutError | - | 7 |
| cn-block | ClientOSError | - | 4 |
| geo | ProxyError | - | 4 |
| cn-block | ProxyError | - | 3 |
| speed | ClientPayloadError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
