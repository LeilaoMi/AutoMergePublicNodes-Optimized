# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-26 13:23:23 |
| 运行耗时 | 318.3s |
| 订阅源总数 | 107 |
| 健康订阅源 | 88 |
| 原始节点 | 96713 |
| 去重后节点 | 26589 |
| TCP 可达 | 3000 |
| 真实可用 | 469 |
| Verified 输出 | 128 |
| Global 输出 | 300 |
| All 输出 | 26589 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.8 |
| geo | 1.7 |
| tcp | 82.4 |
| probe | 90.3 |
| real_test | 88.7 |
| china_check | 35.7 |
| write_verified | 0.1 |
| generate | 12.6 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 57839 |
| vmess | 17497 |
| shadowsocks | 12658 |
| trojan | 6685 |
| hysteria2 | 1393 |
| http | 367 |
| shadowsocksr | 168 |
| socks | 59 |
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
| 94.26 | shadowsocks | 231.8 | 3.6 | 22.41 | 14.86 | 9.79 | 13.76 | 17.44 | Au1rxx-base64 | 156.146.38.170 |
| 94.21 | shadowsocks | 223.8 | 0.1 | 22.6 | 15.0 | 9.41 | 13.76 | 17.44 | Au1rxx-base64 | 156.146.38.169 |
| 93.6 | shadowsocks | 231.2 | 0.8 | 22.43 | 14.97 | 10.0 | 13.76 | 17.44 | Au1rxx-base64 | 156.146.38.168 |
| 92.29 | vless | 244.9 | 18.0 | 22.11 | 14.33 | 9.36 | 9.05 | 17.44 | Au1rxx-base64 | 162.35.8.62 |
| 91.52 | trojan | 308.0 | 8.4 | 20.65 | 14.68 | 8.29 | 13.46 | 17.44 | Au1rxx-base64 | 66.23.203.21 |
| 90.91 | shadowsocks | 268.6 | 0.0 | 21.56 | 15.0 | 9.19 | 13.76 | 17.44 | Au1rxx-base64 | 173.244.56.6 |
| 90.37 | vless | 249.4 | 14.4 | 22.0 | 14.46 | 9.16 | 9.05 | 17.44 | Au1rxx-base64 | 45.63.53.81 |
| 89.7 | shadowsocks | 291.7 | 1.6 | 21.03 | 14.94 | 10.0 | 13.76 | 17.44 | Au1rxx-base64 | 95.215.201.18 |
| 89.48 | shadowsocks | 227.7 | 0.2 | 22.51 | 14.99 | 6.78 | 13.76 | 17.44 | Au1rxx-base64 | 156.146.38.167 |
| 89.29 | shadowsocks | 309.6 | 0.5 | 20.61 | 14.98 | 9.51 | 13.76 | 17.44 | Au1rxx-base64 | 37.19.198.160 |
| 89.23 | vless | 307.9 | 15.2 | 20.65 | 14.43 | 9.36 | 9.05 | 17.44 | Au1rxx-base64 | 45.76.172.197 |
| 89.08 | shadowsocks | 317.8 | 1.5 | 20.42 | 14.95 | 9.16 | 13.76 | 17.44 | Au1rxx-base64 | 185.230.230.18 |
| 88.76 | shadowsocks | 306.4 | 1.3 | 20.68 | 14.95 | 8.66 | 13.76 | 17.44 | Au1rxx-base64 | 193.151.160.9 |
| 87.7 | shadowsocks | 320.1 | 10.9 | 20.37 | 14.59 | 8.5 | 13.76 | 17.44 | Au1rxx-base64 | 37.19.198.243 |
| 87.48 | shadowsocks | 288.6 | 44.6 | 21.1 | 13.33 | 10.0 | 13.76 | 17.44 | Au1rxx-base64 | 173.244.56.9 |
| 86.84 | hysteria2 | 280.7 | 11.8 | 21.28 | 14.56 | 3.86 | 13.93 | 17.44 | Au1rxx-base64 | 66.94.121.46 |
| 86.72 | vless | 304.8 | 16.2 | 20.72 | 14.39 | 9.05 | 9.05 | 17.44 | Au1rxx-base64 | 172.236.227.60 |
| 86.7 | shadowsocks | 383.2 | 50.3 | 18.91 | 13.11 | 10.0 | 13.76 | 17.44 | Au1rxx-base64 | 45.86.51.18 |
| 86.33 | shadowsocks | 318.6 | 1.1 | 20.4 | 14.96 | 6.34 | 13.76 | 17.44 | Au1rxx-base64 | 37.19.198.236 |
| 86.01 | shadowsocks | 311.7 | 1.3 | 20.56 | 14.95 | 6.18 | 13.76 | 17.44 | Au1rxx-base64 | 193.151.160.18 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.988 | 0.971 | 105 | 643 | prefer |
| Au1rxx-base64 | 0.846 | 0.78 | 354 | 1689 | prefer |
| Surfboard-tg-mixed | 0.812 | 0.741 | 54 | 7197 | prefer |
| mheidari-all | 0.74 | 0.667 | 51 | 24314 | prefer |
| DeltaKronecker-all | 0.482 | 0.5 | 14 | 3004 | observe |
| roosterkid-openproxylist-v2ray | 0.445 | 1.0 | 5 | 150 | observe |
| zhangkai | 0.36 | 1.0 | 3 | 43 | observe |
| SoliSpirit-all | 0.335 | 1.0 | 1 | 10312 | observe |
| chromego_merge | 0.265 | 1.0 | 1 | 252 | observe |
| tg-LonUp_M | 0.262 | 1.0 | 1 | 177 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4919 | observe |
| Epodonios-all | 0.255 | None | 0 | 7666 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5522 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4228 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 60 |
| speed | ClientOSError | - | 14 |
| geo | ClientOSError | - | 14 |
| 204 | TimeoutError | - | 10 |
| cn-block | TimeoutError | - | 10 |
| 204 | ProxyError | - | 6 |
| cn-block | ClientOSError | - | 5 |
| 204 | ClientOSError | - | 3 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 117 | 128 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
