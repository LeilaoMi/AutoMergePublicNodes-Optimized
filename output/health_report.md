# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-12 03:33:12 |
| 运行耗时 | 253.3s |
| 订阅源总数 | 107 |
| 健康订阅源 | 103 |
| 原始节点 | 76600 |
| 去重后节点 | 24228 |
| TCP 可达 | 3000 |
| 真实可用 | 508 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 24228 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.8 |
| geo | 1.3 |
| tcp | 31.9 |
| probe | 53.1 |
| real_test | 118.6 |
| generate | 43.7 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 44038 |
| trojan | 11894 |
| vmess | 10592 |
| shadowsocks | 9482 |
| hysteria2 | 265 |
| shadowsocksr | 146 |
| http | 135 |
| socks | 35 |
| hysteria | 8 |
| tuic | 5 |

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
| 78.25 | shadowsocks | 228.9 | 631.2 | 22.48 | 0.0 | 10.0 | 11.97 | 17.8 | Au1rxx-base64 | 37.19.198.244 |
| 78.23 | shadowsocks | 229.7 | 632.4 | 22.46 | 0.0 | 10.0 | 11.97 | 17.8 | Au1rxx-base64 | 37.19.198.243 |
| 76.86 | shadowsocks | 288.8 | 813.9 | 21.09 | 0.0 | 10.0 | 11.97 | 17.8 | Au1rxx-base64 | 37.19.198.236 |
| 76.21 | shadowsocks | 230.5 | 633.2 | 22.44 | 0.0 | 10.0 | 11.97 | 17.8 | Au1rxx-base64 | 37.19.198.160 |
| 74.98 | shadowsocks | 276.7 | 630.3 | 21.37 | 0.0 | 10.0 | 11.97 | 17.8 | Au1rxx-base64 | 156.146.38.168 |
| 74.31 | shadowsocks | 247.0 | 652.6 | 22.06 | 0.0 | 10.0 | 11.97 | 14.78 | mheidari-all | 108.181.57.93 |
| 73.88 | shadowsocks | 278.1 | 642.5 | 21.34 | 0.0 | 10.0 | 11.97 | 17.8 | Au1rxx-base64 | 156.146.38.167 |
| 73.75 | shadowsocks | 298.7 | 661.8 | 20.86 | 0.0 | 10.0 | 11.97 | 17.8 | Au1rxx-base64 | 156.146.38.169 |
| 73.51 | shadowsocks | 220.5 | 593.2 | 22.67 | 0.0 | 10.0 | 11.97 | 17.8 | Au1rxx-base64 | 198.98.53.130 |
| 71.78 | vless | 312.6 | 862.6 | 20.54 | 0.0 | 10.0 | 5.44 | 17.8 | Au1rxx-base64 | 159.89.87.21 |
| 71.13 | shadowsocks | 349.5 | 846.9 | 19.69 | 0.0 | 10.0 | 11.97 | 14.78 | mheidari-all | 185.196.61.82 |
| 70.57 | shadowsocks | 242.6 | 657.5 | 22.16 | 0.0 | 10.0 | 11.97 | 17.8 | Au1rxx-base64 | 147.90.234.133 |
| 70.43 | shadowsocks | 302.2 | 572.4 | 20.78 | 0.0 | 10.0 | 11.97 | 17.8 | Au1rxx-base64 | 108.181.118.10 |
| 70.34 | shadowsocks | 329.8 | 601.3 | 20.14 | 0.0 | 10.0 | 11.97 | 17.8 | Au1rxx-base64 | 173.244.56.6 |
| 70.25 | shadowsocks | 233.4 | 629.3 | 22.37 | 0.0 | 10.0 | 11.97 | 17.8 | Au1rxx-base64 | tinkered-pennies-puppies.freesocks.work |
| 70.13 | hysteria2 | 377.5 | 660.8 | 19.04 | 0.0 | 9.93 | 10.0 | 17.8 | Au1rxx-base64 | 62.210.124.146 |
| 69.86 | shadowsocks | 336.0 | 613.3 | 20.0 | 0.0 | 10.0 | 11.97 | 17.8 | Au1rxx-base64 | 108.181.0.177 |
| 69.77 | shadowsocks | 355.0 | 631.8 | 19.56 | 0.0 | 10.0 | 11.97 | 17.8 | Au1rxx-base64 | 149.22.95.183 |
| 69.37 | shadowsocks | 287.2 | 649.4 | 21.13 | 0.0 | 10.0 | 11.97 | 17.8 | Au1rxx-base64 | 156.146.38.170 |
| 69.17 | vless | 244.2 | 661.4 | 22.13 | 0.0 | 10.0 | 5.44 | 11.6 | Surfboard-tg-mixed | 137.184.218.169 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| Au1rxx-base64 | 0.786 | 0.787 | 80 | 140 | prefer |
| Surfboard-tg-mixed | 0.724 | 0.645 | 332 | 5277 | prefer |
| mheidari-all | 0.577 | 0.497 | 292 | 16401 | observe |
| DeltaKronecker-all | 0.457 | 0.375 | 120 | 7969 | observe |
| nscl5-all | 0.378 | 0.75 | 4 | 1439 | observe |
| 10ium-ScrapeCategorize-Vless | 0.335 | 1.0 | 1 | 3953 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| Epodonios-all | 0.255 | None | 0 | 6385 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3977 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6662 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4046 | observe |
| barry-far-vless | 0.255 | None | 0 | 4725 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5416 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 155 |
| geo | TimeoutError | - | 82 |
| speed | TimeoutError | - | 37 |
| geo | ClientOSError | - | 29 |
| cn-block | ClientOSError | - | 14 |
| 204 | ProxyError | - | 12 |
| 204 | ClientOSError | - | 11 |
| cn-block | TimeoutError | - | 9 |
| 204 | TimeoutError | - | 5 |
| geo | ProxyError | - | 3 |
| cn-block | ProxyError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 280 | 300 | - |
| global | False | 296 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
