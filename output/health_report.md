# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-26 19:24:44 |
| 运行耗时 | 346.4s |
| 订阅源总数 | 107 |
| 健康订阅源 | 102 |
| 原始节点 | 83971 |
| 去重后节点 | 22078 |
| TCP 可达 | 3000 |
| 真实可用 | 725 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22078 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.1 |
| geo | 1.3 |
| tcp | 32.3 |
| probe | 75.0 |
| real_test | 189.0 |
| generate | 42.7 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 46656 |
| trojan | 16109 |
| shadowsocks | 10268 |
| vmess | 10068 |
| hysteria2 | 565 |
| shadowsocksr | 106 |
| http | 83 |
| socks | 70 |
| anytls | 21 |
| hysteria | 15 |
| tuic | 10 |

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
| 80.62 | shadowsocks | 208.0 | 559.8 | 22.96 | 0.0 | 10.0 | 12.06 | 19.6 | Au1rxx-base64 | 149.22.95.183 |
| 78.24 | trojan | 303.2 | 310.0 | 20.76 | 3.37 | 10.0 | 14.2 | 19.6 | Au1rxx-base64 | 31.223.184.218 |
| 78.2 | trojan | 307.6 | 308.4 | 20.66 | 3.44 | 10.0 | 14.2 | 19.6 | Au1rxx-base64 | 31.223.184.164 |
| 78.17 | trojan | 321.2 | 296.4 | 20.34 | 3.89 | 10.0 | 14.2 | 19.6 | Au1rxx-base64 | 95.85.94.96 |
| 78.13 | trojan | 305.1 | 312.7 | 20.72 | 3.27 | 10.0 | 14.2 | 19.6 | Au1rxx-base64 | 31.223.184.109 |
| 78.05 | trojan | 305.1 | 314.1 | 20.71 | 3.22 | 10.0 | 14.2 | 19.6 | Au1rxx-base64 | 31.223.184.43 |
| 77.99 | trojan | 305.6 | 313.6 | 20.7 | 3.24 | 10.0 | 14.2 | 19.6 | Au1rxx-base64 | 31.223.184.125 |
| 77.88 | trojan | 307.9 | 316.3 | 20.65 | 3.14 | 10.0 | 14.2 | 19.6 | Au1rxx-base64 | 31.223.184.178 |
| 77.85 | trojan | 307.1 | 318.5 | 20.67 | 3.06 | 10.0 | 14.2 | 19.6 | Au1rxx-base64 | 31.223.184.249 |
| 77.68 | shadowsocks | 256.5 | 265.4 | 21.84 | 5.05 | 10.0 | 12.06 | 19.6 | Au1rxx-base64 | 149.22.87.240 |
| 77.63 | trojan | 303.8 | 312.2 | 20.75 | 3.29 | 9.52 | 14.2 | 19.6 | Au1rxx-base64 | next-ringtail.rooster465.autos |
| 77.53 | trojan | 306.4 | 315.5 | 20.69 | 3.17 | 9.54 | 14.2 | 19.6 | Au1rxx-base64 | inspired-hound.rooster465.autos |
| 77.04 | trojan | 312.4 | 336.2 | 20.55 | 2.39 | 9.99 | 14.2 | 19.6 | Au1rxx-base64 | 95.85.94.199 |
| 76.08 | trojan | 304.8 | 313.5 | 20.72 | 3.24 | 10.0 | 14.2 | 19.6 | Au1rxx-base64 | 31.223.184.58 |
| 75.83 | trojan | 309.1 | 316.1 | 20.62 | 3.14 | 10.0 | 14.2 | 19.6 | Au1rxx-base64 | 95.85.94.185 |
| 75.78 | shadowsocks | 256.2 | 558.8 | 21.85 | 0.0 | 10.0 | 12.06 | 19.6 | Au1rxx-base64 | 173.244.56.6 |
| 75.24 | shadowsocks | 292.4 | 637.2 | 21.01 | 0.0 | 10.0 | 12.06 | 19.6 | Au1rxx-base64 | 108.181.0.177 |
| 75.15 | trojan | 303.5 | 310.7 | 20.75 | 3.35 | 10.0 | 14.2 | 19.6 | Au1rxx-base64 | 95.85.94.137 |
| 75.14 | trojan | 326.1 | 379.1 | 20.23 | 0.78 | 10.0 | 14.2 | 19.6 | Au1rxx-base64 | 95.85.94.142 |
| 75.04 | shadowsocks | 274.2 | 324.2 | 21.43 | 2.84 | 10.0 | 12.06 | 19.6 | Au1rxx-base64 | 149.22.87.204 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.991 | 1.0 | 76 | 86 | prefer |
| Au1rxx-base64 | 0.978 | 0.92 | 435 | 1507 | prefer |
| mheidari-all | 0.858 | 0.784 | 97 | 19379 | prefer |
| tg-oneclickvpnkeys | 0.456 | 0.857 | 7 | 164 | observe |
| Surfboard-tg-mixed | 0.423 | 0.338 | 65 | 5460 | observe |
| DeltaKronecker-all | 0.383 | 0.302 | 474 | 4320 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| xiaoji235-airport-v2ray-all | 0.259 | 0.333 | 3 | 3959 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4912 | observe |
| Epodonios-all | 0.255 | None | 0 | 6631 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3974 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6557 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4238 | observe |
| barry-far-vless | 0.255 | None | 0 | 4894 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5003 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 145 |
| geo | TimeoutError | - | 99 |
| 204 | ProxyError | - | 54 |
| geo | ClientOSError | - | 41 |
| 204 | TimeoutError | - | 40 |
| cn-block | TimeoutError | - | 21 |
| speed | TimeoutError | - | 13 |
| 204 | ClientOSError | - | 8 |
| cn-block | ClientOSError | - | 8 |
| cn-block | ProxyError | - | 4 |
| speed | ProxyError | - | 1 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
