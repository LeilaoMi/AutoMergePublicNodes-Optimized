# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-17 19:22:49 |
| 运行耗时 | 269.1s |
| 订阅源总数 | 107 |
| 健康订阅源 | 99 |
| 原始节点 | 80102 |
| 去重后节点 | 25151 |
| TCP 可达 | 3000 |
| 真实可用 | 531 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 25151 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 3.3 |
| geo | 1.3 |
| tcp | 34.5 |
| probe | 61.4 |
| real_test | 138.9 |
| generate | 29.8 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 45778 |
| trojan | 13101 |
| vmess | 10823 |
| shadowsocks | 9883 |
| hysteria2 | 271 |
| shadowsocksr | 132 |
| socks | 52 |
| http | 51 |
| hysteria | 8 |
| tuic | 3 |

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
| 79.01 | shadowsocks | 206.8 | 514.2 | 22.99 | 0.0 | 10.0 | 11.36 | 18.66 | Au1rxx-base64 | 173.244.56.6 |
| 78.52 | shadowsocks | 206.3 | 492.6 | 23.0 | 0.0 | 10.0 | 11.36 | 18.66 | Au1rxx-base64 | 108.181.118.10 |
| 77.78 | shadowsocks | 260.2 | 634.5 | 21.76 | 0.0 | 10.0 | 11.36 | 18.66 | Au1rxx-base64 | 156.146.38.170 |
| 77.37 | shadowsocks | 257.2 | 632.0 | 21.82 | 0.0 | 10.0 | 11.36 | 18.66 | Au1rxx-base64 | 156.146.38.169 |
| 77.02 | shadowsocks | 202.4 | 510.0 | 23.09 | 0.0 | 10.0 | 11.36 | 18.66 | Au1rxx-base64 | 173.244.56.9 |
| 76.78 | shadowsocks | 303.2 | 747.3 | 20.76 | 0.0 | 10.0 | 11.36 | 18.66 | Au1rxx-base64 | 156.146.38.168 |
| 76.76 | shadowsocks | 282.4 | 729.1 | 21.24 | 0.0 | 10.0 | 11.36 | 18.66 | Au1rxx-base64 | 108.181.0.177 |
| 76.23 | shadowsocks | 302.4 | 758.0 | 20.78 | 0.0 | 10.0 | 11.36 | 18.66 | Au1rxx-base64 | 156.146.38.167 |
| 72.65 | trojan | 347.9 | 352.8 | 19.72 | 1.77 | 9.83 | 12.21 | 19.22 | mheidari-all | 18.183.224.87 |
| 72.61 | trojan | 344.0 | 344.5 | 19.82 | 2.08 | 9.9 | 12.21 | 18.66 | Au1rxx-base64 | 18.177.136.64 |
| 72.56 | trojan | 344.2 | 345.1 | 19.81 | 2.06 | 9.88 | 12.21 | 18.66 | Au1rxx-base64 | 18.183.164.154 |
| 72.5 | trojan | 344.2 | 348.3 | 19.81 | 1.94 | 9.88 | 12.21 | 18.66 | Au1rxx-base64 | 3.112.234.3 |
| 72.45 | trojan | 344.9 | 348.5 | 19.79 | 1.93 | 9.88 | 12.21 | 18.66 | Au1rxx-base64 | 18.183.149.237 |
| 72.39 | trojan | 344.0 | 350.8 | 19.81 | 1.85 | 9.89 | 12.21 | 18.66 | Au1rxx-base64 | 43.207.117.135 |
| 72.28 | trojan | 344.6 | 352.4 | 19.8 | 1.79 | 9.88 | 12.21 | 18.66 | Au1rxx-base64 | 13.230.252.28 |
| 72.27 | trojan | 349.5 | 351.3 | 19.69 | 1.83 | 9.9 | 12.21 | 18.66 | Au1rxx-base64 | 18.176.53.202 |
| 72.25 | trojan | 347.9 | 351.9 | 19.73 | 1.8 | 9.88 | 12.21 | 18.66 | Au1rxx-base64 | 13.231.189.62 |
| 72.1 | trojan | 348.0 | 355.7 | 19.72 | 1.66 | 9.89 | 12.21 | 18.66 | Au1rxx-base64 | 18.181.201.45 |
| 71.87 | trojan | 345.3 | 338.8 | 19.78 | 2.3 | 8.98 | 12.21 | 18.66 | Au1rxx-base64 | noble-tahr.rooster465.autos |
| 71.87 | trojan | 345.7 | 345.4 | 19.78 | 2.05 | 9.87 | 12.21 | 18.66 | Au1rxx-base64 | 35.77.91.8 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.976 | 1.0 | 36 | 61 | prefer |
| Au1rxx-base64 | 0.876 | 0.875 | 136 | 150 | prefer |
| Surfboard-tg-mixed | 0.835 | 0.759 | 145 | 5558 | prefer |
| mheidari-all | 0.833 | 0.755 | 318 | 16753 | prefer |
| xiaoji235-airport-v2ray-all | 0.322 | 1.0 | 1 | 1680 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4428 | observe |
| Epodonios-all | 0.255 | None | 0 | 6514 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6898 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4258 | observe |
| barry-far-vless | 0.255 | None | 0 | 4875 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5263 | observe |
| nscl5-all | 0.248 | None | 0 | 1821 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 134 |
| speed | ClientOSError | - | 52 |
| cn-block | TimeoutError | - | 15 |
| 204 | ProxyError | - | 12 |
| cn-block | ClientOSError | - | 10 |
| 204 | TimeoutError | - | 9 |
| speed | TimeoutError | - | 9 |
| 204 | ClientOSError | - | 8 |
| geo | ClientOSError | - | 7 |
| cn-block | ProxyError | - | 5 |
| speed | ProxyError | - | 4 |
| geo | ProxyError | - | 2 |
| speed | ClientPayloadError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
