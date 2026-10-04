# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-04 21:17:07 |
| 运行耗时 | 566.4s |
| 订阅源总数 | 107 |
| 健康订阅源 | 94 |
| 原始节点 | 99274 |
| 去重后节点 | 27455 |
| TCP 可达 | 3000 |
| 真实可用 | 491 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 27455 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.9 |
| geo | 1.1 |
| tcp | 45.3 |
| probe | 231.9 |
| real_test | 196.1 |
| generate | 84.1 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 59652 |
| vmess | 15671 |
| shadowsocks | 11498 |
| trojan | 10180 |
| hysteria2 | 1451 |
| http | 523 |
| shadowsocksr | 169 |
| socks | 72 |
| anytls | 27 |
| hysteria | 16 |
| tuic | 15 |

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
| 83.7 | vless | 192.3 | 493.7 | 23.33 | 0.0 | 10.0 | 11.39 | 18.98 | Au1rxx-base64 | 23.95.222.127 |
| 83.47 | vless | 202.2 | 527.9 | 23.1 | 0.0 | 10.0 | 11.39 | 18.98 | Au1rxx-base64 | 107.173.237.146 |
| 83.08 | http | 195.8 | 504.0 | 23.25 | 0.0 | 10.0 | 13.85 | 18.98 | ermaozi | 138.199.35.216 |
| 82.93 | http | 202.1 | 524.3 | 23.1 | 0.0 | 10.0 | 13.85 | 18.98 | ermaozi | 138.199.35.198 |
| 82.7 | vless | 235.2 | 571.4 | 22.33 | 0.0 | 10.0 | 11.39 | 18.98 | Au1rxx-base64 | 15.204.97.216 |
| 82.37 | vless | 249.5 | 644.8 | 22.0 | 0.0 | 10.0 | 11.39 | 18.98 | Au1rxx-base64 | 195.123.240.65 |
| 82.34 | hysteria2 | 234.1 | 581.9 | 22.36 | 0.0 | 10.0 | 12.0 | 18.98 | Au1rxx-base64 | 66.94.121.46 |
| 82.28 | hysteria2 | 226.5 | 239.6 | 22.54 | 6.02 | 9.38 | 12.0 | 18.98 | Au1rxx-base64 | open.w2m.ink |
| 81.24 | shadowsocks | 194.6 | 488.4 | 23.27 | 0.0 | 10.0 | 13.49 | 18.98 | Au1rxx-base64 | 108.181.118.10 |
| 81.22 | shadowsocks | 195.4 | 477.8 | 23.25 | 0.0 | 10.0 | 13.49 | 18.98 | Au1rxx-base64 | 108.181.0.177 |
| 81.07 | trojan | 246.4 | 573.8 | 22.07 | 0.0 | 10.0 | 13.52 | 18.98 | Au1rxx-base64 | happy-gibbon.rooster465.autos |
| 80.93 | shadowsocks | 229.8 | 543.4 | 22.46 | 0.0 | 10.0 | 13.49 | 18.98 | Au1rxx-base64 | 173.244.56.9 |
| 80.48 | shadowsocks | 227.4 | 588.6 | 22.51 | 0.0 | 10.0 | 13.49 | 18.98 | Au1rxx-base64 | 5.78.51.123 |
| 78.67 | vless | 193.5 | 497.6 | 23.3 | 0.0 | 10.0 | 11.39 | 18.98 | Au1rxx-base64 | 144.202.126.147 |
| 78.64 | vless | 410.7 | 1089.9 | 18.27 | 0.0 | 10.0 | 11.39 | 18.98 | Au1rxx-base64 | 51.81.203.63 |
| 78.06 | vless | 219.8 | 566.8 | 22.69 | 0.0 | 10.0 | 11.39 | 18.98 | Au1rxx-base64 | 45.32.69.110 |
| 77.79 | vless | 263.9 | 491.6 | 21.67 | 0.0 | 10.0 | 11.39 | 18.98 | Au1rxx-base64 | 172.64.32.103 |
| 77.77 | trojan | 302.8 | 747.8 | 20.77 | 0.0 | 10.0 | 13.52 | 18.98 | Au1rxx-base64 | guided-ferret.rooster465.autos |
| 77.47 | shadowsocks | 272.4 | 274.2 | 21.47 | 4.72 | 9.94 | 13.49 | 18.98 | Au1rxx-base64 | 149.22.87.204 |
| 77.25 | hysteria2 | 311.3 | 282.6 | 20.57 | 4.4 | 9.35 | 12.0 | 18.98 | Au1rxx-base64 | open.2ml.bid |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.969 | 0.898 | 410 | 1844 | prefer |
| mheidari-all | 0.85 | 0.776 | 85 | 23222 | prefer |
| Surfboard-tg-mixed | 0.841 | 0.773 | 44 | 7257 | prefer |
| ermaozi | 0.804 | 0.8 | 25 | 653 | prefer |
| DeltaKronecker-all | 0.335 | 1.0 | 1 | 5267 | observe |
| ermaozi-get_subscribe | 0.261 | 0.5 | 4 | 518 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5173 | observe |
| Epodonios-all | 0.255 | None | 0 | 7751 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9655 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5820 | observe |
| barry-far-vless | 0.255 | None | 0 | 6058 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4365 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |
| Au1rxx-clash | 0.249 | None | 0 | 1844 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| cn-block | TimeoutError | - | 23 |
| geo | TimeoutError | - | 10 |
| 204 | ProxyError | - | 8 |
| speed | TimeoutError | - | 8 |
| 204 | TimeoutError | - | 8 |
| geo | ClientOSError | - | 5 |
| cn-block | ClientOSError | - | 5 |
| speed | ClientOSError | - | 4 |
| 204 | ProxyConnectionError | - | 3 |
| 204 | ClientOSError | - | 3 |
| cn-block | ProxyError | - | 2 |
| speed | ProxyError | - | 1 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
