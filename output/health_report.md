# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-27 22:29:47 |
| 运行耗时 | 296.0s |
| 订阅源总数 | 107 |
| 健康订阅源 | 88 |
| 原始节点 | 97513 |
| 去重后节点 | 26753 |
| TCP 可达 | 3000 |
| 真实可用 | 459 |
| Verified 输出 | 85 |
| Global 输出 | 300 |
| All 输出 | 26753 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.1 |
| geo | 1.5 |
| tcp | 78.4 |
| probe | 89.6 |
| real_test | 76.9 |
| china_check | 28.5 |
| write_verified | 0.1 |
| generate | 14.1 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 57147 |
| vmess | 17757 |
| shadowsocks | 12807 |
| trojan | 8014 |
| hysteria2 | 1404 |
| shadowsocksr | 167 |
| http | 117 |
| socks | 52 |
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
| 92.08 | shadowsocks | 243.5 | 14.0 | 22.14 | 14.48 | 9.4 | 13.3 | 16.76 | Au1rxx-base64 | 37.19.198.243 |
| 91.84 | shadowsocks | 244.4 | 5.3 | 22.12 | 14.8 | 9.36 | 13.3 | 16.76 | Au1rxx-base64 | 185.230.230.18 |
| 91.22 | hysteria2 | 227.3 | 2.0 | 22.52 | 14.92 | 4.46 | 14.06 | 16.76 | Au1rxx-base64 | 129.213.91.185 |
| 91.16 | vless | 278.1 | 7.6 | 21.34 | 14.72 | 9.38 | 8.96 | 16.76 | Au1rxx-base64 | 195.123.235.183 |
| 90.45 | vless | 301.5 | 2.4 | 20.8 | 14.91 | 9.02 | 8.96 | 16.76 | Au1rxx-base64 | 169.40.42.229 |
| 90.38 | shadowsocks | 332.9 | 2.5 | 20.07 | 14.91 | 9.34 | 13.3 | 16.76 | Au1rxx-base64 | 37.19.198.160 |
| 90.37 | shadowsocks | 273.9 | 2.9 | 21.44 | 14.89 | 9.35 | 13.3 | 16.76 | Au1rxx-base64 | 37.19.198.236 |
| 90.29 | vless | 298.1 | 5.5 | 20.88 | 14.79 | 8.9 | 8.96 | 16.76 | Au1rxx-base64 | 66.70.179.198 |
| 90.08 | vless | 316.5 | 1.6 | 20.45 | 14.94 | 8.97 | 8.96 | 16.76 | Au1rxx-base64 | 169.40.42.163 |
| 89.62 | shadowsocks | 329.1 | 5.4 | 20.16 | 14.8 | 9.1 | 13.3 | 16.76 | Au1rxx-base64 | 45.86.51.18 |
| 89.43 | vless | 346.2 | 9.1 | 19.76 | 14.66 | 9.29 | 8.96 | 16.76 | Au1rxx-base64 | 195.211.98.43 |
| 88.98 | vless | 369.6 | 1.6 | 19.22 | 14.94 | 9.1 | 8.96 | 16.76 | Au1rxx-base64 | 169.40.42.202 |
| 88.87 | vless | 358.7 | 11.5 | 19.48 | 14.57 | 9.1 | 8.96 | 16.76 | Au1rxx-base64 | 169.40.42.35 |
| 88.73 | vless | 275.8 | 5.3 | 21.39 | 14.8 | 9.02 | 8.96 | 16.76 | Au1rxx-base64 | 169.40.42.225 |
| 88.69 | vless | 364.3 | 9.6 | 19.35 | 14.64 | 8.98 | 8.96 | 16.76 | Au1rxx-base64 | 185.95.231.156 |
| 88.68 | vless | 374.1 | 3.8 | 19.12 | 14.86 | 8.98 | 8.96 | 16.76 | Au1rxx-base64 | 169.40.42.231 |
| 88.41 | vless | 332.9 | 11.8 | 20.07 | 14.56 | 9.3 | 8.96 | 16.76 | Au1rxx-base64 | 169.40.42.168 |
| 88.37 | trojan | 259.3 | 2.4 | 21.77 | 14.91 | 9.3 | 11.13 | 16.76 | Au1rxx-base64 | 216.152.156.65 |
| 88.22 | trojan | 263.8 | 2.5 | 21.67 | 14.91 | 9.25 | 11.13 | 16.76 | Au1rxx-base64 | 216.152.155.54 |
| 88.08 | shadowsocks | 395.2 | 6.7 | 18.63 | 14.75 | 9.14 | 13.3 | 16.76 | Au1rxx-base64 | 193.151.160.18 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.988 | 1.0 | 28 | 535 | prefer |
| Surfboard-tg-mixed | 0.951 | 0.883 | 60 | 7532 | prefer |
| Au1rxx-base64 | 0.947 | 0.88 | 375 | 1730 | prefer |
| mheidari-all | 0.849 | 0.78 | 50 | 24397 | prefer |
| DeltaKronecker-all | 0.352 | 0.5 | 6 | 3052 | observe |
| SoliSpirit-all | 0.335 | 1.0 | 1 | 10927 | observe |
| roosterkid-openproxylist-v2ray | 0.326 | 0.75 | 4 | 150 | observe |
| ninja-vless | 0.279 | 0.5 | 2 | 1791 | observe |
| tg-OutlineReleasedKey | 0.257 | 1.0 | 1 | 52 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4988 | observe |
| Epodonios-all | 0.255 | None | 0 | 7530 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5538 | observe |
| barry-far-vless | 0.255 | None | 0 | 5531 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4500 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 41 |
| 204 | ProxyError | - | 6 |
| 204 | TimeoutError | - | 5 |
| cn-block | ClientOSError | - | 4 |
| cn-block | TimeoutError | - | 4 |
| geo | ClientOSError | - | 4 |
| geo | TimeoutError | - | 1 |
| geo | ProxyError | - | 1 |
| cn-block | ProxyError | - | 1 |
| speed | ClientOSError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 143 | 85 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
