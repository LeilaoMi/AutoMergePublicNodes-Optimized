# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-10 19:07:32 |
| 运行耗时 | 236.5s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 84993 |
| 去重后节点 | 24663 |
| TCP 可达 | 3000 |
| 真实可用 | 497 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 24663 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.1 |
| geo | 1.4 |
| tcp | 36.0 |
| probe | 48.9 |
| real_test | 110.5 |
| generate | 33.7 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 50407 |
| vmess | 13222 |
| trojan | 10283 |
| shadowsocks | 9500 |
| hysteria2 | 1325 |
| shadowsocksr | 73 |
| http | 72 |
| socks | 64 |
| anytls | 26 |
| hysteria | 13 |
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
| 82.09 | hysteria2 | 254.8 | 700.9 | 21.88 | 0.0 | 9.2 | 12.63 | 19.38 | Au1rxx-base64 | 138.124.68.188 |
| 80.54 | hysteria2 | 251.5 | 703.6 | 21.95 | 0.0 | 7.58 | 12.63 | 19.38 | Au1rxx-base64 | usa1.spectrumproxy.shop |
| 80.35 | shadowsocks | 225.7 | 620.0 | 22.55 | 0.0 | 9.26 | 13.16 | 19.38 | Au1rxx-base64 | 37.19.198.243 |
| 80.06 | hysteria2 | 337.0 | 935.2 | 19.98 | 0.0 | 9.17 | 12.63 | 19.38 | Au1rxx-base64 | 159.223.157.129 |
| 79.91 | shadowsocks | 244.2 | 679.0 | 22.12 | 0.0 | 9.25 | 13.16 | 19.38 | Au1rxx-base64 | 37.19.198.236 |
| 79.79 | shadowsocks | 249.9 | 681.3 | 21.99 | 0.0 | 9.26 | 13.16 | 19.38 | Au1rxx-base64 | 37.19.198.244 |
| 78.5 | shadowsocks | 293.3 | 728.6 | 20.99 | 0.0 | 9.47 | 13.16 | 19.38 | Au1rxx-base64 | 68.168.222.210 |
| 76.84 | vless | 332.9 | 768.9 | 20.07 | 0.0 | 9.05 | 11.27 | 19.38 | Au1rxx-base64 | 152.53.82.202 |
| 75.7 | shadowsocks | 304.8 | 691.2 | 20.72 | 0.0 | 10.0 | 13.16 | 19.38 | Au1rxx-base64 | 108.181.57.93 |
| 75.59 | vless | 333.0 | 896.5 | 20.07 | 0.0 | 10.0 | 11.27 | 14.48 | Surfboard-tg-mixed | 169.40.42.179 |
| 75.48 | vless | 347.6 | 822.3 | 19.73 | 0.0 | 10.0 | 11.27 | 14.48 | Surfboard-tg-mixed | 169.40.42.133 |
| 75.34 | vless | 265.9 | 609.7 | 21.62 | 0.0 | 10.0 | 11.27 | 19.38 | Au1rxx-base64 | 216.227.161.95 |
| 74.62 | trojan | 385.4 | 905.9 | 18.86 | 0.0 | 10.0 | 13.33 | 19.38 | Au1rxx-base64 | 64.94.95.114 |
| 74.59 | trojan | 397.3 | 947.8 | 18.58 | 0.0 | 10.0 | 13.33 | 19.38 | Au1rxx-base64 | 64.94.95.118 |
| 74.52 | vless | 331.1 | 559.4 | 20.11 | 0.0 | 10.0 | 11.27 | 19.38 | Au1rxx-base64 | 70.39.198.183 |
| 74.51 | trojan | 390.5 | 924.9 | 18.74 | 0.0 | 10.0 | 13.33 | 19.38 | Au1rxx-base64 | 64.94.95.117 |
| 74.23 | vless | 329.9 | 598.0 | 20.14 | 0.0 | 9.01 | 11.27 | 19.38 | Au1rxx-base64 | 179.255.148.66 |
| 74.18 | trojan | 396.2 | 945.1 | 18.61 | 0.0 | 10.0 | 13.33 | 19.38 | Au1rxx-base64 | 64.94.95.115 |
| 73.93 | vless | 366.4 | 681.1 | 19.3 | 0.0 | 10.0 | 11.27 | 19.38 | Au1rxx-base64 | 167.17.68.205 |
| 73.61 | hysteria2 | 369.5 | 702.1 | 19.22 | 0.0 | 9.22 | 12.63 | 19.38 | Au1rxx-base64 | 62.210.124.146 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.983 | 1.0 | 49 | 67 | prefer |
| Au1rxx-base64 | 0.966 | 0.904 | 405 | 1614 | prefer |
| mheidari-all | 0.653 | 0.575 | 73 | 20189 | observe |
| Surfboard-tg-mixed | 0.637 | 0.559 | 68 | 6152 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| tg-LonUp_M | 0.262 | 1.0 | 1 | 178 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5327 | observe |
| DeltaKronecker-all | 0.255 | None | 0 | 5881 | observe |
| Epodonios-all | 0.255 | None | 0 | 6803 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3996 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7537 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5085 | observe |
| barry-far-vless | 0.255 | None | 0 | 5417 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5191 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | ClientOSError | - | 25 |
| 204 | ProxyError | - | 17 |
| 204 | TimeoutError | - | 14 |
| cn-block | TimeoutError | - | 13 |
| speed | TimeoutError | - | 12 |
| geo | TimeoutError | - | 7 |
| speed | ClientOSError | - | 6 |
| cn-block | ClientOSError | - | 2 |
| geo | ProxyError | - | 1 |
| cn-block | ProxyError | - | 1 |
| 204 | ClientOSError | - | 1 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
