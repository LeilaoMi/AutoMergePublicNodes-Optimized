# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-16 03:16:21 |
| 运行耗时 | 187.8s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 76031 |
| 去重后节点 | 23073 |
| TCP 可达 | 3000 |
| 真实可用 | 438 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23073 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 3.6 |
| geo | 1.4 |
| tcp | 32.6 |
| probe | 44.6 |
| real_test | 83.9 |
| generate | 21.6 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 43447 |
| trojan | 11499 |
| vmess | 10975 |
| shadowsocks | 9542 |
| hysteria2 | 290 |
| shadowsocksr | 125 |
| http | 98 |
| socks | 41 |
| hysteria | 10 |
| tuic | 4 |

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
| 73.64 | hysteria2 | 191.0 | 496.0 | 23.36 | 0.0 | 10.0 | 12.5 | 9.88 | Au1rxx-base64 | 38.148.249.252 |
| 70.44 | shadowsocks | 212.2 | 491.0 | 22.87 | 0.0 | 10.0 | 11.69 | 9.88 | Au1rxx-base64 | 173.244.56.9 |
| 70.41 | shadowsocks | 213.4 | 503.3 | 22.84 | 0.0 | 10.0 | 11.69 | 9.88 | Au1rxx-base64 | 173.244.56.6 |
| 69.36 | shadowsocks | 237.0 | 600.7 | 22.29 | 0.0 | 10.0 | 11.69 | 9.88 | Au1rxx-base64 | 108.181.118.10 |
| 69.29 | shadowsocks | 240.2 | 606.9 | 22.22 | 0.0 | 10.0 | 11.69 | 9.88 | Au1rxx-base64 | 108.181.0.177 |
| 69.09 | shadowsocks | 227.0 | 591.0 | 22.52 | 0.0 | 10.0 | 11.69 | 9.88 | Au1rxx-base64 | 216.105.168.18 |
| 68.95 | shadowsocks | 262.6 | 642.5 | 21.7 | 0.0 | 10.0 | 11.69 | 9.88 | Au1rxx-base64 | 156.146.38.170 |
| 68.14 | shadowsocks | 302.5 | 759.2 | 20.77 | 0.0 | 10.0 | 11.69 | 9.88 | Au1rxx-base64 | 156.146.38.169 |
| 67.98 | shadowsocks | 263.0 | 634.7 | 21.69 | 0.0 | 10.0 | 11.69 | 9.88 | Au1rxx-base64 | 156.146.38.168 |
| 65.82 | shadowsocks | 282.4 | 281.4 | 21.24 | 4.45 | 9.91 | 11.69 | 9.88 | Au1rxx-base64 | 149.22.87.240 |
| 64.45 | shadowsocks | 255.0 | 613.1 | 21.88 | 0.0 | 10.0 | 11.69 | 9.88 | Au1rxx-base64 | 156.146.38.167 |
| 63.92 | vmess | 237.4 | 648.9 | 22.28 | 0.0 | 10.0 | 12.5 | 3.64 | Barabama-yudou | 82.198.246.233 |
| 63.62 | trojan | 514.5 | 1327.6 | 15.87 | 0.0 | 10.0 | 11.4 | 12.26 | DeltaKronecker-all | 64.94.95.114 |
| 63.09 | trojan | 564.4 | 1478.5 | 14.71 | 0.0 | 10.0 | 11.4 | 12.26 | DeltaKronecker-all | 64.94.95.117 |
| 62.8 | shadowsocks | 370.1 | 768.5 | 19.21 | 0.0 | 10.0 | 11.69 | 12.26 | DeltaKronecker-all | 68.168.222.210 |
| 62.7 | shadowsocks | 338.7 | 682.9 | 19.94 | 0.0 | 10.0 | 11.69 | 9.88 | Au1rxx-base64 | 198.98.53.130 |
| 62.63 | shadowsocks | 304.8 | 356.5 | 20.72 | 1.63 | 9.91 | 11.69 | 9.88 | Au1rxx-base64 | 149.22.87.241 |
| 62.52 | vmess | 538.6 | 1288.4 | 15.31 | 0.0 | 10.0 | 12.5 | 14.78 | Surfboard-tg-mixed | 67.220.85.46 |
| 62.38 | trojan | 406.2 | 427.4 | 18.37 | 0.0 | 10.0 | 11.4 | 12.26 | DeltaKronecker-all | 104.16.100.66 |
| 62.26 | trojan | 345.2 | 344.4 | 19.79 | 2.08 | 9.88 | 11.4 | 12.28 | mheidari-all | 52.195.207.214 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| Au1rxx-base64 | 0.961 | 0.966 | 88 | 148 | prefer |
| mheidari-all | 0.895 | 0.819 | 144 | 16541 | prefer |
| DeltaKronecker-all | 0.8 | 0.723 | 159 | 6421 | prefer |
| Surfboard-tg-mixed | 0.755 | 0.678 | 118 | 5384 | prefer |
| xiaoji235-airport-v2ray-all | 0.325 | 1.0 | 1 | 1757 | observe |
| Barabama-yudou | 0.318 | 1.0 | 2 | 166 | observe |
| 10ium-HighSpeed | 0.289 | 1.0 | 1 | 839 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 3759 | observe |
| Epodonios-all | 0.255 | None | 0 | 6430 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3973 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6934 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4135 | observe |
| barry-far-vless | 0.255 | None | 0 | 4781 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5183 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 44 |
| geo | TimeoutError | - | 32 |
| geo | ClientOSError | - | 16 |
| speed | TimeoutError | - | 6 |
| cn-block | ClientOSError | - | 6 |
| cn-block | ProxyError | - | 3 |
| 204 | ClientOSError | - | 3 |
| 204 | ProxyError | - | 3 |
| cn-block | TimeoutError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 202 | 300 | - |
| global | False | 212 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
