# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-19 22:33:43 |
| 运行耗时 | 300.4s |
| 订阅源总数 | 107 |
| 健康订阅源 | 93 |
| 原始节点 | 94461 |
| 去重后节点 | 26025 |
| TCP 可达 | 3000 |
| 真实可用 | 471 |
| Verified 输出 | 38 |
| Global 输出 | 300 |
| All 输出 | 26025 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.1 |
| geo | 1.6 |
| tcp | 78.8 |
| probe | 97.5 |
| real_test | 76.1 |
| china_check | 25.8 |
| write_verified | 0.0 |
| generate | 13.5 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 56396 |
| vmess | 17079 |
| shadowsocks | 11213 |
| trojan | 7914 |
| hysteria2 | 1216 |
| http | 338 |
| shadowsocksr | 168 |
| socks | 68 |
| anytls | 46 |
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
| 92.28 | shadowsocks | 257.0 | 2.0 | 21.83 | 14.93 | 9.44 | 12.72 | 17.36 | Au1rxx-base64 | 37.19.198.244 |
| 92.2 | shadowsocks | 255.5 | 2.7 | 21.86 | 14.9 | 9.36 | 12.72 | 17.36 | Au1rxx-base64 | 37.19.198.160 |
| 91.34 | shadowsocks | 256.9 | 0.2 | 21.83 | 14.99 | 9.44 | 12.72 | 17.36 | Au1rxx-base64 | 37.19.198.243 |
| 90.8 | shadowsocks | 255.2 | 2.7 | 21.87 | 14.9 | 7.95 | 12.72 | 17.36 | Au1rxx-base64 | 37.19.198.236 |
| 90.24 | vless | 262.8 | 5.2 | 21.69 | 14.81 | 8.11 | 8.27 | 17.36 | Au1rxx-base64 | 162.35.126.130 |
| 90.01 | vless | 289.9 | 2.2 | 21.07 | 14.92 | 9.07 | 8.27 | 17.36 | Au1rxx-base64 | 169.40.42.231 |
| 89.91 | vless | 330.9 | 1.4 | 20.12 | 14.95 | 9.21 | 8.27 | 17.36 | Au1rxx-base64 | 169.40.42.90 |
| 89.45 | vless | 341.6 | 3.1 | 19.87 | 14.88 | 9.07 | 8.27 | 17.36 | Au1rxx-base64 | 169.40.42.235 |
| 89.4 | vless | 345.4 | 2.2 | 19.78 | 14.92 | 9.07 | 8.27 | 17.36 | Au1rxx-base64 | 185.95.231.156 |
| 89.33 | vless | 342.9 | 9.2 | 19.84 | 14.65 | 9.21 | 8.27 | 17.36 | Au1rxx-base64 | 167.17.69.171 |
| 89.08 | shadowsocks | 280.1 | 5.1 | 21.29 | 14.81 | 8.76 | 12.72 | 17.36 | Au1rxx-base64 | 156.146.38.167 |
| 89.01 | vless | 275.1 | 9.8 | 21.41 | 14.63 | 8.55 | 8.27 | 17.36 | Au1rxx-base64 | 212.104.141.233 |
| 88.95 | shadowsocks | 285.6 | 2.8 | 21.17 | 14.9 | 8.51 | 12.72 | 17.36 | Au1rxx-base64 | 156.146.38.168 |
| 88.82 | vless | 369.5 | 1.9 | 19.23 | 14.93 | 9.03 | 8.27 | 17.36 | Au1rxx-base64 | 169.40.42.104 |
| 88.81 | vless | 265.4 | 13.0 | 21.64 | 14.51 | 9.03 | 8.27 | 17.36 | Au1rxx-base64 | 159.89.87.21 |
| 88.71 | shadowsocks | 282.1 | 1.1 | 21.25 | 14.96 | 9.04 | 12.72 | 17.36 | Au1rxx-base64 | 156.146.38.169 |
| 88.63 | shadowsocks | 285.2 | 0.9 | 21.18 | 14.96 | 9.04 | 12.72 | 17.36 | Au1rxx-base64 | 156.146.38.170 |
| 88.59 | vless | 379.0 | 1.9 | 19.0 | 14.93 | 9.03 | 8.27 | 17.36 | Au1rxx-base64 | 169.40.42.35 |
| 87.92 | vless | 405.0 | 3.4 | 18.4 | 14.87 | 9.02 | 8.27 | 17.36 | Au1rxx-base64 | 169.40.42.163 |
| 87.85 | vless | 358.1 | 8.3 | 19.49 | 14.69 | 8.04 | 8.27 | 17.36 | Au1rxx-base64 | 66.70.179.198 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.956 | 1.0 | 20 | 27 | prefer |
| mheidari-all | 0.926 | 0.857 | 63 | 23238 | prefer |
| DeltaKronecker-all | 0.913 | 0.843 | 70 | 3294 | prefer |
| Au1rxx-base64 | 0.902 | 0.848 | 283 | 1411 | prefer |
| Surfboard-tg-mixed | 0.842 | 0.767 | 120 | 7064 | prefer |
| roosterkid-openproxylist-v2ray | 0.364 | 1.0 | 3 | 150 | observe |
| 10ium-HighSpeed | 0.345 | 1.0 | 2 | 839 | observe |
| SoliSpirit-all | 0.335 | 1.0 | 1 | 9850 | observe |
| tg-LonUp_M | 0.318 | 1.0 | 2 | 170 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| tg-oneclickvpnkeys | 0.258 | 1.0 | 1 | 72 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4940 | observe |
| Epodonios-all | 0.255 | None | 0 | 7515 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5579 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 34 |
| speed | ClientOSError | - | 14 |
| geo | ClientOSError | - | 13 |
| 204 | ProxyError | - | 12 |
| cn-block | ClientOSError | - | 7 |
| 204 | ClientOSError | - | 5 |
| 204 | TimeoutError | - | 4 |
| cn-block | TimeoutError | - | 4 |
| cn-block | ProxyError | - | 2 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 71 | 38 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
