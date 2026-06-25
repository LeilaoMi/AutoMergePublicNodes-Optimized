# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-06-25 14:50:41 |
| 运行耗时 | 216.0s |
| 订阅源总数 | 107 |
| 健康订阅源 | 105 |
| 原始节点 | 83018 |
| 去重后节点 | 23108 |
| TCP 可达 | 3000 |
| 真实可用 | 375 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23108 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.8 |
| geo | 1.4 |
| tcp | 31.2 |
| probe | 53.5 |
| real_test | 94.1 |
| generate | 30.0 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 46296 |
| trojan | 14810 |
| vmess | 11225 |
| shadowsocks | 10054 |
| hysteria2 | 267 |
| shadowsocksr | 158 |
| http | 129 |
| socks | 71 |
| hysteria | 6 |
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
| 79.98 | shadowsocks | 232.5 | 596.8 | 22.4 | 0.0 | 10.0 | 12.12 | 19.46 | Au1rxx-base64 | 156.146.38.168 |
| 79.72 | shadowsocks | 243.5 | 624.2 | 22.14 | 0.0 | 10.0 | 12.12 | 19.46 | Au1rxx-base64 | 156.146.38.169 |
| 79.55 | shadowsocks | 250.7 | 647.5 | 21.97 | 0.0 | 10.0 | 12.12 | 19.46 | Au1rxx-base64 | 156.146.38.167 |
| 75.5 | shadowsocks | 260.0 | 544.5 | 21.76 | 0.0 | 10.0 | 12.12 | 19.46 | Au1rxx-base64 | 173.244.56.9 |
| 75.38 | shadowsocks | 298.5 | 665.2 | 20.87 | 0.0 | 10.0 | 12.12 | 19.46 | Au1rxx-base64 | 173.244.56.6 |
| 73.77 | shadowsocks | 310.3 | 632.6 | 20.6 | 0.0 | 10.0 | 12.12 | 19.46 | Au1rxx-base64 | 149.22.95.183 |
| 73.62 | vless | 349.3 | 836.9 | 19.69 | 0.0 | 10.0 | 8.7 | 19.46 | Au1rxx-base64 | 15.204.97.219 |
| 73.5 | shadowsocks | 329.2 | 716.2 | 20.16 | 0.0 | 10.0 | 12.12 | 19.46 | Au1rxx-base64 | 37.19.198.244 |
| 73.33 | shadowsocks | 340.6 | 746.8 | 19.89 | 0.0 | 10.0 | 12.12 | 19.46 | Au1rxx-base64 | 108.181.118.10 |
| 73.25 | shadowsocks | 332.4 | 726.1 | 20.08 | 0.0 | 10.0 | 12.12 | 19.46 | Au1rxx-base64 | 37.19.198.243 |
| 73.16 | vless | 202.8 | 481.5 | 23.08 | 0.0 | 10.0 | 8.7 | 15.88 | Surfboard-tg-mixed | 92.223.71.246 |
| 73.15 | shadowsocks | 327.9 | 707.9 | 20.19 | 0.0 | 10.0 | 12.12 | 19.46 | Au1rxx-base64 | 37.19.198.160 |
| 73.02 | shadowsocks | 335.8 | 721.6 | 20.0 | 0.0 | 10.0 | 12.12 | 19.46 | Au1rxx-base64 | 108.181.0.177 |
| 72.31 | trojan | 318.1 | 678.9 | 20.41 | 0.0 | 10.0 | 8.45 | 19.46 | Au1rxx-base64 | 45.61.52.243 |
| 71.25 | shadowsocks | 325.6 | 369.8 | 20.24 | 1.13 | 9.79 | 12.12 | 19.46 | Au1rxx-base64 | 149.22.87.240 |
| 71.0 | vless | 357.6 | 873.9 | 19.5 | 0.0 | 10.0 | 8.7 | 19.46 | Au1rxx-base64 | 15.204.97.214 |
| 70.66 | shadowsocks | 330.7 | 380.6 | 20.12 | 0.73 | 9.79 | 12.12 | 19.46 | Au1rxx-base64 | 149.22.87.241 |
| 70.62 | shadowsocks | 330.7 | 713.7 | 20.12 | 0.0 | 10.0 | 12.12 | 19.46 | Au1rxx-base64 | 37.19.198.236 |
| 70.55 | shadowsocks | 332.1 | 385.3 | 20.09 | 0.55 | 9.8 | 12.12 | 19.46 | Au1rxx-base64 | 149.22.87.204 |
| 70.16 | shadowsocks | 373.2 | 797.7 | 19.14 | 0.0 | 10.0 | 12.12 | 19.46 | Au1rxx-base64 | 108.181.57.93 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.977 | 1.0 | 36 | 82 | prefer |
| Au1rxx-base64 | 0.841 | 0.851 | 47 | 101 | prefer |
| Surfboard-tg-mixed | 0.778 | 0.7 | 240 | 5257 | prefer |
| mheidari-all | 0.673 | 0.594 | 170 | 16105 | observe |
| DeltaKronecker-all | 0.617 | 0.538 | 52 | 12590 | observe |
| nscl5-all | 0.3 | 1.0 | 1 | 1136 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4787 | observe |
| Epodonios-all | 0.255 | None | 0 | 7910 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3977 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7492 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 3824 | observe |
| barry-far-vless | 0.255 | None | 0 | 4673 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5133 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 75 |
| 204 | TimeoutError | - | 28 |
| 204 | ClientOSError | - | 16 |
| 204 | ProxyError | - | 12 |
| cn-block | ClientOSError | - | 8 |
| cn-block | TimeoutError | - | 8 |
| cn-block | ProxyError | - | 8 |
| geo | TimeoutError | - | 7 |
| speed | TimeoutError | - | 4 |
| speed | ProxyError | - | 3 |
| geo | ClientOSError | - | 2 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
