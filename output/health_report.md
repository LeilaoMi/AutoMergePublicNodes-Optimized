# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-13 05:14:04 |
| 运行耗时 | 1114.3s |
| 订阅源总数 | 107 |
| 健康订阅源 | 95 |
| 原始节点 | 94336 |
| 去重后节点 | 25332 |
| TCP 可达 | 3000 |
| 真实可用 | 537 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 25332 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.0 |
| geo | 1.4 |
| tcp | 42.2 |
| probe | 385.2 |
| real_test | 584.8 |
| generate | 93.7 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 57575 |
| vmess | 13631 |
| shadowsocks | 11014 |
| trojan | 9030 |
| hysteria2 | 2188 |
| http | 669 |
| shadowsocksr | 124 |
| socks | 64 |
| hysteria | 15 |
| anytls | 14 |
| tuic | 12 |

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
| 81.51 | vless | 294.0 | 721.7 | 20.97 | 0.0 | 10.0 | 10.9 | 19.64 | mheidari-all | 2.24.124.64 |
| 81.38 | shadowsocks | 239.9 | 638.4 | 22.22 | 0.0 | 10.0 | 13.52 | 19.64 | mheidari-all | 37.19.198.160 |
| 81.29 | shadowsocks | 244.0 | 651.8 | 22.13 | 0.0 | 10.0 | 13.52 | 19.64 | mheidari-all | 37.19.198.244 |
| 80.84 | vless | 246.4 | 619.0 | 22.08 | 0.0 | 10.0 | 10.9 | 17.86 | Au1rxx-base64 | 195.123.235.177 |
| 80.37 | vless | 266.4 | 736.3 | 21.61 | 0.0 | 10.0 | 10.9 | 17.86 | Au1rxx-base64 | 47.253.226.114 |
| 80.23 | vless | 272.5 | 740.1 | 21.47 | 0.0 | 10.0 | 10.9 | 17.86 | Au1rxx-base64 | 47.89.186.170 |
| 80.12 | hysteria2 | 279.8 | 767.3 | 21.3 | 0.0 | 8.73 | 13.33 | 17.86 | Au1rxx-base64 | 159.223.157.129 |
| 79.68 | vless | 296.4 | 784.6 | 20.92 | 0.0 | 10.0 | 10.9 | 17.86 | Au1rxx-base64 | 185.95.231.156 |
| 79.57 | vless | 300.9 | 722.9 | 20.81 | 0.0 | 10.0 | 10.9 | 17.86 | Au1rxx-base64 | 169.40.42.163 |
| 79.56 | shadowsocks | 254.1 | 631.8 | 21.9 | 0.0 | 10.0 | 13.52 | 19.64 | mheidari-all | 140.82.63.79 |
| 79.33 | vless | 311.3 | 836.9 | 20.57 | 0.0 | 10.0 | 10.9 | 17.86 | Au1rxx-base64 | 137.184.218.169 |
| 79.12 | vless | 320.3 | 844.8 | 20.36 | 0.0 | 10.0 | 10.9 | 17.86 | Au1rxx-base64 | 169.40.42.179 |
| 78.84 | vless | 308.3 | 689.0 | 20.64 | 0.0 | 10.0 | 10.9 | 17.86 | Au1rxx-base64 | 169.40.42.74 |
| 78.77 | vless | 249.1 | 650.8 | 22.01 | 0.0 | 10.0 | 10.9 | 17.86 | Au1rxx-base64 | 159.89.87.21 |
| 78.4 | vless | 296.3 | 767.4 | 20.92 | 0.0 | 8.72 | 10.9 | 17.86 | Au1rxx-base64 | 169.40.42.133 |
| 78.01 | shadowsocks | 278.2 | 631.6 | 21.34 | 0.0 | 10.0 | 13.52 | 19.64 | mheidari-all | 156.146.38.168 |
| 77.97 | vless | 370.1 | 866.2 | 19.21 | 0.0 | 10.0 | 10.9 | 17.86 | Au1rxx-base64 | 169.40.42.231 |
| 77.95 | vless | 347.8 | 871.9 | 19.73 | 0.0 | 10.0 | 10.9 | 17.86 | Au1rxx-base64 | 216.152.147.28 |
| 77.92 | vless | 316.8 | 825.0 | 20.44 | 0.0 | 8.72 | 10.9 | 17.86 | Au1rxx-base64 | 169.40.42.235 |
| 77.75 | vless | 357.0 | 889.8 | 19.51 | 0.0 | 10.0 | 10.9 | 17.86 | Au1rxx-base64 | 169.40.42.104 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.911 | 0.847 | 372 | 1653 | prefer |
| ermaozi | 0.71 | 0.708 | 24 | 436 | prefer |
| Surfboard-tg-mixed | 0.633 | 0.579 | 19 | 7432 | observe |
| mheidari-all | 0.353 | 0.272 | 511 | 20709 | observe |
| DeltaKronecker-all | 0.349 | 0.267 | 195 | 5970 | observe |
| xiaoji235-airport-v2ray-all | 0.335 | 1.0 | 1 | 5301 | observe |
| tg-oneclickvpnkeys | 0.26 | 1.0 | 1 | 127 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4793 | observe |
| Epodonios-all | 0.255 | None | 0 | 7895 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3996 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 8737 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 6027 | observe |
| barry-far-vless | 0.255 | None | 0 | 6259 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4295 | observe |
| Au1rxx-clash | 0.241 | None | 0 | 1653 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 211 |
| geo | ClientOSError | - | 109 |
| speed | ClientOSError | - | 107 |
| speed | TimeoutError | - | 70 |
| cn-block | ClientOSError | - | 51 |
| 204 | ProxyError | - | 15 |
| cn-block | TimeoutError | - | 15 |
| 204 | TimeoutError | - | 8 |
| 204 | ProxyConnectionError | - | 3 |
| geo | ProxyError | - | 3 |
| speed | ProxyError | - | 2 |
| cn-block | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
