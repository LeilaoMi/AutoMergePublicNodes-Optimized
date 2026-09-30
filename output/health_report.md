# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-30 05:12:52 |
| 运行耗时 | 783.4s |
| 订阅源总数 | 107 |
| 健康订阅源 | 94 |
| 原始节点 | 96916 |
| 去重后节点 | 27039 |
| TCP 可达 | 3000 |
| 真实可用 | 361 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 27039 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.0 |
| geo | 1.5 |
| tcp | 46.1 |
| probe | 305.5 |
| real_test | 387.7 |
| generate | 36.7 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 58711 |
| vmess | 15141 |
| shadowsocks | 11343 |
| trojan | 9330 |
| hysteria2 | 1447 |
| http | 643 |
| shadowsocksr | 166 |
| socks | 75 |
| anytls | 37 |
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
| 82.74 | hysteria2 | 241.4 | 554.5 | 22.19 | 0.0 | 9.51 | 14.4 | 17.64 | Au1rxx-base64 | 192.255.128.123 |
| 80.46 | vless | 239.8 | 534.4 | 22.23 | 0.0 | 10.0 | 11.47 | 18.32 | mheidari-all | 47.251.108.158 |
| 79.97 | vless | 275.3 | 627.0 | 21.4 | 0.0 | 10.0 | 11.47 | 18.32 | mheidari-all | 216.227.161.95 |
| 79.1 | shadowsocks | 242.9 | 622.5 | 22.16 | 0.0 | 9.52 | 13.78 | 17.64 | Au1rxx-base64 | 156.146.38.169 |
| 79.09 | shadowsocks | 243.7 | 623.1 | 22.14 | 0.0 | 9.53 | 13.78 | 17.64 | Au1rxx-base64 | 156.146.38.167 |
| 78.52 | shadowsocks | 312.7 | 742.5 | 20.54 | 0.0 | 10.0 | 13.78 | 19.6 | Surfboard-tg-mixed | 5.78.51.123 |
| 77.59 | http | 246.1 | 549.6 | 22.08 | 0.0 | 10.0 | 12.79 | 17.2 | ermaozi | 138.199.35.207 |
| 77.58 | http | 247.3 | 546.5 | 22.05 | 0.0 | 10.0 | 12.79 | 17.2 | ermaozi | 138.199.35.216 |
| 77.41 | vless | 268.6 | 577.0 | 21.56 | 0.0 | 10.0 | 11.47 | 19.6 | Surfboard-tg-mixed | 172.235.38.85 |
| 77.34 | http | 251.1 | 561.9 | 21.97 | 0.0 | 10.0 | 12.79 | 17.2 | ermaozi | 138.199.35.214 |
| 76.41 | shadowsocks | 254.5 | 566.5 | 21.89 | 0.0 | 10.0 | 13.78 | 18.32 | mheidari-all | 192.3.247.109 |
| 76.33 | http | 252.8 | 548.6 | 21.92 | 0.0 | 10.0 | 12.79 | 17.2 | ermaozi | 138.199.35.215 |
| 75.09 | shadowsocks | 292.0 | 583.2 | 21.02 | 0.0 | 10.0 | 13.78 | 19.6 | Surfboard-tg-mixed | 173.244.56.9 |
| 74.94 | http | 252.1 | 567.6 | 21.94 | 0.0 | 10.0 | 12.79 | 17.2 | ermaozi | 138.199.35.210 |
| 74.83 | shadowsocks | 312.4 | 693.2 | 20.55 | 0.0 | 10.0 | 13.78 | 19.6 | Surfboard-tg-mixed | 108.181.0.177 |
| 74.78 | shadowsocks | 276.8 | 589.6 | 21.37 | 0.0 | 9.47 | 13.78 | 17.64 | Au1rxx-base64 | 173.244.56.6 |
| 74.69 | hysteria2 | 264.4 | 252.7 | 21.66 | 5.52 | 6.0 | 14.4 | 17.64 | Au1rxx-base64 | open.w2m.ink |
| 74.33 | shadowsocks | 273.5 | 539.6 | 21.45 | 0.0 | 9.51 | 13.78 | 17.64 | Au1rxx-base64 | 108.181.118.10 |
| 74.29 | hysteria2 | 352.1 | 732.9 | 19.63 | 0.0 | 10.0 | 14.4 | 17.64 | Au1rxx-base64 | 159.223.157.129 |
| 74.26 | shadowsocks | 341.5 | 726.5 | 19.87 | 0.0 | 10.0 | 13.78 | 19.6 | Surfboard-tg-mixed | 140.82.63.79 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | 0.96 | 100 | 1756 | prefer |
| ermaozi | 0.797 | 0.8 | 35 | 335 | prefer |
| Surfboard-tg-mixed | 0.702 | 0.623 | 146 | 7024 | prefer |
| DeltaKronecker-all | 0.48 | 1.0 | 4 | 5528 | observe |
| mheidari-all | 0.398 | 0.317 | 429 | 22586 | observe |
| tg-oneclickvpnkeys | 0.361 | 1.0 | 3 | 74 | observe |
| ermaozi-get_subscribe | 0.334 | 0.75 | 4 | 353 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5314 | observe |
| Epodonios-all | 0.255 | None | 0 | 7591 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9347 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5656 | observe |
| barry-far-vless | 0.255 | None | 0 | 5895 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4338 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 158 |
| speed | TimeoutError | - | 53 |
| geo | ClientOSError | - | 51 |
| speed | ClientOSError | - | 43 |
| 204 | ProxyError | - | 21 |
| 204 | TimeoutError | - | 16 |
| cn-block | TimeoutError | - | 9 |
| 204 | ClientOSError | - | 6 |
| cn-block | ProxyError | - | 2 |
| cn-block | ClientOSError | - | 1 |
| geo | parse | TimeoutError | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
