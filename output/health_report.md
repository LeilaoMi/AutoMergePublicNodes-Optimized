# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.9.1 |
| 更新时间 | 2026-06-20 14:23:16 |
| 运行耗时 | 435.2s |
| 订阅源总数 | 107 |
| 健康订阅源 | 104 |
| 原始节点 | 73120 |
| 去重后节点 | 21770 |
| TCP 可达 | 793 |
| 真实可用 | 614 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 21770 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.0 |
| geo | 1.3 |
| tcp | 60.9 |
| probe | 112.8 |
| real_test | 203.1 |
| generate | 52.0 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 42435 |
| trojan | 10174 |
| shadowsocks | 10088 |
| vmess | 9840 |
| hysteria2 | 237 |
| shadowsocksr | 165 |
| http | 96 |
| socks | 77 |
| hysteria | 6 |
| tuic | 2 |

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
| 76.22 | vless | 320.6 | 847.5 | 20.36 | 0.0 | 10.0 | 11.16 | 16.3 | Au1rxx-base64 | 15.204.97.214 |
| 75.72 | shadowsocks | 219.4 | 511.4 | 22.7 | 0.0 | 10.0 | 12.92 | 16.3 | Au1rxx-base64 | 149.22.95.183 |
| 75.08 | vless | 304.9 | 804.4 | 20.72 | 0.0 | 10.0 | 11.16 | 16.3 | Au1rxx-base64 | 15.204.97.219 |
| 74.8 | shadowsocks | 263.2 | 659.8 | 21.68 | 0.0 | 10.0 | 12.92 | 16.3 | Au1rxx-base64 | 173.244.56.6 |
| 73.3 | shadowsocks | 220.1 | 494.5 | 22.68 | 0.0 | 10.0 | 12.92 | 16.3 | Au1rxx-base64 | 173.244.56.9 |
| 71.97 | vless | 290.8 | 805.5 | 21.05 | 0.0 | 10.0 | 11.16 | 17.26 | Surfboard-tg-mixed | 141.193.154.182 |
| 71.19 | shadowsocks | 293.4 | 660.9 | 20.99 | 0.0 | 10.0 | 12.92 | 16.3 | Au1rxx-base64 | 156.146.38.169 |
| 71.04 | shadowsocks | 295.1 | 671.0 | 20.95 | 0.0 | 10.0 | 12.92 | 16.3 | Au1rxx-base64 | 156.146.38.170 |
| 71.0 | shadowsocks | 290.3 | 651.9 | 21.06 | 0.0 | 10.0 | 12.92 | 16.3 | Au1rxx-base64 | 156.146.38.167 |
| 70.35 | shadowsocks | 336.1 | 790.8 | 20.0 | 0.0 | 10.0 | 12.92 | 16.3 | Au1rxx-base64 | 156.146.38.168 |
| 69.45 | vless | 349.0 | 388.8 | 19.7 | 0.42 | 9.94 | 11.16 | 17.7 | mheidari-all | 31.76.91.26 |
| 68.92 | shadowsocks | 517.3 | 1490.5 | 15.8 | 0.0 | 10.0 | 12.92 | 16.3 | Au1rxx-base64 | 167.160.90.51 |
| 68.84 | vless | 347.6 | 396.3 | 19.73 | 0.14 | 9.94 | 11.16 | 17.26 | Surfboard-tg-mixed | 31.76.91.28 |
| 68.11 | shadowsocks | 292.1 | 337.5 | 21.02 | 2.34 | 9.94 | 12.92 | 16.3 | Au1rxx-base64 | 149.22.87.241 |
| 67.95 | vless | 268.3 | 705.4 | 21.57 | 0.0 | 10.0 | 11.16 | 17.26 | Surfboard-tg-mixed | 5.78.62.9 |
| 67.81 | vless | 350.7 | 406.0 | 19.66 | 0.0 | 9.94 | 11.16 | 17.26 | Surfboard-tg-mixed | 31.76.91.18 |
| 67.66 | shadowsocks | 294.6 | 344.3 | 20.96 | 2.09 | 9.93 | 12.92 | 16.3 | Au1rxx-base64 | 149.22.87.204 |
| 67.65 | shadowsocks | 296.4 | 346.7 | 20.92 | 2.0 | 9.93 | 12.92 | 16.3 | Au1rxx-base64 | 149.22.87.240 |
| 66.52 | shadowsocks | 374.1 | 759.7 | 19.12 | 0.0 | 10.0 | 12.92 | 16.3 | Au1rxx-base64 | 37.19.198.244 |
| 66.52 | vless | 426.7 | 359.4 | 17.9 | 1.52 | 9.49 | 11.16 | 17.26 | Surfboard-tg-mixed | 64.49.45.57 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.966 | 1.0 | 25 | 73 | prefer |
| Surfboard-tg-mixed | 0.895 | 0.816 | 414 | 4892 | prefer |
| Au1rxx-base64 | 0.816 | 0.833 | 30 | 86 | prefer |
| mheidari-all | 0.809 | 0.731 | 271 | 14626 | prefer |
| DeltaKronecker-all | 0.608 | 0.529 | 51 | 6810 | observe |
| nscl5-all | 0.3 | 1.0 | 1 | 1126 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4507 | observe |
| Epodonios-all | 0.255 | None | 0 | 7484 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3974 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7110 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 3696 | observe |
| barry-far-vless | 0.255 | None | 0 | 4525 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4516 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |
| xiaoji235-airport-v2ray-all | 0.212 | None | 0 | 913 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 60 |
| cn-block | TimeoutError | - | 32 |
| 204 | TimeoutError | - | 18 |
| 204 | ProxyError | - | 16 |
| geo | TimeoutError | - | 14 |
| 204 | ClientOSError | - | 10 |
| geo | ClientOSError | - | 9 |
| cn-block | ClientOSError | - | 8 |
| speed | TimeoutError | - | 5 |
| geo | ProxyError | - | 3 |
| cn-block | ProxyError | - | 3 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
