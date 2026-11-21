# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-11-21 07:30:11 |
| 运行耗时 | 320.3s |
| 订阅源总数 | 107 |
| 健康订阅源 | 88 |
| 原始节点 | 82370 |
| 去重后节点 | 27798 |
| TCP 可达 | 3000 |
| 真实可用 | 448 |
| Verified 输出 | 52 |
| Global 输出 | 300 |
| All 输出 | 27798 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.9 |
| geo | 1.5 |
| tcp | 85.0 |
| probe | 97.8 |
| real_test | 78.3 |
| china_check | 36.0 |
| write_verified | 0.2 |
| generate | 14.9 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 47834 |
| vmess | 15300 |
| shadowsocks | 10354 |
| trojan | 6950 |
| hysteria2 | 1506 |
| shadowsocksr | 150 |
| http | 138 |
| socks | 88 |
| hysteria | 24 |
| tuic | 15 |
| anytls | 11 |

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
| 88.85 | shadowsocks | 187.4 | 0.7 | 23.44 | 14.97 | 10.0 | 12.92 | 13.52 | Au1rxx-base64 | 149.22.95.183 |
| 86.11 | shadowsocks | 267.6 | 0.2 | 21.58 | 14.99 | 10.0 | 12.92 | 13.52 | Au1rxx-base64 | 95.215.201.18 |
| 84.13 | http | 283.2 | 0.3 | 21.22 | 14.99 | 0.0 | 12.78 | 17.64 | ermaozi | 172.64.68.89 |
| 83.69 | vless | 260.5 | 8.4 | 21.75 | 14.69 | 6.75 | 9.62 | 13.52 | Au1rxx-base64 | 45.63.53.81 |
| 83.27 | shadowsocks | 327.7 | 0.3 | 20.19 | 14.99 | 10.0 | 12.92 | 13.52 | Au1rxx-base64 | 156.146.38.170 |
| 82.78 | hysteria2 | 280.8 | 47.5 | 21.28 | 13.22 | 3.76 | 12.0 | 13.52 | Au1rxx-base64 | 66.94.121.46 |
| 82.55 | vless | 265.2 | 0.7 | 21.64 | 14.97 | 4.8 | 9.62 | 13.52 | Au1rxx-base64 | 15.204.97.206 |
| 82.52 | shadowsocks | 226.8 | 3.8 | 22.53 | 14.86 | 0.0 | 12.92 | 17.5 | mheidari-all | 104.238.140.45 |
| 82.07 | shadowsocks | 269.6 | 1.9 | 21.54 | 14.93 | 10.0 | 12.92 | 13.52 | Au1rxx-base64 | 173.244.56.9 |
| 82.01 | shadowsocks | 261.8 | 1.9 | 21.72 | 14.93 | 0.0 | 12.92 | 16.94 | Surfboard-tg-mixed | 137.184.89.151 |
| 81.6 | shadowsocks | 280.7 | 0.5 | 21.28 | 14.98 | 9.83 | 12.92 | 13.52 | Au1rxx-base64 | 149.22.87.204 |
| 81.47 | shadowsocks | 355.6 | 3.6 | 19.55 | 14.87 | 10.0 | 12.92 | 13.52 | Au1rxx-base64 | 37.19.198.243 |
| 81.44 | shadowsocks | 284.8 | 0.8 | 21.18 | 14.97 | 9.83 | 12.92 | 13.52 | Au1rxx-base64 | 149.22.87.241 |
| 81.36 | shadowsocks | 364.4 | 3.5 | 19.34 | 14.87 | 10.0 | 12.92 | 13.52 | Au1rxx-base64 | 37.19.198.160 |
| 81.35 | shadowsocks | 357.2 | 3.2 | 19.51 | 14.88 | 10.0 | 12.92 | 13.52 | Au1rxx-base64 | 37.19.198.244 |
| 81.32 | vless | 262.2 | 3.5 | 21.71 | 14.87 | 0.0 | 9.62 | 17.5 | mheidari-all | 107.191.58.86 |
| 81.24 | http | 264.1 | 4.4 | 21.67 | 14.84 | 0.0 | 12.78 | 17.64 | ermaozi | 38.95.111.226 |
| 81.19 | shadowsocks | 367.2 | 0.3 | 19.28 | 14.99 | 10.0 | 12.92 | 13.52 | Au1rxx-base64 | 185.230.230.18 |
| 80.94 | vless | 275.9 | 1.8 | 21.39 | 14.93 | 0.0 | 9.62 | 17.5 | mheidari-all | 69.17.3.150 |
| 80.94 | shadowsocks | 307.3 | 0.4 | 20.66 | 14.99 | 9.84 | 12.92 | 13.52 | Au1rxx-base64 | 149.22.87.240 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.979 | 1.0 | 24 | 443 | prefer |
| Surfboard-tg-mixed | 0.928 | 0.853 | 143 | 8565 | prefer |
| mheidari-all | 0.914 | 0.838 | 191 | 14439 | prefer |
| Au1rxx-base64 | 0.875 | 0.808 | 177 | 1751 | prefer |
| DeltaKronecker-all | 0.335 | 1.0 | 1 | 2910 | observe |
| tg-LonUp_M | 0.318 | 1.0 | 2 | 166 | observe |
| xiaoji235-airport-v2ray-all | 0.287 | 0.5 | 2 | 6752 | observe |
| tg-oneclickvpnkeys | 0.26 | 1.0 | 1 | 117 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5045 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 11789 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5496 | observe |
| barry-far-vless | 0.255 | None | 0 | 5914 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4518 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 57 |
| 204 | ProxyError | - | 10 |
| cn-block | ClientOSError | - | 8 |
| 204 | TimeoutError | - | 4 |
| cn-block | TimeoutError | - | 4 |
| cn-block | ProxyError | - | 2 |
| geo | ProxyError | - | 1 |
| 204 | ClientOSError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 41 | 52 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
