# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-21 12:07:05 |
| 运行耗时 | 298.4s |
| 订阅源总数 | 107 |
| 健康订阅源 | 92 |
| 原始节点 | 95764 |
| 去重后节点 | 26911 |
| TCP 可达 | 3000 |
| 真实可用 | 410 |
| Verified 输出 | 118 |
| Global 输出 | 300 |
| All 输出 | 26911 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.4 |
| geo | 1.7 |
| tcp | 81.6 |
| probe | 80.6 |
| real_test | 84.4 |
| china_check | 33.7 |
| write_verified | 0.0 |
| generate | 11.1 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 56955 |
| vmess | 16905 |
| shadowsocks | 11803 |
| trojan | 8437 |
| hysteria2 | 1216 |
| http | 173 |
| shadowsocksr | 165 |
| socks | 63 |
| anytls | 24 |
| hysteria | 17 |
| tuic | 6 |

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
| 94.67 | shadowsocks | 295.4 | 2.0 | 20.94 | 14.93 | 10.0 | 14.4 | 18.44 | Au1rxx-base64 | 156.146.38.168 |
| 94.13 | hysteria2 | 309.5 | 0.1 | 20.61 | 14.99 | 9.89 | 13.64 | 18.44 | Au1rxx-base64 | 129.213.91.185 |
| 94.07 | vless | 205.4 | 3.3 | 23.02 | 14.88 | 9.22 | 8.51 | 18.44 | Au1rxx-base64 | 154.29.145.196 |
| 93.92 | vless | 219.8 | 0.9 | 22.69 | 14.97 | 9.31 | 8.51 | 18.44 | Au1rxx-base64 | 45.63.53.81 |
| 93.66 | shadowsocks | 278.2 | 0.7 | 21.34 | 14.98 | 10.0 | 14.4 | 18.44 | Au1rxx-base64 | 95.215.201.18 |
| 93.56 | shadowsocks | 301.2 | 1.8 | 20.81 | 14.93 | 10.0 | 14.4 | 18.44 | Au1rxx-base64 | 156.146.38.169 |
| 92.3 | shadowsocks | 252.7 | 0.1 | 21.93 | 15.0 | 10.0 | 14.4 | 18.44 | Au1rxx-base64 | 156.146.38.170 |
| 91.26 | shadowsocks | 289.4 | 0.2 | 21.08 | 14.99 | 10.0 | 14.4 | 18.44 | Au1rxx-base64 | 149.22.95.183 |
| 90.71 | shadowsocks | 261.5 | 1.1 | 21.73 | 14.96 | 10.0 | 14.4 | 18.44 | Au1rxx-base64 | 156.146.38.167 |
| 90.68 | vless | 219.2 | 0.1 | 22.7 | 15.0 | 6.03 | 8.51 | 18.44 | Au1rxx-base64 | 144.202.126.147 |
| 90.52 | trojan | 392.1 | 2.9 | 18.7 | 14.89 | 9.97 | 14.1 | 18.44 | Au1rxx-base64 | 66.23.203.21 |
| 90.45 | vless | 225.4 | 0.7 | 22.56 | 14.97 | 5.97 | 8.51 | 18.44 | Au1rxx-base64 | 154.12.38.202 |
| 89.59 | vless | 286.4 | 1.7 | 21.15 | 14.94 | 9.82 | 8.51 | 18.44 | Au1rxx-base64 | 44.248.233.99 |
| 88.95 | vless | 278.8 | 5.1 | 21.32 | 14.81 | 8.97 | 8.51 | 18.44 | Au1rxx-base64 | 154.40.55.185 |
| 88.48 | http | 194.3 | 0.3 | 23.28 | 14.99 | 0.0 | 14.03 | 19.18 | ermaozi-get_subscribe | 138.199.35.201 |
| 88.44 | http | 193.7 | 1.6 | 23.29 | 14.94 | 0.0 | 14.03 | 19.18 | ermaozi-get_subscribe | 138.199.35.212 |
| 88.38 | http | 195.8 | 1.8 | 23.24 | 14.93 | 0.0 | 14.03 | 19.18 | ermaozi-get_subscribe | 138.199.35.199 |
| 88.37 | shadowsocks | 350.1 | 3.4 | 19.67 | 14.87 | 10.0 | 14.4 | 18.44 | Au1rxx-base64 | 37.19.198.244 |
| 88.16 | http | 201.9 | 4.2 | 23.11 | 14.84 | 0.0 | 14.03 | 19.18 | ermaozi-get_subscribe | 138.199.35.213 |
| 88.14 | http | 197.3 | 7.4 | 23.21 | 14.72 | 0.0 | 14.03 | 19.18 | ermaozi-get_subscribe | 138.199.35.195 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi-get_subscribe | 0.946 | 0.938 | 65 | 516 | prefer |
| zhangkai | 0.932 | 0.963 | 27 | 31 | prefer |
| mheidari-all | 0.865 | 0.794 | 63 | 23726 | prefer |
| Au1rxx-base64 | 0.845 | 0.786 | 266 | 1541 | prefer |
| Surfboard-tg-mixed | 0.678 | 0.6 | 105 | 6977 | observe |
| DeltaKronecker-all | 0.32 | 0.5 | 4 | 4067 | observe |
| peasoft-NoMoreWalls | 0.261 | 1.0 | 1 | 139 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4925 | observe |
| Epodonios-all | 0.255 | None | 0 | 7465 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 10023 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5462 | observe |
| barry-far-vless | 0.255 | None | 0 | 5674 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4127 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 63 |
| speed | ClientOSError | - | 11 |
| cn-block | TimeoutError | - | 10 |
| geo | ClientOSError | - | 9 |
| 204 | ProxyError | - | 8 |
| cn-block | ClientOSError | - | 5 |
| 204 | ClientOSError | - | 5 |
| cn-block | ProxyError | - | 4 |
| geo | ProxyError | - | 2 |
| 204 | TimeoutError | - | 2 |
| speed | TimeoutError | - | 1 |
| geo | TimeoutError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 118 | 118 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
