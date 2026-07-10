# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-10 14:44:10 |
| 运行耗时 | 238.5s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 75777 |
| 去重后节点 | 23709 |
| TCP 可达 | 3000 |
| 真实可用 | 338 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23709 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.5 |
| geo | 1.4 |
| tcp | 31.8 |
| probe | 50.8 |
| real_test | 112.8 |
| generate | 37.2 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 43133 |
| trojan | 12243 |
| vmess | 10600 |
| shadowsocks | 9124 |
| hysteria2 | 285 |
| shadowsocksr | 148 |
| http | 135 |
| socks | 94 |
| hysteria | 8 |
| anytls | 6 |
| tuic | 1 |

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
| 78.71 | shadowsocks | 247.6 | 629.7 | 22.05 | 0.0 | 10.0 | 13.26 | 17.4 | Au1rxx-base64 | 156.146.38.169 |
| 78.62 | shadowsocks | 251.4 | 647.2 | 21.96 | 0.0 | 10.0 | 13.26 | 17.4 | Au1rxx-base64 | 156.146.38.170 |
| 78.56 | shadowsocks | 253.8 | 613.8 | 21.9 | 0.0 | 10.0 | 13.26 | 17.4 | Au1rxx-base64 | 156.146.38.167 |
| 77.6 | shadowsocks | 295.3 | 734.1 | 20.94 | 0.0 | 10.0 | 13.26 | 17.4 | Au1rxx-base64 | 156.146.38.168 |
| 74.27 | shadowsocks | 297.2 | 718.2 | 20.9 | 0.0 | 10.0 | 13.26 | 14.94 | Surfboard-tg-mixed | 37.19.198.244 |
| 74.04 | shadowsocks | 272.2 | 533.0 | 21.48 | 0.0 | 10.0 | 13.26 | 17.4 | Au1rxx-base64 | 107.172.219.230 |
| 73.39 | shadowsocks | 291.6 | 660.2 | 21.03 | 0.0 | 10.0 | 13.26 | 14.94 | Surfboard-tg-mixed | 198.98.53.130 |
| 73.1 | shadowsocks | 303.0 | 530.1 | 20.76 | 0.0 | 10.0 | 13.26 | 17.4 | Au1rxx-base64 | 173.244.56.9 |
| 72.76 | shadowsocks | 287.9 | 676.9 | 21.11 | 0.0 | 10.0 | 13.26 | 14.94 | Surfboard-tg-mixed | 37.19.198.236 |
| 72.68 | shadowsocks | 295.2 | 557.2 | 20.95 | 0.0 | 10.0 | 13.26 | 17.4 | Au1rxx-base64 | 173.244.56.6 |
| 72.65 | shadowsocks | 331.5 | 727.8 | 20.1 | 0.0 | 10.0 | 13.26 | 17.4 | Au1rxx-base64 | 108.181.57.93 |
| 72.43 | trojan | 365.2 | 950.1 | 19.32 | 0.0 | 10.0 | 8.21 | 17.4 | Au1rxx-base64 | 149.28.241.235 |
| 72.11 | shadowsocks | 290.9 | 681.4 | 21.04 | 0.0 | 10.0 | 13.26 | 14.94 | Surfboard-tg-mixed | 37.19.198.243 |
| 72.02 | shadowsocks | 324.5 | 666.1 | 20.27 | 0.0 | 10.0 | 13.26 | 17.4 | Au1rxx-base64 | 108.181.118.10 |
| 71.88 | shadowsocks | 305.2 | 709.0 | 20.71 | 0.0 | 10.0 | 13.26 | 14.94 | Surfboard-tg-mixed | 37.19.198.160 |
| 71.78 | shadowsocks | 348.3 | 728.9 | 19.71 | 0.0 | 10.0 | 13.26 | 17.4 | Au1rxx-base64 | 108.181.0.177 |
| 67.88 | shadowsocks | 337.6 | 755.2 | 19.96 | 0.0 | 10.0 | 13.26 | 17.4 | Au1rxx-base64 | 216.105.168.18 |
| 67.8 | trojan | 351.3 | 954.0 | 19.65 | 0.0 | 10.0 | 8.21 | 12.44 | DeltaKronecker-all | 45.32.195.168 |
| 67.78 | trojan | 351.9 | 943.6 | 19.63 | 0.0 | 10.0 | 8.21 | 12.44 | DeltaKronecker-all | 45.32.198.247 |
| 67.38 | shadowsocks | 373.1 | 865.0 | 19.14 | 0.0 | 10.0 | 13.26 | 12.48 | mheidari-all | 185.196.61.82 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| Au1rxx-base64 | 0.785 | 0.842 | 19 | 50 | prefer |
| mheidari-all | 0.729 | 0.653 | 75 | 16259 | prefer |
| Surfboard-tg-mixed | 0.669 | 0.59 | 278 | 5542 | observe |
| DeltaKronecker-all | 0.605 | 0.526 | 137 | 7600 | observe |
| nscl5-all | 0.301 | 1.0 | 1 | 1148 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4165 | observe |
| Epodonios-all | 0.255 | None | 0 | 6344 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3970 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6409 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4182 | observe |
| barry-far-vless | 0.255 | None | 0 | 4670 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5391 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| xiaoji235-airport-v2ray-all | 0.228 | None | 0 | 1319 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 72 |
| geo | TimeoutError | - | 29 |
| 204 | ProxyError | - | 18 |
| 204 | TimeoutError | - | 16 |
| cn-block | TimeoutError | - | 14 |
| cn-block | ProxyError | - | 13 |
| geo | ClientOSError | - | 13 |
| speed | TimeoutError | - | 9 |
| 204 | ClientOSError | - | 9 |
| cn-block | ClientOSError | - | 8 |
| speed | ProxyError | - | 6 |
| geo | ProxyError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 250 | 300 | - |
| global | False | 279 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
