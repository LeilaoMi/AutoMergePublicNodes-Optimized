# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-11-03 19:42:54 |
| 运行耗时 | 296.7s |
| 订阅源总数 | 107 |
| 健康订阅源 | 87 |
| 原始节点 | 83456 |
| 去重后节点 | 26791 |
| TCP 可达 | 3000 |
| 真实可用 | 362 |
| Verified 输出 | 37 |
| Global 输出 | 300 |
| All 输出 | 26791 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.2 |
| geo | 1.5 |
| tcp | 78.9 |
| probe | 99.3 |
| real_test | 74.9 |
| china_check | 20.5 |
| write_verified | 0.0 |
| generate | 14.4 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 49740 |
| vmess | 14163 |
| shadowsocks | 8846 |
| trojan | 8658 |
| hysteria2 | 1663 |
| shadowsocksr | 152 |
| http | 91 |
| socks | 78 |
| hysteria | 30 |
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
| 95.97 | hysteria2 | 227.4 | 0.1 | 22.51 | 15.0 | 9.43 | 12.35 | 18.18 | Au1rxx-base64 | 129.213.91.185 |
| 93.85 | shadowsocks | 247.4 | 4.3 | 22.05 | 14.84 | 9.5 | 13.28 | 18.18 | Au1rxx-base64 | 37.19.198.244 |
| 93.33 | shadowsocks | 242.7 | 5.6 | 22.16 | 14.79 | 9.42 | 13.28 | 18.18 | Au1rxx-base64 | 45.86.51.18 |
| 93.22 | shadowsocks | 250.9 | 2.9 | 21.97 | 14.89 | 9.4 | 13.28 | 18.18 | Au1rxx-base64 | 193.151.163.18 |
| 93.2 | shadowsocks | 265.0 | 8.4 | 21.64 | 14.69 | 9.41 | 13.28 | 18.18 | Au1rxx-base64 | 37.19.198.243 |
| 93.14 | shadowsocks | 248.9 | 9.1 | 22.02 | 14.66 | 9.5 | 13.28 | 18.18 | Au1rxx-base64 | 185.230.230.18 |
| 92.89 | shadowsocks | 291.0 | 0.8 | 21.04 | 14.97 | 9.42 | 13.28 | 18.18 | Au1rxx-base64 | 37.19.198.160 |
| 92.82 | vless | 264.4 | 4.1 | 21.66 | 14.84 | 9.36 | 8.78 | 18.18 | Au1rxx-base64 | 169.40.42.74 |
| 91.67 | vless | 230.2 | 2.3 | 22.45 | 14.91 | 7.35 | 8.78 | 18.18 | Au1rxx-base64 | 195.123.235.183 |
| 91.46 | shadowsocks | 295.2 | 0.4 | 20.94 | 14.98 | 9.22 | 13.28 | 18.18 | Au1rxx-base64 | 193.151.160.9 |
| 91.27 | vless | 323.6 | 3.5 | 20.29 | 14.87 | 9.15 | 8.78 | 18.18 | Au1rxx-base64 | 169.40.42.90 |
| 90.75 | vless | 350.4 | 0.8 | 19.67 | 14.97 | 9.15 | 8.78 | 18.18 | Au1rxx-base64 | 169.40.42.235 |
| 90.5 | vless | 361.8 | 0.3 | 19.4 | 14.99 | 9.15 | 8.78 | 18.18 | Au1rxx-base64 | 169.40.42.202 |
| 89.91 | trojan | 274.3 | 1.7 | 21.43 | 14.94 | 7.79 | 10.93 | 18.18 | Au1rxx-base64 | 170.101.101.67 |
| 89.83 | vless | 315.0 | 11.2 | 20.49 | 14.58 | 9.1 | 8.78 | 18.18 | Au1rxx-base64 | 66.70.179.198 |
| 89.44 | vless | 292.0 | 6.8 | 21.02 | 14.75 | 6.71 | 8.78 | 18.18 | Au1rxx-base64 | 2.24.124.64 |
| 88.61 | trojan | 280.7 | 3.8 | 21.28 | 14.86 | 5.86 | 10.93 | 18.18 | Au1rxx-base64 | 170.101.101.211 |
| 88.41 | vless | 389.9 | 12.8 | 18.75 | 14.52 | 9.15 | 8.78 | 18.18 | Au1rxx-base64 | 169.40.42.89 |
| 88.32 | vless | 281.6 | 30.3 | 21.26 | 13.86 | 9.15 | 8.78 | 18.18 | Au1rxx-base64 | 159.89.87.21 |
| 88.2 | shadowsocks | 361.7 | 10.0 | 19.41 | 14.62 | 8.88 | 13.28 | 18.18 | Au1rxx-base64 | 193.151.160.18 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.978 | 1.0 | 20 | 592 | prefer |
| Au1rxx-base64 | 0.783 | 0.714 | 266 | 1751 | prefer |
| mheidari-all | 0.673 | 0.594 | 244 | 15211 | observe |
| Surfboard-tg-mixed | 0.401 | 0.571 | 7 | 8613 | observe |
| xiaoji235-airport-v2ray-all | 0.391 | 1.0 | 2 | 6752 | observe |
| ninja-vless | 0.327 | 1.0 | 1 | 1791 | observe |
| tg-oneclickvpnkeys | 0.26 | 1.0 | 1 | 122 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5017 | observe |
| DeltaKronecker-all | 0.255 | None | 0 | 2526 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 10863 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 6089 | observe |
| barry-far-vless | 0.255 | None | 0 | 6302 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4753 | observe |
| Au1rxx-clash | 0.245 | None | 0 | 1751 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 86 |
| geo | ClientOSError | - | 40 |
| 204 | TimeoutError | - | 15 |
| 204 | ProxyError | - | 14 |
| cn-block | ProxyError | - | 5 |
| cn-block | ClientOSError | - | 4 |
| cn-block | TimeoutError | - | 4 |
| 204 | ClientOSError | - | 3 |
| speed | ClientOSError | - | 3 |
| speed | ProxyError | - | 2 |
| speed | TimeoutError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 34 | 37 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
