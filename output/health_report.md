# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-13 14:09:00 |
| 运行耗时 | 816.1s |
| 订阅源总数 | 107 |
| 健康订阅源 | 94 |
| 原始节点 | 99026 |
| 去重后节点 | 27337 |
| TCP 可达 | 3000 |
| 真实可用 | 430 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 27337 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 8.3 |
| geo | 1.5 |
| tcp | 47.6 |
| probe | 338.3 |
| real_test | 330.8 |
| generate | 89.6 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 58308 |
| vmess | 16033 |
| shadowsocks | 12006 |
| trojan | 10667 |
| hysteria2 | 1299 |
| http | 435 |
| shadowsocksr | 169 |
| socks | 59 |
| anytls | 26 |
| hysteria | 18 |
| tuic | 6 |

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
| 84.7 | hysteria2 | 229.8 | 580.7 | 22.46 | 0.0 | 10.0 | 13.42 | 19.82 | Au1rxx-base64 | 66.94.121.46 |
| 82.1 | trojan | 299.2 | 736.1 | 20.85 | 0.0 | 10.0 | 13.93 | 19.82 | Au1rxx-base64 | pro-mako.rooster465.autos |
| 80.37 | shadowsocks | 257.5 | 568.3 | 21.82 | 0.0 | 10.0 | 14.38 | 19.82 | Au1rxx-base64 | 173.244.56.6 |
| 80.01 | shadowsocks | 254.6 | 564.9 | 21.88 | 0.0 | 10.0 | 14.38 | 19.82 | Au1rxx-base64 | 173.244.56.9 |
| 78.71 | shadowsocks | 271.0 | 275.6 | 21.51 | 4.67 | 9.94 | 14.38 | 19.82 | Au1rxx-base64 | 149.22.87.204 |
| 78.41 | vless | 192.6 | 509.6 | 23.32 | 0.0 | 10.0 | 5.27 | 19.82 | Au1rxx-base64 | 23.95.222.127 |
| 78.24 | trojan | 260.0 | 623.1 | 21.76 | 0.0 | 10.0 | 13.93 | 19.82 | Au1rxx-base64 | 107.149.159.190 |
| 78.21 | vless | 201.3 | 521.5 | 23.12 | 0.0 | 10.0 | 5.27 | 19.82 | Au1rxx-base64 | 144.202.126.147 |
| 78.05 | vless | 208.3 | 511.9 | 22.96 | 0.0 | 10.0 | 5.27 | 19.82 | Au1rxx-base64 | 107.173.237.146 |
| 77.53 | vless | 230.5 | 525.6 | 22.44 | 0.0 | 10.0 | 5.27 | 19.82 | Au1rxx-base64 | 195.123.240.65 |
| 77.32 | vless | 239.8 | 595.2 | 22.23 | 0.0 | 10.0 | 5.27 | 19.82 | Au1rxx-base64 | 154.12.38.159 |
| 77.32 | shadowsocks | 305.4 | 672.1 | 20.71 | 0.0 | 10.0 | 14.38 | 19.82 | Au1rxx-base64 | 156.146.38.169 |
| 77.06 | vless | 207.8 | 538.1 | 22.97 | 0.0 | 10.0 | 5.27 | 19.82 | Au1rxx-base64 | 154.40.55.185 |
| 76.16 | shadowsocks | 294.8 | 339.9 | 20.95 | 2.25 | 9.94 | 14.38 | 19.82 | Au1rxx-base64 | 149.22.87.241 |
| 76.0 | shadowsocks | 293.6 | 336.9 | 20.98 | 2.37 | 9.94 | 14.38 | 19.82 | Au1rxx-base64 | 149.22.87.240 |
| 75.98 | shadowsocks | 312.3 | 686.9 | 20.55 | 0.0 | 10.0 | 14.38 | 19.82 | Au1rxx-base64 | 156.146.38.167 |
| 75.75 | trojan | 363.6 | 311.5 | 19.36 | 3.32 | 9.93 | 13.93 | 19.82 | Au1rxx-base64 | 43.206.225.188 |
| 75.4 | trojan | 333.2 | 337.7 | 20.06 | 2.34 | 9.38 | 13.93 | 19.82 | Au1rxx-base64 | warm-krill.rooster465.autos |
| 75.34 | trojan | 333.5 | 339.5 | 20.06 | 2.27 | 9.38 | 13.93 | 19.82 | Au1rxx-base64 | allowed-poodle.rooster465.autos |
| 74.9 | trojan | 333.9 | 348.0 | 20.05 | 1.95 | 9.94 | 13.93 | 19.82 | Au1rxx-base64 | 45.32.52.173 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.944 | 0.876 | 323 | 1754 | prefer |
| mheidari-all | 0.847 | 0.78 | 41 | 24075 | prefer |
| Surfboard-tg-mixed | 0.76 | 0.683 | 120 | 7201 | prefer |
| DeltaKronecker-all | 0.642 | 0.567 | 30 | 5076 | observe |
| zhangkai | 0.587 | 0.833 | 12 | 144 | observe |
| ermaozi-get_subscribe | 0.34 | 0.3 | 20 | 534 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5086 | observe |
| Epodonios-all | 0.255 | None | 0 | 7717 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9931 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5723 | observe |
| barry-far-vless | 0.255 | None | 0 | 5973 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4312 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| cn-block | TimeoutError | - | 30 |
| 204 | TimeoutError | - | 26 |
| 204 | ProxyError | - | 16 |
| geo | ClientOSError | - | 11 |
| geo | TimeoutError | - | 11 |
| cn-block | ClientOSError | - | 7 |
| speed | ClientOSError | - | 5 |
| cn-block | ProxyError | - | 4 |
| speed | TimeoutError | - | 3 |
| 204 | ProxyConnectionError | - | 2 |
| 204 | ClientOSError | - | 2 |
| speed | ProxyError | - | 1 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
