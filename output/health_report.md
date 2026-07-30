# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-30 02:51:14 |
| 运行耗时 | 261.0s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 77441 |
| 去重后节点 | 22597 |
| TCP 可达 | 3000 |
| 真实可用 | 582 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22597 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.2 |
| geo | 1.4 |
| tcp | 31.4 |
| probe | 52.5 |
| real_test | 133.7 |
| generate | 34.8 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 45293 |
| vmess | 11147 |
| shadowsocks | 10409 |
| trojan | 9796 |
| hysteria2 | 530 |
| shadowsocksr | 78 |
| http | 73 |
| socks | 67 |
| anytls | 26 |
| hysteria | 14 |
| tuic | 8 |

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
| 77.59 | hysteria2 | 258.1 | 660.4 | 21.8 | 0.0 | 10.0 | 10.59 | 16.3 | Au1rxx-base64 | 159.223.157.129 |
| 76.03 | hysteria2 | 272.5 | 691.0 | 21.47 | 0.0 | 8.67 | 10.59 | 16.3 | Au1rxx-base64 | usa1.spectrumproxy.shop |
| 75.15 | shadowsocks | 265.3 | 658.9 | 21.64 | 0.0 | 10.0 | 11.21 | 16.3 | Au1rxx-base64 | 37.19.198.236 |
| 75.02 | shadowsocks | 270.7 | 677.5 | 21.51 | 0.0 | 10.0 | 11.21 | 16.3 | Au1rxx-base64 | 37.19.198.243 |
| 74.72 | trojan | 382.7 | 1066.5 | 18.92 | 0.0 | 10.0 | 12.5 | 16.3 | Au1rxx-base64 | 148.72.168.35 |
| 74.58 | trojan | 282.3 | 629.3 | 21.24 | 0.0 | 10.0 | 12.5 | 16.3 | Au1rxx-base64 | 163.245.196.68 |
| 74.4 | shadowsocks | 258.0 | 629.2 | 21.81 | 0.0 | 10.0 | 11.21 | 16.3 | Au1rxx-base64 | 156.146.38.169 |
| 74.36 | shadowsocks | 263.3 | 643.1 | 21.68 | 0.0 | 10.0 | 11.21 | 16.3 | Au1rxx-base64 | 156.146.38.168 |
| 74.32 | shadowsocks | 300.9 | 785.3 | 20.81 | 0.0 | 10.0 | 11.21 | 16.3 | Au1rxx-base64 | 198.98.53.130 |
| 73.77 | shadowsocks | 303.0 | 786.9 | 20.76 | 0.0 | 10.0 | 11.21 | 16.3 | Au1rxx-base64 | 185.196.61.82 |
| 73.58 | shadowsocks | 292.2 | 705.2 | 21.01 | 0.0 | 10.0 | 11.21 | 16.3 | Au1rxx-base64 | 68.168.222.210 |
| 73.53 | vless | 291.0 | 681.0 | 21.04 | 0.0 | 10.0 | 10.0 | 14.44 | Surfboard-tg-mixed | 45.206.5.122 |
| 73.08 | shadowsocks | 323.8 | 804.6 | 20.28 | 0.0 | 10.0 | 11.21 | 16.3 | Au1rxx-base64 | 72.10.173.91 |
| 72.79 | trojan | 346.8 | 881.6 | 19.75 | 0.0 | 10.0 | 12.5 | 14.24 | DeltaKronecker-all | 64.74.163.118 |
| 72.76 | shadowsocks | 329.1 | 841.0 | 20.16 | 0.0 | 10.0 | 11.21 | 16.3 | Au1rxx-base64 | 68.168.114.226 |
| 72.68 | shadowsocks | 335.9 | 831.6 | 20.0 | 0.0 | 10.0 | 11.21 | 16.3 | Au1rxx-base64 | 68.168.116.6 |
| 72.54 | shadowsocks | 356.1 | 884.9 | 19.53 | 0.0 | 10.0 | 11.21 | 16.3 | Au1rxx-base64 | 146.70.34.226 |
| 72.46 | shadowsocks | 350.4 | 892.0 | 19.67 | 0.0 | 10.0 | 11.21 | 16.3 | Au1rxx-base64 | 156.146.38.167 |
| 72.07 | trojan | 449.2 | 1165.5 | 17.38 | 0.0 | 10.0 | 12.5 | 16.3 | Au1rxx-base64 | 64.94.95.115 |
| 71.81 | trojan | 444.1 | 1149.9 | 17.5 | 0.0 | 10.0 | 12.5 | 16.3 | Au1rxx-base64 | 64.94.95.117 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.989 | 1.0 | 70 | 84 | prefer |
| Au1rxx-base64 | 0.971 | 0.924 | 290 | 1255 | prefer |
| Surfboard-tg-mixed | 0.716 | 0.638 | 174 | 5390 | prefer |
| mheidari-all | 0.447 | 0.357 | 28 | 16333 | observe |
| DeltaKronecker-all | 0.426 | 0.345 | 348 | 5519 | observe |
| 10ium-ScrapeCategorize-Vless | 0.335 | 1.0 | 1 | 5118 | observe |
| xiaoji235-airport-v2ray-all | 0.282 | 0.5 | 2 | 1861 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| Epodonios-all | 0.255 | None | 0 | 6124 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6420 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4279 | observe |
| barry-far-vless | 0.255 | None | 0 | 4688 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5076 | observe |
| Au1rxx-clash | 0.225 | None | 0 | 1255 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 186 |
| geo | ClientOSError | - | 41 |
| speed | TimeoutError | - | 39 |
| speed | ClientOSError | - | 28 |
| cn-block | TimeoutError | - | 21 |
| 204 | ProxyError | - | 8 |
| 204 | TimeoutError | - | 6 |
| cn-block | ClientOSError | - | 3 |
| 204 | ClientOSError | - | 2 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
