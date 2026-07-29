# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-29 14:26:11 |
| 运行耗时 | 250.9s |
| 订阅源总数 | 107 |
| 健康订阅源 | 100 |
| 原始节点 | 78926 |
| 去重后节点 | 22704 |
| TCP 可达 | 3000 |
| 真实可用 | 470 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22704 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 9.0 |
| geo | 1.4 |
| tcp | 31.7 |
| probe | 55.1 |
| real_test | 119.6 |
| generate | 34.2 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 46369 |
| vmess | 10770 |
| trojan | 10592 |
| shadowsocks | 10405 |
| hysteria2 | 548 |
| http | 73 |
| shadowsocksr | 72 |
| socks | 56 |
| anytls | 26 |
| hysteria | 12 |
| tuic | 3 |

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
| 79.08 | hysteria2 | 261.4 | 662.9 | 21.73 | 0.0 | 10.0 | 10.71 | 17.74 | Au1rxx-base64 | 159.223.157.129 |
| 78.61 | shadowsocks | 256.4 | 625.0 | 21.84 | 0.0 | 10.0 | 13.03 | 17.74 | Au1rxx-base64 | 156.146.38.168 |
| 78.36 | shadowsocks | 248.1 | 604.1 | 22.03 | 0.0 | 10.0 | 13.03 | 17.74 | Au1rxx-base64 | 156.146.38.167 |
| 78.3 | shadowsocks | 258.6 | 637.7 | 21.79 | 0.0 | 10.0 | 13.03 | 17.74 | Au1rxx-base64 | 156.146.38.169 |
| 77.56 | shadowsocks | 280.1 | 713.3 | 21.29 | 0.0 | 10.0 | 13.03 | 17.74 | Au1rxx-base64 | 37.19.198.243 |
| 76.89 | shadowsocks | 266.0 | 662.8 | 21.62 | 0.0 | 10.0 | 13.03 | 17.74 | Au1rxx-base64 | 185.232.22.18 |
| 75.95 | shadowsocks | 237.6 | 546.1 | 22.28 | 0.0 | 10.0 | 13.03 | 17.74 | Au1rxx-base64 | 68.168.114.226 |
| 74.56 | shadowsocks | 279.7 | 703.2 | 21.3 | 0.0 | 10.0 | 13.03 | 17.74 | Au1rxx-base64 | 37.19.198.244 |
| 74.34 | shadowsocks | 360.4 | 871.9 | 19.44 | 0.0 | 10.0 | 13.03 | 17.74 | Au1rxx-base64 | 185.247.68.94 |
| 73.9 | shadowsocks | 330.1 | 833.8 | 20.14 | 0.0 | 10.0 | 13.03 | 17.74 | Au1rxx-base64 | 146.70.34.226 |
| 72.78 | shadowsocks | 285.4 | 576.8 | 21.17 | 0.0 | 10.0 | 13.03 | 17.74 | Au1rxx-base64 | 108.181.0.177 |
| 72.34 | shadowsocks | 314.5 | 709.3 | 20.5 | 0.0 | 10.0 | 13.03 | 17.74 | Au1rxx-base64 | 38.132.118.198 |
| 72.14 | vless | 335.9 | 890.2 | 20.0 | 0.0 | 10.0 | 5.5 | 17.74 | Au1rxx-base64 | 45.138.100.226 |
| 71.82 | shadowsocks | 317.0 | 590.6 | 20.44 | 0.0 | 10.0 | 13.03 | 17.74 | Au1rxx-base64 | 149.22.95.183 |
| 71.14 | shadowsocks | 325.2 | 697.4 | 20.25 | 0.0 | 10.0 | 13.03 | 17.74 | Au1rxx-base64 | 185.236.200.210 |
| 70.92 | shadowsocks | 345.5 | 668.4 | 19.78 | 0.0 | 10.0 | 13.03 | 17.74 | Au1rxx-base64 | 108.181.118.10 |
| 69.88 | shadowsocks | 389.8 | 948.7 | 18.75 | 0.0 | 10.0 | 13.03 | 17.74 | Au1rxx-base64 | 38.132.118.30 |
| 69.7 | hysteria2 | 402.5 | 752.1 | 18.46 | 0.0 | 9.87 | 10.71 | 17.74 | Au1rxx-base64 | 178.215.238.30 |
| 69.53 | shadowsocks | 360.5 | 344.1 | 19.43 | 2.09 | 9.5 | 13.03 | 17.74 | Au1rxx-base64 | 149.22.87.241 |
| 69.41 | shadowsocks | 272.8 | 682.6 | 21.46 | 0.0 | 10.0 | 13.03 | 8.92 | Surfboard-tg-mixed | 37.19.198.236 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.989 | 1.0 | 70 | 84 | prefer |
| Au1rxx-base64 | 0.87 | 0.818 | 291 | 1352 | prefer |
| Surfboard-tg-mixed | 0.677 | 0.599 | 147 | 5803 | observe |
| DeltaKronecker-all | 0.67 | 0.592 | 103 | 5519 | observe |
| mheidari-all | 0.594 | 0.556 | 18 | 16071 | observe |
| 10ium-ScrapeCategorize-Vless | 0.335 | 1.0 | 1 | 5118 | observe |
| xiaoji235-airport-v2ray-all | 0.329 | 1.0 | 1 | 1861 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| Epodonios-all | 0.255 | None | 0 | 6469 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6373 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4538 | observe |
| barry-far-vless | 0.255 | None | 0 | 4964 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5089 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 56 |
| cn-block | TimeoutError | - | 30 |
| speed | TimeoutError | - | 28 |
| 204 | TimeoutError | - | 24 |
| 204 | ProxyError | - | 8 |
| speed | ClientOSError | - | 5 |
| geo | ClientOSError | - | 5 |
| cn-block | ClientOSError | - | 3 |
| cn-block | ProxyError | - | 2 |
| 204 | ClientOSError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
