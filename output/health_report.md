# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-26 22:51:08 |
| 运行耗时 | 300.2s |
| 订阅源总数 | 107 |
| 健康订阅源 | 88 |
| 原始节点 | 96962 |
| 去重后节点 | 26586 |
| TCP 可达 | 3000 |
| 真实可用 | 446 |
| Verified 输出 | 96 |
| Global 输出 | 300 |
| All 输出 | 26586 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.3 |
| geo | 1.5 |
| tcp | 84.0 |
| probe | 74.7 |
| real_test | 91.3 |
| china_check | 36.1 |
| write_verified | 0.0 |
| generate | 8.4 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 57301 |
| vmess | 17662 |
| shadowsocks | 12670 |
| trojan | 7517 |
| hysteria2 | 1397 |
| shadowsocksr | 169 |
| http | 142 |
| socks | 56 |
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
| 92.15 | vless | 232.1 | 1.0 | 22.41 | 14.96 | 8.13 | 9.73 | 16.92 | Au1rxx-base64 | 162.35.8.62 |
| 91.82 | shadowsocks | 256.6 | 0.1 | 21.84 | 15.0 | 8.77 | 13.29 | 16.92 | Au1rxx-base64 | 156.146.38.170 |
| 91.38 | shadowsocks | 226.6 | 1.6 | 22.53 | 14.94 | 8.7 | 13.29 | 16.92 | Au1rxx-base64 | 156.146.38.167 |
| 90.96 | shadowsocks | 218.0 | 1.6 | 22.73 | 14.94 | 7.08 | 13.29 | 16.92 | Au1rxx-base64 | 156.146.38.169 |
| 90.11 | hysteria2 | 278.9 | 15.9 | 21.32 | 14.4 | 7.56 | 13.42 | 16.92 | Au1rxx-base64 | 66.94.121.46 |
| 87.98 | trojan | 319.4 | 0.8 | 20.39 | 14.97 | 7.03 | 11.67 | 16.92 | Au1rxx-base64 | 66.23.203.21 |
| 87.04 | shadowsocks | 316.4 | 0.4 | 20.45 | 14.98 | 8.43 | 13.29 | 16.92 | Au1rxx-base64 | 37.19.198.160 |
| 85.77 | vless | 318.0 | 3.3 | 20.42 | 14.88 | 6.71 | 9.73 | 16.92 | Au1rxx-base64 | 45.63.53.81 |
| 85.77 | shadowsocks | 343.7 | 0.4 | 19.82 | 14.98 | 6.82 | 13.29 | 16.92 | Au1rxx-base64 | 95.215.201.18 |
| 85.6 | shadowsocks | 401.9 | 1.2 | 18.47 | 14.96 | 8.39 | 13.29 | 16.92 | Au1rxx-base64 | 45.86.51.18 |
| 85.58 | vless | 259.2 | 1.6 | 21.78 | 14.94 | 7.22 | 9.73 | 16.92 | Au1rxx-base64 | 144.202.126.147 |
| 85.54 | shadowsocks | 309.9 | 5.6 | 20.6 | 14.79 | 6.82 | 13.29 | 16.92 | Au1rxx-base64 | 193.151.160.18 |
| 85.46 | shadowsocks | 377.2 | 3.5 | 19.05 | 14.87 | 8.47 | 13.29 | 16.92 | Au1rxx-base64 | 193.151.160.9 |
| 85.36 | vless | 268.8 | 17.2 | 21.56 | 14.36 | 7.15 | 9.73 | 16.92 | Au1rxx-base64 | 216.167.126.97 |
| 85.32 | vless | 265.6 | 2.3 | 21.63 | 14.91 | 6.14 | 9.73 | 16.92 | Au1rxx-base64 | 47.251.108.158 |
| 85.23 | shadowsocks | 316.5 | 1.4 | 20.45 | 14.95 | 6.77 | 13.29 | 16.92 | Au1rxx-base64 | 185.230.230.18 |
| 84.83 | vless | 312.3 | 0.5 | 20.55 | 14.98 | 6.92 | 9.73 | 16.92 | Au1rxx-base64 | 195.123.235.183 |
| 84.74 | http | 351.0 | 2.2 | 19.65 | 14.92 | 0.0 | 14.58 | 19.76 | ermaozi | 198.44.138.27 |
| 84.68 | vless | 322.6 | 3.4 | 20.31 | 14.87 | 7.91 | 9.73 | 16.92 | Au1rxx-base64 | 44.248.233.99 |
| 84.49 | vless | 281.8 | 1.2 | 21.26 | 14.96 | 6.78 | 9.73 | 16.92 | Au1rxx-base64 | 195.123.240.65 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.996 | 1.0 | 35 | 564 | prefer |
| Surfboard-tg-mixed | 0.826 | 0.75 | 128 | 7052 | prefer |
| Au1rxx-base64 | 0.767 | 0.699 | 395 | 1735 | prefer |
| mheidari-all | 0.761 | 0.689 | 45 | 24769 | prefer |
| DeltaKronecker-all | 0.372 | 0.444 | 9 | 3004 | observe |
| ninja-vless | 0.327 | 1.0 | 1 | 1791 | observe |
| roosterkid-openproxylist-v2ray | 0.317 | 1.0 | 2 | 150 | observe |
| SoliSpirit-all | 0.287 | 0.5 | 2 | 10741 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4919 | observe |
| Epodonios-all | 0.255 | None | 0 | 7537 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5366 | observe |
| barry-far-vless | 0.255 | None | 0 | 5651 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4466 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 68 |
| speed | ClientOSError | - | 41 |
| geo | ClientOSError | - | 33 |
| cn-block | TimeoutError | - | 13 |
| cn-block | ClientOSError | - | 6 |
| 204 | ProxyError | - | 5 |
| cn-block | ProxyError | - | 1 |
| 204 | TimeoutError | - | 1 |
| geo | TimeoutError | - | 1 |
| speed | TimeoutError | - | 1 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 128 | 96 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
