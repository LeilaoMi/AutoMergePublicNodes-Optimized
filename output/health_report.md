# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-13 19:14:21 |
| 运行耗时 | 319.8s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 80087 |
| 去重后节点 | 22489 |
| TCP 可达 | 3000 |
| 真实可用 | 838 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22489 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.2 |
| geo | 1.0 |
| tcp | 33.3 |
| probe | 70.0 |
| real_test | 161.1 |
| generate | 48.3 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 44889 |
| vmess | 13324 |
| trojan | 10244 |
| shadowsocks | 9968 |
| hysteria2 | 1339 |
| http | 152 |
| socks | 78 |
| shadowsocksr | 76 |
| tuic | 8 |
| hysteria | 7 |
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
| 83.87 | http | 249.3 | 674.7 | 22.01 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.28 |
| 83.86 | http | 249.7 | 669.0 | 22.0 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.15 |
| 83.75 | http | 254.2 | 685.3 | 21.89 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.31 |
| 83.14 | hysteria2 | 232.2 | 637.4 | 22.4 | 0.0 | 10.0 | 11.84 | 20.0 | Au1rxx-base64 | 159.223.157.129 |
| 82.87 | vless | 246.5 | 644.4 | 22.07 | 0.0 | 10.0 | 10.8 | 20.0 | Au1rxx-base64 | 204.48.20.223 |
| 82.78 | hysteria2 | 252.2 | 687.2 | 21.94 | 0.0 | 10.0 | 11.84 | 20.0 | Au1rxx-base64 | 138.124.68.188 |
| 82.66 | vless | 255.6 | 665.5 | 21.86 | 0.0 | 10.0 | 10.8 | 20.0 | Au1rxx-base64 | 167.17.69.171 |
| 81.85 | shadowsocks | 248.6 | 654.4 | 22.02 | 0.0 | 10.0 | 13.83 | 20.0 | Au1rxx-base64 | 37.19.198.236 |
| 81.69 | shadowsocks | 255.6 | 676.9 | 21.86 | 0.0 | 10.0 | 13.83 | 20.0 | Au1rxx-base64 | 37.19.198.244 |
| 81.45 | http | 353.7 | 977.9 | 19.59 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.34 |
| 81.42 | http | 355.2 | 977.9 | 19.56 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.39 |
| 81.33 | http | 359.0 | 995.3 | 19.47 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.27 |
| 81.21 | http | 364.0 | 1012.4 | 19.35 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.41 |
| 80.92 | vless | 330.9 | 838.8 | 20.12 | 0.0 | 10.0 | 10.8 | 20.0 | Au1rxx-base64 | 158.69.112.254 |
| 80.82 | http | 381.0 | 1053.2 | 18.96 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.33 |
| 80.48 | vless | 345.0 | 866.2 | 19.79 | 0.0 | 10.0 | 10.8 | 20.0 | Au1rxx-base64 | 216.152.147.28 |
| 79.63 | http | 432.2 | 1199.4 | 17.77 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.4 |
| 79.52 | http | 437.0 | 1214.8 | 17.66 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.9 |
| 79.46 | http | 439.9 | 1234.3 | 17.6 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.8 |
| 79.43 | http | 441.2 | 1242.0 | 17.57 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.21 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.999 | 1.0 | 127 | 159 | prefer |
| Au1rxx-base64 | 0.983 | 0.919 | 616 | 1639 | prefer |
| mheidari-all | 0.91 | 0.836 | 110 | 16814 | prefer |
| Surfboard-tg-mixed | 0.715 | 0.639 | 72 | 6036 | prefer |
| DeltaKronecker-all | 0.461 | 0.545 | 11 | 4878 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5203 | observe |
| Epodonios-all | 0.255 | None | 0 | 6692 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3996 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7502 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4739 | observe |
| barry-far-vless | 0.255 | None | 0 | 5103 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5197 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.241 | None | 0 | 1639 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | TimeoutError | - | 19 |
| cn-block | TimeoutError | - | 18 |
| geo | TimeoutError | - | 17 |
| 204 | ProxyError | - | 11 |
| 204 | ClientOSError | - | 10 |
| geo | ClientOSError | - | 7 |
| speed | ClientOSError | - | 7 |
| speed | TimeoutError | - | 5 |
| geo | ProxyError | - | 2 |
| cn-block | ClientOSError | - | 2 |
| cn-block | ProxyError | - | 1 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
