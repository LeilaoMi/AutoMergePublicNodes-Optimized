# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-11-18 07:47:01 |
| 运行耗时 | 288.9s |
| 订阅源总数 | 107 |
| 健康订阅源 | 87 |
| 原始节点 | 81549 |
| 去重后节点 | 27516 |
| TCP 可达 | 3000 |
| 真实可用 | 424 |
| Verified 输出 | 45 |
| Global 输出 | 300 |
| All 输出 | 27516 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.8 |
| geo | 1.5 |
| tcp | 81.5 |
| probe | 87.3 |
| real_test | 70.9 |
| china_check | 29.7 |
| write_verified | 0.0 |
| generate | 12.2 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 48443 |
| vmess | 14818 |
| shadowsocks | 9643 |
| trojan | 6783 |
| hysteria2 | 1451 |
| shadowsocksr | 155 |
| http | 134 |
| socks | 82 |
| hysteria | 16 |
| tuic | 13 |
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
| 92.46 | shadowsocks | 235.0 | 2.8 | 22.34 | 14.9 | 10.0 | 13.74 | 15.48 | Au1rxx-base64 | 156.146.38.170 |
| 91.95 | shadowsocks | 260.7 | 0.2 | 21.74 | 14.99 | 10.0 | 13.74 | 15.48 | Au1rxx-base64 | 156.146.38.167 |
| 90.13 | shadowsocks | 273.6 | 1.7 | 21.44 | 14.94 | 10.0 | 13.74 | 15.48 | Au1rxx-base64 | 156.146.38.168 |
| 88.23 | shadowsocks | 286.2 | 1.8 | 21.15 | 14.93 | 10.0 | 13.74 | 15.48 | Au1rxx-base64 | 95.215.201.18 |
| 88.03 | http | 255.2 | 6.9 | 21.87 | 14.74 | 0.0 | 14.38 | 19.54 | ermaozi | 38.247.141.135 |
| 87.76 | shadowsocks | 316.5 | 1.2 | 20.45 | 14.95 | 10.0 | 13.74 | 15.48 | Au1rxx-base64 | 185.230.230.18 |
| 87.73 | shadowsocks | 315.9 | 0.8 | 20.47 | 14.97 | 10.0 | 13.74 | 15.48 | Au1rxx-base64 | 193.151.160.9 |
| 86.46 | vless | 282.4 | 6.7 | 21.24 | 14.75 | 7.34 | 9.29 | 15.48 | Au1rxx-base64 | 45.63.53.81 |
| 86.19 | shadowsocks | 305.6 | 4.2 | 20.7 | 14.84 | 8.84 | 13.74 | 15.48 | Au1rxx-base64 | 193.151.160.18 |
| 85.98 | shadowsocks | 319.7 | 1.7 | 20.38 | 14.94 | 10.0 | 13.74 | 15.48 | Au1rxx-base64 | 193.151.163.18 |
| 84.85 | trojan | 296.8 | 2.1 | 20.91 | 14.92 | 10.0 | 9.33 | 15.48 | Au1rxx-base64 | 66.163.112.121 |
| 84.64 | shadowsocks | 414.7 | 1.2 | 18.18 | 14.95 | 6.29 | 13.74 | 15.48 | Au1rxx-base64 | 156.146.38.169 |
| 84.63 | trojan | 419.5 | 6.5 | 18.07 | 14.75 | 10.0 | 9.33 | 15.48 | Au1rxx-base64 | 66.23.203.21 |
| 84.06 | trojan | 301.8 | 0.6 | 20.79 | 14.98 | 8.82 | 9.33 | 15.48 | Au1rxx-base64 | 66.163.112.242 |
| 83.89 | shadowsocks | 307.6 | 2.1 | 20.66 | 14.92 | 10.0 | 13.74 | 15.48 | Au1rxx-base64 | 45.86.51.18 |
| 83.42 | hysteria2 | 376.4 | 7.6 | 19.07 | 14.72 | 0.0 | 12.5 | 18.54 | mheidari-all | 34.24.25.1 |
| 82.64 | shadowsocks | 481.7 | 2.7 | 16.63 | 14.9 | 10.0 | 13.74 | 15.48 | Au1rxx-base64 | 15.204.247.206 |
| 82.6 | shadowsocks | 224.2 | 0.8 | 22.59 | 14.97 | 0.0 | 13.74 | 17.0 | Surfboard-tg-mixed | 104.238.140.45 |
| 82.28 | trojan | 310.4 | 2.4 | 20.59 | 14.91 | 7.57 | 9.33 | 15.48 | Au1rxx-base64 | 216.152.156.65 |
| 81.93 | http | 312.1 | 1.1 | 20.55 | 14.96 | 0.0 | 14.38 | 19.54 | ermaozi | 172.64.68.89 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Surfboard-tg-mixed | 0.957 | 0.882 | 144 | 8419 | prefer |
| mheidari-all | 0.892 | 0.816 | 174 | 14456 | prefer |
| ermaozi | 0.828 | 0.941 | 17 | 502 | prefer |
| Au1rxx-base64 | 0.819 | 0.752 | 161 | 1751 | prefer |
| tg-ShadowsocksM | 0.707 | 0.929 | 14 | 64 | prefer |
| tg-LonUp_M | 0.392 | 0.714 | 7 | 166 | observe |
| xiaoji235-airport-v2ray-all | 0.335 | 1.0 | 1 | 6752 | observe |
| DeltaKronecker-all | 0.287 | 0.5 | 2 | 2790 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4928 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 11512 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5726 | observe |
| barry-far-vless | 0.255 | None | 0 | 5907 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4458 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 56 |
| 204 | ProxyError | - | 9 |
| cn-block | ProxyError | - | 6 |
| 204 | TimeoutError | - | 6 |
| cn-block | TimeoutError | - | 5 |
| cn-block | ClientOSError | - | 4 |
| geo | ClientOSError | - | 3 |
| geo | ProxyError | - | 2 |
| speed | ClientOSError | - | 2 |
| 204 | ClientOSError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 48 | 45 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
