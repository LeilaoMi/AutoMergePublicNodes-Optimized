# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-11-12 07:29:22 |
| 运行耗时 | 297.8s |
| 订阅源总数 | 107 |
| 健康订阅源 | 86 |
| 原始节点 | 83686 |
| 去重后节点 | 26699 |
| TCP 可达 | 3000 |
| 真实可用 | 429 |
| Verified 输出 | 79 |
| Global 输出 | 300 |
| All 输出 | 26699 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.0 |
| geo | 1.6 |
| tcp | 83.3 |
| probe | 86.0 |
| real_test | 75.0 |
| china_check | 34.8 |
| write_verified | 0.0 |
| generate | 11.1 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 51343 |
| vmess | 14264 |
| shadowsocks | 9292 |
| trojan | 6712 |
| hysteria2 | 1490 |
| http | 299 |
| shadowsocksr | 159 |
| socks | 58 |
| hysteria | 35 |
| tuic | 19 |
| anytls | 15 |

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
| 89.78 | http | 220.1 | 0.9 | 22.68 | 14.96 | 0.0 | 14.64 | 20.0 | ermaozi | 172.64.69.89 |
| 89.33 | http | 233.4 | 2.3 | 22.38 | 14.91 | 0.0 | 14.64 | 20.0 | ermaozi | 44.248.167.117 |
| 88.83 | trojan | 230.5 | 0.7 | 22.44 | 14.97 | 10.0 | 9.03 | 15.54 | Au1rxx-base64 | 167.88.61.175 |
| 88.7 | hysteria2 | 201.7 | 1.2 | 23.11 | 14.96 | 3.23 | 12.86 | 15.54 | Au1rxx-base64 | 66.94.121.46 |
| 87.65 | http | 184.1 | 0.3 | 23.52 | 14.99 | 0.0 | 14.64 | 20.0 | ermaozi | 172.64.68.89 |
| 87.36 | trojan | 268.8 | 1.3 | 21.56 | 14.95 | 10.0 | 9.03 | 15.54 | Au1rxx-base64 | 66.163.114.45 |
| 87.19 | trojan | 239.0 | 1.2 | 22.24 | 14.95 | 8.7 | 9.03 | 15.54 | Au1rxx-base64 | 167.88.61.193 |
| 86.88 | trojan | 235.7 | 0.8 | 22.32 | 14.97 | 8.72 | 9.03 | 15.54 | Au1rxx-base64 | 167.88.61.20 |
| 86.75 | shadowsocks | 274.3 | 0.7 | 21.43 | 14.97 | 10.0 | 13.64 | 15.54 | Au1rxx-base64 | 95.215.201.18 |
| 86.49 | trojan | 242.4 | 1.9 | 22.17 | 14.93 | 8.7 | 9.03 | 15.54 | Au1rxx-base64 | 167.88.61.198 |
| 86.08 | shadowsocks | 316.1 | 0.2 | 20.46 | 14.99 | 10.0 | 13.64 | 15.54 | Au1rxx-base64 | 156.146.38.168 |
| 85.76 | http | 256.6 | 0.1 | 21.84 | 15.0 | 0.0 | 14.64 | 20.0 | ermaozi | 167.88.60.242 |
| 85.64 | shadowsocks | 324.3 | 0.7 | 20.27 | 14.97 | 10.0 | 13.64 | 15.54 | Au1rxx-base64 | 156.146.38.170 |
| 85.32 | http | 263.1 | 0.1 | 21.69 | 15.0 | 0.0 | 14.64 | 20.0 | ermaozi | 138.199.35.204 |
| 84.78 | trojan | 295.1 | 1.9 | 20.95 | 14.93 | 9.97 | 9.03 | 15.54 | Au1rxx-base64 | 66.163.112.121 |
| 84.66 | http | 290.3 | 0.8 | 21.06 | 14.97 | 0.0 | 14.64 | 20.0 | ermaozi | 38.95.111.226 |
| 84.46 | http | 306.9 | 0.4 | 20.67 | 14.99 | 0.0 | 14.64 | 20.0 | ermaozi | 138.199.35.212 |
| 83.87 | trojan | 269.8 | 0.5 | 21.53 | 14.98 | 6.22 | 9.03 | 15.54 | Au1rxx-base64 | 66.163.114.106 |
| 83.68 | trojan | 265.8 | 0.9 | 21.63 | 14.97 | 6.2 | 9.03 | 15.54 | Au1rxx-base64 | 66.163.114.114 |
| 83.5 | trojan | 268.0 | 2.6 | 21.57 | 14.9 | 6.13 | 9.03 | 15.54 | Au1rxx-base64 | 66.163.114.166 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.997 | 0.986 | 72 | 596 | prefer |
| Surfboard-tg-mixed | 0.901 | 0.825 | 143 | 8783 | prefer |
| Au1rxx-base64 | 0.871 | 0.804 | 199 | 1751 | prefer |
| mheidari-all | 0.735 | 0.658 | 117 | 14005 | prefer |
| xiaoji235-airport-v2ray-all | 0.335 | 1.0 | 1 | 6752 | observe |
| peasoft-NoMoreWalls | 0.26 | 1.0 | 1 | 130 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4981 | observe |
| DeltaKronecker-all | 0.255 | None | 0 | 2629 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 11526 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 6596 | observe |
| barry-far-vless | 0.255 | None | 0 | 6775 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4595 | observe |
| Au1rxx-clash | 0.245 | None | 0 | 1751 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 53 |
| 204 | ProxyError | - | 19 |
| speed | ClientOSError | - | 8 |
| 204 | TimeoutError | - | 6 |
| cn-block | ClientOSError | - | 5 |
| cn-block | TimeoutError | - | 4 |
| geo | ProxyError | - | 3 |
| cn-block | ProxyError | - | 3 |
| 204 | ClientOSError | - | 2 |
| geo | ClientOSError | - | 2 |
| speed | ProxyError | - | 1 |
| geo | TimeoutError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 80 | 79 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
