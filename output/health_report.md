# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-06-27 19:40:50 |
| 运行耗时 | 232.6s |
| 订阅源总数 | 107 |
| 健康订阅源 | 105 |
| 原始节点 | 76527 |
| 去重后节点 | 23143 |
| TCP 可达 | 3000 |
| 真实可用 | 348 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23143 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.9 |
| geo | 1.4 |
| tcp | 31.0 |
| probe | 56.7 |
| real_test | 102.2 |
| generate | 36.4 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 42559 |
| trojan | 12816 |
| vmess | 11239 |
| shadowsocks | 9308 |
| hysteria2 | 270 |
| shadowsocksr | 146 |
| http | 135 |
| socks | 45 |
| hysteria | 6 |
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
| 78.49 | vless | 302.1 | 765.8 | 20.79 | 0.0 | 10.0 | 10.42 | 17.28 | mheidari-all | 47.253.226.114 |
| 77.64 | shadowsocks | 246.4 | 601.1 | 22.07 | 0.0 | 10.0 | 11.31 | 18.26 | Au1rxx-base64 | 156.146.38.167 |
| 77.4 | shadowsocks | 257.0 | 620.1 | 21.83 | 0.0 | 10.0 | 11.31 | 18.26 | Au1rxx-base64 | 156.146.38.170 |
| 77.3 | shadowsocks | 261.3 | 639.0 | 21.73 | 0.0 | 10.0 | 11.31 | 18.26 | Au1rxx-base64 | 156.146.38.168 |
| 77.11 | shadowsocks | 266.2 | 672.5 | 21.62 | 0.0 | 10.0 | 11.31 | 18.26 | Au1rxx-base64 | 37.19.198.243 |
| 77.07 | shadowsocks | 268.5 | 670.9 | 21.56 | 0.0 | 10.0 | 11.31 | 18.26 | Au1rxx-base64 | 37.19.198.160 |
| 77.07 | shadowsocks | 271.0 | 677.8 | 21.5 | 0.0 | 10.0 | 11.31 | 18.26 | Au1rxx-base64 | 37.19.198.236 |
| 75.47 | shadowsocks | 276.5 | 673.9 | 21.38 | 0.0 | 10.0 | 11.31 | 17.28 | mheidari-all | 108.181.57.93 |
| 75.02 | shadowsocks | 273.5 | 676.1 | 21.45 | 0.0 | 10.0 | 11.31 | 18.26 | Au1rxx-base64 | 37.19.198.244 |
| 72.57 | shadowsocks | 249.6 | 620.2 | 22.0 | 0.0 | 10.0 | 11.31 | 18.26 | Au1rxx-base64 | 156.146.38.169 |
| 72.39 | vless | 401.5 | 880.1 | 18.48 | 0.0 | 10.0 | 10.42 | 18.26 | Au1rxx-base64 | 15.204.97.214 |
| 71.72 | shadowsocks | 302.0 | 586.2 | 20.79 | 0.0 | 10.0 | 11.31 | 18.26 | Au1rxx-base64 | 173.244.56.9 |
| 71.33 | vless | 413.1 | 904.9 | 18.21 | 0.0 | 10.0 | 10.42 | 18.26 | Au1rxx-base64 | 15.204.97.219 |
| 70.98 | shadowsocks | 512.8 | 1114.7 | 15.91 | 0.0 | 10.0 | 11.31 | 18.26 | Au1rxx-base64 | 172.234.202.34 |
| 70.85 | shadowsocks | 336.5 | 733.2 | 19.99 | 0.0 | 10.0 | 11.31 | 18.26 | Au1rxx-base64 | 173.244.56.6 |
| 70.62 | shadowsocks | 372.7 | 954.4 | 19.15 | 0.0 | 10.0 | 11.31 | 15.36 | Surfboard-tg-mixed | 198.98.53.130 |
| 70.54 | shadowsocks | 299.3 | 619.5 | 20.85 | 0.0 | 10.0 | 11.31 | 18.26 | Au1rxx-base64 | 149.22.95.183 |
| 69.81 | vless | 450.0 | 1149.1 | 17.36 | 0.0 | 10.0 | 10.42 | 15.36 | Surfboard-tg-mixed | 15.223.121.250 |
| 69.09 | trojan | 300.4 | 574.8 | 20.82 | 0.0 | 10.0 | 5.91 | 15.36 | Surfboard-tg-mixed | 94.140.0.100 |
| 68.8 | vless | 326.8 | 617.8 | 20.21 | 0.0 | 10.0 | 10.42 | 18.26 | Au1rxx-base64 | 38.244.20.69 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| Au1rxx-base64 | 0.795 | 0.804 | 46 | 95 | prefer |
| Surfboard-tg-mixed | 0.768 | 0.69 | 213 | 5026 | prefer |
| mheidari-all | 0.601 | 0.521 | 165 | 16060 | observe |
| DeltaKronecker-all | 0.524 | 0.443 | 88 | 6822 | observe |
| Barabama-yudou | 0.318 | 1.0 | 2 | 166 | observe |
| nscl5-all | 0.302 | 1.0 | 1 | 1186 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4579 | observe |
| Epodonios-all | 0.255 | None | 0 | 7776 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3980 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7278 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 3682 | observe |
| barry-far-vless | 0.255 | None | 0 | 4576 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5287 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 82 |
| 204 | TimeoutError | - | 24 |
| cn-block | TimeoutError | - | 23 |
| 204 | ClientOSError | - | 18 |
| geo | TimeoutError | - | 18 |
| 204 | ProxyError | - | 16 |
| geo | ClientOSError | - | 8 |
| speed | TimeoutError | - | 8 |
| cn-block | ClientOSError | - | 4 |
| cn-block | ProxyError | - | 2 |
| speed | ProxyError | - | 1 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 296 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
