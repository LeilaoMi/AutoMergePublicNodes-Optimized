# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-16 06:25:17 |
| 运行耗时 | 359.4s |
| 订阅源总数 | 107 |
| 健康订阅源 | 93 |
| 原始节点 | 99736 |
| 去重后节点 | 27922 |
| TCP 可达 | 3000 |
| 真实可用 | 495 |
| Verified 输出 | 18 |
| Global 输出 | 300 |
| All 输出 | 27922 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 8.3 |
| geo | 1.5 |
| tcp | 87.2 |
| probe | 108.2 |
| real_test | 107.4 |
| china_check | 32.4 |
| write_verified | 0.0 |
| generate | 14.4 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 58905 |
| vmess | 16436 |
| shadowsocks | 11794 |
| trojan | 10381 |
| hysteria2 | 1205 |
| http | 740 |
| shadowsocksr | 168 |
| socks | 59 |
| anytls | 25 |
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
| 92.39 | shadowsocks | 216.1 | 2.2 | 22.78 | 14.92 | 9.21 | 13.82 | 17.66 | Au1rxx-base64 | 149.22.95.183 |
| 91.98 | hysteria2 | 216.8 | 4.1 | 22.76 | 14.85 | 8.52 | 12.19 | 17.66 | Au1rxx-base64 | 179.255.104.98 |
| 88.25 | vless | 247.2 | 0.6 | 22.06 | 14.98 | 8.78 | 8.23 | 17.66 | Au1rxx-base64 | 216.234.140.15 |
| 87.2 | shadowsocks | 313.2 | 1.3 | 20.53 | 14.95 | 8.76 | 13.82 | 17.66 | Au1rxx-base64 | 156.146.38.167 |
| 87.12 | shadowsocks | 318.9 | 0.8 | 20.4 | 14.97 | 8.74 | 13.82 | 17.66 | Au1rxx-base64 | 156.146.38.170 |
| 87.01 | shadowsocks | 325.6 | 1.7 | 20.24 | 14.94 | 8.76 | 13.82 | 17.66 | Au1rxx-base64 | 156.146.38.168 |
| 85.22 | http | 277.5 | 3.8 | 21.35 | 14.86 | 0.0 | 14.51 | 20.0 | ermaozi | 149.22.88.65 |
| 85.03 | http | 267.4 | 0.9 | 21.59 | 14.97 | 0.0 | 14.51 | 20.0 | ermaozi | 138.199.35.202 |
| 84.8 | shadowsocks | 377.8 | 0.3 | 19.03 | 14.99 | 8.61 | 13.82 | 17.66 | Au1rxx-base64 | 37.19.198.243 |
| 84.66 | shadowsocks | 402.7 | 0.4 | 18.46 | 14.98 | 8.76 | 13.82 | 17.66 | Au1rxx-base64 | 156.146.38.169 |
| 84.49 | http | 275.7 | 4.8 | 21.4 | 14.82 | 0.0 | 14.51 | 20.0 | ermaozi | 138.199.35.206 |
| 83.94 | shadowsocks | 274.5 | 0.8 | 21.42 | 14.97 | 4.02 | 13.82 | 17.66 | Au1rxx-base64 | 173.244.56.9 |
| 83.77 | http | 266.9 | 0.5 | 21.6 | 14.98 | 0.0 | 14.51 | 20.0 | ermaozi | 138.199.35.199 |
| 83.54 | vless | 233.9 | 3.5 | 22.36 | 14.87 | 6.1 | 8.23 | 17.66 | Au1rxx-base64 | 44.248.233.99 |
| 83.33 | http | 344.4 | 2.1 | 19.8 | 14.92 | 0.0 | 14.51 | 20.0 | ermaozi | 138.199.35.216 |
| 83.31 | shadowsocks | 393.9 | 0.1 | 18.66 | 15.0 | 8.61 | 13.82 | 17.66 | Au1rxx-base64 | 37.19.198.160 |
| 83.27 | http | 346.8 | 2.3 | 19.75 | 14.92 | 0.0 | 14.51 | 20.0 | ermaozi | 138.199.35.210 |
| 83.13 | http | 317.7 | 7.6 | 20.42 | 14.72 | 0.0 | 14.51 | 20.0 | ermaozi | 64.98.50.100 |
| 82.75 | vless | 300.6 | 6.8 | 20.82 | 14.74 | 6.3 | 8.23 | 17.66 | Au1rxx-base64 | 51.81.203.63 |
| 82.61 | shadowsocks | 351.3 | 6.4 | 19.65 | 14.76 | 8.19 | 13.82 | 17.66 | Au1rxx-base64 | 84.247.155.196 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.984 | 0.966 | 89 | 693 | prefer |
| Au1rxx-base64 | 0.878 | 0.8 | 465 | 1992 | prefer |
| mheidari-all | 0.642 | 0.567 | 30 | 23985 | observe |
| Surfboard-tg-mixed | 0.488 | 0.404 | 47 | 7054 | observe |
| tg-oneclickvpnkeys | 0.258 | 1.0 | 1 | 79 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5024 | observe |
| Au1rxx-clash | 0.255 | None | 0 | 1992 | observe |
| Epodonios-all | 0.255 | None | 0 | 7651 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 10060 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5573 | observe |
| barry-far-vless | 0.255 | None | 0 | 5882 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4265 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 81 |
| speed | ClientOSError | - | 16 |
| geo | ClientOSError | - | 13 |
| speed | TimeoutError | - | 8 |
| cn-block | ClientOSError | - | 7 |
| 204 | ProxyError | - | 6 |
| 204 | TimeoutError | - | 4 |
| 204 | ClientOSError | - | 3 |
| cn-block | ProxyError | - | 3 |
| cn-block | TimeoutError | - | 2 |
| speed | ProxyError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 21 | 18 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
