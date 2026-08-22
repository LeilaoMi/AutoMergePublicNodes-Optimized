# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-22 18:42:13 |
| 运行耗时 | 301.0s |
| 订阅源总数 | 107 |
| 健康订阅源 | 99 |
| 原始节点 | 86102 |
| 去重后节点 | 23834 |
| TCP 可达 | 3000 |
| 真实可用 | 721 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23834 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.2 |
| geo | 1.5 |
| tcp | 40.1 |
| probe | 60.2 |
| real_test | 155.6 |
| generate | 36.3 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 50369 |
| trojan | 12973 |
| shadowsocks | 10485 |
| vmess | 10281 |
| hysteria2 | 1511 |
| http | 168 |
| shadowsocksr | 163 |
| socks | 117 |
| anytls | 16 |
| hysteria | 11 |
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
| 82.14 | vless | 245.9 | 611.0 | 22.08 | 0.0 | 10.0 | 11.06 | 20.0 | Au1rxx-base64 | 198.251.78.29 |
| 81.96 | trojan | 263.4 | 614.1 | 21.68 | 0.0 | 10.0 | 14.83 | 20.0 | Au1rxx-base64 | 64.94.95.114 |
| 81.71 | trojan | 262.8 | 625.4 | 21.69 | 0.0 | 10.0 | 14.83 | 20.0 | Au1rxx-base64 | 64.94.95.117 |
| 81.68 | vless | 286.8 | 689.9 | 21.14 | 0.0 | 10.0 | 11.06 | 20.0 | Au1rxx-base64 | 137.184.218.169 |
| 81.54 | shadowsocks | 252.1 | 617.4 | 21.94 | 0.0 | 10.0 | 13.67 | 20.0 | Au1rxx-base64 | 156.146.38.169 |
| 81.46 | shadowsocks | 258.5 | 640.6 | 21.79 | 0.0 | 10.0 | 13.67 | 20.0 | Au1rxx-base64 | 156.146.38.170 |
| 81.14 | shadowsocks | 272.5 | 688.0 | 21.47 | 0.0 | 10.0 | 13.67 | 20.0 | Au1rxx-base64 | 37.19.198.244 |
| 80.75 | trojan | 266.8 | 612.7 | 21.6 | 0.0 | 10.0 | 14.83 | 20.0 | Au1rxx-base64 | 64.94.95.115 |
| 79.75 | vless | 345.1 | 907.4 | 19.79 | 0.0 | 10.0 | 11.06 | 20.0 | Au1rxx-base64 | 45.138.100.226 |
| 79.71 | vless | 324.9 | 752.1 | 20.26 | 0.0 | 10.0 | 11.06 | 20.0 | Au1rxx-base64 | 158.69.112.254 |
| 79.65 | shadowsocks | 259.0 | 642.5 | 21.78 | 0.0 | 10.0 | 13.67 | 18.2 | Surfboard-tg-mixed | 156.146.38.167 |
| 79.53 | shadowsocks | 268.9 | 615.9 | 21.55 | 0.0 | 10.0 | 13.67 | 20.0 | Au1rxx-base64 | 23.150.248.20 |
| 79.3 | vless | 334.1 | 899.7 | 20.04 | 0.0 | 10.0 | 11.06 | 18.2 | Surfboard-tg-mixed | 216.152.147.28 |
| 77.67 | trojan | 299.6 | 741.8 | 20.84 | 0.0 | 10.0 | 14.83 | 20.0 | Au1rxx-base64 | 64.74.163.118 |
| 77.42 | vless | 348.7 | 825.9 | 19.71 | 0.0 | 10.0 | 11.06 | 20.0 | Au1rxx-base64 | 140.99.223.187 |
| 77.12 | shadowsocks | 230.2 | 606.5 | 22.45 | 0.0 | 10.0 | 13.67 | 20.0 | Au1rxx-base64 | 155.138.136.240 |
| 76.65 | vless | 306.1 | 756.7 | 20.69 | 0.0 | 10.0 | 11.06 | 20.0 | Au1rxx-base64 | 185.95.231.156 |
| 76.58 | vless | 510.3 | 837.1 | 15.96 | 0.0 | 10.0 | 11.06 | 20.0 | Au1rxx-base64 | 169.40.42.229 |
| 76.48 | trojan | 337.7 | 683.0 | 19.96 | 0.0 | 10.0 | 14.83 | 20.0 | Au1rxx-base64 | 34.94.125.227 |
| 76.26 | shadowsocks | 304.9 | 641.7 | 20.72 | 0.0 | 10.0 | 13.67 | 20.0 | Au1rxx-base64 | 149.22.95.183 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | 0.936 | 487 | 1853 | prefer |
| zhangkai | 0.997 | 1.0 | 112 | 144 | prefer |
| Surfboard-tg-mixed | 0.784 | 0.707 | 123 | 6394 | prefer |
| mheidari-all | 0.78 | 0.705 | 88 | 14443 | prefer |
| xiaoji235-airport-v2ray-all | 0.335 | 1.0 | 1 | 5974 | observe |
| DeltaKronecker-all | 0.272 | 0.286 | 7 | 5015 | observe |
| tg-oneclickvpnkeys | 0.262 | 1.0 | 1 | 176 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5096 | observe |
| Epodonios-all | 0.255 | None | 0 | 6972 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3988 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7145 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5216 | observe |
| barry-far-vless | 0.255 | None | 0 | 5526 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4074 | observe |
| Au1rxx-clash | 0.249 | None | 0 | 1853 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | TimeoutError | - | 29 |
| cn-block | TimeoutError | - | 18 |
| geo | TimeoutError | - | 15 |
| speed | TimeoutError | - | 11 |
| geo | ClientOSError | - | 8 |
| cn-block | ClientOSError | - | 6 |
| cn-block | ProxyError | - | 4 |
| speed | ClientOSError | - | 4 |
| 204 | ProxyError | - | 4 |
| 204 | ClientOSError | - | 1 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
