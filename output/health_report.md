# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-08 13:02:20 |
| 运行耗时 | 217.1s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 83600 |
| 去重后节点 | 23665 |
| TCP 可达 | 3000 |
| 真实可用 | 411 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23665 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.9 |
| geo | 1.1 |
| tcp | 34.9 |
| probe | 50.9 |
| real_test | 87.2 |
| generate | 37.0 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 49033 |
| vmess | 12926 |
| trojan | 10527 |
| shadowsocks | 9603 |
| hysteria2 | 1313 |
| shadowsocksr | 75 |
| socks | 63 |
| http | 36 |
| hysteria | 13 |
| tuic | 10 |
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
| 83.86 | http | 188.2 | 486.7 | 23.42 | 0.0 | 10.0 | 14.32 | 19.12 | zhangkai | 138.199.35.199 |
| 83.82 | http | 189.9 | 481.7 | 23.38 | 0.0 | 10.0 | 14.32 | 19.12 | zhangkai | 138.199.35.214 |
| 83.8 | http | 190.9 | 489.4 | 23.36 | 0.0 | 10.0 | 14.32 | 19.12 | zhangkai | 138.199.35.207 |
| 83.01 | trojan | 223.0 | 499.7 | 22.62 | 0.0 | 10.0 | 13.01 | 19.88 | Au1rxx-base64 | 44.246.163.102 |
| 82.74 | trojan | 234.3 | 534.8 | 22.35 | 0.0 | 10.0 | 13.01 | 19.88 | Au1rxx-base64 | 44.244.3.114 |
| 82.73 | trojan | 234.8 | 532.6 | 22.34 | 0.0 | 10.0 | 13.01 | 19.88 | Au1rxx-base64 | devoted-tapir.rooster465.autos |
| 82.16 | shadowsocks | 224.5 | 534.2 | 22.58 | 0.0 | 10.0 | 13.7 | 19.88 | Au1rxx-base64 | 173.244.56.9 |
| 82.15 | shadowsocks | 224.9 | 534.3 | 22.57 | 0.0 | 10.0 | 13.7 | 19.88 | Au1rxx-base64 | 173.244.56.6 |
| 81.45 | trojan | 270.3 | 645.6 | 21.52 | 0.0 | 10.0 | 13.01 | 19.88 | Au1rxx-base64 | 35.86.90.51 |
| 81.08 | trojan | 306.3 | 754.5 | 20.69 | 0.0 | 10.0 | 13.01 | 19.88 | Au1rxx-base64 | 44.242.235.129 |
| 80.89 | http | 186.8 | 479.6 | 23.45 | 0.0 | 10.0 | 14.32 | 19.12 | zhangkai | 138.199.35.217 |
| 80.41 | trojan | 231.2 | 525.3 | 22.43 | 0.0 | 7.59 | 13.01 | 19.88 | Au1rxx-base64 | fleet-bonefish.rooster465.autos |
| 79.75 | trojan | 251.2 | 578.0 | 21.96 | 0.0 | 7.52 | 13.01 | 19.88 | Au1rxx-base64 | pet-ghost.rooster465.autos |
| 79.19 | shadowsocks | 223.1 | 512.4 | 22.61 | 0.0 | 10.0 | 13.7 | 19.88 | Au1rxx-base64 | 149.22.95.183 |
| 78.25 | hysteria2 | 358.5 | 773.5 | 19.48 | 0.0 | 10.0 | 13.39 | 19.88 | Au1rxx-base64 | 138.124.68.188 |
| 77.86 | shadowsocks | 295.7 | 671.4 | 20.93 | 0.0 | 10.0 | 13.7 | 19.88 | Au1rxx-base64 | 156.146.38.169 |
| 77.78 | shadowsocks | 295.7 | 673.8 | 20.93 | 0.0 | 10.0 | 13.7 | 19.88 | Au1rxx-base64 | 156.146.38.168 |
| 77.71 | shadowsocks | 292.9 | 664.4 | 21.0 | 0.0 | 10.0 | 13.7 | 19.88 | Au1rxx-base64 | 156.146.38.170 |
| 77.49 | hysteria2 | 352.3 | 720.6 | 19.62 | 0.0 | 10.0 | 13.39 | 19.88 | Au1rxx-base64 | 159.223.157.129 |
| 77.17 | hysteria2 | 350.4 | 762.0 | 19.67 | 0.0 | 8.54 | 13.39 | 19.88 | Au1rxx-base64 | usa1.spectrumproxy.shop |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.996 | 0.939 | 342 | 1488 | prefer |
| zhangkai | 0.956 | 1.0 | 20 | 25 | prefer |
| Surfboard-tg-mixed | 0.676 | 0.598 | 87 | 6570 | observe |
| mheidari-all | 0.438 | 1.0 | 3 | 17827 | observe |
| tg-oneclickvpnkeys | 0.263 | 1.0 | 1 | 196 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| DeltaKronecker-all | 0.257 | 0.169 | 77 | 5347 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5450 | observe |
| Epodonios-all | 0.255 | None | 0 | 7203 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7636 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5374 | observe |
| barry-far-vless | 0.255 | None | 0 | 5686 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5162 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | ClientOSError | - | 29 |
| 204 | TimeoutError | - | 28 |
| geo | TimeoutError | - | 18 |
| cn-block | TimeoutError | - | 13 |
| speed | ClientOSError | - | 11 |
| speed | TimeoutError | - | 10 |
| 204 | ProxyError | - | 6 |
| cn-block | ClientOSError | - | 3 |
| cn-block | ProxyError | - | 1 |
| geo | ProxyError | - | 1 |
| 204 | ClientOSError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
