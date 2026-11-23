# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-11-23 07:58:01 |
| 运行耗时 | 313.9s |
| 订阅源总数 | 107 |
| 健康订阅源 | 88 |
| 原始节点 | 83225 |
| 去重后节点 | 28655 |
| TCP 可达 | 3000 |
| 真实可用 | 404 |
| Verified 输出 | 82 |
| Global 输出 | 300 |
| All 输出 | 28655 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.0 |
| geo | 1.6 |
| tcp | 85.3 |
| probe | 96.2 |
| real_test | 74.3 |
| china_check | 33.8 |
| write_verified | 0.0 |
| generate | 15.8 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 48781 |
| vmess | 15053 |
| shadowsocks | 10529 |
| trojan | 6691 |
| hysteria2 | 1576 |
| http | 237 |
| shadowsocksr | 153 |
| socks | 136 |
| hysteria | 32 |
| anytls | 21 |
| tuic | 16 |

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
| 90.2 | shadowsocks | 239.4 | 3.8 | 22.24 | 14.86 | 10.0 | 12.42 | 14.68 | Au1rxx-base64 | 173.244.56.9 |
| 89.86 | shadowsocks | 232.5 | 3.4 | 22.39 | 14.87 | 10.0 | 12.42 | 14.68 | Au1rxx-base64 | 95.215.201.18 |
| 89.84 | http | 187.5 | 1.0 | 23.44 | 14.96 | 0.0 | 14.4 | 19.54 | ermaozi | 172.64.68.89 |
| 89.0 | http | 199.1 | 2.8 | 23.17 | 14.89 | 0.0 | 14.4 | 19.54 | ermaozi | 38.95.111.226 |
| 88.32 | http | 210.8 | 0.5 | 22.9 | 14.98 | 0.0 | 14.4 | 19.54 | ermaozi | 172.64.69.89 |
| 86.6 | shadowsocks | 295.3 | 0.2 | 20.94 | 14.99 | 10.0 | 12.42 | 14.68 | Au1rxx-base64 | 156.146.38.170 |
| 86.03 | hysteria2 | 248.5 | 5.1 | 22.03 | 14.81 | 5.01 | 10.5 | 14.68 | Au1rxx-base64 | 66.94.121.46 |
| 85.55 | shadowsocks | 297.5 | 6.9 | 20.89 | 14.74 | 10.0 | 12.42 | 14.68 | Au1rxx-base64 | 156.146.38.168 |
| 83.85 | http | 425.5 | 0.4 | 17.93 | 14.98 | 0.0 | 14.4 | 19.54 | ermaozi | 138.199.35.211 |
| 83.48 | vless | 374.5 | 5.0 | 19.11 | 14.81 | 10.0 | 9.88 | 14.68 | Au1rxx-base64 | 15.204.97.214 |
| 83.42 | vless | 211.7 | 2.0 | 22.88 | 14.92 | 0.0 | 9.88 | 15.74 | mheidari-all | 172.235.50.209 |
| 83.24 | shadowsocks | 188.0 | 1.3 | 23.43 | 14.95 | 0.0 | 12.42 | 16.94 | Surfboard-tg-mixed | 104.238.140.45 |
| 82.68 | shadowsocks | 212.2 | 1.0 | 22.86 | 14.96 | 0.0 | 12.42 | 16.94 | Surfboard-tg-mixed | 137.184.89.151 |
| 82.35 | shadowsocks | 227.4 | 0.6 | 22.51 | 14.98 | 0.0 | 12.42 | 16.94 | Surfboard-tg-mixed | 169.197.142.68 |
| 82.08 | shadowsocks | 362.6 | 0.1 | 19.38 | 15.0 | 10.0 | 12.42 | 14.68 | Au1rxx-base64 | 37.19.198.244 |
| 81.98 | shadowsocks | 358.3 | 0.4 | 19.48 | 14.98 | 10.0 | 12.42 | 14.68 | Au1rxx-base64 | 37.19.198.160 |
| 81.85 | shadowsocks | 366.5 | 0.4 | 19.29 | 14.98 | 10.0 | 12.42 | 14.68 | Au1rxx-base64 | 37.19.198.236 |
| 81.82 | shadowsocks | 368.5 | 2.1 | 19.25 | 14.92 | 10.0 | 12.42 | 14.68 | Au1rxx-base64 | 37.19.198.243 |
| 81.78 | vless | 199.1 | 0.2 | 23.17 | 14.99 | 0.0 | 9.88 | 15.74 | mheidari-all | 45.32.70.42 |
| 81.73 | shadowsocks | 294.2 | 0.1 | 20.97 | 15.0 | 9.79 | 12.42 | 14.68 | Au1rxx-base64 | 149.22.87.240 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 1.0 | 1.0 | 74 | 486 | prefer |
| Au1rxx-base64 | 0.89 | 0.824 | 131 | 1751 | prefer |
| Surfboard-tg-mixed | 0.876 | 0.798 | 243 | 8701 | prefer |
| mheidari-all | 0.741 | 0.667 | 54 | 15418 | prefer |
| xiaoji235-airport-v2ray-all | 0.335 | 1.0 | 1 | 6752 | observe |
| roosterkid-openproxylist-v2ray | 0.316 | 1.0 | 2 | 119 | observe |
| ermaozi-get_subscribe | 0.272 | 1.0 | 1 | 421 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5069 | observe |
| DeltaKronecker-all | 0.255 | None | 0 | 2671 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 11834 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5650 | observe |
| barry-far-vless | 0.255 | None | 0 | 5831 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4514 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 41 |
| 204 | ProxyError | - | 22 |
| cn-block | ProxyError | - | 7 |
| cn-block | ClientOSError | - | 5 |
| cn-block | TimeoutError | - | 5 |
| 204 | TimeoutError | - | 3 |
| geo | ProxyError | - | 3 |
| speed | ProxyError | - | 2 |
| 204 | ClientOSError | - | 2 |
| speed | TimeoutError | - | 1 |
| speed | ClientOSError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 41 | 82 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
