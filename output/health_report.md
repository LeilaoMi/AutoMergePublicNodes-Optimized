# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-11-10 04:04:03 |
| 运行耗时 | 291.4s |
| 订阅源总数 | 107 |
| 健康订阅源 | 87 |
| 原始节点 | 82172 |
| 去重后节点 | 26780 |
| TCP 可达 | 3000 |
| 真实可用 | 561 |
| Verified 输出 | 134 |
| Global 输出 | 300 |
| All 输出 | 26780 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.9 |
| geo | 1.6 |
| tcp | 82.6 |
| probe | 86.7 |
| real_test | 85.7 |
| china_check | 17.5 |
| write_verified | 0.1 |
| generate | 11.5 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 49856 |
| vmess | 14148 |
| shadowsocks | 9186 |
| trojan | 6899 |
| hysteria2 | 1571 |
| http | 246 |
| shadowsocksr | 149 |
| socks | 52 |
| hysteria | 30 |
| tuic | 20 |
| anytls | 15 |

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
| 97.22 | trojan | 249.0 | 0.3 | 22.01 | 14.99 | 10.0 | 14.2 | 18.52 | Au1rxx-base64 | 66.163.114.45 |
| 95.66 | trojan | 253.7 | 2.0 | 21.91 | 14.93 | 8.6 | 14.2 | 18.52 | Au1rxx-base64 | 66.163.114.132 |
| 95.55 | shadowsocks | 262.5 | 4.0 | 21.7 | 14.85 | 10.0 | 14.48 | 18.52 | Au1rxx-base64 | 156.146.38.170 |
| 94.94 | trojan | 239.5 | 0.7 | 22.23 | 14.97 | 7.52 | 14.2 | 18.52 | Au1rxx-base64 | 66.163.114.126 |
| 94.9 | trojan | 253.1 | 3.1 | 21.92 | 14.89 | 7.87 | 14.2 | 18.52 | Au1rxx-base64 | 66.163.114.245 |
| 94.65 | trojan | 251.4 | 2.5 | 21.96 | 14.9 | 7.57 | 14.2 | 18.52 | Au1rxx-base64 | 66.163.114.166 |
| 93.14 | shadowsocks | 264.1 | 0.6 | 21.66 | 14.98 | 10.0 | 14.48 | 18.52 | Au1rxx-base64 | 156.146.38.168 |
| 93.06 | trojan | 289.9 | 1.2 | 21.07 | 14.95 | 9.93 | 14.2 | 18.52 | Au1rxx-base64 | 66.163.112.121 |
| 92.62 | trojan | 264.7 | 2.1 | 21.65 | 14.92 | 7.57 | 14.2 | 18.52 | Au1rxx-base64 | 66.163.114.106 |
| 91.75 | trojan | 329.9 | 3.0 | 20.14 | 14.89 | 10.0 | 14.2 | 18.52 | Au1rxx-base64 | 66.23.203.21 |
| 91.73 | trojan | 290.6 | 3.8 | 21.05 | 14.86 | 9.8 | 14.2 | 18.52 | Au1rxx-base64 | 167.88.61.175 |
| 91.66 | trojan | 242.5 | 3.8 | 22.17 | 14.86 | 7.54 | 14.2 | 18.52 | Au1rxx-base64 | 66.163.114.114 |
| 91.17 | trojan | 298.1 | 9.5 | 20.88 | 14.64 | 8.45 | 14.2 | 18.52 | Au1rxx-base64 | 66.163.112.242 |
| 90.84 | trojan | 305.7 | 0.3 | 20.7 | 14.99 | 7.39 | 14.2 | 18.52 | Au1rxx-base64 | 170.101.101.67 |
| 90.78 | trojan | 346.9 | 2.6 | 19.75 | 14.9 | 10.0 | 14.2 | 18.52 | Au1rxx-base64 | 216.238.80.100 |
| 90.49 | trojan | 278.9 | 2.3 | 21.32 | 14.91 | 8.39 | 14.2 | 18.52 | Au1rxx-base64 | 167.88.61.20 |
| 90.41 | trojan | 267.0 | 7.9 | 21.6 | 14.7 | 4.19 | 14.2 | 18.52 | Au1rxx-base64 | 216.152.155.54 |
| 90.33 | shadowsocks | 302.8 | 0.0 | 20.77 | 15.0 | 5.56 | 14.48 | 18.52 | Au1rxx-base64 | 156.146.38.169 |
| 90.22 | trojan | 285.0 | 2.2 | 21.18 | 14.92 | 8.41 | 14.2 | 18.52 | Au1rxx-base64 | 167.88.61.193 |
| 90.2 | shadowsocks | 329.7 | 2.5 | 20.14 | 14.91 | 10.0 | 14.48 | 18.52 | Au1rxx-base64 | 185.230.230.18 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 1.0 | 0.989 | 88 | 602 | prefer |
| Surfboard-tg-mixed | 0.941 | 0.864 | 206 | 8228 | prefer |
| Au1rxx-base64 | 0.906 | 0.839 | 236 | 1751 | prefer |
| mheidari-all | 0.726 | 0.648 | 145 | 14061 | prefer |
| xiaoji235-airport-v2ray-all | 0.335 | 1.0 | 1 | 6752 | observe |
| ninja-vless | 0.327 | 1.0 | 1 | 1791 | observe |
| DeltaKronecker-all | 0.287 | 0.5 | 2 | 2754 | observe |
| roosterkid-openproxylist-v2ray | 0.261 | 1.0 | 1 | 150 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4976 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 11245 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 6133 | observe |
| barry-far-vless | 0.255 | None | 0 | 6344 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4583 | observe |
| Au1rxx-clash | 0.245 | None | 0 | 1751 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 66 |
| speed | ClientOSError | - | 15 |
| geo | ClientOSError | - | 9 |
| speed | TimeoutError | - | 7 |
| 204 | ProxyError | - | 5 |
| 204 | ClientOSError | - | 4 |
| 204 | TimeoutError | - | 4 |
| cn-block | ClientOSError | - | 4 |
| cn-block | ProxyError | - | 2 |
| geo | ProxyError | - | 2 |
| cn-block | TimeoutError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 127 | 134 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
