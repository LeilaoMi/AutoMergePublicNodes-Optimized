# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-05 13:55:26 |
| 运行耗时 | 194.4s |
| 订阅源总数 | 107 |
| 健康订阅源 | 102 |
| 原始节点 | 80046 |
| 去重后节点 | 23893 |
| TCP 可达 | 3000 |
| 真实可用 | 308 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23893 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.1 |
| geo | 1.3 |
| tcp | 30.9 |
| probe | 53.2 |
| real_test | 74.4 |
| generate | 29.4 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 46556 |
| trojan | 12744 |
| vmess | 10445 |
| shadowsocks | 9486 |
| hysteria2 | 476 |
| shadowsocksr | 142 |
| http | 135 |
| socks | 48 |
| tuic | 8 |
| hysteria | 6 |

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
| 77.5 | shadowsocks | 170.7 | 460.2 | 23.83 | 0.0 | 10.0 | 12.41 | 16.36 | DeltaKronecker-all | 107.172.219.230 |
| 77.18 | shadowsocks | 198.2 | 494.2 | 23.19 | 0.0 | 10.0 | 12.41 | 16.08 | Au1rxx-base64 | 108.181.118.10 |
| 77.07 | shadowsocks | 224.4 | 532.9 | 22.58 | 0.0 | 10.0 | 12.41 | 16.08 | Au1rxx-base64 | 149.22.95.183 |
| 76.85 | shadowsocks | 233.8 | 493.2 | 22.36 | 0.0 | 10.0 | 12.41 | 16.08 | Au1rxx-base64 | 173.244.56.9 |
| 76.72 | shadowsocks | 218.3 | 541.1 | 22.73 | 0.0 | 10.0 | 12.41 | 16.08 | Au1rxx-base64 | 108.181.0.177 |
| 75.73 | shadowsocks | 282.2 | 678.1 | 21.24 | 0.0 | 10.0 | 12.41 | 16.08 | Au1rxx-base64 | 173.244.56.6 |
| 73.48 | trojan | 305.3 | 645.5 | 20.71 | 0.0 | 10.0 | 12.98 | 16.36 | DeltaKronecker-all | 64.94.95.117 |
| 73.2 | shadowsocks | 272.9 | 278.9 | 21.46 | 4.54 | 9.91 | 12.41 | 16.08 | Au1rxx-base64 | 149.22.87.240 |
| 72.81 | shadowsocks | 335.6 | 805.9 | 20.01 | 0.0 | 10.0 | 12.41 | 18.26 | mheidari-all | 172.245.235.84 |
| 72.76 | shadowsocks | 293.3 | 660.3 | 20.99 | 0.0 | 10.0 | 12.41 | 16.08 | Au1rxx-base64 | 156.146.38.170 |
| 72.12 | shadowsocks | 295.4 | 656.5 | 20.94 | 0.0 | 10.0 | 12.41 | 16.08 | Au1rxx-base64 | 156.146.38.168 |
| 72.05 | shadowsocks | 291.8 | 651.9 | 21.02 | 0.0 | 10.0 | 12.41 | 16.08 | Au1rxx-base64 | 156.146.38.167 |
| 71.51 | trojan | 294.6 | 411.9 | 20.96 | 0.0 | 10.0 | 12.98 | 17.86 | Surfboard-tg-mixed | 104.26.15.137 |
| 71.51 | trojan | 404.7 | 948.7 | 18.41 | 0.0 | 10.0 | 12.98 | 16.36 | DeltaKronecker-all | 45.32.195.168 |
| 71.35 | trojan | 427.9 | 991.6 | 17.87 | 0.0 | 10.0 | 12.98 | 16.36 | DeltaKronecker-all | 45.32.198.247 |
| 70.95 | trojan | 222.9 | 465.3 | 22.62 | 0.0 | 10.0 | 12.98 | 17.86 | Surfboard-tg-mixed | 172.67.172.95 |
| 70.61 | shadowsocks | 362.9 | 873.1 | 19.38 | 0.0 | 10.0 | 12.41 | 16.08 | Au1rxx-base64 | 156.146.38.169 |
| 70.5 | trojan | 424.9 | 1009.7 | 17.94 | 0.0 | 10.0 | 12.98 | 16.36 | DeltaKronecker-all | 149.28.241.235 |
| 70.33 | shadowsocks | 286.1 | 749.5 | 21.15 | 0.0 | 10.0 | 12.41 | 18.26 | mheidari-all | 216.105.168.18 |
| 70.31 | shadowsocks | 293.7 | 340.3 | 20.98 | 2.24 | 9.91 | 12.41 | 16.08 | Au1rxx-base64 | 149.22.87.204 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| mheidari-all | 0.869 | 0.795 | 88 | 16415 | prefer |
| DeltaKronecker-all | 0.862 | 0.786 | 117 | 7739 | prefer |
| Surfboard-tg-mixed | 0.858 | 0.783 | 106 | 6156 | prefer |
| Au1rxx-base64 | 0.843 | 0.862 | 29 | 114 | prefer |
| nscl5-all | 0.364 | 1.0 | 2 | 1323 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4662 | observe |
| Epodonios-all | 0.255 | None | 0 | 7257 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3970 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7136 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4608 | observe |
| barry-far-vless | 0.255 | None | 0 | 5319 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5372 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| xiaoji235-airport-v2ray-all | 0.227 | None | 0 | 1288 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 21 |
| 204 | ClientOSError | - | 10 |
| 204 | ProxyError | - | 9 |
| geo | TimeoutError | - | 8 |
| 204 | TimeoutError | - | 7 |
| geo | ClientOSError | - | 6 |
| cn-block | TimeoutError | - | 4 |
| cn-block | ClientOSError | - | 3 |
| cn-block | ProxyError | - | 2 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
