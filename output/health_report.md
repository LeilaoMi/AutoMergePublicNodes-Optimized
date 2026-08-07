# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-07 19:08:08 |
| 运行耗时 | 240.7s |
| 订阅源总数 | 107 |
| 健康订阅源 | 100 |
| 原始节点 | 82638 |
| 去重后节点 | 23519 |
| TCP 可达 | 3000 |
| 真实可用 | 455 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23519 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.9 |
| geo | 1.4 |
| tcp | 36.0 |
| probe | 56.4 |
| real_test | 104.4 |
| generate | 36.5 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 47473 |
| vmess | 12852 |
| trojan | 11076 |
| shadowsocks | 9757 |
| hysteria2 | 1282 |
| shadowsocksr | 75 |
| socks | 65 |
| http | 35 |
| hysteria | 13 |
| tuic | 8 |
| anytls | 2 |

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
| 81.63 | shadowsocks | 236.9 | 589.0 | 22.29 | 0.0 | 10.0 | 13.46 | 19.88 | Au1rxx-base64 | 156.146.38.169 |
| 81.63 | shadowsocks | 237.2 | 604.9 | 22.29 | 0.0 | 10.0 | 13.46 | 19.88 | Au1rxx-base64 | 156.146.38.168 |
| 81.45 | shadowsocks | 244.9 | 626.6 | 22.11 | 0.0 | 10.0 | 13.46 | 19.88 | Au1rxx-base64 | 156.146.38.170 |
| 80.74 | hysteria2 | 350.8 | 871.7 | 19.66 | 0.0 | 10.0 | 12.5 | 19.88 | Au1rxx-base64 | 138.124.68.188 |
| 80.68 | http | 247.3 | 551.4 | 22.05 | 0.0 | 10.0 | 14.32 | 19.12 | zhangkai | 138.199.35.199 |
| 80.08 | hysteria2 | 305.7 | 700.9 | 20.7 | 0.0 | 10.0 | 12.5 | 19.88 | Au1rxx-base64 | 159.223.157.129 |
| 77.61 | trojan | 322.3 | 682.5 | 20.32 | 0.0 | 10.0 | 13.99 | 19.88 | Au1rxx-base64 | 44.244.3.114 |
| 77.57 | shadowsocks | 277.8 | 565.4 | 21.35 | 0.0 | 10.0 | 13.46 | 19.88 | Au1rxx-base64 | 173.244.56.6 |
| 77.55 | trojan | 325.5 | 689.8 | 20.24 | 0.0 | 10.0 | 13.99 | 19.88 | Au1rxx-base64 | 35.86.90.51 |
| 77.37 | trojan | 331.4 | 707.5 | 20.11 | 0.0 | 10.0 | 13.99 | 19.88 | Au1rxx-base64 | 44.242.235.129 |
| 77.24 | shadowsocks | 265.5 | 527.0 | 21.63 | 0.0 | 10.0 | 13.46 | 19.88 | Au1rxx-base64 | 108.181.0.177 |
| 76.94 | shadowsocks | 315.6 | 710.5 | 20.47 | 0.0 | 10.0 | 13.46 | 19.88 | Au1rxx-base64 | 37.19.198.236 |
| 76.73 | trojan | 285.2 | 567.7 | 21.17 | 0.0 | 10.0 | 13.99 | 19.88 | Au1rxx-base64 | 44.246.163.102 |
| 76.66 | shadowsocks | 268.3 | 530.7 | 21.57 | 0.0 | 10.0 | 13.46 | 19.88 | Au1rxx-base64 | 108.181.118.10 |
| 76.51 | shadowsocks | 242.1 | 619.6 | 22.17 | 0.0 | 10.0 | 13.46 | 19.88 | Au1rxx-base64 | 156.146.38.167 |
| 76.19 | shadowsocks | 315.0 | 710.3 | 20.49 | 0.0 | 10.0 | 13.46 | 19.88 | Au1rxx-base64 | 173.244.56.9 |
| 75.87 | shadowsocks | 312.7 | 663.6 | 20.54 | 0.0 | 10.0 | 13.46 | 19.88 | Au1rxx-base64 | 37.19.198.244 |
| 75.87 | trojan | 336.0 | 871.5 | 20.0 | 0.0 | 10.0 | 13.99 | 19.88 | Au1rxx-base64 | 64.94.95.114 |
| 75.87 | trojan | 336.1 | 863.9 | 20.0 | 0.0 | 10.0 | 13.99 | 19.88 | Au1rxx-base64 | 64.94.95.115 |
| 75.86 | trojan | 336.6 | 867.0 | 19.99 | 0.0 | 10.0 | 13.99 | 19.88 | Au1rxx-base64 | 64.94.95.118 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.989 | 0.931 | 350 | 1506 | prefer |
| zhangkai | 0.91 | 0.95 | 20 | 25 | prefer |
| DeltaKronecker-all | 0.605 | 0.526 | 175 | 5326 | observe |
| Surfboard-tg-mixed | 0.556 | 0.667 | 12 | 6368 | observe |
| ninja-vless | 0.457 | 0.714 | 7 | 1791 | observe |
| mheidari-all | 0.401 | 0.571 | 7 | 17684 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5282 | observe |
| Epodonios-all | 0.255 | None | 0 | 7096 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3996 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7593 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5103 | observe |
| barry-far-vless | 0.255 | None | 0 | 5504 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5175 | observe |
| Au1rxx-clash | 0.235 | None | 0 | 1506 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | ProxyError | - | 29 |
| 204 | TimeoutError | - | 25 |
| geo | ClientOSError | - | 15 |
| geo | TimeoutError | - | 13 |
| cn-block | TimeoutError | - | 9 |
| speed | ClientOSError | - | 9 |
| speed | TimeoutError | - | 7 |
| 204 | ClientOSError | - | 5 |
| cn-block | ClientOSError | - | 4 |
| speed | ProxyError | - | 2 |
| cn-block | ProxyError | - | 1 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
