# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-23 05:07:32 |
| 运行耗时 | 278.3s |
| 订阅源总数 | 107 |
| 健康订阅源 | 92 |
| 原始节点 | 96386 |
| 去重后节点 | 26819 |
| TCP 可达 | 3000 |
| 真实可用 | 429 |
| Verified 输出 | 175 |
| Global 输出 | 300 |
| All 输出 | 26819 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.2 |
| geo | 1.6 |
| tcp | 82.2 |
| probe | 68.2 |
| real_test | 82.8 |
| china_check | 30.6 |
| write_verified | 0.1 |
| generate | 8.9 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 57182 |
| vmess | 17156 |
| shadowsocks | 12298 |
| trojan | 7869 |
| hysteria2 | 1340 |
| http | 338 |
| shadowsocksr | 96 |
| socks | 59 |
| anytls | 25 |
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
| 95.55 | shadowsocks | 197.2 | 0.4 | 23.21 | 14.99 | 10.0 | 14.17 | 17.68 | Au1rxx-base64 | 95.215.201.18 |
| 95.15 | vless | 222.6 | 8.8 | 22.62 | 14.67 | 10.0 | 10.18 | 17.68 | Au1rxx-base64 | 144.202.126.147 |
| 95.01 | vless | 230.7 | 7.8 | 22.44 | 14.71 | 10.0 | 10.18 | 17.68 | Au1rxx-base64 | 45.63.53.81 |
| 94.88 | hysteria2 | 259.3 | 12.2 | 21.78 | 14.54 | 10.0 | 13.12 | 17.68 | Au1rxx-base64 | 66.94.121.46 |
| 94.69 | vless | 207.1 | 0.4 | 22.98 | 14.99 | 8.86 | 10.18 | 17.68 | Au1rxx-base64 | 172.236.227.60 |
| 94.62 | shadowsocks | 259.3 | 0.2 | 21.78 | 14.99 | 10.0 | 14.17 | 17.68 | Au1rxx-base64 | 156.146.38.170 |
| 92.6 | shadowsocks | 257.6 | 0.7 | 21.81 | 14.97 | 10.0 | 14.17 | 17.68 | Au1rxx-base64 | 156.146.38.167 |
| 92.28 | vless | 216.6 | 10.1 | 22.76 | 14.62 | 7.04 | 10.18 | 17.68 | Au1rxx-base64 | 154.12.38.202 |
| 92.03 | hysteria2 | 315.1 | 0.5 | 20.48 | 14.98 | 9.85 | 13.12 | 17.68 | Au1rxx-base64 | 129.213.91.185 |
| 91.57 | trojan | 276.6 | 1.6 | 21.37 | 14.94 | 9.53 | 14.59 | 17.68 | Au1rxx-base64 | 216.106.186.32 |
| 90.62 | vless | 295.3 | 1.5 | 20.94 | 14.95 | 10.0 | 10.18 | 17.68 | Au1rxx-base64 | 44.248.233.99 |
| 90.54 | vless | 264.5 | 5.0 | 21.66 | 14.81 | 6.21 | 10.18 | 17.68 | Au1rxx-base64 | 154.12.38.159 |
| 90.08 | vless | 194.1 | 3.2 | 23.28 | 14.88 | 6.8 | 10.18 | 17.68 | Au1rxx-base64 | 216.167.126.97 |
| 89.44 | shadowsocks | 278.9 | 3.1 | 21.32 | 14.88 | 10.0 | 14.17 | 17.68 | Au1rxx-base64 | 173.244.56.9 |
| 88.8 | shadowsocks | 387.8 | 0.9 | 18.8 | 14.97 | 10.0 | 14.17 | 17.68 | Au1rxx-base64 | 185.215.132.9 |
| 88.44 | shadowsocks | 343.1 | 2.5 | 19.84 | 14.91 | 9.93 | 14.17 | 17.68 | Au1rxx-base64 | 149.22.95.183 |
| 87.44 | shadowsocks | 347.3 | 0.8 | 19.74 | 14.97 | 9.83 | 14.17 | 17.68 | Au1rxx-base64 | 37.19.198.160 |
| 87.44 | shadowsocks | 365.3 | 0.5 | 19.32 | 14.98 | 10.0 | 14.17 | 17.68 | Au1rxx-base64 | 37.19.198.236 |
| 87.15 | shadowsocks | 383.6 | 0.1 | 18.9 | 15.0 | 10.0 | 14.17 | 17.68 | Au1rxx-base64 | 185.230.230.18 |
| 86.69 | shadowsocks | 409.8 | 1.0 | 18.29 | 14.96 | 10.0 | 14.17 | 17.68 | Au1rxx-base64 | 193.151.160.9 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.986 | 0.971 | 103 | 609 | prefer |
| Au1rxx-base64 | 0.878 | 0.819 | 259 | 1536 | prefer |
| Surfboard-tg-mixed | 0.749 | 0.923 | 13 | 6999 | prefer |
| mheidari-all | 0.621 | 0.541 | 183 | 23958 | observe |
| ninja-vless | 0.383 | 1.0 | 2 | 1791 | observe |
| DeltaKronecker-all | 0.37 | 0.312 | 16 | 3641 | observe |
| SoliSpirit-all | 0.335 | 1.0 | 1 | 10110 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5015 | observe |
| Epodonios-all | 0.255 | None | 0 | 7509 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5447 | observe |
| barry-far-vless | 0.255 | None | 0 | 5666 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4230 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |
| Au1rxx-clash | 0.236 | None | 0 | 1536 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 88 |
| speed | ClientOSError | - | 21 |
| geo | ClientOSError | - | 18 |
| cn-block | ClientOSError | - | 5 |
| 204 | ProxyError | - | 4 |
| cn-block | ProxyError | - | 3 |
| 204 | TimeoutError | - | 3 |
| geo | ProxyError | - | 2 |
| geo | TimeoutError | - | 2 |
| 204 | ClientOSError | - | 1 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 113 | 175 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
