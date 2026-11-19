# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-11-19 20:53:07 |
| 运行耗时 | 293.8s |
| 订阅源总数 | 107 |
| 健康订阅源 | 88 |
| 原始节点 | 83175 |
| 去重后节点 | 27828 |
| TCP 可达 | 3000 |
| 真实可用 | 416 |
| Verified 输出 | 65 |
| Global 输出 | 300 |
| All 输出 | 27828 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.9 |
| geo | 1.4 |
| tcp | 83.6 |
| probe | 76.9 |
| real_test | 80.0 |
| china_check | 35.9 |
| generate | 11.0 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 49429 |
| vmess | 14877 |
| shadowsocks | 10161 |
| trojan | 6827 |
| hysteria2 | 1486 |
| shadowsocksr | 152 |
| http | 128 |
| socks | 70 |
| hysteria | 22 |
| tuic | 12 |
| anytls | 11 |

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
| 88.73 | vless | 347.9 | 0.2 | 19.72 | 14.99 | 8.94 | 9.78 | 15.3 | Au1rxx-base64 | 169.40.42.202 |
| 88.71 | shadowsocks | 257.8 | 2.5 | 21.81 | 14.91 | 10.0 | 13.33 | 15.3 | Au1rxx-base64 | 37.19.198.236 |
| 88.68 | shadowsocks | 348.7 | 4.3 | 19.71 | 14.84 | 10.0 | 13.33 | 15.3 | Au1rxx-base64 | 193.151.160.9 |
| 87.94 | http | 280.0 | 0.1 | 21.3 | 15.0 | 0.0 | 14.44 | 19.7 | ermaozi | 172.64.69.89 |
| 87.78 | shadowsocks | 319.5 | 6.0 | 20.38 | 14.77 | 10.0 | 13.33 | 15.3 | Au1rxx-base64 | 37.19.198.243 |
| 87.2 | shadowsocks | 249.5 | 0.8 | 22.0 | 14.97 | 10.0 | 13.33 | 15.3 | Au1rxx-base64 | 37.19.198.244 |
| 87.15 | shadowsocks | 405.0 | 10.3 | 18.4 | 14.62 | 10.0 | 13.33 | 15.3 | Au1rxx-base64 | 45.86.51.18 |
| 86.94 | shadowsocks | 265.5 | 1.6 | 21.63 | 14.94 | 10.0 | 13.33 | 15.3 | Au1rxx-base64 | 193.151.163.18 |
| 86.88 | shadowsocks | 312.8 | 4.5 | 20.54 | 14.83 | 8.23 | 13.33 | 15.3 | Au1rxx-base64 | 193.151.160.18 |
| 86.74 | shadowsocks | 318.8 | 7.7 | 20.4 | 14.71 | 10.0 | 13.33 | 15.3 | Au1rxx-base64 | 37.19.198.160 |
| 86.42 | shadowsocks | 449.5 | 2.0 | 17.37 | 14.92 | 10.0 | 13.33 | 15.3 | Au1rxx-base64 | 15.204.247.206 |
| 85.75 | http | 374.3 | 0.1 | 19.11 | 15.0 | 0.0 | 14.44 | 19.7 | ermaozi | 172.64.68.89 |
| 85.04 | vless | 367.8 | 0.3 | 19.26 | 14.99 | 10.0 | 9.78 | 15.3 | Au1rxx-base64 | 169.40.42.35 |
| 85.02 | vless | 267.0 | 2.7 | 21.6 | 14.9 | 0.0 | 9.78 | 18.74 | Surfboard-tg-mixed | 45.144.112.55 |
| 84.85 | shadowsocks | 312.2 | 2.2 | 20.55 | 14.92 | 10.0 | 13.33 | 15.3 | Au1rxx-base64 | 95.215.201.18 |
| 84.83 | vless | 330.2 | 1.0 | 20.13 | 14.96 | 9.16 | 9.78 | 15.3 | Au1rxx-base64 | 45.138.100.248 |
| 83.08 | http | 322.0 | 5.2 | 20.32 | 14.81 | 0.0 | 14.44 | 19.7 | ermaozi | 149.88.21.129 |
| 82.77 | shadowsocks | 311.8 | 9.7 | 20.56 | 14.64 | 0.0 | 13.33 | 18.74 | Surfboard-tg-mixed | 169.197.140.247 |
| 82.68 | shadowsocks | 329.8 | 0.8 | 20.14 | 14.97 | 0.0 | 13.33 | 18.74 | Surfboard-tg-mixed | 15.204.247.244 |
| 82.49 | vless | 415.2 | 0.5 | 18.17 | 14.98 | 8.99 | 9.78 | 15.3 | Au1rxx-base64 | 169.40.42.90 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.981 | 1.0 | 24 | 491 | prefer |
| mheidari-all | 0.928 | 0.857 | 77 | 14706 | prefer |
| Surfboard-tg-mixed | 0.857 | 0.779 | 272 | 8602 | prefer |
| Au1rxx-base64 | 0.784 | 0.717 | 145 | 1751 | prefer |
| roosterkid-openproxylist-v2ray | 0.55 | 0.818 | 11 | 150 | observe |
| tg-LonUp_M | 0.407 | 1.0 | 4 | 179 | observe |
| DeltaKronecker-all | 0.335 | 1.0 | 1 | 2728 | observe |
| mahdibland-V2RayAggregator | 0.287 | 0.5 | 2 | 4507 | observe |
| xiaoji235-airport-v2ray-all | 0.287 | 0.5 | 2 | 6752 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4935 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 12076 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5937 | observe |
| barry-far-vless | 0.255 | None | 0 | 5868 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 56 |
| 204 | ProxyError | - | 34 |
| 204 | TimeoutError | - | 8 |
| cn-block | ClientOSError | - | 5 |
| cn-block | TimeoutError | - | 4 |
| cn-block | ProxyError | - | 2 |
| speed | ProxyError | - | 2 |
| geo | ProxyError | - | 2 |
| 204 | ClientOSError | - | 1 |
| speed | ClientOSError | - | 1 |
| geo | TimeoutError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | True | 65 | 29 | 0.5 |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
