# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-22 12:53:58 |
| 运行耗时 | 309.8s |
| 订阅源总数 | 107 |
| 健康订阅源 | 99 |
| 原始节点 | 92293 |
| 去重后节点 | 23763 |
| TCP 可达 | 3000 |
| 真实可用 | 802 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23763 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.2 |
| geo | 1.1 |
| tcp | 38.4 |
| probe | 64.0 |
| real_test | 166.1 |
| generate | 33.9 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 52350 |
| trojan | 16168 |
| shadowsocks | 10804 |
| vmess | 10574 |
| hysteria2 | 1851 |
| shadowsocksr | 202 |
| http | 168 |
| socks | 116 |
| anytls | 32 |
| hysteria | 15 |
| tuic | 13 |

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
| 84.88 | http | 203.3 | 491.8 | 23.07 | 0.0 | 10.0 | 14.87 | 19.94 | zhangkai | 138.199.35.216 |
| 84.7 | http | 211.1 | 553.2 | 22.89 | 0.0 | 10.0 | 14.87 | 19.94 | zhangkai | 138.199.35.198 |
| 84.25 | trojan | 206.3 | 547.1 | 23.0 | 0.0 | 10.0 | 14.41 | 19.84 | Au1rxx-base64 | 14.1.28.76 |
| 82.27 | shadowsocks | 200.1 | 485.1 | 23.14 | 0.0 | 10.0 | 13.79 | 19.84 | Au1rxx-base64 | 108.181.0.177 |
| 81.81 | shadowsocks | 220.2 | 535.8 | 22.68 | 0.0 | 10.0 | 13.79 | 19.84 | Au1rxx-base64 | 108.181.118.10 |
| 81.55 | shadowsocks | 252.9 | 621.9 | 21.92 | 0.0 | 10.0 | 13.79 | 19.84 | Au1rxx-base64 | 156.146.38.169 |
| 81.37 | shadowsocks | 260.7 | 630.0 | 21.74 | 0.0 | 10.0 | 13.79 | 19.84 | Au1rxx-base64 | 173.244.56.9 |
| 81.36 | shadowsocks | 261.2 | 643.4 | 21.73 | 0.0 | 10.0 | 13.79 | 19.84 | Au1rxx-base64 | 156.146.38.168 |
| 81.08 | shadowsocks | 273.5 | 681.9 | 21.45 | 0.0 | 10.0 | 13.79 | 19.84 | Au1rxx-base64 | 173.244.56.6 |
| 80.47 | vless | 190.3 | 485.6 | 23.37 | 0.0 | 10.0 | 7.83 | 19.84 | Au1rxx-base64 | 70.39.198.183 |
| 80.29 | trojan | 255.8 | 513.4 | 21.86 | 0.0 | 10.0 | 14.41 | 19.84 | Au1rxx-base64 | 34.210.213.17 |
| 79.85 | trojan | 277.0 | 568.4 | 21.37 | 0.0 | 10.0 | 14.41 | 19.84 | Au1rxx-base64 | 44.243.85.47 |
| 79.8 | trojan | 274.2 | 558.7 | 21.43 | 0.0 | 10.0 | 14.41 | 19.84 | Au1rxx-base64 | 35.88.120.18 |
| 79.76 | trojan | 273.2 | 559.4 | 21.45 | 0.0 | 10.0 | 14.41 | 19.84 | Au1rxx-base64 | 34.223.2.163 |
| 79.74 | trojan | 276.3 | 571.8 | 21.38 | 0.0 | 10.0 | 14.41 | 19.84 | Au1rxx-base64 | 54.213.46.211 |
| 79.68 | trojan | 285.1 | 592.8 | 21.18 | 0.0 | 10.0 | 14.41 | 19.84 | Au1rxx-base64 | 44.255.190.116 |
| 79.56 | trojan | 288.9 | 492.7 | 21.09 | 0.0 | 10.0 | 14.41 | 19.84 | Au1rxx-base64 | 35.90.27.143 |
| 79.41 | trojan | 287.3 | 608.0 | 21.13 | 0.0 | 10.0 | 14.41 | 19.84 | Au1rxx-base64 | 44.246.163.102 |
| 79.4 | trojan | 290.8 | 612.7 | 21.05 | 0.0 | 9.84 | 14.41 | 19.84 | Au1rxx-base64 | liked-serval.rooster465.autos |
| 79.38 | trojan | 292.8 | 615.2 | 21.0 | 0.0 | 10.0 | 14.41 | 19.84 | Au1rxx-base64 | 35.91.251.124 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | 0.939 | 509 | 1674 | prefer |
| zhangkai | 0.988 | 0.991 | 112 | 144 | prefer |
| Surfboard-tg-mixed | 0.91 | 0.833 | 174 | 6287 | prefer |
| mheidari-all | 0.576 | 0.496 | 133 | 21719 | observe |
| nscl5-all | 0.335 | 1.0 | 1 | 3321 | observe |
| tg-oneclickvpnkeys | 0.261 | 1.0 | 1 | 161 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5096 | observe |
| Epodonios-all | 0.255 | None | 0 | 6868 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3984 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6876 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5093 | observe |
| barry-far-vless | 0.255 | None | 0 | 5403 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4074 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 5974 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | ClientOSError | - | 42 |
| geo | TimeoutError | - | 22 |
| cn-block | TimeoutError | - | 14 |
| 204 | TimeoutError | - | 13 |
| speed | TimeoutError | - | 12 |
| speed | ClientOSError | - | 9 |
| cn-block | ClientOSError | - | 6 |
| 204 | ProxyError | - | 5 |
| 204 | ClientOSError | - | 5 |
| speed | ProxyError | - | 3 |
| cn-block | ProxyError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
