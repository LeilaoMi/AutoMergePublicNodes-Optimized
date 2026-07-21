# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-21 03:23:54 |
| 运行耗时 | 289.4s |
| 订阅源总数 | 107 |
| 健康订阅源 | 102 |
| 原始节点 | 84510 |
| 去重后节点 | 24299 |
| TCP 可达 | 3000 |
| 真实可用 | 599 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 24299 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.2 |
| geo | 1.4 |
| tcp | 33.8 |
| probe | 63.5 |
| real_test | 164.0 |
| generate | 21.4 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 50780 |
| trojan | 11745 |
| vmess | 11008 |
| shadowsocks | 10368 |
| hysteria2 | 408 |
| shadowsocksr | 78 |
| socks | 53 |
| http | 53 |
| hysteria | 10 |
| tuic | 6 |
| anytls | 1 |

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
| 77.99 | shadowsocks | 223.6 | 501.2 | 22.6 | 0.0 | 9.21 | 12.48 | 17.7 | Au1rxx-base64 | 173.244.56.6 |
| 77.88 | shadowsocks | 228.5 | 499.4 | 22.49 | 0.0 | 9.21 | 12.48 | 17.7 | Au1rxx-base64 | 173.244.56.9 |
| 76.98 | shadowsocks | 240.9 | 587.9 | 22.2 | 0.0 | 9.22 | 12.48 | 17.7 | Au1rxx-base64 | 149.22.95.183 |
| 76.24 | trojan | 197.4 | 557.9 | 23.21 | 0.0 | 9.04 | 10.79 | 17.7 | Au1rxx-base64 | jp1.8b1c7c70-ecf1-6891-9fa7-68a86662f902.cheathub.net |
| 75.83 | trojan | 246.4 | 558.0 | 22.07 | 0.0 | 8.77 | 10.79 | 17.7 | Au1rxx-base64 | primary-mallard.rooster465.autos |
| 75.69 | trojan | 240.2 | 544.9 | 22.22 | 0.0 | 8.78 | 10.79 | 17.7 | Au1rxx-base64 | learning-fawn.rooster465.autos |
| 74.68 | trojan | 256.3 | 589.3 | 21.84 | 0.0 | 9.37 | 10.79 | 17.7 | Au1rxx-base64 | 44.251.239.102 |
| 74.22 | trojan | 230.4 | 479.0 | 22.45 | 0.0 | 8.82 | 10.79 | 17.7 | Au1rxx-base64 | sharing-porpoise.rooster465.autos |
| 74.22 | shadowsocks | 272.2 | 280.7 | 21.48 | 4.47 | 9.21 | 12.48 | 17.7 | Au1rxx-base64 | 149.22.87.240 |
| 73.71 | trojan | 251.6 | 554.0 | 21.95 | 0.0 | 8.77 | 10.79 | 17.7 | Au1rxx-base64 | fast-bunny.rooster465.autos |
| 73.7 | shadowsocks | 199.1 | 487.2 | 23.17 | 0.0 | 9.35 | 12.48 | 17.7 | Au1rxx-base64 | 216.105.168.18 |
| 73.54 | shadowsocks | 289.3 | 652.0 | 21.08 | 0.0 | 9.21 | 12.48 | 17.7 | Au1rxx-base64 | 156.146.38.170 |
| 73.41 | trojan | 267.1 | 608.9 | 21.6 | 0.0 | 8.82 | 10.79 | 17.7 | Au1rxx-base64 | nearby-muskrat.rooster465.autos |
| 73.22 | shadowsocks | 292.5 | 655.8 | 21.01 | 0.0 | 9.19 | 12.48 | 17.7 | Au1rxx-base64 | 156.146.38.167 |
| 72.46 | trojan | 246.2 | 552.8 | 22.08 | 0.0 | 9.39 | 10.79 | 17.7 | Au1rxx-base64 | 44.252.127.212 |
| 72.32 | trojan | 164.4 | 462.9 | 23.97 | 0.0 | 10.0 | 10.79 | 11.06 | mheidari-all | 138.197.195.58 |
| 72.31 | trojan | 251.4 | 542.4 | 21.96 | 0.0 | 9.36 | 10.79 | 17.7 | Au1rxx-base64 | 44.251.184.47 |
| 72.16 | trojan | 259.7 | 566.5 | 21.77 | 0.0 | 9.4 | 10.79 | 17.7 | Au1rxx-base64 | 44.249.231.131 |
| 72.03 | trojan | 326.5 | 784.7 | 20.22 | 0.0 | 8.82 | 10.79 | 17.7 | Au1rxx-base64 | tolerant-rattler.rooster465.autos |
| 71.89 | shadowsocks | 422.5 | 1153.6 | 18.0 | 0.0 | 9.21 | 12.48 | 17.7 | Au1rxx-base64 | 108.181.118.10 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.976 | 1.0 | 36 | 61 | prefer |
| Surfboard-tg-mixed | 0.904 | 0.829 | 123 | 5509 | prefer |
| Au1rxx-base64 | 0.882 | 0.869 | 206 | 405 | prefer |
| DeltaKronecker-all | 0.631 | 0.552 | 174 | 5962 | observe |
| mheidari-all | 0.381 | 0.301 | 615 | 20195 | observe |
| roosterkid-openproxylist-v2ray | 0.261 | 1.0 | 1 | 150 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4714 | observe |
| Epodonios-all | 0.255 | None | 0 | 6601 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3974 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6928 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4238 | observe |
| barry-far-vless | 0.255 | None | 0 | 4952 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5173 | observe |
| nscl5-all | 0.255 | None | 0 | 2111 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 222 |
| geo | TimeoutError | - | 193 |
| speed | TimeoutError | - | 50 |
| cn-block | TimeoutError | - | 40 |
| geo | ClientOSError | - | 38 |
| cn-block | ClientOSError | - | 5 |
| 204 | ProxyError | - | 4 |
| 204 | TimeoutError | - | 3 |
| cn-block | ProxyError | - | 2 |
| 204 | ClientOSError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
