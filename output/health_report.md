# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-17 16:50:30 |
| 运行耗时 | 680.2s |
| 订阅源总数 | 107 |
| 健康订阅源 | 96 |
| 原始节点 | 86881 |
| 去重后节点 | 24278 |
| TCP 可达 | 3000 |
| 真实可用 | 445 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 24278 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.8 |
| geo | 1.4 |
| tcp | 41.4 |
| probe | 283.0 |
| real_test | 268.3 |
| generate | 79.2 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 51574 |
| vmess | 13922 |
| shadowsocks | 10638 |
| trojan | 8555 |
| hysteria2 | 1435 |
| http | 545 |
| shadowsocksr | 126 |
| socks | 74 |
| hysteria | 8 |
| tuic | 2 |
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
| 78.3 | vless | 286.5 | 754.8 | 21.15 | 0.0 | 10.0 | 9.51 | 17.64 | Au1rxx-base64 | 167.17.69.171 |
| 77.98 | vless | 300.0 | 819.4 | 20.83 | 0.0 | 10.0 | 9.51 | 17.64 | Au1rxx-base64 | 137.184.218.169 |
| 77.83 | hysteria2 | 234.8 | 652.2 | 22.34 | 0.0 | 10.0 | 11.47 | 15.12 | mheidari-all | 159.223.157.129 |
| 77.65 | vless | 314.3 | 717.9 | 20.5 | 0.0 | 10.0 | 9.51 | 17.64 | Au1rxx-base64 | 169.40.42.173 |
| 77.18 | vless | 334.5 | 844.9 | 20.03 | 0.0 | 10.0 | 9.51 | 17.64 | Au1rxx-base64 | 169.40.42.224 |
| 76.59 | vless | 360.0 | 856.3 | 19.44 | 0.0 | 10.0 | 9.51 | 17.64 | Au1rxx-base64 | 169.40.42.225 |
| 76.52 | vless | 363.4 | 863.3 | 19.37 | 0.0 | 10.0 | 9.51 | 17.64 | Au1rxx-base64 | 169.40.42.163 |
| 76.45 | vless | 366.5 | 990.4 | 19.3 | 0.0 | 10.0 | 9.51 | 17.64 | Au1rxx-base64 | 169.40.42.229 |
| 76.43 | vless | 367.1 | 1027.3 | 19.28 | 0.0 | 10.0 | 9.51 | 17.64 | Au1rxx-base64 | 185.95.231.156 |
| 76.4 | vless | 311.6 | 688.7 | 20.56 | 0.0 | 10.0 | 9.51 | 17.64 | Au1rxx-base64 | 169.40.42.35 |
| 76.36 | shadowsocks | 231.3 | 637.0 | 22.42 | 0.0 | 10.0 | 12.82 | 15.12 | mheidari-all | 37.19.198.236 |
| 76.33 | vless | 371.3 | 947.3 | 19.18 | 0.0 | 10.0 | 9.51 | 17.64 | Au1rxx-base64 | 169.40.42.231 |
| 76.28 | vless | 244.1 | 685.0 | 22.13 | 0.0 | 10.0 | 9.51 | 17.64 | Au1rxx-base64 | 47.253.226.114 |
| 76.23 | shadowsocks | 324.2 | 931.3 | 20.27 | 0.0 | 10.0 | 12.82 | 17.64 | Au1rxx-base64 | 15.204.247.206 |
| 76.21 | vless | 346.9 | 933.4 | 19.75 | 0.0 | 10.0 | 9.51 | 17.64 | Au1rxx-base64 | 169.40.42.89 |
| 76.21 | vless | 375.3 | 952.4 | 19.09 | 0.0 | 10.0 | 9.51 | 17.64 | Au1rxx-base64 | 216.152.147.28 |
| 76.19 | shadowsocks | 238.7 | 660.7 | 22.25 | 0.0 | 10.0 | 12.82 | 15.12 | mheidari-all | 37.19.198.243 |
| 75.55 | vless | 296.0 | 652.4 | 20.93 | 0.0 | 10.0 | 9.51 | 17.64 | Au1rxx-base64 | 169.40.42.182 |
| 75.15 | shadowsocks | 327.7 | 854.1 | 20.19 | 0.0 | 10.0 | 12.82 | 17.64 | Au1rxx-base64 | 38.180.135.156 |
| 74.95 | vless | 376.3 | 969.3 | 19.07 | 0.0 | 10.0 | 9.51 | 17.64 | Au1rxx-base64 | 169.40.42.212 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.928 | 0.866 | 254 | 1619 | prefer |
| ermaozi | 0.733 | 0.733 | 30 | 357 | prefer |
| DeltaKronecker-all | 0.72 | 0.643 | 112 | 5931 | prefer |
| mheidari-all | 0.705 | 0.628 | 78 | 16008 | prefer |
| Surfboard-tg-mixed | 0.698 | 0.62 | 129 | 7430 | observe |
| tg-oneclickvpnkeys | 0.26 | 1.0 | 1 | 119 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5093 | observe |
| Epodonios-all | 0.255 | None | 0 | 7888 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9066 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5904 | observe |
| barry-far-vless | 0.255 | None | 0 | 6129 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4179 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 2484 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | ProxyError | - | 32 |
| geo | ClientOSError | - | 32 |
| geo | TimeoutError | - | 25 |
| 204 | TimeoutError | - | 21 |
| cn-block | TimeoutError | - | 18 |
| speed | ClientOSError | - | 17 |
| speed | TimeoutError | - | 10 |
| cn-block | ClientOSError | - | 10 |
| cn-block | ProxyError | - | 3 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
