# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-03 14:24:12 |
| 运行耗时 | 180.6s |
| 订阅源总数 | 107 |
| 健康订阅源 | 103 |
| 原始节点 | 77345 |
| 去重后节点 | 22900 |
| TCP 可达 | 3000 |
| 真实可用 | 295 |
| Verified 输出 | 295 |
| Global 输出 | 300 |
| All 输出 | 22900 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.1 |
| geo | 1.6 |
| tcp | 30.9 |
| probe | 44.2 |
| real_test | 81.1 |
| generate | 18.6 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 45029 |
| trojan | 12153 |
| vmess | 10373 |
| shadowsocks | 9190 |
| hysteria2 | 237 |
| shadowsocksr | 147 |
| http | 135 |
| socks | 74 |
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
| 74.83 | shadowsocks | 257.3 | 634.4 | 21.82 | 0.0 | 10.0 | 12.19 | 14.82 | Au1rxx-base64 | 156.146.38.169 |
| 74.81 | shadowsocks | 258.2 | 627.8 | 21.8 | 0.0 | 10.0 | 12.19 | 14.82 | Au1rxx-base64 | 156.146.38.170 |
| 74.66 | shadowsocks | 264.8 | 652.3 | 21.65 | 0.0 | 10.0 | 12.19 | 14.82 | Au1rxx-base64 | 37.19.198.160 |
| 74.58 | shadowsocks | 268.2 | 667.5 | 21.57 | 0.0 | 10.0 | 12.19 | 14.82 | Au1rxx-base64 | 37.19.198.243 |
| 73.94 | shadowsocks | 246.9 | 606.4 | 22.06 | 0.0 | 10.0 | 12.19 | 14.82 | Au1rxx-base64 | 156.146.38.167 |
| 73.34 | trojan | 303.3 | 707.8 | 20.76 | 0.0 | 10.0 | 11.3 | 15.32 | DeltaKronecker-all | 64.94.95.117 |
| 73.12 | shadowsocks | 271.4 | 662.0 | 21.5 | 0.0 | 10.0 | 12.19 | 14.82 | Au1rxx-base64 | 37.19.198.236 |
| 72.43 | trojan | 380.4 | 959.2 | 18.97 | 0.0 | 10.0 | 11.3 | 15.32 | DeltaKronecker-all | 64.94.95.114 |
| 72.33 | trojan | 349.2 | 850.4 | 19.69 | 0.0 | 10.0 | 11.3 | 15.32 | DeltaKronecker-all | 64.94.95.115 |
| 70.75 | vless | 281.7 | 670.0 | 21.26 | 0.0 | 10.0 | 6.61 | 15.32 | DeltaKronecker-all | 198.41.209.87 |
| 70.56 | vless | 307.0 | 737.3 | 20.67 | 0.0 | 10.0 | 6.61 | 15.32 | DeltaKronecker-all | 46.8.98.55 |
| 70.15 | vless | 284.1 | 669.9 | 21.2 | 0.0 | 10.0 | 6.61 | 15.32 | DeltaKronecker-all | 104.17.238.33 |
| 69.9 | shadowsocks | 254.3 | 619.2 | 21.89 | 0.0 | 10.0 | 12.19 | 14.82 | Au1rxx-base64 | 156.146.38.168 |
| 69.81 | vless | 285.7 | 666.7 | 21.17 | 0.0 | 10.0 | 6.61 | 15.32 | DeltaKronecker-all | 162.159.252.15 |
| 69.54 | vless | 286.0 | 672.0 | 21.16 | 0.0 | 10.0 | 6.61 | 15.32 | DeltaKronecker-all | 104.19.142.226 |
| 69.5 | shadowsocks | 311.5 | 605.5 | 20.57 | 0.0 | 10.0 | 12.19 | 14.82 | Au1rxx-base64 | 149.22.95.183 |
| 69.41 | vless | 295.1 | 679.3 | 20.95 | 0.0 | 10.0 | 6.61 | 15.32 | DeltaKronecker-all | 104.25.161.29 |
| 69.38 | shadowsocks | 296.8 | 553.4 | 20.91 | 0.0 | 10.0 | 12.19 | 14.82 | Au1rxx-base64 | 173.244.56.9 |
| 69.21 | shadowsocks | 302.2 | 594.7 | 20.78 | 0.0 | 10.0 | 12.19 | 14.82 | Au1rxx-base64 | 108.181.0.177 |
| 68.78 | shadowsocks | 331.7 | 660.7 | 20.1 | 0.0 | 10.0 | 12.19 | 14.82 | Au1rxx-base64 | 173.244.56.6 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| Au1rxx-base64 | 0.843 | 0.87 | 23 | 79 | prefer |
| Surfboard-tg-mixed | 0.767 | 0.691 | 94 | 5871 | prefer |
| mheidari-all | 0.622 | 0.667 | 15 | 16032 | observe |
| DeltaKronecker-all | 0.593 | 0.513 | 312 | 6997 | observe |
| nscl5-all | 0.403 | 1.0 | 3 | 1114 | observe |
| tg-ConfigV2rayNG | 0.263 | 1.0 | 1 | 200 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4368 | observe |
| Epodonios-all | 0.255 | None | 0 | 6926 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7164 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4477 | observe |
| barry-far-vless | 0.255 | None | 0 | 5041 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5372 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 88 |
| geo | TimeoutError | - | 37 |
| 204 | ProxyError | - | 13 |
| 204 | ClientOSError | - | 8 |
| cn-block | ProxyError | - | 7 |
| geo | ProxyError | - | 7 |
| speed | ProxyError | - | 6 |
| cn-block | ClientOSError | - | 5 |
| geo | ClientOSError | - | 5 |
| 204 | TimeoutError | - | 5 |
| cn-block | TimeoutError | - | 5 |
| speed | TimeoutError | - | 3 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 295 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
