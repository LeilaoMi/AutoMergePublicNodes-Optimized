# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-11 08:07:44 |
| 运行耗时 | 210.2s |
| 订阅源总数 | 107 |
| 健康订阅源 | 102 |
| 原始节点 | 75954 |
| 去重后节点 | 23903 |
| TCP 可达 | 3000 |
| 真实可用 | 403 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23903 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.1 |
| geo | 1.4 |
| tcp | 32.0 |
| probe | 46.0 |
| real_test | 102.4 |
| generate | 24.3 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 43291 |
| trojan | 12001 |
| vmess | 10520 |
| shadowsocks | 9485 |
| hysteria2 | 283 |
| shadowsocksr | 145 |
| http | 135 |
| socks | 84 |
| hysteria | 8 |
| tuic | 1 |
| anytls | 1 |

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
| 80.04 | trojan | 290.4 | 737.8 | 21.06 | 0.0 | 10.0 | 14.22 | 17.26 | Au1rxx-base64 | 149.28.241.235 |
| 79.65 | trojan | 243.2 | 595.2 | 22.15 | 0.0 | 10.0 | 14.22 | 16.28 | DeltaKronecker-all | 64.94.95.114 |
| 79.58 | trojan | 246.3 | 596.1 | 22.08 | 0.0 | 10.0 | 14.22 | 16.28 | DeltaKronecker-all | 64.94.95.115 |
| 79.41 | shadowsocks | 238.8 | 602.1 | 22.25 | 0.0 | 10.0 | 13.9 | 17.26 | Au1rxx-base64 | 156.146.38.168 |
| 79.33 | shadowsocks | 242.2 | 612.9 | 22.17 | 0.0 | 10.0 | 13.9 | 17.26 | Au1rxx-base64 | 156.146.38.167 |
| 79.33 | trojan | 278.4 | 706.2 | 21.33 | 0.0 | 10.0 | 14.22 | 16.28 | DeltaKronecker-all | 45.32.195.168 |
| 79.09 | trojan | 289.0 | 741.4 | 21.09 | 0.0 | 10.0 | 14.22 | 16.28 | DeltaKronecker-all | 45.32.198.247 |
| 78.32 | shadowsocks | 285.9 | 749.7 | 21.16 | 0.0 | 10.0 | 13.9 | 17.26 | Au1rxx-base64 | 156.146.38.169 |
| 77.55 | trojan | 333.8 | 844.3 | 20.05 | 0.0 | 10.0 | 14.22 | 16.28 | DeltaKronecker-all | 64.94.95.117 |
| 77.29 | trojan | 263.7 | 633.7 | 21.67 | 0.0 | 10.0 | 14.22 | 14.4 | mheidari-all | 64.94.95.118 |
| 75.37 | shadowsocks | 271.4 | 543.3 | 21.5 | 0.0 | 10.0 | 13.9 | 17.26 | Au1rxx-base64 | 173.244.56.9 |
| 74.4 | shadowsocks | 280.4 | 525.2 | 21.29 | 0.0 | 10.0 | 13.9 | 17.26 | Au1rxx-base64 | 173.244.56.6 |
| 73.16 | shadowsocks | 314.1 | 705.1 | 20.51 | 0.0 | 10.0 | 13.9 | 16.28 | DeltaKronecker-all | 107.172.219.230 |
| 72.99 | shadowsocks | 338.7 | 742.1 | 19.94 | 0.0 | 10.0 | 13.9 | 17.26 | Au1rxx-base64 | 37.19.198.236 |
| 72.96 | shadowsocks | 337.8 | 741.5 | 19.96 | 0.0 | 10.0 | 13.9 | 17.26 | Au1rxx-base64 | 37.19.198.244 |
| 72.85 | shadowsocks | 343.0 | 762.5 | 19.84 | 0.0 | 10.0 | 13.9 | 17.26 | Au1rxx-base64 | 37.19.198.243 |
| 72.78 | trojan | 315.2 | 632.4 | 20.48 | 0.0 | 10.0 | 14.22 | 16.28 | DeltaKronecker-all | 104.16.99.215 |
| 71.19 | shadowsocks | 326.8 | 359.3 | 20.21 | 1.53 | 9.78 | 13.9 | 17.26 | Au1rxx-base64 | 149.22.87.204 |
| 71.03 | trojan | 390.5 | 356.5 | 18.74 | 1.63 | 9.44 | 14.22 | 17.26 | Au1rxx-base64 | rich-mule.rooster465.autos |
| 70.84 | shadowsocks | 325.8 | 365.3 | 20.24 | 1.3 | 9.78 | 13.9 | 17.26 | Au1rxx-base64 | 149.22.87.240 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| mheidari-all | 0.911 | 0.841 | 63 | 16239 | prefer |
| Surfboard-tg-mixed | 0.865 | 0.789 | 128 | 5476 | prefer |
| DeltaKronecker-all | 0.759 | 0.68 | 250 | 7969 | prefer |
| Au1rxx-base64 | 0.682 | 0.683 | 60 | 111 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 3953 | observe |
| Epodonios-all | 0.255 | None | 0 | 6366 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3974 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6404 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4097 | observe |
| barry-far-vless | 0.255 | None | 0 | 4653 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5423 | observe |
| ninja-vless | 0.251 | 0.333 | 3 | 1791 | observe |
| xiaoji235-airport-v2ray-all | 0.229 | None | 0 | 1340 | observe |
| nscl5-all | 0.223 | None | 0 | 1207 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 43 |
| speed | ClientOSError | - | 25 |
| geo | ClientOSError | - | 16 |
| cn-block | ClientOSError | - | 12 |
| 204 | ClientOSError | - | 7 |
| cn-block | TimeoutError | - | 7 |
| 204 | ProxyError | - | 7 |
| speed | TimeoutError | - | 6 |
| geo | ProxyError | - | 6 |
| 204 | TimeoutError | - | 5 |
| cn-block | ProxyError | - | 3 |
| speed | ProxyError | - | 3 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
