# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-24 21:30:15 |
| 运行耗时 | 502.1s |
| 订阅源总数 | 107 |
| 健康订阅源 | 94 |
| 原始节点 | 98134 |
| 去重后节点 | 26548 |
| TCP 可达 | 3000 |
| 真实可用 | 370 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 26548 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.3 |
| geo | 1.4 |
| tcp | 43.5 |
| probe | 214.8 |
| real_test | 159.8 |
| generate | 77.3 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 60228 |
| vmess | 14904 |
| shadowsocks | 11269 |
| trojan | 9246 |
| hysteria2 | 1598 |
| http | 592 |
| shadowsocksr | 174 |
| socks | 76 |
| anytls | 22 |
| hysteria | 18 |
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
| 84.53 | vless | 204.2 | 531.7 | 23.05 | 0.0 | 10.0 | 12.48 | 19.0 | mheidari-all | 172.233.139.46 |
| 83.82 | vless | 208.6 | 532.8 | 22.95 | 0.0 | 8.63 | 12.48 | 19.76 | Au1rxx-base64 | 172.235.43.210 |
| 83.38 | vless | 254.0 | 597.3 | 21.9 | 0.0 | 10.0 | 12.48 | 19.0 | mheidari-all | 47.251.108.158 |
| 82.71 | vless | 257.6 | 672.1 | 21.82 | 0.0 | 8.65 | 12.48 | 19.76 | Au1rxx-base64 | 195.123.240.65 |
| 82.13 | vless | 203.1 | 510.5 | 23.08 | 0.0 | 8.81 | 12.48 | 19.76 | Au1rxx-base64 | 192.3.247.109 |
| 81.52 | shadowsocks | 193.8 | 511.5 | 23.29 | 0.0 | 10.0 | 13.73 | 19.0 | mheidari-all | 192.3.247.109 |
| 80.41 | shadowsocks | 241.9 | 601.3 | 22.18 | 0.0 | 10.0 | 13.73 | 19.0 | mheidari-all | 108.181.118.10 |
| 79.98 | trojan | 249.1 | 669.8 | 22.01 | 0.0 | 10.0 | 11.47 | 19.0 | mheidari-all | 34.94.125.227 |
| 78.52 | trojan | 264.3 | 547.9 | 21.66 | 0.0 | 10.0 | 11.47 | 19.0 | mheidari-all | 100.42.228.109 |
| 78.36 | vless | 332.6 | 761.3 | 20.08 | 0.0 | 8.63 | 12.48 | 19.76 | Au1rxx-base64 | 79.141.172.154 |
| 78.1 | vless | 276.1 | 636.5 | 21.39 | 0.0 | 8.72 | 12.48 | 19.76 | Au1rxx-base64 | 172.64.32.103 |
| 77.79 | shadowsocks | 219.4 | 550.1 | 22.7 | 0.0 | 10.0 | 13.73 | 15.86 | Surfboard-tg-mixed | 108.181.0.177 |
| 77.7 | shadowsocks | 278.0 | 620.7 | 21.34 | 0.0 | 10.0 | 13.73 | 19.0 | mheidari-all | 23.150.248.20 |
| 77.36 | vless | 297.3 | 513.7 | 20.9 | 0.0 | 8.72 | 12.48 | 19.76 | Au1rxx-base64 | 172.64.32.108 |
| 77.22 | shadowsocks | 265.7 | 678.4 | 21.63 | 0.0 | 10.0 | 13.73 | 15.86 | Surfboard-tg-mixed | 173.244.56.6 |
| 76.33 | vless | 340.8 | 652.3 | 19.89 | 0.0 | 8.7 | 12.48 | 19.76 | Au1rxx-base64 | 172.64.229.170 |
| 76.29 | vless | 338.4 | 729.9 | 19.94 | 0.0 | 8.61 | 12.48 | 19.76 | Au1rxx-base64 | 136.117.218.86 |
| 75.51 | vless | 352.9 | 715.7 | 19.61 | 0.0 | 8.67 | 12.48 | 19.76 | Au1rxx-base64 | 195.211.98.43 |
| 75.46 | vless | 259.3 | 499.5 | 21.77 | 0.0 | 8.7 | 12.48 | 19.76 | Au1rxx-base64 | 172.64.158.146 |
| 75.46 | vless | 327.9 | 754.1 | 20.19 | 0.0 | 10.0 | 12.48 | 19.0 | mheidari-all | 216.227.161.95 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.977 | 0.915 | 260 | 1626 | prefer |
| Surfboard-tg-mixed | 0.868 | 1.0 | 15 | 7419 | prefer |
| mheidari-all | 0.68 | 0.601 | 173 | 22744 | observe |
| ermaozi | 0.455 | 0.533 | 15 | 298 | observe |
| DeltaKronecker-all | 0.391 | 1.0 | 2 | 5845 | observe |
| mahdibland-V2RayAggregator | 0.335 | 1.0 | 1 | 4405 | observe |
| ermaozi-get_subscribe | 0.267 | 1.0 | 1 | 304 | observe |
| tg-oneclickvpnkeys | 0.258 | 1.0 | 1 | 65 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5307 | observe |
| Epodonios-all | 0.255 | None | 0 | 7888 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3996 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9086 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5963 | observe |
| barry-far-vless | 0.255 | None | 0 | 6215 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| cn-block | ClientOSError | - | 42 |
| 204 | TimeoutError | - | 15 |
| cn-block | TimeoutError | - | 14 |
| 204 | ProxyError | - | 9 |
| speed | TimeoutError | - | 5 |
| cn-block | ProxyError | - | 4 |
| speed | ClientOSError | - | 4 |
| geo | TimeoutError | - | 3 |
| 204 | ClientOSError | - | 2 |
| geo | ProxyError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
