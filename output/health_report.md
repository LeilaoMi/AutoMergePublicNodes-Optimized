# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-10 13:24:18 |
| 运行耗时 | 248.4s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 86629 |
| 去重后节点 | 24807 |
| TCP 可达 | 3000 |
| 真实可用 | 506 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 24807 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.9 |
| geo | 1.3 |
| tcp | 36.1 |
| probe | 55.8 |
| real_test | 121.5 |
| generate | 28.8 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 51755 |
| vmess | 13294 |
| trojan | 10177 |
| shadowsocks | 9768 |
| hysteria2 | 1370 |
| http | 77 |
| shadowsocksr | 74 |
| socks | 66 |
| anytls | 26 |
| hysteria | 14 |
| tuic | 8 |

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
| 80.71 | shadowsocks | 231.0 | 532.8 | 22.43 | 0.0 | 10.0 | 14.31 | 18.16 | Au1rxx-base64 | 149.22.95.183 |
| 80.42 | vless | 188.4 | 489.7 | 23.42 | 0.0 | 10.0 | 8.84 | 18.16 | Au1rxx-base64 | 179.255.148.66 |
| 80.36 | shadowsocks | 232.9 | 636.2 | 22.39 | 0.0 | 10.0 | 14.31 | 18.16 | Au1rxx-base64 | 108.181.118.10 |
| 80.02 | vless | 181.7 | 466.5 | 23.57 | 0.0 | 10.0 | 8.84 | 18.16 | Au1rxx-base64 | 70.39.198.183 |
| 80.01 | trojan | 219.1 | 492.8 | 22.71 | 0.0 | 9.02 | 12.62 | 18.16 | Au1rxx-base64 | 44.246.163.102 |
| 79.4 | vless | 189.9 | 492.2 | 23.38 | 0.0 | 9.02 | 8.84 | 18.16 | Au1rxx-base64 | 167.17.68.205 |
| 79.35 | vless | 234.5 | 617.1 | 22.35 | 0.0 | 10.0 | 8.84 | 18.16 | Au1rxx-base64 | 70.39.197.13 |
| 79.06 | vless | 198.7 | 518.9 | 23.18 | 0.0 | 8.88 | 8.84 | 18.16 | Au1rxx-base64 | jyvlryz.cvewfjg.shop |
| 79.04 | vless | 205.9 | 537.7 | 23.01 | 0.0 | 9.03 | 8.84 | 18.16 | Au1rxx-base64 | 107.173.237.146 |
| 78.65 | vless | 223.5 | 586.9 | 22.6 | 0.0 | 9.05 | 8.84 | 18.16 | Au1rxx-base64 | 186.241.106.97 |
| 78.56 | trojan | 215.0 | 481.2 | 22.8 | 0.0 | 8.87 | 12.62 | 18.16 | Au1rxx-base64 | devoted-tapir.rooster465.autos |
| 78.18 | shadowsocks | 326.8 | 868.4 | 20.21 | 0.0 | 10.0 | 14.31 | 18.16 | Au1rxx-base64 | 108.181.0.177 |
| 77.85 | shadowsocks | 309.9 | 782.3 | 20.61 | 0.0 | 10.0 | 14.31 | 18.16 | Au1rxx-base64 | 173.244.56.6 |
| 77.85 | shadowsocks | 319.7 | 770.8 | 20.38 | 0.0 | 10.0 | 14.31 | 18.16 | Au1rxx-base64 | 173.244.56.9 |
| 77.69 | vless | 258.9 | 500.8 | 21.79 | 0.0 | 10.0 | 8.84 | 18.16 | Au1rxx-base64 | 172.64.152.241 |
| 76.56 | vless | 220.9 | 518.9 | 22.66 | 0.0 | 10.0 | 8.84 | 18.16 | Au1rxx-base64 | 172.64.145.158 |
| 76.46 | vless | 230.9 | 575.4 | 22.43 | 0.0 | 9.03 | 8.84 | 18.16 | Au1rxx-base64 | 31.58.50.200 |
| 76.15 | hysteria2 | 340.5 | 721.0 | 19.9 | 0.0 | 10.0 | 13.12 | 18.16 | Au1rxx-base64 | 159.223.157.129 |
| 76.02 | vless | 262.2 | 563.8 | 21.71 | 0.0 | 9.05 | 8.84 | 18.16 | Au1rxx-base64 | 70.39.178.231 |
| 75.68 | hysteria2 | 356.9 | 753.9 | 19.52 | 0.0 | 10.0 | 13.12 | 18.16 | Au1rxx-base64 | 138.124.68.188 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.969 | 0.904 | 437 | 1668 | prefer |
| zhangkai | 0.964 | 0.98 | 50 | 67 | prefer |
| Surfboard-tg-mixed | 0.724 | 0.648 | 71 | 6388 | prefer |
| mheidari-all | 0.497 | 0.409 | 22 | 20526 | observe |
| tg-oneclickvpnkeys | 0.405 | 1.0 | 4 | 122 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| Epodonios-all | 0.255 | None | 0 | 7165 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3996 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7747 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5219 | observe |
| barry-far-vless | 0.255 | None | 0 | 5695 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5191 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.242 | None | 0 | 1668 | observe |
| nscl5-all | 0.233 | None | 0 | 1442 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| cn-block | TimeoutError | - | 19 |
| 204 | TimeoutError | - | 18 |
| speed | TimeoutError | - | 15 |
| 204 | ProxyError | - | 11 |
| geo | ClientOSError | - | 9 |
| geo | TimeoutError | - | 9 |
| speed | ClientOSError | - | 6 |
| 204 | ClientOSError | - | 5 |
| cn-block | ClientOSError | - | 4 |
| cn-block | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
