# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-06-23 09:57:49 |
| 运行耗时 | 242.1s |
| 订阅源总数 | 107 |
| 健康订阅源 | 105 |
| 原始节点 | 76152 |
| 去重后节点 | 21940 |
| TCP 可达 | 3000 |
| 真实可用 | 350 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 21940 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.0 |
| geo | 1.4 |
| tcp | 29.3 |
| probe | 63.4 |
| real_test | 107.5 |
| generate | 35.5 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 45881 |
| trojan | 10151 |
| shadowsocks | 9733 |
| vmess | 9730 |
| hysteria2 | 245 |
| http | 171 |
| shadowsocksr | 168 |
| socks | 63 |
| hysteria | 7 |
| tuic | 2 |
| anytls | 1 |

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
| 77.33 | shadowsocks | 192.5 | 470.3 | 23.32 | 0.0 | 10.0 | 13.83 | 14.68 | Au1rxx-base64 | 108.181.118.10 |
| 77.22 | shadowsocks | 197.2 | 483.6 | 23.21 | 0.0 | 10.0 | 13.83 | 14.68 | Au1rxx-base64 | 108.181.0.177 |
| 76.93 | shadowsocks | 231.4 | 526.7 | 22.42 | 0.0 | 10.0 | 13.83 | 14.68 | Au1rxx-base64 | 173.244.56.9 |
| 75.63 | shadowsocks | 244.6 | 596.8 | 22.12 | 0.0 | 10.0 | 13.83 | 14.68 | Au1rxx-base64 | 149.22.95.183 |
| 74.42 | trojan | 283.5 | 675.0 | 21.21 | 0.0 | 10.0 | 11.72 | 14.68 | Au1rxx-base64 | 45.61.52.243 |
| 72.56 | shadowsocks | 289.0 | 649.0 | 21.09 | 0.0 | 10.0 | 13.83 | 14.68 | Au1rxx-base64 | 156.146.38.169 |
| 71.8 | shadowsocks | 291.3 | 650.3 | 21.04 | 0.0 | 10.0 | 13.83 | 14.68 | Au1rxx-base64 | 156.146.38.170 |
| 70.41 | shadowsocks | 380.0 | 925.7 | 18.98 | 0.0 | 10.0 | 13.83 | 14.68 | Au1rxx-base64 | 156.146.38.168 |
| 69.74 | shadowsocks | 301.0 | 356.1 | 20.81 | 1.65 | 9.93 | 13.83 | 14.68 | Au1rxx-base64 | 149.22.87.204 |
| 69.52 | shadowsocks | 305.3 | 355.3 | 20.71 | 1.68 | 9.91 | 13.83 | 14.68 | Au1rxx-base64 | 149.22.87.241 |
| 69.34 | vless | 311.7 | 815.2 | 20.56 | 0.0 | 10.0 | 4.1 | 14.68 | Au1rxx-base64 | 15.204.97.214 |
| 69.11 | vless | 321.8 | 847.6 | 20.33 | 0.0 | 10.0 | 4.1 | 14.68 | Au1rxx-base64 | 15.204.97.219 |
| 68.23 | shadowsocks | 328.7 | 764.3 | 20.17 | 0.0 | 10.0 | 13.83 | 14.68 | Au1rxx-base64 | 156.146.38.167 |
| 68.03 | shadowsocks | 369.9 | 747.2 | 19.22 | 0.0 | 10.0 | 13.83 | 14.68 | Au1rxx-base64 | 37.19.198.236 |
| 67.97 | shadowsocks | 371.9 | 753.5 | 19.17 | 0.0 | 10.0 | 13.83 | 14.68 | Au1rxx-base64 | 37.19.198.243 |
| 67.57 | shadowsocks | 373.8 | 761.0 | 19.13 | 0.0 | 10.0 | 13.83 | 14.68 | Au1rxx-base64 | 37.19.198.160 |
| 66.9 | vmess | 226.3 | 604.3 | 22.54 | 0.0 | 10.0 | 12.5 | 6.36 | Barabama-yudou | 82.198.246.233 |
| 66.79 | shadowsocks | 418.3 | 892.5 | 18.09 | 0.0 | 10.0 | 13.83 | 14.68 | Au1rxx-base64 | 37.19.198.244 |
| 66.61 | trojan | 385.7 | 883.6 | 18.85 | 0.0 | 10.0 | 11.72 | 12.8 | mheidari-all | 64.94.95.118 |
| 65.23 | shadowsocks | 358.0 | 709.4 | 19.49 | 0.0 | 10.0 | 13.83 | 14.68 | Au1rxx-base64 | 198.98.53.130 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.987 | 1.0 | 58 | 95 | prefer |
| Au1rxx-base64 | 0.765 | 0.768 | 69 | 116 | prefer |
| Surfboard-tg-mixed | 0.71 | 0.632 | 209 | 5285 | prefer |
| mheidari-all | 0.615 | 0.535 | 155 | 15546 | observe |
| DeltaKronecker-all | 0.501 | 0.418 | 55 | 6437 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4576 | observe |
| Epodonios-all | 0.255 | None | 0 | 7878 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7202 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4084 | observe |
| barry-far-vless | 0.255 | None | 0 | 4896 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4477 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| nscl5-all | 0.237 | None | 0 | 1559 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 73 |
| 204 | TimeoutError | - | 45 |
| cn-block | TimeoutError | - | 18 |
| geo | TimeoutError | - | 13 |
| geo | ClientOSError | - | 12 |
| 204 | ProxyError | - | 10 |
| cn-block | ClientOSError | - | 6 |
| speed | TimeoutError | - | 6 |
| cn-block | ProxyError | - | 5 |
| 204 | ClientOSError | - | 5 |
| speed | ProxyError | - | 2 |
| geo | ProxyError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
