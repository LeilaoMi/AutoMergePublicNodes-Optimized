# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-17 11:32:34 |
| 运行耗时 | 624.1s |
| 订阅源总数 | 107 |
| 健康订阅源 | 96 |
| 原始节点 | 86889 |
| 去重后节点 | 24175 |
| TCP 可达 | 3000 |
| 真实可用 | 421 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 24175 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.7 |
| geo | 1.4 |
| tcp | 40.4 |
| probe | 234.4 |
| real_test | 256.2 |
| generate | 84.0 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 51540 |
| vmess | 14007 |
| shadowsocks | 10463 |
| trojan | 8663 |
| hysteria2 | 1383 |
| http | 627 |
| shadowsocksr | 120 |
| socks | 74 |
| hysteria | 8 |
| tuic | 2 |
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
| 83.17 | hysteria2 | 240.1 | 668.9 | 22.22 | 0.0 | 10.0 | 13.27 | 18.78 | Au1rxx-base64 | 159.223.157.129 |
| 80.85 | shadowsocks | 260.2 | 728.7 | 21.76 | 0.0 | 10.0 | 14.31 | 18.78 | Au1rxx-base64 | 37.19.198.244 |
| 78.05 | shadowsocks | 273.0 | 708.0 | 21.46 | 0.0 | 10.0 | 14.31 | 18.78 | Au1rxx-base64 | 38.180.135.156 |
| 77.96 | hysteria2 | 291.7 | 582.2 | 21.03 | 0.0 | 10.0 | 13.27 | 18.78 | Au1rxx-base64 | 66.94.121.46 |
| 77.89 | shadowsocks | 366.1 | 1057.3 | 19.3 | 0.0 | 10.0 | 14.31 | 18.78 | Au1rxx-base64 | 15.204.247.206 |
| 77.25 | vless | 250.8 | 697.3 | 21.97 | 0.0 | 10.0 | 6.5 | 18.78 | Au1rxx-base64 | 79.141.172.154 |
| 77.16 | vless | 254.8 | 672.9 | 21.88 | 0.0 | 10.0 | 6.5 | 18.78 | Au1rxx-base64 | 169.40.42.89 |
| 76.95 | vless | 263.8 | 709.5 | 21.67 | 0.0 | 10.0 | 6.5 | 18.78 | Au1rxx-base64 | 185.95.231.156 |
| 76.67 | vless | 276.0 | 681.4 | 21.39 | 0.0 | 10.0 | 6.5 | 18.78 | Au1rxx-base64 | 169.40.42.90 |
| 76.02 | shadowsocks | 326.5 | 784.7 | 20.22 | 0.0 | 10.0 | 14.31 | 18.78 | Au1rxx-base64 | 156.146.38.169 |
| 75.99 | vless | 297.5 | 700.8 | 20.89 | 0.0 | 10.0 | 6.5 | 18.78 | Au1rxx-base64 | 169.40.42.223 |
| 75.81 | vless | 312.9 | 847.0 | 20.53 | 0.0 | 10.0 | 6.5 | 18.78 | Au1rxx-base64 | 169.40.42.16 |
| 75.68 | vless | 318.6 | 830.9 | 20.4 | 0.0 | 10.0 | 6.5 | 18.78 | Au1rxx-base64 | 66.70.179.198 |
| 75.64 | vless | 320.4 | 754.5 | 20.36 | 0.0 | 10.0 | 6.5 | 18.78 | Au1rxx-base64 | 169.40.42.104 |
| 75.47 | vless | 327.6 | 889.9 | 20.19 | 0.0 | 10.0 | 6.5 | 18.78 | Au1rxx-base64 | 169.40.42.74 |
| 75.47 | vless | 327.9 | 771.5 | 20.19 | 0.0 | 10.0 | 6.5 | 18.78 | Au1rxx-base64 | 169.40.42.184 |
| 75.43 | vless | 329.6 | 838.5 | 20.15 | 0.0 | 10.0 | 6.5 | 18.78 | Au1rxx-base64 | 216.152.147.28 |
| 75.14 | shadowsocks | 277.2 | 646.3 | 21.36 | 0.0 | 10.0 | 14.31 | 16.6 | Surfboard-tg-mixed | 156.146.38.168 |
| 74.88 | vless | 353.3 | 846.6 | 19.6 | 0.0 | 10.0 | 6.5 | 18.78 | Au1rxx-base64 | 169.40.42.202 |
| 74.8 | vless | 356.7 | 936.2 | 19.52 | 0.0 | 10.0 | 6.5 | 18.78 | Au1rxx-base64 | 169.40.42.163 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.882 | 0.818 | 274 | 1663 | prefer |
| mheidari-all | 0.756 | 0.682 | 66 | 16008 | prefer |
| ermaozi | 0.753 | 0.745 | 55 | 396 | prefer |
| DeltaKronecker-all | 0.617 | 0.538 | 39 | 5931 | observe |
| Surfboard-tg-mixed | 0.61 | 0.53 | 149 | 7408 | observe |
| ermaozi-get_subscribe | 0.362 | 0.333 | 27 | 431 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| tg-oneclickvpnkeys | 0.26 | 1.0 | 1 | 129 | observe |
| Epodonios-all | 0.255 | None | 0 | 7867 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 8871 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5925 | observe |
| barry-far-vless | 0.255 | None | 0 | 6149 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4179 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 2484 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | ProxyError | - | 38 |
| 204 | TimeoutError | - | 30 |
| geo | ClientOSError | - | 28 |
| cn-block | TimeoutError | - | 22 |
| speed | TimeoutError | - | 21 |
| geo | TimeoutError | - | 19 |
| cn-block | ClientOSError | - | 14 |
| speed | ClientOSError | - | 10 |
| 204 | ClientOSError | - | 8 |
| geo | ProxyError | - | 2 |
| 204 | ProxyConnectionError | - | 1 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
