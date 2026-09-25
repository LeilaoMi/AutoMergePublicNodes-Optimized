# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-25 04:34:40 |
| 运行耗时 | 751.0s |
| 订阅源总数 | 107 |
| 健康订阅源 | 94 |
| 原始节点 | 97834 |
| 去重后节点 | 26576 |
| TCP 可达 | 3000 |
| 真实可用 | 455 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 26576 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.1 |
| geo | 1.6 |
| tcp | 43.8 |
| probe | 265.0 |
| real_test | 356.8 |
| generate | 77.7 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 59346 |
| vmess | 15086 |
| shadowsocks | 11809 |
| trojan | 9001 |
| hysteria2 | 1647 |
| http | 649 |
| shadowsocksr | 175 |
| socks | 74 |
| anytls | 24 |
| hysteria | 16 |
| tuic | 7 |

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
| 81.86 | vless | 256.0 | 611.0 | 21.85 | 0.0 | 9.55 | 10.92 | 19.54 | Au1rxx-base64 | 195.211.98.43 |
| 80.98 | vless | 293.5 | 722.7 | 20.98 | 0.0 | 9.54 | 10.92 | 19.54 | Au1rxx-base64 | 79.141.172.154 |
| 80.84 | shadowsocks | 244.9 | 637.3 | 22.11 | 0.0 | 9.53 | 13.66 | 19.54 | Au1rxx-base64 | 156.146.38.167 |
| 80.62 | shadowsocks | 254.6 | 645.9 | 21.88 | 0.0 | 9.54 | 13.66 | 19.54 | Au1rxx-base64 | 156.146.38.170 |
| 79.72 | shadowsocks | 271.1 | 627.8 | 21.5 | 0.0 | 9.52 | 13.66 | 19.54 | Au1rxx-base64 | 23.150.248.20 |
| 79.2 | hysteria2 | 411.2 | 1077.7 | 18.26 | 0.0 | 10.0 | 13.5 | 19.54 | Au1rxx-base64 | 159.223.157.129 |
| 78.49 | shadowsocks | 300.9 | 743.1 | 20.81 | 0.0 | 9.51 | 13.66 | 19.54 | Au1rxx-base64 | 37.19.198.244 |
| 78.38 | shadowsocks | 305.7 | 749.4 | 20.7 | 0.0 | 9.58 | 13.66 | 19.54 | Au1rxx-base64 | 37.19.198.236 |
| 78.2 | vless | 329.8 | 687.5 | 20.14 | 0.0 | 9.56 | 10.92 | 19.54 | Au1rxx-base64 | 169.40.42.232 |
| 78.12 | shadowsocks | 341.9 | 900.9 | 19.86 | 0.0 | 9.56 | 13.66 | 19.54 | Au1rxx-base64 | 185.156.47.97 |
| 77.98 | shadowsocks | 307.6 | 752.9 | 20.66 | 0.0 | 9.52 | 13.66 | 19.54 | Au1rxx-base64 | 37.19.198.160 |
| 77.83 | vless | 318.3 | 681.9 | 20.41 | 0.0 | 10.0 | 10.92 | 19.54 | Au1rxx-base64 | 169.40.42.168 |
| 77.44 | shadowsocks | 343.3 | 831.3 | 19.83 | 0.0 | 9.52 | 13.66 | 19.54 | Au1rxx-base64 | 142.4.216.225 |
| 77.07 | vless | 374.6 | 892.3 | 19.11 | 0.0 | 9.54 | 10.92 | 19.54 | Au1rxx-base64 | 169.40.42.182 |
| 76.95 | vless | 357.0 | 725.7 | 19.51 | 0.0 | 9.56 | 10.92 | 19.54 | Au1rxx-base64 | 169.40.42.184 |
| 76.56 | vless | 353.7 | 786.9 | 19.59 | 0.0 | 10.0 | 10.92 | 19.54 | Au1rxx-base64 | 158.69.112.254 |
| 76.55 | shadowsocks | 300.3 | 742.8 | 20.83 | 0.0 | 10.0 | 13.66 | 17.36 | Surfboard-tg-mixed | 37.19.198.243 |
| 76.29 | shadowsocks | 309.6 | 741.0 | 20.61 | 0.0 | 9.58 | 13.66 | 19.54 | Au1rxx-base64 | 15.204.233.41 |
| 76.19 | vless | 385.6 | 925.9 | 18.85 | 0.0 | 10.0 | 10.92 | 19.54 | Au1rxx-base64 | 159.89.87.21 |
| 76.14 | vless | 427.6 | 1075.7 | 17.88 | 0.0 | 9.55 | 10.92 | 19.54 | Au1rxx-base64 | 185.95.231.156 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.975 | 0.91 | 266 | 1702 | prefer |
| Surfboard-tg-mixed | 0.791 | 0.714 | 185 | 7399 | prefer |
| ermaozi | 0.514 | 0.5 | 26 | 338 | observe |
| DeltaKronecker-all | 0.352 | 0.364 | 11 | 5845 | observe |
| mahdibland-V2RayAggregator | 0.335 | 1.0 | 1 | 4405 | observe |
| mheidari-all | 0.304 | 0.222 | 270 | 22554 | observe |
| tg-oneclickvpnkeys | 0.258 | 1.0 | 1 | 80 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5307 | observe |
| Epodonios-all | 0.255 | None | 0 | 7876 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9018 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5862 | observe |
| barry-far-vless | 0.255 | None | 0 | 6091 | observe |
| Au1rxx-clash | 0.243 | None | 0 | 1701 | observe |
| ermaozi-get_subscribe | 0.234 | 0.4 | 5 | 359 | downweight |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 128 |
| speed | TimeoutError | - | 49 |
| geo | ClientOSError | - | 36 |
| cn-block | ClientOSError | - | 28 |
| speed | ClientOSError | - | 22 |
| 204 | ProxyError | - | 15 |
| cn-block | TimeoutError | - | 15 |
| 204 | TimeoutError | - | 8 |
| 204 | ProxyConnectionError | - | 7 |
| geo | ProxyError | - | 3 |
| cn-block | ProxyError | - | 2 |
| speed | ClientPayloadError | - | 1 |
| 204 | ClientOSError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
