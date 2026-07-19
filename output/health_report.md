# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-19 19:18:18 |
| 运行耗时 | 294.7s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 86198 |
| 去重后节点 | 23804 |
| TCP 可达 | 3000 |
| 真实可用 | 429 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23804 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.7 |
| geo | 0.5 |
| tcp | 34.4 |
| probe | 62.8 |
| real_test | 150.1 |
| generate | 41.3 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 50165 |
| trojan | 14322 |
| vmess | 10877 |
| shadowsocks | 10208 |
| hysteria2 | 429 |
| shadowsocksr | 72 |
| http | 56 |
| socks | 40 |
| hysteria | 15 |
| tuic | 13 |
| anytls | 1 |

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
| 77.85 | shadowsocks | 232.8 | 634.8 | 22.39 | 0.0 | 10.0 | 12.1 | 17.36 | Au1rxx-base64 | 37.19.198.236 |
| 77.83 | shadowsocks | 233.8 | 647.9 | 22.37 | 0.0 | 10.0 | 12.1 | 17.36 | Au1rxx-base64 | 37.19.198.244 |
| 77.81 | shadowsocks | 234.5 | 642.4 | 22.35 | 0.0 | 10.0 | 12.1 | 17.36 | Au1rxx-base64 | 37.19.198.243 |
| 77.77 | shadowsocks | 236.3 | 638.0 | 22.31 | 0.0 | 10.0 | 12.1 | 17.36 | Au1rxx-base64 | 147.90.234.133 |
| 76.6 | shadowsocks | 286.6 | 803.1 | 21.14 | 0.0 | 10.0 | 12.1 | 17.36 | Au1rxx-base64 | 37.19.198.160 |
| 74.72 | shadowsocks | 346.5 | 915.2 | 19.76 | 0.0 | 10.0 | 12.1 | 17.36 | Au1rxx-base64 | 50.114.177.235 |
| 74.36 | shadowsocks | 332.6 | 820.1 | 20.08 | 0.0 | 10.0 | 12.1 | 17.36 | Au1rxx-base64 | 185.196.61.82 |
| 74.05 | shadowsocks | 287.9 | 650.9 | 21.11 | 0.0 | 10.0 | 12.1 | 17.36 | Au1rxx-base64 | 156.146.38.170 |
| 73.7 | shadowsocks | 286.2 | 658.6 | 21.15 | 0.0 | 10.0 | 12.1 | 17.36 | Au1rxx-base64 | 156.146.38.169 |
| 73.57 | shadowsocks | 283.1 | 643.3 | 21.23 | 0.0 | 10.0 | 12.1 | 17.36 | Au1rxx-base64 | 156.146.38.168 |
| 73.22 | shadowsocks | 286.7 | 645.5 | 21.14 | 0.0 | 10.0 | 12.1 | 17.36 | Au1rxx-base64 | 156.146.38.167 |
| 72.83 | shadowsocks | 233.6 | 627.0 | 22.37 | 0.0 | 10.0 | 12.1 | 17.36 | Au1rxx-base64 | tinkered-pennies-puppies.freesocks.work |
| 71.91 | hysteria2 | 361.1 | 686.0 | 19.42 | 0.0 | 10.0 | 12.0 | 17.36 | Au1rxx-base64 | 62.210.124.146 |
| 70.98 | hysteria2 | 424.8 | 890.5 | 17.94 | 0.0 | 10.0 | 12.0 | 17.36 | Au1rxx-base64 | 5.255.102.165 |
| 70.81 | shadowsocks | 314.3 | 591.7 | 20.5 | 0.0 | 10.0 | 12.1 | 17.36 | Au1rxx-base64 | 173.244.56.6 |
| 70.56 | shadowsocks | 220.4 | 588.1 | 22.68 | 0.0 | 10.0 | 12.1 | 17.36 | Au1rxx-base64 | 198.98.53.130 |
| 70.42 | shadowsocks | 316.7 | 558.9 | 20.45 | 0.0 | 10.0 | 12.1 | 17.36 | Au1rxx-base64 | 108.181.0.177 |
| 70.15 | shadowsocks | 543.7 | 1562.0 | 15.19 | 0.0 | 10.0 | 12.1 | 17.36 | Au1rxx-base64 | 68.168.222.210 |
| 69.67 | shadowsocks | 340.8 | 655.2 | 19.89 | 0.0 | 10.0 | 12.1 | 17.36 | Au1rxx-base64 | 149.22.95.183 |
| 67.13 | trojan | 474.2 | 994.4 | 16.8 | 0.0 | 10.0 | 11.63 | 17.36 | Au1rxx-base64 | 34.242.69.173 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.948 | 0.971 | 35 | 61 | prefer |
| Au1rxx-base64 | 0.87 | 0.829 | 234 | 1082 | prefer |
| Surfboard-tg-mixed | 0.644 | 0.566 | 53 | 5340 | observe |
| xiaoji235-airport-v2ray-all | 0.438 | 1.0 | 3 | 4642 | observe |
| mheidari-all | 0.387 | 0.306 | 487 | 19340 | observe |
| nscl5-all | 0.335 | 1.0 | 1 | 2755 | observe |
| Barabama-yudou | 0.318 | 1.0 | 2 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4478 | observe |
| Epodonios-all | 0.255 | None | 0 | 6712 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7186 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4216 | observe |
| barry-far-vless | 0.255 | None | 0 | 4995 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5229 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 293 |
| geo | TimeoutError | - | 80 |
| cn-block | TimeoutError | - | 45 |
| 204 | TimeoutError | - | 22 |
| geo | ClientOSError | - | 20 |
| cn-block | ClientOSError | - | 9 |
| 204 | ProxyError | - | 8 |
| speed | TimeoutError | - | 8 |
| 204 | ClientOSError | - | 8 |
| cn-block | ProxyError | - | 3 |
| sing-box exited 1 |  [31mFATAL[0m[0000] start service: start inbound/socks[socks-in]: listen tcp 127.0.0.1:43742: bind: address already in use | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
