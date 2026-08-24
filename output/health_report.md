# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-24 18:52:17 |
| 运行耗时 | 257.3s |
| 订阅源总数 | 107 |
| 健康订阅源 | 97 |
| 原始节点 | 84125 |
| 去重后节点 | 23818 |
| TCP 可达 | 3000 |
| 真实可用 | 494 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23818 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.6 |
| geo | 1.4 |
| tcp | 38.3 |
| probe | 56.8 |
| real_test | 107.5 |
| generate | 46.7 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 53013 |
| shadowsocks | 10666 |
| vmess | 10397 |
| trojan | 8172 |
| hysteria2 | 1489 |
| http | 164 |
| shadowsocksr | 128 |
| socks | 76 |
| hysteria | 13 |
| tuic | 5 |
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
| 81.57 | vless | 262.5 | 685.6 | 21.7 | 0.0 | 10.0 | 11.13 | 18.74 | Au1rxx-base64 | 79.127.243.217 |
| 81.55 | vless | 263.3 | 690.2 | 21.68 | 0.0 | 10.0 | 11.13 | 18.74 | Au1rxx-base64 | 137.184.218.169 |
| 81.25 | vless | 276.4 | 730.2 | 21.38 | 0.0 | 10.0 | 11.13 | 18.74 | Au1rxx-base64 | 185.95.231.156 |
| 80.97 | vless | 288.7 | 744.3 | 21.1 | 0.0 | 10.0 | 11.13 | 18.74 | Au1rxx-base64 | 167.17.69.171 |
| 80.79 | hysteria2 | 311.0 | 853.6 | 20.58 | 0.0 | 10.0 | 13.75 | 17.56 | mheidari-all | 159.223.157.129 |
| 80.37 | shadowsocks | 255.0 | 648.4 | 21.87 | 0.0 | 10.0 | 13.76 | 18.74 | Au1rxx-base64 | 155.138.136.240 |
| 79.92 | vless | 286.4 | 785.3 | 21.15 | 0.0 | 10.0 | 11.13 | 18.74 | Au1rxx-base64 | 45.138.100.226 |
| 79.35 | vless | 292.3 | 702.0 | 21.01 | 0.0 | 10.0 | 11.13 | 18.74 | Au1rxx-base64 | 66.70.179.198 |
| 79.03 | vless | 275.8 | 634.0 | 21.39 | 0.0 | 10.0 | 11.13 | 17.56 | mheidari-all | 195.211.99.45 |
| 78.79 | vless | 311.6 | 747.2 | 20.56 | 0.0 | 10.0 | 11.13 | 18.74 | Au1rxx-base64 | 158.69.112.254 |
| 78.32 | vless | 313.5 | 664.4 | 20.52 | 0.0 | 10.0 | 11.13 | 18.74 | Au1rxx-base64 | 198.251.78.29 |
| 77.86 | vless | 299.2 | 689.0 | 20.85 | 0.0 | 10.0 | 11.13 | 18.74 | Au1rxx-base64 | 130.107.73.148 |
| 77.85 | shadowsocks | 313.0 | 847.8 | 20.53 | 0.0 | 10.0 | 13.76 | 17.56 | mheidari-all | 37.19.198.244 |
| 77.79 | shadowsocks | 315.5 | 850.5 | 20.47 | 0.0 | 10.0 | 13.76 | 17.56 | mheidari-all | 37.19.198.243 |
| 77.68 | shadowsocks | 350.0 | 982.5 | 19.68 | 0.0 | 10.0 | 13.76 | 18.74 | Au1rxx-base64 | 15.204.246.132 |
| 77.33 | shadowsocks | 278.6 | 699.4 | 21.33 | 0.0 | 10.0 | 13.76 | 18.74 | Au1rxx-base64 | 140.238.153.81 |
| 76.85 | shadowsocks | 385.6 | 1096.2 | 18.85 | 0.0 | 10.0 | 13.76 | 18.74 | Au1rxx-base64 | 15.204.247.175 |
| 76.58 | trojan | 324.5 | 855.2 | 20.27 | 0.0 | 10.0 | 13.39 | 17.42 | DeltaKronecker-all | 45.56.108.97 |
| 76.46 | vless | 398.5 | 992.9 | 18.55 | 0.0 | 10.0 | 11.13 | 18.74 | Au1rxx-base64 | 216.152.147.28 |
| 76.1 | shadowsocks | 313.5 | 863.4 | 20.52 | 0.0 | 10.0 | 13.76 | 15.82 | Surfboard-tg-mixed | 37.19.198.236 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.953 | 0.884 | 354 | 1779 | prefer |
| zhangkai | 0.929 | 0.958 | 24 | 144 | prefer |
| mheidari-all | 0.677 | 0.598 | 224 | 19577 | observe |
| DeltaKronecker-all | 0.58 | 0.5 | 32 | 5914 | observe |
| Surfboard-tg-mixed | 0.568 | 0.875 | 8 | 6457 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4899 | observe |
| Epodonios-all | 0.255 | None | 0 | 6977 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3987 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7298 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5373 | observe |
| barry-far-vless | 0.255 | None | 0 | 5662 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4132 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.246 | None | 0 | 1780 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | ClientOSError | - | 41 |
| cn-block | TimeoutError | - | 24 |
| 204 | TimeoutError | - | 21 |
| speed | ClientOSError | - | 16 |
| geo | TimeoutError | - | 15 |
| speed | TimeoutError | - | 10 |
| 204 | ClientOSError | - | 8 |
| cn-block | ClientOSError | - | 6 |
| cn-block | ProxyError | - | 4 |
| 204 | ProxyError | - | 3 |
| speed | ClientPayloadError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
