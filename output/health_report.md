# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-09 18:53:23 |
| 运行耗时 | 228.2s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 86184 |
| 去重后节点 | 24016 |
| TCP 可达 | 3000 |
| 真实可用 | 432 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 24016 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.6 |
| geo | 1.4 |
| tcp | 35.3 |
| probe | 52.3 |
| real_test | 92.6 |
| generate | 38.9 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 51605 |
| vmess | 13182 |
| trojan | 10058 |
| shadowsocks | 9651 |
| hysteria2 | 1464 |
| shadowsocksr | 75 |
| socks | 67 |
| http | 33 |
| anytls | 26 |
| hysteria | 15 |
| tuic | 8 |

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
| 83.75 | http | 194.3 | 500.7 | 23.28 | 0.0 | 10.0 | 14.35 | 19.12 | zhangkai | 138.199.35.217 |
| 83.73 | http | 195.3 | 506.7 | 23.26 | 0.0 | 10.0 | 14.35 | 19.12 | zhangkai | 138.199.35.214 |
| 83.68 | http | 197.1 | 503.5 | 23.21 | 0.0 | 10.0 | 14.35 | 19.12 | zhangkai | 138.199.35.207 |
| 83.65 | http | 198.7 | 514.5 | 23.18 | 0.0 | 10.0 | 14.35 | 19.12 | zhangkai | 138.199.35.199 |
| 82.49 | vless | 186.0 | 481.3 | 23.47 | 0.0 | 10.0 | 9.24 | 19.78 | Au1rxx-base64 | 179.253.240.24 |
| 82.48 | trojan | 293.7 | 714.5 | 20.98 | 0.0 | 10.0 | 14.22 | 19.78 | Au1rxx-base64 | 35.86.90.51 |
| 82.47 | vless | 186.8 | 483.9 | 23.45 | 0.0 | 10.0 | 9.24 | 19.78 | Au1rxx-base64 | 179.255.148.66 |
| 82.32 | vless | 193.4 | 491.7 | 23.3 | 0.0 | 10.0 | 9.24 | 19.78 | Au1rxx-base64 | 186.241.106.97 |
| 82.29 | trojan | 213.8 | 477.7 | 22.83 | 0.0 | 7.96 | 14.22 | 19.78 | Au1rxx-base64 | fleet-bonefish.rooster465.autos |
| 82.13 | vless | 201.7 | 515.0 | 23.11 | 0.0 | 10.0 | 9.24 | 19.78 | Au1rxx-base64 | 167.17.68.205 |
| 82.08 | trojan | 218.3 | 491.8 | 22.72 | 0.0 | 7.96 | 14.22 | 19.78 | Au1rxx-base64 | natural-collie.rooster465.autos |
| 81.8 | trojan | 232.8 | 532.0 | 22.39 | 0.0 | 7.91 | 14.22 | 19.78 | Au1rxx-base64 | pet-ghost.rooster465.autos |
| 81.61 | trojan | 272.3 | 645.0 | 21.47 | 0.0 | 8.64 | 14.22 | 19.78 | Au1rxx-base64 | 44.246.163.102 |
| 81.23 | trojan | 277.8 | 659.2 | 21.35 | 0.0 | 8.65 | 14.22 | 19.78 | Au1rxx-base64 | 44.244.3.114 |
| 81.07 | shadowsocks | 267.9 | 621.9 | 21.58 | 0.0 | 10.0 | 14.48 | 19.78 | Au1rxx-base64 | 173.244.56.6 |
| 80.92 | shadowsocks | 238.0 | 601.9 | 22.27 | 0.0 | 8.89 | 14.48 | 19.78 | Au1rxx-base64 | 108.181.118.10 |
| 80.78 | vless | 201.1 | 434.3 | 23.12 | 0.0 | 10.0 | 9.24 | 19.78 | Au1rxx-base64 | 70.39.197.13 |
| 80.76 | shadowsocks | 244.8 | 629.9 | 22.11 | 0.0 | 8.89 | 14.48 | 19.78 | Au1rxx-base64 | 108.181.0.177 |
| 79.88 | vless | 242.3 | 684.6 | 22.17 | 0.0 | 8.69 | 9.24 | 19.78 | Au1rxx-base64 | 66.175.217.170 |
| 79.41 | vless | 200.4 | 498.7 | 23.14 | 0.0 | 7.25 | 9.24 | 19.78 | Au1rxx-base64 | jyvlryz.cvewfjg.shop |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.987 | 0.922 | 371 | 1688 | prefer |
| zhangkai | 0.956 | 1.0 | 20 | 25 | prefer |
| Surfboard-tg-mixed | 0.718 | 0.641 | 92 | 6634 | prefer |
| mheidari-all | 0.413 | 0.321 | 28 | 20206 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| tg-oneclickvpnkeys | 0.259 | 1.0 | 1 | 107 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5505 | observe |
| Epodonios-all | 0.255 | None | 0 | 7178 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7585 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5470 | observe |
| barry-far-vless | 0.255 | None | 0 | 5784 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5189 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.243 | None | 0 | 1688 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | TimeoutError | - | 18 |
| geo | ClientOSError | - | 15 |
| cn-block | TimeoutError | - | 12 |
| speed | TimeoutError | - | 10 |
| 204 | ProxyError | - | 7 |
| geo | TimeoutError | - | 7 |
| speed | ClientOSError | - | 6 |
| 204 | ClientOSError | - | 3 |
| geo | ProxyError | - | 2 |
| cn-block | ClientOSError | - | 2 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
