# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-22 05:07:26 |
| 运行耗时 | 306.6s |
| 订阅源总数 | 107 |
| 健康订阅源 | 91 |
| 原始节点 | 96990 |
| 去重后节点 | 27063 |
| TCP 可达 | 3000 |
| 真实可用 | 425 |
| Verified 输出 | 117 |
| Global 输出 | 300 |
| All 输出 | 27063 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.6 |
| geo | 1.5 |
| tcp | 85.0 |
| probe | 72.7 |
| real_test | 97.6 |
| china_check | 33.9 |
| write_verified | 0.0 |
| generate | 10.3 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 57653 |
| vmess | 17035 |
| shadowsocks | 12083 |
| trojan | 8456 |
| hysteria2 | 1303 |
| http | 194 |
| shadowsocksr | 167 |
| socks | 55 |
| anytls | 21 |
| hysteria | 17 |
| tuic | 6 |

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
| 94.97 | vless | 221.1 | 3.6 | 22.66 | 14.87 | 10.0 | 9.98 | 17.46 | Au1rxx-base64 | 44.248.233.99 |
| 93.93 | shadowsocks | 223.1 | 26.7 | 22.61 | 14.0 | 10.0 | 13.86 | 17.46 | Au1rxx-base64 | 149.22.95.183 |
| 91.1 | hysteria2 | 315.9 | 0.0 | 20.47 | 15.0 | 10.0 | 12.69 | 17.46 | Au1rxx-base64 | 129.213.91.185 |
| 90.61 | vless | 283.6 | 0.2 | 21.21 | 14.99 | 10.0 | 9.98 | 17.46 | Au1rxx-base64 | 45.32.69.110 |
| 89.11 | shadowsocks | 297.9 | 1.6 | 20.88 | 14.94 | 10.0 | 13.86 | 17.46 | Au1rxx-base64 | 173.244.56.6 |
| 88.94 | shadowsocks | 308.4 | 1.5 | 20.64 | 14.94 | 10.0 | 13.86 | 17.46 | Au1rxx-base64 | 95.215.201.18 |
| 88.76 | vless | 317.9 | 1.3 | 20.42 | 14.95 | 10.0 | 9.98 | 17.46 | Au1rxx-base64 | 195.123.240.65 |
| 88.66 | shadowsocks | 318.6 | 0.6 | 20.4 | 14.98 | 10.0 | 13.86 | 17.46 | Au1rxx-base64 | 156.146.38.168 |
| 88.53 | shadowsocks | 340.7 | 3.1 | 19.89 | 14.88 | 10.0 | 13.86 | 17.46 | Au1rxx-base64 | 103.11.76.248 |
| 88.23 | vless | 295.6 | 19.1 | 20.94 | 14.28 | 10.0 | 9.98 | 17.46 | Au1rxx-base64 | 154.40.55.185 |
| 87.67 | vless | 463.7 | 3.3 | 17.04 | 14.88 | 8.31 | 9.98 | 17.46 | Au1rxx-base64 | 51.81.203.63 |
| 87.56 | shadowsocks | 237.9 | 1.3 | 22.27 | 14.95 | 10.0 | 13.86 | 17.46 | Au1rxx-base64 | 167.160.90.54 |
| 86.35 | shadowsocks | 282.7 | 0.4 | 21.23 | 14.99 | 9.9 | 13.86 | 17.46 | Au1rxx-base64 | 149.22.87.240 |
| 86.26 | shadowsocks | 287.9 | 3.0 | 21.11 | 14.89 | 9.9 | 13.86 | 17.46 | Au1rxx-base64 | 149.22.87.204 |
| 86.23 | shadowsocks | 367.3 | 2.6 | 19.27 | 14.9 | 10.0 | 13.86 | 17.46 | Au1rxx-base64 | 37.19.198.243 |
| 85.71 | shadowsocks | 374.6 | 0.8 | 19.11 | 14.97 | 9.86 | 13.86 | 17.46 | Au1rxx-base64 | 37.19.198.244 |
| 85.58 | vless | 289.5 | 2.0 | 21.08 | 14.93 | 8.16 | 9.98 | 17.46 | Au1rxx-base64 | 156.229.164.4 |
| 85.24 | shadowsocks | 317.5 | 11.5 | 20.43 | 14.57 | 9.85 | 13.86 | 17.46 | Au1rxx-base64 | 149.22.87.241 |
| 85.22 | shadowsocks | 368.6 | 1.1 | 19.25 | 14.96 | 9.83 | 13.86 | 17.46 | Au1rxx-base64 | 193.151.163.18 |
| 85.16 | trojan | 203.9 | 4.4 | 23.06 | 14.83 | 3.92 | 13.39 | 17.46 | Au1rxx-base64 | 216.106.186.32 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.966 | 1.0 | 26 | 31 | prefer |
| ermaozi-get_subscribe | 0.933 | 0.924 | 66 | 523 | prefer |
| Au1rxx-base64 | 0.868 | 0.806 | 288 | 1615 | prefer |
| mheidari-all | 0.577 | 0.497 | 179 | 24252 | observe |
| Surfboard-tg-mixed | 0.568 | 0.875 | 8 | 7097 | observe |
| DeltaKronecker-all | 0.474 | 0.467 | 15 | 4067 | observe |
| ninja-vless | 0.364 | 0.6 | 5 | 1791 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4925 | observe |
| Epodonios-all | 0.255 | None | 0 | 7591 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 10126 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5559 | observe |
| barry-far-vless | 0.255 | None | 0 | 5773 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4164 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 105 |
| speed | ClientOSError | - | 18 |
| geo | ClientOSError | - | 14 |
| 204 | ProxyError | - | 9 |
| 204 | TimeoutError | - | 7 |
| cn-block | TimeoutError | - | 4 |
| cn-block | ClientOSError | - | 3 |
| cn-block | ProxyError | - | 2 |
| speed | TimeoutError | - | 2 |
| speed | ProxyError | - | 1 |
| 204 | ClientOSError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 74 | 117 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
