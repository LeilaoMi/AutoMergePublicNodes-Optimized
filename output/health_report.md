# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-30 16:30:50 |
| 运行耗时 | 271.3s |
| 订阅源总数 | 107 |
| 健康订阅源 | 95 |
| 原始节点 | 79914 |
| 去重后节点 | 21856 |
| TCP 可达 | 3000 |
| 真实可用 | 582 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 21856 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.4 |
| geo | 1.6 |
| tcp | 35.2 |
| probe | 58.2 |
| real_test | 137.9 |
| generate | 34.1 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 50292 |
| vmess | 10877 |
| shadowsocks | 10241 |
| trojan | 6614 |
| hysteria2 | 1511 |
| http | 170 |
| shadowsocksr | 123 |
| socks | 70 |
| tuic | 8 |
| hysteria | 7 |
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
| 83.85 | hysteria2 | 179.8 | 486.0 | 23.62 | 0.0 | 10.0 | 14.29 | 19.94 | Au1rxx-base64 | 66.94.121.46 |
| 83.58 | vless | 244.0 | 550.5 | 22.13 | 0.0 | 10.0 | 12.05 | 19.94 | Au1rxx-base64 | 192.155.87.188 |
| 83.46 | vless | 248.1 | 542.5 | 22.03 | 0.0 | 10.0 | 12.05 | 19.94 | Au1rxx-base64 | 173.255.242.56 |
| 83.37 | vless | 276.4 | 753.7 | 21.38 | 0.0 | 10.0 | 12.05 | 19.94 | Au1rxx-base64 | 15.204.97.197 |
| 83.3 | vless | 232.5 | 536.1 | 22.4 | 0.0 | 10.0 | 12.05 | 19.94 | Au1rxx-base64 | 45.33.62.226 |
| 83.25 | vless | 281.8 | 773.2 | 21.26 | 0.0 | 10.0 | 12.05 | 19.94 | Au1rxx-base64 | 15.204.97.209 |
| 83.23 | vless | 282.2 | 776.3 | 21.24 | 0.0 | 10.0 | 12.05 | 19.94 | Au1rxx-base64 | 15.204.97.216 |
| 83.18 | shadowsocks | 183.3 | 487.0 | 23.54 | 0.0 | 10.0 | 13.7 | 19.94 | Au1rxx-base64 | 149.22.95.183 |
| 83.11 | vless | 236.1 | 546.4 | 22.31 | 0.0 | 10.0 | 12.05 | 19.94 | Au1rxx-base64 | 50.116.13.24 |
| 83.01 | vless | 268.5 | 642.8 | 21.56 | 0.0 | 10.0 | 12.05 | 19.94 | Au1rxx-base64 | 64.23.229.123 |
| 82.97 | vless | 247.8 | 577.4 | 22.04 | 0.0 | 10.0 | 12.05 | 19.94 | Au1rxx-base64 | 50.116.9.184 |
| 82.83 | vless | 236.8 | 547.7 | 22.3 | 0.0 | 10.0 | 12.05 | 19.94 | Au1rxx-base64 | 192.81.131.225 |
| 82.83 | vless | 239.5 | 547.5 | 22.23 | 0.0 | 10.0 | 12.05 | 19.94 | Au1rxx-base64 | 45.79.103.108 |
| 82.81 | vless | 235.2 | 529.2 | 22.33 | 0.0 | 10.0 | 12.05 | 19.94 | Au1rxx-base64 | 45.33.107.237 |
| 82.56 | vless | 228.4 | 520.5 | 22.49 | 0.0 | 10.0 | 12.05 | 19.94 | Au1rxx-base64 | 45.33.62.166 |
| 82.12 | vless | 330.3 | 914.6 | 20.13 | 0.0 | 10.0 | 12.05 | 19.94 | Au1rxx-base64 | 15.204.97.206 |
| 82.02 | vless | 334.5 | 927.8 | 20.03 | 0.0 | 10.0 | 12.05 | 19.94 | Au1rxx-base64 | 15.204.97.195 |
| 81.71 | vless | 256.9 | 542.7 | 21.83 | 0.0 | 10.0 | 12.05 | 19.94 | Au1rxx-base64 | 31.58.50.200 |
| 81.42 | vless | 260.3 | 576.2 | 21.75 | 0.0 | 10.0 | 12.05 | 19.94 | Au1rxx-base64 | 172.233.156.118 |
| 81.42 | vless | 265.8 | 600.0 | 21.63 | 0.0 | 10.0 | 12.05 | 19.94 | Au1rxx-base64 | 172.239.67.231 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.967 | 0.897 | 341 | 1804 | prefer |
| zhangkai | 0.966 | 1.0 | 23 | 144 | prefer |
| Surfboard-tg-mixed | 0.862 | 0.785 | 163 | 7004 | prefer |
| DeltaKronecker-all | 0.842 | 0.765 | 149 | 5576 | prefer |
| mheidari-all | 0.679 | 0.909 | 11 | 15115 | observe |
| tg-LonUp_M | 0.262 | 1.0 | 1 | 163 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4762 | observe |
| Epodonios-all | 0.255 | None | 0 | 7409 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7601 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5872 | observe |
| barry-far-vless | 0.255 | None | 0 | 6056 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 3949 | observe |
| Au1rxx-clash | 0.247 | None | 0 | 1804 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | TimeoutError | - | 27 |
| geo | TimeoutError | - | 19 |
| geo | ClientOSError | - | 14 |
| cn-block | TimeoutError | - | 12 |
| speed | TimeoutError | - | 11 |
| 204 | ProxyError | - | 9 |
| speed | ClientOSError | - | 7 |
| cn-block | ClientOSError | - | 3 |
| 204 | ClientOSError | - | 2 |
| geo | ProxyError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
