# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-06 03:16:18 |
| 运行耗时 | 245.2s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 88953 |
| 去重后节点 | 24594 |
| TCP 可达 | 3000 |
| 真实可用 | 511 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 24594 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 8.7 |
| geo | 1.4 |
| tcp | 37.5 |
| probe | 53.6 |
| real_test | 116.5 |
| generate | 27.5 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 52785 |
| vmess | 13279 |
| trojan | 11114 |
| shadowsocks | 10122 |
| hysteria2 | 1392 |
| socks | 108 |
| shadowsocksr | 72 |
| http | 24 |
| anytls | 22 |
| hysteria | 21 |
| tuic | 14 |

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
| 80.93 | shadowsocks | 244.7 | 621.3 | 22.11 | 0.0 | 10.0 | 13.2 | 19.62 | Au1rxx-base64 | 156.146.38.169 |
| 80.93 | http | 247.9 | 547.8 | 22.04 | 0.0 | 10.0 | 14.32 | 19.12 | zhangkai | 138.199.35.214 |
| 80.89 | shadowsocks | 246.7 | 622.6 | 22.07 | 0.0 | 10.0 | 13.2 | 19.62 | Au1rxx-base64 | 156.146.38.168 |
| 80.44 | http | 252.2 | 571.5 | 21.94 | 0.0 | 10.0 | 14.32 | 19.12 | zhangkai | 138.199.35.207 |
| 80.33 | http | 264.2 | 529.8 | 21.66 | 0.0 | 10.0 | 14.32 | 19.12 | zhangkai | 138.199.35.199 |
| 80.13 | shadowsocks | 248.1 | 636.8 | 22.03 | 0.0 | 10.0 | 13.2 | 19.62 | Au1rxx-base64 | 156.146.38.167 |
| 79.32 | http | 240.3 | 531.6 | 22.22 | 0.0 | 10.0 | 14.32 | 19.12 | zhangkai | 138.199.35.217 |
| 78.94 | hysteria2 | 308.8 | 692.3 | 20.63 | 0.0 | 10.0 | 11.74 | 19.62 | Au1rxx-base64 | 159.223.157.129 |
| 78.65 | hysteria2 | 316.1 | 715.9 | 20.46 | 0.0 | 10.0 | 11.74 | 19.62 | Au1rxx-base64 | 138.124.68.188 |
| 78.51 | shadowsocks | 243.7 | 614.5 | 22.14 | 0.0 | 10.0 | 13.2 | 19.62 | Au1rxx-base64 | 156.146.38.170 |
| 78.48 | trojan | 294.7 | 575.8 | 20.96 | 0.0 | 10.0 | 14.45 | 19.62 | Au1rxx-base64 | 44.244.3.114 |
| 77.93 | trojan | 298.9 | 602.4 | 20.86 | 0.0 | 10.0 | 14.45 | 19.62 | Au1rxx-base64 | 35.91.251.124 |
| 77.1 | trojan | 466.6 | 1214.6 | 16.98 | 0.0 | 10.0 | 14.45 | 19.62 | Au1rxx-base64 | 163.245.196.68 |
| 77.08 | trojan | 295.3 | 552.2 | 20.94 | 0.0 | 8.76 | 14.45 | 19.62 | Au1rxx-base64 | fleet-bonefish.rooster465.autos |
| 76.68 | shadowsocks | 266.3 | 530.9 | 21.61 | 0.0 | 10.0 | 13.2 | 19.62 | Au1rxx-base64 | 108.181.0.177 |
| 76.44 | trojan | 381.4 | 835.3 | 18.95 | 0.0 | 10.0 | 14.45 | 19.62 | Au1rxx-base64 | 44.246.163.102 |
| 76.29 | trojan | 393.5 | 887.1 | 18.67 | 0.0 | 10.0 | 14.45 | 19.62 | Au1rxx-base64 | 44.242.235.129 |
| 75.78 | shadowsocks | 306.9 | 292.2 | 20.67 | 4.04 | 9.76 | 13.2 | 19.62 | Au1rxx-base64 | 149.22.87.241 |
| 75.66 | hysteria2 | 319.9 | 741.8 | 20.37 | 0.0 | 7.72 | 11.74 | 19.62 | Au1rxx-base64 | usa1.spectrumproxy.shop |
| 75.37 | trojan | 359.0 | 763.7 | 19.47 | 0.0 | 10.0 | 14.45 | 19.62 | Au1rxx-base64 | 153.75.250.171 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | 0.954 | 368 | 1385 | prefer |
| zhangkai | 0.789 | 1.0 | 15 | 25 | prefer |
| Surfboard-tg-mixed | 0.655 | 0.576 | 191 | 5908 | observe |
| xiaoji235-airport-v2ray-all | 0.391 | 1.0 | 2 | 5214 | observe |
| mheidari-all | 0.271 | 0.187 | 134 | 21048 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5260 | observe |
| Epodonios-all | 0.255 | None | 0 | 6515 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7399 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4791 | observe |
| barry-far-vless | 0.255 | None | 0 | 5104 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5206 | observe |
| DeltaKronecker-all | 0.247 | 0.15 | 40 | 5316 | downweight |
| Au1rxx-clash | 0.23 | None | 0 | 1385 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 120 |
| speed | TimeoutError | - | 34 |
| speed | ClientOSError | - | 31 |
| geo | ClientOSError | - | 25 |
| cn-block | TimeoutError | - | 19 |
| 204 | TimeoutError | - | 11 |
| cn-block | ProxyError | - | 2 |
| 204 | ProxyError | - | 2 |
| 204 | ClientOSError | - | 2 |
| cn-block | ClientOSError | - | 1 |
| geo | status | 403 | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
