# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-14 11:38:32 |
| 运行耗时 | 361.2s |
| 订阅源总数 | 107 |
| 健康订阅源 | 93 |
| 原始节点 | 98043 |
| 去重后节点 | 27216 |
| TCP 可达 | 3000 |
| 真实可用 | 84 |
| Verified 输出 | 84 |
| Global 输出 | 91 |
| All 输出 | 27216 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.8 |
| geo | 1.5 |
| tcp | 118.0 |
| probe | 96.3 |
| real_test | 86.5 |
| generate | 53.1 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 57891 |
| vmess | 16102 |
| shadowsocks | 11799 |
| trojan | 10164 |
| hysteria2 | 1302 |
| http | 483 |
| shadowsocksr | 167 |
| socks | 86 |
| anytls | 25 |
| hysteria | 18 |
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
| 78.28 | hysteria2 | 272.9 | 660.8 | 21.46 | 0.0 | 9.36 | 13.0 | 15.46 | Au1rxx-base64 | 66.94.121.46 |
| 77.59 | vless | 195.7 | 509.1 | 23.25 | 0.0 | 10.0 | 8.88 | 15.46 | Au1rxx-base64 | 45.32.69.110 |
| 77.22 | vless | 211.4 | 536.4 | 22.88 | 0.0 | 10.0 | 8.88 | 15.46 | Au1rxx-base64 | 154.29.145.196 |
| 76.78 | vless | 230.6 | 550.1 | 22.44 | 0.0 | 10.0 | 8.88 | 15.46 | Au1rxx-base64 | 154.12.38.159 |
| 74.09 | shadowsocks | 261.0 | 628.4 | 21.74 | 0.0 | 10.0 | 13.2 | 15.46 | Au1rxx-base64 | 156.146.38.167 |
| 74.05 | shadowsocks | 220.6 | 554.1 | 22.67 | 0.0 | 10.0 | 13.2 | 15.46 | Au1rxx-base64 | 173.244.56.6 |
| 73.22 | http | 196.0 | 510.4 | 23.24 | 0.0 | 0.0 | 14.06 | 18.92 | ermaozi-get_subscribe | 138.199.35.213 |
| 73.14 | http | 199.4 | 515.6 | 23.16 | 0.0 | 0.0 | 14.06 | 18.92 | ermaozi-get_subscribe | 138.199.35.195 |
| 71.48 | http | 197.7 | 517.8 | 23.2 | 0.0 | 0.0 | 14.06 | 17.22 | zhangkai | 138.199.35.198 |
| 71.36 | shadowsocks | 262.4 | 643.4 | 21.7 | 0.0 | 10.0 | 13.2 | 15.46 | Au1rxx-base64 | 156.146.38.168 |
| 71.21 | http | 196.3 | 511.5 | 23.23 | 0.0 | 0.0 | 14.06 | 18.92 | ermaozi-get_subscribe | 138.199.35.218 |
| 70.99 | shadowsocks | 258.2 | 631.3 | 21.8 | 0.0 | 6.53 | 13.2 | 15.46 | Au1rxx-base64 | 156.146.38.169 |
| 70.65 | hysteria2 | 318.3 | 741.6 | 20.41 | 0.0 | 10.0 | 13.0 | 15.46 | Au1rxx-base64 | 129.213.91.185 |
| 70.16 | http | 198.8 | 520.5 | 23.18 | 0.0 | 0.0 | 14.06 | 18.92 | ermaozi-get_subscribe | 138.199.35.197 |
| 69.37 | shadowsocks | 365.9 | 807.5 | 19.31 | 0.0 | 10.0 | 13.2 | 15.46 | Au1rxx-base64 | 37.19.198.160 |
| 69.26 | shadowsocks | 360.5 | 788.0 | 19.43 | 0.0 | 10.0 | 13.2 | 15.46 | Au1rxx-base64 | 37.19.198.244 |
| 68.92 | shadowsocks | 259.8 | 636.4 | 21.76 | 0.0 | 0.0 | 13.2 | 17.96 | mheidari-all | 156.146.38.170 |
| 68.29 | vless | 256.1 | 629.2 | 21.85 | 0.0 | 0.0 | 8.88 | 17.96 | mheidari-all | 47.251.108.158 |
| 68.23 | http | 195.5 | 509.7 | 23.25 | 0.0 | 0.0 | 14.06 | 18.92 | ermaozi-get_subscribe | 138.199.35.212 |
| 68.19 | http | 197.3 | 516.6 | 23.21 | 0.0 | 0.0 | 14.06 | 18.92 | ermaozi-get_subscribe | 138.199.35.205 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.927 | 1.0 | 19 | 144 | prefer |
| ermaozi-get_subscribe | 0.925 | 0.913 | 69 | 598 | prefer |
| Surfboard-tg-mixed | 0.83 | 0.769 | 26 | 7056 | prefer |
| Au1rxx-base64 | 0.822 | 0.754 | 203 | 1778 | prefer |
| mheidari-all | 0.704 | 0.626 | 99 | 23983 | prefer |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5125 | observe |
| DeltaKronecker-all | 0.255 | None | 0 | 4803 | observe |
| Epodonios-all | 0.255 | None | 0 | 7542 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9834 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5579 | observe |
| barry-far-vless | 0.255 | None | 0 | 5831 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4216 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 52 |
| speed | ClientOSError | - | 11 |
| 204 | ProxyError | - | 8 |
| cn-block | TimeoutError | - | 6 |
| geo | ClientOSError | - | 4 |
| 204 | TimeoutError | - | 4 |
| cn-block | ProxyError | - | 3 |
| 204 | ClientOSError | - | 3 |
| geo | TimeoutError | - | 3 |
| cn-block | ClientOSError | - | 3 |
| speed | ProxyError | - | 1 |
| geo | ProxyError | - | 1 |
| speed | TimeoutError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 68 | 84 | - |
| global | False | 74 | 91 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
