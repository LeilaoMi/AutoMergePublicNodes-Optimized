# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-20 11:55:25 |
| 运行耗时 | 300.6s |
| 订阅源总数 | 107 |
| 健康订阅源 | 93 |
| 原始节点 | 94098 |
| 去重后节点 | 26454 |
| TCP 可达 | 3000 |
| 真实可用 | 472 |
| Verified 输出 | 136 |
| Global 输出 | 300 |
| All 输出 | 26454 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.1 |
| geo | 1.4 |
| tcp | 80.5 |
| probe | 75.6 |
| real_test | 97.2 |
| china_check | 33.4 |
| write_verified | 0.0 |
| generate | 8.4 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 55985 |
| vmess | 16889 |
| shadowsocks | 11180 |
| trojan | 8374 |
| hysteria2 | 1106 |
| http | 278 |
| shadowsocksr | 165 |
| socks | 64 |
| anytls | 34 |
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
| 95.33 | shadowsocks | 257.0 | 0.8 | 21.83 | 14.97 | 10.0 | 14.01 | 18.52 | Au1rxx-base64 | 156.146.38.167 |
| 94.7 | trojan | 330.6 | 0.2 | 20.13 | 14.99 | 10.0 | 14.06 | 18.52 | Au1rxx-base64 | 66.23.203.21 |
| 93.28 | shadowsocks | 311.6 | 0.6 | 20.56 | 14.98 | 10.0 | 14.01 | 18.52 | Au1rxx-base64 | 37.19.198.160 |
| 92.95 | shadowsocks | 308.7 | 8.4 | 20.63 | 14.68 | 10.0 | 14.01 | 18.52 | Au1rxx-base64 | 37.19.198.243 |
| 92.94 | shadowsocks | 306.0 | 0.7 | 20.7 | 14.97 | 10.0 | 14.01 | 18.52 | Au1rxx-base64 | 37.19.198.244 |
| 91.06 | shadowsocks | 279.7 | 1.7 | 21.3 | 14.94 | 10.0 | 14.01 | 18.52 | Au1rxx-base64 | 173.244.56.9 |
| 90.28 | trojan | 471.8 | 0.6 | 16.86 | 14.98 | 10.0 | 14.06 | 18.52 | Au1rxx-base64 | 69.164.240.85 |
| 89.29 | vless | 275.9 | 0.8 | 21.39 | 14.97 | 10.0 | 8.91 | 18.52 | Au1rxx-base64 | 69.48.201.136 |
| 88.98 | hysteria2 | 425.3 | 7.8 | 17.93 | 14.71 | 10.0 | 14.12 | 18.52 | Au1rxx-base64 | 179.255.104.98 |
| 88.19 | vless | 250.1 | 3.6 | 21.99 | 14.86 | 5.92 | 8.91 | 18.52 | Au1rxx-base64 | 195.211.98.43 |
| 88.18 | shadowsocks | 325.6 | 2.4 | 20.24 | 14.91 | 10.0 | 14.01 | 18.52 | Au1rxx-base64 | 185.230.230.18 |
| 88.16 | vless | 286.4 | 2.3 | 21.15 | 14.91 | 7.82 | 8.91 | 18.52 | Au1rxx-base64 | 195.123.235.183 |
| 87.53 | vless | 415.6 | 1.5 | 18.16 | 14.94 | 9.01 | 8.91 | 18.52 | Au1rxx-base64 | 185.95.231.156 |
| 87.38 | vless | 433.3 | 4.9 | 17.75 | 14.82 | 10.0 | 8.91 | 18.52 | Au1rxx-base64 | 169.40.42.168 |
| 87.2 | vless | 331.1 | 0.1 | 20.11 | 15.0 | 10.0 | 8.91 | 18.52 | Au1rxx-base64 | 169.40.42.224 |
| 87.14 | vless | 402.8 | 2.1 | 18.45 | 14.92 | 10.0 | 8.91 | 18.52 | Au1rxx-base64 | 169.40.42.89 |
| 86.43 | shadowsocks | 360.0 | 1.1 | 19.44 | 14.96 | 10.0 | 14.01 | 18.52 | Au1rxx-base64 | 185.215.132.9 |
| 86.38 | vless | 362.2 | 2.9 | 19.39 | 14.89 | 9.69 | 8.91 | 18.52 | Au1rxx-base64 | 169.40.42.225 |
| 86.03 | vless | 375.9 | 9.3 | 19.08 | 14.65 | 9.63 | 8.91 | 18.52 | Au1rxx-base64 | 5.34.178.120 |
| 85.76 | vless | 387.5 | 3.4 | 18.81 | 14.87 | 9.96 | 8.91 | 18.52 | Au1rxx-base64 | 44.248.233.99 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.956 | 1.0 | 20 | 27 | prefer |
| ermaozi-get_subscribe | 0.951 | 0.946 | 56 | 510 | prefer |
| mheidari-all | 0.945 | 0.88 | 50 | 23400 | prefer |
| Au1rxx-base64 | 0.848 | 0.803 | 309 | 1192 | prefer |
| Surfboard-tg-mixed | 0.667 | 0.589 | 90 | 6911 | observe |
| tg-LonUp_M | 0.495 | 0.875 | 8 | 167 | observe |
| DeltaKronecker-all | 0.468 | 0.386 | 127 | 3519 | observe |
| tg-oneclickvpnkeys | 0.258 | 1.0 | 1 | 65 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4967 | observe |
| Epodonios-all | 0.255 | None | 0 | 7377 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5515 | observe |
| barry-far-vless | 0.255 | None | 0 | 5733 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4278 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 89 |
| geo | ClientOSError | - | 29 |
| 204 | TimeoutError | - | 20 |
| speed | ClientOSError | - | 11 |
| 204 | ProxyError | - | 9 |
| cn-block | TimeoutError | - | 9 |
| cn-block | ClientOSError | - | 6 |
| 204 | ClientOSError | - | 5 |
| geo | ProxyError | - | 4 |
| cn-block | ProxyError | - | 3 |
| geo | TimeoutError | - | 3 |
| speed | TimeoutError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 91 | 136 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
