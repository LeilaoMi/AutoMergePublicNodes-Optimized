# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-11-07 13:21:20 |
| 运行耗时 | 258.8s |
| 订阅源总数 | 107 |
| 健康订阅源 | 86 |
| 原始节点 | 82306 |
| 去重后节点 | 26976 |
| TCP 可达 | 3000 |
| 真实可用 | 343 |
| Verified 输出 | 68 |
| Global 输出 | 300 |
| All 输出 | 26976 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.9 |
| geo | 1.4 |
| tcp | 78.2 |
| probe | 79.7 |
| real_test | 64.0 |
| china_check | 20.1 |
| generate | 10.6 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 49239 |
| vmess | 14173 |
| shadowsocks | 9318 |
| trojan | 7629 |
| hysteria2 | 1531 |
| shadowsocksr | 151 |
| http | 132 |
| socks | 75 |
| anytls | 22 |
| hysteria | 21 |
| tuic | 15 |

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
| 96.56 | shadowsocks | 229.6 | 2.2 | 22.46 | 14.92 | 10.0 | 14.52 | 18.66 | Au1rxx-base64 | 37.19.198.236 |
| 96.35 | shadowsocks | 237.8 | 2.6 | 22.27 | 14.9 | 10.0 | 14.52 | 18.66 | Au1rxx-base64 | 37.19.198.160 |
| 95.78 | shadowsocks | 237.4 | 4.8 | 22.28 | 14.82 | 10.0 | 14.52 | 18.66 | Au1rxx-base64 | 45.86.51.18 |
| 95.51 | shadowsocks | 250.8 | 3.8 | 21.97 | 14.86 | 10.0 | 14.52 | 18.66 | Au1rxx-base64 | 185.230.230.18 |
| 94.91 | shadowsocks | 273.3 | 5.9 | 21.45 | 14.78 | 10.0 | 14.52 | 18.66 | Au1rxx-base64 | 193.151.163.18 |
| 94.91 | shadowsocks | 293.3 | 7.0 | 20.99 | 14.74 | 10.0 | 14.52 | 18.66 | Au1rxx-base64 | 37.19.198.244 |
| 94.22 | shadowsocks | 309.6 | 2.0 | 20.61 | 14.93 | 10.0 | 14.52 | 18.66 | Au1rxx-base64 | 193.151.160.9 |
| 93.55 | shadowsocks | 292.3 | 0.4 | 21.01 | 14.99 | 8.87 | 14.52 | 18.66 | Au1rxx-base64 | 193.151.160.18 |
| 93.36 | shadowsocks | 283.3 | 5.3 | 21.22 | 14.8 | 10.0 | 14.52 | 18.66 | Au1rxx-base64 | 156.146.38.168 |
| 92.63 | shadowsocks | 286.0 | 5.9 | 21.16 | 14.78 | 10.0 | 14.52 | 18.66 | Au1rxx-base64 | 156.146.38.167 |
| 92.21 | vless | 350.8 | 6.0 | 19.66 | 14.77 | 10.0 | 9.12 | 18.66 | Au1rxx-base64 | 169.40.42.74 |
| 91.98 | vless | 339.3 | 19.3 | 19.92 | 14.28 | 10.0 | 9.12 | 18.66 | Au1rxx-base64 | 169.40.42.35 |
| 91.65 | vless | 293.2 | 0.9 | 20.99 | 14.97 | 7.91 | 9.12 | 18.66 | Au1rxx-base64 | 2.24.124.64 |
| 91.63 | trojan | 273.9 | 1.8 | 21.44 | 14.93 | 8.25 | 13.85 | 18.66 | Au1rxx-base64 | 216.152.156.65 |
| 91.53 | trojan | 310.8 | 6.1 | 20.58 | 14.77 | 8.17 | 13.85 | 18.66 | Au1rxx-base64 | 170.101.101.67 |
| 91.23 | vless | 336.0 | 30.3 | 20.0 | 13.86 | 9.59 | 9.12 | 18.66 | Au1rxx-base64 | 159.89.87.21 |
| 90.63 | vless | 344.9 | 12.0 | 19.79 | 14.55 | 9.51 | 9.12 | 18.66 | Au1rxx-base64 | 66.70.179.198 |
| 90.35 | trojan | 490.0 | 15.9 | 16.44 | 14.4 | 10.0 | 13.85 | 18.66 | Au1rxx-base64 | 69.164.240.85 |
| 89.98 | vless | 422.2 | 10.6 | 18.0 | 14.6 | 9.6 | 9.12 | 18.66 | Au1rxx-base64 | 169.40.42.89 |
| 89.69 | shadowsocks | 281.1 | 0.1 | 21.27 | 14.99 | 6.74 | 14.52 | 18.66 | Au1rxx-base64 | 156.146.38.169 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.896 | 0.947 | 19 | 515 | prefer |
| Au1rxx-base64 | 0.873 | 0.806 | 237 | 1751 | prefer |
| mheidari-all | 0.833 | 0.757 | 152 | 14331 | prefer |
| DeltaKronecker-all | 0.646 | 0.769 | 13 | 2734 | observe |
| Surfboard-tg-mixed | 0.465 | 0.714 | 7 | 8637 | observe |
| xiaoji235-airport-v2ray-all | 0.438 | 1.0 | 3 | 6752 | observe |
| ermaozi-get_subscribe | 0.326 | 1.0 | 2 | 366 | observe |
| tg-LonUp_M | 0.262 | 1.0 | 1 | 176 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4866 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 11009 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 6148 | observe |
| barry-far-vless | 0.255 | None | 0 | 6359 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4522 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 46 |
| 204 | ProxyError | - | 22 |
| 204 | TimeoutError | - | 10 |
| cn-block | TimeoutError | - | 4 |
| cn-block | ClientOSError | - | 2 |
| cn-block | ProxyError | - | 2 |
| 204 | ServerDisconnectedError | - | 1 |
| geo | ProxyError | - | 1 |
| 204 | ClientOSError | - | 1 |
| geo | TimeoutError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | True | 68 | 32 | 0.5 |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
