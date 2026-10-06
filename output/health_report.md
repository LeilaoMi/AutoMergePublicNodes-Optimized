# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-06 22:40:08 |
| 运行耗时 | 444.8s |
| 订阅源总数 | 107 |
| 健康订阅源 | 94 |
| 原始节点 | 97769 |
| 去重后节点 | 27067 |
| TCP 可达 | 3000 |
| 真实可用 | 472 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 27067 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.8 |
| geo | 1.5 |
| tcp | 44.7 |
| probe | 188.6 |
| real_test | 168.2 |
| generate | 34.0 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 57630 |
| vmess | 15982 |
| shadowsocks | 11597 |
| trojan | 10104 |
| hysteria2 | 1424 |
| http | 704 |
| shadowsocksr | 164 |
| socks | 103 |
| anytls | 36 |
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
| 85.26 | hysteria2 | 239.1 | 657.2 | 22.24 | 0.0 | 10.0 | 14.12 | 20.0 | Au1rxx-base64 | 159.223.157.129 |
| 84.82 | hysteria2 | 241.0 | 695.6 | 22.2 | 0.0 | 10.0 | 14.12 | 20.0 | Au1rxx-base64 | 129.213.91.185 |
| 83.97 | vless | 256.8 | 686.5 | 21.83 | 0.0 | 10.0 | 12.14 | 20.0 | Au1rxx-base64 | 137.184.218.169 |
| 83.43 | vless | 280.1 | 535.5 | 21.29 | 0.0 | 10.0 | 12.14 | 20.0 | Au1rxx-base64 | 195.123.235.177 |
| 83.3 | vless | 281.0 | 705.4 | 21.27 | 0.0 | 10.0 | 12.14 | 20.0 | Au1rxx-base64 | 66.70.179.198 |
| 82.93 | vless | 301.9 | 835.6 | 20.79 | 0.0 | 10.0 | 12.14 | 20.0 | Au1rxx-base64 | 159.89.87.21 |
| 82.67 | vless | 263.9 | 715.5 | 21.67 | 0.0 | 8.86 | 12.14 | 20.0 | Au1rxx-base64 | ww9.levikogjgfdd.ir |
| 82.14 | vless | 336.1 | 727.2 | 20.0 | 0.0 | 10.0 | 12.14 | 20.0 | Au1rxx-base64 | 169.40.42.74 |
| 81.82 | vless | 349.9 | 744.5 | 19.68 | 0.0 | 10.0 | 12.14 | 20.0 | Au1rxx-base64 | 169.40.42.179 |
| 81.5 | shadowsocks | 252.3 | 704.3 | 21.94 | 0.0 | 10.0 | 13.56 | 20.0 | Au1rxx-base64 | 37.19.198.236 |
| 81.46 | shadowsocks | 254.0 | 705.2 | 21.9 | 0.0 | 10.0 | 13.56 | 20.0 | Au1rxx-base64 | 37.19.198.244 |
| 81.44 | vless | 347.8 | 830.2 | 19.73 | 0.0 | 10.0 | 12.14 | 20.0 | Au1rxx-base64 | 169.40.42.232 |
| 81.36 | shadowsocks | 258.2 | 718.4 | 21.8 | 0.0 | 10.0 | 13.56 | 20.0 | Au1rxx-base64 | 37.19.198.243 |
| 81.32 | vless | 371.3 | 1025.6 | 19.18 | 0.0 | 10.0 | 12.14 | 20.0 | Au1rxx-base64 | 185.95.231.156 |
| 81.31 | vless | 371.7 | 972.0 | 19.17 | 0.0 | 10.0 | 12.14 | 20.0 | Au1rxx-base64 | 2.24.124.64 |
| 81.01 | vless | 384.7 | 991.7 | 18.87 | 0.0 | 10.0 | 12.14 | 20.0 | Au1rxx-base64 | 169.40.42.168 |
| 80.75 | shadowsocks | 284.7 | 799.2 | 21.19 | 0.0 | 10.0 | 13.56 | 20.0 | Au1rxx-base64 | 37.19.198.160 |
| 80.58 | vless | 403.4 | 1056.6 | 18.44 | 0.0 | 10.0 | 12.14 | 20.0 | Au1rxx-base64 | 169.40.42.95 |
| 80.45 | vless | 300.8 | 737.6 | 20.81 | 0.0 | 10.0 | 12.14 | 20.0 | Au1rxx-base64 | 169.40.42.90 |
| 80.33 | vless | 414.1 | 1028.3 | 18.19 | 0.0 | 10.0 | 12.14 | 20.0 | Au1rxx-base64 | 169.40.42.133 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | 0.951 | 326 | 1829 | prefer |
| mheidari-all | 0.942 | 0.873 | 63 | 23303 | prefer |
| Surfboard-tg-mixed | 0.856 | 0.781 | 105 | 7055 | prefer |
| ermaozi | 0.448 | 0.417 | 48 | 708 | observe |
| DeltaKronecker-all | 0.349 | 0.667 | 3 | 4889 | observe |
| tg-OutlineReleasedKey | 0.257 | 1.0 | 1 | 52 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4990 | observe |
| Epodonios-all | 0.255 | None | 0 | 7604 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9213 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5593 | observe |
| barry-far-vless | 0.255 | None | 0 | 5954 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4373 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |
| Au1rxx-clash | 0.248 | None | 0 | 1829 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | ProxyError | - | 27 |
| 204 | TimeoutError | - | 12 |
| cn-block | TimeoutError | - | 9 |
| speed | ClientOSError | - | 6 |
| cn-block | ClientOSError | - | 6 |
| speed | TimeoutError | - | 6 |
| 204 | ProxyConnectionError | - | 5 |
| geo | ClientOSError | - | 5 |
| 204 | ClientOSError | - | 4 |
| geo | TimeoutError | - | 4 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
