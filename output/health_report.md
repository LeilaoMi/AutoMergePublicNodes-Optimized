# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-02 04:06:36 |
| 运行耗时 | 268.7s |
| 订阅源总数 | 107 |
| 健康订阅源 | 102 |
| 原始节点 | 76385 |
| 去重后节点 | 23479 |
| TCP 可达 | 3000 |
| 真实可用 | 601 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23479 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.3 |
| geo | 1.3 |
| tcp | 31.1 |
| probe | 57.0 |
| real_test | 150.0 |
| generate | 25.0 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 43112 |
| trojan | 12950 |
| vmess | 10362 |
| shadowsocks | 9211 |
| hysteria2 | 232 |
| socks | 217 |
| shadowsocksr | 159 |
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
| 75.66 | shadowsocks | 253.2 | 616.2 | 21.92 | 0.0 | 10.0 | 11.9 | 15.84 | Au1rxx-base64 | 156.146.38.167 |
| 75.65 | shadowsocks | 253.4 | 619.8 | 21.91 | 0.0 | 10.0 | 11.9 | 15.84 | Au1rxx-base64 | 156.146.38.170 |
| 75.6 | shadowsocks | 255.6 | 642.8 | 21.86 | 0.0 | 10.0 | 11.9 | 15.84 | Au1rxx-base64 | 156.146.38.168 |
| 75.38 | shadowsocks | 264.9 | 663.1 | 21.64 | 0.0 | 10.0 | 11.9 | 15.84 | Au1rxx-base64 | 37.19.198.236 |
| 75.29 | shadowsocks | 269.0 | 672.4 | 21.55 | 0.0 | 10.0 | 11.9 | 15.84 | Au1rxx-base64 | 37.19.198.160 |
| 75.28 | shadowsocks | 269.3 | 676.8 | 21.54 | 0.0 | 10.0 | 11.9 | 15.84 | Au1rxx-base64 | 37.19.198.244 |
| 74.64 | shadowsocks | 251.4 | 619.1 | 21.96 | 0.0 | 10.0 | 11.9 | 15.84 | Au1rxx-base64 | 156.146.38.169 |
| 74.23 | shadowsocks | 314.9 | 811.6 | 20.49 | 0.0 | 10.0 | 11.9 | 15.84 | Au1rxx-base64 | 37.19.198.243 |
| 72.25 | shadowsocks | 335.8 | 985.6 | 20.01 | 0.0 | 10.0 | 11.9 | 15.84 | Au1rxx-base64 | 172.234.202.34 |
| 71.5 | shadowsocks | 268.8 | 607.0 | 21.56 | 0.0 | 10.0 | 11.9 | 12.04 | mheidari-all | 198.98.53.130 |
| 70.57 | vless | 312.4 | 772.3 | 20.55 | 0.0 | 10.0 | 8.32 | 12.04 | mheidari-all | 47.253.226.114 |
| 70.14 | shadowsocks | 292.4 | 545.4 | 21.01 | 0.0 | 10.0 | 11.9 | 15.84 | Au1rxx-base64 | 173.244.56.9 |
| 69.61 | vless | 280.7 | 670.1 | 21.28 | 0.0 | 10.0 | 8.32 | 13.14 | Surfboard-tg-mixed | 104.25.161.29 |
| 69.22 | shadowsocks | 309.4 | 596.9 | 20.62 | 0.0 | 10.0 | 11.9 | 15.84 | Au1rxx-base64 | 108.181.0.177 |
| 68.87 | shadowsocks | 304.0 | 564.7 | 20.74 | 0.0 | 10.0 | 11.9 | 15.84 | Au1rxx-base64 | 173.244.56.6 |
| 68.34 | shadowsocks | 345.4 | 915.7 | 19.78 | 0.0 | 10.0 | 11.9 | 12.04 | mheidari-all | 108.181.57.93 |
| 68.26 | shadowsocks | 305.8 | 560.3 | 20.7 | 0.0 | 10.0 | 11.9 | 15.84 | Au1rxx-base64 | 108.181.118.10 |
| 67.18 | vless | 424.1 | 932.9 | 17.96 | 0.0 | 10.0 | 8.32 | 15.84 | Au1rxx-base64 | 15.204.97.214 |
| 67.16 | shadowsocks | 291.7 | 609.7 | 21.03 | 0.0 | 10.0 | 11.9 | 15.84 | Au1rxx-base64 | 216.105.168.18 |
| 65.92 | vless | 304.5 | 606.7 | 20.73 | 0.0 | 10.0 | 8.32 | 12.04 | mheidari-all | 107.173.237.146 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| Surfboard-tg-mixed | 0.831 | 0.752 | 339 | 5684 | prefer |
| Au1rxx-base64 | 0.79 | 0.794 | 68 | 108 | prefer |
| mheidari-all | 0.56 | 0.48 | 304 | 16042 | observe |
| DeltaKronecker-all | 0.39 | 0.309 | 350 | 7631 | observe |
| nscl5-all | 0.301 | 1.0 | 1 | 1162 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4308 | observe |
| Epodonios-all | 0.255 | None | 0 | 6523 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6669 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4186 | observe |
| barry-far-vless | 0.255 | None | 0 | 4744 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5331 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 197 |
| geo | TimeoutError | - | 155 |
| geo | ClientOSError | - | 61 |
| speed | TimeoutError | - | 41 |
| cn-block | TimeoutError | - | 12 |
| 204 | ClientOSError | - | 10 |
| 204 | ProxyError | - | 8 |
| cn-block | ClientOSError | - | 7 |
| 204 | TimeoutError | - | 4 |
| geo | ProxyError | - | 3 |
| cn-block | ProxyError | - | 2 |
| geo | status | 403 | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 269 | 300 | - |
| global | False | 290 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
