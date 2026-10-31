# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-31 06:00:38 |
| 运行耗时 | 288.1s |
| 订阅源总数 | 107 |
| 健康订阅源 | 88 |
| 原始节点 | 80746 |
| 去重后节点 | 26596 |
| TCP 可达 | 3000 |
| 真实可用 | 583 |
| Verified 输出 | 146 |
| Global 输出 | 300 |
| All 输出 | 26596 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.1 |
| geo | 1.4 |
| tcp | 79.3 |
| probe | 68.1 |
| real_test | 94.5 |
| china_check | 31.3 |
| write_verified | 0.0 |
| generate | 9.4 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 48646 |
| vmess | 13885 |
| shadowsocks | 8529 |
| trojan | 7629 |
| hysteria2 | 1471 |
| http | 335 |
| shadowsocksr | 159 |
| socks | 54 |
| tuic | 15 |
| hysteria | 12 |
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
| 98.18 | hysteria2 | 263.2 | 0.5 | 21.68 | 14.98 | 10.0 | 14.0 | 19.02 | Au1rxx-base64 | 129.213.91.185 |
| 96.98 | trojan | 290.7 | 0.5 | 21.05 | 14.98 | 10.0 | 14.43 | 19.02 | Au1rxx-base64 | 66.163.114.45 |
| 96.12 | trojan | 294.4 | 0.1 | 20.96 | 15.0 | 9.44 | 14.43 | 19.02 | Au1rxx-base64 | 66.163.114.132 |
| 95.51 | shadowsocks | 238.5 | 2.4 | 22.26 | 14.91 | 10.0 | 13.32 | 19.02 | Au1rxx-base64 | 156.146.38.170 |
| 95.51 | trojan | 256.4 | 0.1 | 21.84 | 15.0 | 7.72 | 14.43 | 19.02 | Au1rxx-base64 | 66.163.114.166 |
| 95.44 | trojan | 260.6 | 1.7 | 21.75 | 14.93 | 7.91 | 14.43 | 19.02 | Au1rxx-base64 | 66.163.114.245 |
| 95.38 | trojan | 259.0 | 0.9 | 21.78 | 14.97 | 7.68 | 14.43 | 19.02 | Au1rxx-base64 | 66.163.114.114 |
| 95.02 | trojan | 260.5 | 0.1 | 21.75 | 15.0 | 7.32 | 14.43 | 19.02 | Au1rxx-base64 | 66.163.114.126 |
| 94.94 | shadowsocks | 262.6 | 2.6 | 21.7 | 14.9 | 10.0 | 13.32 | 19.02 | Au1rxx-base64 | 156.146.38.167 |
| 94.9 | shadowsocks | 247.9 | 0.8 | 22.04 | 14.97 | 10.0 | 13.32 | 19.02 | Au1rxx-base64 | 156.146.38.168 |
| 94.79 | trojan | 357.5 | 4.2 | 19.5 | 14.84 | 10.0 | 14.43 | 19.02 | Au1rxx-base64 | 66.23.203.21 |
| 94.09 | trojan | 258.2 | 0.2 | 21.8 | 14.99 | 7.72 | 14.43 | 19.02 | Au1rxx-base64 | 66.163.114.106 |
| 93.56 | shadowsocks | 302.6 | 1.4 | 20.77 | 14.95 | 10.0 | 13.32 | 19.02 | Au1rxx-base64 | 45.86.51.18 |
| 92.78 | trojan | 302.6 | 2.5 | 20.77 | 14.9 | 7.28 | 14.43 | 19.02 | Au1rxx-base64 | 216.152.156.65 |
| 92.78 | trojan | 342.8 | 0.6 | 19.84 | 14.98 | 7.4 | 14.43 | 19.02 | Au1rxx-base64 | 216.152.155.59 |
| 92.55 | trojan | 286.5 | 1.5 | 21.15 | 14.94 | 7.39 | 14.43 | 19.02 | Au1rxx-base64 | 170.101.101.67 |
| 92.41 | trojan | 294.7 | 0.5 | 20.96 | 14.98 | 7.21 | 14.43 | 19.02 | Au1rxx-base64 | 216.152.147.93 |
| 92.41 | trojan | 304.7 | 1.2 | 20.72 | 14.95 | 10.0 | 14.43 | 19.02 | Au1rxx-base64 | 66.163.112.121 |
| 92.29 | trojan | 303.4 | 0.5 | 20.75 | 14.98 | 7.3 | 14.43 | 19.02 | Au1rxx-base64 | 216.152.156.49 |
| 92.08 | trojan | 299.7 | 0.3 | 20.84 | 14.99 | 9.96 | 14.43 | 19.02 | Au1rxx-base64 | 167.88.61.175 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.994 | 0.979 | 95 | 622 | prefer |
| Au1rxx-base64 | 0.926 | 0.858 | 339 | 1751 | prefer |
| mheidari-all | 0.846 | 0.771 | 109 | 14594 | prefer |
| Surfboard-tg-mixed | 0.716 | 0.638 | 174 | 7827 | prefer |
| xiaoji235-airport-v2ray-all | 0.391 | 1.0 | 2 | 6752 | observe |
| DeltaKronecker-all | 0.287 | 0.5 | 2 | 2724 | observe |
| roosterkid-openproxylist-v2ray | 0.261 | 1.0 | 1 | 150 | observe |
| tg-oneclickvpnkeys | 0.259 | 1.0 | 1 | 94 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4960 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 10524 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5680 | observe |
| barry-far-vless | 0.255 | None | 0 | 5895 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4635 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 71 |
| geo | ClientOSError | - | 31 |
| cn-block | ClientOSError | - | 7 |
| 204 | TimeoutError | - | 6 |
| cn-block | TimeoutError | - | 6 |
| cn-block | ProxyError | - | 4 |
| 204 | ProxyError | - | 4 |
| speed | ClientOSError | - | 3 |
| 204 | ClientOSError | - | 3 |
| speed | ProxyError | - | 2 |
| speed | TimeoutError | - | 1 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 107 | 146 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
