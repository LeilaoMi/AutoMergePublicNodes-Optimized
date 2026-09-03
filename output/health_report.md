# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-03 20:52:32 |
| 运行耗时 | 240.8s |
| 订阅源总数 | 107 |
| 健康订阅源 | 95 |
| 原始节点 | 82446 |
| 去重后节点 | 22585 |
| TCP 可达 | 3000 |
| 真实可用 | 508 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22585 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.4 |
| geo | 1.4 |
| tcp | 37.8 |
| probe | 67.1 |
| real_test | 100.5 |
| generate | 29.5 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 50927 |
| vmess | 11836 |
| shadowsocks | 10009 |
| trojan | 7766 |
| hysteria2 | 1562 |
| http | 139 |
| shadowsocksr | 122 |
| socks | 59 |
| tuic | 15 |
| hysteria | 10 |
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
| 83.03 | hysteria2 | 251.7 | 558.2 | 21.95 | 0.0 | 10.0 | 13.75 | 20.0 | Au1rxx-base64 | 66.94.121.46 |
| 82.22 | shadowsocks | 249.7 | 616.6 | 22.0 | 0.0 | 10.0 | 14.22 | 20.0 | Au1rxx-base64 | 156.146.38.168 |
| 82.15 | shadowsocks | 252.5 | 633.7 | 21.93 | 0.0 | 10.0 | 14.22 | 20.0 | Au1rxx-base64 | 156.146.38.167 |
| 81.51 | shadowsocks | 254.7 | 628.3 | 21.88 | 0.0 | 10.0 | 14.22 | 20.0 | Au1rxx-base64 | 156.146.38.170 |
| 80.31 | shadowsocks | 267.4 | 647.0 | 21.59 | 0.0 | 10.0 | 14.22 | 20.0 | Au1rxx-base64 | 23.150.248.20 |
| 79.84 | shadowsocks | 305.4 | 726.9 | 20.71 | 0.0 | 10.0 | 14.22 | 20.0 | Au1rxx-base64 | 37.19.198.160 |
| 79.8 | vless | 278.4 | 569.2 | 21.33 | 0.0 | 10.0 | 12.5 | 20.0 | Au1rxx-base64 | 172.233.156.118 |
| 79.71 | vless | 310.6 | 693.1 | 20.59 | 0.0 | 10.0 | 12.5 | 20.0 | Au1rxx-base64 | 172.105.104.54 |
| 79.43 | vless | 322.1 | 717.7 | 20.32 | 0.0 | 10.0 | 12.5 | 20.0 | Au1rxx-base64 | 204.48.20.223 |
| 79.28 | vless | 292.0 | 597.6 | 21.02 | 0.0 | 10.0 | 12.5 | 20.0 | Au1rxx-base64 | 172.239.67.231 |
| 79.15 | vless | 339.7 | 776.3 | 19.92 | 0.0 | 10.0 | 12.5 | 20.0 | Au1rxx-base64 | 169.40.42.229 |
| 79.08 | vless | 302.7 | 563.6 | 20.77 | 0.0 | 10.0 | 12.5 | 20.0 | Au1rxx-base64 | 172.236.252.35 |
| 79.05 | vless | 308.6 | 583.6 | 20.63 | 0.0 | 10.0 | 12.5 | 20.0 | Au1rxx-base64 | 172.233.156.123 |
| 79.04 | vless | 290.0 | 582.1 | 21.06 | 0.0 | 10.0 | 12.5 | 20.0 | Au1rxx-base64 | 172.239.67.156 |
| 78.95 | vless | 292.2 | 593.9 | 21.01 | 0.0 | 10.0 | 12.5 | 20.0 | Au1rxx-base64 | 172.233.139.46 |
| 78.82 | vless | 355.8 | 711.1 | 19.54 | 0.0 | 10.0 | 12.5 | 20.0 | Au1rxx-base64 | 169.40.42.179 |
| 78.74 | vless | 304.8 | 585.9 | 20.72 | 0.0 | 10.0 | 12.5 | 20.0 | Au1rxx-base64 | 172.235.43.210 |
| 78.66 | vless | 302.6 | 632.5 | 20.77 | 0.0 | 10.0 | 12.5 | 20.0 | Au1rxx-base64 | 172.235.38.85 |
| 78.66 | vless | 307.8 | 574.9 | 20.65 | 0.0 | 10.0 | 12.5 | 20.0 | Au1rxx-base64 | 45.79.103.108 |
| 78.5 | shadowsocks | 236.4 | 602.3 | 22.3 | 0.0 | 10.0 | 14.22 | 20.0 | Au1rxx-base64 | 84.32.131.61 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.981 | 0.913 | 369 | 1748 | prefer |
| zhangkai | 0.964 | 1.0 | 22 | 144 | prefer |
| mheidari-all | 0.866 | 0.792 | 96 | 15893 | prefer |
| DeltaKronecker-all | 0.788 | 0.713 | 87 | 6335 | prefer |
| Surfboard-tg-mixed | 0.547 | 0.778 | 9 | 7177 | observe |
| tg-oneclickvpnkeys | 0.405 | 1.0 | 4 | 115 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4671 | observe |
| Epodonios-all | 0.255 | None | 0 | 7695 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 8160 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5920 | observe |
| barry-far-vless | 0.255 | None | 0 | 6131 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4133 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.245 | None | 0 | 1748 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | TimeoutError | - | 24 |
| cn-block | TimeoutError | - | 20 |
| speed | ClientOSError | - | 8 |
| geo | ClientOSError | - | 6 |
| cn-block | ClientOSError | - | 6 |
| cn-block | ProxyError | - | 4 |
| 204 | ProxyError | - | 4 |
| geo | TimeoutError | - | 3 |
| speed | TimeoutError | - | 2 |
| 204 | ServerDisconnectedError | - | 1 |
| 204 | ClientOSError | - | 1 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
