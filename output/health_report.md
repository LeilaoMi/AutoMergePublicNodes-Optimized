# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-26 05:03:59 |
| 运行耗时 | 317.1s |
| 订阅源总数 | 107 |
| 健康订阅源 | 87 |
| 原始节点 | 98294 |
| 去重后节点 | 27405 |
| TCP 可达 | 3000 |
| 真实可用 | 494 |
| Verified 输出 | 117 |
| Global 输出 | 300 |
| All 输出 | 27405 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.2 |
| geo | 1.7 |
| tcp | 85.4 |
| probe | 91.8 |
| real_test | 90.7 |
| china_check | 26.2 |
| write_verified | 0.1 |
| generate | 14.2 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 58606 |
| vmess | 17251 |
| shadowsocks | 12693 |
| trojan | 7704 |
| hysteria2 | 1360 |
| http | 402 |
| shadowsocksr | 173 |
| socks | 58 |
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
| 96.6 | hysteria2 | 231.5 | 1.8 | 22.42 | 14.93 | 9.44 | 13.85 | 17.46 | Au1rxx-base64 | 129.213.91.185 |
| 94.36 | shadowsocks | 251.5 | 0.3 | 21.96 | 14.99 | 10.0 | 13.95 | 17.46 | Au1rxx-base64 | 37.19.198.244 |
| 94.19 | shadowsocks | 255.2 | 2.4 | 21.87 | 14.91 | 10.0 | 13.95 | 17.46 | Au1rxx-base64 | 37.19.198.243 |
| 93.9 | shadowsocks | 248.4 | 1.0 | 22.03 | 14.96 | 10.0 | 13.95 | 17.46 | Au1rxx-base64 | 185.230.230.18 |
| 93.7 | vless | 269.9 | 2.1 | 21.53 | 14.92 | 9.48 | 10.31 | 17.46 | Au1rxx-base64 | 167.17.69.171 |
| 93.25 | vless | 270.2 | 4.9 | 21.52 | 14.81 | 9.26 | 10.31 | 17.46 | Au1rxx-base64 | 162.35.8.62 |
| 92.86 | vless | 296.8 | 2.2 | 20.91 | 14.92 | 9.29 | 10.31 | 17.46 | Au1rxx-base64 | 66.70.179.198 |
| 92.73 | shadowsocks | 300.5 | 0.0 | 20.82 | 15.0 | 10.0 | 13.95 | 17.46 | Au1rxx-base64 | 45.86.51.18 |
| 92.48 | shadowsocks | 310.1 | 0.9 | 20.6 | 14.97 | 10.0 | 13.95 | 17.46 | Au1rxx-base64 | 15.204.246.132 |
| 92.47 | vless | 234.5 | 5.2 | 22.35 | 14.8 | 7.55 | 10.31 | 17.46 | Au1rxx-base64 | 195.123.235.183 |
| 91.65 | shadowsocks | 275.3 | 0.5 | 21.4 | 14.98 | 9.98 | 13.95 | 17.46 | Au1rxx-base64 | 156.146.38.169 |
| 91.33 | shadowsocks | 282.4 | 4.1 | 21.24 | 14.84 | 10.0 | 13.95 | 17.46 | Au1rxx-base64 | 156.146.38.170 |
| 91.17 | vless | 386.8 | 0.6 | 18.82 | 14.98 | 9.6 | 10.31 | 17.46 | Au1rxx-base64 | 169.40.42.202 |
| 91.02 | vless | 385.1 | 2.5 | 18.86 | 14.91 | 9.48 | 10.31 | 17.46 | Au1rxx-base64 | 169.40.42.225 |
| 90.42 | shadowsocks | 380.5 | 12.3 | 18.97 | 14.54 | 10.0 | 13.95 | 17.46 | Au1rxx-base64 | 193.151.163.18 |
| 90.38 | vless | 388.1 | 1.9 | 18.79 | 14.93 | 9.6 | 10.31 | 17.46 | Au1rxx-base64 | 169.40.42.168 |
| 90.14 | shadowsocks | 282.5 | 0.2 | 21.24 | 14.99 | 10.0 | 13.95 | 17.46 | Au1rxx-base64 | 156.146.38.168 |
| 89.57 | vless | 236.5 | 0.2 | 22.3 | 14.99 | 4.51 | 10.31 | 17.46 | Au1rxx-base64 | 195.123.235.177 |
| 89.31 | vless | 373.1 | 3.8 | 19.14 | 14.86 | 7.54 | 10.31 | 17.46 | Au1rxx-base64 | 169.40.42.229 |
| 89.12 | shadowsocks | 287.7 | 1.1 | 21.12 | 14.96 | 10.0 | 13.95 | 17.46 | Au1rxx-base64 | 193.151.160.9 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.998 | 0.981 | 105 | 643 | prefer |
| Au1rxx-base64 | 0.872 | 0.807 | 362 | 1674 | prefer |
| mheidari-all | 0.606 | 0.526 | 152 | 24290 | observe |
| Surfboard-tg-mixed | 0.57 | 0.727 | 11 | 7351 | observe |
| DeltaKronecker-all | 0.455 | 0.364 | 22 | 3849 | observe |
| roosterkid-openproxylist-v2ray | 0.364 | 1.0 | 3 | 150 | observe |
| ninja-vless | 0.327 | 1.0 | 1 | 1791 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4912 | observe |
| Epodonios-all | 0.255 | None | 0 | 7848 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 10571 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5665 | observe |
| barry-far-vless | 0.255 | None | 0 | 5884 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4228 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 85 |
| speed | ClientOSError | - | 27 |
| geo | ClientOSError | - | 20 |
| cn-block | TimeoutError | - | 9 |
| cn-block | ClientOSError | - | 5 |
| 204 | ProxyError | - | 4 |
| geo | ProxyError | - | 3 |
| 204 | TimeoutError | - | 3 |
| 204 | ClientOSError | - | 3 |
| cn-block | ProxyError | - | 1 |
| speed | TimeoutError | - | 1 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 105 | 117 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
