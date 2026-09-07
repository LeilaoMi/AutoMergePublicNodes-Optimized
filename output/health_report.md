# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-07 12:10:30 |
| 运行耗时 | 284.9s |
| 订阅源总数 | 107 |
| 健康订阅源 | 96 |
| 原始节点 | 94664 |
| 去重后节点 | 24930 |
| TCP 可达 | 3000 |
| 真实可用 | 492 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 24930 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.8 |
| geo | 1.4 |
| tcp | 40.8 |
| probe | 90.7 |
| real_test | 101.3 |
| generate | 43.8 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 59131 |
| vmess | 12762 |
| shadowsocks | 11079 |
| trojan | 9214 |
| hysteria2 | 2094 |
| http | 138 |
| shadowsocksr | 130 |
| socks | 61 |
| anytls | 22 |
| hysteria | 19 |
| tuic | 14 |

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
| 82.28 | shadowsocks | 228.2 | 628.4 | 22.5 | 0.0 | 10.0 | 13.94 | 19.84 | Au1rxx-base64 | 37.19.198.244 |
| 80.27 | hysteria2 | 288.9 | 578.8 | 21.09 | 0.0 | 10.0 | 14.4 | 19.84 | Au1rxx-base64 | 66.94.121.46 |
| 79.36 | vless | 247.7 | 652.3 | 22.04 | 0.0 | 10.0 | 7.48 | 19.84 | Au1rxx-base64 | 169.40.42.232 |
| 78.79 | vless | 272.4 | 656.0 | 21.47 | 0.0 | 10.0 | 7.48 | 19.84 | Au1rxx-base64 | 169.40.42.184 |
| 78.03 | vless | 305.1 | 807.6 | 20.71 | 0.0 | 10.0 | 7.48 | 19.84 | Au1rxx-base64 | 169.40.42.104 |
| 77.99 | vless | 306.9 | 786.0 | 20.67 | 0.0 | 10.0 | 7.48 | 19.84 | Au1rxx-base64 | 66.70.179.198 |
| 77.96 | vless | 308.3 | 697.7 | 20.64 | 0.0 | 10.0 | 7.48 | 19.84 | Au1rxx-base64 | 169.40.42.74 |
| 77.59 | shadowsocks | 249.3 | 669.0 | 22.01 | 0.0 | 10.0 | 13.94 | 15.64 | Surfboard-tg-mixed | 198.98.53.130 |
| 77.28 | vless | 337.5 | 798.1 | 19.96 | 0.0 | 10.0 | 7.48 | 19.84 | Au1rxx-base64 | 169.40.42.133 |
| 77.25 | vless | 339.0 | 923.0 | 19.93 | 0.0 | 10.0 | 7.48 | 19.84 | Au1rxx-base64 | 169.40.42.229 |
| 77.15 | vless | 343.3 | 791.5 | 19.83 | 0.0 | 10.0 | 7.48 | 19.84 | Au1rxx-base64 | 169.40.42.231 |
| 77.09 | vless | 264.6 | 700.4 | 21.65 | 0.0 | 10.0 | 7.48 | 19.84 | Au1rxx-base64 | 169.40.42.35 |
| 77.06 | vless | 347.2 | 966.7 | 19.74 | 0.0 | 10.0 | 7.48 | 19.84 | Au1rxx-base64 | 185.95.231.156 |
| 77.06 | shadowsocks | 431.9 | 1180.5 | 17.78 | 0.0 | 10.0 | 13.94 | 19.84 | Au1rxx-base64 | 51.79.64.198 |
| 76.93 | shadowsocks | 243.0 | 673.8 | 22.15 | 0.0 | 10.0 | 13.94 | 19.84 | Au1rxx-base64 | 37.19.198.243 |
| 76.93 | vless | 247.5 | 639.1 | 22.05 | 0.0 | 10.0 | 7.48 | 19.84 | Au1rxx-base64 | 169.40.42.182 |
| 76.82 | vless | 357.7 | 926.2 | 19.5 | 0.0 | 10.0 | 7.48 | 19.84 | Au1rxx-base64 | 169.40.42.212 |
| 76.75 | vless | 360.4 | 920.2 | 19.43 | 0.0 | 10.0 | 7.48 | 19.84 | Au1rxx-base64 | 169.40.42.89 |
| 76.49 | vless | 371.7 | 1011.6 | 19.17 | 0.0 | 10.0 | 7.48 | 19.84 | Au1rxx-base64 | 169.40.42.95 |
| 76.2 | vless | 288.3 | 745.7 | 21.1 | 0.0 | 10.0 | 7.48 | 19.84 | Au1rxx-base64 | 169.40.42.163 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.976 | 0.907 | 322 | 1781 | prefer |
| zhangkai | 0.919 | 0.952 | 21 | 144 | prefer |
| Surfboard-tg-mixed | 0.839 | 0.762 | 143 | 7247 | prefer |
| mheidari-all | 0.58 | 0.5 | 134 | 21631 | observe |
| DeltaKronecker-all | 0.335 | 1.0 | 1 | 6417 | observe |
| xiaoji235-airport-v2ray-all | 0.287 | 0.5 | 2 | 5750 | observe |
| tg-oneclickvpnkeys | 0.275 | 0.667 | 3 | 151 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4650 | observe |
| Epodonios-all | 0.255 | None | 0 | 7707 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 8442 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 6030 | observe |
| barry-far-vless | 0.255 | None | 0 | 6245 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4138 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | ClientOSError | - | 38 |
| cn-block | ClientOSError | - | 34 |
| 204 | TimeoutError | - | 16 |
| cn-block | TimeoutError | - | 11 |
| 204 | ClientOSError | - | 7 |
| 204 | ProxyError | - | 6 |
| speed | ClientOSError | - | 6 |
| speed | TimeoutError | - | 6 |
| geo | TimeoutError | - | 4 |
| cn-block | ProxyError | - | 3 |
| 204 | ProxyConnectionError | - | 2 |
| speed | ProxyError | - | 1 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
