# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-11-18 20:46:24 |
| 运行耗时 | 263.7s |
| 订阅源总数 | 107 |
| 健康订阅源 | 87 |
| 原始节点 | 82675 |
| 去重后节点 | 27633 |
| TCP 可达 | 3000 |
| 真实可用 | 361 |
| Verified 输出 | 35 |
| Global 输出 | 300 |
| All 输出 | 27633 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.2 |
| geo | 1.4 |
| tcp | 69.6 |
| probe | 69.1 |
| real_test | 71.9 |
| china_check | 37.4 |
| write_verified | 0.0 |
| generate | 9.1 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 48895 |
| vmess | 14922 |
| shadowsocks | 10107 |
| trojan | 6883 |
| hysteria2 | 1495 |
| shadowsocksr | 153 |
| http | 112 |
| socks | 67 |
| hysteria | 16 |
| anytls | 13 |
| tuic | 12 |

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
| 90.13 | shadowsocks | 265.9 | 0.1 | 21.62 | 14.99 | 10.0 | 13.62 | 16.38 | Au1rxx-base64 | 95.215.201.18 |
| 88.79 | shadowsocks | 210.2 | 3.2 | 22.91 | 14.88 | 10.0 | 13.62 | 16.38 | Au1rxx-base64 | 149.22.95.183 |
| 87.83 | trojan | 282.7 | 3.5 | 21.23 | 14.87 | 9.21 | 11.69 | 16.38 | Au1rxx-base64 | 66.163.112.242 |
| 87.8 | vless | 297.7 | 4.3 | 20.89 | 14.84 | 7.94 | 10.47 | 16.38 | Au1rxx-base64 | 45.63.53.81 |
| 87.08 | trojan | 279.4 | 1.6 | 21.31 | 14.94 | 8.09 | 11.69 | 16.38 | Au1rxx-base64 | 66.163.112.13 |
| 86.42 | trojan | 283.0 | 2.7 | 21.23 | 14.9 | 8.09 | 11.69 | 16.38 | Au1rxx-base64 | 66.163.112.76 |
| 86.28 | hysteria2 | 243.0 | 2.0 | 22.15 | 14.92 | 2.04 | 11.79 | 16.38 | Au1rxx-base64 | 66.94.121.46 |
| 86.22 | trojan | 294.6 | 3.3 | 20.96 | 14.88 | 10.0 | 11.69 | 16.38 | Au1rxx-base64 | 66.163.112.121 |
| 85.46 | shadowsocks | 222.1 | 2.1 | 22.64 | 14.92 | 0.0 | 13.62 | 19.14 | Surfboard-tg-mixed | 38.145.220.193 |
| 84.41 | shadowsocks | 285.1 | 0.9 | 21.18 | 14.97 | 0.0 | 13.62 | 19.14 | Surfboard-tg-mixed | 137.184.89.151 |
| 84.09 | vless | 260.8 | 8.8 | 21.74 | 14.67 | 0.0 | 10.47 | 19.14 | Surfboard-tg-mixed | 199.7.140.201 |
| 83.8 | shadowsocks | 235.3 | 13.0 | 22.33 | 14.51 | 0.0 | 13.62 | 17.84 | mheidari-all | 23.150.152.38 |
| 83.4 | shadowsocks | 280.1 | 4.3 | 21.29 | 14.84 | 10.0 | 13.62 | 16.38 | Au1rxx-base64 | 173.244.56.9 |
| 83.29 | vless | 282.2 | 1.5 | 21.24 | 14.95 | 0.0 | 10.47 | 19.14 | Surfboard-tg-mixed | 179.254.92.134 |
| 83.19 | trojan | 266.3 | 0.5 | 21.61 | 14.98 | 9.24 | 11.69 | 16.38 | Au1rxx-base64 | 167.88.61.198 |
| 82.45 | trojan | 264.8 | 9.0 | 21.65 | 14.66 | 9.23 | 11.69 | 16.38 | Au1rxx-base64 | 167.88.61.20 |
| 82.39 | vless | 285.1 | 1.3 | 21.18 | 14.95 | 0.0 | 10.47 | 19.14 | Surfboard-tg-mixed | 143.246.62.191 |
| 82.32 | vless | 450.8 | 1.6 | 17.34 | 14.94 | 9.38 | 10.47 | 16.38 | Au1rxx-base64 | 167.17.69.171 |
| 82.08 | shadowsocks | 447.6 | 0.6 | 17.42 | 14.98 | 10.0 | 13.62 | 16.38 | Au1rxx-base64 | 185.230.230.18 |
| 82.0 | vless | 310.9 | 4.5 | 20.58 | 14.83 | 0.0 | 10.47 | 19.14 | Surfboard-tg-mixed | 179.254.92.190 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.975 | 1.0 | 20 | 508 | prefer |
| mheidari-all | 0.889 | 0.816 | 87 | 14408 | prefer |
| Surfboard-tg-mixed | 0.823 | 0.745 | 247 | 8521 | prefer |
| Au1rxx-base64 | 0.82 | 0.754 | 114 | 1751 | prefer |
| SoliSpirit-all | 0.335 | 1.0 | 1 | 11959 | observe |
| xiaoji235-airport-v2ray-all | 0.335 | 1.0 | 1 | 6752 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4919 | observe |
| DeltaKronecker-all | 0.255 | None | 0 | 2925 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5794 | observe |
| barry-far-vless | 0.255 | None | 0 | 5945 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4458 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.245 | None | 0 | 1751 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 57 |
| 204 | ProxyError | - | 27 |
| 204 | TimeoutError | - | 7 |
| cn-block | ClientOSError | - | 4 |
| cn-block | ProxyError | - | 4 |
| cn-block | TimeoutError | - | 3 |
| geo | ProxyError | - | 2 |
| speed | ProxyError | - | 2 |
| 204 | ClientOSError | - | 1 |
| geo | ClientOSError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 45 | 35 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
