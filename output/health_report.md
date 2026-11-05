# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-11-05 20:10:36 |
| 运行耗时 | 272.5s |
| 订阅源总数 | 107 |
| 健康订阅源 | 88 |
| 原始节点 | 82601 |
| 去重后节点 | 26726 |
| TCP 可达 | 3000 |
| 真实可用 | 402 |
| Verified 输出 | 34 |
| Global 输出 | 300 |
| All 输出 | 26726 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.7 |
| geo | 1.5 |
| tcp | 80.5 |
| probe | 73.0 |
| real_test | 73.1 |
| china_check | 30.8 |
| write_verified | 0.0 |
| generate | 8.8 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 49811 |
| vmess | 14278 |
| shadowsocks | 9083 |
| trojan | 7334 |
| hysteria2 | 1605 |
| http | 190 |
| shadowsocksr | 149 |
| socks | 88 |
| hysteria | 33 |
| tuic | 16 |
| anytls | 14 |

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
| 93.8 | shadowsocks | 261.1 | 1.6 | 21.73 | 14.94 | 10.0 | 14.27 | 16.86 | Au1rxx-base64 | 156.146.38.168 |
| 93.18 | shadowsocks | 289.7 | 0.5 | 21.07 | 14.98 | 10.0 | 14.27 | 16.86 | Au1rxx-base64 | 156.146.38.167 |
| 90.2 | shadowsocks | 319.4 | 7.5 | 20.38 | 14.72 | 10.0 | 14.27 | 16.86 | Au1rxx-base64 | 193.151.163.18 |
| 89.09 | shadowsocks | 314.4 | 2.3 | 20.5 | 14.91 | 10.0 | 14.27 | 16.86 | Au1rxx-base64 | 185.230.230.18 |
| 88.66 | shadowsocks | 307.1 | 3.6 | 20.67 | 14.87 | 10.0 | 14.27 | 16.86 | Au1rxx-base64 | 173.244.56.6 |
| 88.55 | shadowsocks | 337.2 | 1.3 | 19.97 | 14.95 | 10.0 | 14.27 | 16.86 | Au1rxx-base64 | 37.19.198.160 |
| 88.44 | shadowsocks | 290.8 | 9.6 | 21.05 | 14.64 | 10.0 | 14.27 | 16.86 | Au1rxx-base64 | 95.215.201.18 |
| 88.2 | shadowsocks | 282.6 | 0.9 | 21.24 | 14.97 | 10.0 | 14.27 | 16.86 | Au1rxx-base64 | 149.22.95.183 |
| 87.81 | shadowsocks | 302.4 | 0.4 | 20.78 | 14.99 | 10.0 | 14.27 | 16.86 | Au1rxx-base64 | 37.19.198.244 |
| 87.56 | hysteria2 | 273.4 | 4.6 | 21.45 | 14.83 | 4.43 | 13.0 | 16.86 | Au1rxx-base64 | 66.94.121.46 |
| 87.46 | trojan | 321.5 | 1.6 | 20.33 | 14.94 | 9.83 | 12.83 | 16.86 | Au1rxx-base64 | 66.163.112.121 |
| 87.32 | shadowsocks | 331.1 | 4.3 | 20.11 | 14.84 | 8.65 | 14.27 | 16.86 | Au1rxx-base64 | 193.151.160.18 |
| 87.21 | trojan | 348.6 | 1.3 | 19.71 | 14.95 | 10.0 | 12.83 | 16.86 | Au1rxx-base64 | 216.238.80.100 |
| 86.9 | vless | 382.9 | 5.5 | 18.91 | 14.79 | 9.73 | 8.83 | 16.86 | Au1rxx-base64 | 167.17.69.171 |
| 86.78 | shadowsocks | 361.8 | 6.7 | 19.4 | 14.75 | 10.0 | 14.27 | 16.86 | Au1rxx-base64 | 193.151.160.9 |
| 86.7 | hysteria2 | 218.2 | 9.4 | 22.73 | 14.65 | 0.0 | 13.0 | 17.32 | mheidari-all | 88.216.195.188 |
| 86.54 | trojan | 317.4 | 1.8 | 20.43 | 14.93 | 8.52 | 12.83 | 16.86 | Au1rxx-base64 | 66.163.112.242 |
| 86.21 | vless | 340.4 | 27.6 | 19.9 | 13.97 | 9.49 | 8.83 | 16.86 | Au1rxx-base64 | 169.40.42.89 |
| 85.88 | shadowsocks | 244.6 | 5.2 | 22.12 | 14.81 | 6.82 | 14.27 | 16.86 | Au1rxx-base64 | 156.146.38.169 |
| 85.83 | trojan | 319.2 | 5.6 | 20.39 | 14.79 | 7.85 | 12.83 | 16.86 | Au1rxx-base64 | 66.163.112.76 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.993 | 0.984 | 63 | 593 | prefer |
| mheidari-all | 0.942 | 0.869 | 107 | 14461 | prefer |
| Surfboard-tg-mixed | 0.771 | 0.694 | 134 | 8690 | prefer |
| Au1rxx-base64 | 0.756 | 0.688 | 218 | 1751 | prefer |
| xiaoji235-airport-v2ray-all | 0.391 | 1.0 | 2 | 6752 | observe |
| DeltaKronecker-all | 0.335 | 1.0 | 1 | 2653 | observe |
| peasoft-NoMoreWalls | 0.259 | 1.0 | 1 | 96 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5039 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 10977 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 6065 | observe |
| barry-far-vless | 0.255 | None | 0 | 6358 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4612 | observe |
| Au1rxx-clash | 0.245 | None | 0 | 1751 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | ProxyError | - | 53 |
| test_one_timeout | 15.0s | - | 50 |
| cn-block | ClientOSError | - | 6 |
| cn-block | TimeoutError | - | 6 |
| cn-block | ProxyError | - | 5 |
| 204 | TimeoutError | - | 4 |
| 204 | ClientOSError | - | 2 |
| speed | ProxyError | - | 1 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 36 | 34 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
