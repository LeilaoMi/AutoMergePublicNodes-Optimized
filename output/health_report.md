# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-11-10 19:56:36 |
| 运行耗时 | 290.0s |
| 订阅源总数 | 107 |
| 健康订阅源 | 86 |
| 原始节点 | 82772 |
| 去重后节点 | 27016 |
| TCP 可达 | 3000 |
| 真实可用 | 406 |
| Verified 输出 | 93 |
| Global 输出 | 300 |
| All 输出 | 27016 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.9 |
| geo | 1.5 |
| tcp | 76.7 |
| probe | 90.5 |
| real_test | 76.9 |
| china_check | 25.9 |
| write_verified | 0.0 |
| generate | 12.5 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 50557 |
| vmess | 14240 |
| shadowsocks | 9098 |
| trojan | 6751 |
| hysteria2 | 1577 |
| http | 279 |
| shadowsocksr | 152 |
| socks | 52 |
| hysteria | 30 |
| anytls | 19 |
| tuic | 17 |

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
| 94.62 | shadowsocks | 246.6 | 4.1 | 22.07 | 14.85 | 10.0 | 13.76 | 17.94 | Au1rxx-base64 | 156.146.38.167 |
| 94.36 | shadowsocks | 244.9 | 1.0 | 22.11 | 14.96 | 10.0 | 13.76 | 17.94 | Au1rxx-base64 | 156.146.38.168 |
| 94.36 | shadowsocks | 259.6 | 2.8 | 21.77 | 14.89 | 10.0 | 13.76 | 17.94 | Au1rxx-base64 | 156.146.38.170 |
| 93.28 | shadowsocks | 267.9 | 4.6 | 21.58 | 14.83 | 9.67 | 13.76 | 17.94 | Au1rxx-base64 | 193.151.160.18 |
| 93.0 | shadowsocks | 285.7 | 0.3 | 21.16 | 14.99 | 10.0 | 13.76 | 17.94 | Au1rxx-base64 | 193.151.163.18 |
| 92.49 | shadowsocks | 291.9 | 19.6 | 21.02 | 14.27 | 10.0 | 13.76 | 17.94 | Au1rxx-base64 | 193.151.160.9 |
| 92.1 | vless | 303.4 | 6.5 | 20.75 | 14.76 | 9.98 | 9.35 | 17.94 | Au1rxx-base64 | 159.89.87.21 |
| 91.73 | vless | 315.7 | 2.2 | 20.47 | 14.92 | 10.0 | 9.35 | 17.94 | Au1rxx-base64 | 167.17.69.171 |
| 91.59 | trojan | 335.0 | 4.4 | 20.02 | 14.84 | 10.0 | 12.79 | 17.94 | Au1rxx-base64 | 66.23.203.21 |
| 91.09 | shadowsocks | 257.6 | 8.3 | 21.82 | 14.69 | 6.96 | 13.76 | 17.94 | Au1rxx-base64 | 156.146.38.169 |
| 90.14 | shadowsocks | 284.8 | 0.3 | 21.18 | 14.99 | 10.0 | 13.76 | 17.94 | Au1rxx-base64 | 95.215.201.18 |
| 89.72 | vless | 324.4 | 6.4 | 20.27 | 14.76 | 10.0 | 9.35 | 17.94 | Au1rxx-base64 | 66.70.179.198 |
| 89.42 | trojan | 467.7 | 6.8 | 16.95 | 14.74 | 10.0 | 12.79 | 17.94 | Au1rxx-base64 | 69.164.240.85 |
| 89.3 | vless | 383.2 | 24.9 | 18.91 | 14.07 | 10.0 | 9.35 | 17.94 | Au1rxx-base64 | 169.40.42.202 |
| 89.05 | trojan | 311.2 | 7.2 | 20.57 | 14.73 | 9.37 | 12.79 | 17.94 | Au1rxx-base64 | 66.163.112.242 |
| 88.28 | shadowsocks | 279.7 | 139.2 | 21.3 | 9.78 | 10.0 | 13.76 | 17.94 | Au1rxx-base64 | 45.86.51.18 |
| 87.46 | trojan | 315.2 | 7.7 | 20.48 | 14.71 | 8.38 | 12.79 | 17.94 | Au1rxx-base64 | 66.163.112.76 |
| 87.34 | shadowsocks | 520.3 | 15.8 | 15.73 | 14.41 | 10.0 | 13.76 | 17.94 | Au1rxx-base64 | 185.230.230.18 |
| 87.01 | vless | 308.3 | 2.6 | 20.64 | 14.9 | 6.28 | 9.35 | 17.94 | Au1rxx-base64 | 172.67.199.126 |
| 86.71 | trojan | 304.6 | 0.8 | 20.73 | 14.97 | 6.64 | 12.79 | 17.94 | Au1rxx-base64 | 66.163.112.31 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.956 | 0.944 | 71 | 619 | prefer |
| mheidari-all | 0.858 | 0.784 | 97 | 14274 | prefer |
| Au1rxx-base64 | 0.782 | 0.714 | 182 | 1751 | prefer |
| Surfboard-tg-mixed | 0.716 | 0.638 | 207 | 8562 | prefer |
| ninja-vless | 0.327 | 1.0 | 1 | 1791 | observe |
| DeltaKronecker-all | 0.287 | 0.5 | 2 | 2620 | observe |
| xiaoji235-airport-v2ray-all | 0.287 | 0.5 | 2 | 6752 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4955 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 11116 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 6459 | observe |
| barry-far-vless | 0.255 | None | 0 | 6491 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4667 | observe |
| Au1rxx-clash | 0.245 | None | 0 | 1751 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 62 |
| 204 | ProxyError | - | 32 |
| speed | ClientOSError | - | 14 |
| 204 | TimeoutError | - | 11 |
| cn-block | ProxyError | - | 9 |
| 204 | ClientOSError | - | 6 |
| geo | ProxyError | - | 6 |
| cn-block | TimeoutError | - | 5 |
| speed | ProxyError | - | 4 |
| geo | ClientOSError | - | 3 |
| speed | TimeoutError | - | 2 |
| cn-block | ClientOSError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 108 | 93 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
