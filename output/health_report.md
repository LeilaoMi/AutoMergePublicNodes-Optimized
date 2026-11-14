# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-11-14 22:38:56 |
| 运行耗时 | 297.0s |
| 订阅源总数 | 107 |
| 健康订阅源 | 86 |
| 原始节点 | 82855 |
| 去重后节点 | 27069 |
| TCP 可达 | 3000 |
| 真实可用 | 450 |
| Verified 输出 | 89 |
| Global 输出 | 300 |
| All 输出 | 27069 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.8 |
| geo | 1.6 |
| tcp | 83.3 |
| probe | 88.5 |
| real_test | 74.8 |
| china_check | 31.1 |
| generate | 11.9 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 49739 |
| vmess | 14652 |
| shadowsocks | 9616 |
| trojan | 6844 |
| hysteria2 | 1521 |
| http | 183 |
| shadowsocksr | 150 |
| socks | 77 |
| anytls | 33 |
| hysteria | 22 |
| tuic | 18 |

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
| 90.49 | shadowsocks | 254.7 | 2.1 | 21.88 | 14.92 | 10.0 | 13.81 | 15.22 | Au1rxx-base64 | 156.146.38.170 |
| 88.48 | shadowsocks | 271.4 | 0.5 | 21.5 | 14.98 | 10.0 | 13.81 | 15.22 | Au1rxx-base64 | 95.215.201.18 |
| 87.76 | vless | 249.8 | 0.8 | 22.0 | 14.97 | 6.36 | 10.89 | 15.22 | Au1rxx-base64 | 45.63.53.81 |
| 86.46 | vless | 248.0 | 1.3 | 22.04 | 14.95 | 6.52 | 10.89 | 15.22 | Au1rxx-base64 | 47.251.108.158 |
| 85.79 | shadowsocks | 354.5 | 4.7 | 19.57 | 14.82 | 10.0 | 13.81 | 15.22 | Au1rxx-base64 | 185.230.230.18 |
| 85.53 | shadowsocks | 327.7 | 2.6 | 20.19 | 14.9 | 10.0 | 13.81 | 15.22 | Au1rxx-base64 | 193.151.163.18 |
| 85.32 | shadowsocks | 297.1 | 0.7 | 20.9 | 14.97 | 10.0 | 13.81 | 15.22 | Au1rxx-base64 | 156.146.38.168 |
| 85.15 | shadowsocks | 223.8 | 3.7 | 22.6 | 14.86 | 0.0 | 13.81 | 17.98 | Surfboard-tg-mixed | 38.145.220.193 |
| 84.72 | shadowsocks | 267.2 | 2.4 | 21.59 | 14.91 | 10.0 | 13.81 | 15.22 | Au1rxx-base64 | 156.146.38.167 |
| 84.39 | shadowsocks | 375.5 | 6.2 | 19.09 | 14.77 | 10.0 | 13.81 | 15.22 | Au1rxx-base64 | 193.151.160.9 |
| 84.22 | shadowsocks | 214.3 | 0.4 | 22.82 | 14.99 | 0.0 | 13.81 | 17.1 | mheidari-all | 137.184.89.151 |
| 84.12 | shadowsocks | 321.0 | 2.3 | 20.35 | 14.91 | 10.0 | 13.81 | 15.22 | Au1rxx-base64 | 45.86.51.18 |
| 84.05 | http | 369.2 | 0.2 | 19.23 | 14.99 | 0.0 | 13.39 | 18.94 | ermaozi | 172.64.69.89 |
| 83.72 | shadowsocks | 359.0 | 9.3 | 19.47 | 14.65 | 9.98 | 13.81 | 15.22 | Au1rxx-base64 | 15.204.247.206 |
| 83.34 | vless | 382.1 | 3.1 | 18.93 | 14.88 | 8.84 | 10.89 | 15.22 | Au1rxx-base64 | 159.89.87.21 |
| 83.14 | vless | 411.9 | 9.4 | 18.24 | 14.65 | 8.89 | 10.89 | 15.22 | Au1rxx-base64 | 66.70.179.198 |
| 83.07 | shadowsocks | 376.0 | 1.0 | 19.07 | 14.96 | 8.59 | 13.81 | 15.22 | Au1rxx-base64 | 193.151.160.18 |
| 83.03 | shadowsocks | 259.6 | 0.8 | 21.77 | 14.97 | 4.65 | 13.81 | 15.22 | Au1rxx-base64 | 156.146.38.169 |
| 82.99 | shadowsocks | 303.9 | 1.0 | 20.74 | 14.96 | 0.0 | 13.81 | 17.98 | Surfboard-tg-mixed | 167.88.62.203 |
| 82.78 | vless | 373.6 | 2.2 | 19.13 | 14.92 | 8.89 | 10.89 | 15.22 | Au1rxx-base64 | 167.17.69.171 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.984 | 1.0 | 25 | 527 | prefer |
| mheidari-all | 0.942 | 0.871 | 85 | 13757 | prefer |
| Surfboard-tg-mixed | 0.928 | 0.851 | 208 | 9013 | prefer |
| Au1rxx-base64 | 0.878 | 0.81 | 211 | 1751 | prefer |
| xiaoji235-airport-v2ray-all | 0.391 | 1.0 | 2 | 6752 | observe |
| DeltaKronecker-all | 0.335 | 1.0 | 1 | 2652 | observe |
| ermaozi-get_subscribe | 0.271 | 1.0 | 1 | 405 | observe |
| tg-LonUp_M | 0.262 | 1.0 | 1 | 168 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4966 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 11640 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 6319 | observe |
| barry-far-vless | 0.255 | None | 0 | 6499 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4551 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 48 |
| 204 | ProxyError | - | 11 |
| 204 | TimeoutError | - | 7 |
| 204 | ClientOSError | - | 6 |
| cn-block | ClientOSError | - | 2 |
| cn-block | TimeoutError | - | 2 |
| cn-block | ProxyError | - | 2 |
| speed | TimeoutError | - | 2 |
| geo | ProxyError | - | 1 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | True | 89 | 43 | 0.5 |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
