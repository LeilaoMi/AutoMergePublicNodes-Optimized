# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-17 18:53:43 |
| 运行耗时 | 424.9s |
| 订阅源总数 | 107 |
| 健康订阅源 | 100 |
| 原始节点 | 80814 |
| 去重后节点 | 22843 |
| TCP 可达 | 3000 |
| 真实可用 | 1404 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22843 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.8 |
| geo | 0.9 |
| tcp | 35.9 |
| probe | 73.3 |
| real_test | 268.9 |
| generate | 39.2 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 46734 |
| trojan | 14339 |
| shadowsocks | 9736 |
| vmess | 8327 |
| hysteria2 | 1231 |
| http | 195 |
| socks | 143 |
| shadowsocksr | 80 |
| tuic | 20 |
| hysteria | 7 |
| anytls | 2 |

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
| 82.51 | http | 242.8 | 534.4 | 22.16 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.213 |
| 82.43 | http | 244.9 | 539.1 | 22.11 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.206 |
| 82.16 | http | 255.2 | 565.5 | 21.87 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.208 |
| 82.05 | http | 250.1 | 545.4 | 21.99 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.215 |
| 81.66 | http | 244.7 | 534.8 | 22.11 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.211 |
| 81.45 | http | 251.3 | 563.7 | 21.96 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.214 |
| 81.41 | http | 247.2 | 549.9 | 22.06 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.204 |
| 81.38 | http | 253.8 | 557.8 | 21.9 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.212 |
| 81.34 | http | 239.3 | 526.6 | 22.24 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.195 |
| 81.31 | http | 254.3 | 568.7 | 21.89 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.209 |
| 81.22 | http | 250.9 | 558.4 | 21.97 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.197 |
| 81.09 | http | 242.8 | 538.8 | 22.16 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.220 |
| 80.9 | http | 246.9 | 541.8 | 22.06 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.210 |
| 80.84 | shadowsocks | 255.9 | 613.0 | 21.85 | 0.0 | 10.0 | 14.15 | 18.84 | Surfboard-tg-mixed | 156.146.38.168 |
| 80.8 | http | 246.4 | 540.5 | 22.07 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.199 |
| 80.69 | trojan | 265.9 | 524.9 | 21.62 | 0.0 | 10.0 | 14.71 | 20.0 | Au1rxx-base64 | 14.1.28.76 |
| 80.69 | hysteria2 | 326.3 | 745.1 | 20.23 | 0.0 | 10.0 | 13.2 | 20.0 | Au1rxx-base64 | 138.124.68.188 |
| 80.57 | trojan | 335.0 | 863.5 | 20.02 | 0.0 | 10.0 | 14.71 | 18.84 | Surfboard-tg-mixed | 64.94.95.114 |
| 80.3 | shadowsocks | 236.3 | 590.8 | 22.31 | 0.0 | 10.0 | 14.15 | 18.84 | Surfboard-tg-mixed | 156.146.38.170 |
| 80.07 | trojan | 356.7 | 859.9 | 19.52 | 0.0 | 10.0 | 14.71 | 18.84 | Surfboard-tg-mixed | 64.94.95.118 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| mheidari-all | 1.0 | 0.99 | 303 | 15619 | prefer |
| zhangkai | 0.999 | 1.0 | 127 | 159 | prefer |
| Au1rxx-base64 | 0.97 | 0.892 | 960 | 1983 | prefer |
| Surfboard-tg-mixed | 0.861 | 0.785 | 149 | 6228 | prefer |
| DeltaKronecker-all | 0.324 | 0.375 | 8 | 6368 | observe |
| tg-oneclickvpnkeys | 0.263 | 1.0 | 1 | 192 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5085 | observe |
| Epodonios-all | 0.255 | None | 0 | 6789 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3984 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6707 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4903 | observe |
| barry-far-vless | 0.255 | None | 0 | 5131 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4027 | observe |
| nscl5-all | 0.255 | None | 0 | 3043 | observe |
| Au1rxx-clash | 0.254 | None | 0 | 1983 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | ClientOSError | - | 50 |
| cn-block | TimeoutError | - | 24 |
| 204 | TimeoutError | - | 19 |
| 204 | ProxyError | - | 11 |
| geo | TimeoutError | - | 10 |
| speed | ClientOSError | - | 10 |
| geo | ClientOSError | - | 6 |
| speed | TimeoutError | - | 6 |
| cn-block | ClientOSError | - | 5 |
| cn-block | ProxyError | - | 2 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
