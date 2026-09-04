# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-04 20:40:46 |
| 运行耗时 | 287.2s |
| 订阅源总数 | 107 |
| 健康订阅源 | 96 |
| 原始节点 | 84229 |
| 去重后节点 | 23541 |
| TCP 可达 | 3000 |
| 真实可用 | 584 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23541 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.5 |
| geo | 1.3 |
| tcp | 38.5 |
| probe | 73.6 |
| real_test | 129.9 |
| generate | 39.4 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 53339 |
| vmess | 11497 |
| shadowsocks | 9658 |
| trojan | 7966 |
| hysteria2 | 1359 |
| http | 192 |
| shadowsocksr | 125 |
| socks | 67 |
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
| 84.95 | vless | 212.3 | 505.6 | 22.86 | 0.0 | 10.0 | 12.37 | 19.72 | Au1rxx-base64 | 172.235.38.85 |
| 84.94 | vless | 213.0 | 496.2 | 22.85 | 0.0 | 10.0 | 12.37 | 19.72 | Au1rxx-base64 | 172.233.139.46 |
| 84.01 | hysteria2 | 257.6 | 533.9 | 21.81 | 0.0 | 10.0 | 14.0 | 19.72 | Au1rxx-base64 | 66.94.121.46 |
| 82.6 | vless | 227.5 | 552.4 | 22.51 | 0.0 | 10.0 | 12.37 | 19.72 | Au1rxx-base64 | 38.127.121.44 |
| 80.49 | shadowsocks | 254.5 | 600.1 | 21.89 | 0.0 | 10.0 | 13.41 | 19.72 | Au1rxx-base64 | 156.146.38.168 |
| 80.36 | shadowsocks | 260.7 | 630.3 | 21.74 | 0.0 | 10.0 | 13.41 | 19.72 | Au1rxx-base64 | 156.146.38.169 |
| 80.28 | vless | 348.1 | 830.7 | 19.72 | 0.0 | 10.0 | 12.37 | 19.72 | Au1rxx-base64 | 15.204.97.197 |
| 80.27 | vless | 312.7 | 566.8 | 20.54 | 0.0 | 10.0 | 12.37 | 19.72 | Au1rxx-base64 | 31.58.50.200 |
| 79.72 | vless | 357.0 | 864.3 | 19.51 | 0.0 | 10.0 | 12.37 | 19.72 | Au1rxx-base64 | 15.204.97.216 |
| 79.42 | vless | 201.0 | 508.5 | 23.12 | 0.0 | 10.0 | 12.37 | 19.72 | Au1rxx-base64 | 38.150.33.232 |
| 79.1 | vless | 249.0 | 573.0 | 22.01 | 0.0 | 10.0 | 12.37 | 19.72 | Au1rxx-base64 | 38.209.125.45 |
| 79.08 | vless | 360.4 | 345.0 | 19.43 | 2.06 | 10.0 | 12.37 | 19.72 | Au1rxx-base64 | 172.64.154.8 |
| 78.79 | vless | 216.6 | 506.3 | 22.76 | 0.0 | 10.0 | 12.37 | 19.72 | Au1rxx-base64 | 162.159.24.131 |
| 78.33 | vless | 249.9 | 284.3 | 21.99 | 4.34 | 9.91 | 12.37 | 16.02 | Surfboard-tg-mixed | 31.76.91.72 |
| 77.9 | vless | 229.5 | 505.1 | 22.47 | 0.0 | 10.0 | 12.37 | 19.72 | Au1rxx-base64 | 172.64.229.2 |
| 77.62 | vless | 205.0 | 513.0 | 23.03 | 0.0 | 10.0 | 12.37 | 19.72 | Au1rxx-base64 | 192.220.11.234 |
| 77.34 | shadowsocks | 266.7 | 643.3 | 21.6 | 0.0 | 10.0 | 13.41 | 16.96 | mheidari-all | 156.146.38.170 |
| 77.34 | shadowsocks | 271.7 | 576.4 | 21.49 | 0.0 | 10.0 | 13.41 | 19.72 | Au1rxx-base64 | 149.22.95.183 |
| 77.33 | vless | 246.3 | 541.7 | 22.08 | 0.0 | 10.0 | 12.37 | 19.72 | Au1rxx-base64 | 5.78.48.21 |
| 77.27 | shadowsocks | 256.7 | 606.6 | 21.84 | 0.0 | 10.0 | 13.41 | 16.02 | Surfboard-tg-mixed | 156.146.38.167 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.962 | 1.0 | 21 | 144 | prefer |
| Au1rxx-base64 | 0.915 | 0.847 | 346 | 1756 | prefer |
| mheidari-all | 0.882 | 0.806 | 124 | 16096 | prefer |
| DeltaKronecker-all | 0.81 | 0.743 | 35 | 7089 | prefer |
| Surfboard-tg-mixed | 0.81 | 0.732 | 183 | 7342 | prefer |
| tg-oneclickvpnkeys | 0.589 | 1.0 | 9 | 118 | observe |
| tg-OutlineReleasedKey | 0.257 | 1.0 | 1 | 52 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4810 | observe |
| Epodonios-all | 0.255 | None | 0 | 7798 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 8118 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 6159 | observe |
| barry-far-vless | 0.255 | None | 0 | 6376 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4095 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| cn-block | TimeoutError | - | 26 |
| 204 | TimeoutError | - | 25 |
| geo | ClientOSError | - | 23 |
| cn-block | ClientOSError | - | 18 |
| speed | ClientOSError | - | 13 |
| geo | TimeoutError | - | 9 |
| 204 | ProxyError | - | 7 |
| speed | TimeoutError | - | 7 |
| cn-block | ProxyError | - | 3 |
| 204 | ClientOSError | - | 3 |
| geo | ProxyError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
