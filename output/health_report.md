# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-28 22:47:31 |
| 运行耗时 | 315.5s |
| 订阅源总数 | 107 |
| 健康订阅源 | 87 |
| 原始节点 | 99282 |
| 去重后节点 | 27866 |
| TCP 可达 | 3000 |
| 真实可用 | 412 |
| Verified 输出 | 76 |
| Global 输出 | 300 |
| All 输出 | 27866 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.7 |
| geo | 1.7 |
| tcp | 85.1 |
| probe | 101.4 |
| real_test | 74.7 |
| china_check | 29.6 |
| write_verified | 0.0 |
| generate | 15.4 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 62967 |
| vmess | 14227 |
| shadowsocks | 10776 |
| trojan | 8681 |
| hysteria2 | 2260 |
| shadowsocksr | 165 |
| http | 116 |
| socks | 52 |
| tuic | 16 |
| hysteria | 11 |
| anytls | 11 |

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
| 94.43 | vless | 270.7 | 7.4 | 21.51 | 14.72 | 9.86 | 10.32 | 18.02 | Au1rxx-base64 | 167.17.69.171 |
| 93.5 | shadowsocks | 248.6 | 1.1 | 22.02 | 14.96 | 10.0 | 12.5 | 18.02 | Au1rxx-base64 | 37.19.198.244 |
| 93.29 | shadowsocks | 250.8 | 5.5 | 21.97 | 14.8 | 10.0 | 12.5 | 18.02 | Au1rxx-base64 | 37.19.198.160 |
| 93.16 | vless | 336.6 | 2.7 | 19.98 | 14.9 | 9.94 | 10.32 | 18.02 | Au1rxx-base64 | 169.40.42.229 |
| 92.91 | shadowsocks | 243.2 | 7.1 | 22.15 | 14.74 | 10.0 | 12.5 | 18.02 | Au1rxx-base64 | 193.151.163.18 |
| 92.67 | vless | 279.6 | 1.8 | 21.31 | 14.93 | 8.09 | 10.32 | 18.02 | Au1rxx-base64 | 195.123.235.183 |
| 92.35 | hysteria2 | 224.9 | 0.6 | 22.57 | 14.98 | 6.28 | 12.0 | 18.02 | Au1rxx-base64 | 129.213.91.185 |
| 92.23 | shadowsocks | 293.4 | 7.4 | 20.99 | 14.72 | 10.0 | 12.5 | 18.02 | Au1rxx-base64 | 37.19.198.243 |
| 92.17 | vless | 328.9 | 5.3 | 20.17 | 14.8 | 9.86 | 10.32 | 18.02 | Au1rxx-base64 | 169.40.42.163 |
| 90.96 | vless | 314.2 | 7.1 | 20.5 | 14.73 | 9.06 | 10.32 | 18.02 | Au1rxx-base64 | 5.34.178.120 |
| 90.86 | shadowsocks | 334.0 | 5.6 | 20.05 | 14.79 | 10.0 | 12.5 | 18.02 | Au1rxx-base64 | 45.86.51.18 |
| 90.76 | shadowsocks | 251.8 | 4.8 | 21.95 | 14.82 | 7.97 | 12.5 | 18.02 | Au1rxx-base64 | 185.230.230.18 |
| 90.39 | vless | 372.3 | 6.7 | 19.16 | 14.75 | 9.25 | 10.32 | 18.02 | Au1rxx-base64 | 169.40.42.89 |
| 90.33 | vless | 325.2 | 6.6 | 20.25 | 14.75 | 10.0 | 10.32 | 18.02 | Au1rxx-base64 | 169.40.42.74 |
| 90.0 | vless | 330.1 | 4.1 | 20.14 | 14.84 | 9.84 | 10.32 | 18.02 | Au1rxx-base64 | 169.40.42.104 |
| 89.29 | shadowsocks | 285.1 | 1.5 | 21.18 | 14.94 | 10.0 | 12.5 | 18.02 | Au1rxx-base64 | 156.146.38.170 |
| 89.29 | vless | 306.5 | 18.3 | 20.68 | 14.31 | 9.76 | 10.32 | 18.02 | Au1rxx-base64 | 66.70.179.198 |
| 89.18 | vless | 371.4 | 4.6 | 19.18 | 14.83 | 9.83 | 10.32 | 18.02 | Au1rxx-base64 | 169.40.42.90 |
| 89.16 | vless | 320.3 | 7.3 | 20.36 | 14.72 | 9.94 | 10.32 | 18.02 | Au1rxx-base64 | 169.40.42.35 |
| 89.16 | shadowsocks | 393.3 | 0.9 | 18.67 | 14.97 | 10.0 | 12.5 | 18.02 | Au1rxx-base64 | 193.151.160.18 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.956 | 0.966 | 29 | 513 | prefer |
| Au1rxx-base64 | 0.951 | 0.884 | 310 | 1746 | prefer |
| Surfboard-tg-mixed | 0.853 | 0.938 | 16 | 7686 | prefer |
| mheidari-all | 0.65 | 0.571 | 163 | 33849 | observe |
| DeltaKronecker-all | 0.335 | 1.0 | 1 | 2801 | observe |
| xiaoji235-airport-v2ray-all | 0.335 | 1.0 | 1 | 6752 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5004 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 10359 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5749 | observe |
| barry-far-vless | 0.255 | None | 0 | 5963 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4323 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.245 | None | 0 | 1746 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 68 |
| geo | ClientOSError | - | 11 |
| cn-block | ClientOSError | - | 7 |
| 204 | ClientOSError | - | 6 |
| 204 | ProxyError | - | 6 |
| 204 | TimeoutError | - | 4 |
| cn-block | ProxyError | - | 2 |
| cn-block | TimeoutError | - | 1 |
| speed | ClientOSError | - | 1 |
| speed | TimeoutError | - | 1 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 66 | 76 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
