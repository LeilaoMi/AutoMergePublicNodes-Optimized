# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-11-15 19:02:47 |
| 运行耗时 | 303.5s |
| 订阅源总数 | 107 |
| 健康订阅源 | 87 |
| 原始节点 | 84509 |
| 去重后节点 | 27682 |
| TCP 可达 | 3000 |
| 真实可用 | 339 |
| Verified 输出 | 44 |
| Global 输出 | 300 |
| All 输出 | 27682 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.9 |
| geo | 1.5 |
| tcp | 76.4 |
| probe | 95.5 |
| real_test | 65.8 |
| china_check | 42.8 |
| write_verified | 0.0 |
| generate | 14.7 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 50593 |
| vmess | 14823 |
| shadowsocks | 10097 |
| trojan | 7030 |
| hysteria2 | 1541 |
| shadowsocksr | 152 |
| http | 138 |
| socks | 66 |
| hysteria | 37 |
| tuic | 17 |
| anytls | 15 |

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
| 92.61 | shadowsocks | 268.6 | 7.0 | 21.56 | 14.74 | 10.0 | 13.61 | 17.2 | Au1rxx-base64 | 45.86.51.18 |
| 92.36 | vless | 297.3 | 3.2 | 20.9 | 14.88 | 10.0 | 9.38 | 17.2 | Au1rxx-base64 | 167.17.69.171 |
| 91.25 | shadowsocks | 295.8 | 26.5 | 20.93 | 14.01 | 10.0 | 13.61 | 17.2 | Au1rxx-base64 | 185.230.230.18 |
| 91.06 | shadowsocks | 302.6 | 9.6 | 20.77 | 14.64 | 10.0 | 13.61 | 17.2 | Au1rxx-base64 | 193.151.160.9 |
| 90.85 | shadowsocks | 354.3 | 1.1 | 19.58 | 14.96 | 10.0 | 13.61 | 17.2 | Au1rxx-base64 | 15.204.247.206 |
| 90.31 | shadowsocks | 290.1 | 1.2 | 21.06 | 14.96 | 9.6 | 13.61 | 17.2 | Au1rxx-base64 | 193.151.160.18 |
| 90.25 | vless | 379.3 | 8.8 | 19.0 | 14.67 | 10.0 | 9.38 | 17.2 | Au1rxx-base64 | 169.40.42.35 |
| 90.12 | shadowsocks | 307.2 | 0.1 | 20.67 | 15.0 | 10.0 | 13.61 | 17.2 | Au1rxx-base64 | 156.146.38.170 |
| 89.82 | shadowsocks | 395.1 | 3.2 | 18.63 | 14.88 | 10.0 | 13.61 | 17.2 | Au1rxx-base64 | 193.151.163.18 |
| 89.35 | vless | 425.4 | 4.2 | 17.93 | 14.84 | 10.0 | 9.38 | 17.2 | Au1rxx-base64 | 169.40.42.74 |
| 88.85 | trojan | 468.8 | 0.9 | 16.93 | 14.97 | 10.0 | 12.75 | 17.2 | Au1rxx-base64 | 69.164.240.85 |
| 88.64 | shadowsocks | 364.9 | 1.4 | 19.33 | 14.95 | 10.0 | 13.61 | 17.2 | Au1rxx-base64 | 156.146.38.168 |
| 87.7 | vless | 455.4 | 5.0 | 17.24 | 14.81 | 9.82 | 9.38 | 17.2 | Au1rxx-base64 | 66.70.179.198 |
| 87.4 | shadowsocks | 305.7 | 6.1 | 20.7 | 14.77 | 10.0 | 13.61 | 17.2 | Au1rxx-base64 | 95.215.201.18 |
| 87.09 | trojan | 378.7 | 3.2 | 19.01 | 14.88 | 10.0 | 12.75 | 17.2 | Au1rxx-base64 | 66.23.203.21 |
| 86.48 | vless | 481.7 | 17.8 | 16.63 | 14.33 | 9.94 | 9.38 | 17.2 | Au1rxx-base64 | 169.40.42.202 |
| 86.04 | vless | 396.0 | 5.5 | 18.61 | 14.79 | 10.0 | 9.38 | 17.2 | Au1rxx-base64 | 169.40.42.168 |
| 85.73 | http | 290.0 | 10.0 | 21.07 | 14.63 | 0.0 | 13.93 | 18.6 | ermaozi | 172.64.68.89 |
| 85.06 | shadowsocks | 325.4 | 1.4 | 20.24 | 14.95 | 5.84 | 13.61 | 17.2 | Au1rxx-base64 | 156.146.38.169 |
| 84.88 | shadowsocks | 252.5 | 1.1 | 21.93 | 14.96 | 0.0 | 13.61 | 18.88 | Surfboard-tg-mixed | 172.111.38.72 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.942 | 0.957 | 23 | 544 | prefer |
| mheidari-all | 0.887 | 0.818 | 55 | 14826 | prefer |
| Au1rxx-base64 | 0.832 | 0.766 | 128 | 1751 | prefer |
| Surfboard-tg-mixed | 0.827 | 0.749 | 235 | 9142 | prefer |
| xiaoji235-airport-v2ray-all | 0.335 | 1.0 | 1 | 6752 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4916 | observe |
| DeltaKronecker-all | 0.255 | None | 0 | 3024 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 11885 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 6162 | observe |
| barry-far-vless | 0.255 | None | 0 | 6310 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4584 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.245 | None | 0 | 1751 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 47 |
| 204 | ProxyError | - | 23 |
| 204 | TimeoutError | - | 10 |
| cn-block | ProxyError | - | 6 |
| 204 | ClientOSError | - | 4 |
| speed | ClientOSError | - | 3 |
| geo | ProxyError | - | 2 |
| speed | ProxyError | - | 2 |
| cn-block | TimeoutError | - | 1 |
| speed | TimeoutError | - | 1 |
| cn-block | ClientOSError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 67 | 44 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
