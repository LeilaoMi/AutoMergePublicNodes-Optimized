# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-11 16:24:12 |
| 运行耗时 | 642.6s |
| 订阅源总数 | 107 |
| 健康订阅源 | 94 |
| 原始节点 | 83892 |
| 去重后节点 | 23240 |
| TCP 可达 | 3000 |
| 真实可用 | 418 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23240 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.7 |
| geo | 1.4 |
| tcp | 39.3 |
| probe | 265.6 |
| real_test | 235.9 |
| generate | 93.7 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 50697 |
| vmess | 12815 |
| shadowsocks | 9896 |
| trojan | 8027 |
| hysteria2 | 1659 |
| http | 599 |
| shadowsocksr | 125 |
| socks | 51 |
| tuic | 12 |
| hysteria | 9 |
| anytls | 2 |

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
| 81.88 | hysteria2 | 251.7 | 653.8 | 21.95 | 0.0 | 10.0 | 12.27 | 18.76 | Au1rxx-base64 | 159.223.157.129 |
| 81.06 | vless | 234.0 | 615.5 | 22.36 | 0.0 | 10.0 | 9.94 | 18.76 | Au1rxx-base64 | 195.123.235.177 |
| 80.72 | vless | 248.7 | 698.3 | 22.02 | 0.0 | 10.0 | 9.94 | 18.76 | Au1rxx-base64 | 47.253.226.114 |
| 80.65 | vless | 251.9 | 660.5 | 21.95 | 0.0 | 10.0 | 9.94 | 18.76 | Au1rxx-base64 | 137.184.218.169 |
| 80.43 | shadowsocks | 237.7 | 644.7 | 22.28 | 0.0 | 10.0 | 13.39 | 18.76 | Au1rxx-base64 | 198.98.53.130 |
| 80.26 | vless | 268.7 | 735.1 | 21.56 | 0.0 | 10.0 | 9.94 | 18.76 | Au1rxx-base64 | 79.141.172.154 |
| 80.25 | vless | 269.2 | 700.6 | 21.55 | 0.0 | 10.0 | 9.94 | 18.76 | Au1rxx-base64 | 167.17.69.171 |
| 80.14 | shadowsocks | 250.0 | 695.4 | 21.99 | 0.0 | 10.0 | 13.39 | 18.76 | Au1rxx-base64 | 37.19.198.244 |
| 80.14 | vless | 273.9 | 706.0 | 21.44 | 0.0 | 10.0 | 9.94 | 18.76 | Au1rxx-base64 | 169.40.42.182 |
| 80.11 | vless | 275.1 | 659.7 | 21.41 | 0.0 | 10.0 | 9.94 | 18.76 | Au1rxx-base64 | 169.40.42.231 |
| 79.99 | vless | 280.1 | 682.5 | 21.29 | 0.0 | 10.0 | 9.94 | 18.76 | Au1rxx-base64 | 169.40.42.89 |
| 79.98 | vless | 237.7 | 661.9 | 22.28 | 0.0 | 10.0 | 9.94 | 18.76 | Au1rxx-base64 | 188.137.243.243 |
| 79.85 | vless | 286.2 | 703.6 | 21.15 | 0.0 | 10.0 | 9.94 | 18.76 | Au1rxx-base64 | 66.70.179.198 |
| 79.7 | vless | 292.7 | 641.3 | 21.0 | 0.0 | 10.0 | 9.94 | 18.76 | Au1rxx-base64 | 169.40.42.15 |
| 79.57 | vless | 298.4 | 734.8 | 20.87 | 0.0 | 10.0 | 9.94 | 18.76 | Au1rxx-base64 | 169.40.42.35 |
| 79.51 | vless | 301.1 | 673.4 | 20.81 | 0.0 | 10.0 | 9.94 | 18.76 | Au1rxx-base64 | 169.40.42.104 |
| 79.25 | shadowsocks | 288.4 | 791.8 | 21.1 | 0.0 | 10.0 | 13.39 | 18.76 | Au1rxx-base64 | 37.19.198.243 |
| 79.06 | vless | 320.4 | 865.0 | 20.36 | 0.0 | 10.0 | 9.94 | 18.76 | Au1rxx-base64 | 169.40.42.179 |
| 78.96 | vless | 324.6 | 828.6 | 20.26 | 0.0 | 10.0 | 9.94 | 18.76 | Au1rxx-base64 | 169.40.42.229 |
| 78.94 | vless | 325.7 | 785.7 | 20.24 | 0.0 | 10.0 | 9.94 | 18.76 | Au1rxx-base64 | 169.40.42.212 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.895 | 0.827 | 260 | 1758 | prefer |
| ermaozi | 0.796 | 0.8 | 30 | 377 | prefer |
| Surfboard-tg-mixed | 0.728 | 0.65 | 140 | 7370 | prefer |
| mheidari-all | 0.707 | 0.63 | 81 | 15708 | prefer |
| DeltaKronecker-all | 0.651 | 0.574 | 61 | 6070 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4932 | observe |
| Epodonios-all | 0.255 | None | 0 | 7833 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 8514 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5979 | observe |
| barry-far-vless | 0.255 | None | 0 | 6192 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4223 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.245 | None | 0 | 1758 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | ClientOSError | - | 53 |
| 204 | TimeoutError | - | 26 |
| 204 | ProxyError | - | 24 |
| cn-block | TimeoutError | - | 20 |
| cn-block | ClientOSError | - | 14 |
| speed | ClientOSError | - | 10 |
| 204 | ClientOSError | - | 5 |
| cn-block | ProxyError | - | 3 |
| speed | TimeoutError | - | 3 |
| geo | TimeoutError | - | 3 |
| 204 | ServerDisconnectedError | - | 1 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
