# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-19 15:51:57 |
| 运行耗时 | 587.8s |
| 订阅源总数 | 107 |
| 健康订阅源 | 95 |
| 原始节点 | 88522 |
| 去重后节点 | 25250 |
| TCP 可达 | 3000 |
| 真实可用 | 495 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 25250 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.5 |
| geo | 1.5 |
| tcp | 42.3 |
| probe | 215.5 |
| real_test | 238.7 |
| generate | 83.3 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 53553 |
| vmess | 13973 |
| shadowsocks | 10471 |
| trojan | 8544 |
| hysteria2 | 1197 |
| http | 575 |
| shadowsocksr | 128 |
| socks | 64 |
| hysteria | 9 |
| tuic | 4 |
| anytls | 4 |

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
| 82.97 | hysteria2 | 229.7 | 554.3 | 22.46 | 0.0 | 10.0 | 13.33 | 18.18 | Au1rxx-base64 | 66.94.121.46 |
| 79.8 | shadowsocks | 247.2 | 630.9 | 22.06 | 0.0 | 10.0 | 13.56 | 18.18 | Au1rxx-base64 | 156.146.38.168 |
| 78.28 | vless | 264.3 | 576.2 | 21.66 | 0.0 | 10.0 | 9.18 | 18.18 | Au1rxx-base64 | 38.180.242.205 |
| 74.49 | shadowsocks | 312.3 | 700.1 | 20.55 | 0.0 | 10.0 | 13.56 | 18.18 | Au1rxx-base64 | 173.244.56.9 |
| 74.23 | shadowsocks | 259.5 | 619.8 | 21.77 | 0.0 | 10.0 | 13.56 | 13.4 | Surfboard-tg-mixed | 23.150.248.20 |
| 74.04 | shadowsocks | 288.0 | 567.6 | 21.11 | 0.0 | 10.0 | 13.56 | 18.18 | Au1rxx-base64 | 149.22.95.183 |
| 73.96 | shadowsocks | 323.9 | 712.0 | 20.28 | 0.0 | 10.0 | 13.56 | 18.18 | Au1rxx-base64 | 37.19.198.160 |
| 73.73 | vless | 405.3 | 1004.3 | 18.4 | 0.0 | 10.0 | 9.18 | 18.18 | Au1rxx-base64 | 15.204.97.216 |
| 73.45 | vless | 340.6 | 762.2 | 19.89 | 0.0 | 10.0 | 9.18 | 18.18 | Au1rxx-base64 | 172.235.43.210 |
| 73.33 | http | 249.1 | 554.2 | 22.01 | 0.0 | 10.0 | 11.25 | 14.9 | ermaozi | 138.199.35.216 |
| 72.85 | http | 253.0 | 565.3 | 21.92 | 0.0 | 10.0 | 11.25 | 14.9 | ermaozi | 138.199.35.198 |
| 72.05 | vless | 308.6 | 617.0 | 20.64 | 0.0 | 10.0 | 9.18 | 18.18 | Au1rxx-base64 | 198.200.42.129 |
| 71.74 | shadowsocks | 333.0 | 741.3 | 20.07 | 0.0 | 10.0 | 13.56 | 18.18 | Au1rxx-base64 | 37.19.198.244 |
| 71.24 | shadowsocks | 280.9 | 721.2 | 21.28 | 0.0 | 10.0 | 13.56 | 13.4 | Surfboard-tg-mixed | 156.146.38.169 |
| 71.09 | shadowsocks | 434.8 | 1055.4 | 17.71 | 0.0 | 10.0 | 13.56 | 18.18 | Au1rxx-base64 | 198.98.53.130 |
| 71.05 | shadowsocks | 392.9 | 818.8 | 18.68 | 0.0 | 10.0 | 13.56 | 18.18 | Au1rxx-base64 | 108.181.57.93 |
| 71.0 | vless | 400.4 | 872.1 | 18.51 | 0.0 | 10.0 | 9.18 | 18.18 | Au1rxx-base64 | 66.70.179.198 |
| 70.9 | shadowsocks | 316.8 | 701.9 | 20.44 | 0.0 | 10.0 | 13.56 | 18.18 | Au1rxx-base64 | 173.244.56.6 |
| 70.9 | shadowsocks | 325.6 | 714.7 | 20.24 | 0.0 | 10.0 | 13.56 | 18.18 | Au1rxx-base64 | 37.19.198.236 |
| 70.79 | hysteria2 | 311.6 | 697.6 | 20.56 | 0.0 | 10.0 | 13.33 | 10.24 | mheidari-all | 159.223.157.129 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.9 | 0.836 | 318 | 1651 | prefer |
| ermaozi | 0.899 | 0.92 | 25 | 250 | prefer |
| Surfboard-tg-mixed | 0.696 | 0.617 | 183 | 7296 | observe |
| mheidari-all | 0.69 | 0.612 | 139 | 19364 | observe |
| DeltaKronecker-all | 0.515 | 0.636 | 11 | 6421 | observe |
| mahdibland-V2RayAggregator | 0.335 | 1.0 | 1 | 4251 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5174 | observe |
| Epodonios-all | 0.255 | None | 0 | 7933 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3995 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9336 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5900 | observe |
| barry-far-vless | 0.255 | None | 0 | 6222 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.241 | None | 0 | 1652 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | ClientOSError | - | 48 |
| 204 | TimeoutError | - | 30 |
| cn-block | ClientOSError | - | 28 |
| speed | ClientOSError | - | 21 |
| geo | TimeoutError | - | 20 |
| cn-block | TimeoutError | - | 14 |
| 204 | ProxyError | - | 12 |
| 204 | ClientOSError | - | 5 |
| speed | TimeoutError | - | 4 |
| cn-block | ProxyError | - | 2 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
