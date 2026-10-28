# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-28 13:18:02 |
| 运行耗时 | 303.9s |
| 订阅源总数 | 107 |
| 健康订阅源 | 88 |
| 原始节点 | 97874 |
| 去重后节点 | 26563 |
| TCP 可达 | 3000 |
| 真实可用 | 394 |
| Verified 输出 | 66 |
| Global 输出 | 300 |
| All 输出 | 26563 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.2 |
| geo | 1.6 |
| tcp | 82.1 |
| probe | 98.2 |
| real_test | 79.7 |
| china_check | 21.4 |
| write_verified | 0.0 |
| generate | 13.8 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 57449 |
| vmess | 17773 |
| shadowsocks | 12872 |
| trojan | 8038 |
| hysteria2 | 1364 |
| shadowsocksr | 166 |
| http | 117 |
| socks | 51 |
| anytls | 21 |
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
| 95.79 | hysteria2 | 261.6 | 9.4 | 21.72 | 14.65 | 9.5 | 12.5 | 18.92 | Au1rxx-base64 | 129.213.91.185 |
| 94.07 | trojan | 263.2 | 7.2 | 21.69 | 14.73 | 9.33 | 13.1 | 18.92 | Au1rxx-base64 | 66.23.203.21 |
| 93.67 | shadowsocks | 302.1 | 9.9 | 20.79 | 14.63 | 9.4 | 13.93 | 18.92 | Au1rxx-base64 | 156.146.38.168 |
| 93.43 | shadowsocks | 296.3 | 9.9 | 20.92 | 14.63 | 9.03 | 13.93 | 18.92 | Au1rxx-base64 | 37.19.198.243 |
| 93.27 | shadowsocks | 294.7 | 2.7 | 20.96 | 14.9 | 9.06 | 13.93 | 18.92 | Au1rxx-base64 | 193.151.163.18 |
| 93.25 | trojan | 222.9 | 1.2 | 22.62 | 14.96 | 7.15 | 13.1 | 18.92 | Au1rxx-base64 | 216.152.155.176 |
| 93.19 | shadowsocks | 334.9 | 2.6 | 20.02 | 14.9 | 9.42 | 13.93 | 18.92 | Au1rxx-base64 | 37.19.198.244 |
| 93.11 | shadowsocks | 281.4 | 26.8 | 21.26 | 14.0 | 9.0 | 13.93 | 18.92 | Au1rxx-base64 | 156.146.38.170 |
| 92.98 | trojan | 259.5 | 2.6 | 21.77 | 14.9 | 9.01 | 13.1 | 18.92 | Au1rxx-base64 | 66.163.114.132 |
| 92.64 | shadowsocks | 288.3 | 22.4 | 21.11 | 14.16 | 9.02 | 13.93 | 18.92 | Au1rxx-base64 | 185.230.230.18 |
| 92.55 | trojan | 226.9 | 17.1 | 22.52 | 14.36 | 7.15 | 13.1 | 18.92 | Au1rxx-base64 | 216.152.155.23 |
| 92.08 | trojan | 222.3 | 3.1 | 22.63 | 14.88 | 6.05 | 13.1 | 18.92 | Au1rxx-base64 | 216.152.155.158 |
| 91.8 | shadowsocks | 363.6 | 8.6 | 19.36 | 14.68 | 9.41 | 13.93 | 18.92 | Au1rxx-base64 | 45.86.51.18 |
| 91.64 | shadowsocks | 249.6 | 0.5 | 22.0 | 14.98 | 5.81 | 13.93 | 18.92 | Au1rxx-base64 | 156.146.38.169 |
| 91.48 | trojan | 309.2 | 2.6 | 20.62 | 14.9 | 7.44 | 13.1 | 18.92 | Au1rxx-base64 | 66.163.114.245 |
| 91.44 | trojan | 225.6 | 1.3 | 22.56 | 14.95 | 5.41 | 13.1 | 18.92 | Au1rxx-base64 | 216.152.155.54 |
| 91.23 | vless | 305.7 | 4.2 | 20.7 | 14.84 | 8.72 | 9.26 | 18.92 | Au1rxx-base64 | 195.123.235.177 |
| 91.12 | shadowsocks | 314.9 | 12.7 | 20.49 | 14.52 | 9.31 | 13.93 | 18.92 | Au1rxx-base64 | 193.151.160.18 |
| 91.1 | trojan | 215.8 | 6.6 | 22.78 | 14.75 | 6.05 | 13.1 | 18.92 | Au1rxx-base64 | 216.152.155.59 |
| 90.43 | trojan | 260.6 | 3.8 | 21.75 | 14.86 | 6.92 | 13.1 | 18.92 | Au1rxx-base64 | 66.163.114.106 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.939 | 0.943 | 35 | 513 | prefer |
| Au1rxx-base64 | 0.901 | 0.832 | 315 | 1778 | prefer |
| mheidari-all | 0.794 | 0.727 | 33 | 24702 | prefer |
| Surfboard-tg-mixed | 0.6 | 0.52 | 123 | 7544 | observe |
| roosterkid-openproxylist-v2ray | 0.372 | 0.8 | 5 | 150 | observe |
| xiaoji235-airport-v2ray-all | 0.335 | 1.0 | 1 | 6752 | observe |
| DeltaKronecker-all | 0.324 | 0.375 | 8 | 2801 | observe |
| ninja-vless | 0.279 | 0.5 | 2 | 1791 | observe |
| Epodonios-all | 0.272 | 0.286 | 7 | 8008 | observe |
| tg-OutlineReleasedKey | 0.257 | 1.0 | 1 | 50 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5004 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 10344 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5575 | observe |
| barry-far-vless | 0.255 | None | 0 | 5789 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 79 |
| geo | ClientOSError | - | 20 |
| 204 | ProxyError | - | 11 |
| cn-block | TimeoutError | - | 8 |
| 204 | TimeoutError | - | 6 |
| cn-block | ClientOSError | - | 5 |
| geo | ProxyError | - | 3 |
| geo | TimeoutError | - | 2 |
| 204 | ClientOSError | - | 1 |
| cn-block | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 68 | 66 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
