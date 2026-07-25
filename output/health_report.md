# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-25 03:22:06 |
| 运行耗时 | 319.1s |
| 订阅源总数 | 107 |
| 健康订阅源 | 102 |
| 原始节点 | 80289 |
| 去重后节点 | 22838 |
| TCP 可达 | 3000 |
| 真实可用 | 826 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22838 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.5 |
| geo | 1.3 |
| tcp | 32.2 |
| probe | 61.5 |
| real_test | 189.9 |
| generate | 29.7 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 45418 |
| trojan | 14276 |
| vmess | 10176 |
| shadowsocks | 9843 |
| hysteria2 | 345 |
| socks | 87 |
| shadowsocksr | 73 |
| http | 50 |
| hysteria | 15 |
| tuic | 5 |
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
| 77.71 | trojan | 262.2 | 689.9 | 21.71 | 0.0 | 10.0 | 12.82 | 16.18 | mheidari-all | 153.75.250.171 |
| 76.5 | shadowsocks | 237.8 | 638.3 | 22.27 | 0.0 | 10.0 | 11.53 | 16.7 | Au1rxx-base64 | 37.19.198.243 |
| 76.46 | shadowsocks | 239.6 | 644.9 | 22.23 | 0.0 | 10.0 | 11.53 | 16.7 | Au1rxx-base64 | 37.19.198.160 |
| 76.45 | shadowsocks | 240.2 | 643.5 | 22.22 | 0.0 | 10.0 | 11.53 | 16.7 | Au1rxx-base64 | 37.19.198.244 |
| 76.2 | shadowsocks | 250.9 | 679.0 | 21.97 | 0.0 | 10.0 | 11.53 | 16.7 | Au1rxx-base64 | 37.19.198.236 |
| 75.94 | vless | 246.5 | 644.4 | 22.07 | 0.0 | 10.0 | 6.79 | 17.08 | Surfboard-tg-mixed | 47.89.186.170 |
| 72.84 | vmess | 324.6 | 926.2 | 20.26 | 0.0 | 10.0 | 10.0 | 17.08 | Surfboard-tg-mixed | 67.220.95.3 |
| 72.53 | hysteria2 | 347.0 | 687.5 | 19.75 | 0.0 | 10.0 | 12.5 | 16.7 | Au1rxx-base64 | 62.210.124.146 |
| 72.3 | trojan | 308.6 | 641.1 | 20.63 | 0.0 | 10.0 | 12.82 | 16.18 | mheidari-all | 163.245.196.68 |
| 70.46 | hysteria2 | 431.3 | 904.7 | 17.8 | 0.0 | 10.0 | 12.5 | 16.7 | Au1rxx-base64 | 5.255.102.165 |
| 70.45 | trojan | 508.3 | 1311.7 | 16.01 | 0.0 | 10.0 | 12.82 | 16.7 | Au1rxx-base64 | 148.72.168.35 |
| 70.25 | shadowsocks | 325.2 | 696.1 | 20.25 | 0.0 | 10.0 | 11.53 | 16.7 | Au1rxx-base64 | 108.181.57.93 |
| 69.37 | trojan | 451.2 | 788.6 | 17.33 | 0.0 | 10.0 | 12.82 | 17.08 | Surfboard-tg-mixed | 198.62.62.23 |
| 69.21 | shadowsocks | 410.8 | 997.1 | 18.27 | 0.0 | 10.0 | 11.53 | 16.7 | Au1rxx-base64 | 156.146.38.170 |
| 68.64 | trojan | 441.2 | 779.0 | 17.56 | 0.0 | 10.0 | 12.82 | 16.18 | mheidari-all | 216.24.57.7 |
| 68.63 | trojan | 440.8 | 777.8 | 17.57 | 0.0 | 10.0 | 12.82 | 16.18 | mheidari-all | 8.6.112.6 |
| 68.59 | trojan | 441.5 | 782.3 | 17.56 | 0.0 | 10.0 | 12.82 | 16.18 | mheidari-all | 104.16.174.71 |
| 68.51 | trojan | 470.5 | 1146.7 | 16.89 | 0.0 | 10.0 | 12.82 | 16.7 | Au1rxx-base64 | 64.94.95.115 |
| 68.47 | trojan | 447.2 | 770.8 | 17.43 | 0.0 | 10.0 | 12.82 | 16.18 | mheidari-all | 104.19.64.105 |
| 68.31 | trojan | 443.1 | 769.8 | 17.52 | 0.0 | 10.0 | 12.82 | 17.08 | Surfboard-tg-mixed | 104.16.174.44 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.95 | 0.972 | 36 | 61 | prefer |
| Au1rxx-base64 | 0.924 | 0.913 | 138 | 432 | prefer |
| Surfboard-tg-mixed | 0.729 | 0.65 | 320 | 5472 | prefer |
| mheidari-all | 0.664 | 0.584 | 734 | 19397 | observe |
| DeltaKronecker-all | 0.406 | 0.321 | 84 | 5559 | observe |
| tg-ConfigV2rayNG | 0.263 | 1.0 | 1 | 200 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4588 | observe |
| Epodonios-all | 0.255 | None | 0 | 6656 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3970 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6389 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4180 | observe |
| barry-far-vless | 0.255 | None | 0 | 4847 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5027 | observe |
| nscl5-all | 0.255 | None | 0 | 2974 | observe |
| xiaoji235-airport-v2ray-all | 0.24 | None | 0 | 1624 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 167 |
| speed | ClientOSError | - | 145 |
| speed | TimeoutError | - | 59 |
| geo | ClientOSError | - | 54 |
| cn-block | TimeoutError | - | 41 |
| cn-block | ClientOSError | - | 9 |
| 204 | ProxyError | - | 6 |
| 204 | ClientOSError | - | 4 |
| 204 | TimeoutError | - | 4 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
