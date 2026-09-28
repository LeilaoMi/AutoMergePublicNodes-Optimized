# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-28 05:01:50 |
| 运行耗时 | 920.9s |
| 订阅源总数 | 107 |
| 健康订阅源 | 94 |
| 原始节点 | 95255 |
| 去重后节点 | 26814 |
| TCP 可达 | 3000 |
| 真实可用 | 535 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 26814 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.3 |
| geo | 1.5 |
| tcp | 43.6 |
| probe | 326.6 |
| real_test | 467.3 |
| generate | 74.6 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 57657 |
| vmess | 14873 |
| shadowsocks | 11468 |
| trojan | 8887 |
| hysteria2 | 1450 |
| http | 621 |
| shadowsocksr | 176 |
| socks | 76 |
| anytls | 24 |
| hysteria | 15 |
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
| 83.77 | hysteria2 | 228.4 | 567.4 | 22.49 | 0.0 | 10.0 | 14.38 | 17.9 | Au1rxx-base64 | 66.94.121.46 |
| 83.11 | hysteria2 | 213.6 | 526.7 | 22.83 | 0.0 | 10.0 | 14.38 | 17.9 | Au1rxx-base64 | 192.255.128.123 |
| 82.06 | vless | 201.6 | 525.6 | 23.11 | 0.0 | 10.0 | 11.05 | 17.9 | Au1rxx-base64 | 172.235.43.210 |
| 82.04 | vless | 202.3 | 532.2 | 23.09 | 0.0 | 10.0 | 11.05 | 17.9 | Au1rxx-base64 | 172.235.38.85 |
| 82.01 | vless | 203.7 | 519.7 | 23.06 | 0.0 | 10.0 | 11.05 | 17.9 | Au1rxx-base64 | 192.3.247.109 |
| 81.81 | vless | 212.3 | 534.1 | 22.86 | 0.0 | 10.0 | 11.05 | 17.9 | Au1rxx-base64 | 195.123.240.65 |
| 81.38 | vless | 231.2 | 640.5 | 22.43 | 0.0 | 10.0 | 11.05 | 17.9 | Au1rxx-base64 | 137.175.82.40 |
| 81.33 | vless | 233.3 | 571.7 | 22.38 | 0.0 | 10.0 | 11.05 | 17.9 | Au1rxx-base64 | 15.204.97.216 |
| 80.65 | vless | 262.5 | 675.6 | 21.7 | 0.0 | 10.0 | 11.05 | 17.9 | Au1rxx-base64 | 5.78.159.214 |
| 80.39 | vless | 273.8 | 751.3 | 21.44 | 0.0 | 10.0 | 11.05 | 17.9 | Au1rxx-base64 | 23.95.222.127 |
| 78.96 | shadowsocks | 225.3 | 532.7 | 22.56 | 0.0 | 10.0 | 12.82 | 17.9 | Au1rxx-base64 | 173.244.56.9 |
| 78.25 | shadowsocks | 200.0 | 491.6 | 23.15 | 0.0 | 10.0 | 12.82 | 16.78 | Surfboard-tg-mixed | 108.181.118.10 |
| 77.7 | shadowsocks | 188.5 | 502.9 | 23.42 | 0.0 | 10.0 | 12.82 | 15.96 | mheidari-all | 192.3.247.109 |
| 76.37 | shadowsocks | 281.2 | 728.3 | 21.27 | 0.0 | 10.0 | 12.82 | 16.78 | Surfboard-tg-mixed | 108.181.0.177 |
| 76.24 | vless | 237.0 | 573.8 | 22.29 | 0.0 | 10.0 | 11.05 | 17.9 | Au1rxx-base64 | 15.204.97.195 |
| 75.31 | shadowsocks | 336.1 | 814.8 | 20.0 | 0.0 | 8.98 | 12.82 | 17.9 | Au1rxx-base64 | 173.244.56.6 |
| 74.53 | shadowsocks | 279.3 | 778.2 | 21.31 | 0.0 | 10.0 | 12.82 | 17.9 | Au1rxx-base64 | 103.214.109.42 |
| 74.52 | vless | 203.6 | 469.0 | 23.07 | 0.0 | 10.0 | 11.05 | 17.9 | Au1rxx-base64 | 188.114.97.6 |
| 74.49 | vless | 312.6 | 811.5 | 20.54 | 0.0 | 10.0 | 11.05 | 17.9 | Au1rxx-base64 | 15.204.97.197 |
| 73.95 | vless | 551.7 | 1402.8 | 15.01 | 0.0 | 10.0 | 11.05 | 17.9 | Au1rxx-base64 | 51.81.203.63 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.912 | 0.857 | 329 | 1437 | prefer |
| Surfboard-tg-mixed | 0.784 | 0.706 | 204 | 6916 | prefer |
| ermaozi | 0.642 | 0.634 | 41 | 347 | observe |
| mheidari-all | 0.297 | 0.215 | 367 | 22305 | observe |
| DeltaKronecker-all | 0.263 | 0.25 | 8 | 5466 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5327 | observe |
| Epodonios-all | 0.255 | None | 0 | 7506 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9195 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5591 | observe |
| barry-far-vless | 0.255 | None | 0 | 5817 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4185 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.232 | None | 0 | 1437 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 158 |
| speed | TimeoutError | - | 73 |
| geo | ClientOSError | - | 64 |
| speed | ClientOSError | - | 51 |
| cn-block | TimeoutError | - | 23 |
| 204 | TimeoutError | - | 19 |
| 204 | ProxyError | - | 16 |
| 204 | ProxyConnectionError | - | 10 |
| 204 | ClientOSError | - | 3 |
| cn-block | ClientOSError | - | 3 |
| sing-box exited 1 |  [31mFATAL[0m[0000] start service: start inbound/socks[socks-in]: listen tcp 127.0.0.1:32349: bind: address already in use | - | 1 |
| cn-block | ProxyError | - | 1 |
| speed | ProxyError | - | 1 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
