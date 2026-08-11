# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-11 02:10:23 |
| 运行耗时 | 306.2s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 85365 |
| 去重后节点 | 24753 |
| TCP 可达 | 3000 |
| 真实可用 | 635 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 24753 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.2 |
| geo | 1.4 |
| tcp | 37.0 |
| probe | 60.3 |
| real_test | 165.2 |
| generate | 37.0 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 50219 |
| vmess | 13252 |
| trojan | 10593 |
| shadowsocks | 9737 |
| hysteria2 | 1295 |
| socks | 76 |
| shadowsocksr | 73 |
| http | 72 |
| anytls | 26 |
| hysteria | 13 |
| tuic | 9 |

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
| 82.75 | trojan | 247.7 | 602.3 | 22.04 | 0.0 | 10.0 | 14.39 | 19.32 | Au1rxx-base64 | 64.94.95.115 |
| 81.98 | trojan | 281.0 | 706.0 | 21.27 | 0.0 | 10.0 | 14.39 | 19.32 | Au1rxx-base64 | 64.94.95.117 |
| 81.58 | shadowsocks | 233.8 | 594.2 | 22.36 | 0.0 | 10.0 | 13.9 | 19.32 | Au1rxx-base64 | 156.146.38.168 |
| 81.5 | shadowsocks | 237.6 | 606.7 | 22.28 | 0.0 | 10.0 | 13.9 | 19.32 | Au1rxx-base64 | 156.146.38.170 |
| 81.28 | shadowsocks | 246.8 | 632.1 | 22.06 | 0.0 | 10.0 | 13.9 | 19.32 | Au1rxx-base64 | 156.146.38.169 |
| 80.6 | trojan | 322.6 | 828.5 | 20.31 | 0.0 | 10.0 | 14.39 | 19.32 | Au1rxx-base64 | 64.94.95.118 |
| 80.48 | hysteria2 | 317.0 | 733.5 | 20.44 | 0.0 | 10.0 | 13.5 | 19.32 | Au1rxx-base64 | 138.124.68.188 |
| 78.43 | hysteria2 | 378.6 | 894.7 | 19.01 | 0.0 | 10.0 | 13.5 | 19.32 | Au1rxx-base64 | 159.223.157.129 |
| 78.42 | vless | 260.5 | 551.1 | 21.75 | 0.0 | 10.0 | 9.94 | 19.32 | Au1rxx-base64 | 179.255.148.66 |
| 78.37 | vless | 260.8 | 542.7 | 21.74 | 0.0 | 10.0 | 9.94 | 19.32 | Au1rxx-base64 | 179.253.240.24 |
| 78.21 | trojan | 289.8 | 584.5 | 21.07 | 0.0 | 10.0 | 14.39 | 19.32 | Au1rxx-base64 | 44.246.163.102 |
| 77.61 | hysteria2 | 331.1 | 773.6 | 20.11 | 0.0 | 7.76 | 13.5 | 19.32 | Au1rxx-base64 | usa1.spectrumproxy.shop |
| 77.4 | trojan | 323.6 | 679.7 | 20.29 | 0.0 | 10.0 | 14.39 | 19.32 | Au1rxx-base64 | 44.244.3.114 |
| 77.27 | vless | 273.3 | 577.9 | 21.45 | 0.0 | 10.0 | 9.94 | 19.32 | Au1rxx-base64 | 186.241.106.97 |
| 77.06 | trojan | 339.2 | 731.4 | 19.93 | 0.0 | 10.0 | 14.39 | 19.32 | Au1rxx-base64 | 35.86.90.51 |
| 76.75 | trojan | 350.1 | 759.2 | 19.67 | 0.0 | 10.0 | 14.39 | 19.32 | Au1rxx-base64 | 44.242.235.129 |
| 76.53 | shadowsocks | 236.4 | 601.0 | 22.31 | 0.0 | 10.0 | 13.9 | 19.32 | Au1rxx-base64 | 156.146.38.167 |
| 76.18 | shadowsocks | 303.2 | 689.4 | 20.76 | 0.0 | 10.0 | 13.9 | 19.32 | Au1rxx-base64 | 173.244.56.9 |
| 75.49 | shadowsocks | 328.4 | 707.2 | 20.18 | 0.0 | 10.0 | 13.9 | 19.32 | Au1rxx-base64 | 37.19.198.236 |
| 75.44 | shadowsocks | 322.0 | 713.5 | 20.32 | 0.0 | 10.0 | 13.9 | 19.32 | Au1rxx-base64 | 37.19.198.160 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.983 | 1.0 | 49 | 67 | prefer |
| Au1rxx-base64 | 0.938 | 0.881 | 404 | 1463 | prefer |
| Surfboard-tg-mixed | 0.713 | 0.643 | 28 | 6329 | prefer |
| mheidari-all | 0.459 | 0.378 | 534 | 20211 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| roosterkid-openproxylist-v2ray | 0.261 | 1.0 | 1 | 150 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5327 | observe |
| Epodonios-all | 0.255 | None | 0 | 6946 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3996 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7525 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5163 | observe |
| barry-far-vless | 0.255 | None | 0 | 5506 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5191 | observe |
| DeltaKronecker-all | 0.25 | 0.157 | 51 | 5881 | downweight |
| nscl5-all | 0.239 | None | 0 | 1607 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 176 |
| speed | TimeoutError | - | 86 |
| geo | ClientOSError | - | 80 |
| speed | ClientOSError | - | 43 |
| cn-block | TimeoutError | - | 19 |
| 204 | ProxyError | - | 13 |
| 204 | TimeoutError | - | 12 |
| 204 | ClientOSError | - | 4 |
| cn-block | ProxyError | - | 3 |
| cn-block | ClientOSError | - | 1 |
| speed | ClientPayloadError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
