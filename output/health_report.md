# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-11-26 21:48:36 |
| 运行耗时 | 329.6s |
| 订阅源总数 | 107 |
| 健康订阅源 | 86 |
| 原始节点 | 78821 |
| 去重后节点 | 27291 |
| TCP 可达 | 3000 |
| 真实可用 | 350 |
| Verified 输出 | 63 |
| Global 输出 | 300 |
| All 输出 | 27291 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.7 |
| geo | 1.5 |
| tcp | 79.7 |
| probe | 105.2 |
| real_test | 77.7 |
| china_check | 44.1 |
| write_verified | 0.0 |
| generate | 14.5 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 46240 |
| vmess | 15228 |
| shadowsocks | 9671 |
| trojan | 5653 |
| hysteria2 | 1612 |
| shadowsocksr | 146 |
| http | 108 |
| socks | 96 |
| anytls | 33 |
| hysteria | 22 |
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
| 93.12 | shadowsocks | 226.4 | 1.3 | 22.54 | 14.95 | 10.0 | 13.01 | 16.62 | Au1rxx-base64 | 173.244.56.6 |
| 92.59 | shadowsocks | 229.0 | 0.5 | 22.48 | 14.98 | 10.0 | 13.01 | 16.62 | Au1rxx-base64 | 95.215.201.18 |
| 92.4 | vless | 198.4 | 1.3 | 23.18 | 14.95 | 7.88 | 9.77 | 16.62 | Au1rxx-base64 | 45.63.53.81 |
| 91.78 | shadowsocks | 240.8 | 6.4 | 22.2 | 14.76 | 10.0 | 13.01 | 16.62 | Au1rxx-base64 | 173.244.56.9 |
| 89.95 | hysteria2 | 223.7 | 1.5 | 22.6 | 14.94 | 4.79 | 12.0 | 16.62 | Au1rxx-base64 | 66.94.121.46 |
| 89.54 | http | 196.1 | 0.6 | 23.24 | 14.98 | 0.0 | 14.32 | 19.5 | ermaozi | usgp1-cdn-route.couldflare-cdn.com |
| 89.11 | shadowsocks | 291.9 | 0.3 | 21.02 | 14.99 | 10.0 | 13.01 | 16.62 | Au1rxx-base64 | 156.146.38.170 |
| 88.67 | http | 233.0 | 0.9 | 22.38 | 14.97 | 0.0 | 14.32 | 19.5 | ermaozi | 172.64.69.89 |
| 87.97 | trojan | 173.1 | 0.9 | 23.77 | 14.97 | 10.0 | 5.11 | 16.62 | Au1rxx-base64 | 167.88.61.175 |
| 87.96 | http | 195.1 | 3.3 | 23.26 | 14.88 | 0.0 | 14.32 | 19.5 | ermaozi | 138.199.35.220 |
| 86.36 | trojan | 179.5 | 11.6 | 23.62 | 14.56 | 8.95 | 5.11 | 16.62 | Au1rxx-base64 | 167.88.61.20 |
| 86.21 | trojan | 204.7 | 0.2 | 23.04 | 14.99 | 8.95 | 5.11 | 16.62 | Au1rxx-base64 | 167.88.61.193 |
| 85.67 | shadowsocks | 409.9 | 0.2 | 18.29 | 14.99 | 10.0 | 13.01 | 16.62 | Au1rxx-base64 | 156.146.38.168 |
| 85.26 | trojan | 240.5 | 3.8 | 22.21 | 14.86 | 8.96 | 5.11 | 16.62 | Au1rxx-base64 | 167.88.61.198 |
| 84.97 | shadowsocks | 365.2 | 0.3 | 19.32 | 14.99 | 10.0 | 13.01 | 16.62 | Au1rxx-base64 | 37.19.198.244 |
| 84.67 | shadowsocks | 272.5 | 2.4 | 21.47 | 14.91 | 9.77 | 13.01 | 16.62 | Au1rxx-base64 | 149.22.87.241 |
| 84.58 | vless | 196.5 | 0.5 | 23.23 | 14.98 | 0.0 | 9.77 | 16.6 | mheidari-all | 172.233.129.179 |
| 84.52 | vless | 197.7 | 1.3 | 23.2 | 14.95 | 0.0 | 9.77 | 16.6 | mheidari-all | 172.235.50.209 |
| 84.4 | shadowsocks | 362.3 | 1.7 | 19.39 | 14.94 | 10.0 | 13.01 | 16.62 | Au1rxx-base64 | 37.19.198.236 |
| 84.38 | vless | 201.5 | 2.7 | 23.11 | 14.9 | 0.0 | 9.77 | 16.6 | mheidari-all | 172.235.40.143 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.974 | 1.0 | 22 | 393 | prefer |
| Surfboard-tg-mixed | 0.924 | 0.848 | 145 | 8568 | prefer |
| Au1rxx-base64 | 0.822 | 0.756 | 127 | 1751 | prefer |
| mheidari-all | 0.749 | 0.671 | 164 | 14669 | prefer |
| tg-LonUp_M | 0.365 | 1.0 | 3 | 168 | observe |
| xiaoji235-airport-v2ray-all | 0.287 | 0.5 | 2 | 6752 | observe |
| tg-proxy_mtm | 0.258 | 1.0 | 1 | 67 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4936 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 11794 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5426 | observe |
| barry-far-vless | 0.255 | None | 0 | 5607 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4485 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.245 | None | 0 | 1751 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 75 |
| speed | TimeoutError | - | 11 |
| cn-block | ClientOSError | - | 9 |
| cn-block | TimeoutError | - | 4 |
| 204 | TimeoutError | - | 4 |
| cn-block | ProxyError | - | 3 |
| 204 | ProxyError | - | 2 |
| 204 | ClientOSError | - | 1 |
| speed | ClientOSError | - | 1 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 54 | 63 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
