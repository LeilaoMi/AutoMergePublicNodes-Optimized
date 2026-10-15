# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-15 21:14:29 |
| 运行耗时 | 300.0s |
| 订阅源总数 | 107 |
| 健康订阅源 | 93 |
| 原始节点 | 99675 |
| 去重后节点 | 27750 |
| TCP 可达 | 3000 |
| 真实可用 | 85 |
| Verified 输出 | 85 |
| Global 输出 | 93 |
| All 输出 | 27750 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.4 |
| geo | 1.5 |
| tcp | 83.2 |
| probe | 102.7 |
| real_test | 68.9 |
| china_check | 27.4 |
| write_verified | 0.0 |
| generate | 10.9 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 58652 |
| vmess | 16542 |
| shadowsocks | 11941 |
| trojan | 10417 |
| hysteria2 | 1206 |
| http | 649 |
| shadowsocksr | 161 |
| socks | 57 |
| anytls | 27 |
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
| 74.15 | hysteria2 | 241.3 | 695.2 | 22.19 | 0.0 | 7.28 | 12.0 | 14.18 | Au1rxx-base64 | 129.213.91.185 |
| 72.7 | shadowsocks | 252.9 | 703.4 | 21.92 | 0.0 | 10.0 | 10.6 | 14.18 | Au1rxx-base64 | 37.19.198.244 |
| 72.57 | shadowsocks | 258.9 | 713.8 | 21.79 | 0.0 | 10.0 | 10.6 | 14.18 | Au1rxx-base64 | 37.19.198.243 |
| 69.82 | vless | 249.3 | 694.4 | 22.01 | 0.0 | 10.0 | 8.63 | 14.18 | Au1rxx-base64 | 47.253.226.114 |
| 69.7 | shadowsocks | 279.2 | 642.1 | 21.32 | 0.0 | 10.0 | 10.6 | 14.18 | Au1rxx-base64 | 156.146.38.168 |
| 69.68 | http | 304.5 | 688.8 | 20.73 | 0.0 | 0.0 | 14.37 | 19.68 | ermaozi | 35.183.131.26 |
| 69.6 | shadowsocks | 257.2 | 709.0 | 21.82 | 0.0 | 10.0 | 10.6 | 14.18 | Au1rxx-base64 | 37.19.198.236 |
| 69.5 | shadowsocks | 283.2 | 652.2 | 21.22 | 0.0 | 10.0 | 10.6 | 14.18 | Au1rxx-base64 | 156.146.38.170 |
| 69.27 | http | 302.4 | 742.0 | 20.78 | 0.0 | 0.0 | 14.37 | 19.68 | ermaozi | 198.44.157.19 |
| 68.64 | shadowsocks | 280.7 | 648.7 | 21.28 | 0.0 | 10.0 | 10.6 | 14.18 | Au1rxx-base64 | 156.146.38.167 |
| 67.76 | vless | 289.6 | 713.4 | 21.07 | 0.0 | 8.39 | 8.63 | 14.18 | Au1rxx-base64 | 66.70.179.198 |
| 67.59 | vless | 266.3 | 704.9 | 21.61 | 0.0 | 8.17 | 8.63 | 14.18 | Au1rxx-base64 | 195.123.235.183 |
| 67.55 | shadowsocks | 259.5 | 711.6 | 21.77 | 0.0 | 10.0 | 10.6 | 14.18 | Au1rxx-base64 | 37.19.198.160 |
| 67.55 | vless | 268.8 | 643.2 | 21.55 | 0.0 | 8.72 | 8.63 | 14.18 | Au1rxx-base64 | 195.211.98.43 |
| 67.39 | vless | 354.0 | 887.9 | 19.58 | 0.0 | 10.0 | 8.63 | 14.18 | Au1rxx-base64 | 169.40.42.224 |
| 67.29 | vless | 381.0 | 811.6 | 18.96 | 0.0 | 10.0 | 8.63 | 14.18 | Au1rxx-base64 | 51.79.31.36 |
| 66.8 | vless | 379.6 | 909.8 | 18.99 | 0.0 | 10.0 | 8.63 | 14.18 | Au1rxx-base64 | 169.40.42.182 |
| 66.69 | vless | 306.5 | 681.5 | 20.68 | 0.0 | 10.0 | 8.63 | 14.18 | Au1rxx-base64 | 69.48.201.136 |
| 66.56 | http | 393.2 | 921.9 | 18.68 | 0.0 | 0.0 | 14.37 | 19.68 | ermaozi | 192.227.176.234 |
| 66.12 | http | 354.6 | 890.7 | 19.57 | 0.0 | 0.0 | 14.37 | 19.68 | ermaozi | 206.223.183.13 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.982 | 0.97 | 66 | 659 | prefer |
| Au1rxx-base64 | 0.773 | 0.701 | 355 | 1827 | prefer |
| mheidari-all | 0.628 | 0.552 | 29 | 24072 | observe |
| Surfboard-tg-mixed | 0.391 | 1.0 | 2 | 7166 | observe |
| tg-oneclickvpnkeys | 0.259 | 1.0 | 1 | 89 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5089 | observe |
| DeltaKronecker-all | 0.255 | None | 0 | 5147 | observe |
| Epodonios-all | 0.255 | None | 0 | 7793 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9888 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5625 | observe |
| barry-far-vless | 0.255 | None | 0 | 5957 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4235 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |
| Au1rxx-clash | 0.248 | None | 0 | 1827 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 69 |
| speed | ClientOSError | - | 19 |
| 204 | TimeoutError | - | 9 |
| 204 | ProxyError | - | 9 |
| cn-block | ClientOSError | - | 5 |
| cn-block | ProxyError | - | 3 |
| geo | ProxyError | - | 3 |
| geo | ClientOSError | - | 2 |
| geo | TimeoutError | - | 1 |
| speed | ProxyError | - | 1 |
| cn-block | TimeoutError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 89 | 85 | - |
| global | False | 94 | 93 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
