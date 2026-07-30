# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-30 08:40:47 |
| 运行耗时 | 274.1s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 78173 |
| 去重后节点 | 22773 |
| TCP 可达 | 3000 |
| 真实可用 | 507 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22773 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.1 |
| geo | 1.3 |
| tcp | 31.6 |
| probe | 55.3 |
| real_test | 143.7 |
| generate | 36.0 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 45723 |
| vmess | 11317 |
| shadowsocks | 10454 |
| trojan | 9828 |
| hysteria2 | 535 |
| http | 121 |
| shadowsocksr | 75 |
| socks | 61 |
| anytls | 26 |
| tuic | 19 |
| hysteria | 14 |

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
| 82.22 | shadowsocks | 182.1 | 480.0 | 23.56 | 0.0 | 10.0 | 13.74 | 19.42 | Au1rxx-base64 | 185.236.200.210 |
| 81.95 | shadowsocks | 194.0 | 486.2 | 23.29 | 0.0 | 10.0 | 13.74 | 19.42 | Au1rxx-base64 | 108.181.0.177 |
| 81.87 | http | 193.6 | 502.2 | 23.3 | 0.0 | 10.0 | 14.79 | 19.78 | zhangkai | 138.199.35.196 |
| 81.84 | shadowsocks | 198.8 | 494.2 | 23.18 | 0.0 | 10.0 | 13.74 | 19.42 | Au1rxx-base64 | 108.181.118.10 |
| 81.07 | shadowsocks | 210.2 | 499.6 | 22.91 | 0.0 | 10.0 | 13.74 | 19.42 | Au1rxx-base64 | 173.244.56.9 |
| 81.0 | shadowsocks | 256.6 | 636.1 | 21.84 | 0.0 | 10.0 | 13.74 | 19.42 | Au1rxx-base64 | 156.146.38.169 |
| 80.98 | shadowsocks | 257.4 | 628.2 | 21.82 | 0.0 | 10.0 | 13.74 | 19.42 | Au1rxx-base64 | 156.146.38.168 |
| 80.92 | shadowsocks | 259.8 | 635.3 | 21.76 | 0.0 | 10.0 | 13.74 | 19.42 | Au1rxx-base64 | 156.146.38.167 |
| 80.21 | shadowsocks | 268.5 | 645.8 | 21.56 | 0.0 | 10.0 | 13.74 | 19.42 | Au1rxx-base64 | 156.146.38.195 |
| 79.92 | http | 191.2 | 495.1 | 23.35 | 0.0 | 10.0 | 14.79 | 19.78 | zhangkai | 138.199.35.207 |
| 79.87 | http | 193.6 | 485.5 | 23.3 | 0.0 | 10.0 | 14.79 | 19.78 | zhangkai | 138.199.35.198 |
| 79.86 | http | 194.1 | 502.5 | 23.29 | 0.0 | 10.0 | 14.79 | 19.78 | zhangkai | 138.199.35.218 |
| 79.84 | http | 194.9 | 489.7 | 23.27 | 0.0 | 10.0 | 14.79 | 19.78 | zhangkai | 138.199.35.217 |
| 79.82 | http | 195.4 | 503.9 | 23.25 | 0.0 | 10.0 | 14.79 | 19.78 | zhangkai | 138.199.35.206 |
| 79.81 | http | 196.0 | 495.9 | 23.24 | 0.0 | 10.0 | 14.79 | 19.78 | zhangkai | 138.199.35.205 |
| 79.8 | http | 196.3 | 499.3 | 23.23 | 0.0 | 10.0 | 14.79 | 19.78 | zhangkai | 138.199.35.202 |
| 79.79 | http | 196.9 | 497.9 | 23.22 | 0.0 | 10.0 | 14.79 | 19.78 | zhangkai | 138.199.35.209 |
| 79.77 | http | 197.7 | 503.3 | 23.2 | 0.0 | 10.0 | 14.79 | 19.78 | zhangkai | 138.199.35.213 |
| 79.77 | http | 197.9 | 494.1 | 23.2 | 0.0 | 10.0 | 14.79 | 19.78 | zhangkai | 138.199.35.216 |
| 79.72 | http | 199.8 | 503.2 | 23.15 | 0.0 | 10.0 | 14.79 | 19.78 | zhangkai | 138.199.35.212 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.998 | 1.0 | 118 | 157 | prefer |
| Au1rxx-base64 | 0.88 | 0.835 | 266 | 1201 | prefer |
| Surfboard-tg-mixed | 0.645 | 0.565 | 168 | 5473 | observe |
| DeltaKronecker-all | 0.637 | 0.558 | 95 | 5759 | observe |
| mheidari-all | 0.455 | 0.37 | 46 | 16105 | observe |
| xiaoji235-airport-v2ray-all | 0.329 | 1.0 | 1 | 1861 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5342 | observe |
| Epodonios-all | 0.255 | None | 0 | 6219 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6833 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4282 | observe |
| barry-far-vless | 0.255 | None | 0 | 4657 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5029 | observe |
| Au1rxx-clash | 0.223 | None | 0 | 1201 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 66 |
| cn-block | TimeoutError | - | 29 |
| 204 | TimeoutError | - | 23 |
| speed | TimeoutError | - | 21 |
| speed | ClientOSError | - | 17 |
| 204 | ProxyError | - | 12 |
| geo | ClientOSError | - | 10 |
| 204 | ClientOSError | - | 7 |
| cn-block | ClientOSError | - | 6 |
| cn-block | ProxyError | - | 1 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
