# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-11-16 06:52:06 |
| 运行耗时 | 298.0s |
| 订阅源总数 | 107 |
| 健康订阅源 | 88 |
| 原始节点 | 82990 |
| 去重后节点 | 27371 |
| TCP 可达 | 3000 |
| 真实可用 | 433 |
| Verified 输出 | 51 |
| Global 输出 | 300 |
| All 输出 | 27371 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.4 |
| geo | 1.5 |
| tcp | 82.4 |
| probe | 94.3 |
| real_test | 71.7 |
| china_check | 28.8 |
| write_verified | 0.0 |
| generate | 13.0 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 49510 |
| vmess | 14802 |
| shadowsocks | 9762 |
| trojan | 6980 |
| hysteria2 | 1529 |
| shadowsocksr | 153 |
| http | 114 |
| socks | 61 |
| hysteria | 36 |
| anytls | 26 |
| tuic | 17 |

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
| 93.39 | vless | 201.8 | 1.2 | 23.11 | 14.96 | 7.66 | 11.02 | 16.64 | Au1rxx-base64 | 45.63.53.81 |
| 93.22 | shadowsocks | 186.5 | 1.0 | 23.46 | 14.96 | 10.0 | 12.66 | 16.64 | Au1rxx-base64 | 95.215.201.18 |
| 91.7 | shadowsocks | 269.1 | 4.1 | 21.55 | 14.85 | 10.0 | 12.66 | 16.64 | Au1rxx-base64 | 156.146.38.167 |
| 89.64 | vless | 273.6 | 57.0 | 21.44 | 12.86 | 8.68 | 11.02 | 16.64 | Au1rxx-base64 | 195.123.240.65 |
| 87.98 | shadowsocks | 269.0 | 1.9 | 21.55 | 14.93 | 6.2 | 12.66 | 16.64 | Au1rxx-base64 | 156.146.38.169 |
| 87.62 | trojan | 201.8 | 6.9 | 23.11 | 14.74 | 9.75 | 5.88 | 16.64 | Au1rxx-base64 | 66.163.112.242 |
| 86.75 | shadowsocks | 289.6 | 3.5 | 21.07 | 14.87 | 10.0 | 12.66 | 16.64 | Au1rxx-base64 | 156.146.38.170 |
| 86.32 | hysteria2 | 221.6 | 3.0 | 22.65 | 14.89 | 0.0 | 13.24 | 16.54 | Surfboard-tg-mixed | 192.255.152.147 |
| 86.01 | trojan | 198.1 | 5.3 | 23.19 | 14.8 | 10.0 | 5.88 | 16.64 | Au1rxx-base64 | 66.163.112.121 |
| 85.37 | shadowsocks | 335.5 | 1.1 | 20.01 | 14.96 | 10.0 | 12.66 | 16.64 | Au1rxx-base64 | 45.86.51.18 |
| 85.21 | shadowsocks | 346.0 | 4.1 | 19.77 | 14.85 | 10.0 | 12.66 | 16.64 | Au1rxx-base64 | 185.230.230.18 |
| 85.03 | shadowsocks | 364.4 | 1.1 | 19.34 | 14.96 | 10.0 | 12.66 | 16.64 | Au1rxx-base64 | 193.151.160.9 |
| 84.85 | shadowsocks | 345.8 | 2.8 | 19.77 | 14.89 | 9.26 | 12.66 | 16.64 | Au1rxx-base64 | 193.151.160.18 |
| 84.29 | trojan | 195.3 | 7.4 | 23.26 | 14.72 | 6.29 | 5.88 | 16.64 | Au1rxx-base64 | 66.163.112.142 |
| 83.94 | vless | 240.3 | 1.2 | 22.22 | 14.96 | 0.0 | 11.02 | 17.74 | mheidari-all | 107.174.50.37 |
| 83.84 | shadowsocks | 362.7 | 3.3 | 19.38 | 14.88 | 10.0 | 12.66 | 16.64 | Au1rxx-base64 | 193.151.163.18 |
| 83.59 | http | 210.1 | 1.2 | 22.91 | 14.96 | 0.0 | 14.38 | 18.84 | ermaozi | 172.64.68.89 |
| 83.53 | shadowsocks | 183.1 | 2.9 | 23.54 | 14.89 | 0.0 | 12.66 | 16.54 | Surfboard-tg-mixed | 38.145.220.193 |
| 83.04 | trojan | 199.7 | 4.1 | 23.16 | 14.85 | 8.01 | 5.88 | 16.64 | Au1rxx-base64 | 66.163.112.76 |
| 82.91 | http | 298.2 | 0.5 | 20.88 | 14.98 | 0.0 | 14.38 | 18.84 | ermaozi | 44.248.167.117 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Surfboard-tg-mixed | 0.982 | 0.908 | 130 | 8824 | prefer |
| ermaozi | 0.94 | 1.0 | 19 | 471 | prefer |
| Au1rxx-base64 | 0.899 | 0.832 | 173 | 1751 | prefer |
| mheidari-all | 0.871 | 0.795 | 185 | 14209 | prefer |
| ninja-vless | 0.383 | 1.0 | 2 | 1791 | observe |
| tg-LonUp_M | 0.365 | 1.0 | 3 | 164 | observe |
| mahdibland-V2RayAggregator | 0.335 | 1.0 | 1 | 4545 | observe |
| xiaoji235-airport-v2ray-all | 0.335 | 1.0 | 1 | 6752 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4916 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 11553 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 6113 | observe |
| barry-far-vless | 0.255 | None | 0 | 6294 | observe |
| Au1rxx-clash | 0.245 | None | 0 | 1751 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 44 |
| 204 | ProxyError | - | 18 |
| 204 | TimeoutError | - | 4 |
| speed | ClientOSError | - | 3 |
| cn-block | ProxyError | - | 3 |
| 204 | ClientOSError | - | 3 |
| cn-block | TimeoutError | - | 2 |
| geo | ClientOSError | - | 2 |
| cn-block | ClientOSError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 44 | 51 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
