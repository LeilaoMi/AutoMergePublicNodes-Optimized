# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-04 13:49:30 |
| 运行耗时 | 212.4s |
| 订阅源总数 | 107 |
| 健康订阅源 | 103 |
| 原始节点 | 78542 |
| 去重后节点 | 23660 |
| TCP 可达 | 3000 |
| 真实可用 | 300 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23660 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 3.7 |
| geo | 1.4 |
| tcp | 31.1 |
| probe | 49.8 |
| real_test | 91.6 |
| generate | 34.8 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 45337 |
| trojan | 12507 |
| vmess | 10537 |
| shadowsocks | 9491 |
| hysteria2 | 306 |
| shadowsocksr | 145 |
| http | 135 |
| socks | 74 |
| hysteria | 6 |
| tuic | 3 |
| anytls | 1 |

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
| 77.49 | shadowsocks | 250.5 | 607.0 | 21.98 | 0.0 | 10.0 | 12.79 | 16.72 | Au1rxx-base64 | 156.146.38.167 |
| 77.0 | shadowsocks | 271.5 | 707.5 | 21.49 | 0.0 | 10.0 | 12.79 | 16.72 | Au1rxx-base64 | 156.146.38.168 |
| 76.99 | shadowsocks | 272.0 | 704.1 | 21.48 | 0.0 | 10.0 | 12.79 | 16.72 | Au1rxx-base64 | 156.146.38.170 |
| 76.9 | shadowsocks | 276.0 | 726.6 | 21.39 | 0.0 | 10.0 | 12.79 | 16.72 | Au1rxx-base64 | 156.146.38.169 |
| 76.58 | trojan | 246.2 | 602.2 | 22.08 | 0.0 | 10.0 | 11.42 | 16.08 | DeltaKronecker-all | 64.94.95.114 |
| 74.86 | trojan | 271.1 | 675.2 | 21.5 | 0.0 | 10.0 | 11.42 | 14.94 | mheidari-all | 64.94.95.118 |
| 73.13 | shadowsocks | 264.8 | 525.9 | 21.65 | 0.0 | 10.0 | 12.79 | 16.72 | Au1rxx-base64 | 108.181.118.10 |
| 72.02 | trojan | 443.1 | 1130.7 | 17.52 | 0.0 | 10.0 | 11.42 | 16.08 | DeltaKronecker-all | 64.94.95.115 |
| 71.89 | shadowsocks | 308.2 | 307.3 | 20.64 | 3.47 | 9.79 | 12.79 | 16.72 | Au1rxx-base64 | 149.22.87.241 |
| 71.72 | shadowsocks | 320.3 | 700.2 | 20.36 | 0.0 | 10.0 | 12.79 | 16.72 | Au1rxx-base64 | 37.19.198.236 |
| 71.7 | shadowsocks | 325.1 | 712.4 | 20.25 | 0.0 | 10.0 | 12.79 | 16.72 | Au1rxx-base64 | 37.19.198.160 |
| 71.4 | shadowsocks | 305.4 | 621.1 | 20.71 | 0.0 | 10.0 | 12.79 | 16.72 | Au1rxx-base64 | 149.22.95.183 |
| 71.31 | trojan | 279.5 | 713.0 | 21.31 | 0.0 | 10.0 | 11.42 | 16.08 | DeltaKronecker-all | 45.32.195.168 |
| 71.18 | trojan | 285.1 | 734.4 | 21.18 | 0.0 | 10.0 | 11.42 | 16.08 | DeltaKronecker-all | 149.28.241.235 |
| 71.07 | trojan | 289.7 | 750.3 | 21.07 | 0.0 | 10.0 | 11.42 | 16.08 | DeltaKronecker-all | 45.32.198.247 |
| 70.57 | shadowsocks | 354.8 | 799.6 | 19.56 | 0.0 | 10.0 | 12.79 | 16.72 | Au1rxx-base64 | 108.181.0.177 |
| 69.97 | shadowsocks | 321.8 | 610.3 | 20.33 | 0.0 | 10.0 | 12.79 | 16.72 | Au1rxx-base64 | 173.244.56.9 |
| 69.44 | shadowsocks | 322.2 | 707.1 | 20.32 | 0.0 | 10.0 | 12.79 | 16.72 | Au1rxx-base64 | 37.19.198.244 |
| 69.42 | shadowsocks | 357.3 | 719.1 | 19.51 | 0.0 | 10.0 | 12.79 | 16.72 | Au1rxx-base64 | 173.244.56.6 |
| 68.82 | shadowsocks | 327.6 | 375.1 | 20.19 | 0.94 | 9.79 | 12.79 | 16.72 | Au1rxx-base64 | 149.22.87.204 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| mheidari-all | 0.804 | 0.73 | 74 | 16374 | prefer |
| Au1rxx-base64 | 0.799 | 0.81 | 42 | 94 | prefer |
| Surfboard-tg-mixed | 0.794 | 0.719 | 89 | 6003 | prefer |
| DeltaKronecker-all | 0.727 | 0.648 | 165 | 7309 | prefer |
| SoliSpirit-all | 0.335 | 1.0 | 1 | 7174 | observe |
| nscl5-all | 0.303 | 1.0 | 1 | 1189 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| tg-LonUp_M | 0.262 | 1.0 | 1 | 180 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4579 | observe |
| Epodonios-all | 0.255 | None | 0 | 6895 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3973 | observe |
| barry-far-vless | 0.255 | None | 0 | 5028 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5333 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 24 |
| 204 | TimeoutError | - | 19 |
| 204 | ProxyError | - | 17 |
| geo | TimeoutError | - | 17 |
| cn-block | TimeoutError | - | 14 |
| cn-block | ClientOSError | - | 7 |
| 204 | ClientOSError | - | 6 |
| geo | ClientOSError | - | 3 |
| speed | TimeoutError | - | 2 |
| cn-block | ProxyError | - | 2 |
| geo | ProxyError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
