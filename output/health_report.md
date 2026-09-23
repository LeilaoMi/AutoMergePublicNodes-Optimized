# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-23 04:30:17 |
| 运行耗时 | 1020.3s |
| 订阅源总数 | 107 |
| 健康订阅源 | 96 |
| 原始节点 | 96642 |
| 去重后节点 | 26618 |
| TCP 可达 | 3000 |
| 真实可用 | 564 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 26618 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.5 |
| geo | 1.8 |
| tcp | 43.5 |
| probe | 381.3 |
| real_test | 506.7 |
| generate | 80.5 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 59154 |
| vmess | 14890 |
| shadowsocks | 11265 |
| trojan | 8755 |
| hysteria2 | 1586 |
| http | 681 |
| shadowsocksr | 171 |
| socks | 89 |
| anytls | 24 |
| hysteria | 19 |
| tuic | 8 |

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
| 80.71 | shadowsocks | 284.6 | 730.8 | 21.19 | 0.0 | 10.0 | 14.18 | 19.34 | Surfboard-tg-mixed | 37.19.198.243 |
| 79.01 | hysteria2 | 345.2 | 903.4 | 19.79 | 0.0 | 8.55 | 14.25 | 17.52 | Au1rxx-base64 | 159.223.157.129 |
| 78.65 | vless | 221.8 | 612.2 | 22.64 | 0.0 | 8.6 | 9.89 | 17.52 | Au1rxx-base64 | 195.211.98.43 |
| 78.33 | vless | 288.3 | 728.3 | 21.1 | 0.0 | 10.0 | 9.89 | 19.34 | Surfboard-tg-mixed | 47.253.226.114 |
| 78.22 | shadowsocks | 256.8 | 631.5 | 21.83 | 0.0 | 8.69 | 14.18 | 17.52 | Au1rxx-base64 | 156.146.38.169 |
| 78.14 | shadowsocks | 252.1 | 629.0 | 21.94 | 0.0 | 8.5 | 14.18 | 17.52 | Au1rxx-base64 | 156.146.38.168 |
| 77.93 | shadowsocks | 259.9 | 637.0 | 21.76 | 0.0 | 8.5 | 14.18 | 17.52 | Au1rxx-base64 | 156.146.38.167 |
| 77.79 | shadowsocks | 365.1 | 917.8 | 19.33 | 0.0 | 10.0 | 14.18 | 19.34 | Surfboard-tg-mixed | 51.222.136.236 |
| 77.59 | shadowsocks | 280.5 | 720.1 | 21.28 | 0.0 | 8.61 | 14.18 | 17.52 | Au1rxx-base64 | 37.19.198.244 |
| 77.36 | shadowsocks | 257.8 | 633.3 | 21.81 | 0.0 | 10.0 | 14.18 | 16.08 | mheidari-all | 156.146.38.170 |
| 77.36 | vless | 273.5 | 709.4 | 21.45 | 0.0 | 8.5 | 9.89 | 17.52 | Au1rxx-base64 | 79.141.172.154 |
| 77.31 | shadowsocks | 290.8 | 744.8 | 21.05 | 0.0 | 10.0 | 14.18 | 16.08 | mheidari-all | 37.19.198.236 |
| 77.16 | hysteria2 | 301.4 | 639.5 | 20.8 | 0.0 | 8.55 | 14.25 | 17.52 | Au1rxx-base64 | 66.94.121.46 |
| 76.7 | vless | 292.9 | 678.6 | 21.0 | 0.0 | 8.72 | 9.89 | 17.52 | Au1rxx-base64 | 138.124.60.146 |
| 76.52 | vless | 311.3 | 767.2 | 20.57 | 0.0 | 8.54 | 9.89 | 17.52 | Au1rxx-base64 | 185.95.231.156 |
| 76.49 | vless | 307.0 | 728.5 | 20.67 | 0.0 | 10.0 | 9.89 | 17.52 | Au1rxx-base64 | 66.70.179.198 |
| 76.43 | shadowsocks | 326.0 | 832.7 | 20.23 | 0.0 | 8.5 | 14.18 | 17.52 | Au1rxx-base64 | 142.4.216.225 |
| 75.96 | vless | 309.4 | 748.3 | 20.62 | 0.0 | 8.55 | 9.89 | 17.52 | Au1rxx-base64 | 169.40.42.15 |
| 75.59 | shadowsocks | 367.0 | 909.4 | 19.28 | 0.0 | 10.0 | 14.18 | 19.34 | Surfboard-tg-mixed | 51.222.12.127 |
| 75.39 | shadowsocks | 265.8 | 609.0 | 21.62 | 0.0 | 8.75 | 14.18 | 17.52 | Au1rxx-base64 | 23.150.248.20 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.904 | 0.843 | 331 | 1585 | prefer |
| ermaozi | 0.726 | 0.719 | 57 | 346 | prefer |
| Surfboard-tg-mixed | 0.633 | 0.553 | 244 | 7168 | observe |
| DeltaKronecker-all | 0.389 | 0.385 | 13 | 6324 | observe |
| mheidari-all | 0.289 | 0.208 | 490 | 22274 | observe |
| ermaozi-get_subscribe | 0.283 | 0.667 | 3 | 372 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4915 | observe |
| Epodonios-all | 0.255 | None | 0 | 7633 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 8890 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5836 | observe |
| barry-far-vless | 0.255 | None | 0 | 6054 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4252 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 198 |
| speed | ClientOSError | - | 97 |
| geo | ClientOSError | - | 89 |
| speed | TimeoutError | - | 85 |
| cn-block | ClientOSError | - | 47 |
| 204 | ProxyError | - | 19 |
| 204 | TimeoutError | - | 18 |
| cn-block | TimeoutError | - | 14 |
| cn-block | ProxyError | - | 4 |
| 204 | ClientOSError | - | 2 |
| 204 | ProxyConnectionError | - | 1 |
| geo | exit-country | CN | 1 |
| speed | ClientPayloadError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
