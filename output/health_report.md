# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-31 09:00:51 |
| 运行耗时 | 228.7s |
| 订阅源总数 | 107 |
| 健康订阅源 | 102 |
| 原始节点 | 77153 |
| 去重后节点 | 22423 |
| TCP 可达 | 3000 |
| 真实可用 | 361 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22423 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.2 |
| geo | 1.4 |
| tcp | 32.1 |
| probe | 54.8 |
| real_test | 99.0 |
| generate | 36.1 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 44562 |
| vmess | 11819 |
| shadowsocks | 10117 |
| trojan | 9779 |
| hysteria2 | 586 |
| http | 98 |
| shadowsocksr | 73 |
| socks | 63 |
| anytls | 26 |
| tuic | 16 |
| hysteria | 14 |

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
| 81.7 | shadowsocks | 240.6 | 616.7 | 22.21 | 0.0 | 10.0 | 14.13 | 19.36 | Au1rxx-base64 | 156.146.38.170 |
| 81.66 | shadowsocks | 242.1 | 622.3 | 22.17 | 0.0 | 10.0 | 14.13 | 19.36 | Au1rxx-base64 | 156.146.38.167 |
| 81.47 | shadowsocks | 250.3 | 622.8 | 21.98 | 0.0 | 10.0 | 14.13 | 19.36 | Au1rxx-base64 | 156.146.38.168 |
| 81.19 | hysteria2 | 305.3 | 716.9 | 20.71 | 0.0 | 9.3 | 14.17 | 19.36 | Au1rxx-base64 | usa1.spectrumproxy.shop |
| 80.84 | hysteria2 | 311.5 | 695.8 | 20.57 | 0.0 | 10.0 | 14.17 | 19.36 | Au1rxx-base64 | 159.223.157.129 |
| 80.42 | trojan | 284.4 | 716.4 | 21.2 | 0.0 | 10.0 | 12.86 | 19.36 | Au1rxx-base64 | 64.94.95.115 |
| 80.34 | trojan | 287.4 | 724.9 | 21.12 | 0.0 | 10.0 | 12.86 | 19.36 | Au1rxx-base64 | 64.94.95.114 |
| 79.92 | trojan | 268.5 | 634.8 | 21.56 | 0.0 | 10.0 | 12.86 | 19.36 | Au1rxx-base64 | 163.245.196.68 |
| 79.88 | trojan | 307.4 | 773.9 | 20.66 | 0.0 | 10.0 | 12.86 | 19.36 | Au1rxx-base64 | 64.94.95.118 |
| 78.67 | trojan | 359.6 | 932.2 | 19.45 | 0.0 | 10.0 | 12.86 | 19.36 | Au1rxx-base64 | 64.94.95.117 |
| 78.58 | shadowsocks | 265.3 | 529.8 | 21.64 | 0.0 | 10.0 | 14.13 | 19.36 | Au1rxx-base64 | 108.181.0.177 |
| 78.56 | shadowsocks | 246.4 | 624.3 | 22.07 | 0.0 | 10.0 | 14.13 | 19.36 | Au1rxx-base64 | 156.146.38.169 |
| 78.22 | shadowsocks | 267.4 | 528.3 | 21.59 | 0.0 | 10.0 | 14.13 | 19.36 | Au1rxx-base64 | 108.181.118.10 |
| 77.99 | shadowsocks | 264.3 | 564.4 | 21.66 | 0.0 | 10.0 | 14.13 | 19.36 | Au1rxx-base64 | 173.244.56.6 |
| 77.94 | shadowsocks | 272.4 | 546.5 | 21.47 | 0.0 | 10.0 | 14.13 | 19.36 | Au1rxx-base64 | 173.244.56.9 |
| 77.3 | hysteria2 | 307.9 | 724.1 | 20.65 | 0.0 | 10.0 | 14.17 | 19.36 | Au1rxx-base64 | 138.124.68.188 |
| 76.39 | shadowsocks | 319.7 | 707.3 | 20.38 | 0.0 | 10.0 | 14.13 | 19.36 | Au1rxx-base64 | 37.19.198.160 |
| 75.83 | shadowsocks | 308.4 | 633.2 | 20.64 | 0.0 | 10.0 | 14.13 | 19.36 | Au1rxx-base64 | 149.22.95.183 |
| 75.69 | shadowsocks | 326.5 | 731.7 | 20.22 | 0.0 | 10.0 | 14.13 | 19.36 | Au1rxx-base64 | 37.19.198.244 |
| 75.6 | shadowsocks | 334.5 | 750.9 | 20.03 | 0.0 | 10.0 | 14.13 | 19.36 | Au1rxx-base64 | 37.19.198.236 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.992 | 1.0 | 81 | 110 | prefer |
| Au1rxx-base64 | 0.849 | 0.799 | 194 | 1319 | prefer |
| mheidari-all | 0.646 | 0.769 | 13 | 16339 | observe |
| Surfboard-tg-mixed | 0.609 | 0.529 | 155 | 5242 | observe |
| DeltaKronecker-all | 0.543 | 0.462 | 65 | 5144 | observe |
| tg-LonUp_M | 0.262 | 1.0 | 1 | 174 | observe |
| roosterkid-openproxylist-v2ray | 0.261 | 1.0 | 1 | 150 | observe |
| tg-OutlineReleasedKey | 0.257 | 1.0 | 1 | 45 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5507 | observe |
| Epodonios-all | 0.255 | None | 0 | 5918 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6473 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4146 | observe |
| barry-far-vless | 0.255 | None | 0 | 4510 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5074 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 40 |
| 204 | ProxyError | - | 32 |
| 204 | TimeoutError | - | 23 |
| geo | ClientOSError | - | 14 |
| speed | TimeoutError | - | 14 |
| cn-block | ProxyError | - | 8 |
| speed | ClientOSError | - | 8 |
| cn-block | TimeoutError | - | 8 |
| 204 | ClientOSError | - | 4 |
| cn-block | ClientOSError | - | 3 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
