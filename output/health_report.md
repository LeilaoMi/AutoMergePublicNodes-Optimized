# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-26 21:03:15 |
| 运行耗时 | 586.5s |
| 订阅源总数 | 107 |
| 健康订阅源 | 93 |
| 原始节点 | 96520 |
| 去重后节点 | 26455 |
| TCP 可达 | 3000 |
| 真实可用 | 403 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 26455 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.0 |
| geo | 1.4 |
| tcp | 43.5 |
| probe | 262.0 |
| real_test | 188.9 |
| generate | 85.7 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 58929 |
| vmess | 14943 |
| shadowsocks | 11304 |
| trojan | 8927 |
| hysteria2 | 1509 |
| http | 611 |
| shadowsocksr | 170 |
| socks | 77 |
| anytls | 25 |
| hysteria | 15 |
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
| 82.02 | vless | 208.9 | 515.3 | 22.94 | 0.0 | 9.03 | 11.33 | 18.72 | Au1rxx-base64 | 195.123.240.65 |
| 81.91 | vless | 212.2 | 510.0 | 22.87 | 0.0 | 8.99 | 11.33 | 18.72 | Au1rxx-base64 | 137.175.82.40 |
| 80.35 | vless | 278.1 | 737.5 | 21.34 | 0.0 | 8.96 | 11.33 | 18.72 | Au1rxx-base64 | 38.244.20.25 |
| 79.28 | vless | 201.7 | 532.9 | 23.11 | 0.0 | 10.0 | 11.33 | 14.84 | mheidari-all | 172.233.139.46 |
| 78.96 | vless | 215.6 | 507.1 | 22.79 | 0.0 | 10.0 | 11.33 | 14.84 | mheidari-all | 47.251.108.158 |
| 78.64 | hysteria2 | 248.2 | 292.2 | 22.03 | 4.04 | 7.84 | 12.86 | 18.72 | Au1rxx-base64 | open.w2m.ink |
| 78.23 | vless | 205.4 | 535.9 | 23.02 | 0.0 | 10.0 | 11.33 | 13.88 | Surfboard-tg-mixed | 172.235.38.85 |
| 77.73 | vless | 219.1 | 506.6 | 22.71 | 0.0 | 8.97 | 11.33 | 18.72 | Au1rxx-base64 | 173.249.207.28 |
| 77.32 | shadowsocks | 272.7 | 701.2 | 21.47 | 0.0 | 8.94 | 12.19 | 18.72 | Au1rxx-base64 | 173.244.56.6 |
| 76.86 | shadowsocks | 261.3 | 639.2 | 21.73 | 0.0 | 9.01 | 12.19 | 18.72 | Au1rxx-base64 | 156.146.38.169 |
| 76.61 | vless | 338.8 | 769.2 | 19.93 | 0.0 | 8.97 | 11.33 | 18.72 | Au1rxx-base64 | 79.141.172.154 |
| 75.98 | shadowsocks | 186.9 | 504.7 | 23.45 | 0.0 | 10.0 | 12.19 | 14.84 | mheidari-all | 192.3.247.109 |
| 75.87 | vless | 243.0 | 553.5 | 22.15 | 0.0 | 8.17 | 11.33 | 18.72 | Au1rxx-base64 | www.fbi.gov |
| 75.14 | vless | 354.4 | 841.6 | 19.58 | 0.0 | 8.97 | 11.33 | 18.72 | Au1rxx-base64 | 51.81.203.63 |
| 74.92 | shadowsocks | 254.5 | 625.7 | 21.89 | 0.0 | 10.0 | 12.19 | 14.84 | mheidari-all | 156.146.38.170 |
| 74.33 | shadowsocks | 216.9 | 548.8 | 22.76 | 0.0 | 10.0 | 12.19 | 13.88 | Surfboard-tg-mixed | 108.181.0.177 |
| 74.18 | shadowsocks | 223.2 | 545.5 | 22.61 | 0.0 | 10.0 | 12.19 | 13.88 | Surfboard-tg-mixed | 108.181.118.10 |
| 74.17 | vless | 234.2 | 489.4 | 22.36 | 0.0 | 9.15 | 11.33 | 18.72 | Au1rxx-base64 | 162.159.24.131 |
| 74.15 | shadowsocks | 280.2 | 288.4 | 21.29 | 4.18 | 8.98 | 12.19 | 18.72 | Au1rxx-base64 | 149.22.87.240 |
| 74.07 | vless | 272.9 | 465.3 | 21.46 | 0.0 | 9.06 | 11.33 | 18.72 | Au1rxx-base64 | 172.64.229.2 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.951 | 0.888 | 277 | 1654 | prefer |
| Surfboard-tg-mixed | 0.824 | 0.75 | 84 | 7263 | prefer |
| mheidari-all | 0.574 | 0.494 | 158 | 22366 | observe |
| ermaozi | 0.487 | 0.529 | 17 | 296 | observe |
| mahdibland-V2RayAggregator | 0.335 | 1.0 | 1 | 4355 | observe |
| 10ium-HighSpeed | 0.289 | 1.0 | 1 | 839 | observe |
| xiaoji235-airport-v2ray-all | 0.287 | 0.5 | 2 | 6752 | observe |
| tg-oneclickvpnkeys | 0.258 | 1.0 | 1 | 66 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5242 | observe |
| Epodonios-all | 0.255 | None | 0 | 7740 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3995 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 8923 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5823 | observe |
| barry-far-vless | 0.255 | None | 0 | 6052 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| cn-block | ClientOSError | - | 49 |
| 204 | TimeoutError | - | 38 |
| cn-block | TimeoutError | - | 18 |
| 204 | ProxyError | - | 13 |
| speed | TimeoutError | - | 11 |
| geo | TimeoutError | - | 8 |
| speed | ClientOSError | - | 3 |
| cn-block | ProxyError | - | 2 |
| speed | ProxyError | - | 2 |
| sing-box exited 1 |  [31mFATAL[0m[0000] start service: start inbound/socks[socks-in]: listen tcp 127.0.0.1:32653: bind: address already in use | - | 1 |
| geo | ClientOSError | - | 1 |
| 204 | ClientOSError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
