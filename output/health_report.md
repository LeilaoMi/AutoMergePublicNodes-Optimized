# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-06-24 09:45:24 |
| 运行耗时 | 259.4s |
| 订阅源总数 | 107 |
| 健康订阅源 | 105 |
| 原始节点 | 76985 |
| 去重后节点 | 22299 |
| TCP 可达 | 3000 |
| 真实可用 | 414 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22299 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 3.7 |
| geo | 1.4 |
| tcp | 29.3 |
| probe | 57.6 |
| real_test | 124.3 |
| generate | 43.1 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 45441 |
| trojan | 10764 |
| vmess | 10283 |
| shadowsocks | 9862 |
| hysteria2 | 233 |
| shadowsocksr | 164 |
| http | 161 |
| socks | 69 |
| hysteria | 6 |
| tuic | 2 |

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
| 78.67 | shadowsocks | 217.4 | 514.3 | 22.75 | 0.0 | 10.0 | 14.0 | 15.92 | Au1rxx-base64 | 149.22.95.183 |
| 78.59 | vless | 242.4 | 551.1 | 22.17 | 0.0 | 10.0 | 8.84 | 18.08 | mheidari-all | 34.213.172.16 |
| 78.44 | shadowsocks | 227.2 | 517.3 | 22.52 | 0.0 | 10.0 | 14.0 | 15.92 | Au1rxx-base64 | 173.244.56.9 |
| 76.21 | trojan | 352.0 | 833.1 | 19.63 | 0.0 | 10.0 | 11.0 | 18.08 | mheidari-all | 45.61.58.89 |
| 75.87 | shadowsocks | 251.7 | 630.2 | 21.95 | 0.0 | 10.0 | 14.0 | 15.92 | Au1rxx-base64 | 173.244.56.6 |
| 75.3 | vless | 312.5 | 824.7 | 20.54 | 0.0 | 10.0 | 8.84 | 15.92 | Au1rxx-base64 | 15.204.97.214 |
| 75.2 | vless | 317.0 | 838.7 | 20.44 | 0.0 | 10.0 | 8.84 | 15.92 | Au1rxx-base64 | 15.204.97.219 |
| 74.88 | shadowsocks | 359.2 | 976.5 | 19.46 | 0.0 | 10.0 | 14.0 | 15.92 | Au1rxx-base64 | 108.181.0.177 |
| 74.39 | shadowsocks | 288.7 | 647.7 | 21.09 | 0.0 | 10.0 | 14.0 | 15.92 | Au1rxx-base64 | 156.146.38.170 |
| 73.48 | shadowsocks | 292.4 | 652.2 | 21.01 | 0.0 | 10.0 | 14.0 | 15.92 | Au1rxx-base64 | 156.146.38.169 |
| 73.45 | shadowsocks | 294.5 | 662.9 | 20.96 | 0.0 | 10.0 | 14.0 | 15.92 | Au1rxx-base64 | 156.146.38.167 |
| 73.11 | shadowsocks | 296.6 | 671.7 | 20.91 | 0.0 | 10.0 | 14.0 | 15.92 | Au1rxx-base64 | 156.146.38.168 |
| 72.61 | shadowsocks | 457.3 | 1263.3 | 17.19 | 0.0 | 10.0 | 14.0 | 15.92 | Au1rxx-base64 | 108.181.118.10 |
| 72.3 | trojan | 427.8 | 1068.5 | 17.88 | 0.0 | 10.0 | 11.0 | 15.92 | Au1rxx-base64 | 45.61.52.243 |
| 72.16 | shadowsocks | 351.9 | 688.7 | 19.63 | 0.0 | 10.0 | 14.0 | 18.08 | mheidari-all | 198.98.53.130 |
| 71.78 | shadowsocks | 295.2 | 338.8 | 20.95 | 2.3 | 9.89 | 14.0 | 15.92 | Au1rxx-base64 | 149.22.87.240 |
| 71.19 | shadowsocks | 300.5 | 349.2 | 20.82 | 1.9 | 9.89 | 14.0 | 15.92 | Au1rxx-base64 | 149.22.87.241 |
| 70.43 | shadowsocks | 306.3 | 368.7 | 20.69 | 1.18 | 9.84 | 14.0 | 15.92 | Au1rxx-base64 | 149.22.87.204 |
| 69.75 | shadowsocks | 177.5 | 484.4 | 23.67 | 0.0 | 10.0 | 14.0 | 13.16 | DeltaKronecker-all | 107.172.219.230 |
| 69.25 | shadowsocks | 374.1 | 758.7 | 19.12 | 0.0 | 10.0 | 14.0 | 15.92 | Au1rxx-base64 | 37.19.198.244 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.984 | 1.0 | 50 | 73 | prefer |
| Surfboard-tg-mixed | 0.778 | 0.7 | 243 | 5405 | prefer |
| Au1rxx-base64 | 0.766 | 0.769 | 65 | 117 | prefer |
| mheidari-all | 0.622 | 0.543 | 164 | 15611 | observe |
| DeltaKronecker-all | 0.504 | 0.423 | 123 | 6644 | observe |
| Barabama-yudou | 0.318 | 1.0 | 2 | 166 | observe |
| nscl5-all | 0.301 | 1.0 | 1 | 1140 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4745 | observe |
| Epodonios-all | 0.255 | None | 0 | 8238 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3980 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7317 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4121 | observe |
| barry-far-vless | 0.255 | None | 0 | 4922 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4710 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 70 |
| 204 | TimeoutError | - | 34 |
| geo | TimeoutError | - | 26 |
| cn-block | TimeoutError | - | 24 |
| 204 | ProxyError | - | 21 |
| 204 | ClientOSError | - | 16 |
| geo | ClientOSError | - | 14 |
| cn-block | ProxyError | - | 7 |
| cn-block | ClientOSError | - | 7 |
| speed | TimeoutError | - | 7 |
| geo | ProxyError | - | 6 |
| speed | ProxyError | - | 3 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
