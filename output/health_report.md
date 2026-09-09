# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-09 11:13:44 |
| 运行耗时 | 632.4s |
| 订阅源总数 | 107 |
| 健康订阅源 | 96 |
| 原始节点 | 85046 |
| 去重后节点 | 22059 |
| TCP 可达 | 3000 |
| 真实可用 | 456 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22059 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.7 |
| geo | 1.4 |
| tcp | 36.5 |
| probe | 230.5 |
| real_test | 277.1 |
| generate | 80.2 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 52670 |
| vmess | 12062 |
| shadowsocks | 9857 |
| trojan | 7990 |
| hysteria2 | 1629 |
| http | 639 |
| shadowsocksr | 124 |
| socks | 56 |
| hysteria | 9 |
| tuic | 8 |
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
| 84.07 | hysteria2 | 217.7 | 505.4 | 22.74 | 0.0 | 9.34 | 13.75 | 19.24 | Au1rxx-base64 | 66.94.121.46 |
| 80.65 | vless | 193.1 | 491.4 | 23.31 | 0.0 | 9.11 | 8.99 | 19.24 | Au1rxx-base64 | 172.235.38.85 |
| 80.56 | vless | 200.8 | 476.3 | 23.13 | 0.0 | 9.2 | 8.99 | 19.24 | Au1rxx-base64 | 172.233.139.46 |
| 80.28 | vless | 215.3 | 553.9 | 22.79 | 0.0 | 9.26 | 8.99 | 19.24 | Au1rxx-base64 | 38.209.125.45 |
| 79.72 | vless | 235.9 | 534.9 | 22.32 | 0.0 | 9.17 | 8.99 | 19.24 | Au1rxx-base64 | 31.58.50.200 |
| 78.79 | shadowsocks | 273.1 | 702.7 | 21.46 | 0.0 | 9.42 | 13.17 | 19.24 | Au1rxx-base64 | 108.181.0.177 |
| 78.03 | vless | 310.1 | 816.8 | 20.6 | 0.0 | 9.2 | 8.99 | 19.24 | Au1rxx-base64 | 15.204.97.216 |
| 77.99 | shadowsocks | 213.4 | 495.7 | 22.84 | 0.0 | 10.0 | 13.17 | 16.48 | Surfboard-tg-mixed | 108.181.118.10 |
| 77.72 | shadowsocks | 246.6 | 554.4 | 22.07 | 0.0 | 10.0 | 13.17 | 16.48 | Surfboard-tg-mixed | 173.244.56.6 |
| 77.57 | trojan | 202.4 | 528.3 | 23.09 | 0.0 | 8.64 | 9.6 | 19.24 | Au1rxx-base64 | us01.duotg.top |
| 77.03 | shadowsocks | 276.3 | 645.6 | 21.38 | 0.0 | 10.0 | 13.17 | 16.48 | Surfboard-tg-mixed | 173.244.56.9 |
| 75.29 | shadowsocks | 220.3 | 518.5 | 22.68 | 0.0 | 10.0 | 13.17 | 13.44 | mheidari-all | 149.22.95.183 |
| 75.16 | trojan | 200.7 | 525.5 | 23.13 | 0.0 | 9.19 | 9.6 | 19.24 | Au1rxx-base64 | 107.150.105.84 |
| 74.56 | hysteria2 | 348.3 | 725.2 | 19.71 | 0.0 | 10.0 | 13.75 | 16.48 | Surfboard-tg-mixed | 159.223.157.129 |
| 74.13 | vless | 478.9 | 1274.3 | 16.69 | 0.0 | 9.21 | 8.99 | 19.24 | Au1rxx-base64 | 51.81.203.63 |
| 73.71 | vless | 239.7 | 579.2 | 22.23 | 0.0 | 9.23 | 8.99 | 19.24 | Au1rxx-base64 | 38.246.229.58 |
| 72.75 | shadowsocks | 302.9 | 648.9 | 20.77 | 0.0 | 10.0 | 13.17 | 16.48 | Surfboard-tg-mixed | 156.146.38.167 |
| 72.08 | vless | 335.1 | 339.3 | 20.02 | 2.27 | 9.07 | 8.99 | 19.24 | Au1rxx-base64 | 13.231.19.51 |
| 72.04 | vless | 336.2 | 341.4 | 19.99 | 2.2 | 9.12 | 8.99 | 19.24 | Au1rxx-base64 | 18.177.61.231 |
| 72.02 | vless | 337.8 | 336.1 | 19.96 | 2.4 | 9.12 | 8.99 | 19.24 | Au1rxx-base64 | 18.183.215.124 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.987 | 0.921 | 227 | 1749 | prefer |
| Surfboard-tg-mixed | 0.863 | 0.787 | 164 | 7479 | prefer |
| mheidari-all | 0.847 | 0.775 | 71 | 16452 | prefer |
| ermaozi | 0.724 | 0.714 | 49 | 442 | prefer |
| DeltaKronecker-all | 0.679 | 0.632 | 19 | 5187 | observe |
| ermaozi-get_subscribe | 0.659 | 0.652 | 23 | 473 | observe |
| tg-oneclickvpnkeys | 0.262 | 1.0 | 1 | 180 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4795 | observe |
| Epodonios-all | 0.255 | None | 0 | 7964 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9095 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 6181 | observe |
| barry-far-vless | 0.255 | None | 0 | 6404 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4219 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | ProxyError | - | 28 |
| 204 | TimeoutError | - | 25 |
| geo | ClientOSError | - | 15 |
| cn-block | TimeoutError | - | 12 |
| geo | TimeoutError | - | 5 |
| cn-block | ClientOSError | - | 4 |
| 204 | ClientOSError | - | 3 |
| 204 | ProxyConnectionError | - | 2 |
| speed | TimeoutError | - | 2 |
| cn-block | ProxyError | - | 1 |
| speed | ClientOSError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
