# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-22 12:10:07 |
| 运行耗时 | 306.2s |
| 订阅源总数 | 107 |
| 健康订阅源 | 92 |
| 原始节点 | 95591 |
| 去重后节点 | 26659 |
| TCP 可达 | 3000 |
| 真实可用 | 383 |
| Verified 输出 | 123 |
| Global 输出 | 300 |
| All 输出 | 26659 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.0 |
| geo | 1.6 |
| tcp | 83.9 |
| probe | 86.1 |
| real_test | 82.7 |
| china_check | 35.5 |
| write_verified | 0.1 |
| generate | 10.5 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 56581 |
| vmess | 17129 |
| shadowsocks | 12102 |
| trojan | 8077 |
| hysteria2 | 1251 |
| http | 193 |
| shadowsocksr | 161 |
| socks | 53 |
| anytls | 21 |
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
| 94.57 | shadowsocks | 241.8 | 0.2 | 22.18 | 14.99 | 10.0 | 14.04 | 17.36 | Au1rxx-base64 | 156.146.38.170 |
| 94.56 | shadowsocks | 242.0 | 0.6 | 22.18 | 14.98 | 10.0 | 14.04 | 17.36 | Au1rxx-base64 | 156.146.38.168 |
| 93.72 | trojan | 246.3 | 2.3 | 22.08 | 14.91 | 10.0 | 12.93 | 17.36 | Au1rxx-base64 | 66.23.203.21 |
| 92.52 | shadowsocks | 311.5 | 2.0 | 20.57 | 14.93 | 10.0 | 14.04 | 17.36 | Au1rxx-base64 | 37.19.198.243 |
| 90.99 | shadowsocks | 245.3 | 2.5 | 22.1 | 14.9 | 7.14 | 14.04 | 17.36 | Au1rxx-base64 | 156.146.38.169 |
| 89.05 | shadowsocks | 368.1 | 1.2 | 19.26 | 14.96 | 10.0 | 14.04 | 17.36 | Au1rxx-base64 | 185.215.132.9 |
| 89.0 | shadowsocks | 302.2 | 1.5 | 20.78 | 14.94 | 10.0 | 14.04 | 17.36 | Au1rxx-base64 | 193.151.163.18 |
| 88.01 | shadowsocks | 353.8 | 0.9 | 19.59 | 14.97 | 10.0 | 14.04 | 17.36 | Au1rxx-base64 | 185.230.230.18 |
| 87.89 | shadowsocks | 306.0 | 0.1 | 20.69 | 15.0 | 10.0 | 14.04 | 17.36 | Au1rxx-base64 | 173.244.56.6 |
| 87.83 | shadowsocks | 359.4 | 0.6 | 19.46 | 14.98 | 7.04 | 14.04 | 17.36 | Au1rxx-base64 | 37.19.198.236 |
| 87.46 | shadowsocks | 399.6 | 2.3 | 18.53 | 14.92 | 10.0 | 14.04 | 17.36 | Au1rxx-base64 | 193.151.160.18 |
| 87.24 | trojan | 468.9 | 2.1 | 16.92 | 14.92 | 10.0 | 12.93 | 17.36 | Au1rxx-base64 | 69.164.240.85 |
| 87.15 | shadowsocks | 249.3 | 2.1 | 22.01 | 14.92 | 10.0 | 14.04 | 17.36 | Au1rxx-base64 | 156.146.38.167 |
| 87.11 | shadowsocks | 320.2 | 10.5 | 20.36 | 14.61 | 9.66 | 14.04 | 17.36 | Au1rxx-base64 | 149.22.95.183 |
| 87.07 | vless | 290.8 | 2.1 | 21.05 | 14.92 | 10.0 | 7.9 | 17.36 | Au1rxx-base64 | 45.32.69.110 |
| 86.83 | shadowsocks | 365.2 | 6.8 | 19.32 | 14.75 | 10.0 | 14.04 | 17.36 | Au1rxx-base64 | 95.215.201.18 |
| 86.79 | shadowsocks | 310.8 | 1.3 | 20.58 | 14.95 | 10.0 | 14.04 | 17.36 | Au1rxx-base64 | 173.244.56.9 |
| 86.46 | vless | 401.5 | 4.4 | 18.48 | 14.83 | 9.6 | 7.9 | 17.36 | Au1rxx-base64 | 169.40.42.225 |
| 85.8 | shadowsocks | 307.3 | 0.1 | 20.66 | 15.0 | 7.07 | 14.04 | 17.36 | Au1rxx-base64 | 37.19.198.160 |
| 85.33 | shadowsocks | 355.8 | 0.4 | 19.54 | 14.98 | 8.29 | 14.04 | 17.36 | Au1rxx-base64 | 51.222.136.236 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.972 | 1.0 | 32 | 45 | prefer |
| ermaozi-get_subscribe | 0.884 | 0.878 | 49 | 523 | prefer |
| Au1rxx-base64 | 0.846 | 0.787 | 254 | 1519 | prefer |
| mheidari-all | 0.797 | 0.724 | 58 | 23951 | prefer |
| Surfboard-tg-mixed | 0.757 | 0.683 | 60 | 7043 | prefer |
| DeltaKronecker-all | 0.655 | 0.579 | 38 | 3641 | observe |
| ninja-vless | 0.392 | 0.75 | 4 | 1791 | observe |
| tg-oneclickvpnkeys | 0.257 | 1.0 | 1 | 55 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5015 | observe |
| Epodonios-all | 0.255 | None | 0 | 7460 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 10067 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5382 | observe |
| barry-far-vless | 0.255 | None | 0 | 5666 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 68 |
| speed | ClientOSError | - | 12 |
| 204 | TimeoutError | - | 7 |
| 204 | ProxyError | - | 6 |
| cn-block | TimeoutError | - | 6 |
| geo | ClientOSError | - | 4 |
| cn-block | ClientOSError | - | 3 |
| 204 | ClientOSError | - | 3 |
| cn-block | ProxyError | - | 2 |
| geo | ProxyError | - | 1 |
| geo | TimeoutError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 117 | 123 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
