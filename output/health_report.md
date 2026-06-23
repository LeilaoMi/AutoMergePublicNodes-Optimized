# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-06-23 20:17:13 |
| 运行耗时 | 257.7s |
| 订阅源总数 | 107 |
| 健康订阅源 | 105 |
| 原始节点 | 77271 |
| 去重后节点 | 22334 |
| TCP 可达 | 3000 |
| 真实可用 | 369 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22334 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.5 |
| geo | 1.4 |
| tcp | 29.9 |
| probe | 62.3 |
| real_test | 124.2 |
| generate | 35.4 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 46040 |
| trojan | 10492 |
| vmess | 10191 |
| shadowsocks | 9902 |
| hysteria2 | 255 |
| http | 159 |
| shadowsocksr | 157 |
| socks | 66 |
| hysteria | 6 |
| tuic | 2 |
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
| 77.53 | shadowsocks | 231.1 | 587.1 | 22.43 | 0.0 | 10.0 | 13.88 | 15.22 | Au1rxx-base64 | 156.146.38.168 |
| 77.31 | shadowsocks | 240.7 | 608.4 | 22.21 | 0.0 | 10.0 | 13.88 | 15.22 | Au1rxx-base64 | 156.146.38.170 |
| 76.23 | shadowsocks | 244.1 | 628.8 | 22.13 | 0.0 | 10.0 | 13.88 | 15.22 | Au1rxx-base64 | 156.146.38.167 |
| 73.58 | shadowsocks | 248.9 | 597.8 | 22.02 | 0.0 | 10.0 | 13.88 | 15.22 | Au1rxx-base64 | 156.146.38.169 |
| 73.46 | shadowsocks | 259.3 | 579.2 | 21.78 | 0.0 | 10.0 | 13.88 | 15.22 | Au1rxx-base64 | 108.181.0.177 |
| 71.67 | shadowsocks | 291.4 | 561.5 | 21.03 | 0.0 | 10.0 | 13.88 | 15.22 | Au1rxx-base64 | 149.22.95.183 |
| 71.06 | shadowsocks | 328.4 | 714.3 | 20.18 | 0.0 | 10.0 | 13.88 | 15.22 | Au1rxx-base64 | 37.19.198.236 |
| 70.88 | shadowsocks | 331.3 | 724.6 | 20.11 | 0.0 | 10.0 | 13.88 | 15.22 | Au1rxx-base64 | 37.19.198.244 |
| 70.82 | shadowsocks | 327.8 | 714.0 | 20.19 | 0.0 | 10.0 | 13.88 | 15.22 | Au1rxx-base64 | 37.19.198.243 |
| 70.61 | shadowsocks | 236.5 | 520.9 | 22.3 | 0.0 | 10.0 | 13.88 | 15.22 | Au1rxx-base64 | 216.105.168.18 |
| 70.32 | shadowsocks | 320.1 | 725.2 | 20.37 | 0.0 | 10.0 | 13.88 | 15.22 | Au1rxx-base64 | 108.181.118.10 |
| 69.84 | shadowsocks | 375.9 | 860.0 | 19.08 | 0.0 | 10.0 | 13.88 | 15.22 | Au1rxx-base64 | 37.19.198.160 |
| 69.28 | shadowsocks | 363.2 | 799.3 | 19.37 | 0.0 | 10.0 | 13.88 | 15.22 | Au1rxx-base64 | 173.244.56.9 |
| 68.94 | vless | 345.2 | 838.5 | 19.79 | 0.0 | 10.0 | 6.15 | 15.22 | Au1rxx-base64 | 15.204.97.219 |
| 68.53 | shadowsocks | 327.1 | 376.1 | 20.21 | 0.9 | 9.8 | 13.88 | 15.22 | Au1rxx-base64 | 149.22.87.204 |
| 68.33 | shadowsocks | 328.9 | 378.4 | 20.16 | 0.81 | 9.79 | 13.88 | 15.22 | Au1rxx-base64 | 149.22.87.241 |
| 68.21 | vless | 359.6 | 874.9 | 19.45 | 0.0 | 10.0 | 6.15 | 15.22 | Au1rxx-base64 | 15.204.97.214 |
| 66.12 | shadowsocks | 338.7 | 690.3 | 19.94 | 0.0 | 10.0 | 13.88 | 15.22 | Au1rxx-base64 | 198.98.53.130 |
| 65.94 | shadowsocks | 331.5 | 389.2 | 20.1 | 0.4 | 9.79 | 13.88 | 15.22 | Au1rxx-base64 | 149.22.87.240 |
| 65.6 | shadowsocks | 387.8 | 499.5 | 18.8 | 0.0 | 9.79 | 13.88 | 15.22 | Au1rxx-base64 | 103.106.228.175 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.984 | 1.0 | 50 | 73 | prefer |
| Au1rxx-base64 | 0.797 | 0.8 | 70 | 124 | prefer |
| Surfboard-tg-mixed | 0.722 | 0.644 | 216 | 5373 | prefer |
| DeltaKronecker-all | 0.55 | 0.469 | 81 | 6437 | observe |
| mheidari-all | 0.532 | 0.451 | 184 | 15741 | observe |
| Surfboard-tg-vless | 0.335 | 1.0 | 1 | 4175 | observe |
| Barabama-yudou | 0.318 | 1.0 | 2 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4576 | observe |
| Epodonios-all | 0.255 | None | 0 | 8167 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7442 | observe |
| barry-far-vless | 0.255 | None | 0 | 4987 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4664 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | ClientOSError | - | 60 |
| speed | ClientOSError | - | 56 |
| cn-block | TimeoutError | - | 26 |
| 204 | TimeoutError | - | 24 |
| 204 | ProxyError | - | 21 |
| geo | TimeoutError | - | 13 |
| cn-block | ClientOSError | - | 9 |
| speed | TimeoutError | - | 7 |
| cn-block | ProxyError | - | 6 |
| 204 | ClientOSError | - | 5 |
| speed | ProxyError | - | 5 |
| geo | ProxyError | - | 4 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
