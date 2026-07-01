# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-01 10:04:01 |
| 运行耗时 | 248.4s |
| 订阅源总数 | 107 |
| 健康订阅源 | 103 |
| 原始节点 | 75612 |
| 去重后节点 | 23077 |
| TCP 可达 | 3000 |
| 真实可用 | 326 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23077 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.4 |
| geo | 1.4 |
| tcp | 30.9 |
| probe | 55.2 |
| real_test | 113.0 |
| generate | 43.4 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 42712 |
| trojan | 12691 |
| vmess | 10272 |
| shadowsocks | 9330 |
| hysteria2 | 254 |
| shadowsocksr | 153 |
| http | 135 |
| socks | 58 |
| hysteria | 6 |
| tuic | 1 |

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
| 78.28 | shadowsocks | 253.9 | 619.1 | 21.9 | 0.0 | 10.0 | 13.76 | 16.62 | Au1rxx-base64 | 156.146.38.169 |
| 78.19 | shadowsocks | 257.6 | 629.5 | 21.81 | 0.0 | 10.0 | 13.76 | 16.62 | Au1rxx-base64 | 156.146.38.170 |
| 78.17 | shadowsocks | 258.7 | 640.9 | 21.79 | 0.0 | 10.0 | 13.76 | 16.62 | Au1rxx-base64 | 156.146.38.167 |
| 78.1 | shadowsocks | 261.7 | 658.4 | 21.72 | 0.0 | 10.0 | 13.76 | 16.62 | Au1rxx-base64 | 37.19.198.160 |
| 77.11 | shadowsocks | 304.7 | 775.7 | 20.73 | 0.0 | 10.0 | 13.76 | 16.62 | Au1rxx-base64 | 37.19.198.236 |
| 76.86 | shadowsocks | 315.4 | 818.3 | 20.48 | 0.0 | 10.0 | 13.76 | 16.62 | Au1rxx-base64 | 37.19.198.244 |
| 75.89 | shadowsocks | 270.8 | 651.3 | 21.51 | 0.0 | 10.0 | 13.76 | 16.62 | Au1rxx-base64 | 37.19.198.243 |
| 75.69 | shadowsocks | 366.0 | 958.6 | 19.31 | 0.0 | 10.0 | 13.76 | 16.62 | Au1rxx-base64 | 156.146.38.168 |
| 74.51 | shadowsocks | 369.3 | 914.5 | 19.23 | 0.0 | 10.0 | 13.76 | 16.62 | Au1rxx-base64 | 108.181.57.93 |
| 72.34 | shadowsocks | 287.0 | 583.7 | 21.13 | 0.0 | 10.0 | 13.76 | 16.62 | Au1rxx-base64 | 173.244.56.9 |
| 71.56 | shadowsocks | 296.8 | 615.5 | 20.91 | 0.0 | 10.0 | 13.76 | 16.62 | Au1rxx-base64 | 149.22.95.183 |
| 71.56 | shadowsocks | 322.9 | 676.0 | 20.3 | 0.0 | 10.0 | 13.76 | 16.62 | Au1rxx-base64 | 173.244.56.6 |
| 71.16 | shadowsocks | 323.8 | 946.3 | 20.28 | 0.0 | 10.0 | 13.76 | 16.62 | Au1rxx-base64 | 172.234.202.34 |
| 68.97 | trojan | 261.4 | 619.1 | 21.73 | 0.0 | 10.0 | 12.0 | 8.24 | DeltaKronecker-all | 64.94.95.115 |
| 68.58 | vless | 366.0 | 889.9 | 19.31 | 0.0 | 10.0 | 6.13 | 15.9 | Surfboard-tg-mixed | 137.184.218.169 |
| 68.4 | trojan | 285.7 | 681.7 | 21.16 | 0.0 | 10.0 | 12.0 | 8.24 | DeltaKronecker-all | 64.94.95.117 |
| 67.44 | trojan | 290.8 | 696.3 | 21.05 | 0.0 | 10.0 | 12.0 | 8.24 | DeltaKronecker-all | 64.94.95.114 |
| 66.92 | shadowsocks | 378.9 | 409.8 | 19.01 | 0.0 | 9.53 | 13.76 | 16.62 | Au1rxx-base64 | 149.22.87.240 |
| 66.83 | shadowsocks | 382.0 | 404.5 | 18.93 | 0.0 | 9.5 | 13.76 | 16.62 | Au1rxx-base64 | 149.22.87.241 |
| 66.11 | vless | 337.1 | 592.9 | 19.97 | 0.0 | 10.0 | 6.13 | 15.9 | Surfboard-tg-mixed | 34.213.172.16 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.952 | 0.974 | 38 | 61 | prefer |
| Au1rxx-base64 | 0.714 | 0.717 | 60 | 115 | prefer |
| Surfboard-tg-mixed | 0.674 | 0.594 | 249 | 5595 | observe |
| mheidari-all | 0.539 | 0.458 | 72 | 15660 | observe |
| DeltaKronecker-all | 0.515 | 0.434 | 145 | 7631 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| ermaozi | 0.256 | 1.0 | 1 | 28 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4308 | observe |
| Epodonios-all | 0.255 | None | 0 | 6487 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6549 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4151 | observe |
| barry-far-vless | 0.255 | None | 0 | 4743 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5331 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 110 |
| 204 | TimeoutError | - | 41 |
| geo | TimeoutError | - | 27 |
| 204 | ProxyError | - | 12 |
| 204 | ClientOSError | - | 12 |
| cn-block | TimeoutError | - | 12 |
| geo | ClientOSError | - | 11 |
| speed | TimeoutError | - | 8 |
| cn-block | ClientOSError | - | 7 |
| cn-block | ProxyError | - | 3 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
