# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-11-08 06:23:23 |
| 运行耗时 | 281.7s |
| 订阅源总数 | 107 |
| 健康订阅源 | 87 |
| 原始节点 | 81513 |
| 去重后节点 | 27137 |
| TCP 可达 | 3000 |
| 真实可用 | 519 |
| Verified 输出 | 59 |
| Global 输出 | 300 |
| All 输出 | 27137 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 3.8 |
| geo | 1.4 |
| tcp | 81.0 |
| probe | 67.8 |
| real_test | 88.7 |
| china_check | 29.8 |
| write_verified | 0.0 |
| generate | 9.2 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 48495 |
| vmess | 14185 |
| shadowsocks | 9186 |
| trojan | 7521 |
| hysteria2 | 1595 |
| http | 254 |
| shadowsocksr | 148 |
| socks | 67 |
| hysteria | 27 |
| anytls | 19 |
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
| 94.0 | shadowsocks | 239.1 | 1.3 | 22.24 | 14.95 | 10.0 | 13.93 | 16.88 | Au1rxx-base64 | 156.146.38.167 |
| 93.96 | shadowsocks | 242.4 | 0.6 | 22.17 | 14.98 | 10.0 | 13.93 | 16.88 | Au1rxx-base64 | 156.146.38.168 |
| 92.08 | shadowsocks | 301.7 | 1.0 | 20.79 | 14.96 | 10.0 | 13.93 | 16.88 | Au1rxx-base64 | 37.19.198.160 |
| 91.86 | shadowsocks | 291.3 | 0.2 | 21.04 | 14.99 | 10.0 | 13.93 | 16.88 | Au1rxx-base64 | 37.19.198.243 |
| 91.83 | shadowsocks | 313.4 | 0.1 | 20.52 | 15.0 | 10.0 | 13.93 | 16.88 | Au1rxx-base64 | 185.230.230.18 |
| 91.58 | shadowsocks | 291.3 | 1.2 | 21.04 | 14.95 | 10.0 | 13.93 | 16.88 | Au1rxx-base64 | 37.19.198.236 |
| 90.68 | trojan | 357.9 | 0.3 | 19.49 | 14.99 | 10.0 | 12.32 | 16.88 | Au1rxx-base64 | 66.23.203.21 |
| 90.62 | trojan | 318.5 | 1.5 | 20.4 | 14.95 | 10.0 | 12.32 | 16.88 | Au1rxx-base64 | 66.163.114.45 |
| 89.33 | trojan | 236.2 | 0.1 | 22.31 | 15.0 | 7.32 | 12.32 | 16.88 | Au1rxx-base64 | 216.152.155.59 |
| 88.63 | shadowsocks | 295.0 | 1.2 | 20.95 | 14.95 | 10.0 | 13.93 | 16.88 | Au1rxx-base64 | 95.215.201.18 |
| 88.12 | shadowsocks | 302.1 | 1.6 | 20.78 | 14.94 | 10.0 | 13.93 | 16.88 | Au1rxx-base64 | 193.151.163.18 |
| 86.54 | trojan | 332.4 | 0.1 | 20.08 | 15.0 | 10.0 | 12.32 | 16.88 | Au1rxx-base64 | 66.163.112.121 |
| 86.25 | trojan | 372.2 | 0.9 | 19.16 | 14.97 | 10.0 | 12.32 | 16.88 | Au1rxx-base64 | 216.238.80.100 |
| 86.12 | vless | 283.3 | 0.2 | 21.22 | 14.99 | 6.98 | 9.55 | 16.88 | Au1rxx-base64 | 108.61.119.63 |
| 86.11 | trojan | 404.5 | 2.8 | 18.42 | 14.9 | 7.37 | 12.32 | 16.88 | Au1rxx-base64 | 66.163.114.245 |
| 85.98 | trojan | 258.8 | 0.3 | 21.79 | 14.99 | 7.39 | 12.32 | 16.88 | Au1rxx-base64 | 66.163.114.106 |
| 85.98 | trojan | 335.0 | 2.0 | 20.02 | 14.93 | 7.36 | 12.32 | 16.88 | Au1rxx-base64 | 170.101.101.67 |
| 85.85 | hysteria2 | 321.5 | 0.7 | 20.34 | 14.97 | 3.4 | 12.19 | 16.88 | Au1rxx-base64 | 66.94.121.46 |
| 85.76 | http | 329.3 | 0.4 | 20.15 | 14.98 | 0.0 | 14.29 | 18.84 | ermaozi | 23.133.176.14 |
| 85.67 | trojan | 267.9 | 1.0 | 21.58 | 14.96 | 4.43 | 12.32 | 16.88 | Au1rxx-base64 | 216.152.155.23 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 1.0 | 0.989 | 95 | 613 | prefer |
| Surfboard-tg-mixed | 0.936 | 0.862 | 109 | 8112 | prefer |
| Au1rxx-base64 | 0.903 | 0.835 | 237 | 1751 | prefer |
| mheidari-all | 0.784 | 0.706 | 187 | 14505 | prefer |
| DeltaKronecker-all | 0.335 | 1.0 | 1 | 2734 | observe |
| xiaoji235-airport-v2ray-all | 0.335 | 1.0 | 1 | 6752 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4866 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3996 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 10963 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5849 | observe |
| barry-far-vless | 0.255 | None | 0 | 6061 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4529 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.245 | None | 0 | 1751 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 70 |
| 204 | ProxyError | - | 15 |
| 204 | TimeoutError | - | 10 |
| geo | ClientOSError | - | 6 |
| cn-block | TimeoutError | - | 4 |
| 204 | ClientOSError | - | 2 |
| cn-block | ProxyError | - | 1 |
| geo | TimeoutError | - | 1 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 41 | 59 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
