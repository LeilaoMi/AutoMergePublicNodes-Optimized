# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-25 05:00:22 |
| 运行耗时 | 291.6s |
| 订阅源总数 | 107 |
| 健康订阅源 | 87 |
| 原始节点 | 96475 |
| 去重后节点 | 27106 |
| TCP 可达 | 3000 |
| 真实可用 | 471 |
| Verified 输出 | 104 |
| Global 输出 | 300 |
| All 输出 | 27106 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.3 |
| geo | 1.5 |
| tcp | 77.9 |
| probe | 79.5 |
| real_test | 86.9 |
| china_check | 29.6 |
| write_verified | 0.0 |
| generate | 10.9 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 57112 |
| vmess | 17093 |
| shadowsocks | 12624 |
| trojan | 7719 |
| hysteria2 | 1364 |
| http | 284 |
| shadowsocksr | 170 |
| socks | 61 |
| anytls | 25 |
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
| 94.68 | shadowsocks | 239.3 | 0.1 | 22.24 | 15.0 | 10.0 | 14.36 | 17.08 | Au1rxx-base64 | 37.19.198.244 |
| 94.09 | shadowsocks | 257.0 | 4.9 | 21.83 | 14.82 | 10.0 | 14.36 | 17.08 | Au1rxx-base64 | 37.19.198.160 |
| 93.72 | vless | 254.5 | 8.1 | 21.89 | 14.7 | 10.0 | 10.05 | 17.08 | Au1rxx-base64 | 159.89.87.21 |
| 93.69 | vless | 268.3 | 0.2 | 21.57 | 14.99 | 10.0 | 10.05 | 17.08 | Au1rxx-base64 | 169.40.42.225 |
| 93.39 | shadowsocks | 239.5 | 0.2 | 22.23 | 14.99 | 9.23 | 14.36 | 17.08 | Au1rxx-base64 | 185.230.230.18 |
| 93.33 | shadowsocks | 293.1 | 2.7 | 20.99 | 14.9 | 10.0 | 14.36 | 17.08 | Au1rxx-base64 | 37.19.198.236 |
| 93.23 | vless | 265.5 | 14.0 | 21.63 | 14.47 | 10.0 | 10.05 | 17.08 | Au1rxx-base64 | 167.17.69.171 |
| 93.08 | shadowsocks | 247.7 | 2.3 | 22.04 | 14.91 | 9.19 | 14.36 | 17.08 | Au1rxx-base64 | 193.151.163.18 |
| 92.95 | vless | 263.3 | 22.8 | 21.68 | 14.14 | 10.0 | 10.05 | 17.08 | Au1rxx-base64 | 195.211.98.43 |
| 92.4 | hysteria2 | 253.2 | 31.3 | 21.92 | 13.83 | 7.95 | 13.12 | 17.08 | Au1rxx-base64 | 129.213.91.185 |
| 92.37 | shadowsocks | 311.3 | 3.7 | 20.57 | 14.86 | 10.0 | 14.36 | 17.08 | Au1rxx-base64 | 15.204.246.132 |
| 91.96 | vless | 247.0 | 0.4 | 22.06 | 14.99 | 7.78 | 10.05 | 17.08 | Au1rxx-base64 | 195.123.235.183 |
| 91.86 | vless | 250.9 | 0.2 | 21.97 | 14.99 | 7.77 | 10.05 | 17.08 | Au1rxx-base64 | 195.123.235.177 |
| 91.86 | vless | 288.8 | 17.0 | 21.09 | 14.36 | 9.28 | 10.05 | 17.08 | Au1rxx-base64 | 66.70.179.198 |
| 91.78 | shadowsocks | 277.7 | 0.6 | 21.35 | 14.98 | 9.89 | 14.36 | 17.08 | Au1rxx-base64 | 156.146.38.170 |
| 91.78 | vless | 348.4 | 1.6 | 19.71 | 14.94 | 10.0 | 10.05 | 17.08 | Au1rxx-base64 | 169.40.42.231 |
| 91.55 | shadowsocks | 241.6 | 0.3 | 22.19 | 14.99 | 6.93 | 14.36 | 17.08 | Au1rxx-base64 | 37.19.198.243 |
| 91.5 | vless | 361.5 | 1.0 | 19.41 | 14.96 | 10.0 | 10.05 | 17.08 | Au1rxx-base64 | 169.40.42.90 |
| 91.23 | vless | 277.5 | 26.0 | 21.35 | 14.03 | 8.72 | 10.05 | 17.08 | Au1rxx-base64 | 162.35.8.62 |
| 91.22 | shadowsocks | 277.4 | 2.7 | 21.36 | 14.9 | 10.0 | 14.36 | 17.08 | Au1rxx-base64 | 156.146.38.167 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.98 | 0.966 | 88 | 604 | prefer |
| Au1rxx-base64 | 0.926 | 0.863 | 321 | 1625 | prefer |
| Surfboard-tg-mixed | 0.835 | 1.0 | 14 | 7102 | prefer |
| mheidari-all | 0.522 | 0.441 | 195 | 24115 | observe |
| DeltaKronecker-all | 0.48 | 1.0 | 4 | 3780 | observe |
| SoliSpirit-all | 0.438 | 1.0 | 3 | 10204 | observe |
| tg-oneclickvpnkeys | 0.273 | 0.667 | 3 | 107 | observe |
| tg-LonUp_M | 0.262 | 1.0 | 1 | 179 | observe |
| roosterkid-openproxylist-v2ray | 0.261 | 1.0 | 1 | 150 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4911 | observe |
| Epodonios-all | 0.255 | None | 0 | 7585 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5419 | observe |
| barry-far-vless | 0.255 | None | 0 | 5635 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4186 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 97 |
| geo | ClientOSError | - | 28 |
| speed | ClientOSError | - | 15 |
| cn-block | ClientOSError | - | 5 |
| 204 | ProxyError | - | 3 |
| cn-block | TimeoutError | - | 3 |
| cn-block | ProxyError | - | 2 |
| geo | TimeoutError | - | 1 |
| geo | ProxyError | - | 1 |
| 204 | ClientOSError | - | 1 |
| speed | TimeoutError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 81 | 104 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
