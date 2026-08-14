# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-14 02:28:38 |
| 运行耗时 | 342.3s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 79423 |
| 去重后节点 | 21338 |
| TCP 可达 | 3000 |
| 真实可用 | 997 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 21338 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.2 |
| geo | 1.0 |
| tcp | 33.2 |
| probe | 63.4 |
| real_test | 204.8 |
| generate | 34.7 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 43964 |
| vmess | 13621 |
| trojan | 10756 |
| shadowsocks | 9703 |
| hysteria2 | 1066 |
| http | 149 |
| socks | 80 |
| shadowsocksr | 68 |
| tuic | 8 |
| hysteria | 7 |
| anytls | 1 |

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
| 82.65 | http | 292.4 | 701.3 | 21.01 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.25 |
| 82.64 | http | 277.9 | 660.3 | 21.34 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.11 |
| 82.39 | http | 302.1 | 727.0 | 20.79 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.39 |
| 82.35 | vless | 260.8 | 681.0 | 21.74 | 0.0 | 10.0 | 10.95 | 19.66 | Au1rxx-base64 | 216.152.147.28 |
| 82.29 | http | 303.0 | 722.6 | 20.76 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.33 |
| 82.21 | http | 287.3 | 678.3 | 21.13 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.31 |
| 82.06 | http | 304.5 | 740.7 | 20.73 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.41 |
| 81.98 | http | 305.9 | 738.5 | 20.7 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.5 |
| 81.94 | hysteria2 | 265.0 | 672.4 | 21.64 | 0.0 | 10.0 | 11.74 | 19.66 | Au1rxx-base64 | 159.223.157.129 |
| 81.87 | http | 284.0 | 665.2 | 21.2 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.10 |
| 81.83 | http | 296.5 | 700.7 | 20.91 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.27 |
| 81.73 | http | 295.9 | 712.4 | 20.93 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.28 |
| 81.6 | hysteria2 | 284.2 | 686.7 | 21.2 | 0.0 | 10.0 | 11.74 | 19.66 | Au1rxx-base64 | 138.124.68.188 |
| 81.58 | trojan | 272.9 | 649.2 | 21.46 | 0.0 | 10.0 | 14.86 | 19.66 | Au1rxx-base64 | 64.94.95.117 |
| 81.25 | vless | 222.0 | 603.1 | 22.64 | 0.0 | 10.0 | 10.95 | 19.66 | Au1rxx-base64 | 195.211.98.214 |
| 81.06 | vless | 298.6 | 729.8 | 20.87 | 0.0 | 10.0 | 10.95 | 19.66 | Au1rxx-base64 | 204.48.20.223 |
| 80.23 | http | 280.8 | 661.0 | 21.28 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.34 |
| 79.41 | vless | 340.7 | 859.2 | 19.89 | 0.0 | 10.0 | 10.95 | 19.66 | Au1rxx-base64 | 167.17.69.171 |
| 79.31 | vless | 279.7 | 683.4 | 21.3 | 0.0 | 10.0 | 10.95 | 19.66 | Au1rxx-base64 | 169.40.42.179 |
| 79.14 | vless | 372.2 | 944.8 | 19.16 | 0.0 | 10.0 | 10.95 | 19.66 | Au1rxx-base64 | 169.40.42.182 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | 0.948 | 711 | 1965 | prefer |
| zhangkai | 0.999 | 1.0 | 128 | 159 | prefer |
| Surfboard-tg-mixed | 0.772 | 0.694 | 170 | 5918 | prefer |
| DeltaKronecker-all | 0.671 | 0.733 | 15 | 3656 | observe |
| mheidari-all | 0.443 | 0.361 | 169 | 16929 | observe |
| 10ium-ScrapeCategorize-Vless | 0.373 | 0.6 | 5 | 5203 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| Epodonios-all | 0.255 | None | 0 | 6600 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7655 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4638 | observe |
| barry-far-vless | 0.255 | None | 0 | 5003 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5197 | observe |
| Au1rxx-clash | 0.254 | None | 0 | 1965 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 68 |
| cn-block | TimeoutError | - | 39 |
| speed | TimeoutError | - | 39 |
| geo | ClientOSError | - | 20 |
| speed | ClientOSError | - | 18 |
| 204 | TimeoutError | - | 10 |
| 204 | ProxyError | - | 7 |
| cn-block | ProxyError | - | 4 |
| 204 | ClientOSError | - | 4 |
| cn-block | ClientOSError | - | 1 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
