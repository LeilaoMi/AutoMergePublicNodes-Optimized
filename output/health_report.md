# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-12 07:44:53 |
| 运行耗时 | 293.5s |
| 订阅源总数 | 107 |
| 健康订阅源 | 103 |
| 原始节点 | 88266 |
| 去重后节点 | 23639 |
| TCP 可达 | 3000 |
| 真实可用 | 609 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23639 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.1 |
| geo | 1.3 |
| tcp | 35.4 |
| probe | 59.0 |
| real_test | 150.0 |
| generate | 41.7 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 51863 |
| vmess | 13955 |
| trojan | 10556 |
| shadowsocks | 10067 |
| hysteria2 | 1448 |
| http | 159 |
| socks | 100 |
| shadowsocksr | 72 |
| tuic | 18 |
| hysteria | 16 |
| anytls | 12 |

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
| 80.09 | trojan | 248.5 | 576.2 | 22.03 | 0.0 | 10.0 | 12.68 | 18.38 | Au1rxx-base64 | 64.94.95.118 |
| 79.88 | hysteria2 | 295.8 | 734.8 | 20.93 | 0.0 | 9.3 | 12.27 | 18.38 | Au1rxx-base64 | 138.124.68.188 |
| 79.79 | trojan | 261.3 | 610.9 | 21.73 | 0.0 | 10.0 | 12.68 | 18.38 | Au1rxx-base64 | 64.94.95.114 |
| 79.75 | trojan | 257.9 | 610.3 | 21.81 | 0.0 | 10.0 | 12.68 | 18.38 | Au1rxx-base64 | 64.94.95.117 |
| 79.75 | hysteria2 | 288.3 | 704.8 | 21.1 | 0.0 | 9.3 | 12.27 | 18.38 | Au1rxx-base64 | 159.223.157.129 |
| 79.34 | trojan | 261.4 | 613.4 | 21.73 | 0.0 | 10.0 | 12.68 | 18.38 | Au1rxx-base64 | 64.94.95.115 |
| 78.59 | http | 295.5 | 596.3 | 20.94 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.213 |
| 78.55 | http | 326.5 | 741.5 | 20.22 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.21 |
| 78.44 | http | 298.2 | 612.8 | 20.88 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.211 |
| 78.33 | http | 302.4 | 625.1 | 20.78 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.204 |
| 78.32 | shadowsocks | 286.7 | 693.9 | 21.14 | 0.0 | 10.0 | 13.93 | 18.38 | Au1rxx-base64 | 37.19.198.244 |
| 78.28 | http | 291.4 | 589.3 | 21.03 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.209 |
| 78.2 | shadowsocks | 282.4 | 664.7 | 21.24 | 0.0 | 10.0 | 13.93 | 18.38 | Au1rxx-base64 | 37.19.198.236 |
| 78.09 | http | 320.1 | 707.6 | 20.37 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.41 |
| 78.03 | http | 307.9 | 643.2 | 20.65 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.208 |
| 77.95 | http | 322.1 | 688.6 | 20.32 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.215 |
| 77.92 | shadowsocks | 287.3 | 694.6 | 21.13 | 0.0 | 10.0 | 13.93 | 18.38 | Au1rxx-base64 | 37.19.198.243 |
| 77.8 | http | 321.0 | 685.9 | 20.35 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.195 |
| 77.72 | http | 320.6 | 702.8 | 20.36 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.9 |
| 77.65 | http | 315.3 | 670.5 | 20.48 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.212 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.999 | 1.0 | 128 | 159 | prefer |
| Au1rxx-base64 | 0.908 | 0.845 | 412 | 1632 | prefer |
| Surfboard-tg-mixed | 0.682 | 0.604 | 101 | 5943 | observe |
| DeltaKronecker-all | 0.535 | 0.45 | 20 | 4975 | observe |
| xiaoji235-airport-v2ray-all | 0.391 | 1.0 | 2 | 4568 | observe |
| 10ium-ScrapeCategorize-Vless | 0.335 | 1.0 | 1 | 5328 | observe |
| nscl5-all | 0.314 | 1.0 | 1 | 1481 | observe |
| mheidari-all | 0.308 | 0.226 | 252 | 20330 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| Epodonios-all | 0.255 | None | 0 | 6602 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7652 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4919 | observe |
| barry-far-vless | 0.255 | None | 0 | 5267 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5196 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | ClientOSError | - | 93 |
| geo | TimeoutError | - | 93 |
| speed | TimeoutError | - | 47 |
| speed | ClientOSError | - | 32 |
| 204 | TimeoutError | - | 14 |
| 204 | ProxyError | - | 14 |
| cn-block | TimeoutError | - | 13 |
| 204 | ClientOSError | - | 4 |
| cn-block | ProxyError | - | 1 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
