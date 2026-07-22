# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-22 19:39:01 |
| 运行耗时 | 263.3s |
| 订阅源总数 | 107 |
| 健康订阅源 | 102 |
| 原始节点 | 81866 |
| 去重后节点 | 22606 |
| TCP 可达 | 3000 |
| 真实可用 | 565 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22606 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.7 |
| geo | 1.2 |
| tcp | 32.3 |
| probe | 59.2 |
| real_test | 139.3 |
| generate | 25.6 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 48092 |
| trojan | 12865 |
| vmess | 10138 |
| shadowsocks | 10125 |
| hysteria2 | 427 |
| shadowsocksr | 79 |
| http | 50 |
| socks | 48 |
| tuic | 24 |
| hysteria | 16 |
| anytls | 2 |

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
| 77.97 | trojan | 280.9 | 703.4 | 21.28 | 0.0 | 10.0 | 13.13 | 16.56 | Au1rxx-base64 | 64.94.95.115 |
| 77.88 | trojan | 284.5 | 711.6 | 21.19 | 0.0 | 10.0 | 13.13 | 16.56 | Au1rxx-base64 | 64.94.95.118 |
| 77.56 | shadowsocks | 246.7 | 634.0 | 22.07 | 0.0 | 10.0 | 12.93 | 16.56 | Au1rxx-base64 | 156.146.38.169 |
| 77.06 | trojan | 320.2 | 801.3 | 20.37 | 0.0 | 10.0 | 13.13 | 16.56 | Au1rxx-base64 | 64.94.95.117 |
| 76.98 | trojan | 323.5 | 821.3 | 20.29 | 0.0 | 10.0 | 13.13 | 16.56 | Au1rxx-base64 | 64.94.95.114 |
| 76.95 | trojan | 267.3 | 648.9 | 21.59 | 0.0 | 10.0 | 13.13 | 17.74 | mheidari-all | 163.245.196.68 |
| 76.05 | shadowsocks | 232.6 | 593.6 | 22.39 | 0.0 | 10.0 | 12.93 | 16.56 | Au1rxx-base64 | 156.146.38.168 |
| 75.45 | shadowsocks | 248.2 | 629.6 | 22.03 | 0.0 | 10.0 | 12.93 | 16.56 | Au1rxx-base64 | 156.146.38.170 |
| 75.44 | shadowsocks | 310.2 | 733.2 | 20.6 | 0.0 | 10.0 | 12.93 | 16.56 | Au1rxx-base64 | 37.19.198.243 |
| 74.01 | shadowsocks | 302.0 | 710.3 | 20.79 | 0.0 | 10.0 | 12.93 | 16.56 | Au1rxx-base64 | 37.19.198.244 |
| 73.99 | vless | 241.9 | 604.3 | 22.18 | 0.0 | 10.0 | 4.53 | 17.74 | mheidari-all | 154.193.55.183 |
| 73.82 | shadowsocks | 279.7 | 659.5 | 21.3 | 0.0 | 10.0 | 12.93 | 16.56 | Au1rxx-base64 | 37.19.198.236 |
| 73.69 | shadowsocks | 241.1 | 637.1 | 22.2 | 0.0 | 10.0 | 12.93 | 16.56 | Au1rxx-base64 | 156.146.38.167 |
| 72.34 | trojan | 312.8 | 563.3 | 20.54 | 0.0 | 10.0 | 13.13 | 16.56 | Au1rxx-base64 | 44.252.127.212 |
| 71.93 | shadowsocks | 279.5 | 550.1 | 21.31 | 0.0 | 10.0 | 12.93 | 16.56 | Au1rxx-base64 | 173.244.56.6 |
| 71.8 | vless | 247.0 | 531.8 | 22.06 | 0.0 | 10.0 | 4.53 | 17.74 | mheidari-all | 86.109.75.147 |
| 71.63 | shadowsocks | 287.4 | 550.4 | 21.12 | 0.0 | 10.0 | 12.93 | 16.56 | Au1rxx-base64 | 108.181.118.10 |
| 71.49 | trojan | 310.0 | 561.2 | 20.6 | 0.0 | 10.0 | 13.13 | 16.56 | Au1rxx-base64 | 52.32.130.95 |
| 71.32 | shadowsocks | 415.6 | 1004.7 | 18.16 | 0.0 | 10.0 | 12.93 | 16.56 | Au1rxx-base64 | 108.181.57.93 |
| 71.27 | trojan | 331.2 | 608.0 | 20.11 | 0.0 | 10.0 | 13.13 | 16.56 | Au1rxx-base64 | 44.249.231.131 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.95 | 0.972 | 36 | 61 | prefer |
| Au1rxx-base64 | 0.805 | 0.79 | 186 | 432 | prefer |
| mheidari-all | 0.709 | 0.629 | 523 | 19265 | prefer |
| DeltaKronecker-all | 0.705 | 0.628 | 78 | 5212 | prefer |
| xiaoji235-airport-v2ray-all | 0.391 | 1.0 | 2 | 4246 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4613 | observe |
| Epodonios-all | 0.255 | None | 0 | 6453 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3970 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6754 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4192 | observe |
| barry-far-vless | 0.255 | None | 0 | 4789 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4954 | observe |
| nscl5-all | 0.255 | None | 0 | 2197 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 83 |
| speed | ClientOSError | - | 68 |
| cn-block | TimeoutError | - | 44 |
| geo | ClientOSError | - | 31 |
| 204 | TimeoutError | - | 11 |
| 204 | ProxyError | - | 9 |
| cn-block | ClientOSError | - | 8 |
| 204 | ClientOSError | - | 8 |
| cn-block | ProxyError | - | 5 |
| speed | TimeoutError | - | 5 |
| speed | ProxyError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
