# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-04 19:47:35 |
| 运行耗时 | 242.4s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 86001 |
| 去重后节点 | 24515 |
| TCP 可达 | 3000 |
| 真实可用 | 509 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 24515 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.6 |
| geo | 0.8 |
| tcp | 36.5 |
| probe | 52.6 |
| real_test | 105.8 |
| generate | 41.0 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 51148 |
| vmess | 13151 |
| shadowsocks | 10261 |
| trojan | 9991 |
| hysteria2 | 1174 |
| socks | 80 |
| shadowsocksr | 76 |
| http | 67 |
| anytls | 21 |
| hysteria | 19 |
| tuic | 13 |

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
| 83.66 | http | 238.4 | 636.3 | 22.26 | 0.0 | 10.0 | 14.72 | 19.68 | zhangkai | 156.146.59.33 |
| 82.41 | hysteria2 | 235.4 | 643.8 | 22.33 | 0.0 | 9.28 | 13.64 | 18.26 | Au1rxx-base64 | 159.223.157.129 |
| 82.4 | hysteria2 | 239.9 | 661.7 | 22.22 | 0.0 | 9.28 | 13.64 | 18.26 | Au1rxx-base64 | 138.124.68.188 |
| 81.96 | hysteria2 | 239.1 | 660.8 | 22.24 | 0.0 | 8.82 | 13.64 | 18.26 | Au1rxx-base64 | usa1.spectrumproxy.shop |
| 81.49 | trojan | 247.8 | 680.7 | 22.04 | 0.0 | 10.0 | 14.19 | 18.26 | Au1rxx-base64 | 153.75.250.171 |
| 81.22 | vless | 245.9 | 673.9 | 22.09 | 0.0 | 10.0 | 10.87 | 18.26 | Au1rxx-base64 | 47.253.226.114 |
| 80.79 | vless | 264.1 | 666.6 | 21.66 | 0.0 | 10.0 | 10.87 | 18.26 | Au1rxx-base64 | 167.17.69.171 |
| 80.25 | vless | 287.7 | 722.9 | 21.12 | 0.0 | 10.0 | 10.87 | 18.26 | Au1rxx-base64 | 159.195.12.98 |
| 78.75 | vless | 336.1 | 853.9 | 20.0 | 0.0 | 10.0 | 10.87 | 18.26 | Au1rxx-base64 | 158.69.112.254 |
| 78.16 | shadowsocks | 240.7 | 669.8 | 22.21 | 0.0 | 10.0 | 11.69 | 18.26 | Au1rxx-base64 | 37.19.198.243 |
| 77.9 | vless | 351.8 | 868.9 | 19.63 | 0.0 | 9.14 | 10.87 | 18.26 | Au1rxx-base64 | 169.40.42.15 |
| 77.69 | shadowsocks | 232.8 | 634.3 | 22.39 | 0.0 | 9.35 | 11.69 | 18.26 | Au1rxx-base64 | 37.19.198.244 |
| 77.65 | shadowsocks | 234.3 | 631.9 | 22.35 | 0.0 | 9.35 | 11.69 | 18.26 | Au1rxx-base64 | 37.19.198.236 |
| 77.29 | shadowsocks | 249.8 | 676.9 | 21.99 | 0.0 | 9.35 | 11.69 | 18.26 | Au1rxx-base64 | 37.19.198.160 |
| 77.05 | vless | 378.3 | 1060.5 | 19.02 | 0.0 | 10.0 | 10.87 | 18.26 | Au1rxx-base64 | 45.138.100.226 |
| 76.41 | trojan | 304.4 | 656.5 | 20.73 | 0.0 | 10.0 | 14.19 | 18.26 | Au1rxx-base64 | 163.245.196.68 |
| 75.65 | trojan | 326.5 | 741.3 | 20.22 | 0.0 | 10.0 | 14.19 | 18.26 | Au1rxx-base64 | 64.94.95.114 |
| 75.53 | trojan | 334.2 | 760.3 | 20.04 | 0.0 | 10.0 | 14.19 | 18.26 | Au1rxx-base64 | 64.94.95.115 |
| 74.99 | trojan | 379.0 | 890.8 | 19.01 | 0.0 | 10.0 | 14.19 | 18.26 | Au1rxx-base64 | 64.94.95.118 |
| 74.91 | shadowsocks | 316.7 | 664.1 | 20.45 | 0.0 | 9.36 | 11.69 | 18.26 | Au1rxx-base64 | 68.168.222.210 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.985 | 1.0 | 53 | 72 | prefer |
| Au1rxx-base64 | 0.965 | 0.904 | 418 | 1560 | prefer |
| DeltaKronecker-all | 0.654 | 0.575 | 106 | 5788 | observe |
| Surfboard-tg-mixed | 0.595 | 0.692 | 13 | 5570 | observe |
| mheidari-all | 0.53 | 0.7 | 10 | 19967 | observe |
| tg-OutlineReleasedKey | 0.257 | 1.0 | 1 | 58 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5251 | observe |
| Epodonios-all | 0.255 | None | 0 | 6154 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6965 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4451 | observe |
| barry-far-vless | 0.255 | None | 0 | 4787 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5141 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.237 | None | 0 | 1560 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | ProxyError | - | 21 |
| 204 | TimeoutError | - | 16 |
| geo | TimeoutError | - | 14 |
| cn-block | TimeoutError | - | 10 |
| geo | ClientOSError | - | 10 |
| speed | TimeoutError | - | 8 |
| 204 | ClientOSError | - | 7 |
| cn-block | ClientOSError | - | 4 |
| cn-block | ProxyError | - | 4 |
| speed | ClientOSError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
