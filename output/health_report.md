# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-16 14:56:22 |
| 运行耗时 | 278.6s |
| 订阅源总数 | 107 |
| 健康订阅源 | 93 |
| 原始节点 | 99200 |
| 去重后节点 | 27685 |
| TCP 可达 | 3000 |
| 真实可用 | 421 |
| Verified 输出 | 77 |
| Global 输出 | 300 |
| All 输出 | 27685 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.6 |
| geo | 1.4 |
| tcp | 86.9 |
| probe | 80.4 |
| real_test | 75.7 |
| china_check | 18.2 |
| write_verified | 0.0 |
| generate | 10.5 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 58482 |
| vmess | 16398 |
| shadowsocks | 11979 |
| trojan | 10095 |
| hysteria2 | 1309 |
| http | 662 |
| shadowsocksr | 164 |
| socks | 59 |
| anytls | 29 |
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
| 95.35 | hysteria2 | 238.0 | 1.3 | 22.27 | 14.95 | 10.0 | 13.85 | 15.78 | Au1rxx-base64 | 129.213.91.185 |
| 92.83 | vless | 241.7 | 1.8 | 22.18 | 14.93 | 10.0 | 9.94 | 15.78 | Au1rxx-base64 | 147.45.60.160 |
| 90.32 | vless | 352.6 | 0.4 | 19.62 | 14.98 | 10.0 | 9.94 | 15.78 | Au1rxx-base64 | 185.95.231.156 |
| 89.83 | shadowsocks | 254.6 | 3.9 | 21.89 | 14.86 | 10.0 | 11.3 | 15.78 | Au1rxx-base64 | 37.19.198.244 |
| 89.82 | shadowsocks | 259.3 | 0.9 | 21.77 | 14.97 | 10.0 | 11.3 | 15.78 | Au1rxx-base64 | 37.19.198.160 |
| 89.68 | shadowsocks | 256.4 | 6.3 | 21.84 | 14.76 | 10.0 | 11.3 | 15.78 | Au1rxx-base64 | 37.19.198.236 |
| 88.51 | vless | 366.3 | 24.8 | 19.3 | 14.07 | 9.42 | 9.94 | 15.78 | Au1rxx-base64 | 159.89.87.21 |
| 87.6 | vless | 266.5 | 6.0 | 21.61 | 14.77 | 10.0 | 9.94 | 15.78 | Au1rxx-base64 | 104.243.33.154 |
| 87.6 | vless | 293.1 | 0.7 | 20.99 | 14.97 | 6.16 | 9.94 | 15.78 | Au1rxx-base64 | 66.70.179.198 |
| 87.49 | shadowsocks | 336.3 | 2.2 | 19.99 | 14.92 | 10.0 | 11.3 | 15.78 | Au1rxx-base64 | 51.222.136.236 |
| 87.48 | shadowsocks | 261.0 | 8.9 | 21.74 | 14.66 | 10.0 | 11.3 | 15.78 | Au1rxx-base64 | 37.19.198.243 |
| 87.41 | shadowsocks | 343.6 | 0.0 | 19.83 | 15.0 | 10.0 | 11.3 | 15.78 | Au1rxx-base64 | 15.204.233.41 |
| 87.32 | shadowsocks | 276.9 | 1.0 | 21.37 | 14.96 | 10.0 | 11.3 | 15.78 | Au1rxx-base64 | 156.146.38.170 |
| 87.29 | shadowsocks | 285.8 | 2.5 | 21.16 | 14.91 | 10.0 | 11.3 | 15.78 | Au1rxx-base64 | 156.146.38.167 |
| 87.15 | hysteria2 | 355.5 | 3.0 | 19.55 | 14.89 | 9.71 | 13.85 | 15.78 | Au1rxx-base64 | 62.210.124.146 |
| 86.64 | shadowsocks | 281.6 | 0.9 | 21.26 | 14.97 | 10.0 | 11.3 | 15.78 | Au1rxx-base64 | 156.146.38.169 |
| 85.73 | vless | 315.4 | 2.0 | 20.48 | 14.92 | 9.9 | 9.94 | 15.78 | Au1rxx-base64 | 131.143.180.110 |
| 85.33 | shadowsocks | 285.2 | 1.9 | 21.18 | 14.93 | 10.0 | 11.3 | 15.78 | Au1rxx-base64 | 156.146.38.168 |
| 84.71 | http | 311.9 | 1.5 | 20.56 | 14.94 | 0.0 | 14.03 | 19.18 | ermaozi | 198.44.135.19 |
| 84.65 | http | 339.8 | 2.4 | 19.91 | 14.91 | 0.0 | 14.03 | 19.18 | ermaozi | 121.127.34.82 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.941 | 0.931 | 58 | 618 | prefer |
| Au1rxx-base64 | 0.868 | 0.789 | 446 | 1991 | prefer |
| mheidari-all | 0.625 | 0.55 | 20 | 23974 | observe |
| DeltaKronecker-all | 0.349 | 0.667 | 3 | 4946 | observe |
| Surfboard-tg-mixed | 0.349 | 0.667 | 3 | 7090 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| tg-oneclickvpnkeys | 0.258 | 1.0 | 1 | 79 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5024 | observe |
| Au1rxx-clash | 0.255 | None | 0 | 1991 | observe |
| Epodonios-all | 0.255 | None | 0 | 7568 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 10094 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5572 | observe |
| barry-far-vless | 0.255 | None | 0 | 5822 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 56 |
| speed | ClientOSError | - | 14 |
| 204 | TimeoutError | - | 12 |
| 204 | ProxyError | - | 7 |
| geo | ClientOSError | - | 7 |
| cn-block | ClientOSError | - | 4 |
| 204 | ClientOSError | - | 3 |
| geo | ProxyError | - | 2 |
| cn-block | ProxyError | - | 2 |
| cn-block | TimeoutError | - | 2 |
| cn-block | status | 530 | 1 |
| geo | TimeoutError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 50 | 77 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
