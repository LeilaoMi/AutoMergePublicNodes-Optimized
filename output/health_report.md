# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-17 07:11:31 |
| 运行耗时 | 370.3s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 82922 |
| 去重后节点 | 23092 |
| TCP 可达 | 3000 |
| 真实可用 | 1340 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23092 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.8 |
| geo | 1.2 |
| tcp | 34.4 |
| probe | 67.9 |
| real_test | 229.6 |
| generate | 31.4 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 45610 |
| trojan | 15281 |
| vmess | 11027 |
| shadowsocks | 9578 |
| hysteria2 | 1080 |
| http | 160 |
| socks | 87 |
| shadowsocksr | 76 |
| tuic | 10 |
| hysteria | 7 |
| anytls | 6 |

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
| 84.99 | trojan | 216.4 | 489.3 | 22.77 | 0.0 | 10.0 | 14.72 | 20.0 | Au1rxx-base64 | 44.246.163.102 |
| 84.9 | http | 193.1 | 487.9 | 23.31 | 0.0 | 10.0 | 14.77 | 19.82 | zhangkai | 138.199.35.210 |
| 84.84 | http | 195.7 | 497.3 | 23.25 | 0.0 | 10.0 | 14.77 | 19.82 | zhangkai | 138.199.35.208 |
| 84.83 | http | 195.9 | 506.4 | 23.24 | 0.0 | 10.0 | 14.77 | 19.82 | zhangkai | 138.199.35.199 |
| 84.83 | http | 196.0 | 495.0 | 23.24 | 0.0 | 10.0 | 14.77 | 19.82 | zhangkai | 138.199.35.215 |
| 84.83 | http | 196.1 | 500.3 | 23.24 | 0.0 | 10.0 | 14.77 | 19.82 | zhangkai | 138.199.35.209 |
| 84.76 | http | 198.9 | 507.3 | 23.17 | 0.0 | 10.0 | 14.77 | 19.82 | zhangkai | 138.199.35.213 |
| 84.76 | http | 199.2 | 500.9 | 23.17 | 0.0 | 10.0 | 14.77 | 19.82 | zhangkai | 138.199.35.212 |
| 84.73 | http | 200.3 | 504.6 | 23.14 | 0.0 | 10.0 | 14.77 | 19.82 | zhangkai | 138.199.35.195 |
| 84.73 | http | 200.5 | 510.2 | 23.14 | 0.0 | 10.0 | 14.77 | 19.82 | zhangkai | 138.199.35.206 |
| 84.7 | http | 201.4 | 510.4 | 23.11 | 0.0 | 10.0 | 14.77 | 19.82 | zhangkai | 138.199.35.204 |
| 84.7 | trojan | 223.2 | 505.6 | 22.61 | 0.0 | 9.87 | 14.72 | 20.0 | Au1rxx-base64 | sharing-duck.rooster465.autos |
| 84.66 | trojan | 230.6 | 533.1 | 22.44 | 0.0 | 10.0 | 14.72 | 20.0 | Au1rxx-base64 | 44.244.3.114 |
| 84.65 | trojan | 228.8 | 520.3 | 22.48 | 0.0 | 9.95 | 14.72 | 20.0 | Au1rxx-base64 | fleet-bonefish.rooster465.autos |
| 84.64 | trojan | 231.4 | 533.1 | 22.42 | 0.0 | 10.0 | 14.72 | 20.0 | Au1rxx-base64 | liked-serval.rooster465.autos |
| 84.62 | http | 205.2 | 499.7 | 23.03 | 0.0 | 10.0 | 14.77 | 19.82 | zhangkai | 138.199.35.220 |
| 84.55 | http | 208.2 | 524.6 | 22.96 | 0.0 | 10.0 | 14.77 | 19.82 | zhangkai | 138.199.35.214 |
| 84.55 | http | 208.3 | 533.5 | 22.96 | 0.0 | 10.0 | 14.77 | 19.82 | zhangkai | 138.199.35.211 |
| 84.55 | trojan | 218.4 | 494.2 | 22.72 | 0.0 | 10.0 | 14.72 | 20.0 | Au1rxx-base64 | pet-ghost.rooster465.autos |
| 84.46 | trojan | 239.2 | 555.1 | 22.24 | 0.0 | 10.0 | 14.72 | 20.0 | Au1rxx-base64 | 35.88.120.18 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | 0.942 | 867 | 1991 | prefer |
| mheidari-all | 1.0 | 0.959 | 246 | 17400 | prefer |
| zhangkai | 0.999 | 1.0 | 127 | 159 | prefer |
| Surfboard-tg-mixed | 0.767 | 0.688 | 215 | 5925 | prefer |
| nscl5-all | 0.335 | 1.0 | 1 | 3043 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| tg-oneclickvpnkeys | 0.262 | 1.0 | 1 | 164 | observe |
| Au1rxx-clash | 0.255 | None | 0 | 1991 | observe |
| Epodonios-all | 0.255 | None | 0 | 6602 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3988 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7808 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4592 | observe |
| barry-far-vless | 0.255 | None | 0 | 4931 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4046 | observe |
| DeltaKronecker-all | 0.252 | 0.161 | 56 | 6368 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 50 |
| cn-block | TimeoutError | - | 26 |
| 204 | TimeoutError | - | 24 |
| speed | TimeoutError | - | 21 |
| geo | ClientOSError | - | 19 |
| speed | ClientOSError | - | 16 |
| cn-block | ClientOSError | - | 7 |
| 204 | ProxyError | - | 6 |
| 204 | ClientOSError | - | 5 |
| cn-block | ProxyError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
