# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-25 16:38:59 |
| 运行耗时 | 309.2s |
| 订阅源总数 | 107 |
| 健康订阅源 | 88 |
| 原始节点 | 98405 |
| 去重后节点 | 27202 |
| TCP 可达 | 3000 |
| 真实可用 | 380 |
| Verified 输出 | 105 |
| Global 输出 | 300 |
| All 输出 | 27202 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.7 |
| geo | 1.5 |
| tcp | 84.2 |
| probe | 99.1 |
| real_test | 80.8 |
| china_check | 21.4 |
| write_verified | 0.1 |
| generate | 14.5 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 58410 |
| vmess | 17512 |
| shadowsocks | 12951 |
| trojan | 7603 |
| hysteria2 | 1407 |
| http | 254 |
| shadowsocksr | 164 |
| socks | 58 |
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
| 94.4 | vless | 279.2 | 0.9 | 21.32 | 14.97 | 9.31 | 10.94 | 17.86 | Au1rxx-base64 | 169.40.42.90 |
| 93.94 | hysteria2 | 223.0 | 0.1 | 22.62 | 15.0 | 5.96 | 14.0 | 17.86 | Au1rxx-base64 | 129.213.91.185 |
| 93.75 | vless | 297.5 | 3.3 | 20.89 | 14.88 | 9.18 | 10.94 | 17.86 | Au1rxx-base64 | 66.70.179.198 |
| 93.52 | vless | 278.1 | 10.4 | 21.34 | 14.61 | 8.77 | 10.94 | 17.86 | Au1rxx-base64 | 195.123.235.183 |
| 93.15 | shadowsocks | 245.5 | 3.6 | 22.09 | 14.87 | 9.24 | 13.09 | 17.86 | Au1rxx-base64 | 37.19.198.244 |
| 92.79 | vless | 344.5 | 1.9 | 19.8 | 14.93 | 9.26 | 10.94 | 17.86 | Au1rxx-base64 | 169.40.42.229 |
| 92.74 | shadowsocks | 249.6 | 5.3 | 22.0 | 14.8 | 8.99 | 13.09 | 17.86 | Au1rxx-base64 | 37.19.198.236 |
| 92.18 | vless | 255.6 | 5.6 | 21.86 | 14.79 | 9.27 | 10.94 | 17.86 | Au1rxx-base64 | 169.40.42.231 |
| 91.87 | vless | 267.8 | 1.4 | 21.58 | 14.95 | 6.54 | 10.94 | 17.86 | Au1rxx-base64 | 195.123.235.177 |
| 91.87 | shadowsocks | 302.3 | 2.6 | 20.78 | 14.9 | 9.24 | 13.09 | 17.86 | Au1rxx-base64 | 37.19.198.160 |
| 91.81 | vless | 366.7 | 3.9 | 19.29 | 14.86 | 8.86 | 10.94 | 17.86 | Au1rxx-base64 | 169.40.42.225 |
| 91.22 | shadowsocks | 316.9 | 0.9 | 20.44 | 14.97 | 9.36 | 13.09 | 17.86 | Au1rxx-base64 | 45.86.51.18 |
| 91.2 | vless | 394.1 | 3.0 | 18.66 | 14.89 | 9.27 | 10.94 | 17.86 | Au1rxx-base64 | 169.40.42.104 |
| 90.3 | vless | 420.9 | 10.1 | 18.03 | 14.62 | 8.85 | 10.94 | 17.86 | Au1rxx-base64 | 169.40.42.224 |
| 90.03 | vless | 380.4 | 2.2 | 18.97 | 14.92 | 9.13 | 10.94 | 17.86 | Au1rxx-base64 | 169.40.42.89 |
| 89.96 | shadowsocks | 361.3 | 0.7 | 19.41 | 14.97 | 9.13 | 13.09 | 17.86 | Au1rxx-base64 | 193.151.163.18 |
| 89.9 | shadowsocks | 287.7 | 1.9 | 21.12 | 14.93 | 8.91 | 13.09 | 17.86 | Au1rxx-base64 | 156.146.38.170 |
| 89.58 | vless | 320.8 | 2.8 | 20.35 | 14.9 | 9.3 | 10.94 | 17.86 | Au1rxx-base64 | 169.40.42.235 |
| 89.58 | vless | 353.1 | 1.8 | 19.6 | 14.93 | 9.14 | 10.94 | 17.86 | Au1rxx-base64 | 169.40.42.168 |
| 89.53 | shadowsocks | 238.7 | 3.1 | 22.25 | 14.88 | 5.95 | 13.09 | 17.86 | Au1rxx-base64 | 185.230.230.18 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.992 | 0.984 | 63 | 575 | prefer |
| Au1rxx-base64 | 0.879 | 0.815 | 297 | 1657 | prefer |
| mheidari-all | 0.805 | 0.737 | 38 | 24301 | prefer |
| Surfboard-tg-mixed | 0.592 | 0.512 | 80 | 7560 | observe |
| ninja-vless | 0.383 | 1.0 | 2 | 1791 | observe |
| xiaoji235-airport-v2ray-all | 0.335 | 1.0 | 1 | 6752 | observe |
| roosterkid-openproxylist-v2ray | 0.317 | 1.0 | 2 | 150 | observe |
| DeltaKronecker-all | 0.298 | 0.273 | 11 | 3849 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4912 | observe |
| Epodonios-all | 0.255 | None | 0 | 7729 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 10761 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5715 | observe |
| barry-far-vless | 0.255 | None | 0 | 5928 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4177 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 74 |
| 204 | TimeoutError | - | 8 |
| geo | ClientOSError | - | 8 |
| 204 | ProxyError | - | 5 |
| 204 | ClientOSError | - | 4 |
| cn-block | TimeoutError | - | 4 |
| cn-block | ClientOSError | - | 3 |
| cn-block | ProxyError | - | 2 |
| geo | TimeoutError | - | 2 |
| speed | ClientOSError | - | 2 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 172 | 105 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
