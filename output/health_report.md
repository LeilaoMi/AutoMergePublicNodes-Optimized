# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-19 04:59:03 |
| 运行耗时 | 342.2s |
| 订阅源总数 | 107 |
| 健康订阅源 | 93 |
| 原始节点 | 97393 |
| 去重后节点 | 27778 |
| TCP 可达 | 3000 |
| 真实可用 | 511 |
| Verified 输出 | 118 |
| Global 输出 | 300 |
| All 输出 | 27778 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.9 |
| geo | 1.5 |
| tcp | 86.3 |
| probe | 94.1 |
| real_test | 100.9 |
| china_check | 36.9 |
| write_verified | 0.1 |
| generate | 14.6 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 56587 |
| vmess | 16660 |
| shadowsocks | 11778 |
| trojan | 9734 |
| hysteria2 | 1583 |
| http | 761 |
| shadowsocksr | 167 |
| socks | 71 |
| anytls | 29 |
| hysteria | 17 |
| tuic | 6 |

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
| 96.77 | vless | 198.2 | 3.0 | 23.19 | 14.89 | 10.0 | 10.85 | 17.84 | Au1rxx-base64 | 45.63.53.81 |
| 95.67 | vless | 248.8 | 1.2 | 22.02 | 14.96 | 10.0 | 10.85 | 17.84 | Au1rxx-base64 | 44.248.233.99 |
| 95.03 | shadowsocks | 229.4 | 3.6 | 22.47 | 14.86 | 10.0 | 13.86 | 17.84 | Au1rxx-base64 | 173.244.56.6 |
| 94.0 | vless | 222.9 | 0.8 | 22.62 | 14.97 | 7.72 | 10.85 | 17.84 | Au1rxx-base64 | 95.111.212.241 |
| 93.88 | vless | 215.5 | 10.6 | 22.79 | 14.6 | 7.8 | 10.85 | 17.84 | Au1rxx-base64 | 195.123.240.65 |
| 92.64 | vless | 369.0 | 7.6 | 19.24 | 14.71 | 10.0 | 10.85 | 17.84 | Au1rxx-base64 | 51.81.203.63 |
| 92.42 | hysteria2 | 354.8 | 16.6 | 19.56 | 14.38 | 9.76 | 12.86 | 17.84 | Au1rxx-base64 | 66.94.121.46 |
| 92.21 | vless | 197.9 | 9.5 | 23.2 | 14.65 | 10.0 | 10.85 | 17.84 | Au1rxx-base64 | 67.209.184.133 |
| 92.21 | shadowsocks | 332.3 | 2.2 | 20.09 | 14.92 | 10.0 | 13.86 | 17.84 | Au1rxx-base64 | 103.11.76.248 |
| 91.22 | vless | 189.6 | 1.0 | 23.39 | 14.96 | 7.83 | 10.85 | 17.84 | Au1rxx-base64 | 131.143.180.87 |
| 90.87 | shadowsocks | 293.1 | 3.6 | 20.99 | 14.87 | 10.0 | 13.86 | 17.84 | Au1rxx-base64 | 156.146.38.167 |
| 90.57 | shadowsocks | 296.3 | 2.8 | 20.92 | 14.89 | 10.0 | 13.86 | 17.84 | Au1rxx-base64 | 156.146.38.168 |
| 90.21 | shadowsocks | 249.3 | 0.2 | 22.01 | 14.99 | 7.03 | 13.86 | 17.84 | Au1rxx-base64 | 149.22.95.183 |
| 89.88 | shadowsocks | 297.0 | 8.4 | 20.9 | 14.68 | 10.0 | 13.86 | 17.84 | Au1rxx-base64 | 156.146.38.170 |
| 89.59 | http | 204.2 | 0.7 | 23.05 | 14.97 | 0.0 | 14.59 | 19.98 | ermaozi | 138.199.35.218 |
| 89.52 | http | 207.4 | 0.7 | 22.98 | 14.97 | 0.0 | 14.59 | 19.98 | ermaozi | 138.199.35.215 |
| 89.5 | http | 207.1 | 1.3 | 22.98 | 14.95 | 0.0 | 14.59 | 19.98 | ermaozi | 138.199.35.198 |
| 89.49 | http | 208.0 | 1.0 | 22.96 | 14.96 | 0.0 | 14.59 | 19.98 | ermaozi | 138.199.35.214 |
| 89.05 | http | 242.4 | 5.1 | 22.17 | 14.81 | 0.0 | 14.59 | 19.98 | ermaozi | 172.64.68.89 |
| 88.82 | http | 215.6 | 14.3 | 22.79 | 14.46 | 0.0 | 14.59 | 19.98 | ermaozi | 138.199.35.216 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.999 | 0.98 | 101 | 696 | prefer |
| Au1rxx-base64 | 0.918 | 0.851 | 436 | 1726 | prefer |
| DeltaKronecker-all | 0.557 | 1.0 | 6 | 4750 | observe |
| Surfboard-tg-mixed | 0.489 | 0.833 | 6 | 7003 | observe |
| mheidari-all | 0.323 | 0.239 | 134 | 23518 | observe |
| 10ium-HighSpeed | 0.289 | 1.0 | 1 | 839 | observe |
| roosterkid-openproxylist-v2ray | 0.261 | 1.0 | 1 | 150 | observe |
| Epodonios-all | 0.255 | None | 0 | 7467 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9822 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5523 | observe |
| barry-far-vless | 0.255 | None | 0 | 5700 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4246 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 117 |
| geo | ClientOSError | - | 19 |
| speed | ClientOSError | - | 15 |
| 204 | ClientOSError | - | 6 |
| cn-block | ClientOSError | - | 4 |
| 204 | ProxyError | - | 3 |
| cn-block | TimeoutError | - | 3 |
| geo | TimeoutError | - | 3 |
| cn-block | ProxyError | - | 1 |
| 204 | TimeoutError | - | 1 |
| geo | ProxyError | - | 1 |
| speed | ClientPayloadError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 143 | 118 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
