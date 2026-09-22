# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-22 21:14:35 |
| 运行耗时 | 513.8s |
| 订阅源总数 | 107 |
| 健康订阅源 | 96 |
| 原始节点 | 84314 |
| 去重后节点 | 23820 |
| TCP 可达 | 3000 |
| 真实可用 | 484 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23820 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.8 |
| geo | 1.4 |
| tcp | 39.5 |
| probe | 182.3 |
| real_test | 201.8 |
| generate | 82.9 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 51036 |
| vmess | 13649 |
| shadowsocks | 9723 |
| trojan | 8041 |
| hysteria2 | 1035 |
| http | 584 |
| shadowsocksr | 164 |
| socks | 64 |
| hysteria | 11 |
| tuic | 4 |
| anytls | 3 |

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
| 80.14 | shadowsocks | 260.1 | 649.7 | 21.76 | 0.0 | 10.0 | 13.9 | 18.48 | Au1rxx-base64 | 156.146.38.170 |
| 79.72 | hysteria2 | 298.4 | 728.5 | 20.87 | 0.0 | 10.0 | 11.47 | 18.48 | Au1rxx-base64 | 159.223.157.129 |
| 79.4 | shadowsocks | 270.5 | 621.2 | 21.52 | 0.0 | 10.0 | 13.9 | 18.48 | Au1rxx-base64 | 23.150.248.20 |
| 79.4 | shadowsocks | 291.9 | 742.2 | 21.02 | 0.0 | 10.0 | 13.9 | 18.48 | Au1rxx-base64 | 156.146.38.169 |
| 78.34 | shadowsocks | 312.8 | 750.1 | 20.54 | 0.0 | 10.0 | 13.9 | 18.48 | Au1rxx-base64 | 37.19.198.160 |
| 77.95 | vless | 290.6 | 727.3 | 21.05 | 0.0 | 10.0 | 8.9 | 18.48 | Au1rxx-base64 | 79.141.172.154 |
| 76.91 | shadowsocks | 306.1 | 737.1 | 20.69 | 0.0 | 10.0 | 13.9 | 18.48 | Au1rxx-base64 | 37.19.198.244 |
| 76.52 | shadowsocks | 343.1 | 854.1 | 19.83 | 0.0 | 10.0 | 13.9 | 18.48 | Au1rxx-base64 | 37.19.198.236 |
| 75.53 | shadowsocks | 309.1 | 759.4 | 20.62 | 0.0 | 10.0 | 13.9 | 18.48 | Au1rxx-base64 | 37.19.198.243 |
| 75.44 | vless | 289.3 | 684.5 | 21.08 | 0.0 | 10.0 | 8.9 | 18.48 | Au1rxx-base64 | 195.211.98.43 |
| 75.36 | hysteria2 | 330.7 | 752.3 | 20.12 | 0.0 | 10.0 | 11.47 | 18.48 | Au1rxx-base64 | 66.94.121.46 |
| 74.67 | shadowsocks | 252.5 | 616.0 | 21.93 | 0.0 | 10.0 | 13.9 | 12.84 | mheidari-all | 156.146.38.168 |
| 74.45 | vless | 330.7 | 713.9 | 20.12 | 0.0 | 10.0 | 8.9 | 18.48 | Au1rxx-base64 | 138.124.60.146 |
| 74.24 | vless | 341.5 | 712.8 | 19.87 | 0.0 | 10.0 | 8.9 | 18.48 | Au1rxx-base64 | 169.40.42.35 |
| 74.13 | shadowsocks | 411.4 | 717.5 | 18.25 | 0.0 | 10.0 | 13.9 | 18.48 | Au1rxx-base64 | 15.204.246.132 |
| 74.11 | shadowsocks | 339.8 | 760.4 | 19.91 | 0.0 | 10.0 | 13.9 | 18.48 | Au1rxx-base64 | 108.181.57.93 |
| 73.72 | vless | 359.0 | 807.8 | 19.47 | 0.0 | 10.0 | 8.9 | 18.48 | Au1rxx-base64 | 169.40.42.212 |
| 73.66 | vless | 340.3 | 706.6 | 19.9 | 0.0 | 10.0 | 8.9 | 18.48 | Au1rxx-base64 | 169.40.42.52 |
| 73.53 | vless | 295.0 | 585.5 | 20.95 | 0.0 | 10.0 | 8.9 | 18.48 | Au1rxx-base64 | 70.39.196.142 |
| 73.28 | vless | 296.9 | 702.7 | 20.9 | 0.0 | 10.0 | 8.9 | 18.48 | Au1rxx-base64 | 198.251.78.29 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Surfboard-tg-mixed | 0.967 | 0.9 | 60 | 7279 | prefer |
| Au1rxx-base64 | 0.876 | 0.809 | 299 | 1718 | prefer |
| mheidari-all | 0.804 | 0.729 | 85 | 15951 | prefer |
| ermaozi | 0.787 | 0.793 | 29 | 325 | prefer |
| DeltaKronecker-all | 0.671 | 0.593 | 162 | 6324 | observe |
| tg-oneclickvpnkeys | 0.363 | 1.0 | 3 | 116 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| roosterkid-openproxylist-v2ray | 0.261 | 1.0 | 1 | 150 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4915 | observe |
| Epodonios-all | 0.255 | None | 0 | 7749 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9217 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5930 | observe |
| barry-far-vless | 0.255 | None | 0 | 5928 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4252 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 61 |
| geo | TimeoutError | - | 22 |
| geo | ClientOSError | - | 18 |
| 204 | ProxyError | - | 16 |
| cn-block | TimeoutError | - | 15 |
| 204 | TimeoutError | - | 11 |
| speed | TimeoutError | - | 7 |
| 204 | ClientOSError | - | 4 |
| cn-block | ClientOSError | - | 4 |
| cn-block | ProxyError | - | 3 |
| speed | ProxyError | - | 1 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
