# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-07 13:10:52 |
| 运行耗时 | 563.2s |
| 订阅源总数 | 107 |
| 健康订阅源 | 94 |
| 原始节点 | 98660 |
| 去重后节点 | 27302 |
| TCP 可达 | 3000 |
| 真实可用 | 406 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 27302 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.7 |
| geo | 1.3 |
| tcp | 45.6 |
| probe | 272.6 |
| real_test | 160.2 |
| generate | 78.8 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 57830 |
| vmess | 15977 |
| shadowsocks | 11588 |
| trojan | 10878 |
| hysteria2 | 1463 |
| http | 610 |
| shadowsocksr | 161 |
| socks | 92 |
| anytls | 34 |
| hysteria | 17 |
| tuic | 10 |

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
| 82.39 | hysteria2 | 284.0 | 720.3 | 21.2 | 0.0 | 10.0 | 13.33 | 19.36 | Au1rxx-base64 | 129.213.91.185 |
| 81.58 | shadowsocks | 248.5 | 638.9 | 22.02 | 0.0 | 10.0 | 14.2 | 19.36 | Au1rxx-base64 | 156.146.38.170 |
| 81.27 | shadowsocks | 255.9 | 639.4 | 21.85 | 0.0 | 10.0 | 14.2 | 19.36 | Au1rxx-base64 | 156.146.38.169 |
| 80.3 | shadowsocks | 304.0 | 783.0 | 20.74 | 0.0 | 10.0 | 14.2 | 19.36 | Au1rxx-base64 | 156.146.38.168 |
| 80.28 | shadowsocks | 305.0 | 754.2 | 20.72 | 0.0 | 10.0 | 14.2 | 19.36 | Au1rxx-base64 | 37.19.198.236 |
| 80.03 | shadowsocks | 315.8 | 791.8 | 20.47 | 0.0 | 10.0 | 14.2 | 19.36 | Au1rxx-base64 | 37.19.198.244 |
| 79.61 | shadowsocks | 297.9 | 682.8 | 20.88 | 0.0 | 10.0 | 14.2 | 19.36 | Au1rxx-base64 | 140.82.63.79 |
| 79.11 | hysteria2 | 286.7 | 287.6 | 21.14 | 4.21 | 8.89 | 13.33 | 19.36 | Au1rxx-base64 | open.2ml.bid |
| 78.7 | hysteria2 | 288.1 | 258.0 | 21.11 | 5.32 | 9.48 | 13.33 | 19.36 | Au1rxx-base64 | 158.101.148.79 |
| 78.62 | shadowsocks | 298.4 | 740.5 | 20.87 | 0.0 | 10.0 | 14.2 | 19.36 | Au1rxx-base64 | 37.19.198.160 |
| 78.22 | shadowsocks | 330.8 | 830.0 | 20.12 | 0.0 | 10.0 | 14.2 | 19.36 | Au1rxx-base64 | 37.19.198.243 |
| 77.26 | shadowsocks | 323.1 | 768.7 | 20.3 | 0.0 | 10.0 | 14.2 | 19.36 | Au1rxx-base64 | 15.204.233.41 |
| 75.96 | shadowsocks | 384.2 | 966.9 | 18.88 | 0.0 | 10.0 | 14.2 | 19.36 | Au1rxx-base64 | 15.204.246.132 |
| 75.12 | shadowsocks | 301.7 | 602.5 | 20.79 | 0.0 | 10.0 | 14.2 | 19.36 | Au1rxx-base64 | 173.244.56.6 |
| 75.04 | shadowsocks | 340.2 | 783.0 | 19.9 | 0.0 | 10.0 | 14.2 | 19.36 | Au1rxx-base64 | 5.78.51.123 |
| 74.95 | shadowsocks | 243.9 | 592.6 | 22.13 | 0.0 | 10.0 | 14.2 | 19.36 | Au1rxx-base64 | 156.146.38.167 |
| 74.51 | hysteria2 | 337.5 | 445.2 | 19.97 | 0.0 | 9.59 | 13.33 | 19.36 | Au1rxx-base64 | 132.226.14.77 |
| 73.4 | trojan | 379.1 | 782.6 | 19.0 | 0.0 | 10.0 | 12.88 | 19.36 | Au1rxx-base64 | 34.220.15.24 |
| 72.9 | vless | 278.0 | 570.1 | 21.34 | 0.0 | 10.0 | 6.33 | 19.36 | Au1rxx-base64 | 47.251.108.158 |
| 72.89 | shadowsocks | 395.7 | 865.8 | 18.62 | 0.0 | 10.0 | 14.2 | 19.36 | Au1rxx-base64 | 108.181.0.177 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.969 | 0.898 | 334 | 1830 | prefer |
| mheidari-all | 0.873 | 0.804 | 56 | 23381 | prefer |
| Surfboard-tg-mixed | 0.678 | 0.6 | 85 | 7069 | observe |
| ermaozi | 0.447 | 0.444 | 18 | 664 | observe |
| tg-OutlineReleasedKey | 0.257 | 1.0 | 1 | 50 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5138 | observe |
| DeltaKronecker-all | 0.255 | None | 0 | 5344 | observe |
| Epodonios-all | 0.255 | None | 0 | 7480 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9550 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5616 | observe |
| barry-far-vless | 0.255 | None | 0 | 5861 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4418 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |
| Au1rxx-clash | 0.248 | None | 0 | 1830 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | ProxyError | - | 23 |
| cn-block | TimeoutError | - | 22 |
| 204 | TimeoutError | - | 21 |
| speed | ClientOSError | - | 9 |
| geo | ClientOSError | - | 7 |
| 204 | ClientOSError | - | 4 |
| cn-block | ProxyError | - | 2 |
| speed | TimeoutError | - | 2 |
| cn-block | ClientOSError | - | 2 |
| geo | TimeoutError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
