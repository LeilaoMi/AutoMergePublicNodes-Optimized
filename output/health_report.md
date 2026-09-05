# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-05 20:14:37 |
| 运行耗时 | 286.9s |
| 订阅源总数 | 107 |
| 健康订阅源 | 96 |
| 原始节点 | 97140 |
| 去重后节点 | 25678 |
| TCP 可达 | 3000 |
| 真实可用 | 480 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 25678 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.0 |
| geo | 1.4 |
| tcp | 42.0 |
| probe | 84.6 |
| real_test | 104.1 |
| generate | 47.7 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 62021 |
| vmess | 12479 |
| shadowsocks | 11142 |
| trojan | 9208 |
| hysteria2 | 1879 |
| http | 144 |
| shadowsocksr | 132 |
| socks | 63 |
| anytls | 38 |
| hysteria | 20 |
| tuic | 14 |

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
| 84.25 | vless | 201.9 | 521.9 | 23.11 | 0.0 | 10.0 | 11.88 | 19.26 | Au1rxx-base64 | 172.235.43.210 |
| 83.46 | vless | 195.7 | 504.7 | 23.25 | 0.0 | 9.07 | 11.88 | 19.26 | Au1rxx-base64 | 172.233.139.46 |
| 83.35 | vless | 197.1 | 518.4 | 23.22 | 0.0 | 8.99 | 11.88 | 19.26 | Au1rxx-base64 | 172.235.38.85 |
| 82.9 | hysteria2 | 223.7 | 553.8 | 22.6 | 0.0 | 9.04 | 13.0 | 19.26 | Au1rxx-base64 | 66.94.121.46 |
| 82.1 | vless | 209.4 | 524.9 | 22.93 | 0.0 | 9.03 | 11.88 | 19.26 | Au1rxx-base64 | 23.94.227.94 |
| 81.72 | vless | 274.1 | 733.5 | 21.43 | 0.0 | 9.15 | 11.88 | 19.26 | Au1rxx-base64 | 216.167.94.71 |
| 81.15 | shadowsocks | 201.3 | 490.7 | 23.12 | 0.0 | 9.0 | 14.27 | 19.26 | Au1rxx-base64 | 108.181.118.10 |
| 80.85 | vless | 319.2 | 843.1 | 20.39 | 0.0 | 9.32 | 11.88 | 19.26 | Au1rxx-base64 | 15.204.97.216 |
| 80.07 | vless | 202.1 | 499.4 | 23.1 | 0.0 | 9.33 | 11.88 | 19.26 | Au1rxx-base64 | 172.235.62.90 |
| 79.63 | shadowsocks | 241.7 | 588.9 | 22.18 | 0.0 | 10.0 | 14.27 | 17.18 | Surfboard-tg-mixed | 149.22.95.183 |
| 79.51 | vless | 190.2 | 494.4 | 23.37 | 0.0 | 10.0 | 11.88 | 19.26 | Au1rxx-base64 | 104.160.40.178 |
| 79.11 | http | 411.0 | 1140.2 | 18.26 | 0.0 | 10.0 | 14.53 | 19.32 | zhangkai | 138.199.35.216 |
| 79.02 | vless | 225.1 | 588.8 | 22.57 | 0.0 | 9.15 | 11.88 | 19.26 | Au1rxx-base64 | 38.150.33.232 |
| 78.69 | http | 429.3 | 1159.9 | 17.84 | 0.0 | 10.0 | 14.53 | 19.32 | zhangkai | 138.199.35.198 |
| 78.42 | vless | 227.7 | 483.1 | 22.51 | 0.0 | 9.27 | 11.88 | 19.26 | Au1rxx-base64 | 172.64.154.8 |
| 77.96 | vless | 263.0 | 297.0 | 21.69 | 3.86 | 9.81 | 11.88 | 17.18 | Surfboard-tg-mixed | 31.76.91.72 |
| 77.87 | vless | 261.3 | 619.3 | 21.73 | 0.0 | 10.0 | 11.88 | 19.26 | Au1rxx-base64 | 38.246.229.58 |
| 77.67 | vless | 230.2 | 494.1 | 22.45 | 0.0 | 9.31 | 11.88 | 19.26 | Au1rxx-base64 | 162.159.39.218 |
| 77.19 | trojan | 281.5 | 762.4 | 21.26 | 0.0 | 10.0 | 12.55 | 15.88 | mheidari-all | 34.94.125.227 |
| 77.15 | vless | 210.9 | 478.8 | 22.9 | 0.0 | 9.26 | 11.88 | 19.26 | Au1rxx-base64 | 108.162.198.178 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.966 | 1.0 | 23 | 144 | prefer |
| Au1rxx-base64 | 0.948 | 0.88 | 325 | 1764 | prefer |
| Surfboard-tg-mixed | 0.83 | 0.753 | 150 | 7292 | prefer |
| mheidari-all | 0.585 | 0.505 | 99 | 22630 | observe |
| tg-oneclickvpnkeys | 0.482 | 1.0 | 6 | 132 | observe |
| DeltaKronecker-all | 0.335 | 1.0 | 1 | 6212 | observe |
| xiaoji235-airport-v2ray-all | 0.287 | 0.5 | 2 | 6965 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4887 | observe |
| Epodonios-all | 0.255 | None | 0 | 7653 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 8694 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 6126 | observe |
| barry-far-vless | 0.255 | None | 0 | 6249 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4087 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| cn-block | ClientOSError | - | 40 |
| 204 | TimeoutError | - | 23 |
| geo | ClientOSError | - | 19 |
| cn-block | TimeoutError | - | 18 |
| 204 | ProxyError | - | 7 |
| speed | TimeoutError | - | 7 |
| speed | ClientOSError | - | 5 |
| geo | TimeoutError | - | 3 |
| 204 | ClientOSError | - | 2 |
| speed | ProxyError | - | 1 |
| geo | ProxyError | - | 1 |
| cn-block | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
