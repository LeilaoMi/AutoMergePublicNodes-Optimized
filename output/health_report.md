# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-17 13:00:12 |
| 运行耗时 | 402.8s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 83032 |
| 去重后节点 | 23200 |
| TCP 可达 | 3000 |
| 真实可用 | 1265 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23200 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.2 |
| geo | 0.8 |
| tcp | 34.7 |
| probe | 85.3 |
| real_test | 237.6 |
| generate | 38.2 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 45327 |
| trojan | 15202 |
| vmess | 11069 |
| shadowsocks | 9744 |
| hysteria2 | 1214 |
| socks | 192 |
| http | 190 |
| shadowsocksr | 73 |
| tuic | 10 |
| hysteria | 7 |
| anytls | 4 |

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
| 85.35 | http | 185.3 | 477.0 | 23.49 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.206 |
| 85.3 | http | 187.5 | 482.9 | 23.44 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.220 |
| 85.29 | http | 187.7 | 485.0 | 23.43 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.195 |
| 85.28 | http | 188.3 | 489.5 | 23.42 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.197 |
| 85.18 | http | 192.4 | 490.9 | 23.32 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.210 |
| 85.16 | http | 193.6 | 506.1 | 23.3 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.213 |
| 85.13 | http | 194.9 | 504.8 | 23.27 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.209 |
| 85.12 | http | 195.2 | 497.3 | 23.26 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.215 |
| 85.11 | http | 195.5 | 511.0 | 23.25 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.208 |
| 85.06 | http | 197.9 | 515.8 | 23.2 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.211 |
| 85.05 | http | 198.1 | 508.8 | 23.19 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.214 |
| 84.89 | http | 205.1 | 534.7 | 23.03 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.212 |
| 84.88 | http | 205.6 | 531.9 | 23.02 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.199 |
| 83.69 | vless | 192.8 | 506.8 | 23.31 | 0.0 | 10.0 | 10.38 | 20.0 | Au1rxx-base64 | 216.36.124.176 |
| 82.79 | shadowsocks | 207.8 | 532.4 | 22.97 | 0.0 | 10.0 | 13.82 | 20.0 | Au1rxx-base64 | 173.244.56.9 |
| 82.04 | shadowsocks | 193.5 | 495.3 | 23.3 | 0.0 | 10.0 | 13.82 | 20.0 | Au1rxx-base64 | 70.39.198.35 |
| 81.5 | shadowsocks | 241.7 | 581.7 | 22.18 | 0.0 | 10.0 | 13.82 | 20.0 | Au1rxx-base64 | 108.181.118.10 |
| 81.47 | shadowsocks | 264.6 | 661.5 | 21.65 | 0.0 | 10.0 | 13.82 | 20.0 | Au1rxx-base64 | 173.244.56.6 |
| 81.27 | shadowsocks | 273.6 | 638.8 | 21.45 | 0.0 | 10.0 | 13.82 | 20.0 | Au1rxx-base64 | 156.146.38.168 |
| 80.56 | vless | 204.4 | 507.7 | 23.05 | 0.0 | 10.0 | 10.38 | 20.0 | Au1rxx-base64 | 70.39.198.183 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | 0.943 | 884 | 1983 | prefer |
| zhangkai | 0.999 | 1.0 | 127 | 159 | prefer |
| Surfboard-tg-mixed | 0.942 | 0.873 | 63 | 6086 | prefer |
| mheidari-all | 0.933 | 0.856 | 284 | 17057 | prefer |
| DeltaKronecker-all | 0.376 | 0.333 | 15 | 6368 | observe |
| tg-oneclickvpnkeys | 0.263 | 1.0 | 1 | 194 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5085 | observe |
| Epodonios-all | 0.255 | None | 0 | 6645 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3989 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7827 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4669 | observe |
| barry-far-vless | 0.255 | None | 0 | 4992 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4046 | observe |
| nscl5-all | 0.255 | None | 0 | 3043 | observe |
| Au1rxx-clash | 0.254 | None | 0 | 1983 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| cn-block | TimeoutError | - | 31 |
| speed | TimeoutError | - | 20 |
| geo | TimeoutError | - | 15 |
| 204 | TimeoutError | - | 13 |
| speed | ClientOSError | - | 10 |
| geo | ClientOSError | - | 6 |
| cn-block | ClientOSError | - | 5 |
| 204 | ProxyError | - | 5 |
| 204 | ClientOSError | - | 4 |
| cn-block | ProxyError | - | 1 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
