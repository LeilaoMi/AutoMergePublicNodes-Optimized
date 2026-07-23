# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-23 08:43:53 |
| 运行耗时 | 343.3s |
| 订阅源总数 | 107 |
| 健康订阅源 | 102 |
| 原始节点 | 83067 |
| 去重后节点 | 22726 |
| TCP 可达 | 3000 |
| 真实可用 | 837 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22726 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.4 |
| geo | 1.3 |
| tcp | 32.1 |
| probe | 66.6 |
| real_test | 207.4 |
| generate | 31.6 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 47778 |
| trojan | 14017 |
| shadowsocks | 10471 |
| vmess | 10181 |
| hysteria2 | 421 |
| shadowsocksr | 72 |
| http | 50 |
| socks | 43 |
| tuic | 17 |
| hysteria | 14 |
| anytls | 3 |

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
| 77.16 | shadowsocks | 222.5 | 607.1 | 22.63 | 0.0 | 10.0 | 13.47 | 15.06 | Au1rxx-base64 | 198.98.53.130 |
| 77.12 | shadowsocks | 224.2 | 614.2 | 22.59 | 0.0 | 10.0 | 13.47 | 15.06 | Au1rxx-base64 | 37.19.198.236 |
| 76.76 | shadowsocks | 239.5 | 663.9 | 22.23 | 0.0 | 10.0 | 13.47 | 15.06 | Au1rxx-base64 | 37.19.198.243 |
| 76.57 | shadowsocks | 247.8 | 692.2 | 22.04 | 0.0 | 10.0 | 13.47 | 15.06 | Au1rxx-base64 | 37.19.198.244 |
| 76.05 | shadowsocks | 248.6 | 671.3 | 22.02 | 0.0 | 10.0 | 13.47 | 15.06 | Au1rxx-base64 | 68.168.222.210 |
| 72.97 | shadowsocks | 284.8 | 659.5 | 21.19 | 0.0 | 10.0 | 13.47 | 15.06 | Au1rxx-base64 | 156.146.38.170 |
| 72.71 | shadowsocks | 312.7 | 750.6 | 20.54 | 0.0 | 10.0 | 13.47 | 15.06 | Au1rxx-base64 | 156.146.38.168 |
| 72.51 | shadowsocks | 289.5 | 660.6 | 21.08 | 0.0 | 10.0 | 13.47 | 15.06 | Au1rxx-base64 | 156.146.38.167 |
| 71.98 | shadowsocks | 230.4 | 639.3 | 22.45 | 0.0 | 10.0 | 13.47 | 15.06 | Au1rxx-base64 | 37.19.198.160 |
| 71.68 | trojan | 430.1 | 1103.2 | 17.82 | 0.0 | 10.0 | 13.24 | 15.06 | Au1rxx-base64 | 148.72.168.35 |
| 70.78 | shadowsocks | 317.6 | 718.7 | 20.43 | 0.0 | 10.0 | 13.47 | 15.06 | Au1rxx-base64 | 108.181.57.93 |
| 70.1 | shadowsocks | 307.5 | 590.3 | 20.66 | 0.0 | 10.0 | 13.47 | 15.06 | Au1rxx-base64 | 173.244.56.9 |
| 69.47 | hysteria2 | 423.2 | 886.6 | 17.98 | 0.0 | 10.0 | 12.5 | 15.06 | Au1rxx-base64 | 5.255.102.165 |
| 69.12 | shadowsocks | 331.6 | 561.9 | 20.1 | 0.0 | 10.0 | 13.47 | 15.06 | Au1rxx-base64 | 149.22.95.183 |
| 68.92 | trojan | 304.2 | 654.4 | 20.74 | 0.0 | 10.0 | 13.24 | 11.62 | mheidari-all | 163.245.196.68 |
| 68.75 | shadowsocks | 326.1 | 612.5 | 20.23 | 0.0 | 10.0 | 13.47 | 15.06 | Au1rxx-base64 | 108.181.118.10 |
| 68.22 | shadowsocks | 387.0 | 770.6 | 18.82 | 0.0 | 10.0 | 13.47 | 15.06 | Au1rxx-base64 | 108.181.0.177 |
| 67.98 | shadowsocks | 335.5 | 842.5 | 20.01 | 0.0 | 10.0 | 13.47 | 15.06 | Au1rxx-base64 | 185.196.61.82 |
| 67.35 | vmess | 326.2 | 936.2 | 20.23 | 0.0 | 10.0 | 10.0 | 11.62 | mheidari-all | 67.220.95.3 |
| 67.33 | trojan | 404.5 | 671.3 | 18.41 | 0.0 | 10.0 | 13.24 | 15.06 | Au1rxx-base64 | 44.251.47.151 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.976 | 1.0 | 36 | 61 | prefer |
| DeltaKronecker-all | 0.902 | 0.824 | 245 | 5572 | prefer |
| Surfboard-tg-mixed | 0.841 | 0.767 | 86 | 5330 | prefer |
| Au1rxx-base64 | 0.792 | 0.777 | 193 | 432 | prefer |
| mheidari-all | 0.642 | 0.562 | 676 | 19639 | observe |
| xiaoji235-airport-v2ray-all | 0.391 | 1.0 | 2 | 4399 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4757 | observe |
| Epodonios-all | 0.255 | None | 0 | 6489 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3968 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6912 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4154 | observe |
| barry-far-vless | 0.255 | None | 0 | 4690 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4954 | observe |
| nscl5-all | 0.255 | None | 0 | 2435 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 194 |
| cn-block | TimeoutError | - | 64 |
| speed | ClientOSError | - | 57 |
| geo | ClientOSError | - | 26 |
| speed | TimeoutError | - | 25 |
| 204 | TimeoutError | - | 15 |
| 204 | ProxyError | - | 7 |
| cn-block | ClientOSError | - | 6 |
| 204 | ClientOSError | - | 4 |
| speed | ProxyError | - | 2 |
| cn-block | ProxyError | - | 2 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
