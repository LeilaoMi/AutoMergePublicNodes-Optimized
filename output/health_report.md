# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-19 01:43:03 |
| 运行耗时 | 392.0s |
| 订阅源总数 | 107 |
| 健康订阅源 | 100 |
| 原始节点 | 82111 |
| 去重后节点 | 22333 |
| TCP 可达 | 3000 |
| 真实可用 | 1440 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22333 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.5 |
| geo | 0.6 |
| tcp | 33.6 |
| probe | 76.9 |
| real_test | 248.3 |
| generate | 27.2 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 44949 |
| trojan | 17069 |
| shadowsocks | 9899 |
| vmess | 8641 |
| hysteria2 | 1142 |
| http | 179 |
| socks | 117 |
| shadowsocksr | 93 |
| tuic | 8 |
| hysteria | 7 |
| anytls | 7 |

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
| 84.22 | http | 234.0 | 631.4 | 22.36 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.21 |
| 84.2 | http | 234.8 | 625.5 | 22.34 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.25 |
| 84.19 | http | 235.4 | 627.9 | 22.33 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.10 |
| 84.13 | http | 238.1 | 634.3 | 22.27 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.11 |
| 84.11 | http | 238.8 | 629.4 | 22.25 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.23 |
| 84.07 | http | 240.6 | 642.4 | 22.21 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.19 |
| 84.05 | http | 241.4 | 632.8 | 22.19 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.34 |
| 84.04 | http | 241.9 | 646.3 | 22.18 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.28 |
| 83.9 | http | 247.8 | 671.7 | 22.04 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.9 |
| 83.86 | http | 249.7 | 675.1 | 22.0 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.27 |
| 83.83 | http | 251.1 | 667.5 | 21.97 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.8 |
| 83.82 | http | 251.4 | 676.4 | 21.96 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.31 |
| 83.8 | http | 252.1 | 673.0 | 21.94 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.4 |
| 83.78 | http | 253.0 | 670.4 | 21.92 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.15 |
| 83.76 | http | 254.0 | 677.3 | 21.9 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.41 |
| 83.68 | http | 257.2 | 686.9 | 21.82 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.33 |
| 82.47 | http | 309.5 | 849.6 | 20.61 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.5 |
| 81.93 | vless | 259.6 | 681.0 | 21.77 | 0.0 | 10.0 | 10.16 | 20.0 | Au1rxx-base64 | 169.40.42.89 |
| 81.84 | vless | 263.4 | 626.5 | 21.68 | 0.0 | 10.0 | 10.16 | 20.0 | Au1rxx-base64 | 195.211.99.45 |
| 81.62 | shadowsocks | 225.4 | 618.6 | 22.56 | 0.0 | 10.0 | 13.12 | 19.94 | Surfboard-tg-mixed | 37.19.198.236 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | 0.991 | 817 | 1745 | prefer |
| mheidari-all | 1.0 | 0.936 | 265 | 16675 | prefer |
| zhangkai | 0.999 | 1.0 | 127 | 159 | prefer |
| Surfboard-tg-mixed | 0.889 | 0.811 | 296 | 6344 | prefer |
| nscl5-all | 0.519 | 1.0 | 5 | 3330 | observe |
| roosterkid-openproxylist-v2ray | 0.261 | 1.0 | 1 | 150 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5068 | observe |
| Epodonios-all | 0.255 | None | 0 | 6993 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3988 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7254 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4847 | observe |
| barry-far-vless | 0.255 | None | 0 | 5142 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4035 | observe |
| Au1rxx-clash | 0.245 | None | 0 | 1745 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 64 |
| speed | TimeoutError | - | 24 |
| geo | ClientOSError | - | 23 |
| speed | ClientOSError | - | 13 |
| cn-block | TimeoutError | - | 6 |
| 204 | ClientOSError | - | 4 |
| cn-block | ClientOSError | - | 3 |
| 204 | TimeoutError | - | 3 |
| 204 | ProxyError | - | 2 |
| cn-block | ProxyError | - | 1 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
