# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-11-25 08:55:17 |
| 运行耗时 | 312.6s |
| 订阅源总数 | 107 |
| 健康订阅源 | 86 |
| 原始节点 | 78303 |
| 去重后节点 | 27473 |
| TCP 可达 | 3000 |
| 真实可用 | 381 |
| Verified 输出 | 80 |
| Global 输出 | 300 |
| All 输出 | 27473 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.6 |
| geo | 1.6 |
| tcp | 82.5 |
| probe | 94.6 |
| real_test | 85.1 |
| china_check | 27.4 |
| write_verified | 0.0 |
| generate | 14.9 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 46752 |
| vmess | 14977 |
| shadowsocks | 9010 |
| trojan | 5403 |
| hysteria2 | 1625 |
| http | 203 |
| shadowsocksr | 151 |
| socks | 113 |
| anytls | 34 |
| hysteria | 23 |
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
| 96.65 | shadowsocks | 248.6 | 4.2 | 22.02 | 14.84 | 10.0 | 13.79 | 20.0 | Au1rxx-base64 | 156.146.38.168 |
| 96.14 | shadowsocks | 274.6 | 0.6 | 21.42 | 14.98 | 10.0 | 13.79 | 20.0 | Au1rxx-base64 | 37.19.198.244 |
| 95.42 | shadowsocks | 288.5 | 0.7 | 21.1 | 14.97 | 10.0 | 13.79 | 20.0 | Au1rxx-base64 | 37.19.198.160 |
| 94.53 | shadowsocks | 344.3 | 1.8 | 19.81 | 14.93 | 10.0 | 13.79 | 20.0 | Au1rxx-base64 | 37.19.198.243 |
| 93.41 | shadowsocks | 368.0 | 3.8 | 19.26 | 14.86 | 10.0 | 13.79 | 20.0 | Au1rxx-base64 | 45.86.51.18 |
| 93.28 | shadowsocks | 349.8 | 3.9 | 19.68 | 14.85 | 10.0 | 13.79 | 20.0 | Au1rxx-base64 | 37.19.198.236 |
| 92.95 | trojan | 265.6 | 7.3 | 21.63 | 14.73 | 8.55 | 13.54 | 20.0 | Au1rxx-base64 | 216.152.155.59 |
| 92.92 | shadowsocks | 245.3 | 1.1 | 22.1 | 14.96 | 6.07 | 13.79 | 20.0 | Au1rxx-base64 | 156.146.38.169 |
| 92.62 | vless | 292.3 | 2.1 | 21.01 | 14.92 | 7.79 | 12.08 | 20.0 | Au1rxx-base64 | 195.123.235.183 |
| 91.13 | shadowsocks | 311.8 | 0.6 | 20.56 | 14.98 | 10.0 | 13.79 | 20.0 | Au1rxx-base64 | 185.230.230.18 |
| 91.05 | shadowsocks | 340.0 | 4.1 | 19.91 | 14.85 | 10.0 | 13.79 | 20.0 | Au1rxx-base64 | 193.151.160.9 |
| 90.97 | shadowsocks | 305.8 | 1.3 | 20.7 | 14.95 | 10.0 | 13.79 | 20.0 | Au1rxx-base64 | 173.244.56.9 |
| 90.83 | trojan | 468.4 | 2.7 | 16.93 | 14.9 | 9.98 | 13.54 | 20.0 | Au1rxx-base64 | 69.164.240.85 |
| 90.81 | vless | 324.2 | 2.8 | 20.27 | 14.89 | 7.73 | 12.08 | 20.0 | Au1rxx-base64 | 45.63.53.81 |
| 90.63 | trojan | 334.0 | 0.3 | 20.05 | 14.99 | 9.27 | 13.54 | 20.0 | Au1rxx-base64 | 167.88.61.193 |
| 90.55 | trojan | 290.9 | 4.4 | 21.04 | 14.83 | 9.28 | 13.54 | 20.0 | Au1rxx-base64 | 167.88.61.20 |
| 90.36 | shadowsocks | 306.4 | 4.4 | 20.68 | 14.83 | 10.0 | 13.79 | 20.0 | Au1rxx-base64 | 173.244.56.6 |
| 90.36 | vless | 392.5 | 3.7 | 18.69 | 14.86 | 9.89 | 12.08 | 20.0 | Au1rxx-base64 | 169.40.42.202 |
| 90.34 | trojan | 305.5 | 4.2 | 20.71 | 14.84 | 9.27 | 13.54 | 20.0 | Au1rxx-base64 | 167.88.61.198 |
| 90.29 | vless | 345.4 | 0.9 | 19.78 | 14.97 | 8.87 | 12.08 | 20.0 | Au1rxx-base64 | 169.40.42.229 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.954 | 0.951 | 61 | 442 | prefer |
| mheidari-all | 0.847 | 0.776 | 58 | 14996 | prefer |
| Surfboard-tg-mixed | 0.796 | 0.718 | 241 | 8136 | prefer |
| Au1rxx-base64 | 0.793 | 0.725 | 153 | 1751 | prefer |
| roosterkid-openproxylist-v2ray | 0.363 | 1.0 | 3 | 116 | observe |
| ermaozi-get_subscribe | 0.326 | 1.0 | 2 | 376 | observe |
| xiaoji235-airport-v2ray-all | 0.287 | 0.5 | 2 | 6752 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4839 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 11514 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5440 | observe |
| barry-far-vless | 0.255 | None | 0 | 5649 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4463 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.245 | None | 0 | 1751 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 53 |
| 204 | ProxyError | - | 29 |
| cn-block | TimeoutError | - | 12 |
| cn-block | ProxyError | - | 8 |
| geo | ProxyError | - | 6 |
| speed | ProxyError | - | 5 |
| cn-block | ClientOSError | - | 5 |
| 204 | TimeoutError | - | 4 |
| geo | TimeoutError | - | 2 |
| geo | ClientOSError | - | 1 |
| speed | TimeoutError | - | 1 |
| speed | ClientOSError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 86 | 80 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
