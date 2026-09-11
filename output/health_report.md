# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-11 11:09:50 |
| 运行耗时 | 714.6s |
| 订阅源总数 | 107 |
| 健康订阅源 | 94 |
| 原始节点 | 84388 |
| 去重后节点 | 23243 |
| TCP 可达 | 3000 |
| 真实可用 | 483 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23243 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.3 |
| geo | 1.4 |
| tcp | 40.4 |
| probe | 286.6 |
| real_test | 304.0 |
| generate | 77.9 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 51448 |
| vmess | 12338 |
| shadowsocks | 10033 |
| trojan | 8112 |
| hysteria2 | 1598 |
| http | 650 |
| shadowsocksr | 132 |
| socks | 55 |
| tuic | 12 |
| hysteria | 8 |
| anytls | 2 |

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
| 81.13 | hysteria2 | 287.9 | 689.9 | 21.11 | 0.0 | 10.0 | 13.12 | 18.0 | Au1rxx-base64 | 159.223.157.129 |
| 79.51 | shadowsocks | 254.0 | 622.6 | 21.9 | 0.0 | 10.0 | 13.78 | 18.0 | Au1rxx-base64 | 156.146.38.168 |
| 77.81 | shadowsocks | 301.6 | 714.2 | 20.8 | 0.0 | 10.0 | 13.78 | 18.0 | Au1rxx-base64 | 37.19.198.244 |
| 77.77 | shadowsocks | 250.2 | 616.3 | 21.99 | 0.0 | 10.0 | 13.78 | 18.0 | Au1rxx-base64 | 156.146.38.170 |
| 76.14 | shadowsocks | 306.0 | 727.6 | 20.7 | 0.0 | 10.0 | 13.78 | 18.0 | Au1rxx-base64 | 37.19.198.243 |
| 76.11 | shadowsocks | 261.4 | 643.2 | 21.73 | 0.0 | 10.0 | 13.78 | 14.6 | Surfboard-tg-mixed | 156.146.38.167 |
| 75.54 | shadowsocks | 335.1 | 835.4 | 20.02 | 0.0 | 10.0 | 13.78 | 18.0 | Au1rxx-base64 | 15.204.247.206 |
| 75.36 | vless | 299.1 | 715.4 | 20.85 | 0.0 | 10.0 | 6.51 | 18.0 | Au1rxx-base64 | 79.141.172.154 |
| 74.36 | vless | 307.4 | 745.0 | 20.66 | 0.0 | 10.0 | 6.51 | 18.0 | Au1rxx-base64 | 47.253.226.114 |
| 74.31 | vless | 344.8 | 913.2 | 19.8 | 0.0 | 10.0 | 6.51 | 18.0 | Au1rxx-base64 | 38.180.242.205 |
| 73.78 | shadowsocks | 366.6 | 890.0 | 19.29 | 0.0 | 10.0 | 13.78 | 18.0 | Au1rxx-base64 | 38.180.135.156 |
| 73.4 | shadowsocks | 439.7 | 1121.3 | 17.6 | 0.0 | 10.0 | 13.78 | 18.0 | Au1rxx-base64 | 198.98.53.130 |
| 73.21 | shadowsocks | 332.8 | 732.3 | 20.07 | 0.0 | 10.0 | 13.78 | 18.0 | Au1rxx-base64 | 173.244.56.6 |
| 73.2 | shadowsocks | 309.9 | 759.2 | 20.6 | 0.0 | 10.0 | 13.78 | 14.6 | Surfboard-tg-mixed | 23.150.248.20 |
| 73.08 | shadowsocks | 302.3 | 718.7 | 20.78 | 0.0 | 10.0 | 13.78 | 14.6 | Surfboard-tg-mixed | 37.19.198.160 |
| 72.58 | shadowsocks | 345.8 | 725.7 | 19.77 | 0.0 | 10.0 | 13.78 | 18.0 | Au1rxx-base64 | 173.244.56.9 |
| 72.21 | vless | 297.4 | 679.1 | 20.89 | 0.0 | 10.0 | 6.51 | 18.0 | Au1rxx-base64 | 216.152.147.28 |
| 71.69 | vless | 293.5 | 670.5 | 20.98 | 0.0 | 10.0 | 6.51 | 18.0 | Au1rxx-base64 | 188.137.243.243 |
| 71.44 | vless | 337.3 | 712.3 | 19.97 | 0.0 | 10.0 | 6.51 | 18.0 | Au1rxx-base64 | 169.40.42.231 |
| 71.06 | shadowsocks | 303.1 | 724.3 | 20.76 | 0.0 | 10.0 | 13.78 | 14.6 | Surfboard-tg-mixed | 37.19.198.236 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.938 | 0.869 | 283 | 1772 | prefer |
| mheidari-all | 0.895 | 0.84 | 25 | 15701 | prefer |
| ermaozi | 0.808 | 0.805 | 41 | 431 | prefer |
| Surfboard-tg-mixed | 0.755 | 0.678 | 121 | 7422 | prefer |
| DeltaKronecker-all | 0.609 | 0.53 | 185 | 6070 | observe |
| tg-oneclickvpnkeys | 0.263 | 1.0 | 1 | 199 | observe |
| roosterkid-openproxylist-v2ray | 0.261 | 1.0 | 1 | 150 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4932 | observe |
| Epodonios-all | 0.255 | None | 0 | 7889 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 8749 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5995 | observe |
| barry-far-vless | 0.255 | None | 0 | 6213 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4223 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | ClientOSError | - | 56 |
| 204 | TimeoutError | - | 21 |
| speed | TimeoutError | - | 20 |
| 204 | ProxyError | - | 19 |
| geo | TimeoutError | - | 19 |
| cn-block | TimeoutError | - | 13 |
| cn-block | ClientOSError | - | 9 |
| 204 | ClientOSError | - | 7 |
| speed | ClientOSError | - | 6 |
| cn-block | ProxyError | - | 4 |
| geo | ProxyError | - | 3 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
