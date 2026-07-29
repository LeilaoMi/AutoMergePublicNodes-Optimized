# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-29 08:54:20 |
| 运行耗时 | 345.1s |
| 订阅源总数 | 107 |
| 健康订阅源 | 100 |
| 原始节点 | 77964 |
| 去重后节点 | 22464 |
| TCP 可达 | 3000 |
| 真实可用 | 606 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22464 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 3.7 |
| geo | 1.3 |
| tcp | 31.8 |
| probe | 72.6 |
| real_test | 202.7 |
| generate | 33.0 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 45823 |
| shadowsocks | 10689 |
| trojan | 10522 |
| vmess | 10159 |
| hysteria2 | 501 |
| http | 98 |
| shadowsocksr | 75 |
| socks | 56 |
| anytls | 26 |
| hysteria | 12 |
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
| 82.18 | hysteria2 | 356.9 | 842.5 | 19.52 | 0.0 | 10.0 | 14.12 | 19.64 | Au1rxx-base64 | 159.223.157.129 |
| 81.69 | shadowsocks | 234.4 | 581.7 | 22.35 | 0.0 | 10.0 | 13.7 | 19.64 | Au1rxx-base64 | 156.146.38.167 |
| 80.1 | shadowsocks | 289.9 | 684.3 | 21.07 | 0.0 | 10.0 | 13.7 | 19.64 | Au1rxx-base64 | 37.19.198.243 |
| 80.08 | shadowsocks | 260.7 | 658.5 | 21.74 | 0.0 | 10.0 | 13.7 | 19.64 | Au1rxx-base64 | 156.146.38.168 |
| 79.96 | shadowsocks | 309.4 | 805.6 | 20.62 | 0.0 | 10.0 | 13.7 | 19.64 | Au1rxx-base64 | 156.146.38.169 |
| 79.74 | trojan | 357.0 | 783.8 | 19.51 | 0.0 | 10.0 | 13.65 | 19.64 | Au1rxx-base64 | 64.94.95.115 |
| 78.52 | shadowsocks | 281.8 | 655.5 | 21.25 | 0.0 | 10.0 | 13.7 | 19.64 | Au1rxx-base64 | 37.19.198.244 |
| 78.46 | shadowsocks | 330.6 | 873.8 | 20.12 | 0.0 | 10.0 | 13.7 | 19.64 | Au1rxx-base64 | 156.146.38.170 |
| 78.32 | shadowsocks | 298.2 | 716.3 | 20.87 | 0.0 | 10.0 | 13.7 | 19.64 | Au1rxx-base64 | 37.19.198.236 |
| 78.16 | shadowsocks | 358.7 | 885.3 | 19.47 | 0.0 | 10.0 | 13.7 | 19.64 | Au1rxx-base64 | 37.19.198.160 |
| 77.6 | trojan | 312.3 | 726.3 | 20.55 | 0.0 | 10.0 | 13.65 | 19.64 | Au1rxx-base64 | 153.75.250.171 |
| 76.05 | trojan | 400.8 | 1043.2 | 18.5 | 0.0 | 10.0 | 13.65 | 19.64 | Au1rxx-base64 | 148.72.168.35 |
| 76.0 | shadowsocks | 288.5 | 564.9 | 21.1 | 0.0 | 10.0 | 13.7 | 19.64 | Au1rxx-base64 | 108.181.0.177 |
| 75.95 | shadowsocks | 252.9 | 538.0 | 21.92 | 0.0 | 10.0 | 13.7 | 19.64 | Au1rxx-base64 | 185.236.200.210 |
| 75.86 | shadowsocks | 312.5 | 736.4 | 20.54 | 0.0 | 10.0 | 13.7 | 19.64 | Au1rxx-base64 | 108.181.57.93 |
| 75.85 | shadowsocks | 289.7 | 576.7 | 21.07 | 0.0 | 10.0 | 13.7 | 19.64 | Au1rxx-base64 | 108.181.118.10 |
| 75.54 | trojan | 541.3 | 1485.7 | 15.25 | 0.0 | 10.0 | 13.65 | 19.64 | Au1rxx-base64 | 64.94.95.114 |
| 75.37 | shadowsocks | 356.5 | 934.5 | 19.53 | 0.0 | 10.0 | 13.7 | 19.64 | Au1rxx-base64 | 156.146.38.195 |
| 75.37 | trojan | 476.9 | 1252.6 | 16.74 | 0.0 | 10.0 | 13.65 | 19.64 | Au1rxx-base64 | 163.245.196.68 |
| 75.24 | shadowsocks | 369.8 | 882.2 | 19.22 | 0.0 | 10.0 | 13.7 | 19.64 | Au1rxx-base64 | 185.196.61.82 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.996 | 1.0 | 95 | 167 | prefer |
| Au1rxx-base64 | 0.887 | 0.84 | 257 | 1232 | prefer |
| Surfboard-tg-mixed | 0.446 | 0.625 | 8 | 5706 | observe |
| DeltaKronecker-all | 0.436 | 0.356 | 801 | 5519 | observe |
| mheidari-all | 0.305 | 0.3 | 10 | 15942 | observe |
| xiaoji235-airport-v2ray-all | 0.282 | 0.5 | 2 | 1861 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| Epodonios-all | 0.255 | None | 0 | 6451 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3973 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6039 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4505 | observe |
| barry-far-vless | 0.255 | None | 0 | 4902 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5089 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| nscl5-all | 0.246 | None | 0 | 1774 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 215 |
| speed | ClientOSError | - | 91 |
| 204 | ProxyError | - | 65 |
| speed | TimeoutError | - | 64 |
| geo | ClientOSError | - | 46 |
| cn-block | TimeoutError | - | 29 |
| cn-block | ProxyError | - | 20 |
| 204 | TimeoutError | - | 19 |
| cn-block | ClientOSError | - | 6 |
| 204 | ClientOSError | - | 6 |
| geo | ProxyError | - | 6 |
| speed | ProxyError | - | 3 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
