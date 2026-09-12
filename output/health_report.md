# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-12 04:17:57 |
| 运行耗时 | 917.9s |
| 订阅源总数 | 107 |
| 健康订阅源 | 94 |
| 原始节点 | 83274 |
| 去重后节点 | 23411 |
| TCP 可达 | 3000 |
| 真实可用 | 546 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23411 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.0 |
| geo | 1.4 |
| tcp | 40.5 |
| probe | 367.3 |
| real_test | 426.4 |
| generate | 77.3 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 50326 |
| vmess | 12500 |
| shadowsocks | 9778 |
| trojan | 8118 |
| hysteria2 | 1692 |
| http | 661 |
| shadowsocksr | 120 |
| socks | 54 |
| tuic | 12 |
| hysteria | 11 |
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
| 83.24 | hysteria2 | 246.7 | 572.9 | 22.07 | 0.0 | 10.0 | 13.33 | 18.84 | Au1rxx-base64 | 66.94.121.46 |
| 81.9 | vless | 208.1 | 538.9 | 22.96 | 0.0 | 10.0 | 10.1 | 18.84 | Au1rxx-base64 | 216.36.124.176 |
| 81.87 | vless | 209.3 | 500.2 | 22.93 | 0.0 | 10.0 | 10.1 | 18.84 | Au1rxx-base64 | 172.233.139.46 |
| 81.79 | vless | 212.9 | 506.2 | 22.85 | 0.0 | 10.0 | 10.1 | 18.84 | Au1rxx-base64 | 172.235.38.85 |
| 81.72 | vless | 216.0 | 513.2 | 22.78 | 0.0 | 10.0 | 10.1 | 18.84 | Au1rxx-base64 | 172.236.233.59 |
| 81.27 | vless | 235.2 | 598.1 | 22.33 | 0.0 | 10.0 | 10.1 | 18.84 | Au1rxx-base64 | 38.209.125.45 |
| 80.97 | vless | 248.4 | 635.2 | 22.03 | 0.0 | 10.0 | 10.1 | 18.84 | Au1rxx-base64 | 172.235.43.210 |
| 79.96 | shadowsocks | 270.9 | 708.7 | 21.51 | 0.0 | 10.0 | 13.61 | 18.84 | Au1rxx-base64 | 173.244.56.6 |
| 79.78 | shadowsocks | 260.2 | 638.8 | 21.75 | 0.0 | 10.0 | 13.61 | 18.84 | Au1rxx-base64 | 156.146.38.170 |
| 78.0 | shadowsocks | 189.6 | 493.0 | 23.39 | 0.0 | 10.0 | 13.61 | 15.5 | mheidari-all | 108.181.118.10 |
| 77.58 | shadowsocks | 207.6 | 498.4 | 22.97 | 0.0 | 10.0 | 13.61 | 15.5 | mheidari-all | 108.181.0.177 |
| 77.05 | shadowsocks | 287.0 | 637.8 | 21.13 | 0.0 | 10.0 | 13.61 | 18.84 | Au1rxx-base64 | 23.150.248.20 |
| 76.88 | vless | 330.6 | 757.1 | 20.13 | 0.0 | 10.0 | 10.1 | 18.84 | Au1rxx-base64 | 79.141.172.154 |
| 76.74 | vless | 352.3 | 851.7 | 19.62 | 0.0 | 10.0 | 10.1 | 18.84 | Au1rxx-base64 | 15.204.97.216 |
| 76.64 | shadowsocks | 269.8 | 651.1 | 21.53 | 0.0 | 10.0 | 13.61 | 15.5 | mheidari-all | 173.244.56.9 |
| 76.51 | vless | 232.2 | 510.2 | 22.4 | 0.0 | 10.0 | 10.1 | 18.84 | Au1rxx-base64 | 172.64.53.55 |
| 75.99 | vless | 295.8 | 604.4 | 20.93 | 0.0 | 10.0 | 10.1 | 18.84 | Au1rxx-base64 | 31.58.50.200 |
| 75.17 | http | 197.1 | 500.3 | 23.21 | 0.0 | 10.0 | 10.0 | 14.96 | ermaozi | 138.199.35.198 |
| 75.02 | shadowsocks | 253.3 | 612.4 | 21.91 | 0.0 | 10.0 | 13.61 | 15.5 | mheidari-all | 156.146.38.168 |
| 74.95 | vless | 237.7 | 227.2 | 22.27 | 6.48 | 9.85 | 10.1 | 13.46 | Surfboard-tg-mixed | 31.76.91.72 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.948 | 0.883 | 317 | 1681 | prefer |
| ermaozi | 0.74 | 0.731 | 52 | 434 | prefer |
| Surfboard-tg-mixed | 0.719 | 0.641 | 192 | 7263 | prefer |
| mheidari-all | 0.58 | 0.5 | 112 | 15597 | observe |
| ermaozi-get_subscribe | 0.338 | 0.75 | 4 | 459 | observe |
| DeltaKronecker-all | 0.281 | 0.198 | 227 | 6070 | observe |
| tg-oneclickvpnkeys | 0.263 | 1.0 | 1 | 194 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4932 | observe |
| Epodonios-all | 0.255 | None | 0 | 7719 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 8500 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5889 | observe |
| barry-far-vless | 0.255 | None | 0 | 6106 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4223 | observe |
| Au1rxx-clash | 0.242 | None | 0 | 1681 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 118 |
| geo | ClientOSError | - | 93 |
| speed | TimeoutError | - | 44 |
| speed | ClientOSError | - | 36 |
| cn-block | TimeoutError | - | 26 |
| 204 | ProxyError | - | 20 |
| cn-block | ClientOSError | - | 15 |
| 204 | TimeoutError | - | 8 |
| 204 | ClientOSError | - | 2 |
| cn-block | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
