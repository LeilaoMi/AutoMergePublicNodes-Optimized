# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-26 04:43:22 |
| 运行耗时 | 1014.6s |
| 订阅源总数 | 107 |
| 健康订阅源 | 94 |
| 原始节点 | 96568 |
| 去重后节点 | 26493 |
| TCP 可达 | 3000 |
| 真实可用 | 531 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 26493 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.2 |
| geo | 1.5 |
| tcp | 43.0 |
| probe | 334.5 |
| real_test | 540.3 |
| generate | 88.2 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 58822 |
| vmess | 15089 |
| shadowsocks | 11202 |
| trojan | 8929 |
| hysteria2 | 1558 |
| http | 638 |
| shadowsocksr | 168 |
| socks | 101 |
| anytls | 32 |
| hysteria | 15 |
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
| 81.98 | vless | 239.4 | 686.5 | 22.24 | 0.0 | 8.72 | 12.04 | 18.98 | Au1rxx-base64 | 79.141.172.154 |
| 81.4 | vless | 275.1 | 736.2 | 21.41 | 0.0 | 8.97 | 12.04 | 18.98 | Au1rxx-base64 | 195.123.235.177 |
| 81.32 | vless | 270.0 | 666.1 | 21.53 | 0.0 | 8.77 | 12.04 | 18.98 | Au1rxx-base64 | 169.40.42.232 |
| 81.27 | vless | 258.4 | 632.6 | 21.8 | 0.0 | 8.65 | 12.04 | 18.98 | Au1rxx-base64 | 195.211.98.43 |
| 81.24 | vless | 273.4 | 724.8 | 21.45 | 0.0 | 8.77 | 12.04 | 18.98 | Au1rxx-base64 | 169.40.42.212 |
| 80.88 | vless | 287.1 | 761.8 | 21.13 | 0.0 | 8.73 | 12.04 | 18.98 | Au1rxx-base64 | 169.40.42.35 |
| 80.84 | vless | 294.6 | 745.8 | 20.96 | 0.0 | 8.86 | 12.04 | 18.98 | Au1rxx-base64 | 66.70.179.198 |
| 80.83 | vless | 293.4 | 661.9 | 20.99 | 0.0 | 8.82 | 12.04 | 18.98 | Au1rxx-base64 | 169.40.42.184 |
| 80.79 | vless | 301.5 | 770.3 | 20.8 | 0.0 | 8.97 | 12.04 | 18.98 | Au1rxx-base64 | 169.40.42.173 |
| 80.46 | vless | 311.0 | 774.6 | 20.58 | 0.0 | 8.86 | 12.04 | 18.98 | Au1rxx-base64 | 158.69.112.254 |
| 80.42 | vless | 284.3 | 766.4 | 21.2 | 0.0 | 8.73 | 12.04 | 18.98 | Au1rxx-base64 | 169.40.42.235 |
| 80.4 | shadowsocks | 220.9 | 602.8 | 22.67 | 0.0 | 9.07 | 13.68 | 18.98 | Au1rxx-base64 | 198.98.53.130 |
| 80.22 | vless | 328.6 | 892.5 | 20.17 | 0.0 | 9.03 | 12.04 | 18.98 | Au1rxx-base64 | 169.40.42.89 |
| 80.11 | vless | 320.4 | 856.9 | 20.36 | 0.0 | 8.73 | 12.04 | 18.98 | Au1rxx-base64 | 169.40.42.163 |
| 79.96 | vless | 327.0 | 761.6 | 20.21 | 0.0 | 8.73 | 12.04 | 18.98 | Au1rxx-base64 | 169.40.42.231 |
| 79.85 | vless | 333.6 | 899.5 | 20.06 | 0.0 | 8.77 | 12.04 | 18.98 | Au1rxx-base64 | 169.40.42.223 |
| 79.7 | vless | 339.5 | 873.2 | 19.92 | 0.0 | 8.76 | 12.04 | 18.98 | Au1rxx-base64 | 169.40.42.95 |
| 79.69 | vless | 281.3 | 757.5 | 21.27 | 0.0 | 8.82 | 12.04 | 18.98 | Au1rxx-base64 | 169.40.42.16 |
| 79.62 | vless | 341.1 | 932.7 | 19.88 | 0.0 | 8.72 | 12.04 | 18.98 | Au1rxx-base64 | 169.40.42.90 |
| 79.52 | vless | 361.2 | 916.6 | 19.42 | 0.0 | 9.08 | 12.04 | 18.98 | Au1rxx-base64 | 169.40.42.74 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.924 | 0.863 | 284 | 1594 | prefer |
| Surfboard-tg-mixed | 0.845 | 0.772 | 79 | 7217 | prefer |
| mheidari-all | 0.403 | 0.322 | 649 | 22526 | observe |
| ermaozi | 0.357 | 0.333 | 33 | 352 | observe |
| xiaoji235-airport-v2ray-all | 0.335 | 1.0 | 1 | 6752 | observe |
| ermaozi-get_subscribe | 0.272 | 0.308 | 13 | 375 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5293 | observe |
| Epodonios-all | 0.255 | None | 0 | 7682 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 8923 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5837 | observe |
| barry-far-vless | 0.255 | None | 0 | 6063 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4304 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.239 | None | 0 | 1594 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 204 |
| speed | TimeoutError | - | 116 |
| geo | ClientOSError | - | 59 |
| 204 | ProxyError | - | 45 |
| cn-block | ClientOSError | - | 35 |
| 204 | TimeoutError | - | 28 |
| speed | ClientOSError | - | 25 |
| cn-block | TimeoutError | - | 15 |
| 204 | ClientOSError | - | 4 |
| cn-block | ProxyError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
