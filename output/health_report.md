# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-14 21:33:04 |
| 运行耗时 | 288.3s |
| 订阅源总数 | 107 |
| 健康订阅源 | 93 |
| 原始节点 | 98750 |
| 去重后节点 | 27406 |
| TCP 可达 | 3000 |
| 真实可用 | 69 |
| Verified 输出 | 69 |
| Global 输出 | 74 |
| All 输出 | 27406 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.6 |
| geo | 1.6 |
| tcp | 86.1 |
| probe | 89.0 |
| real_test | 67.0 |
| china_check | 31.3 |
| write_verified | 0.0 |
| generate | 8.6 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 58836 |
| vmess | 16341 |
| shadowsocks | 11639 |
| trojan | 9975 |
| hysteria2 | 1282 |
| http | 398 |
| shadowsocksr | 171 |
| socks | 59 |
| anytls | 25 |
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
| 77.1 | hysteria2 | 280.5 | 717.4 | 21.28 | 0.0 | 10.0 | 12.0 | 15.32 | Au1rxx-base64 | 129.213.91.185 |
| 75.27 | vless | 269.9 | 672.3 | 21.53 | 0.0 | 10.0 | 8.78 | 15.32 | Au1rxx-base64 | 147.45.60.160 |
| 74.14 | shadowsocks | 242.1 | 605.5 | 22.17 | 0.0 | 8.21 | 12.44 | 15.32 | Au1rxx-base64 | 156.146.38.170 |
| 72.55 | shadowsocks | 303.6 | 734.0 | 20.75 | 0.0 | 10.0 | 12.44 | 15.32 | Au1rxx-base64 | 37.19.198.244 |
| 72.1 | shadowsocks | 309.0 | 753.4 | 20.62 | 0.0 | 10.0 | 12.44 | 15.32 | Au1rxx-base64 | 37.19.198.160 |
| 72.06 | shadowsocks | 308.6 | 748.5 | 20.63 | 0.0 | 10.0 | 12.44 | 15.32 | Au1rxx-base64 | 37.19.198.236 |
| 70.98 | vless | 293.1 | 591.6 | 20.99 | 0.0 | 10.0 | 8.78 | 15.32 | Au1rxx-base64 | 45.32.69.110 |
| 70.79 | shadowsocks | 248.4 | 622.9 | 22.03 | 0.0 | 10.0 | 12.44 | 15.32 | Au1rxx-base64 | 156.146.38.169 |
| 70.74 | vless | 275.6 | 550.5 | 21.4 | 0.0 | 10.0 | 8.78 | 15.32 | Au1rxx-base64 | 47.251.108.158 |
| 70.54 | shadowsocks | 248.3 | 615.6 | 22.03 | 0.0 | 10.0 | 12.44 | 15.32 | Au1rxx-base64 | 156.146.38.168 |
| 70.46 | shadowsocks | 312.6 | 683.9 | 20.54 | 0.0 | 10.0 | 12.44 | 15.32 | Au1rxx-base64 | 140.82.63.79 |
| 70.19 | vless | 300.0 | 594.4 | 20.83 | 0.0 | 10.0 | 8.78 | 15.32 | Au1rxx-base64 | 144.202.126.147 |
| 69.55 | vless | 303.2 | 644.0 | 20.76 | 0.0 | 7.64 | 8.78 | 15.32 | Au1rxx-base64 | 195.123.235.183 |
| 68.99 | vless | 309.0 | 666.9 | 20.63 | 0.0 | 7.61 | 8.78 | 15.32 | Au1rxx-base64 | 213.165.50.45 |
| 68.99 | shadowsocks | 316.1 | 763.8 | 20.46 | 0.0 | 6.43 | 12.44 | 15.32 | Au1rxx-base64 | 37.19.198.243 |
| 68.98 | vless | 290.2 | 672.5 | 21.06 | 0.0 | 8.32 | 8.78 | 15.32 | Au1rxx-base64 | 69.48.201.136 |
| 68.97 | vless | 339.6 | 779.4 | 19.92 | 0.0 | 7.63 | 8.78 | 15.32 | Au1rxx-base64 | 195.123.235.177 |
| 68.67 | vless | 328.0 | 650.9 | 20.19 | 0.0 | 10.0 | 8.78 | 15.32 | Au1rxx-base64 | 154.29.145.196 |
| 68.41 | shadowsocks | 249.1 | 604.4 | 22.01 | 0.0 | 7.64 | 12.44 | 15.32 | Au1rxx-base64 | 156.146.38.167 |
| 68.4 | vless | 331.8 | 692.4 | 20.1 | 0.0 | 8.22 | 8.78 | 15.32 | Au1rxx-base64 | 193.233.202.250 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.964 | 1.0 | 22 | 144 | prefer |
| mheidari-all | 0.905 | 0.833 | 78 | 23828 | prefer |
| Au1rxx-base64 | 0.853 | 0.786 | 210 | 1761 | prefer |
| Surfboard-tg-mixed | 0.709 | 0.633 | 60 | 7197 | prefer |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5125 | observe |
| DeltaKronecker-all | 0.255 | None | 0 | 4803 | observe |
| Epodonios-all | 0.255 | None | 0 | 7716 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 10189 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5754 | observe |
| barry-far-vless | 0.255 | None | 0 | 5978 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4271 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.245 | None | 0 | 1761 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 45 |
| geo | ClientOSError | - | 11 |
| speed | ClientOSError | - | 9 |
| 204 | TimeoutError | - | 5 |
| 204 | ProxyError | - | 4 |
| cn-block | ProxyError | - | 3 |
| cn-block | ClientOSError | - | 3 |
| cn-block | TimeoutError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 63 | 69 | - |
| global | False | 73 | 74 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
