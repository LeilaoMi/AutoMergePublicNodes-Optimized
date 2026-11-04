# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-11-04 19:58:50 |
| 运行耗时 | 318.2s |
| 订阅源总数 | 107 |
| 健康订阅源 | 87 |
| 原始节点 | 82735 |
| 去重后节点 | 26928 |
| TCP 可达 | 3000 |
| 真实可用 | 365 |
| Verified 输出 | 40 |
| Global 输出 | 300 |
| All 输出 | 26928 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 35.3 |
| geo | 1.5 |
| tcp | 82.3 |
| probe | 86.3 |
| real_test | 74.4 |
| china_check | 26.2 |
| write_verified | 0.0 |
| generate | 12.3 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 49805 |
| vmess | 13895 |
| shadowsocks | 9082 |
| trojan | 8011 |
| hysteria2 | 1585 |
| shadowsocksr | 151 |
| http | 76 |
| socks | 62 |
| hysteria | 32 |
| anytls | 21 |
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
| 92.52 | shadowsocks | 239.0 | 3.6 | 22.24 | 14.86 | 10.0 | 13.56 | 15.86 | Au1rxx-base64 | 156.146.38.168 |
| 92.36 | shadowsocks | 233.0 | 4.1 | 22.39 | 14.85 | 10.0 | 13.56 | 15.86 | Au1rxx-base64 | 156.146.38.170 |
| 92.29 | shadowsocks | 252.5 | 1.7 | 21.93 | 14.94 | 10.0 | 13.56 | 15.86 | Au1rxx-base64 | 156.146.38.167 |
| 89.93 | shadowsocks | 337.6 | 1.5 | 19.96 | 14.95 | 10.0 | 13.56 | 15.86 | Au1rxx-base64 | 37.19.198.244 |
| 88.01 | shadowsocks | 315.3 | 1.5 | 20.48 | 14.94 | 10.0 | 13.56 | 15.86 | Au1rxx-base64 | 45.86.51.18 |
| 87.5 | hysteria2 | 279.4 | 4.4 | 21.31 | 14.84 | 10.0 | 10.71 | 15.86 | Au1rxx-base64 | 129.213.91.185 |
| 87.47 | shadowsocks | 324.9 | 1.6 | 20.26 | 14.94 | 10.0 | 13.56 | 15.86 | Au1rxx-base64 | 185.230.230.18 |
| 86.35 | shadowsocks | 317.0 | 0.3 | 20.44 | 14.99 | 10.0 | 13.56 | 15.86 | Au1rxx-base64 | 193.151.163.18 |
| 85.87 | shadowsocks | 337.5 | 2.0 | 19.97 | 14.93 | 10.0 | 13.56 | 15.86 | Au1rxx-base64 | 193.151.160.9 |
| 85.74 | shadowsocks | 296.4 | 2.0 | 20.92 | 14.92 | 10.0 | 13.56 | 15.86 | Au1rxx-base64 | 95.215.201.18 |
| 85.35 | shadowsocks | 330.8 | 3.7 | 20.12 | 14.86 | 10.0 | 13.56 | 15.86 | Au1rxx-base64 | 149.22.95.183 |
| 85.23 | shadowsocks | 340.5 | 1.1 | 19.9 | 14.96 | 10.0 | 13.56 | 15.86 | Au1rxx-base64 | 173.244.56.9 |
| 85.05 | hysteria2 | 237.6 | 21.9 | 22.28 | 14.18 | 0.0 | 10.71 | 18.88 | mheidari-all | 88.216.195.188 |
| 85.01 | vless | 306.9 | 7.0 | 20.67 | 14.74 | 7.1 | 9.85 | 15.86 | Au1rxx-base64 | 195.123.235.183 |
| 84.84 | vless | 431.4 | 1.6 | 17.79 | 14.94 | 9.61 | 9.85 | 15.86 | Au1rxx-base64 | 159.89.87.21 |
| 84.52 | shadowsocks | 332.9 | 15.1 | 20.07 | 14.43 | 8.71 | 13.56 | 15.86 | Au1rxx-base64 | 193.151.160.18 |
| 84.0 | shadowsocks | 326.1 | 0.7 | 20.23 | 14.97 | 10.0 | 13.56 | 15.86 | Au1rxx-base64 | 37.19.198.160 |
| 83.98 | trojan | 382.1 | 19.1 | 18.93 | 14.28 | 10.0 | 9.59 | 15.86 | Au1rxx-base64 | 66.23.203.21 |
| 83.98 | vless | 438.4 | 1.2 | 17.63 | 14.96 | 9.57 | 9.85 | 15.86 | Au1rxx-base64 | 167.17.69.171 |
| 83.74 | shadowsocks | 354.5 | 3.7 | 19.57 | 14.86 | 10.0 | 13.56 | 15.86 | Au1rxx-base64 | 173.244.56.6 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| mheidari-all | 0.88 | 0.804 | 163 | 15192 | prefer |
| Surfboard-tg-mixed | 0.805 | 0.731 | 67 | 8707 | prefer |
| zhangkai | 0.796 | 0.889 | 18 | 43 | prefer |
| Au1rxx-base64 | 0.759 | 0.69 | 239 | 1751 | prefer |
| xiaoji235-airport-v2ray-all | 0.349 | 0.667 | 3 | 6752 | observe |
| ninja-vless | 0.327 | 1.0 | 1 | 1791 | observe |
| ermaozi | 0.315 | 1.0 | 2 | 83 | observe |
| tg-LonUp_M | 0.262 | 1.0 | 1 | 174 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5005 | observe |
| DeltaKronecker-all | 0.255 | None | 0 | 2526 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 10836 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 6137 | observe |
| barry-far-vless | 0.255 | None | 0 | 6348 | observe |
| Au1rxx-clash | 0.245 | None | 0 | 1751 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 66 |
| 204 | ProxyError | - | 21 |
| 204 | TimeoutError | - | 10 |
| 204 | ClientOSError | - | 9 |
| cn-block | ProxyError | - | 6 |
| cn-block | ClientOSError | - | 5 |
| speed | ClientOSError | - | 3 |
| geo | ProxyError | - | 2 |
| speed | ProxyError | - | 2 |
| cn-block | TimeoutError | - | 2 |
| geo | ClientOSError | - | 1 |
| geo | TimeoutError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 33 | 40 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
