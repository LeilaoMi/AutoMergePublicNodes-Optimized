# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-02 22:08:31 |
| 运行耗时 | 429.1s |
| 订阅源总数 | 107 |
| 健康订阅源 | 94 |
| 原始节点 | 98974 |
| 去重后节点 | 27178 |
| TCP 可达 | 3000 |
| 真实可用 | 413 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 27178 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.7 |
| geo | 0.9 |
| tcp | 46.3 |
| probe | 195.3 |
| real_test | 145.2 |
| generate | 33.7 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 60740 |
| vmess | 15479 |
| shadowsocks | 11438 |
| trojan | 8931 |
| hysteria2 | 1566 |
| http | 522 |
| shadowsocksr | 166 |
| socks | 67 |
| anytls | 40 |
| hysteria | 17 |
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
| 80.33 | vless | 253.1 | 691.0 | 21.92 | 0.0 | 10.0 | 10.55 | 17.86 | Au1rxx-base64 | 159.89.87.21 |
| 79.8 | vless | 274.1 | 654.5 | 21.43 | 0.0 | 10.0 | 10.55 | 17.86 | Au1rxx-base64 | 169.40.42.212 |
| 79.8 | vless | 276.2 | 636.1 | 21.39 | 0.0 | 10.0 | 10.55 | 17.86 | Au1rxx-base64 | 169.40.42.104 |
| 79.56 | vless | 286.3 | 717.6 | 21.15 | 0.0 | 10.0 | 10.55 | 17.86 | Au1rxx-base64 | 2.24.124.64 |
| 79.54 | vless | 287.3 | 720.1 | 21.13 | 0.0 | 10.0 | 10.55 | 17.86 | Au1rxx-base64 | 66.70.179.198 |
| 79.53 | hysteria2 | 237.0 | 655.5 | 22.29 | 0.0 | 10.0 | 12.0 | 16.34 | mheidari-all | 159.223.157.129 |
| 79.4 | vless | 293.4 | 674.3 | 20.99 | 0.0 | 10.0 | 10.55 | 17.86 | Au1rxx-base64 | 169.40.42.235 |
| 79.0 | shadowsocks | 258.7 | 719.2 | 21.79 | 0.0 | 10.0 | 13.35 | 17.86 | Au1rxx-base64 | 37.19.198.243 |
| 78.97 | vless | 300.1 | 725.9 | 20.83 | 0.0 | 10.0 | 10.55 | 17.86 | Au1rxx-base64 | 209.200.246.148 |
| 78.7 | vless | 323.4 | 752.8 | 20.29 | 0.0 | 10.0 | 10.55 | 17.86 | Au1rxx-base64 | 169.40.42.202 |
| 78.67 | vless | 324.9 | 824.0 | 20.26 | 0.0 | 10.0 | 10.55 | 17.86 | Au1rxx-base64 | 169.40.42.182 |
| 78.59 | vless | 316.8 | 817.9 | 20.44 | 0.0 | 10.0 | 10.55 | 17.86 | Au1rxx-base64 | 169.40.42.179 |
| 78.45 | vless | 334.3 | 792.5 | 20.04 | 0.0 | 10.0 | 10.55 | 17.86 | Au1rxx-base64 | 169.40.42.16 |
| 78.24 | shadowsocks | 270.0 | 698.9 | 21.53 | 0.0 | 10.0 | 13.35 | 17.86 | Au1rxx-base64 | 140.82.63.79 |
| 78.14 | vless | 347.7 | 819.4 | 19.73 | 0.0 | 10.0 | 10.55 | 17.86 | Au1rxx-base64 | 169.40.42.133 |
| 77.93 | vless | 356.6 | 845.1 | 19.52 | 0.0 | 10.0 | 10.55 | 17.86 | Au1rxx-base64 | 169.40.42.74 |
| 77.87 | vless | 356.4 | 862.4 | 19.53 | 0.0 | 10.0 | 10.55 | 17.86 | Au1rxx-base64 | 169.40.42.225 |
| 77.31 | vless | 266.2 | 651.6 | 21.62 | 0.0 | 10.0 | 10.55 | 17.86 | Au1rxx-base64 | 169.40.42.231 |
| 77.3 | vless | 307.5 | 680.0 | 20.66 | 0.0 | 10.0 | 10.55 | 17.86 | Au1rxx-base64 | 198.251.78.29 |
| 77.23 | vless | 387.2 | 946.2 | 18.82 | 0.0 | 10.0 | 10.55 | 17.86 | Au1rxx-base64 | 169.40.42.52 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.969 | 0.901 | 294 | 1771 | prefer |
| mheidari-all | 0.955 | 0.882 | 102 | 23213 | prefer |
| Surfboard-tg-mixed | 0.94 | 0.875 | 48 | 7321 | prefer |
| ermaozi | 0.64 | 0.625 | 24 | 620 | observe |
| DeltaKronecker-all | 0.335 | 1.0 | 1 | 4981 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5276 | observe |
| Epodonios-all | 0.255 | None | 0 | 7814 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9326 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5999 | observe |
| barry-far-vless | 0.255 | None | 0 | 6241 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4357 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.246 | None | 0 | 1771 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| cn-block | TimeoutError | - | 18 |
| 204 | ProxyConnectionError | - | 8 |
| 204 | TimeoutError | - | 8 |
| 204 | ProxyError | - | 5 |
| speed | TimeoutError | - | 5 |
| speed | ClientOSError | - | 4 |
| cn-block | ClientOSError | - | 3 |
| cn-block | ProxyError | - | 2 |
| 204 | ClientOSError | - | 2 |
| geo | TimeoutError | - | 2 |
| geo | ClientOSError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
