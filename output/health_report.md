# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-11 13:21:15 |
| 运行耗时 | 233.4s |
| 订阅源总数 | 107 |
| 健康订阅源 | 102 |
| 原始节点 | 84618 |
| 去重后节点 | 24389 |
| TCP 可达 | 3000 |
| 真实可用 | 537 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 24389 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.0 |
| geo | 1.4 |
| tcp | 36.3 |
| probe | 49.9 |
| real_test | 113.5 |
| generate | 26.3 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 48886 |
| vmess | 13380 |
| trojan | 10676 |
| shadowsocks | 10009 |
| hysteria2 | 1318 |
| http | 159 |
| shadowsocksr | 74 |
| socks | 69 |
| anytls | 26 |
| hysteria | 13 |
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
| 83.37 | hysteria2 | 238.7 | 656.7 | 22.25 | 0.0 | 10.0 | 13.24 | 18.98 | Au1rxx-base64 | 159.223.157.129 |
| 82.02 | http | 308.1 | 847.6 | 20.65 | 0.0 | 10.0 | 14.71 | 19.66 | zhangkai | 156.146.59.5 |
| 81.99 | http | 309.3 | 850.7 | 20.62 | 0.0 | 10.0 | 14.71 | 19.66 | zhangkai | 156.146.59.23 |
| 81.89 | http | 313.7 | 865.2 | 20.52 | 0.0 | 10.0 | 14.71 | 19.66 | zhangkai | 156.146.59.25 |
| 81.63 | http | 325.0 | 889.8 | 20.26 | 0.0 | 10.0 | 14.71 | 19.66 | zhangkai | 156.146.59.8 |
| 81.62 | http | 325.1 | 893.8 | 20.25 | 0.0 | 10.0 | 14.71 | 19.66 | zhangkai | 156.146.59.21 |
| 80.87 | shadowsocks | 231.4 | 632.6 | 22.42 | 0.0 | 10.0 | 13.47 | 18.98 | Au1rxx-base64 | 37.19.198.160 |
| 80.66 | shadowsocks | 240.5 | 667.4 | 22.21 | 0.0 | 10.0 | 13.47 | 18.98 | Au1rxx-base64 | 37.19.198.244 |
| 80.63 | shadowsocks | 241.9 | 664.0 | 22.18 | 0.0 | 10.0 | 13.47 | 18.98 | Au1rxx-base64 | 37.19.198.243 |
| 80.39 | shadowsocks | 252.4 | 687.6 | 21.94 | 0.0 | 10.0 | 13.47 | 18.98 | Au1rxx-base64 | 37.19.198.236 |
| 80.21 | http | 386.3 | 1075.8 | 18.84 | 0.0 | 10.0 | 14.71 | 19.66 | zhangkai | 156.146.59.33 |
| 79.42 | http | 377.1 | 1041.6 | 19.05 | 0.0 | 10.0 | 14.71 | 19.66 | zhangkai | 156.146.59.41 |
| 77.67 | shadowsocks | 278.0 | 628.0 | 21.34 | 0.0 | 10.0 | 13.47 | 18.98 | Au1rxx-base64 | 156.146.38.168 |
| 77.16 | shadowsocks | 370.2 | 890.1 | 19.21 | 0.0 | 10.0 | 13.47 | 18.98 | Au1rxx-base64 | 68.168.222.210 |
| 77.14 | http | 302.8 | 832.0 | 20.77 | 0.0 | 10.0 | 14.71 | 19.66 | zhangkai | 156.146.59.10 |
| 77.06 | shadowsocks | 283.0 | 654.9 | 21.23 | 0.0 | 10.0 | 13.47 | 18.98 | Au1rxx-base64 | 156.146.38.169 |
| 76.88 | http | 313.9 | 858.7 | 20.51 | 0.0 | 10.0 | 14.71 | 19.66 | zhangkai | 156.146.59.19 |
| 76.86 | http | 314.9 | 853.6 | 20.49 | 0.0 | 10.0 | 14.71 | 19.66 | zhangkai | 156.146.59.11 |
| 76.85 | http | 315.1 | 861.2 | 20.48 | 0.0 | 10.0 | 14.71 | 19.66 | zhangkai | 156.146.59.9 |
| 76.82 | http | 316.6 | 866.6 | 20.45 | 0.0 | 10.0 | 14.71 | 19.66 | zhangkai | 156.146.59.4 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.999 | 1.0 | 128 | 159 | prefer |
| Au1rxx-base64 | 0.912 | 0.854 | 391 | 1501 | prefer |
| Surfboard-tg-mixed | 0.721 | 0.644 | 90 | 6195 | prefer |
| mheidari-all | 0.602 | 0.588 | 17 | 20194 | observe |
| DeltaKronecker-all | 0.389 | 0.385 | 13 | 5522 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| roosterkid-openproxylist-v2ray | 0.261 | 1.0 | 1 | 150 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5419 | observe |
| Epodonios-all | 0.255 | None | 0 | 6769 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7602 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5048 | observe |
| barry-far-vless | 0.255 | None | 0 | 5245 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5209 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | TimeoutError | - | 23 |
| 204 | ProxyError | - | 18 |
| 204 | TimeoutError | - | 17 |
| geo | ClientOSError | - | 16 |
| speed | ClientOSError | - | 10 |
| geo | TimeoutError | - | 8 |
| cn-block | TimeoutError | - | 4 |
| 204 | ClientOSError | - | 4 |
| cn-block | ProxyError | - | 2 |
| cn-block | ClientOSError | - | 2 |
| speed | ProxyError | - | 1 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
