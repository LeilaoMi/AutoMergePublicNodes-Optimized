# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-02 20:55:43 |
| 运行耗时 | 274.8s |
| 订阅源总数 | 107 |
| 健康订阅源 | 95 |
| 原始节点 | 82593 |
| 去重后节点 | 23713 |
| TCP 可达 | 3000 |
| 真实可用 | 483 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23713 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.9 |
| geo | 1.4 |
| tcp | 37.6 |
| probe | 81.9 |
| real_test | 97.7 |
| generate | 49.3 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 51944 |
| vmess | 11157 |
| shadowsocks | 9828 |
| trojan | 7776 |
| hysteria2 | 1514 |
| http | 144 |
| shadowsocksr | 128 |
| socks | 84 |
| tuic | 11 |
| hysteria | 7 |

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
| 85.04 | hysteria2 | 203.4 | 562.8 | 23.07 | 0.0 | 10.0 | 13.75 | 19.22 | Au1rxx-base64 | 66.94.121.46 |
| 83.72 | vless | 244.2 | 553.4 | 22.13 | 0.0 | 10.0 | 12.53 | 19.22 | Au1rxx-base64 | 74.207.245.124 |
| 83.63 | vless | 249.2 | 569.0 | 22.01 | 0.0 | 10.0 | 12.53 | 19.22 | Au1rxx-base64 | 45.33.62.166 |
| 83.61 | vless | 255.5 | 575.6 | 21.86 | 0.0 | 10.0 | 12.53 | 19.22 | Au1rxx-base64 | 45.79.103.108 |
| 83.01 | vless | 256.1 | 572.6 | 21.85 | 0.0 | 10.0 | 12.53 | 19.22 | Au1rxx-base64 | 50.116.9.184 |
| 81.79 | shadowsocks | 191.6 | 515.3 | 23.34 | 0.0 | 10.0 | 13.23 | 19.22 | Au1rxx-base64 | 149.22.95.183 |
| 81.41 | vless | 268.0 | 591.5 | 21.58 | 0.0 | 10.0 | 12.53 | 19.22 | Au1rxx-base64 | 172.236.252.35 |
| 81.33 | vless | 275.1 | 602.9 | 21.41 | 0.0 | 10.0 | 12.53 | 19.22 | Au1rxx-base64 | 172.235.43.210 |
| 80.45 | vless | 284.8 | 643.6 | 21.18 | 0.0 | 10.0 | 12.53 | 19.22 | Au1rxx-base64 | 172.235.38.85 |
| 80.06 | vless | 276.6 | 627.4 | 21.38 | 0.0 | 10.0 | 12.53 | 19.22 | Au1rxx-base64 | 172.233.156.123 |
| 79.41 | vless | 242.9 | 469.9 | 22.16 | 0.0 | 10.0 | 12.53 | 19.22 | Au1rxx-base64 | 162.159.0.53 |
| 79.36 | vless | 237.4 | 539.8 | 22.28 | 0.0 | 10.0 | 12.53 | 19.22 | Au1rxx-base64 | 192.155.87.188 |
| 79.1 | vless | 280.6 | 602.9 | 21.28 | 0.0 | 10.0 | 12.53 | 19.22 | Au1rxx-base64 | 172.239.67.156 |
| 78.86 | vless | 357.4 | 716.9 | 19.51 | 0.0 | 10.0 | 12.53 | 19.22 | Au1rxx-base64 | 172.233.156.118 |
| 78.15 | vless | 265.3 | 587.7 | 21.64 | 0.0 | 10.0 | 12.53 | 19.22 | Au1rxx-base64 | 172.239.67.231 |
| 78.12 | vless | 261.3 | 574.7 | 21.73 | 0.0 | 10.0 | 12.53 | 19.22 | Au1rxx-base64 | 172.233.139.46 |
| 77.74 | http | 280.5 | 610.8 | 21.28 | 0.0 | 10.0 | 13.85 | 18.52 | zhangkai | 138.199.35.216 |
| 77.4 | vless | 315.5 | 331.1 | 20.47 | 2.58 | 10.0 | 12.53 | 19.22 | Au1rxx-base64 | 57.180.65.248 |
| 77.32 | vless | 318.6 | 332.0 | 20.4 | 2.55 | 10.0 | 12.53 | 19.22 | Au1rxx-base64 | 13.230.140.251 |
| 77.31 | vless | 320.3 | 333.8 | 20.36 | 2.48 | 10.0 | 12.53 | 19.22 | Au1rxx-base64 | 18.183.215.124 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.983 | 0.913 | 346 | 1798 | prefer |
| mheidari-all | 0.851 | 0.777 | 103 | 15504 | prefer |
| zhangkai | 0.766 | 0.783 | 23 | 144 | prefer |
| DeltaKronecker-all | 0.743 | 0.667 | 90 | 7295 | prefer |
| Surfboard-tg-mixed | 0.606 | 0.889 | 9 | 7091 | observe |
| tg-oneclickvpnkeys | 0.26 | 1.0 | 1 | 131 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4765 | observe |
| Epodonios-all | 0.255 | None | 0 | 7530 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3996 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7745 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 6013 | observe |
| barry-far-vless | 0.255 | None | 0 | 6223 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4066 | observe |
| Au1rxx-clash | 0.247 | None | 0 | 1798 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | TimeoutError | - | 17 |
| cn-block | TimeoutError | - | 17 |
| geo | ClientOSError | - | 14 |
| cn-block | ClientOSError | - | 11 |
| speed | ClientOSError | - | 8 |
| 204 | ProxyError | - | 7 |
| 204 | ProxyConnectionError | - | 6 |
| 204 | ClientOSError | - | 4 |
| cn-block | ProxyError | - | 4 |
| geo | ProxyError | - | 2 |
| geo | TimeoutError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
