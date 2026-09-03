# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-03 16:15:56 |
| 运行耗时 | 282.9s |
| 订阅源总数 | 107 |
| 健康订阅源 | 95 |
| 原始节点 | 82139 |
| 去重后节点 | 22600 |
| TCP 可达 | 3000 |
| 真实可用 | 554 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22600 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.4 |
| geo | 1.6 |
| tcp | 36.9 |
| probe | 84.5 |
| real_test | 112.2 |
| generate | 41.4 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 51269 |
| vmess | 11465 |
| shadowsocks | 9821 |
| trojan | 7614 |
| hysteria2 | 1603 |
| http | 140 |
| shadowsocksr | 130 |
| socks | 75 |
| tuic | 11 |
| hysteria | 10 |
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
| 85.15 | vless | 171.4 | 475.7 | 23.81 | 0.0 | 10.0 | 11.82 | 19.52 | Au1rxx-base64 | 74.207.245.124 |
| 85.14 | vless | 172.0 | 475.5 | 23.8 | 0.0 | 10.0 | 11.82 | 19.52 | Au1rxx-base64 | 45.33.107.237 |
| 85.09 | vless | 174.1 | 487.7 | 23.75 | 0.0 | 10.0 | 11.82 | 19.52 | Au1rxx-base64 | 45.79.103.108 |
| 84.98 | vless | 178.7 | 482.8 | 23.64 | 0.0 | 10.0 | 11.82 | 19.52 | Au1rxx-base64 | 50.116.9.184 |
| 84.58 | vless | 195.9 | 486.4 | 23.24 | 0.0 | 10.0 | 11.82 | 19.52 | Au1rxx-base64 | 192.155.87.188 |
| 84.55 | vless | 197.4 | 492.0 | 23.21 | 0.0 | 10.0 | 11.82 | 19.52 | Au1rxx-base64 | 31.58.50.200 |
| 84.4 | vless | 203.9 | 528.0 | 23.06 | 0.0 | 10.0 | 11.82 | 19.52 | Au1rxx-base64 | 172.233.139.46 |
| 84.39 | vless | 204.2 | 506.8 | 23.05 | 0.0 | 10.0 | 11.82 | 19.52 | Au1rxx-base64 | 172.233.156.118 |
| 84.36 | vless | 205.7 | 534.5 | 23.02 | 0.0 | 10.0 | 11.82 | 19.52 | Au1rxx-base64 | 172.236.252.35 |
| 84.26 | hysteria2 | 211.7 | 520.8 | 22.88 | 0.0 | 10.0 | 12.86 | 19.52 | Au1rxx-base64 | 66.94.121.46 |
| 84.2 | vless | 212.4 | 480.6 | 22.86 | 0.0 | 10.0 | 11.82 | 19.52 | Au1rxx-base64 | 172.239.67.231 |
| 84.11 | vless | 216.1 | 498.0 | 22.77 | 0.0 | 10.0 | 11.82 | 19.52 | Au1rxx-base64 | 172.239.67.156 |
| 84.08 | vless | 217.5 | 517.4 | 22.74 | 0.0 | 10.0 | 11.82 | 19.52 | Au1rxx-base64 | 172.235.43.210 |
| 84.04 | vless | 219.2 | 485.8 | 22.7 | 0.0 | 10.0 | 11.82 | 19.52 | Au1rxx-base64 | 172.235.38.85 |
| 82.31 | vless | 294.2 | 589.5 | 20.97 | 0.0 | 10.0 | 11.82 | 19.52 | Au1rxx-base64 | 172.233.156.123 |
| 82.14 | shadowsocks | 222.1 | 519.4 | 22.64 | 0.0 | 10.0 | 13.98 | 19.52 | Au1rxx-base64 | 149.22.95.183 |
| 82.01 | vless | 172.2 | 481.0 | 23.79 | 0.0 | 10.0 | 11.82 | 16.4 | Surfboard-tg-mixed | 173.255.242.235 |
| 81.06 | vless | 295.7 | 787.2 | 20.93 | 0.0 | 8.79 | 11.82 | 19.52 | Au1rxx-base64 | us3.i13.bid |
| 80.2 | vless | 250.4 | 486.4 | 21.98 | 0.0 | 10.0 | 11.82 | 16.4 | Surfboard-tg-mixed | 172.233.156.42 |
| 80.12 | vless | 172.9 | 472.3 | 23.78 | 0.0 | 10.0 | 11.82 | 19.52 | Au1rxx-base64 | 45.33.62.166 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | 0.946 | 334 | 1770 | prefer |
| zhangkai | 0.915 | 0.95 | 20 | 144 | prefer |
| mheidari-all | 0.893 | 0.819 | 105 | 15770 | prefer |
| DeltaKronecker-all | 0.875 | 0.889 | 18 | 6335 | prefer |
| Surfboard-tg-mixed | 0.807 | 0.73 | 152 | 7139 | prefer |
| tg-oneclickvpnkeys | 0.406 | 1.0 | 4 | 145 | observe |
| SoliSpirit-all | 0.335 | 1.0 | 1 | 7991 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4671 | observe |
| Epodonios-all | 0.255 | None | 0 | 7586 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 6006 | observe |
| barry-far-vless | 0.255 | None | 0 | 6219 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4081 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| cn-block | TimeoutError | - | 17 |
| geo | ClientOSError | - | 16 |
| 204 | TimeoutError | - | 16 |
| 204 | ProxyError | - | 9 |
| speed | ClientOSError | - | 9 |
| speed | TimeoutError | - | 4 |
| cn-block | ClientOSError | - | 4 |
| 204 | ClientOSError | - | 3 |
| geo | TimeoutError | - | 2 |
| 204 | ProxyConnectionError | - | 1 |
| cn-block | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
