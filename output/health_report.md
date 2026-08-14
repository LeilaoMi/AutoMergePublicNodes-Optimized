# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-14 13:22:42 |
| 运行耗时 | 299.9s |
| 订阅源总数 | 107 |
| 健康订阅源 | 102 |
| 原始节点 | 81447 |
| 去重后节点 | 23220 |
| TCP 可达 | 3000 |
| 真实可用 | 841 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23220 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.1 |
| geo | 0.8 |
| tcp | 34.8 |
| probe | 64.0 |
| real_test | 159.3 |
| generate | 36.0 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 44630 |
| vmess | 13652 |
| trojan | 11963 |
| shadowsocks | 9855 |
| hysteria2 | 1026 |
| http | 156 |
| socks | 76 |
| shadowsocksr | 70 |
| tuic | 10 |
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
| 83.8 | hysteria2 | 272.4 | 697.8 | 21.47 | 0.0 | 10.0 | 13.33 | 20.0 | Au1rxx-base64 | 138.124.68.188 |
| 82.64 | http | 288.8 | 694.7 | 21.09 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.11 |
| 82.34 | http | 288.4 | 686.9 | 21.1 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.31 |
| 82.24 | http | 300.8 | 718.5 | 20.82 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.33 |
| 82.06 | http | 295.8 | 692.4 | 20.93 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.41 |
| 82.04 | http | 298.9 | 707.5 | 20.86 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.27 |
| 82.03 | http | 290.5 | 685.3 | 21.05 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.25 |
| 81.88 | http | 295.6 | 711.4 | 20.93 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.5 |
| 81.88 | http | 301.7 | 726.9 | 20.79 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.9 |
| 81.86 | http | 305.4 | 736.2 | 20.71 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.15 |
| 81.83 | http | 299.0 | 718.2 | 20.86 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.8 |
| 81.6 | shadowsocks | 274.2 | 692.0 | 21.43 | 0.0 | 10.0 | 14.17 | 20.0 | Au1rxx-base64 | 37.19.198.244 |
| 81.32 | http | 291.4 | 703.4 | 21.03 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.28 |
| 81.27 | http | 315.6 | 767.2 | 20.47 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.21 |
| 81.08 | http | 313.2 | 767.7 | 20.53 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.34 |
| 81.0 | http | 300.4 | 720.5 | 20.82 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.19 |
| 80.99 | vless | 266.4 | 692.5 | 21.61 | 0.0 | 10.0 | 9.38 | 20.0 | Au1rxx-base64 | 216.152.147.28 |
| 80.94 | vless | 225.2 | 602.7 | 22.56 | 0.0 | 10.0 | 9.38 | 20.0 | Au1rxx-base64 | 195.211.98.214 |
| 80.9 | http | 314.7 | 757.7 | 20.49 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.4 |
| 80.75 | http | 293.3 | 702.1 | 20.99 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.39 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | 0.939 | 652 | 1959 | prefer |
| zhangkai | 0.999 | 1.0 | 127 | 159 | prefer |
| Surfboard-tg-mixed | 0.804 | 0.728 | 103 | 5728 | prefer |
| DeltaKronecker-all | 0.719 | 0.647 | 34 | 5969 | prefer |
| mheidari-all | 0.446 | 0.8 | 5 | 17030 | observe |
| nscl5-all | 0.326 | 1.0 | 1 | 1768 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5157 | observe |
| Epodonios-all | 0.255 | None | 0 | 6515 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7682 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4474 | observe |
| barry-far-vless | 0.255 | None | 0 | 4931 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5332 | observe |
| Au1rxx-clash | 0.253 | None | 0 | 1959 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | TimeoutError | - | 20 |
| speed | ClientOSError | - | 15 |
| geo | TimeoutError | - | 14 |
| cn-block | TimeoutError | - | 8 |
| speed | TimeoutError | - | 7 |
| 204 | ProxyError | - | 6 |
| geo | ClientOSError | - | 5 |
| cn-block | ClientOSError | - | 3 |
| cn-block | ProxyError | - | 2 |
| sing-box exited 1 |  [31mFATAL[0m[0000] start service: start inbound/socks[socks-in]: listen tcp 127.0.0.1:40102: bind: address already in use | - | 1 |
| 204 | ClientOSError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
