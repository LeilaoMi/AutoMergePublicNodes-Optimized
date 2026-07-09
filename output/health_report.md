# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-09 10:08:13 |
| 运行耗时 | 225.3s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 79146 |
| 去重后节点 | 23828 |
| TCP 可达 | 3000 |
| 真实可用 | 320 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23828 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.2 |
| geo | 1.3 |
| tcp | 32.3 |
| probe | 51.0 |
| real_test | 99.1 |
| generate | 35.4 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 45328 |
| trojan | 12736 |
| vmess | 10326 |
| shadowsocks | 9555 |
| hysteria2 | 829 |
| shadowsocksr | 139 |
| http | 136 |
| socks | 83 |
| hysteria | 8 |
| anytls | 4 |
| tuic | 2 |

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
| 81.01 | shadowsocks | 237.4 | 589.8 | 22.28 | 0.0 | 10.0 | 14.01 | 18.72 | Au1rxx-base64 | 156.146.38.167 |
| 80.9 | shadowsocks | 242.4 | 620.7 | 22.17 | 0.0 | 10.0 | 14.01 | 18.72 | Au1rxx-base64 | 156.146.38.170 |
| 80.67 | trojan | 279.5 | 717.2 | 21.31 | 0.0 | 10.0 | 13.14 | 18.72 | Au1rxx-base64 | 149.28.241.235 |
| 78.73 | trojan | 363.4 | 969.4 | 19.37 | 0.0 | 10.0 | 13.14 | 18.72 | Au1rxx-base64 | 45.32.195.168 |
| 77.98 | shadowsocks | 282.2 | 745.3 | 21.25 | 0.0 | 10.0 | 14.01 | 18.72 | Au1rxx-base64 | 156.146.38.169 |
| 77.96 | shadowsocks | 245.1 | 623.8 | 22.1 | 0.0 | 10.0 | 14.01 | 18.72 | Au1rxx-base64 | 156.146.38.168 |
| 77.32 | shadowsocks | 279.7 | 571.3 | 21.3 | 0.0 | 10.0 | 14.01 | 18.72 | Au1rxx-base64 | 108.181.0.177 |
| 76.11 | shadowsocks | 271.3 | 540.3 | 21.5 | 0.0 | 10.0 | 14.01 | 18.72 | Au1rxx-base64 | 173.244.56.9 |
| 76.03 | shadowsocks | 272.5 | 537.1 | 21.47 | 0.0 | 10.0 | 14.01 | 18.72 | Au1rxx-base64 | 108.181.118.10 |
| 75.96 | shadowsocks | 301.0 | 502.7 | 20.81 | 0.0 | 10.0 | 14.01 | 18.72 | Au1rxx-base64 | 173.244.56.6 |
| 75.31 | shadowsocks | 304.0 | 305.7 | 20.74 | 3.54 | 9.79 | 14.01 | 18.72 | Au1rxx-base64 | 149.22.87.241 |
| 74.74 | shadowsocks | 304.9 | 626.7 | 20.72 | 0.0 | 10.0 | 14.01 | 18.72 | Au1rxx-base64 | 149.22.95.183 |
| 74.4 | trojan | 245.1 | 597.4 | 22.1 | 0.0 | 10.0 | 13.14 | 12.16 | DeltaKronecker-all | 64.94.95.114 |
| 74.27 | trojan | 250.9 | 613.4 | 21.97 | 0.0 | 10.0 | 13.14 | 12.16 | DeltaKronecker-all | 64.94.95.117 |
| 74.19 | shadowsocks | 353.2 | 810.8 | 19.6 | 0.0 | 10.0 | 14.01 | 18.72 | Au1rxx-base64 | 37.19.198.244 |
| 74.11 | trojan | 257.6 | 590.4 | 21.81 | 0.0 | 10.0 | 13.14 | 12.16 | DeltaKronecker-all | 64.94.95.115 |
| 73.87 | shadowsocks | 360.7 | 693.6 | 19.43 | 0.0 | 10.0 | 14.01 | 18.72 | Au1rxx-base64 | 37.19.198.236 |
| 73.8 | trojan | 292.6 | 747.7 | 21.0 | 0.0 | 10.0 | 13.14 | 12.16 | DeltaKronecker-all | 45.32.198.247 |
| 73.5 | shadowsocks | 330.0 | 727.0 | 20.14 | 0.0 | 10.0 | 14.01 | 18.72 | Au1rxx-base64 | 37.19.198.160 |
| 73.36 | shadowsocks | 306.9 | 667.1 | 20.67 | 0.0 | 10.0 | 14.01 | 16.44 | mheidari-all | 198.98.53.130 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| Au1rxx-base64 | 0.743 | 0.746 | 63 | 118 | prefer |
| DeltaKronecker-all | 0.645 | 0.566 | 113 | 7533 | observe |
| mheidari-all | 0.586 | 0.507 | 75 | 17088 | observe |
| Surfboard-tg-mixed | 0.574 | 0.494 | 265 | 5778 | observe |
| xiaoji235-airport-v2ray-all | 0.48 | 1.0 | 4 | 2703 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4306 | observe |
| Epodonios-all | 0.255 | None | 0 | 6686 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3976 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6293 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4286 | observe |
| barry-far-vless | 0.255 | None | 0 | 4851 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5440 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| nscl5-all | 0.228 | None | 0 | 1319 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 83 |
| 204 | ProxyError | - | 40 |
| geo | TimeoutError | - | 33 |
| 204 | TimeoutError | - | 23 |
| geo | ClientOSError | - | 11 |
| cn-block | TimeoutError | - | 11 |
| 204 | ClientOSError | - | 9 |
| geo | ProxyError | - | 9 |
| cn-block | ProxyError | - | 7 |
| cn-block | ClientOSError | - | 5 |
| speed | TimeoutError | - | 4 |
| speed | ProxyError | - | 3 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
