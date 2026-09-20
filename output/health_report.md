# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-20 11:11:31 |
| 运行耗时 | 556.5s |
| 订阅源总数 | 107 |
| 健康订阅源 | 94 |
| 原始节点 | 83340 |
| 去重后节点 | 23411 |
| TCP 可达 | 3000 |
| 真实可用 | 471 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23411 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.0 |
| geo | 1.5 |
| tcp | 38.4 |
| probe | 213.6 |
| real_test | 227.7 |
| generate | 71.3 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 49643 |
| vmess | 13449 |
| shadowsocks | 9954 |
| trojan | 8246 |
| hysteria2 | 1173 |
| http | 667 |
| shadowsocksr | 120 |
| socks | 72 |
| hysteria | 11 |
| tuic | 3 |
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
| 80.05 | shadowsocks | 259.7 | 670.3 | 21.77 | 0.0 | 10.0 | 13.86 | 18.42 | Au1rxx-base64 | 173.244.56.6 |
| 79.25 | hysteria2 | 259.3 | 557.3 | 21.78 | 0.0 | 10.0 | 10.31 | 18.42 | Au1rxx-base64 | 66.94.121.46 |
| 78.04 | trojan | 230.5 | 524.9 | 22.44 | 0.0 | 10.0 | 9.68 | 18.42 | Au1rxx-base64 | 100.42.228.109 |
| 75.94 | http | 207.6 | 539.2 | 22.97 | 0.0 | 10.0 | 11.13 | 14.84 | ermaozi | 138.199.35.217 |
| 75.91 | http | 208.9 | 544.7 | 22.94 | 0.0 | 10.0 | 11.13 | 14.84 | ermaozi | 138.199.35.219 |
| 75.77 | http | 215.2 | 569.4 | 22.8 | 0.0 | 10.0 | 11.13 | 14.84 | ermaozi | 138.199.35.198 |
| 75.75 | http | 216.1 | 570.7 | 22.78 | 0.0 | 10.0 | 11.13 | 14.84 | ermaozi | 138.199.35.214 |
| 75.41 | http | 230.7 | 612.5 | 22.44 | 0.0 | 10.0 | 11.13 | 14.84 | ermaozi | 138.199.35.216 |
| 75.35 | http | 233.2 | 621.4 | 22.38 | 0.0 | 10.0 | 11.13 | 14.84 | ermaozi | 138.199.35.206 |
| 75.31 | shadowsocks | 268.1 | 659.1 | 21.57 | 0.0 | 10.0 | 13.86 | 13.88 | Surfboard-tg-mixed | 173.244.56.9 |
| 74.88 | vless | 206.4 | 509.1 | 23.0 | 0.0 | 10.0 | 8.63 | 18.42 | Au1rxx-base64 | 162.159.45.19 |
| 74.52 | vless | 207.6 | 515.8 | 22.97 | 0.0 | 10.0 | 8.63 | 18.42 | Au1rxx-base64 | 104.18.34.14 |
| 73.79 | shadowsocks | 283.9 | 637.5 | 21.21 | 0.0 | 10.0 | 13.86 | 18.42 | Au1rxx-base64 | 23.150.248.20 |
| 73.45 | shadowsocks | 331.7 | 683.4 | 20.1 | 0.0 | 10.0 | 13.86 | 18.42 | Au1rxx-base64 | 198.98.53.130 |
| 73.19 | shadowsocks | 351.3 | 754.6 | 19.65 | 0.0 | 10.0 | 13.86 | 18.42 | Au1rxx-base64 | 37.19.198.243 |
| 72.36 | shadowsocks | 256.8 | 627.4 | 21.83 | 0.0 | 10.0 | 13.86 | 18.42 | Au1rxx-base64 | 156.146.38.170 |
| 72.05 | shadowsocks | 260.6 | 640.5 | 21.74 | 0.0 | 10.0 | 13.86 | 18.42 | Au1rxx-base64 | 156.146.38.169 |
| 71.59 | shadowsocks | 264.0 | 652.1 | 21.67 | 0.0 | 10.0 | 13.86 | 18.42 | Au1rxx-base64 | 156.146.38.168 |
| 71.19 | vless | 351.0 | 841.3 | 19.65 | 0.0 | 10.0 | 8.63 | 18.42 | Au1rxx-base64 | 15.204.97.209 |
| 70.94 | http | 207.8 | 544.9 | 22.97 | 0.0 | 10.0 | 11.13 | 14.84 | ermaozi | 138.199.35.196 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| mheidari-all | 1.0 | 0.951 | 41 | 15979 | prefer |
| Au1rxx-base64 | 0.942 | 0.881 | 269 | 1589 | prefer |
| ermaozi | 0.778 | 0.774 | 53 | 365 | prefer |
| Surfboard-tg-mixed | 0.719 | 0.64 | 189 | 7118 | prefer |
| DeltaKronecker-all | 0.47 | 0.388 | 80 | 6092 | observe |
| mahdibland-V2RayAggregator | 0.335 | 1.0 | 1 | 4315 | observe |
| tg-oneclickvpnkeys | 0.259 | 1.0 | 1 | 89 | observe |
| Epodonios-all | 0.255 | None | 0 | 7603 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 8786 | observe |
| barry-far-vless | 0.255 | None | 0 | 5912 | observe |
| Au1rxx-clash | 0.239 | None | 0 | 1589 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |
| 10ium-HighSpeed | 0.209 | None | 0 | 839 | observe |
| Surfboard-tg-vless | 0.207 | 0.0 | 1 | 5686 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | ClientOSError | - | 41 |
| geo | TimeoutError | - | 36 |
| 204 | TimeoutError | - | 23 |
| 204 | ProxyError | - | 21 |
| cn-block | TimeoutError | - | 16 |
| cn-block | ClientOSError | - | 12 |
| speed | TimeoutError | - | 12 |
| speed | ClientOSError | - | 5 |
| cn-block | ProxyError | - | 2 |
| 204 | ClientOSError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
