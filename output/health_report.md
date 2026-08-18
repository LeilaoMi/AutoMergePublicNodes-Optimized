# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-18 18:51:37 |
| 运行耗时 | 414.4s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 93066 |
| 去重后节点 | 24084 |
| TCP 可达 | 3000 |
| 真实可用 | 1197 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 24084 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.1 |
| geo | 1.0 |
| tcp | 36.5 |
| probe | 72.6 |
| real_test | 257.4 |
| generate | 39.8 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 52159 |
| trojan | 18721 |
| shadowsocks | 10565 |
| vmess | 9543 |
| hysteria2 | 1521 |
| http | 179 |
| socks | 154 |
| shadowsocksr | 149 |
| anytls | 47 |
| tuic | 15 |
| hysteria | 13 |

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
| 82.78 | http | 296.4 | 806.4 | 20.92 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.5 |
| 82.64 | http | 302.4 | 826.5 | 20.78 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.23 |
| 82.61 | http | 303.4 | 832.0 | 20.75 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.10 |
| 82.61 | http | 303.6 | 797.8 | 20.75 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.21 |
| 82.58 | http | 305.1 | 823.1 | 20.72 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.19 |
| 82.5 | http | 308.3 | 848.6 | 20.64 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.9 |
| 82.38 | http | 313.5 | 847.7 | 20.52 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.15 |
| 82.37 | http | 314.0 | 852.5 | 20.51 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.25 |
| 82.23 | http | 319.8 | 868.5 | 20.37 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.8 |
| 82.23 | http | 320.0 | 878.0 | 20.37 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.4 |
| 82.04 | http | 328.1 | 881.8 | 20.18 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.11 |
| 81.09 | http | 369.2 | 1028.2 | 19.23 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.27 |
| 80.82 | http | 380.7 | 1054.1 | 18.96 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.28 |
| 80.69 | http | 386.5 | 1082.8 | 18.83 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.31 |
| 80.68 | http | 387.2 | 1081.1 | 18.82 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.39 |
| 80.65 | http | 388.4 | 1068.8 | 18.79 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.41 |
| 80.63 | http | 389.1 | 1085.1 | 18.77 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.34 |
| 80.6 | vless | 292.8 | 716.2 | 21.0 | 0.0 | 10.0 | 9.6 | 20.0 | Au1rxx-base64 | 216.152.147.28 |
| 79.98 | vless | 319.7 | 890.7 | 20.38 | 0.0 | 10.0 | 9.6 | 20.0 | Au1rxx-base64 | 137.184.218.169 |
| 79.96 | vless | 262.8 | 623.6 | 21.69 | 0.0 | 10.0 | 9.6 | 20.0 | mheidari-all | 195.211.98.214 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | 0.976 | 755 | 1643 | prefer |
| zhangkai | 0.999 | 1.0 | 127 | 159 | prefer |
| Surfboard-tg-mixed | 0.997 | 0.941 | 34 | 6301 | prefer |
| mheidari-all | 0.889 | 0.811 | 365 | 22150 | prefer |
| nscl5-all | 0.438 | 1.0 | 3 | 2992 | observe |
| DeltaKronecker-all | 0.335 | 1.0 | 1 | 5725 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5068 | observe |
| Epodonios-all | 0.255 | None | 0 | 6927 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7150 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4855 | observe |
| barry-far-vless | 0.255 | None | 0 | 5149 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4035 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | ClientOSError | - | 40 |
| speed | TimeoutError | - | 14 |
| 204 | TimeoutError | - | 10 |
| cn-block | TimeoutError | - | 9 |
| geo | TimeoutError | - | 6 |
| speed | ClientOSError | - | 4 |
| cn-block | ClientOSError | - | 4 |
| 204 | ProxyError | - | 2 |
| cn-block | ProxyError | - | 1 |
| 204 | ClientOSError | - | 1 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
