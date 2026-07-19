# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-19 13:41:44 |
| 运行耗时 | 330.2s |
| 订阅源总数 | 107 |
| 健康订阅源 | 100 |
| 原始节点 | 86572 |
| 去重后节点 | 23745 |
| TCP 可达 | 3000 |
| 真实可用 | 444 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23745 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.9 |
| geo | 0.8 |
| tcp | 34.1 |
| probe | 66.4 |
| real_test | 178.5 |
| generate | 44.6 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 49317 |
| trojan | 15519 |
| vmess | 10827 |
| shadowsocks | 10266 |
| hysteria2 | 394 |
| shadowsocksr | 124 |
| http | 55 |
| socks | 47 |
| hysteria | 15 |
| tuic | 7 |
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
| 78.03 | shadowsocks | 250.8 | 612.0 | 21.97 | 0.0 | 10.0 | 12.98 | 17.08 | Au1rxx-base64 | 156.146.38.167 |
| 77.99 | shadowsocks | 252.5 | 623.0 | 21.93 | 0.0 | 10.0 | 12.98 | 17.08 | Au1rxx-base64 | 198.98.53.130 |
| 77.87 | shadowsocks | 257.7 | 639.1 | 21.81 | 0.0 | 10.0 | 12.98 | 17.08 | Au1rxx-base64 | 156.146.38.168 |
| 77.72 | shadowsocks | 264.2 | 662.4 | 21.66 | 0.0 | 10.0 | 12.98 | 17.08 | Au1rxx-base64 | 37.19.198.236 |
| 77.66 | shadowsocks | 266.8 | 675.5 | 21.6 | 0.0 | 10.0 | 12.98 | 17.08 | Au1rxx-base64 | 37.19.198.243 |
| 77.66 | shadowsocks | 267.0 | 676.0 | 21.6 | 0.0 | 10.0 | 12.98 | 17.08 | Au1rxx-base64 | 37.19.198.244 |
| 77.5 | vmess | 322.9 | 858.4 | 20.3 | 0.0 | 10.0 | 13.12 | 18.58 | Surfboard-tg-mixed | 67.220.95.3 |
| 77.1 | shadowsocks | 250.5 | 619.4 | 21.98 | 0.0 | 10.0 | 12.98 | 17.08 | Au1rxx-base64 | 156.146.38.169 |
| 76.84 | shadowsocks | 302.3 | 775.0 | 20.78 | 0.0 | 10.0 | 12.98 | 17.08 | Au1rxx-base64 | 37.19.198.160 |
| 76.66 | shadowsocks | 283.5 | 682.8 | 21.22 | 0.0 | 10.0 | 12.98 | 17.08 | Au1rxx-base64 | 108.181.57.93 |
| 75.48 | shadowsocks | 339.7 | 884.4 | 19.92 | 0.0 | 10.0 | 12.98 | 17.08 | Au1rxx-base64 | 185.196.61.82 |
| 74.87 | shadowsocks | 249.1 | 609.9 | 22.01 | 0.0 | 10.0 | 12.98 | 17.08 | Au1rxx-base64 | 156.146.38.170 |
| 72.56 | shadowsocks | 300.3 | 624.3 | 20.83 | 0.0 | 10.0 | 12.98 | 17.08 | Au1rxx-base64 | 149.22.95.183 |
| 72.52 | shadowsocks | 302.0 | 578.7 | 20.79 | 0.0 | 10.0 | 12.98 | 17.08 | Au1rxx-base64 | 173.244.56.6 |
| 72.19 | shadowsocks | 287.3 | 540.6 | 21.13 | 0.0 | 10.0 | 12.98 | 17.08 | Au1rxx-base64 | 108.181.0.177 |
| 71.34 | shadowsocks | 304.1 | 547.4 | 20.74 | 0.0 | 10.0 | 12.98 | 17.08 | Au1rxx-base64 | 108.181.118.10 |
| 70.94 | shadowsocks | 297.3 | 556.7 | 20.89 | 0.0 | 10.0 | 12.98 | 17.08 | Au1rxx-base64 | 173.244.56.9 |
| 70.75 | shadowsocks | 307.3 | 763.4 | 20.67 | 0.0 | 10.0 | 12.98 | 17.08 | Au1rxx-base64 | 147.90.234.133 |
| 70.27 | trojan | 355.6 | 509.9 | 19.55 | 0.0 | 10.0 | 13.86 | 18.58 | Surfboard-tg-mixed | 198.177.57.9 |
| 70.15 | shadowsocks | 324.7 | 891.2 | 20.26 | 0.0 | 10.0 | 12.98 | 17.08 | Au1rxx-base64 | 50.114.177.235 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.976 | 1.0 | 36 | 61 | prefer |
| Au1rxx-base64 | 0.868 | 0.826 | 213 | 1124 | prefer |
| mheidari-all | 0.756 | 0.679 | 109 | 20221 | prefer |
| Surfboard-tg-mixed | 0.463 | 0.382 | 204 | 5306 | observe |
| xiaoji235-airport-v2ray-all | 0.438 | 1.0 | 3 | 4642 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4478 | observe |
| Epodonios-all | 0.255 | None | 0 | 6635 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3973 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6812 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4184 | observe |
| barry-far-vless | 0.255 | None | 0 | 4858 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5355 | observe |
| nscl5-all | 0.255 | None | 0 | 2755 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 408 |
| speed | ClientOSError | - | 154 |
| geo | ClientOSError | - | 75 |
| cn-block | TimeoutError | - | 34 |
| 204 | TimeoutError | - | 21 |
| 204 | ProxyError | - | 17 |
| speed | TimeoutError | - | 9 |
| 204 | ClientOSError | - | 8 |
| cn-block | ClientOSError | - | 6 |
| cn-block | ProxyError | - | 5 |
| geo | ProxyError | - | 3 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
