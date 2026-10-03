# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-03 04:59:45 |
| 运行耗时 | 862.3s |
| 订阅源总数 | 107 |
| 健康订阅源 | 94 |
| 原始节点 | 98934 |
| 去重后节点 | 27176 |
| TCP 可达 | 3000 |
| 真实可用 | 453 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 27176 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.6 |
| geo | 1.2 |
| tcp | 47.4 |
| probe | 337.6 |
| real_test | 394.7 |
| generate | 75.8 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 60523 |
| vmess | 15585 |
| shadowsocks | 11418 |
| trojan | 8979 |
| hysteria2 | 1616 |
| http | 522 |
| shadowsocksr | 164 |
| socks | 68 |
| anytls | 30 |
| hysteria | 17 |
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
| 83.83 | vless | 260.4 | 632.2 | 21.75 | 0.0 | 10.0 | 12.98 | 19.1 | mheidari-all | 216.227.161.95 |
| 83.68 | vless | 278.9 | 669.4 | 21.32 | 0.0 | 10.0 | 12.98 | 19.38 | Au1rxx-base64 | 198.251.78.29 |
| 82.19 | hysteria2 | 275.8 | 532.8 | 21.39 | 0.0 | 10.0 | 13.57 | 19.38 | Au1rxx-base64 | 192.255.128.123 |
| 81.34 | vless | 227.3 | 573.8 | 22.52 | 0.0 | 8.46 | 12.98 | 19.38 | Au1rxx-base64 | us51.mech-pro.online |
| 81.16 | shadowsocks | 251.9 | 630.8 | 21.95 | 0.0 | 10.0 | 13.83 | 19.38 | Au1rxx-base64 | 156.146.38.168 |
| 81.09 | shadowsocks | 254.6 | 639.7 | 21.88 | 0.0 | 10.0 | 13.83 | 19.38 | Au1rxx-base64 | 156.146.38.167 |
| 81.07 | vless | 262.0 | 639.3 | 21.71 | 0.0 | 10.0 | 12.98 | 19.38 | Au1rxx-base64 | 38.180.254.125 |
| 81.06 | shadowsocks | 256.3 | 621.7 | 21.85 | 0.0 | 10.0 | 13.83 | 19.38 | Au1rxx-base64 | 156.146.38.170 |
| 80.69 | hysteria2 | 314.4 | 673.8 | 20.5 | 0.0 | 10.0 | 13.57 | 19.1 | mheidari-all | 159.223.157.129 |
| 80.47 | shadowsocks | 281.6 | 723.7 | 21.26 | 0.0 | 10.0 | 13.83 | 19.38 | Au1rxx-base64 | 156.146.38.169 |
| 80.01 | shadowsocks | 301.3 | 745.7 | 20.8 | 0.0 | 10.0 | 13.83 | 19.38 | Au1rxx-base64 | 37.19.198.244 |
| 79.87 | vless | 333.8 | 698.6 | 20.05 | 0.0 | 10.0 | 12.98 | 19.38 | Au1rxx-base64 | 169.40.42.104 |
| 79.66 | vless | 316.7 | 726.8 | 20.45 | 0.0 | 10.0 | 12.98 | 19.38 | Au1rxx-base64 | 159.89.87.21 |
| 79.61 | shadowsocks | 305.8 | 748.1 | 20.7 | 0.0 | 10.0 | 13.83 | 19.38 | Au1rxx-base64 | 37.19.198.243 |
| 79.5 | vless | 276.0 | 560.8 | 21.39 | 0.0 | 10.0 | 12.98 | 19.1 | mheidari-all | 47.251.108.158 |
| 79.46 | shadowsocks | 302.4 | 692.2 | 20.78 | 0.0 | 10.0 | 13.83 | 19.38 | Au1rxx-base64 | 140.82.63.79 |
| 79.21 | vless | 405.9 | 1003.4 | 18.38 | 0.0 | 10.0 | 12.98 | 19.38 | Au1rxx-base64 | 185.95.231.156 |
| 78.83 | vless | 359.8 | 806.4 | 19.45 | 0.0 | 10.0 | 12.98 | 19.38 | Au1rxx-base64 | 169.40.42.16 |
| 78.67 | vless | 295.8 | 597.2 | 20.93 | 0.0 | 10.0 | 12.98 | 19.38 | Au1rxx-base64 | 172.233.139.46 |
| 78.67 | vless | 329.7 | 680.5 | 20.15 | 0.0 | 10.0 | 12.98 | 19.38 | Au1rxx-base64 | 169.40.42.182 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.956 | 0.888 | 269 | 1751 | prefer |
| ermaozi | 0.949 | 0.958 | 24 | 645 | prefer |
| Surfboard-tg-mixed | 0.741 | 0.667 | 54 | 7256 | prefer |
| mheidari-all | 0.432 | 0.351 | 424 | 23323 | observe |
| ermaozi-get_subscribe | 0.341 | 0.75 | 4 | 516 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5276 | observe |
| DeltaKronecker-all | 0.255 | 0.222 | 9 | 4981 | observe |
| Epodonios-all | 0.255 | None | 0 | 7743 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9351 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5980 | observe |
| barry-far-vless | 0.255 | None | 0 | 6214 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4357 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 143 |
| speed | TimeoutError | - | 76 |
| geo | ClientOSError | - | 33 |
| cn-block | TimeoutError | - | 22 |
| 204 | ProxyError | - | 19 |
| speed | ClientOSError | - | 18 |
| 204 | TimeoutError | - | 8 |
| cn-block | ClientOSError | - | 6 |
| 204 | ClientOSError | - | 4 |
| cn-block | ProxyError | - | 2 |
| geo | ProxyError | - | 1 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
