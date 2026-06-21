# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.9.1 |
| 更新时间 | 2026-06-21 20:00:03 |
| 运行耗时 | 497.3s |
| 订阅源总数 | 107 |
| 健康订阅源 | 105 |
| 原始节点 | 72909 |
| 去重后节点 | 22018 |
| TCP 可达 | 845 |
| 真实可用 | 622 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22018 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.9 |
| geo | 1.4 |
| tcp | 62.5 |
| probe | 120.3 |
| real_test | 267.0 |
| generate | 41.1 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 42767 |
| trojan | 9926 |
| shadowsocks | 9804 |
| vmess | 9734 |
| hysteria2 | 255 |
| http | 182 |
| shadowsocksr | 169 |
| socks | 64 |
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
| 78.75 | vless | 304.8 | 801.8 | 20.72 | 0.0 | 10.0 | 11.77 | 17.96 | Au1rxx-base64 | 15.204.97.219 |
| 78.39 | vless | 320.3 | 845.4 | 20.36 | 0.0 | 10.0 | 11.77 | 17.96 | Au1rxx-base64 | 15.204.97.214 |
| 78.09 | vless | 191.0 | 486.4 | 23.36 | 0.0 | 10.0 | 11.77 | 17.96 | Au1rxx-base64 | a.cflive.top |
| 77.68 | shadowsocks | 211.5 | 503.2 | 22.88 | 0.0 | 10.0 | 13.04 | 17.96 | Au1rxx-base64 | 173.244.56.9 |
| 76.62 | shadowsocks | 257.3 | 639.7 | 21.82 | 0.0 | 10.0 | 13.04 | 17.96 | Au1rxx-base64 | 173.244.56.6 |
| 76.3 | shadowsocks | 237.6 | 569.0 | 22.28 | 0.0 | 10.0 | 13.04 | 17.96 | Au1rxx-base64 | 149.22.95.183 |
| 75.44 | vless | 253.4 | 699.3 | 21.91 | 0.0 | 10.0 | 11.77 | 17.96 | Au1rxx-base64 | 141.193.154.182 |
| 74.63 | vless | 335.4 | 820.1 | 20.01 | 0.0 | 10.0 | 11.77 | 17.96 | Au1rxx-base64 | 34.213.172.16 |
| 73.77 | vless | 161.5 | 463.9 | 24.04 | 0.0 | 10.0 | 11.77 | 17.16 | Surfboard-tg-mixed | 64.118.155.66 |
| 72.69 | shadowsocks | 291.8 | 653.8 | 21.02 | 0.0 | 10.0 | 13.04 | 17.96 | Au1rxx-base64 | 156.146.38.167 |
| 72.6 | shadowsocks | 289.1 | 649.3 | 21.09 | 0.0 | 10.0 | 13.04 | 17.96 | Au1rxx-base64 | 156.146.38.168 |
| 72.57 | shadowsocks | 287.7 | 647.2 | 21.12 | 0.0 | 10.0 | 13.04 | 17.96 | Au1rxx-base64 | 156.146.38.170 |
| 71.06 | shadowsocks | 293.9 | 342.5 | 20.98 | 2.16 | 9.94 | 13.04 | 17.96 | Au1rxx-base64 | 149.22.87.240 |
| 70.73 | shadowsocks | 511.9 | 1470.1 | 15.93 | 0.0 | 10.0 | 13.04 | 17.96 | Au1rxx-base64 | 108.181.0.177 |
| 70.56 | shadowsocks | 296.7 | 352.0 | 20.91 | 1.8 | 9.95 | 13.04 | 17.96 | Au1rxx-base64 | 149.22.87.204 |
| 70.49 | shadowsocks | 522.1 | 1459.7 | 15.69 | 0.0 | 10.0 | 13.04 | 17.96 | Au1rxx-base64 | 108.181.118.10 |
| 70.34 | shadowsocks | 299.3 | 356.9 | 20.85 | 1.62 | 9.94 | 13.04 | 17.96 | Au1rxx-base64 | 149.22.87.241 |
| 69.8 | shadowsocks | 300.9 | 683.2 | 20.81 | 0.0 | 10.0 | 13.04 | 17.96 | Au1rxx-base64 | 156.146.38.169 |
| 69.24 | trojan | 343.7 | 732.7 | 19.82 | 0.0 | 10.0 | 10.23 | 17.82 | mheidari-all | 64.94.95.118 |
| 68.73 | vless | 458.9 | 320.4 | 17.15 | 2.99 | 9.48 | 11.77 | 17.16 | Surfboard-tg-mixed | 64.49.45.57 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.991 | 1.0 | 69 | 131 | prefer |
| Au1rxx-base64 | 0.885 | 0.888 | 89 | 138 | prefer |
| mheidari-all | 0.818 | 0.739 | 284 | 14833 | prefer |
| Surfboard-tg-mixed | 0.759 | 0.68 | 350 | 4837 | prefer |
| DeltaKronecker-all | 0.549 | 0.468 | 47 | 6748 | observe |
| SoliSpirit-all | 0.391 | 1.0 | 2 | 6721 | observe |
| Barabama-yudou | 0.318 | 1.0 | 2 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4494 | observe |
| Epodonios-all | 0.255 | None | 0 | 7211 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 3719 | observe |
| barry-far-vless | 0.255 | None | 0 | 4563 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4505 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | TimeoutError | - | 85 |
| speed | ClientOSError | - | 44 |
| cn-block | TimeoutError | - | 26 |
| geo | TimeoutError | - | 16 |
| 204 | ProxyError | - | 14 |
| speed | TimeoutError | - | 14 |
| geo | ClientOSError | - | 8 |
| 204 | ClientOSError | - | 7 |
| cn-block | ProxyError | - | 4 |
| cn-block | ClientOSError | - | 3 |
| geo | ProxyError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
