# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-06-22 00:48:47 |
| 运行耗时 | 208.6s |
| 订阅源总数 | 107 |
| 健康订阅源 | 105 |
| 原始节点 | 73174 |
| 去重后节点 | 22101 |
| TCP 可达 | 3000 |
| 真实可用 | 581 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22101 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.7 |
| geo | 1.3 |
| tcp | 29.3 |
| probe | 45.7 |
| real_test | 107.2 |
| generate | 20.4 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 42749 |
| trojan | 9965 |
| shadowsocks | 9948 |
| vmess | 9857 |
| hysteria2 | 250 |
| http | 182 |
| shadowsocksr | 160 |
| socks | 55 |
| hysteria | 6 |
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
| 81.55 | shadowsocks | 253.9 | 621.4 | 21.9 | 0.0 | 10.0 | 13.85 | 19.8 | mheidari-all | 198.98.53.130 |
| 79.96 | vless | 327.2 | 888.5 | 20.2 | 0.0 | 10.0 | 12.56 | 19.8 | mheidari-all | 185.156.47.96 |
| 79.93 | shadowsocks | 271.9 | 663.1 | 21.48 | 0.0 | 10.0 | 13.85 | 18.86 | Au1rxx-base64 | 37.19.198.236 |
| 79.86 | shadowsocks | 268.2 | 652.1 | 21.57 | 0.0 | 10.0 | 13.85 | 18.86 | Au1rxx-base64 | 37.19.198.160 |
| 79.77 | shadowsocks | 284.7 | 694.8 | 21.19 | 0.0 | 10.0 | 13.85 | 18.86 | Au1rxx-base64 | 37.19.198.244 |
| 79.49 | shadowsocks | 300.1 | 582.4 | 20.83 | 0.0 | 10.0 | 13.85 | 18.86 | Au1rxx-base64 | 156.146.38.170 |
| 78.23 | vless | 303.2 | 575.6 | 20.76 | 0.0 | 10.0 | 12.56 | 19.8 | mheidari-all | 64.23.143.23 |
| 78.12 | shadowsocks | 313.3 | 601.0 | 20.52 | 0.0 | 10.0 | 13.85 | 18.86 | Au1rxx-base64 | 37.19.198.243 |
| 78.01 | shadowsocks | 344.5 | 880.9 | 19.8 | 0.0 | 10.0 | 13.85 | 18.86 | Au1rxx-base64 | 69.164.240.83 |
| 77.42 | shadowsocks | 286.3 | 691.7 | 21.15 | 0.0 | 10.0 | 13.85 | 18.58 | DeltaKronecker-all | 108.181.57.93 |
| 77.13 | shadowsocks | 296.1 | 789.0 | 20.92 | 0.0 | 10.0 | 13.85 | 18.86 | Au1rxx-base64 | 107.172.250.161 |
| 76.06 | shadowsocks | 467.4 | 1215.8 | 16.96 | 0.0 | 10.0 | 13.85 | 19.8 | mheidari-all | 161.129.71.148 |
| 75.68 | shadowsocks | 256.8 | 627.5 | 21.83 | 0.0 | 10.0 | 13.85 | 18.86 | Au1rxx-base64 | 156.146.38.167 |
| 75.34 | vmess | 389.6 | 1000.1 | 18.76 | 0.0 | 10.0 | 12.5 | 18.58 | DeltaKronecker-all | 67.220.95.3 |
| 75.21 | vless | 259.6 | 604.7 | 21.77 | 0.0 | 10.0 | 12.56 | 19.8 | mheidari-all | 104.19.87.194 |
| 74.77 | shadowsocks | 475.5 | 1271.1 | 16.77 | 0.0 | 10.0 | 13.85 | 18.86 | Au1rxx-base64 | 205.209.104.91 |
| 74.72 | shadowsocks | 290.8 | 578.4 | 21.05 | 0.0 | 10.0 | 13.85 | 18.86 | Au1rxx-base64 | 156.146.38.168 |
| 74.65 | shadowsocks | 279.0 | 565.9 | 21.32 | 0.0 | 10.0 | 13.85 | 18.86 | Au1rxx-base64 | 216.105.168.18 |
| 74.48 | shadowsocks | 327.0 | 699.9 | 20.21 | 0.0 | 10.0 | 13.85 | 18.86 | Au1rxx-base64 | 173.244.56.6 |
| 74.31 | shadowsocks | 318.7 | 618.4 | 20.4 | 0.0 | 10.0 | 13.85 | 18.86 | Au1rxx-base64 | 173.244.56.9 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.991 | 1.0 | 69 | 131 | prefer |
| Au1rxx-base64 | 0.847 | 0.857 | 42 | 149 | prefer |
| mheidari-all | 0.829 | 0.751 | 425 | 15086 | prefer |
| DeltaKronecker-all | 0.731 | 0.652 | 227 | 6748 | prefer |
| Surfboard-tg-mixed | 0.53 | 0.7 | 10 | 4738 | observe |
| Barabama-yudou | 0.318 | 1.0 | 2 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4494 | observe |
| Epodonios-all | 0.255 | None | 0 | 7244 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3978 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6793 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 3632 | observe |
| barry-far-vless | 0.255 | None | 0 | 4524 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4505 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |
| xiaoji235-airport-v2ray-all | 0.212 | None | 0 | 935 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 73 |
| speed | ClientOSError | - | 70 |
| speed | TimeoutError | - | 20 |
| geo | ClientOSError | - | 10 |
| cn-block | TimeoutError | - | 6 |
| 204 | TimeoutError | - | 5 |
| 204 | ClientOSError | - | 4 |
| cn-block | ClientOSError | - | 4 |
| 204 | ProxyError | - | 3 |
| cn-block | ProxyError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
