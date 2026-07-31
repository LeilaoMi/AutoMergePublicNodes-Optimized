# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-31 19:46:50 |
| 运行耗时 | 285.7s |
| 订阅源总数 | 107 |
| 健康订阅源 | 102 |
| 原始节点 | 78935 |
| 去重后节点 | 22858 |
| TCP 可达 | 3000 |
| 真实可用 | 470 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22858 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.6 |
| geo | 1.4 |
| tcp | 34.2 |
| probe | 62.7 |
| real_test | 138.3 |
| generate | 42.6 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 47455 |
| vmess | 11920 |
| shadowsocks | 10228 |
| trojan | 8485 |
| hysteria2 | 572 |
| http | 87 |
| shadowsocksr | 77 |
| socks | 57 |
| anytls | 26 |
| hysteria | 14 |
| tuic | 14 |

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
| 81.1 | vless | 198.1 | 485.1 | 23.19 | 0.0 | 10.0 | 11.37 | 17.54 | Au1rxx-base64 | 192.204.50.220 |
| 80.05 | vless | 260.2 | 606.8 | 21.76 | 0.0 | 10.0 | 11.37 | 17.54 | Au1rxx-base64 | 52.43.158.158 |
| 79.99 | http | 408.2 | 1143.4 | 18.33 | 0.0 | 10.0 | 14.82 | 19.84 | zhangkai | 138.199.35.198 |
| 79.91 | http | 411.7 | 1155.2 | 18.25 | 0.0 | 10.0 | 14.82 | 19.84 | zhangkai | 138.199.35.207 |
| 79.86 | http | 413.6 | 1160.2 | 18.2 | 0.0 | 10.0 | 14.82 | 19.84 | zhangkai | 138.199.35.209 |
| 79.86 | http | 413.6 | 1146.7 | 18.2 | 0.0 | 10.0 | 14.82 | 19.84 | zhangkai | 138.199.35.205 |
| 79.86 | http | 413.9 | 1164.4 | 18.2 | 0.0 | 10.0 | 14.82 | 19.84 | zhangkai | 138.199.35.204 |
| 79.86 | http | 413.9 | 1158.1 | 18.2 | 0.0 | 10.0 | 14.82 | 19.84 | zhangkai | 138.199.35.220 |
| 79.85 | http | 414.3 | 1163.9 | 18.19 | 0.0 | 10.0 | 14.82 | 19.84 | zhangkai | 138.199.35.199 |
| 79.84 | http | 414.6 | 1155.8 | 18.18 | 0.0 | 10.0 | 14.82 | 19.84 | zhangkai | 138.199.35.196 |
| 79.77 | vless | 212.5 | 539.3 | 22.86 | 0.0 | 10.0 | 11.37 | 17.54 | Au1rxx-base64 | 172.247.109.66 |
| 79.77 | http | 417.8 | 1171.6 | 18.11 | 0.0 | 10.0 | 14.82 | 19.84 | zhangkai | 138.199.35.217 |
| 79.75 | http | 418.3 | 1168.0 | 18.09 | 0.0 | 10.0 | 14.82 | 19.84 | zhangkai | 138.199.35.202 |
| 79.66 | http | 422.2 | 1165.8 | 18.0 | 0.0 | 10.0 | 14.82 | 19.84 | zhangkai | 138.199.35.197 |
| 78.39 | http | 477.4 | 1102.2 | 16.73 | 0.0 | 10.0 | 14.82 | 19.84 | zhangkai | 138.199.35.218 |
| 77.41 | shadowsocks | 226.5 | 505.6 | 22.54 | 0.0 | 9.53 | 11.8 | 17.54 | Au1rxx-base64 | 173.244.56.6 |
| 77.1 | shadowsocks | 225.5 | 508.2 | 22.56 | 0.0 | 9.53 | 11.8 | 17.54 | Au1rxx-base64 | 173.244.56.9 |
| 76.93 | shadowsocks | 247.1 | 597.9 | 22.06 | 0.0 | 9.53 | 11.8 | 17.54 | Au1rxx-base64 | 149.22.95.183 |
| 76.51 | shadowsocks | 243.7 | 616.7 | 22.14 | 0.0 | 9.53 | 11.8 | 17.54 | Au1rxx-base64 | 108.181.118.10 |
| 76.34 | vless | 205.7 | 522.8 | 23.02 | 0.0 | 9.41 | 11.37 | 17.54 | Au1rxx-base64 | 154.9.240.153 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.992 | 1.0 | 80 | 110 | prefer |
| Au1rxx-base64 | 0.763 | 0.697 | 508 | 1685 | prefer |
| mheidari-all | 0.569 | 0.488 | 43 | 16449 | observe |
| DeltaKronecker-all | 0.447 | 0.357 | 28 | 5144 | observe |
| Surfboard-tg-mixed | 0.373 | 0.6 | 5 | 5433 | observe |
| xiaoji235-airport-v2ray-all | 0.329 | 1.0 | 1 | 1861 | observe |
| tg-OutlineReleasedKey | 0.257 | 1.0 | 1 | 51 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5507 | observe |
| Epodonios-all | 0.255 | None | 0 | 6115 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3975 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6602 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4317 | observe |
| barry-far-vless | 0.255 | None | 0 | 4677 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5081 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 61 |
| 204 | TimeoutError | - | 34 |
| speed | TimeoutError | - | 26 |
| cn-block | TimeoutError | - | 20 |
| 204 | ProxyError | - | 20 |
| speed | ClientOSError | - | 15 |
| geo | ClientOSError | - | 9 |
| cn-block | ClientOSError | - | 5 |
| 204 | ClientOSError | - | 5 |
| cn-block | ProxyError | - | 3 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
