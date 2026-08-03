# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-03 14:55:24 |
| 运行耗时 | 252.8s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 83610 |
| 去重后节点 | 24688 |
| TCP 可达 | 3000 |
| 真实可用 | 486 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 24688 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.7 |
| geo | 1.6 |
| tcp | 37.6 |
| probe | 58.0 |
| real_test | 116.8 |
| generate | 32.2 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 50828 |
| vmess | 12741 |
| shadowsocks | 10446 |
| trojan | 8614 |
| hysteria2 | 731 |
| http | 86 |
| socks | 71 |
| shadowsocksr | 71 |
| hysteria | 10 |
| anytls | 7 |
| tuic | 5 |

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
| 84.88 | http | 207.2 | 492.0 | 22.98 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.216 |
| 84.39 | http | 228.6 | 588.7 | 22.49 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.211 |
| 79.1 | http | 456.8 | 1284.0 | 17.2 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.218 |
| 77.07 | vless | 180.0 | 458.7 | 23.61 | 0.0 | 10.0 | 7.26 | 16.2 | Au1rxx-base64 | 70.39.198.93 |
| 77.01 | shadowsocks | 203.3 | 490.2 | 23.07 | 0.0 | 10.0 | 12.24 | 16.2 | Au1rxx-base64 | 108.181.0.177 |
| 76.85 | shadowsocks | 232.0 | 523.6 | 22.41 | 0.0 | 10.0 | 12.24 | 16.2 | Au1rxx-base64 | 173.244.56.9 |
| 76.79 | vless | 192.3 | 453.2 | 23.33 | 0.0 | 10.0 | 7.26 | 16.2 | Au1rxx-base64 | 70.39.198.183 |
| 76.77 | vless | 192.9 | 489.6 | 23.31 | 0.0 | 10.0 | 7.26 | 16.2 | Au1rxx-base64 | 192.204.50.220 |
| 76.6 | vless | 200.5 | 520.1 | 23.14 | 0.0 | 10.0 | 7.26 | 16.2 | Au1rxx-base64 | 172.247.109.66 |
| 76.47 | shadowsocks | 248.1 | 604.2 | 22.03 | 0.0 | 10.0 | 12.24 | 16.2 | Au1rxx-base64 | 149.22.95.183 |
| 76.19 | shadowsocks | 239.0 | 602.2 | 22.25 | 0.0 | 10.0 | 12.24 | 16.2 | Au1rxx-base64 | 108.181.118.10 |
| 76.04 | vless | 224.4 | 583.0 | 22.58 | 0.0 | 10.0 | 7.26 | 16.2 | Au1rxx-base64 | 70.39.178.231 |
| 75.66 | vless | 241.1 | 615.9 | 22.2 | 0.0 | 10.0 | 7.26 | 16.2 | Au1rxx-base64 | 70.39.197.13 |
| 74.74 | vless | 280.5 | 806.0 | 21.28 | 0.0 | 10.0 | 7.26 | 16.2 | Au1rxx-base64 | 66.175.217.170 |
| 74.45 | vless | 278.3 | 629.6 | 21.34 | 0.0 | 10.0 | 7.26 | 16.2 | Au1rxx-base64 | 52.43.158.158 |
| 74.12 | shadowsocks | 220.2 | 529.1 | 22.68 | 0.0 | 10.0 | 12.24 | 16.2 | Au1rxx-base64 | 173.244.56.6 |
| 73.91 | hysteria2 | 353.0 | 725.2 | 19.61 | 0.0 | 10.0 | 13.57 | 16.2 | Au1rxx-base64 | 159.223.157.129 |
| 73.42 | trojan | 297.0 | 640.6 | 20.9 | 0.0 | 10.0 | 12.66 | 16.2 | Au1rxx-base64 | 64.94.95.114 |
| 73.36 | trojan | 302.0 | 649.5 | 20.79 | 0.0 | 10.0 | 12.66 | 16.2 | Au1rxx-base64 | 64.94.95.117 |
| 73.3 | trojan | 296.9 | 642.7 | 20.91 | 0.0 | 10.0 | 12.66 | 16.2 | Au1rxx-base64 | 64.94.95.118 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.976 | 0.986 | 69 | 92 | prefer |
| Au1rxx-base64 | 0.8 | 0.734 | 518 | 1692 | prefer |
| DeltaKronecker-all | 0.402 | 0.316 | 19 | 6205 | observe |
| mheidari-all | 0.361 | 0.4 | 10 | 18776 | observe |
| xiaoji235-airport-v2ray-all | 0.335 | 1.0 | 1 | 3833 | observe |
| Surfboard-tg-mixed | 0.332 | 0.248 | 105 | 5293 | observe |
| tg-OutlineReleasedKey | 0.257 | 1.0 | 1 | 54 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5285 | observe |
| Epodonios-all | 0.255 | None | 0 | 5890 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6783 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4162 | observe |
| barry-far-vless | 0.255 | None | 0 | 4526 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5196 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | ClientOSError | - | 74 |
| 204 | TimeoutError | - | 46 |
| geo | TimeoutError | - | 29 |
| 204 | ProxyError | - | 24 |
| speed | TimeoutError | - | 21 |
| speed | ClientOSError | - | 20 |
| cn-block | ProxyError | - | 8 |
| cn-block | TimeoutError | - | 7 |
| cn-block | ClientOSError | - | 4 |
| 204 | ClientOSError | - | 3 |
| geo | ProxyError | - | 2 |
| sing-box exited 1 |  [31mFATAL[0m[0000] start service: start inbound/socks[socks-in]: listen tcp 127.0.0.1:41974: bind: address already in use | - | 1 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
