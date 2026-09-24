# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-24 04:25:56 |
| 运行耗时 | 1026.6s |
| 订阅源总数 | 107 |
| 健康订阅源 | 95 |
| 原始节点 | 96874 |
| 去重后节点 | 26610 |
| TCP 可达 | 3000 |
| 真实可用 | 554 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 26610 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.0 |
| geo | 1.4 |
| tcp | 43.0 |
| probe | 352.9 |
| real_test | 549.5 |
| generate | 75.8 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 59127 |
| vmess | 14786 |
| shadowsocks | 11176 |
| trojan | 9244 |
| hysteria2 | 1562 |
| http | 669 |
| shadowsocksr | 170 |
| socks | 89 |
| anytls | 24 |
| hysteria | 19 |
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
| 81.6 | vless | 289.2 | 711.8 | 21.08 | 0.0 | 9.38 | 11.96 | 19.18 | Au1rxx-base64 | 79.141.172.154 |
| 81.46 | vless | 264.1 | 666.2 | 21.66 | 0.0 | 9.38 | 11.96 | 19.18 | Au1rxx-base64 | 195.211.98.43 |
| 80.98 | hysteria2 | 281.2 | 606.5 | 21.27 | 0.0 | 10.0 | 13.33 | 19.18 | Au1rxx-base64 | 66.94.121.46 |
| 78.65 | shadowsocks | 251.4 | 638.9 | 21.96 | 0.0 | 10.0 | 12.99 | 17.7 | mheidari-all | 156.146.38.168 |
| 78.46 | shadowsocks | 259.5 | 647.3 | 21.77 | 0.0 | 10.0 | 12.99 | 17.7 | mheidari-all | 156.146.38.170 |
| 77.95 | vless | 313.2 | 681.7 | 20.53 | 0.0 | 9.4 | 11.96 | 19.18 | Au1rxx-base64 | 169.40.42.184 |
| 77.69 | vless | 357.4 | 867.7 | 19.51 | 0.0 | 10.0 | 11.96 | 19.18 | Au1rxx-base64 | 185.95.231.233 |
| 77.22 | shadowsocks | 268.4 | 598.7 | 21.57 | 0.0 | 10.0 | 12.99 | 17.7 | mheidari-all | 23.150.248.20 |
| 77.18 | vless | 303.1 | 603.8 | 20.76 | 0.0 | 9.38 | 11.96 | 19.18 | Au1rxx-base64 | 172.235.43.210 |
| 77.1 | vless | 438.6 | 1107.2 | 17.62 | 0.0 | 10.0 | 11.96 | 19.18 | Au1rxx-base64 | 34.85.179.6 |
| 76.95 | shadowsocks | 253.1 | 630.1 | 21.92 | 0.0 | 10.0 | 12.99 | 16.04 | Surfboard-tg-mixed | 156.146.38.169 |
| 76.86 | vless | 381.9 | 924.8 | 18.94 | 0.0 | 9.4 | 11.96 | 19.18 | Au1rxx-base64 | 137.184.218.169 |
| 76.85 | shadowsocks | 257.6 | 629.6 | 21.82 | 0.0 | 10.0 | 12.99 | 16.04 | Surfboard-tg-mixed | 156.146.38.167 |
| 76.81 | vless | 328.9 | 843.6 | 20.16 | 0.0 | 10.0 | 11.96 | 17.7 | mheidari-all | 216.227.161.95 |
| 76.72 | vless | 330.7 | 709.9 | 20.12 | 0.0 | 9.39 | 11.96 | 19.18 | Au1rxx-base64 | 169.40.42.212 |
| 76.5 | vless | 445.6 | 1085.4 | 17.46 | 0.0 | 10.0 | 11.96 | 19.18 | Au1rxx-base64 | 23.132.28.51 |
| 76.41 | shadowsocks | 305.7 | 757.6 | 20.7 | 0.0 | 10.0 | 12.99 | 17.7 | mheidari-all | 37.19.198.236 |
| 76.27 | vless | 394.5 | 902.9 | 18.65 | 0.0 | 9.38 | 11.96 | 19.18 | Au1rxx-base64 | 169.40.42.35 |
| 76.27 | vless | 400.5 | 912.1 | 18.51 | 0.0 | 10.0 | 11.96 | 19.18 | Au1rxx-base64 | 66.70.179.198 |
| 76.26 | vless | 337.0 | 721.6 | 19.98 | 0.0 | 10.0 | 11.96 | 19.18 | Au1rxx-base64 | 5.78.139.175 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.969 | 0.906 | 255 | 1648 | prefer |
| Surfboard-tg-mixed | 0.862 | 0.788 | 99 | 7099 | prefer |
| ermaozi | 0.6 | 0.593 | 27 | 339 | observe |
| mheidari-all | 0.409 | 0.329 | 681 | 22298 | observe |
| mahdibland-V2RayAggregator | 0.335 | 1.0 | 1 | 4332 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5131 | observe |
| Epodonios-all | 0.255 | None | 0 | 7563 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 8881 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5729 | observe |
| barry-far-vless | 0.255 | None | 0 | 5948 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |
| ninja-vless | 0.251 | 0.333 | 3 | 1791 | observe |
| Au1rxx-clash | 0.241 | None | 0 | 1648 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 215 |
| speed | TimeoutError | - | 82 |
| cn-block | ClientOSError | - | 54 |
| geo | ClientOSError | - | 53 |
| speed | ClientOSError | - | 38 |
| 204 | TimeoutError | - | 32 |
| 204 | ProxyError | - | 29 |
| cn-block | TimeoutError | - | 20 |
| cn-block | ProxyError | - | 2 |
| 204 | ClientOSError | - | 2 |
| speed | ClientPayloadError | - | 1 |
| geo | parse | ClientPayloadError | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
