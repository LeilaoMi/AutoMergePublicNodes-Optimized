# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-11-02 21:52:58 |
| 运行耗时 | 303.4s |
| 订阅源总数 | 107 |
| 健康订阅源 | 88 |
| 原始节点 | 81771 |
| 去重后节点 | 26678 |
| TCP 可达 | 3000 |
| 真实可用 | 413 |
| Verified 输出 | 55 |
| Global 输出 | 300 |
| All 输出 | 26678 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.2 |
| geo | 1.5 |
| tcp | 81.2 |
| probe | 93.8 |
| real_test | 76.6 |
| china_check | 31.2 |
| write_verified | 0.0 |
| generate | 12.8 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 48949 |
| vmess | 14011 |
| shadowsocks | 8701 |
| trojan | 8113 |
| hysteria2 | 1533 |
| http | 165 |
| shadowsocksr | 154 |
| socks | 71 |
| anytls | 34 |
| hysteria | 26 |
| tuic | 14 |

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
| 95.9 | trojan | 230.0 | 3.4 | 22.45 | 14.87 | 9.98 | 13.7 | 17.4 | Au1rxx-base64 | 167.88.61.175 |
| 94.8 | shadowsocks | 226.4 | 2.8 | 22.54 | 14.89 | 10.0 | 13.97 | 17.4 | Au1rxx-base64 | 173.244.56.9 |
| 94.69 | shadowsocks | 205.9 | 5.0 | 23.01 | 14.81 | 10.0 | 13.97 | 17.4 | Au1rxx-base64 | 95.215.201.18 |
| 94.06 | trojan | 201.6 | 3.0 | 23.11 | 14.89 | 7.46 | 13.7 | 17.4 | Au1rxx-base64 | 66.163.112.242 |
| 93.58 | trojan | 330.5 | 4.1 | 20.13 | 14.85 | 10.0 | 13.7 | 17.4 | Au1rxx-base64 | 66.163.112.121 |
| 92.92 | trojan | 228.9 | 3.3 | 22.48 | 14.88 | 7.32 | 13.7 | 17.4 | Au1rxx-base64 | 167.88.61.20 |
| 92.81 | shadowsocks | 233.3 | 8.1 | 22.38 | 14.69 | 10.0 | 13.97 | 17.4 | Au1rxx-base64 | 173.244.56.6 |
| 92.81 | trojan | 264.5 | 0.7 | 21.65 | 14.97 | 10.0 | 13.7 | 17.4 | Au1rxx-base64 | 66.163.114.45 |
| 92.71 | trojan | 221.2 | 1.5 | 22.66 | 14.94 | 7.32 | 13.7 | 17.4 | Au1rxx-base64 | 167.88.61.198 |
| 92.66 | trojan | 198.8 | 2.9 | 23.18 | 14.89 | 5.99 | 13.7 | 17.4 | Au1rxx-base64 | 66.163.112.76 |
| 92.64 | shadowsocks | 283.9 | 1.7 | 21.21 | 14.94 | 10.0 | 13.97 | 17.4 | Au1rxx-base64 | 156.146.38.167 |
| 92.29 | trojan | 218.5 | 6.0 | 22.72 | 14.78 | 7.32 | 13.7 | 17.4 | Au1rxx-base64 | 167.88.61.193 |
| 91.84 | shadowsocks | 275.7 | 5.7 | 21.4 | 14.78 | 10.0 | 13.97 | 17.4 | Au1rxx-base64 | 156.146.38.170 |
| 91.59 | shadowsocks | 265.0 | 18.0 | 21.64 | 14.33 | 10.0 | 13.97 | 17.4 | Au1rxx-base64 | 156.146.38.168 |
| 90.4 | hysteria2 | 316.9 | 0.8 | 20.44 | 14.97 | 9.89 | 11.67 | 17.4 | Au1rxx-base64 | 129.213.91.185 |
| 89.18 | trojan | 206.5 | 0.9 | 23.0 | 14.97 | 2.61 | 13.7 | 17.4 | Au1rxx-base64 | 66.163.112.142 |
| 89.15 | shadowsocks | 315.0 | 1.2 | 20.49 | 14.96 | 10.0 | 13.97 | 17.4 | Au1rxx-base64 | 149.22.95.183 |
| 88.83 | trojan | 210.9 | 7.6 | 22.9 | 14.72 | 2.61 | 13.7 | 17.4 | Au1rxx-base64 | 66.163.112.31 |
| 88.82 | trojan | 334.6 | 5.5 | 20.03 | 14.8 | 10.0 | 13.7 | 17.4 | Au1rxx-base64 | 216.238.80.100 |
| 88.63 | vless | 246.6 | 9.0 | 22.07 | 14.66 | 7.78 | 6.72 | 17.4 | Au1rxx-base64 | 144.202.126.147 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Surfboard-tg-mixed | 0.911 | 0.84 | 75 | 8355 | prefer |
| Au1rxx-base64 | 0.91 | 0.842 | 291 | 1751 | prefer |
| zhangkai | 0.857 | 1.0 | 17 | 43 | prefer |
| ermaozi-get_subscribe | 0.771 | 1.0 | 14 | 403 | prefer |
| mheidari-all | 0.532 | 0.451 | 164 | 14971 | observe |
| xiaoji235-airport-v2ray-all | 0.335 | 1.0 | 1 | 6752 | observe |
| ninja-vless | 0.327 | 1.0 | 1 | 1791 | observe |
| tg-oneclickvpnkeys | 0.261 | 1.0 | 1 | 139 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4941 | observe |
| DeltaKronecker-all | 0.255 | None | 0 | 2726 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 10678 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5917 | observe |
| barry-far-vless | 0.255 | None | 0 | 6131 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4726 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 60 |
| geo | ClientOSError | - | 52 |
| 204 | TimeoutError | - | 9 |
| 204 | ProxyError | - | 7 |
| speed | ClientOSError | - | 5 |
| cn-block | TimeoutError | - | 5 |
| cn-block | ProxyError | - | 3 |
| 204 | ClientOSError | - | 3 |
| cn-block | ClientOSError | - | 2 |
| geo | ProxyError | - | 1 |
| speed | TimeoutError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 41 | 55 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
