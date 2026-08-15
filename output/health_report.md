# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-15 18:42:13 |
| 运行耗时 | 351.6s |
| 订阅源总数 | 107 |
| 健康订阅源 | 99 |
| 原始节点 | 78636 |
| 去重后节点 | 22463 |
| TCP 可达 | 3000 |
| 真实可用 | 1055 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22463 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 10.7 |
| geo | 0.8 |
| tcp | 34.6 |
| probe | 74.1 |
| real_test | 189.5 |
| generate | 41.9 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 43064 |
| trojan | 13402 |
| vmess | 10700 |
| shadowsocks | 10037 |
| hysteria2 | 1069 |
| http | 189 |
| socks | 82 |
| shadowsocksr | 76 |
| tuic | 10 |
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
| 84.02 | hysteria2 | 256.0 | 551.7 | 21.85 | 0.0 | 9.11 | 14.06 | 20.0 | Au1rxx-base64 | 150.241.102.127 |
| 83.17 | trojan | 250.6 | 610.3 | 21.98 | 0.0 | 10.0 | 14.55 | 19.64 | mheidari-all | 64.94.95.118 |
| 82.69 | http | 241.3 | 527.1 | 22.19 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.206 |
| 82.52 | http | 247.3 | 544.4 | 22.05 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.215 |
| 82.51 | http | 244.2 | 530.9 | 22.12 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.204 |
| 82.25 | http | 248.8 | 535.3 | 22.02 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.197 |
| 82.13 | shadowsocks | 253.6 | 603.4 | 21.91 | 0.0 | 10.0 | 14.22 | 20.0 | Au1rxx-base64 | 156.146.38.170 |
| 82.06 | http | 255.3 | 562.4 | 21.87 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.211 |
| 82.06 | shadowsocks | 256.7 | 598.3 | 21.84 | 0.0 | 10.0 | 14.22 | 20.0 | Au1rxx-base64 | 156.146.38.168 |
| 81.72 | http | 255.1 | 558.1 | 21.87 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.195 |
| 81.61 | http | 243.0 | 532.2 | 22.15 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.199 |
| 81.55 | http | 245.6 | 535.5 | 22.09 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.220 |
| 81.38 | hysteria2 | 313.1 | 696.6 | 20.53 | 0.0 | 10.0 | 14.06 | 20.0 | Au1rxx-base64 | 159.223.157.129 |
| 81.35 | hysteria2 | 354.9 | 695.8 | 19.56 | 0.0 | 10.0 | 14.06 | 20.0 | Au1rxx-base64 | 138.124.68.188 |
| 81.14 | http | 243.8 | 530.1 | 22.13 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.210 |
| 80.88 | http | 235.9 | 517.8 | 22.32 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.209 |
| 80.65 | http | 243.9 | 534.1 | 22.13 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.212 |
| 80.46 | http | 240.5 | 519.0 | 22.21 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.213 |
| 79.96 | http | 245.2 | 531.3 | 22.1 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.214 |
| 79.78 | http | 249.6 | 546.5 | 22.0 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.208 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | 0.967 | 699 | 1997 | prefer |
| zhangkai | 0.999 | 1.0 | 127 | 159 | prefer |
| mheidari-all | 0.951 | 0.875 | 192 | 16339 | prefer |
| Surfboard-tg-mixed | 0.896 | 0.824 | 74 | 5684 | prefer |
| DeltaKronecker-all | 0.663 | 0.588 | 34 | 5773 | observe |
| nscl5-all | 0.349 | 0.667 | 3 | 2081 | observe |
| tg-oneclickvpnkeys | 0.261 | 1.0 | 1 | 160 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5113 | observe |
| Au1rxx-clash | 0.255 | None | 0 | 1997 | observe |
| Epodonios-all | 0.255 | None | 0 | 6266 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3996 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7464 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4350 | observe |
| barry-far-vless | 0.255 | None | 0 | 4694 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 3935 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | TimeoutError | - | 19 |
| speed | TimeoutError | - | 13 |
| cn-block | TimeoutError | - | 9 |
| 204 | ClientOSError | - | 7 |
| geo | TimeoutError | - | 7 |
| cn-block | ClientOSError | - | 6 |
| geo | ClientOSError | - | 5 |
| speed | ClientOSError | - | 4 |
| 204 | ProxyError | - | 4 |
| cn-block | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
