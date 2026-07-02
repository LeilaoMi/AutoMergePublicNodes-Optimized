# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-02 14:18:47 |
| 运行耗时 | 276.9s |
| 订阅源总数 | 107 |
| 健康订阅源 | 104 |
| 原始节点 | 76990 |
| 去重后节点 | 23319 |
| TCP 可达 | 3000 |
| 真实可用 | 436 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23319 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.6 |
| geo | 1.5 |
| tcp | 30.9 |
| probe | 61.8 |
| real_test | 135.7 |
| generate | 42.4 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 44008 |
| trojan | 12764 |
| vmess | 10432 |
| shadowsocks | 9105 |
| hysteria2 | 231 |
| socks | 159 |
| shadowsocksr | 149 |
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
| 78.17 | shadowsocks | 207.1 | 484.3 | 22.98 | 0.0 | 10.0 | 12.55 | 16.64 | Au1rxx-base64 | 173.244.56.6 |
| 77.67 | shadowsocks | 207.1 | 505.9 | 22.98 | 0.0 | 10.0 | 12.55 | 16.64 | Au1rxx-base64 | 108.181.118.10 |
| 77.12 | shadowsocks | 252.7 | 619.6 | 21.93 | 0.0 | 10.0 | 12.55 | 16.64 | Au1rxx-base64 | 156.146.38.170 |
| 76.92 | shadowsocks | 239.7 | 605.5 | 22.23 | 0.0 | 10.0 | 12.55 | 16.64 | Au1rxx-base64 | 108.181.0.177 |
| 76.1 | shadowsocks | 296.8 | 753.0 | 20.91 | 0.0 | 10.0 | 12.55 | 16.64 | Au1rxx-base64 | 156.146.38.168 |
| 75.58 | shadowsocks | 319.1 | 817.9 | 20.39 | 0.0 | 10.0 | 12.55 | 16.64 | Au1rxx-base64 | 156.146.38.167 |
| 74.9 | shadowsocks | 348.6 | 905.3 | 19.71 | 0.0 | 10.0 | 12.55 | 16.64 | Au1rxx-base64 | 156.146.38.169 |
| 74.26 | vless | 237.9 | 569.5 | 22.27 | 0.0 | 10.0 | 7.71 | 15.28 | Surfboard-tg-mixed | 64.23.143.23 |
| 73.85 | vless | 247.7 | 652.9 | 22.04 | 0.0 | 10.0 | 7.71 | 14.1 | mheidari-all | 107.173.237.146 |
| 73.64 | shadowsocks | 402.8 | 481.2 | 18.45 | 0.0 | 10.0 | 12.55 | 16.64 | Au1rxx-base64 | 173.244.56.9 |
| 73.08 | shadowsocks | 283.4 | 290.0 | 21.22 | 4.12 | 9.91 | 12.55 | 16.64 | Au1rxx-base64 | 149.22.87.240 |
| 72.93 | socks | 200.1 | 502.1 | 23.15 | 0.0 | 10.0 | 12.0 | 15.28 | Surfboard-tg-mixed | 104.152.50.252 |
| 71.64 | vless | 360.8 | 880.9 | 19.43 | 0.0 | 10.0 | 7.71 | 16.64 | Au1rxx-base64 | 15.204.97.214 |
| 70.32 | shadowsocks | 266.9 | 545.7 | 21.6 | 0.0 | 10.0 | 12.55 | 16.64 | Au1rxx-base64 | 149.22.95.183 |
| 70.12 | shadowsocks | 303.6 | 357.1 | 20.75 | 1.61 | 9.91 | 12.55 | 16.64 | Au1rxx-base64 | 149.22.87.241 |
| 70.08 | shadowsocks | 305.8 | 357.5 | 20.7 | 1.59 | 9.89 | 12.55 | 16.64 | Au1rxx-base64 | 149.22.87.204 |
| 69.62 | shadowsocks | 360.0 | 727.9 | 19.44 | 0.0 | 10.0 | 12.55 | 16.64 | Au1rxx-base64 | 37.19.198.236 |
| 69.55 | shadowsocks | 345.3 | 706.4 | 19.78 | 0.0 | 10.0 | 12.55 | 16.64 | Au1rxx-base64 | 37.19.198.160 |
| 69.51 | shadowsocks | 349.2 | 727.9 | 19.69 | 0.0 | 10.0 | 12.55 | 16.64 | Au1rxx-base64 | 37.19.198.244 |
| 69.41 | vless | 274.5 | 700.6 | 21.42 | 0.0 | 10.0 | 7.71 | 15.28 | Surfboard-tg-mixed | 112.121.184.10 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| Au1rxx-base64 | 0.776 | 0.786 | 42 | 78 | prefer |
| Surfboard-tg-mixed | 0.76 | 0.682 | 292 | 5750 | prefer |
| mheidari-all | 0.634 | 0.555 | 238 | 16231 | observe |
| DeltaKronecker-all | 0.602 | 0.523 | 65 | 7467 | observe |
| nscl5-all | 0.301 | 1.0 | 1 | 1162 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4254 | observe |
| Epodonios-all | 0.255 | None | 0 | 6611 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3976 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6844 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4338 | observe |
| barry-far-vless | 0.255 | None | 0 | 4895 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5365 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 88 |
| 204 | ProxyError | - | 63 |
| cn-block | TimeoutError | - | 20 |
| 204 | TimeoutError | - | 15 |
| 204 | ClientOSError | - | 13 |
| geo | TimeoutError | - | 11 |
| cn-block | ClientOSError | - | 10 |
| geo | ClientOSError | - | 7 |
| speed | TimeoutError | - | 6 |
| cn-block | ProxyError | - | 5 |
| geo | ProxyError | - | 4 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
