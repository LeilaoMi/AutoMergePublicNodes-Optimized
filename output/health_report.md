# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-09 07:08:06 |
| 运行耗时 | 260.1s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 82916 |
| 去重后节点 | 23032 |
| TCP 可达 | 3000 |
| 真实可用 | 528 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23032 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.0 |
| geo | 1.4 |
| tcp | 34.2 |
| probe | 59.1 |
| real_test | 116.5 |
| generate | 42.9 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 48662 |
| vmess | 13113 |
| trojan | 9929 |
| shadowsocks | 9632 |
| hysteria2 | 1382 |
| shadowsocksr | 70 |
| socks | 61 |
| http | 43 |
| hysteria | 13 |
| tuic | 11 |

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
| 82.91 | trojan | 232.3 | 532.9 | 22.4 | 0.0 | 10.0 | 13.01 | 20.0 | Au1rxx-base64 | pet-ghost.rooster465.autos |
| 82.38 | shadowsocks | 232.5 | 516.0 | 22.4 | 0.0 | 10.0 | 13.98 | 20.0 | Au1rxx-base64 | 173.244.56.6 |
| 82.29 | vless | 177.4 | 479.0 | 23.67 | 0.0 | 10.0 | 8.62 | 20.0 | Au1rxx-base64 | 66.175.217.170 |
| 82.28 | vless | 178.1 | 454.4 | 23.66 | 0.0 | 10.0 | 8.62 | 20.0 | Au1rxx-base64 | 70.39.178.231 |
| 82.21 | vless | 181.1 | 454.3 | 23.59 | 0.0 | 10.0 | 8.62 | 20.0 | Au1rxx-base64 | 70.39.197.13 |
| 82.0 | vless | 189.9 | 495.3 | 23.38 | 0.0 | 10.0 | 8.62 | 20.0 | Au1rxx-base64 | 186.241.106.97 |
| 81.98 | vless | 191.0 | 487.4 | 23.36 | 0.0 | 10.0 | 8.62 | 20.0 | Au1rxx-base64 | 167.17.68.205 |
| 81.81 | vless | 198.2 | 507.9 | 23.19 | 0.0 | 10.0 | 8.62 | 20.0 | Au1rxx-base64 | t17.qifei.app |
| 81.73 | shadowsocks | 238.6 | 605.8 | 22.25 | 0.0 | 10.0 | 13.98 | 20.0 | Au1rxx-base64 | 108.181.118.10 |
| 81.72 | shadowsocks | 260.8 | 632.2 | 21.74 | 0.0 | 10.0 | 13.98 | 20.0 | Au1rxx-base64 | 149.22.95.183 |
| 81.68 | shadowsocks | 240.8 | 607.2 | 22.2 | 0.0 | 10.0 | 13.98 | 20.0 | Au1rxx-base64 | 108.181.0.177 |
| 81.65 | vless | 204.9 | 509.4 | 23.03 | 0.0 | 10.0 | 8.62 | 20.0 | Au1rxx-base64 | 70.39.198.183 |
| 81.49 | trojan | 293.8 | 716.6 | 20.98 | 0.0 | 10.0 | 13.01 | 20.0 | Au1rxx-base64 | 44.242.235.129 |
| 81.06 | trojan | 312.1 | 773.0 | 20.55 | 0.0 | 10.0 | 13.01 | 20.0 | Au1rxx-base64 | 44.244.3.114 |
| 80.12 | vless | 184.6 | 480.1 | 23.5 | 0.0 | 10.0 | 8.62 | 20.0 | Au1rxx-base64 | 179.253.240.24 |
| 79.97 | vless | 191.3 | 498.9 | 23.35 | 0.0 | 10.0 | 8.62 | 20.0 | Au1rxx-base64 | 179.255.148.66 |
| 79.13 | shadowsocks | 270.6 | 271.8 | 21.51 | 4.81 | 9.95 | 13.98 | 20.0 | Au1rxx-base64 | 149.22.87.204 |
| 78.9 | http | 404.9 | 1137.1 | 18.4 | 0.0 | 10.0 | 14.38 | 19.12 | zhangkai | 138.199.35.217 |
| 78.87 | http | 406.4 | 1143.4 | 18.37 | 0.0 | 10.0 | 14.38 | 19.12 | zhangkai | 138.199.35.199 |
| 78.78 | http | 410.4 | 1152.8 | 18.28 | 0.0 | 10.0 | 14.38 | 19.12 | zhangkai | 138.199.35.207 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.983 | 0.919 | 397 | 1640 | prefer |
| zhangkai | 0.956 | 1.0 | 20 | 25 | prefer |
| Surfboard-tg-mixed | 0.78 | 0.705 | 88 | 6537 | prefer |
| mheidari-all | 0.625 | 0.546 | 141 | 17626 | observe |
| tg-oneclickvpnkeys | 0.318 | 1.0 | 2 | 171 | observe |
| Epodonios-all | 0.255 | None | 0 | 7052 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7616 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5295 | observe |
| barry-far-vless | 0.255 | None | 0 | 5569 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5130 | observe |
| Au1rxx-clash | 0.241 | None | 0 | 1640 | observe |
| nscl5-all | 0.235 | None | 0 | 1506 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |
| 10ium-HighSpeed | 0.209 | None | 0 | 839 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 40 |
| 204 | TimeoutError | - | 27 |
| cn-block | TimeoutError | - | 20 |
| speed | TimeoutError | - | 17 |
| speed | ClientOSError | - | 14 |
| 204 | ProxyError | - | 13 |
| geo | ClientOSError | - | 11 |
| 204 | ClientOSError | - | 4 |
| geo | ProxyError | - | 1 |
| cn-block | ClientOSError | - | 1 |
| speed | ProxyError | - | 1 |
| cn-block | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
