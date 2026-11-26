# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-11-26 08:40:36 |
| 运行耗时 | 258.5s |
| 订阅源总数 | 107 |
| 健康订阅源 | 85 |
| 原始节点 | 78785 |
| 去重后节点 | 27338 |
| TCP 可达 | 3000 |
| 真实可用 | 320 |
| Verified 输出 | 54 |
| Global 输出 | 300 |
| All 输出 | 27338 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.7 |
| geo | 1.4 |
| tcp | 80.4 |
| probe | 78.0 |
| real_test | 63.5 |
| china_check | 19.2 |
| write_verified | 0.0 |
| generate | 11.2 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 46639 |
| vmess | 15115 |
| shadowsocks | 9381 |
| trojan | 5555 |
| hysteria2 | 1623 |
| shadowsocksr | 156 |
| socks | 123 |
| http | 109 |
| anytls | 41 |
| hysteria | 31 |
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
| 96.12 | shadowsocks | 240.4 | 1.0 | 22.21 | 14.96 | 10.0 | 13.05 | 19.9 | Au1rxx-base64 | 37.19.198.236 |
| 96.0 | shadowsocks | 246.2 | 0.7 | 22.08 | 14.97 | 10.0 | 13.05 | 19.9 | Au1rxx-base64 | 37.19.198.244 |
| 95.97 | shadowsocks | 246.1 | 1.5 | 22.08 | 14.94 | 10.0 | 13.05 | 19.9 | Au1rxx-base64 | 37.19.198.243 |
| 95.65 | shadowsocks | 240.2 | 0.6 | 22.22 | 14.98 | 10.0 | 13.05 | 19.9 | Au1rxx-base64 | 45.86.51.18 |
| 95.59 | shadowsocks | 241.9 | 1.0 | 22.18 | 14.96 | 10.0 | 13.05 | 19.9 | Au1rxx-base64 | 185.230.230.18 |
| 95.34 | shadowsocks | 253.6 | 0.5 | 21.91 | 14.98 | 10.0 | 13.05 | 19.9 | Au1rxx-base64 | 193.151.163.18 |
| 94.99 | trojan | 280.8 | 0.7 | 21.28 | 14.97 | 9.84 | 12.0 | 19.9 | Au1rxx-base64 | 69.164.240.85 |
| 94.35 | vless | 353.7 | 2.3 | 19.59 | 14.91 | 10.0 | 11.69 | 19.9 | Au1rxx-base64 | 169.40.42.74 |
| 94.05 | vless | 365.4 | 1.3 | 19.32 | 14.95 | 9.22 | 11.69 | 19.9 | Au1rxx-base64 | 169.40.42.202 |
| 93.93 | shadowsocks | 314.8 | 0.3 | 20.49 | 14.99 | 10.0 | 13.05 | 19.9 | Au1rxx-base64 | 193.151.160.9 |
| 93.72 | vless | 362.5 | 0.9 | 19.39 | 14.96 | 7.92 | 11.69 | 19.9 | Au1rxx-base64 | 169.40.42.229 |
| 92.56 | shadowsocks | 300.7 | 1.9 | 20.82 | 14.93 | 8.73 | 13.05 | 19.9 | Au1rxx-base64 | 193.151.160.18 |
| 92.31 | shadowsocks | 332.7 | 4.8 | 20.08 | 14.82 | 10.0 | 13.05 | 19.9 | Au1rxx-base64 | 156.146.38.170 |
| 92.05 | shadowsocks | 241.3 | 3.1 | 22.19 | 14.88 | 10.0 | 13.05 | 19.9 | Au1rxx-base64 | 37.19.198.160 |
| 91.74 | vless | 253.1 | 0.4 | 21.92 | 14.99 | 9.21 | 11.69 | 19.9 | Au1rxx-base64 | 159.89.87.21 |
| 89.9 | trojan | 374.5 | 2.9 | 19.11 | 14.89 | 10.0 | 12.0 | 19.9 | Au1rxx-base64 | 66.23.203.21 |
| 89.46 | vless | 334.4 | 1.7 | 20.04 | 14.94 | 9.19 | 11.69 | 19.9 | Au1rxx-base64 | 169.40.42.89 |
| 89.34 | shadowsocks | 308.5 | 0.3 | 20.64 | 14.99 | 10.0 | 13.05 | 19.9 | Au1rxx-base64 | 173.244.56.9 |
| 89.28 | shadowsocks | 309.5 | 0.1 | 20.61 | 14.99 | 10.0 | 13.05 | 19.9 | Au1rxx-base64 | 173.244.56.6 |
| 88.46 | vless | 372.8 | 2.9 | 19.15 | 14.89 | 9.33 | 11.69 | 19.9 | Au1rxx-base64 | 45.138.100.248 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.975 | 1.0 | 22 | 406 | prefer |
| Au1rxx-base64 | 0.831 | 0.765 | 136 | 1751 | prefer |
| mheidari-all | 0.83 | 0.759 | 58 | 14817 | prefer |
| Surfboard-tg-mixed | 0.805 | 0.727 | 209 | 8442 | prefer |
| ermaozi-get_subscribe | 0.381 | 0.8 | 5 | 363 | observe |
| xiaoji235-airport-v2ray-all | 0.335 | 1.0 | 1 | 6752 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 11584 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5447 | observe |
| barry-far-vless | 0.255 | None | 0 | 5694 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4485 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.245 | None | 0 | 1751 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |
| 10ium-HighSpeed | 0.209 | None | 0 | 839 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 45 |
| 204 | ProxyError | - | 28 |
| 204 | TimeoutError | - | 8 |
| 204 | ClientOSError | - | 5 |
| cn-block | ProxyError | - | 5 |
| cn-block | ClientOSError | - | 4 |
| cn-block | TimeoutError | - | 4 |
| geo | ProxyError | - | 3 |
| speed | TimeoutError | - | 3 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 81 | 54 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
