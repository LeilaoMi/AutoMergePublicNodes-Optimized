# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-27 14:53:16 |
| 运行耗时 | 315.5s |
| 订阅源总数 | 107 |
| 健康订阅源 | 102 |
| 原始节点 | 85525 |
| 去重后节点 | 22983 |
| TCP 可达 | 3000 |
| 真实可用 | 698 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22983 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.7 |
| geo | 1.4 |
| tcp | 32.5 |
| probe | 63.2 |
| real_test | 172.0 |
| generate | 40.7 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 48275 |
| trojan | 15968 |
| vmess | 10401 |
| shadowsocks | 9890 |
| hysteria2 | 704 |
| shadowsocksr | 109 |
| socks | 69 |
| http | 64 |
| anytls | 22 |
| hysteria | 15 |
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
| 80.37 | shadowsocks | 252.7 | 604.6 | 21.93 | 0.0 | 10.0 | 12.94 | 19.5 | Au1rxx-base64 | 173.244.56.6 |
| 79.75 | shadowsocks | 262.8 | 631.4 | 21.69 | 0.0 | 10.0 | 12.94 | 19.5 | Au1rxx-base64 | 156.146.38.168 |
| 79.52 | shadowsocks | 257.7 | 624.2 | 21.81 | 0.0 | 10.0 | 12.94 | 19.5 | Au1rxx-base64 | 156.146.38.169 |
| 79.51 | shadowsocks | 203.2 | 509.0 | 23.07 | 0.0 | 10.0 | 12.94 | 19.5 | Au1rxx-base64 | 173.244.56.9 |
| 78.93 | shadowsocks | 260.5 | 633.2 | 21.75 | 0.0 | 10.0 | 12.94 | 19.5 | Au1rxx-base64 | 156.146.38.170 |
| 77.69 | shadowsocks | 267.3 | 646.8 | 21.59 | 0.0 | 10.0 | 12.94 | 19.5 | Au1rxx-base64 | 156.146.38.167 |
| 76.62 | shadowsocks | 264.4 | 555.4 | 21.66 | 0.0 | 10.0 | 12.94 | 19.5 | Au1rxx-base64 | 149.22.95.183 |
| 76.16 | trojan | 319.9 | 734.9 | 20.37 | 0.0 | 10.0 | 13.02 | 19.5 | Au1rxx-base64 | 64.94.95.117 |
| 76.02 | trojan | 383.3 | 926.9 | 18.91 | 0.0 | 10.0 | 13.02 | 19.5 | Au1rxx-base64 | 64.94.95.115 |
| 74.94 | trojan | 384.6 | 926.5 | 18.87 | 0.0 | 10.0 | 13.02 | 19.5 | Au1rxx-base64 | 64.94.95.118 |
| 74.51 | trojan | 440.0 | 1099.3 | 17.59 | 0.0 | 10.0 | 13.02 | 19.5 | Au1rxx-base64 | 64.94.95.114 |
| 73.84 | shadowsocks | 302.4 | 347.6 | 20.78 | 1.96 | 9.91 | 12.94 | 19.5 | Au1rxx-base64 | 149.22.87.240 |
| 73.72 | shadowsocks | 302.6 | 350.7 | 20.77 | 1.85 | 9.9 | 12.94 | 19.5 | Au1rxx-base64 | 149.22.87.241 |
| 73.6 | trojan | 458.9 | 1141.9 | 17.15 | 0.0 | 10.0 | 13.02 | 19.5 | Au1rxx-base64 | 163.245.196.68 |
| 73.59 | shadowsocks | 197.8 | 499.7 | 23.2 | 0.0 | 10.0 | 12.94 | 19.5 | Au1rxx-base64 | 216.105.168.18 |
| 73.28 | shadowsocks | 341.2 | 692.6 | 19.88 | 0.0 | 10.0 | 12.94 | 19.5 | Au1rxx-base64 | 198.98.53.130 |
| 72.88 | shadowsocks | 352.8 | 733.1 | 19.61 | 0.0 | 10.0 | 12.94 | 19.5 | Au1rxx-base64 | 37.19.198.160 |
| 72.68 | shadowsocks | 356.7 | 734.9 | 19.52 | 0.0 | 10.0 | 12.94 | 19.5 | Au1rxx-base64 | 37.19.198.244 |
| 72.22 | trojan | 212.4 | 508.8 | 22.86 | 0.0 | 10.0 | 13.02 | 14.1 | Surfboard-tg-mixed | 46.202.30.27 |
| 72.17 | shadowsocks | 359.0 | 742.3 | 19.47 | 0.0 | 10.0 | 12.94 | 19.5 | Au1rxx-base64 | 108.181.57.93 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.988 | 0.93 | 415 | 1507 | prefer |
| zhangkai | 0.97 | 0.983 | 59 | 74 | prefer |
| mheidari-all | 0.779 | 0.702 | 121 | 19227 | prefer |
| DeltaKronecker-all | 0.623 | 0.543 | 138 | 5643 | observe |
| Surfboard-tg-mixed | 0.535 | 0.454 | 196 | 5641 | observe |
| tg-oneclickvpnkeys | 0.371 | 0.8 | 5 | 131 | observe |
| xiaoji235-airport-v2ray-all | 0.259 | 0.333 | 3 | 3959 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4831 | observe |
| Epodonios-all | 0.255 | None | 0 | 6520 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3970 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6628 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4484 | observe |
| barry-far-vless | 0.255 | None | 0 | 4866 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5017 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 60 |
| speed | ClientOSError | - | 45 |
| cn-block | TimeoutError | - | 29 |
| 204 | ProxyError | - | 28 |
| 204 | TimeoutError | - | 22 |
| geo | ClientOSError | - | 20 |
| speed | TimeoutError | - | 10 |
| cn-block | ProxyError | - | 9 |
| cn-block | ClientOSError | - | 8 |
| 204 | ClientOSError | - | 4 |
| geo | ProxyError | - | 4 |
| speed | ProxyError | - | 3 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
