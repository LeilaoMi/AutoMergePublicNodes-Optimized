# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-13 16:07:49 |
| 运行耗时 | 609.5s |
| 订阅源总数 | 107 |
| 健康订阅源 | 95 |
| 原始节点 | 95131 |
| 去重后节点 | 25342 |
| TCP 可达 | 3000 |
| 真实可用 | 432 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 25342 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.3 |
| geo | 1.4 |
| tcp | 42.7 |
| probe | 238.8 |
| real_test | 228.4 |
| generate | 90.8 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 58652 |
| vmess | 13652 |
| shadowsocks | 10958 |
| trojan | 8804 |
| hysteria2 | 2252 |
| http | 584 |
| shadowsocksr | 126 |
| socks | 60 |
| hysteria | 17 |
| anytls | 14 |
| tuic | 12 |

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
| 80.39 | vless | 245.8 | 626.2 | 22.09 | 0.0 | 10.0 | 10.6 | 17.7 | Au1rxx-base64 | 195.123.235.177 |
| 80.22 | vless | 253.2 | 696.8 | 21.92 | 0.0 | 10.0 | 10.6 | 17.7 | Au1rxx-base64 | 47.253.226.114 |
| 80.18 | vless | 254.9 | 679.2 | 21.88 | 0.0 | 10.0 | 10.6 | 17.7 | Au1rxx-base64 | 47.89.186.170 |
| 79.35 | vless | 290.7 | 808.5 | 21.05 | 0.0 | 10.0 | 10.6 | 17.7 | Au1rxx-base64 | 79.141.172.154 |
| 79.26 | vless | 270.7 | 696.0 | 21.51 | 0.0 | 10.0 | 10.6 | 17.7 | Au1rxx-base64 | 169.40.42.229 |
| 79.17 | hysteria2 | 279.1 | 757.4 | 21.32 | 0.0 | 10.0 | 11.25 | 17.7 | Au1rxx-base64 | 159.223.157.129 |
| 78.89 | vless | 310.7 | 678.1 | 20.59 | 0.0 | 10.0 | 10.6 | 17.7 | Au1rxx-base64 | 169.40.42.231 |
| 78.83 | vless | 292.7 | 694.0 | 21.0 | 0.0 | 10.0 | 10.6 | 17.7 | Au1rxx-base64 | 169.40.42.90 |
| 78.8 | vless | 307.7 | 801.5 | 20.66 | 0.0 | 10.0 | 10.6 | 17.7 | Au1rxx-base64 | 169.40.42.75 |
| 78.75 | shadowsocks | 251.2 | 676.5 | 21.96 | 0.0 | 10.0 | 13.09 | 17.7 | Au1rxx-base64 | 37.19.198.160 |
| 78.73 | vless | 286.5 | 729.0 | 21.15 | 0.0 | 10.0 | 10.6 | 17.7 | Au1rxx-base64 | 169.40.42.52 |
| 78.67 | vless | 320.2 | 856.8 | 20.37 | 0.0 | 10.0 | 10.6 | 17.7 | Au1rxx-base64 | 137.184.218.169 |
| 78.06 | vless | 346.4 | 784.9 | 19.76 | 0.0 | 10.0 | 10.6 | 17.7 | Au1rxx-base64 | 169.40.42.74 |
| 77.93 | vless | 301.9 | 650.1 | 20.79 | 0.0 | 10.0 | 10.6 | 17.7 | Au1rxx-base64 | 169.40.42.225 |
| 77.82 | vless | 304.4 | 721.8 | 20.73 | 0.0 | 10.0 | 10.6 | 17.7 | Au1rxx-base64 | 216.152.147.28 |
| 77.81 | vless | 357.0 | 820.6 | 19.51 | 0.0 | 10.0 | 10.6 | 17.7 | Au1rxx-base64 | 169.40.42.133 |
| 77.67 | vless | 363.1 | 988.8 | 19.37 | 0.0 | 10.0 | 10.6 | 17.7 | Au1rxx-base64 | 185.95.231.156 |
| 77.64 | vless | 364.3 | 856.4 | 19.34 | 0.0 | 10.0 | 10.6 | 17.7 | Au1rxx-base64 | 169.40.42.202 |
| 77.23 | vless | 382.3 | 987.1 | 18.93 | 0.0 | 10.0 | 10.6 | 17.7 | Au1rxx-base64 | 2.24.124.64 |
| 77.19 | vless | 348.9 | 920.0 | 19.7 | 0.0 | 10.0 | 10.6 | 17.7 | Au1rxx-base64 | 169.40.42.104 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.887 | 0.822 | 298 | 1678 | prefer |
| Surfboard-tg-mixed | 0.813 | 0.737 | 133 | 7605 | prefer |
| ermaozi | 0.599 | 0.588 | 34 | 382 | observe |
| mheidari-all | 0.524 | 0.444 | 142 | 20611 | observe |
| DeltaKronecker-all | 0.43 | 0.556 | 9 | 5892 | observe |
| xiaoji235-airport-v2ray-all | 0.335 | 1.0 | 1 | 5301 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4839 | observe |
| Epodonios-all | 0.255 | None | 0 | 7899 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3996 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9265 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 6236 | observe |
| barry-far-vless | 0.255 | None | 0 | 6452 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4221 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.242 | None | 0 | 1678 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | ClientOSError | - | 54 |
| cn-block | ClientOSError | - | 35 |
| speed | ClientOSError | - | 26 |
| 204 | TimeoutError | - | 21 |
| 204 | ProxyError | - | 18 |
| cn-block | TimeoutError | - | 14 |
| geo | TimeoutError | - | 10 |
| cn-block | ProxyError | - | 5 |
| 204 | ClientOSError | - | 3 |
| 204 | ProxyConnectionError | - | 2 |
| speed | TimeoutError | - | 2 |
| 204 | ServerDisconnectedError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
