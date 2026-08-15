# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-15 12:52:51 |
| 运行耗时 | 327.2s |
| 订阅源总数 | 107 |
| 健康订阅源 | 100 |
| 原始节点 | 77456 |
| 去重后节点 | 22403 |
| TCP 可达 | 3000 |
| 真实可用 | 1031 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22403 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 11.6 |
| geo | 1.0 |
| tcp | 34.7 |
| probe | 66.7 |
| real_test | 187.8 |
| generate | 25.2 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 42730 |
| trojan | 12245 |
| vmess | 10509 |
| shadowsocks | 10217 |
| hysteria2 | 1403 |
| http | 188 |
| socks | 75 |
| shadowsocksr | 74 |
| tuic | 8 |
| hysteria | 7 |

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
| 82.61 | http | 241.8 | 539.2 | 22.18 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.214 |
| 82.38 | http | 242.8 | 536.5 | 22.16 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.215 |
| 82.23 | shadowsocks | 240.1 | 618.9 | 22.22 | 0.0 | 10.0 | 14.01 | 20.0 | Au1rxx-base64 | 156.146.38.168 |
| 82.21 | shadowsocks | 241.0 | 600.8 | 22.2 | 0.0 | 10.0 | 14.01 | 20.0 | Au1rxx-base64 | 156.146.38.169 |
| 82.06 | shadowsocks | 247.5 | 617.8 | 22.05 | 0.0 | 10.0 | 14.01 | 20.0 | Au1rxx-base64 | 156.146.38.170 |
| 82.06 | http | 264.2 | 598.7 | 21.66 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.213 |
| 82.05 | http | 261.0 | 596.9 | 21.74 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.204 |
| 81.92 | http | 263.1 | 595.2 | 21.69 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.206 |
| 81.75 | http | 263.8 | 598.0 | 21.67 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.197 |
| 81.71 | http | 263.0 | 596.9 | 21.69 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.220 |
| 81.7 | http | 257.2 | 587.8 | 21.82 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.211 |
| 81.55 | http | 255.5 | 575.8 | 21.86 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.199 |
| 81.46 | http | 254.3 | 577.1 | 21.89 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.195 |
| 81.32 | http | 258.4 | 585.2 | 21.8 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.208 |
| 81.27 | hysteria2 | 274.6 | 613.5 | 21.42 | 0.0 | 10.0 | 12.0 | 20.0 | Au1rxx-base64 | 150.241.102.127 |
| 81.26 | http | 259.6 | 585.6 | 21.77 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.210 |
| 81.16 | http | 261.2 | 597.0 | 21.73 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.212 |
| 81.01 | http | 258.5 | 594.1 | 21.79 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.209 |
| 79.04 | shadowsocks | 356.4 | 884.4 | 19.53 | 0.0 | 10.0 | 14.01 | 20.0 | Au1rxx-base64 | 23.150.248.20 |
| 78.68 | hysteria2 | 316.8 | 713.7 | 20.44 | 0.0 | 10.0 | 12.0 | 20.0 | Au1rxx-base64 | 159.223.157.129 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | 0.971 | 734 | 1659 | prefer |
| zhangkai | 0.999 | 1.0 | 127 | 159 | prefer |
| mheidari-all | 0.982 | 0.918 | 49 | 15977 | prefer |
| Surfboard-tg-mixed | 0.798 | 0.722 | 115 | 5656 | prefer |
| DeltaKronecker-all | 0.778 | 0.702 | 84 | 5773 | prefer |
| nscl5-all | 0.349 | 0.667 | 3 | 2081 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| tg-oneclickvpnkeys | 0.261 | 1.0 | 1 | 160 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5113 | observe |
| Epodonios-all | 0.255 | None | 0 | 6303 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7258 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4372 | observe |
| barry-far-vless | 0.255 | None | 0 | 4711 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 3935 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | TimeoutError | - | 24 |
| geo | TimeoutError | - | 15 |
| cn-block | TimeoutError | - | 13 |
| speed | TimeoutError | - | 12 |
| geo | ClientOSError | - | 10 |
| cn-block | ClientOSError | - | 4 |
| 204 | ClientOSError | - | 3 |
| cn-block | ProxyError | - | 1 |
| 204 | ProxyError | - | 1 |
| speed | ClientOSError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
