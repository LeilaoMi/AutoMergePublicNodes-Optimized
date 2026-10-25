# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-25 21:02:39 |
| 运行耗时 | 272.5s |
| 订阅源总数 | 107 |
| 健康订阅源 | 88 |
| 原始节点 | 98673 |
| 去重后节点 | 27238 |
| TCP 可达 | 3000 |
| 真实可用 | 363 |
| Verified 输出 | 105 |
| Global 输出 | 300 |
| All 输出 | 27238 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.3 |
| geo | 1.9 |
| tcp | 84.0 |
| probe | 80.1 |
| real_test | 71.8 |
| china_check | 18.8 |
| write_verified | 0.0 |
| generate | 10.6 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 58865 |
| vmess | 17471 |
| shadowsocks | 12798 |
| trojan | 7595 |
| hysteria2 | 1422 |
| http | 253 |
| shadowsocksr | 167 |
| socks | 56 |
| anytls | 23 |
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
| 93.54 | shadowsocks | 237.5 | 2.0 | 22.28 | 14.92 | 10.0 | 12.76 | 17.58 | Au1rxx-base64 | 156.146.38.170 |
| 92.08 | trojan | 263.1 | 1.3 | 21.69 | 14.95 | 10.0 | 10.86 | 17.58 | Au1rxx-base64 | 66.23.203.21 |
| 91.9 | shadowsocks | 310.7 | 0.9 | 20.59 | 14.97 | 10.0 | 12.76 | 17.58 | Au1rxx-base64 | 156.146.38.169 |
| 91.81 | shadowsocks | 294.7 | 4.5 | 20.96 | 14.83 | 10.0 | 12.76 | 17.58 | Au1rxx-base64 | 37.19.198.244 |
| 91.54 | shadowsocks | 297.8 | 0.9 | 20.89 | 14.97 | 10.0 | 12.76 | 17.58 | Au1rxx-base64 | 37.19.198.236 |
| 90.91 | shadowsocks | 286.9 | 1.8 | 21.14 | 14.93 | 10.0 | 12.76 | 17.58 | Au1rxx-base64 | 37.19.198.160 |
| 89.54 | shadowsocks | 258.6 | 8.1 | 21.79 | 14.7 | 10.0 | 12.76 | 17.58 | Au1rxx-base64 | 156.146.38.168 |
| 89.35 | hysteria2 | 399.1 | 0.1 | 18.54 | 14.99 | 6.41 | 13.33 | 17.58 | Au1rxx-base64 | 129.213.91.185 |
| 88.63 | vless | 413.2 | 0.6 | 18.21 | 14.98 | 10.0 | 9.81 | 17.58 | Au1rxx-base64 | 185.95.231.156 |
| 88.39 | vless | 307.6 | 1.0 | 20.66 | 14.96 | 10.0 | 9.81 | 17.58 | Au1rxx-base64 | 172.236.227.60 |
| 88.21 | vless | 415.6 | 1.1 | 18.16 | 14.96 | 10.0 | 9.81 | 17.58 | Au1rxx-base64 | 169.40.42.74 |
| 87.91 | vless | 340.3 | 3.8 | 19.9 | 14.86 | 10.0 | 9.81 | 17.58 | Au1rxx-base64 | 167.17.69.171 |
| 87.84 | shadowsocks | 246.2 | 0.7 | 22.08 | 14.97 | 10.0 | 12.76 | 17.58 | Au1rxx-base64 | 156.146.38.167 |
| 87.8 | vless | 296.9 | 6.9 | 20.9 | 14.74 | 9.39 | 9.81 | 17.58 | Au1rxx-base64 | 45.63.53.81 |
| 87.61 | shadowsocks | 315.4 | 1.6 | 20.48 | 14.94 | 10.0 | 12.76 | 17.58 | Au1rxx-base64 | 149.22.95.183 |
| 87.5 | shadowsocks | 383.7 | 10.3 | 18.9 | 14.61 | 10.0 | 12.76 | 17.58 | Au1rxx-base64 | 45.86.51.18 |
| 87.27 | shadowsocks | 297.4 | 3.1 | 20.89 | 14.88 | 6.27 | 12.76 | 17.58 | Au1rxx-base64 | 37.19.198.243 |
| 87.25 | shadowsocks | 318.8 | 4.6 | 20.4 | 14.83 | 6.18 | 12.76 | 17.58 | Au1rxx-base64 | 185.230.230.18 |
| 87.23 | http | 297.2 | 1.3 | 20.9 | 14.95 | 0.0 | 14.54 | 19.84 | ermaozi | 154.47.25.78 |
| 87.23 | shadowsocks | 311.9 | 1.6 | 20.56 | 14.94 | 10.0 | 12.76 | 17.58 | Au1rxx-base64 | 173.244.56.9 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.992 | 0.984 | 63 | 575 | prefer |
| Au1rxx-base64 | 0.873 | 0.807 | 326 | 1702 | prefer |
| mheidari-all | 0.772 | 0.703 | 37 | 24713 | prefer |
| Surfboard-tg-mixed | 0.563 | 0.562 | 16 | 7442 | observe |
| DeltaKronecker-all | 0.314 | 0.333 | 9 | 3849 | observe |
| tg-OutlineReleasedKey | 0.257 | 1.0 | 1 | 53 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4912 | observe |
| Epodonios-all | 0.255 | None | 0 | 7913 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 10415 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5721 | observe |
| barry-far-vless | 0.255 | None | 0 | 5934 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4177 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 47 |
| 204 | TimeoutError | - | 11 |
| cn-block | TimeoutError | - | 9 |
| geo | ClientOSError | - | 7 |
| cn-block | ClientOSError | - | 4 |
| 204 | ProxyError | - | 3 |
| 204 | ClientOSError | - | 3 |
| speed | ClientOSError | - | 3 |
| geo | ProxyError | - | 1 |
| speed | TimeoutError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 105 | 105 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
