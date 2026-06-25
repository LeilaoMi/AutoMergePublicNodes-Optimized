# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-06-25 20:13:21 |
| 运行耗时 | 237.5s |
| 订阅源总数 | 107 |
| 健康订阅源 | 105 |
| 原始节点 | 82829 |
| 去重后节点 | 22935 |
| TCP 可达 | 3000 |
| 真实可用 | 287 |
| Verified 输出 | 287 |
| Global 输出 | 293 |
| All 输出 | 22935 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.5 |
| geo | 1.3 |
| tcp | 30.3 |
| probe | 60.6 |
| real_test | 97.4 |
| generate | 42.4 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 46027 |
| trojan | 14975 |
| vmess | 11103 |
| shadowsocks | 10107 |
| hysteria2 | 263 |
| shadowsocksr | 154 |
| http | 118 |
| socks | 74 |
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
| 76.72 | vless | 307.6 | 800.1 | 20.66 | 0.0 | 10.0 | 9.24 | 16.82 | Au1rxx-base64 | 15.204.97.214 |
| 76.67 | vless | 309.7 | 811.1 | 20.61 | 0.0 | 10.0 | 9.24 | 16.82 | Au1rxx-base64 | 15.204.97.219 |
| 76.54 | shadowsocks | 219.0 | 499.7 | 22.71 | 0.0 | 10.0 | 11.98 | 16.82 | Au1rxx-base64 | 149.22.95.183 |
| 75.8 | shadowsocks | 292.6 | 739.4 | 21.0 | 0.0 | 10.0 | 11.98 | 16.82 | Au1rxx-base64 | 173.244.56.6 |
| 74.36 | vless | 160.7 | 441.4 | 24.06 | 0.0 | 10.0 | 9.24 | 15.56 | Surfboard-tg-mixed | 92.223.71.246 |
| 73.73 | trojan | 255.8 | 647.2 | 21.86 | 0.0 | 10.0 | 8.81 | 15.56 | Surfboard-tg-mixed | 207.126.167.150 |
| 73.61 | trojan | 315.1 | 840.7 | 20.48 | 0.0 | 10.0 | 8.81 | 16.82 | Au1rxx-base64 | 45.61.52.243 |
| 72.35 | shadowsocks | 298.4 | 660.5 | 20.87 | 0.0 | 10.0 | 11.98 | 16.82 | Au1rxx-base64 | 156.146.38.167 |
| 71.78 | shadowsocks | 299.8 | 675.2 | 20.84 | 0.0 | 10.0 | 11.98 | 16.82 | Au1rxx-base64 | 156.146.38.168 |
| 70.65 | shadowsocks | 260.9 | 603.8 | 21.74 | 0.0 | 10.0 | 11.98 | 16.82 | Au1rxx-base64 | 173.244.56.9 |
| 70.65 | shadowsocks | 293.3 | 342.8 | 20.99 | 2.14 | 9.91 | 11.98 | 16.82 | Au1rxx-base64 | 149.22.87.241 |
| 70.28 | shadowsocks | 296.3 | 351.6 | 20.92 | 1.81 | 9.91 | 11.98 | 16.82 | Au1rxx-base64 | 149.22.87.240 |
| 68.42 | shadowsocks | 363.7 | 726.8 | 19.36 | 0.0 | 10.0 | 11.98 | 16.82 | Au1rxx-base64 | 37.19.198.160 |
| 68.31 | shadowsocks | 368.7 | 737.7 | 19.24 | 0.0 | 10.0 | 11.98 | 16.82 | Au1rxx-base64 | 37.19.198.244 |
| 67.98 | vless | 356.0 | 406.7 | 19.54 | 0.0 | 9.89 | 9.24 | 16.82 | Au1rxx-base64 | 13.231.185.74 |
| 67.61 | shadowsocks | 371.8 | 735.2 | 19.17 | 0.0 | 10.0 | 11.98 | 16.82 | Au1rxx-base64 | 37.19.198.243 |
| 67.5 | shadowsocks | 393.5 | 763.0 | 18.67 | 0.0 | 10.0 | 11.98 | 16.82 | Au1rxx-base64 | 108.181.118.10 |
| 67.45 | shadowsocks | 395.2 | 789.2 | 18.63 | 0.0 | 10.0 | 11.98 | 16.82 | Au1rxx-base64 | 198.98.53.130 |
| 67.37 | shadowsocks | 291.8 | 639.6 | 21.02 | 0.0 | 10.0 | 11.98 | 16.82 | Au1rxx-base64 | 156.146.38.170 |
| 66.6 | shadowsocks | 404.2 | 757.3 | 18.42 | 0.0 | 10.0 | 11.98 | 16.82 | Au1rxx-base64 | 108.181.57.93 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.977 | 1.0 | 36 | 82 | prefer |
| Au1rxx-base64 | 0.82 | 0.83 | 47 | 104 | prefer |
| Surfboard-tg-mixed | 0.785 | 0.707 | 181 | 5178 | prefer |
| mheidari-all | 0.588 | 0.508 | 120 | 16098 | observe |
| DeltaKronecker-all | 0.487 | 0.404 | 52 | 12590 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4787 | observe |
| Epodonios-all | 0.255 | None | 0 | 7883 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7637 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 3800 | observe |
| barry-far-vless | 0.255 | None | 0 | 4620 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5117 | observe |
| nscl5-all | 0.253 | 0.5 | 2 | 1136 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 45 |
| 204 | TimeoutError | - | 32 |
| 204 | ProxyError | - | 21 |
| 204 | ClientOSError | - | 13 |
| cn-block | TimeoutError | - | 12 |
| geo | TimeoutError | - | 11 |
| speed | TimeoutError | - | 7 |
| cn-block | ClientOSError | - | 5 |
| geo | ProxyError | - | 2 |
| cn-block | ProxyError | - | 2 |
| geo | ClientOSError | - | 1 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 287 | - |
| global | False | 300 | 293 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
