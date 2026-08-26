# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-26 13:06:14 |
| 运行耗时 | 253.6s |
| 订阅源总数 | 107 |
| 健康订阅源 | 96 |
| 原始节点 | 78650 |
| 去重后节点 | 22232 |
| TCP 可达 | 3000 |
| 真实可用 | 518 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22232 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.5 |
| geo | 1.4 |
| tcp | 36.4 |
| probe | 56.9 |
| real_test | 118.6 |
| generate | 33.7 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 49668 |
| shadowsocks | 10445 |
| vmess | 10247 |
| trojan | 6430 |
| hysteria2 | 1484 |
| http | 172 |
| shadowsocksr | 129 |
| socks | 65 |
| hysteria | 7 |
| tuic | 3 |

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
| 78.11 | vless | 265.4 | 595.1 | 21.63 | 0.0 | 10.0 | 9.73 | 18.24 | Au1rxx-base64 | 15.204.97.197 |
| 77.94 | vless | 263.7 | 593.8 | 21.67 | 0.0 | 10.0 | 9.73 | 18.24 | Au1rxx-base64 | 15.204.97.216 |
| 77.75 | shadowsocks | 241.7 | 622.9 | 22.18 | 0.0 | 10.0 | 13.83 | 15.74 | Surfboard-tg-mixed | 156.146.38.168 |
| 77.67 | shadowsocks | 245.5 | 634.4 | 22.1 | 0.0 | 10.0 | 13.83 | 15.74 | Surfboard-tg-mixed | 156.146.38.167 |
| 77.02 | shadowsocks | 251.6 | 611.6 | 21.95 | 0.0 | 10.0 | 13.83 | 15.74 | Surfboard-tg-mixed | 23.150.248.20 |
| 76.63 | vless | 273.4 | 581.6 | 21.45 | 0.0 | 10.0 | 9.73 | 18.24 | Au1rxx-base64 | 166.88.186.151 |
| 76.54 | vless | 347.1 | 841.0 | 19.74 | 0.0 | 10.0 | 9.73 | 18.24 | Au1rxx-base64 | 15.204.97.209 |
| 76.16 | vless | 414.3 | 1075.2 | 18.19 | 0.0 | 10.0 | 9.73 | 18.24 | Au1rxx-base64 | 38.180.242.205 |
| 76.04 | shadowsocks | 244.9 | 632.8 | 22.11 | 0.0 | 10.0 | 13.83 | 14.1 | mheidari-all | 156.146.38.169 |
| 76.03 | shadowsocks | 245.1 | 631.3 | 22.1 | 0.0 | 10.0 | 13.83 | 14.1 | mheidari-all | 156.146.38.170 |
| 75.86 | vless | 355.0 | 864.3 | 19.56 | 0.0 | 10.0 | 9.73 | 18.24 | Au1rxx-base64 | 15.204.97.195 |
| 75.67 | http | 445.6 | 1148.1 | 17.46 | 0.0 | 10.0 | 14.44 | 18.58 | zhangkai | 138.199.35.216 |
| 75.22 | trojan | 259.0 | 545.1 | 21.78 | 0.0 | 10.0 | 11.04 | 18.24 | Au1rxx-base64 | 14.1.28.76 |
| 75.02 | http | 450.5 | 1158.7 | 17.35 | 0.0 | 10.0 | 14.44 | 18.58 | zhangkai | 138.199.35.198 |
| 73.34 | vless | 372.3 | 657.3 | 19.16 | 0.0 | 10.0 | 9.73 | 18.24 | Au1rxx-base64 | 198.251.78.29 |
| 73.27 | vless | 258.3 | 543.8 | 21.8 | 0.0 | 10.0 | 9.73 | 18.24 | Au1rxx-base64 | 69.63.193.78 |
| 73.18 | trojan | 327.8 | 688.0 | 20.19 | 0.0 | 10.0 | 11.04 | 18.24 | Au1rxx-base64 | 35.91.251.124 |
| 72.94 | vless | 309.6 | 667.5 | 20.61 | 0.0 | 10.0 | 9.73 | 18.24 | Au1rxx-base64 | 195.211.99.45 |
| 72.94 | vless | 342.1 | 827.4 | 19.86 | 0.0 | 10.0 | 9.73 | 18.24 | Au1rxx-base64 | 15.204.97.214 |
| 72.85 | shadowsocks | 299.7 | 653.8 | 20.84 | 0.0 | 10.0 | 13.83 | 15.74 | Surfboard-tg-mixed | 198.98.53.130 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.978 | 0.901 | 323 | 1988 | prefer |
| DeltaKronecker-all | 0.933 | 0.875 | 32 | 6107 | prefer |
| zhangkai | 0.926 | 0.957 | 23 | 144 | prefer |
| Surfboard-tg-mixed | 0.8 | 0.723 | 166 | 6535 | prefer |
| mheidari-all | 0.692 | 0.614 | 83 | 14222 | observe |
| nscl5-all | 0.435 | 1.0 | 4 | 887 | observe |
| tg-oneclickvpnkeys | 0.319 | 1.0 | 2 | 206 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4825 | observe |
| Au1rxx-clash | 0.255 | None | 0 | 1992 | observe |
| Epodonios-all | 0.255 | None | 0 | 7011 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3988 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7145 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5395 | observe |
| barry-far-vless | 0.255 | None | 0 | 5628 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 3981 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | TimeoutError | - | 45 |
| 204 | TimeoutError | - | 20 |
| cn-block | TimeoutError | - | 19 |
| 204 | ProxyError | - | 8 |
| speed | ClientOSError | - | 6 |
| cn-block | ProxyError | - | 4 |
| geo | ClientOSError | - | 4 |
| cn-block | ClientOSError | - | 3 |
| 204 | ClientOSError | - | 2 |
| speed | ProxyError | - | 2 |
| geo | TimeoutError | - | 2 |
| sing-box exited 1 |  [31mFATAL[0m[0000] start service: start inbound/socks[socks-in]: listen tcp 127.0.0.1:49471: bind: address already in use | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
