# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-01 20:07:17 |
| 运行耗时 | 237.3s |
| 订阅源总数 | 107 |
| 健康订阅源 | 103 |
| 原始节点 | 77093 |
| 去重后节点 | 23359 |
| TCP 可达 | 3000 |
| 真实可用 | 269 |
| Verified 输出 | 269 |
| Global 输出 | 290 |
| All 输出 | 23359 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.8 |
| geo | 1.3 |
| tcp | 31.2 |
| probe | 55.1 |
| real_test | 97.9 |
| generate | 46.9 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 43507 |
| trojan | 13331 |
| vmess | 10487 |
| shadowsocks | 9171 |
| hysteria2 | 249 |
| shadowsocksr | 155 |
| http | 135 |
| socks | 51 |
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
| 77.59 | shadowsocks | 230.0 | 504.6 | 22.45 | 0.0 | 10.0 | 12.22 | 16.92 | Au1rxx-base64 | 173.244.56.9 |
| 74.52 | shadowsocks | 269.5 | 628.9 | 21.54 | 0.0 | 10.0 | 12.22 | 16.92 | Au1rxx-base64 | 173.244.56.6 |
| 73.86 | vless | 311.3 | 813.1 | 20.57 | 0.0 | 10.0 | 6.37 | 16.92 | Au1rxx-base64 | 15.204.97.214 |
| 73.13 | shadowsocks | 291.9 | 649.7 | 21.02 | 0.0 | 10.0 | 12.22 | 16.92 | Au1rxx-base64 | 156.146.38.168 |
| 72.67 | shadowsocks | 296.1 | 670.1 | 20.92 | 0.0 | 10.0 | 12.22 | 16.92 | Au1rxx-base64 | 156.146.38.169 |
| 72.3 | shadowsocks | 295.2 | 669.9 | 20.94 | 0.0 | 10.0 | 12.22 | 16.92 | Au1rxx-base64 | 156.146.38.167 |
| 71.32 | shadowsocks | 299.6 | 660.8 | 20.84 | 0.0 | 10.0 | 12.22 | 16.92 | Au1rxx-base64 | 156.146.38.170 |
| 71.09 | shadowsocks | 489.5 | 1352.2 | 16.45 | 0.0 | 10.0 | 12.22 | 16.92 | Au1rxx-base64 | 108.181.118.10 |
| 71.02 | shadowsocks | 492.4 | 1355.6 | 16.38 | 0.0 | 10.0 | 12.22 | 16.92 | Au1rxx-base64 | 108.181.0.177 |
| 70.94 | shadowsocks | 296.3 | 344.8 | 20.92 | 2.07 | 9.93 | 12.22 | 16.92 | Au1rxx-base64 | 149.22.87.241 |
| 70.05 | shadowsocks | 300.1 | 365.0 | 20.83 | 1.31 | 9.93 | 12.22 | 16.92 | Au1rxx-base64 | 149.22.87.204 |
| 69.8 | shadowsocks | 171.1 | 467.5 | 23.82 | 0.0 | 10.0 | 12.22 | 9.86 | DeltaKronecker-all | 107.172.219.230 |
| 68.89 | vless | 171.9 | 476.9 | 23.8 | 0.0 | 10.0 | 6.37 | 13.72 | Surfboard-tg-mixed | 64.23.143.23 |
| 68.65 | shadowsocks | 368.3 | 733.7 | 19.25 | 0.0 | 10.0 | 12.22 | 16.92 | Au1rxx-base64 | 37.19.198.243 |
| 68.36 | shadowsocks | 372.1 | 726.4 | 19.16 | 0.0 | 10.0 | 12.22 | 16.92 | Au1rxx-base64 | 37.19.198.236 |
| 68.21 | shadowsocks | 370.0 | 738.1 | 19.21 | 0.0 | 10.0 | 12.22 | 16.92 | Au1rxx-base64 | 37.19.198.160 |
| 68.21 | shadowsocks | 376.8 | 765.2 | 19.06 | 0.0 | 10.0 | 12.22 | 16.92 | Au1rxx-base64 | 37.19.198.244 |
| 67.51 | trojan | 226.3 | 474.5 | 22.54 | 0.0 | 10.0 | 9.97 | 13.72 | Surfboard-tg-mixed | 45.131.4.115 |
| 67.18 | vmess | 192.6 | 490.0 | 23.32 | 0.0 | 10.0 | 13.12 | 5.24 | Barabama-yudou | 82.198.246.233 |
| 65.77 | shadowsocks | 445.1 | 1057.3 | 17.47 | 0.0 | 10.0 | 12.22 | 16.92 | Au1rxx-base64 | 172.234.202.34 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| Au1rxx-base64 | 0.792 | 0.8 | 50 | 82 | prefer |
| Surfboard-tg-mixed | 0.657 | 0.577 | 220 | 5816 | observe |
| mheidari-all | 0.602 | 0.523 | 65 | 16033 | observe |
| DeltaKronecker-all | 0.35 | 0.265 | 113 | 7631 | observe |
| nscl5-all | 0.3 | 1.0 | 1 | 1113 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4308 | observe |
| Epodonios-all | 0.255 | None | 0 | 6737 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3975 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6642 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4378 | observe |
| barry-far-vless | 0.255 | None | 0 | 4858 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5331 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 101 |
| 204 | TimeoutError | - | 25 |
| 204 | ProxyError | - | 22 |
| cn-block | TimeoutError | - | 17 |
| 204 | ClientOSError | - | 15 |
| cn-block | ClientOSError | - | 11 |
| geo | TimeoutError | - | 11 |
| cn-block | ProxyError | - | 7 |
| geo | ClientOSError | - | 7 |
| geo | ProxyError | - | 4 |
| speed | TimeoutError | - | 3 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 269 | - |
| global | False | 300 | 290 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
