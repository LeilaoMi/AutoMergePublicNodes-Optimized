# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-11-02 06:30:05 |
| 运行耗时 | 298.7s |
| 订阅源总数 | 107 |
| 健康订阅源 | 88 |
| 原始节点 | 82989 |
| 去重后节点 | 26848 |
| TCP 可达 | 3000 |
| 真实可用 | 369 |
| Verified 输出 | 41 |
| Global 输出 | 300 |
| All 输出 | 26848 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.5 |
| geo | 1.5 |
| tcp | 81.9 |
| probe | 81.2 |
| real_test | 81.5 |
| china_check | 36.0 |
| write_verified | 0.0 |
| generate | 11.2 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 49590 |
| vmess | 13938 |
| trojan | 8834 |
| shadowsocks | 8610 |
| hysteria2 | 1535 |
| http | 202 |
| shadowsocksr | 152 |
| socks | 78 |
| anytls | 24 |
| tuic | 15 |
| hysteria | 11 |

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
| 96.94 | trojan | 203.0 | 1.2 | 23.08 | 14.96 | 10.0 | 14.04 | 17.36 | Au1rxx-base64 | 66.163.112.121 |
| 96.62 | trojan | 199.1 | 0.1 | 23.17 | 15.0 | 9.55 | 14.04 | 17.36 | Au1rxx-base64 | 66.163.112.242 |
| 96.5 | trojan | 222.5 | 0.8 | 22.63 | 14.97 | 10.0 | 14.04 | 17.36 | Au1rxx-base64 | 167.88.61.175 |
| 95.8 | trojan | 225.6 | 1.3 | 22.56 | 14.95 | 9.39 | 14.04 | 17.36 | Au1rxx-base64 | 167.88.61.20 |
| 95.8 | trojan | 226.5 | 0.8 | 22.54 | 14.97 | 9.39 | 14.04 | 17.36 | Au1rxx-base64 | 167.88.61.193 |
| 95.08 | trojan | 229.3 | 18.3 | 22.47 | 14.31 | 9.4 | 14.04 | 17.36 | Au1rxx-base64 | 167.88.61.198 |
| 94.37 | vless | 198.6 | 3.9 | 23.18 | 14.85 | 9.99 | 8.99 | 17.36 | Au1rxx-base64 | 144.202.126.147 |
| 93.31 | trojan | 195.7 | 1.0 | 23.25 | 14.96 | 6.2 | 14.04 | 17.36 | Au1rxx-base64 | 66.163.112.13 |
| 93.27 | trojan | 198.7 | 0.2 | 23.18 | 14.99 | 6.2 | 14.04 | 17.36 | Au1rxx-base64 | 66.163.112.76 |
| 93.06 | trojan | 274.5 | 0.8 | 21.42 | 14.97 | 10.0 | 14.04 | 17.36 | Au1rxx-base64 | 66.163.114.45 |
| 91.93 | shadowsocks | 215.3 | 0.9 | 22.79 | 14.97 | 10.0 | 10.81 | 17.36 | Au1rxx-base64 | 173.244.56.6 |
| 91.85 | shadowsocks | 196.4 | 1.3 | 23.23 | 14.95 | 10.0 | 10.81 | 17.36 | Au1rxx-base64 | 95.215.201.18 |
| 91.78 | shadowsocks | 218.9 | 2.7 | 22.71 | 14.9 | 10.0 | 10.81 | 17.36 | Au1rxx-base64 | 173.244.56.9 |
| 91.1 | trojan | 251.2 | 3.1 | 21.96 | 14.88 | 5.36 | 14.04 | 17.36 | Au1rxx-base64 | 66.163.112.142 |
| 90.87 | shadowsocks | 262.7 | 0.1 | 21.7 | 15.0 | 10.0 | 10.81 | 17.36 | Au1rxx-base64 | 156.146.38.167 |
| 90.77 | shadowsocks | 265.8 | 0.6 | 21.62 | 14.98 | 10.0 | 10.81 | 17.36 | Au1rxx-base64 | 156.146.38.170 |
| 90.69 | trojan | 254.4 | 0.8 | 21.89 | 14.97 | 4.93 | 14.04 | 17.36 | Au1rxx-base64 | 167.88.61.85 |
| 90.65 | trojan | 322.9 | 1.6 | 20.3 | 14.94 | 10.0 | 14.04 | 17.36 | Au1rxx-base64 | 216.238.80.100 |
| 90.46 | vless | 203.5 | 2.1 | 23.07 | 14.92 | 6.12 | 8.99 | 17.36 | Au1rxx-base64 | 45.63.53.81 |
| 90.37 | trojan | 366.5 | 0.8 | 19.29 | 14.97 | 10.0 | 14.04 | 17.36 | Au1rxx-base64 | 66.23.203.21 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.89 | 1.0 | 18 | 43 | prefer |
| Au1rxx-base64 | 0.87 | 0.802 | 308 | 1751 | prefer |
| mheidari-all | 0.521 | 0.441 | 220 | 15216 | observe |
| ninja-vless | 0.383 | 1.0 | 2 | 1791 | observe |
| Surfboard-tg-mixed | 0.352 | 0.5 | 6 | 8273 | observe |
| xiaoji235-airport-v2ray-all | 0.32 | 0.5 | 4 | 6752 | observe |
| ermaozi-get_subscribe | 0.277 | 1.0 | 1 | 547 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4976 | observe |
| DeltaKronecker-all | 0.255 | None | 0 | 3716 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 10657 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5823 | observe |
| barry-far-vless | 0.255 | None | 0 | 6036 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4726 | observe |
| Au1rxx-clash | 0.245 | None | 0 | 1751 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 74 |
| geo | ClientOSError | - | 57 |
| 204 | ProxyError | - | 16 |
| cn-block | ProxyError | - | 9 |
| cn-block | TimeoutError | - | 8 |
| geo | ProxyError | - | 6 |
| 204 | TimeoutError | - | 6 |
| speed | ClientOSError | - | 6 |
| cn-block | ClientOSError | - | 4 |
| 204 | ClientOSError | - | 1 |
| speed | ProxyError | - | 1 |
| speed | TimeoutError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 74 | 41 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
