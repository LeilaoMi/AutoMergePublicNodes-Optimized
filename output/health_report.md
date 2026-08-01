# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-01 19:21:55 |
| 运行耗时 | 291.3s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 78665 |
| 去重后节点 | 23513 |
| TCP 可达 | 3000 |
| 真实可用 | 590 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23513 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.9 |
| geo | 1.4 |
| tcp | 34.8 |
| probe | 58.4 |
| real_test | 149.4 |
| generate | 40.4 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 47018 |
| vmess | 12254 |
| shadowsocks | 10197 |
| trojan | 8223 |
| hysteria2 | 633 |
| http | 157 |
| shadowsocksr | 70 |
| socks | 65 |
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
| 84.21 | http | 231.1 | 620.6 | 22.43 | 0.0 | 10.0 | 14.9 | 19.88 | zhangkai | 156.146.59.8 |
| 83.98 | http | 240.8 | 629.6 | 22.2 | 0.0 | 10.0 | 14.9 | 19.88 | zhangkai | 156.146.59.33 |
| 83.93 | http | 243.1 | 649.0 | 22.15 | 0.0 | 10.0 | 14.9 | 19.88 | zhangkai | 156.146.59.21 |
| 83.8 | http | 248.6 | 656.4 | 22.02 | 0.0 | 10.0 | 14.9 | 19.88 | zhangkai | 156.146.59.7 |
| 83.63 | http | 256.2 | 683.8 | 21.85 | 0.0 | 10.0 | 14.9 | 19.88 | zhangkai | 156.146.59.16 |
| 83.58 | http | 258.3 | 687.2 | 21.8 | 0.0 | 10.0 | 14.9 | 19.88 | zhangkai | 156.146.59.25 |
| 83.55 | http | 259.5 | 691.4 | 21.77 | 0.0 | 10.0 | 14.9 | 19.88 | zhangkai | 156.146.59.50 |
| 81.82 | http | 247.9 | 653.4 | 22.04 | 0.0 | 10.0 | 14.9 | 19.88 | zhangkai | 156.146.59.49 |
| 81.71 | http | 252.5 | 671.6 | 21.93 | 0.0 | 10.0 | 14.9 | 19.88 | zhangkai | 156.146.59.43 |
| 81.06 | http | 237.7 | 638.6 | 22.28 | 0.0 | 10.0 | 14.9 | 19.88 | zhangkai | 156.146.59.41 |
| 80.43 | hysteria2 | 232.2 | 641.3 | 22.4 | 0.0 | 9.45 | 13.12 | 16.56 | Au1rxx-base64 | 159.223.157.129 |
| 80.14 | hysteria2 | 249.6 | 684.4 | 22.0 | 0.0 | 9.46 | 13.12 | 16.56 | Au1rxx-base64 | 138.124.68.188 |
| 79.0 | vless | 239.7 | 648.9 | 22.23 | 0.0 | 10.0 | 10.21 | 16.56 | Au1rxx-base64 | 167.99.48.117 |
| 78.81 | hysteria2 | 252.5 | 693.2 | 21.93 | 0.0 | 8.2 | 13.12 | 16.56 | Au1rxx-base64 | usa1.spectrumproxy.shop |
| 78.31 | vless | 269.3 | 716.4 | 21.54 | 0.0 | 10.0 | 10.21 | 16.56 | Au1rxx-base64 | 78.111.89.171 |
| 77.85 | vless | 287.6 | 713.5 | 21.12 | 0.0 | 10.0 | 10.21 | 16.56 | Au1rxx-base64 | 216.152.147.28 |
| 77.75 | shadowsocks | 230.0 | 631.0 | 22.45 | 0.0 | 10.0 | 12.74 | 16.56 | Au1rxx-base64 | 37.19.198.243 |
| 77.55 | vless | 302.1 | 817.5 | 20.78 | 0.0 | 10.0 | 10.21 | 16.56 | Au1rxx-base64 | 137.184.218.169 |
| 77.53 | trojan | 254.3 | 694.7 | 21.89 | 0.0 | 10.0 | 12.08 | 16.56 | Au1rxx-base64 | 153.75.250.171 |
| 77.29 | shadowsocks | 229.7 | 632.5 | 22.46 | 0.0 | 9.53 | 12.74 | 16.56 | Au1rxx-base64 | 37.19.198.160 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 1.0 | 1.0 | 148 | 194 | prefer |
| Au1rxx-base64 | 0.766 | 0.699 | 502 | 1692 | prefer |
| Surfboard-tg-mixed | 0.638 | 0.56 | 75 | 5294 | observe |
| DeltaKronecker-all | 0.514 | 0.433 | 104 | 5502 | observe |
| mheidari-all | 0.4 | 0.75 | 4 | 16619 | observe |
| tg-OutlineReleasedKey | 0.257 | 1.0 | 1 | 55 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5391 | observe |
| Epodonios-all | 0.255 | None | 0 | 5909 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3975 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6647 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4168 | observe |
| barry-far-vless | 0.255 | None | 0 | 4547 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5071 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.243 | None | 0 | 1692 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 98 |
| speed | TimeoutError | - | 33 |
| 204 | TimeoutError | - | 31 |
| cn-block | TimeoutError | - | 27 |
| geo | ClientOSError | - | 18 |
| speed | ClientOSError | - | 11 |
| 204 | ProxyError | - | 9 |
| 204 | ClientOSError | - | 6 |
| cn-block | ProxyError | - | 5 |
| cn-block | ClientOSError | - | 4 |
| geo | ProxyError | - | 2 |
| speed | ProxyError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
