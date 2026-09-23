# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-23 21:29:21 |
| 运行耗时 | 536.4s |
| 订阅源总数 | 107 |
| 健康订阅源 | 95 |
| 原始节点 | 96813 |
| 去重后节点 | 26642 |
| TCP 可达 | 3000 |
| 真实可用 | 406 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 26642 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.6 |
| geo | 1.5 |
| tcp | 43.1 |
| probe | 247.2 |
| real_test | 158.3 |
| generate | 79.6 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 59376 |
| vmess | 14844 |
| shadowsocks | 11129 |
| trojan | 9067 |
| hysteria2 | 1486 |
| http | 601 |
| shadowsocksr | 177 |
| socks | 82 |
| anytls | 25 |
| hysteria | 18 |
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
| 81.95 | shadowsocks | 222.5 | 525.5 | 22.63 | 0.0 | 10.0 | 13.52 | 19.8 | Au1rxx-base64 | 173.244.56.6 |
| 81.72 | hysteria2 | 307.6 | 689.1 | 20.66 | 0.0 | 10.0 | 13.5 | 19.8 | Au1rxx-base64 | 66.94.121.46 |
| 81.6 | vless | 202.9 | 534.1 | 23.08 | 0.0 | 9.48 | 9.24 | 19.8 | Au1rxx-base64 | 172.235.43.210 |
| 80.84 | shadowsocks | 257.8 | 626.4 | 21.81 | 0.0 | 10.0 | 13.52 | 19.8 | Au1rxx-base64 | 156.146.38.169 |
| 80.28 | vless | 208.5 | 513.4 | 22.95 | 0.0 | 9.48 | 9.24 | 19.8 | Au1rxx-base64 | 195.123.240.65 |
| 79.08 | shadowsocks | 262.6 | 640.3 | 21.7 | 0.0 | 9.49 | 13.52 | 19.8 | Au1rxx-base64 | 156.146.38.168 |
| 77.1 | vless | 203.9 | 523.5 | 23.06 | 0.0 | 10.0 | 9.24 | 19.8 | Au1rxx-base64 | 192.3.247.109 |
| 76.21 | shadowsocks | 315.8 | 695.9 | 20.47 | 0.0 | 10.0 | 13.52 | 19.8 | Au1rxx-base64 | 149.22.95.183 |
| 75.89 | vless | 331.5 | 769.3 | 20.11 | 0.0 | 10.0 | 9.24 | 19.8 | Au1rxx-base64 | 15.204.97.216 |
| 75.64 | vless | 219.4 | 537.8 | 22.7 | 0.0 | 10.0 | 9.24 | 19.8 | Au1rxx-base64 | 172.67.130.159 |
| 74.51 | vless | 198.3 | 515.2 | 23.19 | 0.0 | 10.0 | 9.24 | 12.08 | Surfboard-tg-mixed | 172.235.38.85 |
| 74.45 | vless | 288.5 | 657.6 | 21.1 | 0.0 | 9.48 | 9.24 | 19.8 | Au1rxx-base64 | 5.78.28.48 |
| 74.3 | shadowsocks | 193.2 | 507.7 | 23.3 | 0.0 | 10.0 | 13.52 | 11.98 | mheidari-all | 192.3.247.109 |
| 74.18 | vless | 244.6 | 499.7 | 22.12 | 0.0 | 9.52 | 9.24 | 19.8 | Au1rxx-base64 | 162.159.48.32 |
| 74.04 | vless | 271.2 | 483.7 | 21.5 | 0.0 | 10.0 | 9.24 | 19.8 | Au1rxx-base64 | 162.159.43.187 |
| 73.22 | shadowsocks | 239.9 | 599.7 | 22.22 | 0.0 | 10.0 | 13.52 | 11.98 | mheidari-all | 108.181.118.10 |
| 73.21 | shadowsocks | 244.8 | 604.3 | 22.11 | 0.0 | 10.0 | 13.52 | 12.08 | Surfboard-tg-mixed | 108.181.0.177 |
| 73.2 | shadowsocks | 262.8 | 639.0 | 21.7 | 0.0 | 10.0 | 13.52 | 11.98 | mheidari-all | 156.146.38.170 |
| 72.96 | shadowsocks | 277.1 | 664.5 | 21.36 | 0.0 | 10.0 | 13.52 | 12.08 | Surfboard-tg-mixed | 173.244.56.9 |
| 72.53 | shadowsocks | 261.4 | 629.4 | 21.73 | 0.0 | 10.0 | 13.52 | 12.08 | Surfboard-tg-mixed | 156.146.38.167 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.959 | 0.897 | 252 | 1635 | prefer |
| mheidari-all | 0.885 | 0.812 | 85 | 22531 | prefer |
| Surfboard-tg-mixed | 0.802 | 0.726 | 113 | 7072 | prefer |
| ermaozi | 0.793 | 0.8 | 30 | 291 | prefer |
| DeltaKronecker-all | 0.438 | 1.0 | 3 | 6471 | observe |
| mahdibland-V2RayAggregator | 0.335 | 1.0 | 1 | 4332 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5131 | observe |
| Epodonios-all | 0.255 | None | 0 | 7534 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 8842 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5711 | observe |
| barry-far-vless | 0.255 | None | 0 | 5930 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.24 | None | 0 | 1635 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| cn-block | TimeoutError | - | 20 |
| 204 | ProxyError | - | 11 |
| cn-block | ClientOSError | - | 11 |
| 204 | TimeoutError | - | 10 |
| speed | TimeoutError | - | 7 |
| geo | TimeoutError | - | 7 |
| 204 | ProxyConnectionError | - | 6 |
| 204 | ClientOSError | - | 5 |
| speed | ClientOSError | - | 4 |
| cn-block | ProxyError | - | 3 |
| geo | ClientOSError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
