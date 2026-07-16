# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-16 14:09:43 |
| 运行耗时 | 227.3s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 79344 |
| 去重后节点 | 24515 |
| TCP 可达 | 3000 |
| 真实可用 | 500 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 24515 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.3 |
| geo | 1.1 |
| tcp | 33.1 |
| probe | 48.1 |
| real_test | 110.8 |
| generate | 29.8 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 46222 |
| trojan | 12126 |
| vmess | 10780 |
| shadowsocks | 9634 |
| hysteria2 | 304 |
| shadowsocksr | 128 |
| http | 97 |
| socks | 39 |
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
| 80.29 | shadowsocks | 231.2 | 642.0 | 22.43 | 0.0 | 10.0 | 12.34 | 19.52 | Au1rxx-base64 | 37.19.198.160 |
| 80.24 | shadowsocks | 233.2 | 638.2 | 22.38 | 0.0 | 10.0 | 12.34 | 19.52 | Au1rxx-base64 | 37.19.198.236 |
| 77.28 | shadowsocks | 284.6 | 659.3 | 21.19 | 0.0 | 10.0 | 12.34 | 19.52 | Au1rxx-base64 | 156.146.38.169 |
| 77.23 | shadowsocks | 363.1 | 1028.9 | 19.37 | 0.0 | 10.0 | 12.34 | 19.52 | Au1rxx-base64 | 37.19.198.243 |
| 77.16 | shadowsocks | 220.9 | 589.3 | 22.66 | 0.0 | 10.0 | 12.34 | 16.28 | mheidari-all | 198.98.53.130 |
| 77.13 | shadowsocks | 288.8 | 651.1 | 21.09 | 0.0 | 10.0 | 12.34 | 19.52 | Au1rxx-base64 | 156.146.38.168 |
| 76.9 | shadowsocks | 289.5 | 664.6 | 21.08 | 0.0 | 10.0 | 12.34 | 19.52 | Au1rxx-base64 | 156.146.38.170 |
| 76.26 | shadowsocks | 243.4 | 647.1 | 22.14 | 0.0 | 10.0 | 12.34 | 16.28 | mheidari-all | 108.181.57.93 |
| 74.83 | shadowsocks | 358.7 | 946.3 | 19.47 | 0.0 | 10.0 | 12.34 | 19.52 | Au1rxx-base64 | 50.114.177.235 |
| 74.21 | shadowsocks | 284.4 | 646.9 | 21.2 | 0.0 | 10.0 | 12.34 | 19.52 | Au1rxx-base64 | 156.146.38.167 |
| 73.19 | vless | 238.0 | 665.7 | 22.27 | 0.0 | 10.0 | 1.4 | 19.52 | Au1rxx-base64 | 47.253.226.114 |
| 73.01 | shadowsocks | 383.9 | 786.9 | 18.89 | 0.0 | 10.0 | 12.34 | 16.28 | mheidari-all | 68.168.222.210 |
| 72.86 | shadowsocks | 316.3 | 580.2 | 20.46 | 0.0 | 10.0 | 12.34 | 19.52 | Au1rxx-base64 | 173.244.56.6 |
| 72.86 | hysteria2 | 362.3 | 684.7 | 19.39 | 0.0 | 10.0 | 11.25 | 19.52 | Au1rxx-base64 | 62.210.124.146 |
| 72.7 | shadowsocks | 322.1 | 587.8 | 20.32 | 0.0 | 10.0 | 12.34 | 19.52 | Au1rxx-base64 | 173.244.56.9 |
| 71.4 | shadowsocks | 342.7 | 576.5 | 19.84 | 0.0 | 10.0 | 12.34 | 19.52 | Au1rxx-base64 | 108.181.118.10 |
| 71.18 | shadowsocks | 343.2 | 580.9 | 19.83 | 0.0 | 10.0 | 12.34 | 19.52 | Au1rxx-base64 | 108.181.0.177 |
| 69.75 | shadowsocks | 240.3 | 650.0 | 22.21 | 0.0 | 10.0 | 12.34 | 16.28 | mheidari-all | 147.90.234.133 |
| 69.5 | shadowsocks | 362.7 | 1012.8 | 19.38 | 0.0 | 10.0 | 12.34 | 19.52 | Au1rxx-base64 | tinkered-pennies-puppies.freesocks.work |
| 69.19 | shadowsocks | 349.7 | 866.8 | 19.68 | 0.0 | 10.0 | 12.34 | 12.98 | DeltaKronecker-all | 185.196.61.82 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| mheidari-all | 0.924 | 0.85 | 120 | 16416 | prefer |
| Au1rxx-base64 | 0.906 | 0.906 | 128 | 150 | prefer |
| Surfboard-tg-mixed | 0.899 | 0.826 | 92 | 5430 | prefer |
| DeltaKronecker-all | 0.802 | 0.724 | 232 | 8462 | prefer |
| xiaoji235-airport-v2ray-all | 0.325 | 1.0 | 1 | 1757 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4470 | observe |
| Epodonios-all | 0.255 | None | 0 | 6545 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7282 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4211 | observe |
| barry-far-vless | 0.255 | None | 0 | 4817 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5262 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| nscl5-all | 0.236 | None | 0 | 1519 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 33 |
| speed | ClientOSError | - | 30 |
| 204 | ClientOSError | - | 10 |
| 204 | ProxyError | - | 9 |
| 204 | TimeoutError | - | 8 |
| geo | ClientOSError | - | 6 |
| cn-block | ClientOSError | - | 6 |
| cn-block | ProxyError | - | 4 |
| cn-block | TimeoutError | - | 4 |
| speed | TimeoutError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
