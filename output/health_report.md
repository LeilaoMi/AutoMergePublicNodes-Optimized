# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-11-06 07:04:17 |
| 运行耗时 | 292.8s |
| 订阅源总数 | 107 |
| 健康订阅源 | 88 |
| 原始节点 | 82780 |
| 去重后节点 | 26710 |
| TCP 可达 | 3000 |
| 真实可用 | 440 |
| Verified 输出 | 123 |
| Global 输出 | 300 |
| All 输出 | 26710 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.0 |
| geo | 1.5 |
| tcp | 79.3 |
| probe | 91.0 |
| real_test | 68.9 |
| china_check | 30.5 |
| write_verified | 0.1 |
| generate | 14.7 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 49932 |
| vmess | 14348 |
| shadowsocks | 9005 |
| trojan | 7254 |
| hysteria2 | 1596 |
| http | 352 |
| shadowsocksr | 145 |
| socks | 79 |
| hysteria | 35 |
| anytls | 18 |
| tuic | 16 |

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
| 91.56 | shadowsocks | 250.9 | 0.1 | 21.97 | 14.99 | 10.0 | 13.48 | 15.12 | Au1rxx-base64 | 156.146.38.168 |
| 91.55 | shadowsocks | 243.3 | 5.4 | 22.15 | 14.8 | 10.0 | 13.48 | 15.12 | Au1rxx-base64 | 156.146.38.167 |
| 89.08 | shadowsocks | 307.1 | 3.6 | 20.67 | 14.87 | 10.0 | 13.48 | 15.12 | Au1rxx-base64 | 37.19.198.244 |
| 88.44 | shadowsocks | 290.7 | 0.6 | 21.05 | 14.98 | 10.0 | 13.48 | 15.12 | Au1rxx-base64 | 37.19.198.160 |
| 87.61 | shadowsocks | 305.3 | 1.8 | 20.71 | 14.93 | 10.0 | 13.48 | 15.12 | Au1rxx-base64 | 45.86.51.18 |
| 87.29 | shadowsocks | 326.8 | 7.5 | 20.21 | 14.72 | 10.0 | 13.48 | 15.12 | Au1rxx-base64 | 37.19.198.243 |
| 86.55 | shadowsocks | 315.0 | 4.0 | 20.49 | 14.85 | 10.0 | 13.48 | 15.12 | Au1rxx-base64 | 185.230.230.18 |
| 86.53 | hysteria2 | 215.7 | 6.7 | 22.78 | 14.75 | 0.0 | 12.19 | 18.84 | mheidari-all | 88.216.195.188 |
| 86.49 | shadowsocks | 287.7 | 2.5 | 21.12 | 14.91 | 10.0 | 13.48 | 15.12 | Au1rxx-base64 | 95.215.201.18 |
| 85.81 | shadowsocks | 315.6 | 4.2 | 20.47 | 14.84 | 10.0 | 13.48 | 15.12 | Au1rxx-base64 | 193.151.163.18 |
| 85.78 | shadowsocks | 320.4 | 0.4 | 20.36 | 14.99 | 10.0 | 13.48 | 15.12 | Au1rxx-base64 | 173.244.56.9 |
| 85.65 | vless | 367.7 | 3.2 | 19.27 | 14.88 | 10.0 | 9.18 | 15.12 | Au1rxx-base64 | 169.40.42.90 |
| 85.44 | shadowsocks | 361.9 | 7.7 | 19.4 | 14.71 | 10.0 | 13.48 | 15.12 | Au1rxx-base64 | 193.151.160.9 |
| 85.28 | shadowsocks | 300.9 | 10.7 | 20.81 | 14.6 | 10.0 | 13.48 | 15.12 | Au1rxx-base64 | 173.244.56.6 |
| 84.75 | vless | 361.6 | 1.7 | 19.41 | 14.94 | 9.99 | 9.18 | 15.12 | Au1rxx-base64 | 167.17.69.171 |
| 84.57 | http | 298.6 | 8.3 | 20.86 | 14.69 | 0.0 | 14.32 | 19.86 | ermaozi | 121.127.34.82 |
| 84.49 | shadowsocks | 263.9 | 0.1 | 21.67 | 15.0 | 0.0 | 13.48 | 18.84 | mheidari-all | 167.88.62.203 |
| 84.28 | shadowsocks | 363.5 | 3.3 | 19.36 | 14.88 | 9.24 | 13.48 | 15.12 | Au1rxx-base64 | 193.151.160.18 |
| 84.17 | hysteria2 | 273.9 | 48.7 | 21.44 | 13.17 | 5.11 | 12.19 | 15.12 | Au1rxx-base64 | 66.94.121.46 |
| 84.03 | http | 376.8 | 3.0 | 19.06 | 14.89 | 0.0 | 14.32 | 19.86 | ermaozi | 198.44.135.27 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.987 | 0.971 | 102 | 639 | prefer |
| mheidari-all | 0.869 | 0.792 | 197 | 14233 | prefer |
| Au1rxx-base64 | 0.858 | 0.79 | 229 | 1751 | prefer |
| Surfboard-tg-mixed | 0.4 | 0.75 | 4 | 8762 | observe |
| xiaoji235-airport-v2ray-all | 0.391 | 1.0 | 2 | 6752 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5039 | observe |
| DeltaKronecker-all | 0.255 | None | 0 | 2653 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 10891 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 6268 | observe |
| barry-far-vless | 0.255 | None | 0 | 6478 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4703 | observe |
| Au1rxx-clash | 0.245 | None | 0 | 1751 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |
| 10ium-HighSpeed | 0.209 | None | 0 | 839 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 45 |
| 204 | ProxyError | - | 16 |
| 204 | TimeoutError | - | 10 |
| cn-block | TimeoutError | - | 7 |
| cn-block | ProxyError | - | 5 |
| geo | ClientOSError | - | 4 |
| cn-block | ClientOSError | - | 3 |
| speed | TimeoutError | - | 2 |
| geo | TimeoutError | - | 1 |
| 204 | ClientOSError | - | 1 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 34 | 123 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
