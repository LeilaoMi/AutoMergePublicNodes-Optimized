# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-15 04:08:59 |
| 运行耗时 | 302.3s |
| 订阅源总数 | 107 |
| 健康订阅源 | 93 |
| 原始节点 | 98808 |
| 去重后节点 | 27524 |
| TCP 可达 | 3000 |
| 真实可用 | 62 |
| Verified 输出 | 62 |
| Global 输出 | 72 |
| All 输出 | 27524 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.4 |
| geo | 1.5 |
| tcp | 87.5 |
| probe | 86.8 |
| real_test | 85.5 |
| china_check | 29.0 |
| write_verified | 0.0 |
| generate | 7.8 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 58478 |
| vmess | 16366 |
| shadowsocks | 11782 |
| trojan | 10088 |
| hysteria2 | 1149 |
| http | 657 |
| shadowsocksr | 165 |
| socks | 68 |
| anytls | 32 |
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
| 77.55 | vless | 265.4 | 606.1 | 21.64 | 0.0 | 9.0 | 9.85 | 17.06 | Au1rxx-base64 | 195.211.98.43 |
| 77.39 | shadowsocks | 239.6 | 613.6 | 22.23 | 0.0 | 10.0 | 14.1 | 17.06 | Au1rxx-base64 | 156.146.38.168 |
| 77.34 | shadowsocks | 306.4 | 718.6 | 20.68 | 0.0 | 10.0 | 14.1 | 17.06 | Au1rxx-base64 | 140.82.63.79 |
| 77.18 | shadowsocks | 299.7 | 741.7 | 20.84 | 0.0 | 10.0 | 14.1 | 17.06 | Au1rxx-base64 | 37.19.198.244 |
| 76.62 | shadowsocks | 301.3 | 743.7 | 20.8 | 0.0 | 10.0 | 14.1 | 17.06 | Au1rxx-base64 | 37.19.198.243 |
| 76.56 | hysteria2 | 273.7 | 710.4 | 21.44 | 0.0 | 7.29 | 12.27 | 17.06 | Au1rxx-base64 | 129.213.91.185 |
| 76.36 | vless | 259.5 | 629.6 | 21.77 | 0.0 | 9.0 | 9.85 | 17.06 | Au1rxx-base64 | 216.227.161.95 |
| 74.28 | shadowsocks | 244.2 | 619.4 | 22.12 | 0.0 | 10.0 | 14.1 | 17.06 | Au1rxx-base64 | 156.146.38.169 |
| 73.6 | shadowsocks | 313.9 | 636.8 | 20.51 | 0.0 | 10.0 | 14.1 | 17.06 | Au1rxx-base64 | 149.22.95.183 |
| 72.83 | shadowsocks | 312.2 | 721.1 | 20.55 | 0.0 | 8.75 | 14.1 | 17.06 | Au1rxx-base64 | 64.74.163.67 |
| 71.81 | shadowsocks | 314.3 | 740.4 | 20.5 | 0.0 | 9.65 | 14.1 | 17.06 | Au1rxx-base64 | 64.74.163.69 |
| 71.19 | vless | 334.1 | 822.9 | 20.05 | 0.0 | 9.12 | 9.85 | 17.06 | Au1rxx-base64 | 69.48.201.136 |
| 69.69 | vless | 429.9 | 1084.4 | 17.83 | 0.0 | 7.43 | 9.85 | 17.06 | Au1rxx-base64 | 185.95.231.156 |
| 68.92 | shadowsocks | 389.0 | 960.0 | 18.77 | 0.0 | 8.88 | 14.1 | 17.06 | Au1rxx-base64 | 15.204.246.107 |
| 68.09 | shadowsocks | 251.4 | 632.3 | 21.96 | 0.0 | 0.0 | 14.1 | 17.06 | Au1rxx-base64 | 156.146.38.170 |
| 67.82 | hysteria2 | 410.3 | 728.4 | 18.28 | 0.0 | 7.92 | 12.27 | 17.06 | Au1rxx-base64 | 62.210.124.146 |
| 67.52 | shadowsocks | 410.0 | 934.0 | 18.29 | 0.0 | 7.29 | 14.1 | 17.06 | Au1rxx-base64 | 51.222.136.236 |
| 67.52 | shadowsocks | 454.8 | 752.2 | 17.25 | 0.0 | 8.65 | 14.1 | 17.06 | Au1rxx-base64 | 103.11.76.248 |
| 66.46 | vless | 398.4 | 929.7 | 18.55 | 0.0 | 4.81 | 9.85 | 17.06 | Au1rxx-base64 | 213.165.50.45 |
| 66.2 | shadowsocks | 405.0 | 932.0 | 18.4 | 0.0 | 9.77 | 14.1 | 17.06 | Au1rxx-base64 | 51.79.49.116 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.996 | 0.984 | 61 | 703 | prefer |
| Au1rxx-base64 | 0.832 | 0.771 | 388 | 1576 | prefer |
| mheidari-all | 0.449 | 0.366 | 101 | 23886 | observe |
| Surfboard-tg-mixed | 0.32 | 0.5 | 4 | 7169 | observe |
| 10ium-HighSpeed | 0.289 | 1.0 | 1 | 839 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5125 | observe |
| DeltaKronecker-all | 0.255 | None | 0 | 4803 | observe |
| Epodonios-all | 0.255 | None | 0 | 7681 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9917 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5728 | observe |
| barry-far-vless | 0.255 | None | 0 | 5978 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4271 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 102 |
| speed | ClientOSError | - | 15 |
| geo | ClientOSError | - | 14 |
| cn-block | ClientOSError | - | 8 |
| 204 | ProxyError | - | 6 |
| cn-block | ProxyError | - | 2 |
| 204 | ClientOSError | - | 2 |
| cn-block | TimeoutError | - | 2 |
| speed | TimeoutError | - | 2 |
| 204 | TimeoutError | - | 2 |
| geo | ProxyError | - | 1 |
| speed | ClientPayloadError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 69 | 62 | - |
| global | False | 74 | 72 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
