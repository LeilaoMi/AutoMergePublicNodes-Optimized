# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-11-07 06:16:39 |
| 运行耗时 | 254.7s |
| 订阅源总数 | 107 |
| 健康订阅源 | 86 |
| 原始节点 | 81836 |
| 去重后节点 | 26377 |
| TCP 可达 | 3000 |
| 真实可用 | 385 |
| Verified 输出 | 68 |
| Global 输出 | 300 |
| All 输出 | 26377 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.9 |
| geo | 1.5 |
| tcp | 77.0 |
| probe | 78.0 |
| real_test | 58.1 |
| china_check | 24.7 |
| write_verified | 0.0 |
| generate | 10.5 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 49018 |
| vmess | 14216 |
| shadowsocks | 9371 |
| trojan | 7219 |
| hysteria2 | 1530 |
| http | 187 |
| shadowsocksr | 151 |
| socks | 75 |
| hysteria | 34 |
| anytls | 20 |
| tuic | 15 |

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
| 94.04 | shadowsocks | 254.3 | 3.2 | 21.89 | 14.88 | 10.0 | 14.21 | 17.06 | Au1rxx-base64 | 37.19.198.244 |
| 93.52 | shadowsocks | 280.9 | 0.8 | 21.28 | 14.97 | 10.0 | 14.21 | 17.06 | Au1rxx-base64 | 37.19.198.243 |
| 93.37 | shadowsocks | 264.8 | 1.3 | 21.65 | 14.95 | 10.0 | 14.21 | 17.06 | Au1rxx-base64 | 45.86.51.18 |
| 93.31 | shadowsocks | 268.1 | 0.9 | 21.57 | 14.97 | 10.0 | 14.21 | 17.06 | Au1rxx-base64 | 185.230.230.18 |
| 93.11 | shadowsocks | 295.9 | 2.3 | 20.93 | 14.91 | 10.0 | 14.21 | 17.06 | Au1rxx-base64 | 156.146.38.168 |
| 93.11 | shadowsocks | 296.5 | 2.0 | 20.91 | 14.93 | 10.0 | 14.21 | 17.06 | Au1rxx-base64 | 156.146.38.167 |
| 92.37 | shadowsocks | 318.3 | 2.8 | 20.41 | 14.9 | 10.0 | 14.21 | 17.06 | Au1rxx-base64 | 37.19.198.160 |
| 92.02 | shadowsocks | 295.2 | 5.0 | 20.94 | 14.81 | 10.0 | 14.21 | 17.06 | Au1rxx-base64 | 37.19.198.236 |
| 91.75 | vless | 331.7 | 0.1 | 20.1 | 14.99 | 8.87 | 10.73 | 17.06 | Au1rxx-base64 | 169.40.42.202 |
| 91.4 | shadowsocks | 311.2 | 1.2 | 20.57 | 14.95 | 10.0 | 14.21 | 17.06 | Au1rxx-base64 | 193.151.160.9 |
| 90.05 | vless | 399.0 | 0.1 | 18.54 | 15.0 | 8.88 | 10.73 | 17.06 | Au1rxx-base64 | 169.40.42.90 |
| 89.73 | shadowsocks | 295.5 | 0.5 | 20.94 | 14.98 | 8.22 | 14.21 | 17.06 | Au1rxx-base64 | 193.151.160.18 |
| 88.83 | http | 251.9 | 0.5 | 21.95 | 14.98 | 0.0 | 14.56 | 19.84 | ermaozi | 172.64.69.89 |
| 88.75 | http | 255.5 | 0.2 | 21.86 | 14.99 | 0.0 | 14.56 | 19.84 | ermaozi | 172.64.68.89 |
| 88.09 | vless | 288.1 | 1.4 | 21.11 | 14.95 | 8.88 | 10.73 | 17.06 | Au1rxx-base64 | 167.17.69.171 |
| 88.03 | shadowsocks | 304.0 | 0.8 | 20.74 | 14.97 | 10.0 | 14.21 | 17.06 | Au1rxx-base64 | 173.244.56.9 |
| 88.01 | shadowsocks | 306.7 | 1.3 | 20.68 | 14.95 | 10.0 | 14.21 | 17.06 | Au1rxx-base64 | 173.244.56.6 |
| 87.91 | shadowsocks | 298.4 | 3.6 | 20.87 | 14.86 | 10.0 | 14.21 | 17.06 | Au1rxx-base64 | 95.215.201.18 |
| 87.83 | http | 292.3 | 2.1 | 21.01 | 14.92 | 0.0 | 14.56 | 19.84 | ermaozi | 149.88.21.129 |
| 87.34 | shadowsocks | 255.2 | 0.3 | 21.87 | 14.99 | 10.0 | 14.21 | 17.06 | Au1rxx-base64 | 156.146.38.170 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 1.0 | 1.0 | 59 | 562 | prefer |
| Au1rxx-base64 | 0.933 | 0.866 | 224 | 1751 | prefer |
| mheidari-all | 0.806 | 0.729 | 166 | 13634 | prefer |
| Surfboard-tg-mixed | 0.609 | 0.75 | 12 | 8637 | observe |
| tg-LonUp_M | 0.262 | 1.0 | 1 | 178 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4934 | observe |
| DeltaKronecker-all | 0.255 | None | 0 | 2768 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 11015 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 6148 | observe |
| barry-far-vless | 0.255 | None | 0 | 6359 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4540 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.245 | None | 0 | 1751 | observe |
| xiaoji235-airport-v2ray-all | 0.24 | 0.25 | 4 | 6752 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 49 |
| 204 | ProxyError | - | 14 |
| 204 | TimeoutError | - | 8 |
| geo | ClientOSError | - | 4 |
| speed | ClientOSError | - | 3 |
| cn-block | ClientOSError | - | 1 |
| 204 | ClientOSError | - | 1 |
| cn-block | TimeoutError | - | 1 |
| speed | ClientPayloadError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 123 | 68 | - |
| global | False | 282 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
