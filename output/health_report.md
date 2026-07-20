# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-20 19:53:46 |
| 运行耗时 | 273.4s |
| 订阅源总数 | 107 |
| 健康订阅源 | 102 |
| 原始节点 | 85798 |
| 去重后节点 | 24302 |
| TCP 可达 | 3000 |
| 真实可用 | 415 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 24302 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.6 |
| geo | 0.9 |
| tcp | 33.9 |
| probe | 61.6 |
| real_test | 132.5 |
| generate | 38.9 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 51310 |
| trojan | 12477 |
| vmess | 11049 |
| shadowsocks | 10342 |
| hysteria2 | 412 |
| shadowsocksr | 74 |
| socks | 58 |
| http | 52 |
| hysteria | 16 |
| tuic | 7 |
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
| 79.58 | shadowsocks | 246.9 | 603.0 | 22.06 | 0.0 | 10.0 | 12.98 | 18.54 | Au1rxx-base64 | 156.146.38.167 |
| 79.3 | shadowsocks | 259.3 | 638.0 | 21.78 | 0.0 | 10.0 | 12.98 | 18.54 | Au1rxx-base64 | 156.146.38.168 |
| 79.02 | shadowsocks | 254.2 | 629.0 | 21.89 | 0.0 | 10.0 | 12.98 | 18.54 | Au1rxx-base64 | 156.146.38.170 |
| 78.57 | shadowsocks | 268.3 | 671.4 | 21.57 | 0.0 | 10.0 | 12.98 | 18.54 | Au1rxx-base64 | 37.19.198.244 |
| 78.57 | shadowsocks | 270.3 | 666.5 | 21.52 | 0.0 | 10.0 | 12.98 | 18.54 | Au1rxx-base64 | 37.19.198.236 |
| 78.56 | shadowsocks | 249.0 | 606.8 | 22.01 | 0.0 | 10.0 | 12.98 | 18.54 | Au1rxx-base64 | 156.146.38.169 |
| 78.36 | shadowsocks | 266.9 | 662.9 | 21.6 | 0.0 | 10.0 | 12.98 | 18.54 | Au1rxx-base64 | 37.19.198.243 |
| 77.94 | shadowsocks | 273.7 | 665.2 | 21.44 | 0.0 | 10.0 | 12.98 | 18.54 | Au1rxx-base64 | 37.19.198.160 |
| 77.02 | shadowsocks | 336.0 | 885.9 | 20.0 | 0.0 | 10.0 | 12.98 | 18.54 | Au1rxx-base64 | 185.196.61.82 |
| 76.3 | trojan | 405.1 | 1123.7 | 18.4 | 0.0 | 10.0 | 12.36 | 18.54 | Au1rxx-base64 | 148.72.168.35 |
| 75.55 | trojan | 284.5 | 673.1 | 21.19 | 0.0 | 10.0 | 12.36 | 18.54 | Au1rxx-base64 | 64.94.95.117 |
| 74.77 | shadowsocks | 416.1 | 1087.9 | 18.14 | 0.0 | 10.0 | 12.98 | 18.54 | Au1rxx-base64 | 108.181.57.93 |
| 73.92 | trojan | 349.5 | 874.4 | 19.69 | 0.0 | 10.0 | 12.36 | 18.54 | Au1rxx-base64 | 64.94.95.118 |
| 73.85 | trojan | 323.0 | 787.9 | 20.3 | 0.0 | 10.0 | 12.36 | 18.54 | Au1rxx-base64 | 64.94.95.115 |
| 73.73 | shadowsocks | 318.0 | 673.0 | 20.42 | 0.0 | 10.0 | 12.98 | 18.54 | Au1rxx-base64 | 149.22.95.183 |
| 73.67 | shadowsocks | 305.4 | 593.3 | 20.71 | 0.0 | 10.0 | 12.98 | 18.54 | Au1rxx-base64 | 173.244.56.9 |
| 73.45 | shadowsocks | 292.0 | 525.1 | 21.02 | 0.0 | 10.0 | 12.98 | 18.54 | Au1rxx-base64 | 108.181.0.177 |
| 73.32 | shadowsocks | 294.9 | 547.3 | 20.95 | 0.0 | 10.0 | 12.98 | 18.54 | Au1rxx-base64 | 173.244.56.6 |
| 71.64 | shadowsocks | 562.5 | 1519.1 | 14.76 | 0.0 | 10.0 | 12.98 | 18.54 | Au1rxx-base64 | 68.168.222.210 |
| 71.46 | shadowsocks | 283.8 | 659.5 | 21.21 | 0.0 | 10.0 | 12.98 | 18.54 | Au1rxx-base64 | 198.98.53.130 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.976 | 1.0 | 36 | 61 | prefer |
| Au1rxx-base64 | 0.885 | 0.86 | 228 | 719 | prefer |
| mheidari-all | 0.553 | 0.472 | 108 | 19990 | observe |
| Surfboard-tg-mixed | 0.547 | 0.466 | 193 | 5499 | observe |
| DeltaKronecker-all | 0.427 | 0.345 | 119 | 5962 | observe |
| xiaoji235-airport-v2ray-all | 0.335 | 1.0 | 1 | 5035 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4714 | observe |
| Epodonios-all | 0.255 | None | 0 | 6648 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7049 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4237 | observe |
| barry-far-vless | 0.255 | None | 0 | 4959 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5173 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 83 |
| speed | ClientOSError | - | 65 |
| cn-block | TimeoutError | - | 62 |
| 204 | TimeoutError | - | 23 |
| geo | ClientOSError | - | 9 |
| cn-block | ClientOSError | - | 9 |
| 204 | ProxyError | - | 7 |
| 204 | ClientOSError | - | 6 |
| cn-block | ProxyError | - | 3 |
| speed | TimeoutError | - | 3 |
| speed | ProxyError | - | 2 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
