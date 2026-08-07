# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-07 07:28:07 |
| 运行耗时 | 238.8s |
| 订阅源总数 | 107 |
| 健康订阅源 | 102 |
| 原始节点 | 89705 |
| 去重后节点 | 24235 |
| TCP 可达 | 3000 |
| 真实可用 | 456 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 24235 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.0 |
| geo | 1.3 |
| tcp | 35.5 |
| probe | 52.1 |
| real_test | 114.6 |
| generate | 29.2 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 52575 |
| vmess | 13487 |
| trojan | 11381 |
| shadowsocks | 10453 |
| hysteria2 | 1533 |
| socks | 106 |
| shadowsocksr | 72 |
| http | 35 |
| anytls | 30 |
| hysteria | 21 |
| tuic | 12 |

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
| 85.34 | hysteria2 | 233.7 | 649.3 | 22.37 | 0.0 | 10.0 | 14.35 | 19.72 | Au1rxx-base64 | 159.223.157.129 |
| 84.66 | hysteria2 | 267.2 | 687.4 | 21.59 | 0.0 | 10.0 | 14.35 | 19.72 | Au1rxx-base64 | 138.124.68.188 |
| 84.28 | hysteria2 | 247.4 | 689.3 | 22.05 | 0.0 | 9.16 | 14.35 | 19.72 | Au1rxx-base64 | usa1.spectrumproxy.shop |
| 81.4 | shadowsocks | 247.8 | 693.1 | 22.04 | 0.0 | 10.0 | 13.64 | 19.72 | Au1rxx-base64 | 37.19.198.244 |
| 80.8 | shadowsocks | 230.5 | 642.1 | 22.44 | 0.0 | 10.0 | 13.64 | 19.72 | Au1rxx-base64 | 37.19.198.160 |
| 80.35 | trojan | 347.1 | 973.6 | 19.74 | 0.0 | 10.0 | 13.89 | 19.72 | Au1rxx-base64 | 153.75.250.171 |
| 78.65 | trojan | 293.0 | 638.3 | 21.0 | 0.0 | 10.0 | 13.89 | 19.72 | Au1rxx-base64 | 64.94.95.118 |
| 78.58 | trojan | 294.8 | 639.6 | 20.95 | 0.0 | 10.0 | 13.89 | 19.72 | Au1rxx-base64 | 64.94.95.115 |
| 78.55 | trojan | 295.2 | 641.2 | 20.94 | 0.0 | 10.0 | 13.89 | 19.72 | Au1rxx-base64 | 64.94.95.117 |
| 78.52 | trojan | 293.2 | 636.4 | 20.99 | 0.0 | 10.0 | 13.89 | 19.72 | Au1rxx-base64 | 64.94.95.114 |
| 78.11 | shadowsocks | 280.3 | 637.9 | 21.29 | 0.0 | 10.0 | 13.64 | 19.72 | Au1rxx-base64 | 156.146.38.170 |
| 77.69 | shadowsocks | 321.1 | 773.0 | 20.34 | 0.0 | 10.0 | 13.64 | 19.72 | Au1rxx-base64 | 156.146.38.168 |
| 77.65 | trojan | 303.0 | 651.8 | 20.76 | 0.0 | 10.0 | 13.89 | 19.72 | Au1rxx-base64 | 163.245.196.68 |
| 77.64 | shadowsocks | 285.7 | 653.3 | 21.16 | 0.0 | 10.0 | 13.64 | 19.72 | Au1rxx-base64 | 156.146.38.169 |
| 77.04 | shadowsocks | 222.5 | 604.9 | 22.63 | 0.0 | 10.0 | 13.64 | 19.72 | Au1rxx-base64 | 198.98.53.130 |
| 76.89 | hysteria2 | 356.1 | 689.6 | 19.53 | 0.0 | 10.0 | 14.35 | 19.72 | Au1rxx-base64 | 62.210.124.146 |
| 76.69 | shadowsocks | 235.4 | 653.3 | 22.33 | 0.0 | 10.0 | 13.64 | 19.72 | Au1rxx-base64 | 37.19.198.243 |
| 76.35 | shadowsocks | 308.8 | 732.3 | 20.63 | 0.0 | 10.0 | 13.64 | 19.72 | Au1rxx-base64 | 108.181.57.93 |
| 75.67 | hysteria2 | 422.6 | 867.0 | 17.99 | 0.0 | 10.0 | 14.35 | 19.72 | Au1rxx-base64 | 5.255.102.165 |
| 74.65 | shadowsocks | 313.5 | 575.5 | 20.52 | 0.0 | 10.0 | 13.64 | 19.72 | Au1rxx-base64 | 173.244.56.6 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.979 | 0.929 | 381 | 1300 | prefer |
| zhangkai | 0.956 | 1.0 | 20 | 25 | prefer |
| DeltaKronecker-all | 0.564 | 0.483 | 29 | 5326 | observe |
| Surfboard-tg-mixed | 0.526 | 0.445 | 128 | 6241 | observe |
| mheidari-all | 0.3 | 0.208 | 48 | 20715 | observe |
| xiaoji235-airport-v2ray-all | 0.287 | 0.5 | 2 | 5184 | observe |
| Epodonios-all | 0.255 | None | 0 | 6873 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7440 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4967 | observe |
| barry-far-vless | 0.255 | None | 0 | 5297 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5247 | observe |
| nscl5-all | 0.246 | None | 0 | 1772 | observe |
| Au1rxx-clash | 0.227 | None | 0 | 1300 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 47 |
| geo | ClientOSError | - | 38 |
| 204 | TimeoutError | - | 14 |
| speed | TimeoutError | - | 13 |
| 204 | ProxyError | - | 12 |
| cn-block | TimeoutError | - | 10 |
| speed | ClientOSError | - | 9 |
| 204 | ClientOSError | - | 6 |
| cn-block | ClientOSError | - | 3 |
| geo | ProxyError | - | 2 |
| cn-block | ProxyError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
