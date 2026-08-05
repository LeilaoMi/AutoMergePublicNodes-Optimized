# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-05 14:25:17 |
| 运行耗时 | 242.7s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 87256 |
| 去重后节点 | 24192 |
| TCP 可达 | 3000 |
| 真实可用 | 515 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 24192 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.4 |
| geo | 1.1 |
| tcp | 36.0 |
| probe | 50.9 |
| real_test | 106.1 |
| generate | 42.2 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 51752 |
| vmess | 13107 |
| trojan | 10684 |
| shadowsocks | 10138 |
| hysteria2 | 1340 |
| socks | 74 |
| shadowsocksr | 68 |
| http | 39 |
| anytls | 21 |
| hysteria | 19 |
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
| 82.98 | hysteria2 | 231.9 | 645.5 | 22.41 | 0.0 | 8.73 | 13.64 | 19.3 | Au1rxx-base64 | 159.223.157.129 |
| 82.74 | hysteria2 | 246.6 | 688.0 | 22.07 | 0.0 | 8.73 | 13.64 | 19.3 | Au1rxx-base64 | 138.124.68.188 |
| 82.31 | hysteria2 | 247.1 | 681.5 | 22.06 | 0.0 | 8.31 | 13.64 | 19.3 | Au1rxx-base64 | usa1.spectrumproxy.shop |
| 80.47 | vless | 259.0 | 680.2 | 21.78 | 0.0 | 10.0 | 9.39 | 19.3 | Au1rxx-base64 | 167.17.69.171 |
| 80.19 | vless | 271.3 | 624.6 | 21.5 | 0.0 | 10.0 | 9.39 | 19.3 | Au1rxx-base64 | 169.40.42.15 |
| 79.24 | trojan | 347.0 | 968.5 | 19.75 | 0.0 | 9.09 | 14.1 | 19.3 | Au1rxx-base64 | 153.75.250.171 |
| 79.02 | shadowsocks | 226.2 | 623.0 | 22.54 | 0.0 | 8.83 | 12.35 | 19.3 | Au1rxx-base64 | 37.19.198.244 |
| 78.52 | shadowsocks | 247.9 | 681.0 | 22.04 | 0.0 | 8.83 | 12.35 | 19.3 | Au1rxx-base64 | 37.19.198.236 |
| 77.46 | vless | 341.8 | 957.1 | 19.87 | 0.0 | 10.0 | 9.39 | 19.3 | Au1rxx-base64 | 45.138.100.226 |
| 77.11 | vless | 404.1 | 1055.2 | 18.42 | 0.0 | 10.0 | 9.39 | 19.3 | Au1rxx-base64 | 158.69.112.254 |
| 76.3 | trojan | 309.1 | 660.7 | 20.62 | 0.0 | 9.08 | 14.1 | 19.3 | Au1rxx-base64 | 163.245.196.68 |
| 75.74 | vless | 269.0 | 741.5 | 21.55 | 0.0 | 10.0 | 9.39 | 19.3 | Au1rxx-base64 | 104.18.185.26 |
| 75.63 | shadowsocks | 372.7 | 1059.3 | 19.15 | 0.0 | 8.83 | 12.35 | 19.3 | Au1rxx-base64 | 37.19.198.160 |
| 75.55 | vless | 277.4 | 735.3 | 21.36 | 0.0 | 10.0 | 9.39 | 19.3 | Au1rxx-base64 | 104.17.101.139 |
| 75.55 | vless | 277.4 | 732.4 | 21.36 | 0.0 | 10.0 | 9.39 | 19.3 | Au1rxx-base64 | 104.18.42.163 |
| 75.12 | vless | 295.8 | 780.9 | 20.93 | 0.0 | 10.0 | 9.39 | 19.3 | Au1rxx-base64 | 172.64.144.82 |
| 75.1 | shadowsocks | 281.0 | 635.3 | 21.27 | 0.0 | 8.82 | 12.35 | 19.3 | Au1rxx-base64 | 156.146.38.169 |
| 74.96 | shadowsocks | 286.6 | 666.5 | 21.14 | 0.0 | 8.82 | 12.35 | 19.3 | Au1rxx-base64 | 156.146.38.167 |
| 74.87 | vless | 306.7 | 830.0 | 20.68 | 0.0 | 10.0 | 9.39 | 19.3 | Au1rxx-base64 | 8.47.69.0 |
| 74.85 | vless | 307.5 | 807.1 | 20.66 | 0.0 | 10.0 | 9.39 | 19.3 | Au1rxx-base64 | 104.17.185.207 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.998 | 0.938 | 422 | 1552 | prefer |
| zhangkai | 0.956 | 1.0 | 20 | 25 | prefer |
| Surfboard-tg-mixed | 0.712 | 0.634 | 123 | 5862 | prefer |
| mheidari-all | 0.437 | 0.35 | 40 | 20132 | observe |
| DeltaKronecker-all | 0.401 | 0.571 | 7 | 5316 | observe |
| Epodonios-all | 0.335 | 1.0 | 1 | 6386 | observe |
| xiaoji235-airport-v2ray-all | 0.335 | 1.0 | 1 | 4655 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5260 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3996 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7443 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4686 | observe |
| barry-far-vless | 0.255 | None | 0 | 4943 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5147 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 26 |
| 204 | TimeoutError | - | 20 |
| geo | ClientOSError | - | 14 |
| cn-block | TimeoutError | - | 13 |
| speed | TimeoutError | - | 8 |
| 204 | ProxyError | - | 7 |
| 204 | ClientOSError | - | 5 |
| speed | ClientOSError | - | 3 |
| cn-block | ClientOSError | - | 2 |
| cn-block | ProxyError | - | 1 |
| speed | ProxyError | - | 1 |
| speed | status | 403 | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
