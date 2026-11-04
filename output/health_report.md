# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-11-04 14:28:29 |
| 运行耗时 | 287.4s |
| 订阅源总数 | 107 |
| 健康订阅源 | 88 |
| 原始节点 | 82244 |
| 去重后节点 | 26846 |
| TCP 可达 | 3000 |
| 真实可用 | 395 |
| Verified 输出 | 33 |
| Global 输出 | 300 |
| All 输出 | 26846 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.4 |
| geo | 1.5 |
| tcp | 80.3 |
| probe | 82.0 |
| real_test | 75.3 |
| china_check | 30.9 |
| write_verified | 0.0 |
| generate | 11.9 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 49227 |
| vmess | 13897 |
| shadowsocks | 9031 |
| trojan | 8153 |
| hysteria2 | 1571 |
| shadowsocksr | 146 |
| socks | 78 |
| http | 72 |
| hysteria | 32 |
| anytls | 21 |
| tuic | 16 |

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
| 94.29 | shadowsocks | 250.3 | 0.6 | 21.98 | 14.98 | 10.0 | 14.27 | 17.06 | Au1rxx-base64 | 156.146.38.167 |
| 93.33 | shadowsocks | 286.1 | 4.3 | 21.16 | 14.84 | 10.0 | 14.27 | 17.06 | Au1rxx-base64 | 156.146.38.170 |
| 92.84 | shadowsocks | 311.0 | 1.8 | 20.58 | 14.93 | 10.0 | 14.27 | 17.06 | Au1rxx-base64 | 156.146.38.168 |
| 92.52 | shadowsocks | 301.5 | 2.9 | 20.8 | 14.89 | 10.0 | 14.27 | 17.06 | Au1rxx-base64 | 185.230.230.18 |
| 92.4 | shadowsocks | 291.6 | 2.5 | 21.03 | 14.91 | 10.0 | 14.27 | 17.06 | Au1rxx-base64 | 37.19.198.243 |
| 91.74 | shadowsocks | 302.2 | 2.9 | 20.78 | 14.89 | 9.99 | 14.27 | 17.06 | Au1rxx-base64 | 45.86.51.18 |
| 91.62 | hysteria2 | 297.8 | 0.5 | 20.88 | 14.98 | 10.0 | 10.31 | 17.06 | Au1rxx-base64 | 129.213.91.185 |
| 91.32 | shadowsocks | 325.3 | 4.8 | 20.25 | 14.82 | 10.0 | 14.27 | 17.06 | Au1rxx-base64 | 37.19.198.244 |
| 90.21 | trojan | 431.6 | 2.4 | 17.79 | 14.91 | 10.0 | 13.45 | 17.06 | Au1rxx-base64 | 66.23.203.21 |
| 89.34 | shadowsocks | 308.7 | 6.3 | 20.63 | 14.77 | 10.0 | 14.27 | 17.06 | Au1rxx-base64 | 193.151.163.18 |
| 88.42 | shadowsocks | 330.7 | 2.8 | 20.12 | 14.89 | 10.0 | 14.27 | 17.06 | Au1rxx-base64 | 193.151.160.9 |
| 88.31 | shadowsocks | 286.8 | 4.2 | 21.14 | 14.84 | 10.0 | 14.27 | 17.06 | Au1rxx-base64 | 37.19.198.160 |
| 88.31 | shadowsocks | 334.2 | 2.7 | 20.04 | 14.9 | 10.0 | 14.27 | 17.06 | Au1rxx-base64 | 149.22.95.183 |
| 88.04 | shadowsocks | 287.4 | 2.4 | 21.12 | 14.91 | 10.0 | 14.27 | 17.06 | Au1rxx-base64 | 95.215.201.18 |
| 87.7 | shadowsocks | 358.3 | 0.3 | 19.48 | 14.99 | 10.0 | 14.27 | 17.06 | Au1rxx-base64 | 173.244.56.9 |
| 87.3 | shadowsocks | 341.7 | 1.7 | 19.87 | 14.94 | 10.0 | 14.27 | 17.06 | Au1rxx-base64 | 173.244.56.6 |
| 84.23 | trojan | 479.1 | 0.8 | 16.69 | 14.97 | 8.11 | 13.45 | 17.06 | Au1rxx-base64 | 69.164.240.85 |
| 83.9 | shadowsocks | 340.1 | 2.4 | 19.91 | 14.91 | 9.51 | 14.27 | 17.06 | Au1rxx-base64 | 149.22.87.204 |
| 83.64 | trojan | 324.3 | 1.3 | 20.27 | 14.95 | 5.29 | 13.45 | 17.06 | Au1rxx-base64 | 167.88.61.198 |
| 83.5 | trojan | 307.4 | 0.7 | 20.66 | 14.97 | 5.26 | 13.45 | 17.06 | Au1rxx-base64 | 167.88.61.193 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| mheidari-all | 0.944 | 0.87 | 108 | 15179 | prefer |
| zhangkai | 0.923 | 1.0 | 19 | 43 | prefer |
| Surfboard-tg-mixed | 0.864 | 0.789 | 114 | 8518 | prefer |
| Au1rxx-base64 | 0.793 | 0.725 | 258 | 1751 | prefer |
| ninja-vless | 0.327 | 1.0 | 1 | 1791 | observe |
| tg-LonUp_M | 0.318 | 1.0 | 2 | 177 | observe |
| ermaozi | 0.315 | 1.0 | 2 | 83 | observe |
| xiaoji235-airport-v2ray-all | 0.287 | 0.5 | 2 | 6752 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5005 | observe |
| DeltaKronecker-all | 0.255 | None | 0 | 2526 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 10830 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5997 | observe |
| barry-far-vless | 0.255 | None | 0 | 6238 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4608 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 63 |
| 204 | ProxyError | - | 14 |
| cn-block | ProxyError | - | 10 |
| 204 | TimeoutError | - | 8 |
| geo | ProxyError | - | 3 |
| 204 | ClientOSError | - | 3 |
| cn-block | TimeoutError | - | 3 |
| cn-block | ClientOSError | - | 3 |
| speed | ProxyError | - | 2 |
| 204 | ServerDisconnectedError | - | 1 |
| geo | ClientOSError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 61 | 33 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
