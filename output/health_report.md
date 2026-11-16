# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-11-16 22:23:32 |
| 运行耗时 | 300.1s |
| 订阅源总数 | 107 |
| 健康订阅源 | 86 |
| 原始节点 | 83258 |
| 去重后节点 | 27658 |
| TCP 可达 | 3000 |
| 真实可用 | 527 |
| Verified 输出 | 27 |
| Global 输出 | 300 |
| All 输出 | 27658 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.9 |
| geo | 1.4 |
| tcp | 80.7 |
| probe | 78.6 |
| real_test | 84.8 |
| china_check | 38.1 |
| write_verified | 0.3 |
| generate | 11.5 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 49988 |
| vmess | 14780 |
| shadowsocks | 9652 |
| trojan | 6909 |
| hysteria2 | 1500 |
| shadowsocksr | 156 |
| http | 118 |
| socks | 93 |
| hysteria | 32 |
| tuic | 16 |
| anytls | 14 |

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
| 94.33 | vless | 323.2 | 3.1 | 20.3 | 14.89 | 9.93 | 11.23 | 17.98 | Au1rxx-base64 | 169.40.42.89 |
| 94.16 | vless | 332.4 | 1.5 | 20.08 | 14.94 | 9.93 | 11.23 | 17.98 | Au1rxx-base64 | 167.17.69.171 |
| 93.88 | vless | 313.6 | 0.7 | 20.52 | 14.97 | 9.84 | 11.23 | 17.98 | Au1rxx-base64 | 66.70.179.198 |
| 93.17 | shadowsocks | 246.1 | 8.6 | 22.08 | 14.68 | 10.0 | 13.85 | 17.98 | Au1rxx-base64 | 45.86.51.18 |
| 92.56 | vless | 386.3 | 4.8 | 18.83 | 14.82 | 9.92 | 11.23 | 17.98 | Au1rxx-base64 | 169.40.42.168 |
| 92.1 | shadowsocks | 306.9 | 1.3 | 20.67 | 14.95 | 9.15 | 13.85 | 17.98 | Au1rxx-base64 | 193.151.160.18 |
| 91.97 | shadowsocks | 304.4 | 4.4 | 20.73 | 14.84 | 10.0 | 13.85 | 17.98 | Au1rxx-base64 | 193.151.160.9 |
| 91.62 | shadowsocks | 264.3 | 0.5 | 21.66 | 14.98 | 10.0 | 13.85 | 17.98 | Au1rxx-base64 | 37.19.198.244 |
| 91.43 | vless | 391.5 | 3.1 | 18.72 | 14.88 | 9.92 | 11.23 | 17.98 | Au1rxx-base64 | 169.40.42.202 |
| 91.33 | vless | 417.2 | 1.8 | 18.12 | 14.93 | 10.0 | 11.23 | 17.98 | Au1rxx-base64 | 169.40.42.74 |
| 91.08 | shadowsocks | 307.4 | 0.4 | 20.66 | 14.98 | 10.0 | 13.85 | 17.98 | Au1rxx-base64 | 156.146.38.168 |
| 90.46 | shadowsocks | 257.8 | 4.8 | 21.81 | 14.82 | 10.0 | 13.85 | 17.98 | Au1rxx-base64 | 193.151.163.18 |
| 90.07 | shadowsocks | 313.6 | 5.0 | 20.52 | 14.81 | 10.0 | 13.85 | 17.98 | Au1rxx-base64 | 156.146.38.170 |
| 89.97 | trojan | 290.3 | 5.2 | 21.06 | 14.81 | 8.43 | 11.25 | 17.98 | Au1rxx-base64 | 170.101.101.19 |
| 89.69 | vless | 307.1 | 2.9 | 20.67 | 14.89 | 9.92 | 11.23 | 17.98 | Au1rxx-base64 | 159.89.87.21 |
| 89.69 | vless | 389.3 | 3.2 | 18.77 | 14.88 | 10.0 | 11.23 | 17.98 | Au1rxx-base64 | 169.40.42.35 |
| 89.69 | trojan | 394.4 | 5.1 | 18.65 | 14.81 | 10.0 | 11.25 | 17.98 | Au1rxx-base64 | 69.164.240.85 |
| 89.03 | vless | 379.4 | 2.9 | 19.0 | 14.89 | 9.04 | 11.23 | 17.98 | Au1rxx-base64 | 169.40.42.229 |
| 88.65 | trojan | 294.3 | 6.2 | 20.97 | 14.77 | 8.42 | 11.25 | 17.98 | Au1rxx-base64 | 170.101.101.67 |
| 87.87 | shadowsocks | 321.1 | 7.2 | 20.35 | 14.73 | 10.0 | 13.85 | 17.98 | Au1rxx-base64 | 95.215.201.18 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.985 | 1.0 | 25 | 548 | prefer |
| Surfboard-tg-mixed | 0.968 | 0.891 | 275 | 8691 | prefer |
| mheidari-all | 0.967 | 0.894 | 113 | 14735 | prefer |
| Au1rxx-base64 | 0.928 | 0.862 | 174 | 1751 | prefer |
| Surfboard-tg-vless | 0.391 | 1.0 | 2 | 6010 | observe |
| ninja-vless | 0.383 | 1.0 | 2 | 1791 | observe |
| xiaoji235-airport-v2ray-all | 0.335 | 1.0 | 1 | 6752 | observe |
| tg-LonUp_M | 0.318 | 1.0 | 2 | 170 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4964 | observe |
| DeltaKronecker-all | 0.255 | None | 0 | 2915 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 11743 | observe |
| barry-far-vless | 0.255 | None | 0 | 6209 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4545 | observe |
| Au1rxx-clash | 0.245 | None | 0 | 1751 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 38 |
| 204 | ProxyError | - | 11 |
| 204 | TimeoutError | - | 6 |
| cn-block | ClientOSError | - | 3 |
| 204 | ClientOSError | - | 2 |
| cn-block | TimeoutError | - | 2 |
| geo | ClientOSError | - | 1 |
| speed | ClientOSError | - | 1 |
| cn-block | ProxyError | - | 1 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 51 | 27 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
