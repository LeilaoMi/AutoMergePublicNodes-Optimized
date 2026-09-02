# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-02 03:59:42 |
| 运行耗时 | 301.0s |
| 订阅源总数 | 107 |
| 健康订阅源 | 95 |
| 原始节点 | 82051 |
| 去重后节点 | 23604 |
| TCP 可达 | 3000 |
| 真实可用 | 750 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23604 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 3.9 |
| geo | 1.4 |
| tcp | 38.4 |
| probe | 67.2 |
| real_test | 161.7 |
| generate | 28.3 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 51178 |
| vmess | 11353 |
| shadowsocks | 9914 |
| trojan | 7698 |
| hysteria2 | 1536 |
| http | 143 |
| shadowsocksr | 130 |
| socks | 81 |
| tuic | 11 |
| hysteria | 7 |

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
| 83.63 | vless | 276.8 | 657.0 | 21.37 | 0.0 | 10.0 | 12.72 | 19.54 | Au1rxx-base64 | 195.211.99.49 |
| 80.91 | shadowsocks | 251.3 | 608.4 | 21.96 | 0.0 | 10.0 | 13.41 | 19.54 | Au1rxx-base64 | 156.146.38.169 |
| 80.9 | shadowsocks | 251.6 | 649.7 | 21.95 | 0.0 | 10.0 | 13.41 | 19.54 | Au1rxx-base64 | 156.146.38.168 |
| 80.35 | vless | 273.1 | 644.0 | 21.46 | 0.0 | 10.0 | 12.72 | 19.54 | Au1rxx-base64 | 172.105.104.54 |
| 80.28 | trojan | 257.1 | 604.2 | 21.83 | 0.0 | 10.0 | 11.91 | 19.54 | Au1rxx-base64 | 64.94.95.114 |
| 79.69 | vless | 369.2 | 858.7 | 19.23 | 0.0 | 10.0 | 12.72 | 19.54 | Au1rxx-base64 | 169.40.42.235 |
| 79.56 | trojan | 263.5 | 568.9 | 21.68 | 0.0 | 10.0 | 11.91 | 19.54 | Au1rxx-base64 | 64.94.95.118 |
| 79.5 | vless | 315.5 | 698.6 | 20.47 | 0.0 | 10.0 | 12.72 | 19.54 | Au1rxx-base64 | 216.152.147.28 |
| 79.4 | vless | 275.9 | 557.5 | 21.39 | 0.0 | 10.0 | 12.72 | 19.54 | Au1rxx-base64 | 64.23.229.123 |
| 79.38 | vless | 301.3 | 579.0 | 20.8 | 0.0 | 10.0 | 12.72 | 19.54 | Au1rxx-base64 | 172.239.67.156 |
| 79.34 | vless | 429.7 | 1047.2 | 17.83 | 0.0 | 10.0 | 12.72 | 19.54 | Au1rxx-base64 | 185.95.231.156 |
| 79.17 | vless | 365.5 | 843.4 | 19.32 | 0.0 | 10.0 | 12.72 | 19.54 | Au1rxx-base64 | 169.40.42.89 |
| 79.14 | vless | 366.1 | 810.1 | 19.3 | 0.0 | 10.0 | 12.72 | 19.54 | Au1rxx-base64 | 169.40.42.232 |
| 78.95 | trojan | 259.6 | 614.4 | 21.77 | 0.0 | 10.0 | 11.91 | 19.54 | Au1rxx-base64 | 64.94.95.117 |
| 78.74 | vless | 308.8 | 638.7 | 20.63 | 0.0 | 10.0 | 12.72 | 19.54 | Au1rxx-base64 | 172.233.156.123 |
| 78.5 | vless | 297.6 | 611.2 | 20.89 | 0.0 | 10.0 | 12.72 | 19.54 | Au1rxx-base64 | 172.233.156.118 |
| 78.4 | vless | 304.3 | 597.3 | 20.73 | 0.0 | 10.0 | 12.72 | 19.54 | Au1rxx-base64 | 50.116.9.184 |
| 78.36 | vless | 309.1 | 572.4 | 20.62 | 0.0 | 10.0 | 12.72 | 19.54 | Au1rxx-base64 | 172.233.139.46 |
| 78.35 | vless | 300.5 | 580.8 | 20.82 | 0.0 | 10.0 | 12.72 | 19.54 | Au1rxx-base64 | 31.58.50.200 |
| 78.34 | vless | 305.8 | 597.0 | 20.7 | 0.0 | 10.0 | 12.72 | 19.54 | Au1rxx-base64 | 45.33.107.237 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.975 | 0.907 | 441 | 1736 | prefer |
| zhangkai | 0.967 | 1.0 | 24 | 144 | prefer |
| Surfboard-tg-mixed | 0.819 | 0.741 | 216 | 6990 | prefer |
| mheidari-all | 0.701 | 0.622 | 246 | 15712 | prefer |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4708 | observe |
| Epodonios-all | 0.255 | None | 0 | 7407 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7631 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5850 | observe |
| barry-far-vless | 0.255 | None | 0 | 6027 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4159 | observe |
| Au1rxx-clash | 0.244 | None | 0 | 1736 | observe |
| DeltaKronecker-all | 0.234 | 0.146 | 89 | 7294 | downweight |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |
| 10ium-HighSpeed | 0.209 | None | 0 | 839 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 90 |
| speed | TimeoutError | - | 49 |
| geo | ClientOSError | - | 40 |
| cn-block | TimeoutError | - | 24 |
| speed | ClientOSError | - | 20 |
| 204 | TimeoutError | - | 15 |
| 204 | ProxyError | - | 12 |
| cn-block | ClientOSError | - | 10 |
| 204 | ClientOSError | - | 5 |
| geo | ProxyError | - | 3 |
| cn-block | ProxyError | - | 1 |
| 204 | ServerDisconnectedError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
