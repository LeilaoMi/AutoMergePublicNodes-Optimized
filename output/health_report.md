# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-28 13:37:14 |
| 运行耗时 | 606.3s |
| 订阅源总数 | 107 |
| 健康订阅源 | 94 |
| 原始节点 | 96149 |
| 去重后节点 | 26789 |
| TCP 可达 | 3000 |
| 真实可用 | 463 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 26789 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.4 |
| geo | 1.4 |
| tcp | 45.7 |
| probe | 272.5 |
| real_test | 189.9 |
| generate | 92.4 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 58652 |
| vmess | 14819 |
| shadowsocks | 11430 |
| trojan | 8868 |
| hysteria2 | 1473 |
| http | 617 |
| shadowsocksr | 169 |
| socks | 74 |
| anytls | 24 |
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
| 80.12 | hysteria2 | 248.4 | 550.5 | 22.03 | 0.0 | 9.87 | 11.74 | 18.24 | Au1rxx-base64 | 192.255.128.123 |
| 78.73 | shadowsocks | 241.2 | 590.4 | 22.2 | 0.0 | 9.94 | 13.35 | 18.24 | Au1rxx-base64 | 156.146.38.169 |
| 78.25 | shadowsocks | 307.3 | 755.1 | 20.66 | 0.0 | 10.0 | 13.35 | 18.24 | Au1rxx-base64 | 37.19.198.244 |
| 77.82 | shadowsocks | 257.0 | 629.6 | 21.83 | 0.0 | 9.92 | 13.35 | 18.24 | Au1rxx-base64 | 156.146.38.168 |
| 77.68 | shadowsocks | 307.0 | 755.2 | 20.67 | 0.0 | 10.0 | 13.35 | 18.24 | Au1rxx-base64 | 37.19.198.236 |
| 77.61 | hysteria2 | 287.4 | 660.6 | 21.12 | 0.0 | 10.0 | 11.74 | 18.24 | Au1rxx-base64 | 66.94.121.46 |
| 77.54 | shadowsocks | 265.9 | 602.7 | 21.62 | 0.0 | 10.0 | 13.35 | 18.24 | Au1rxx-base64 | 23.150.248.20 |
| 76.71 | vless | 254.5 | 630.9 | 21.89 | 0.0 | 9.9 | 6.68 | 18.24 | Au1rxx-base64 | 195.211.98.43 |
| 76.47 | shadowsocks | 337.3 | 872.5 | 19.97 | 0.0 | 9.41 | 13.35 | 18.24 | Au1rxx-base64 | yyz-ca-01.blncvpn4u.cc |
| 76.1 | vless | 281.0 | 718.3 | 21.27 | 0.0 | 9.91 | 6.68 | 18.24 | Au1rxx-base64 | 79.141.172.154 |
| 75.28 | shadowsocks | 304.5 | 741.9 | 20.73 | 0.0 | 9.9 | 13.35 | 18.24 | Au1rxx-base64 | 37.19.198.160 |
| 74.36 | shadowsocks | 284.4 | 595.5 | 21.2 | 0.0 | 9.88 | 13.35 | 18.24 | Au1rxx-base64 | 173.244.56.9 |
| 73.55 | shadowsocks | 246.9 | 614.9 | 22.06 | 0.0 | 10.0 | 13.35 | 15.68 | Surfboard-tg-mixed | 156.146.38.167 |
| 73.24 | shadowsocks | 350.1 | 777.7 | 19.67 | 0.0 | 9.9 | 13.35 | 18.24 | Au1rxx-base64 | 149.22.95.183 |
| 73.22 | shadowsocks | 408.4 | 1099.6 | 18.32 | 0.0 | 9.88 | 13.35 | 18.24 | Au1rxx-base64 | 185.156.47.97 |
| 72.92 | shadowsocks | 376.8 | 912.7 | 19.06 | 0.0 | 9.91 | 13.35 | 18.24 | Au1rxx-base64 | 15.204.247.206 |
| 72.73 | shadowsocks | 359.9 | 828.4 | 19.45 | 0.0 | 9.91 | 13.35 | 18.24 | Au1rxx-base64 | 108.181.57.93 |
| 72.56 | shadowsocks | 401.4 | 1000.7 | 18.49 | 0.0 | 9.89 | 13.35 | 18.24 | Au1rxx-base64 | 198.98.53.130 |
| 72.52 | vless | 319.2 | 749.0 | 20.39 | 0.0 | 9.92 | 6.68 | 18.24 | Au1rxx-base64 | 47.90.153.88 |
| 72.4 | vless | 339.0 | 781.7 | 19.93 | 0.0 | 9.9 | 6.68 | 18.24 | Au1rxx-base64 | 169.40.42.104 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.927 | 0.862 | 311 | 1677 | prefer |
| mheidari-all | 0.88 | 0.81 | 58 | 22474 | prefer |
| Surfboard-tg-mixed | 0.814 | 0.737 | 137 | 7046 | prefer |
| ermaozi | 0.72 | 0.714 | 49 | 344 | prefer |
| DeltaKronecker-all | 0.573 | 0.6 | 15 | 5428 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| tg-oneclickvpnkeys | 0.259 | 1.0 | 1 | 94 | observe |
| tg-OutlineReleasedKey | 0.257 | 1.0 | 1 | 50 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5326 | observe |
| Epodonios-all | 0.255 | None | 0 | 7414 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9420 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5638 | observe |
| barry-far-vless | 0.255 | None | 0 | 5752 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4185 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| cn-block | TimeoutError | - | 27 |
| 204 | ProxyError | - | 22 |
| 204 | TimeoutError | - | 20 |
| speed | ClientOSError | - | 19 |
| speed | TimeoutError | - | 7 |
| geo | TimeoutError | - | 6 |
| cn-block | ProxyError | - | 4 |
| 204 | ClientOSError | - | 3 |
| cn-block | ClientOSError | - | 3 |
| geo | ProxyError | - | 2 |
| geo | ClientOSError | - | 1 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
