# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-28 08:49:10 |
| 运行耗时 | 334.8s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 86095 |
| 去重后节点 | 23310 |
| TCP 可达 | 3000 |
| 真实可用 | 679 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23310 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.4 |
| geo | 1.3 |
| tcp | 32.0 |
| probe | 62.7 |
| real_test | 188.4 |
| generate | 44.0 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 48732 |
| trojan | 16058 |
| vmess | 10310 |
| shadowsocks | 10165 |
| hysteria2 | 560 |
| shadowsocksr | 95 |
| http | 73 |
| socks | 72 |
| hysteria | 15 |
| anytls | 10 |
| tuic | 5 |

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
| 82.89 | shadowsocks | 204.8 | 520.7 | 23.04 | 0.0 | 10.0 | 13.85 | 20.0 | Au1rxx-base64 | 173.244.56.9 |
| 82.88 | shadowsocks | 205.1 | 520.1 | 23.03 | 0.0 | 10.0 | 13.85 | 20.0 | Au1rxx-base64 | 173.244.56.6 |
| 82.46 | shadowsocks | 201.8 | 496.6 | 23.11 | 0.0 | 10.0 | 13.85 | 20.0 | Au1rxx-base64 | 108.181.118.10 |
| 80.48 | shadowsocks | 287.2 | 738.1 | 21.13 | 0.0 | 10.0 | 13.85 | 20.0 | Au1rxx-base64 | 108.181.0.177 |
| 78.2 | shadowsocks | 321.9 | 722.8 | 20.33 | 0.0 | 10.0 | 13.85 | 20.0 | Au1rxx-base64 | 172.245.235.84 |
| 78.12 | shadowsocks | 296.5 | 662.4 | 20.92 | 0.0 | 10.0 | 13.85 | 20.0 | Au1rxx-base64 | 156.146.38.167 |
| 78.07 | trojan | 333.6 | 752.3 | 20.06 | 0.0 | 10.0 | 14.42 | 20.0 | Au1rxx-base64 | 64.94.95.114 |
| 77.98 | trojan | 343.0 | 780.3 | 19.84 | 0.0 | 10.0 | 14.42 | 20.0 | Au1rxx-base64 | 64.94.95.117 |
| 77.86 | shadowsocks | 296.4 | 673.5 | 20.92 | 0.0 | 10.0 | 13.85 | 20.0 | Au1rxx-base64 | 156.146.38.169 |
| 77.81 | trojan | 335.3 | 749.9 | 20.02 | 0.0 | 10.0 | 14.42 | 20.0 | Au1rxx-base64 | 64.94.95.118 |
| 77.72 | trojan | 336.9 | 761.5 | 19.98 | 0.0 | 10.0 | 14.42 | 20.0 | Au1rxx-base64 | 64.94.95.115 |
| 77.05 | hysteria2 | 352.5 | 728.6 | 19.62 | 0.0 | 10.0 | 13.0 | 20.0 | Au1rxx-base64 | 159.223.157.129 |
| 76.93 | trojan | 330.6 | 675.2 | 20.13 | 0.0 | 10.0 | 14.42 | 20.0 | Au1rxx-base64 | 163.245.196.68 |
| 75.82 | trojan | 367.7 | 753.3 | 19.27 | 0.0 | 10.0 | 14.42 | 20.0 | Au1rxx-base64 | 148.72.168.35 |
| 75.44 | shadowsocks | 275.1 | 279.2 | 21.41 | 4.53 | 9.94 | 13.85 | 20.0 | Au1rxx-base64 | 149.22.87.204 |
| 75.28 | shadowsocks | 297.7 | 354.1 | 20.89 | 1.72 | 9.95 | 13.85 | 20.0 | Au1rxx-base64 | 149.22.87.241 |
| 73.49 | shadowsocks | 373.4 | 746.7 | 19.13 | 0.0 | 10.0 | 13.85 | 20.0 | Au1rxx-base64 | 37.19.198.243 |
| 73.34 | vless | 243.8 | 583.4 | 22.13 | 0.0 | 10.0 | 4.83 | 18.9 | mheidari-all | 185.164.111.48 |
| 73.07 | shadowsocks | 294.8 | 662.5 | 20.95 | 0.0 | 10.0 | 13.85 | 20.0 | Au1rxx-base64 | 156.146.38.170 |
| 73.06 | shadowsocks | 385.2 | 792.3 | 18.86 | 0.0 | 10.0 | 13.85 | 20.0 | Au1rxx-base64 | 37.19.198.244 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.989 | 1.0 | 69 | 81 | prefer |
| Au1rxx-base64 | 0.961 | 0.909 | 408 | 1345 | prefer |
| DeltaKronecker-all | 0.637 | 0.558 | 104 | 5965 | observe |
| Surfboard-tg-mixed | 0.636 | 0.558 | 43 | 5743 | observe |
| mheidari-all | 0.593 | 0.513 | 300 | 18776 | observe |
| Barabama-yudou | 0.318 | 1.0 | 2 | 166 | observe |
| xiaoji235-airport-v2ray-all | 0.259 | 0.333 | 3 | 3959 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4972 | observe |
| Epodonios-all | 0.255 | None | 0 | 6749 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3972 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6579 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4586 | observe |
| barry-far-vless | 0.255 | None | 0 | 5112 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4991 | observe |
| Au1rxx-clash | 0.229 | None | 0 | 1345 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 91 |
| cn-block | TimeoutError | - | 30 |
| speed | ClientOSError | - | 27 |
| 204 | TimeoutError | - | 21 |
| speed | TimeoutError | - | 21 |
| 204 | ProxyError | - | 20 |
| geo | ClientOSError | - | 19 |
| cn-block | ProxyError | - | 8 |
| cn-block | ClientOSError | - | 6 |
| geo | ProxyError | - | 6 |
| 204 | ClientOSError | - | 4 |
| speed | ProxyError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
