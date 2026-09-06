# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-06 20:19:43 |
| 运行耗时 | 306.7s |
| 订阅源总数 | 107 |
| 健康订阅源 | 96 |
| 原始节点 | 94324 |
| 去重后节点 | 24687 |
| TCP 可达 | 3000 |
| 真实可用 | 515 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 24687 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.9 |
| geo | 1.4 |
| tcp | 41.3 |
| probe | 92.5 |
| real_test | 124.7 |
| generate | 39.9 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 58830 |
| vmess | 12738 |
| shadowsocks | 11244 |
| trojan | 9054 |
| hysteria2 | 2061 |
| http | 139 |
| shadowsocksr | 130 |
| socks | 63 |
| anytls | 30 |
| hysteria | 19 |
| tuic | 16 |

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
| 80.63 | shadowsocks | 227.1 | 621.8 | 22.52 | 0.0 | 8.96 | 13.67 | 19.48 | Au1rxx-base64 | 37.19.198.236 |
| 80.11 | vless | 265.1 | 637.1 | 21.64 | 0.0 | 8.87 | 10.12 | 19.48 | Au1rxx-base64 | 169.40.42.179 |
| 79.98 | vless | 263.5 | 691.9 | 21.68 | 0.0 | 8.7 | 10.12 | 19.48 | Au1rxx-base64 | 167.17.69.171 |
| 79.82 | vless | 270.1 | 701.3 | 21.53 | 0.0 | 8.69 | 10.12 | 19.48 | Au1rxx-base64 | 169.40.42.182 |
| 79.28 | vless | 293.0 | 651.3 | 21.0 | 0.0 | 8.68 | 10.12 | 19.48 | Au1rxx-base64 | 169.40.42.89 |
| 79.22 | vless | 295.2 | 615.2 | 20.94 | 0.0 | 8.68 | 10.12 | 19.48 | Au1rxx-base64 | 169.40.42.104 |
| 79.19 | vless | 297.0 | 737.5 | 20.9 | 0.0 | 8.69 | 10.12 | 19.48 | Au1rxx-base64 | 169.40.42.212 |
| 78.84 | vless | 311.7 | 705.9 | 20.56 | 0.0 | 8.68 | 10.12 | 19.48 | Au1rxx-base64 | 169.40.42.231 |
| 78.7 | vless | 317.9 | 722.7 | 20.42 | 0.0 | 8.68 | 10.12 | 19.48 | Au1rxx-base64 | 169.40.42.173 |
| 78.64 | vless | 323.1 | 874.0 | 20.3 | 0.0 | 8.74 | 10.12 | 19.48 | Au1rxx-base64 | 169.40.42.15 |
| 78.58 | vless | 325.8 | 827.5 | 20.24 | 0.0 | 8.74 | 10.12 | 19.48 | Au1rxx-base64 | 66.70.179.198 |
| 78.21 | vless | 339.9 | 930.0 | 19.91 | 0.0 | 8.7 | 10.12 | 19.48 | Au1rxx-base64 | 185.95.231.156 |
| 77.94 | vless | 359.4 | 816.3 | 19.46 | 0.0 | 8.88 | 10.12 | 19.48 | Au1rxx-base64 | 169.40.42.224 |
| 77.54 | vless | 370.4 | 954.7 | 19.2 | 0.0 | 8.74 | 10.12 | 19.48 | Au1rxx-base64 | 169.40.42.35 |
| 77.47 | shadowsocks | 334.6 | 868.6 | 20.03 | 0.0 | 8.79 | 13.67 | 19.48 | Au1rxx-base64 | 38.180.135.156 |
| 77.46 | vless | 359.9 | 903.9 | 19.45 | 0.0 | 8.68 | 10.12 | 19.48 | Au1rxx-base64 | 216.152.147.28 |
| 77.38 | hysteria2 | 293.2 | 584.2 | 20.99 | 0.0 | 8.88 | 13.85 | 19.48 | Au1rxx-base64 | 66.94.121.46 |
| 77.35 | vless | 385.4 | 937.6 | 18.86 | 0.0 | 8.89 | 10.12 | 19.48 | Au1rxx-base64 | 169.40.42.235 |
| 77.32 | vless | 377.9 | 970.4 | 19.03 | 0.0 | 8.69 | 10.12 | 19.48 | Au1rxx-base64 | 169.40.42.74 |
| 77.22 | vless | 279.8 | 682.8 | 21.3 | 0.0 | 8.69 | 10.12 | 19.48 | Au1rxx-base64 | 169.40.42.225 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.975 | 0.904 | 311 | 1862 | prefer |
| zhangkai | 0.96 | 1.0 | 20 | 144 | prefer |
| Surfboard-tg-mixed | 0.826 | 0.749 | 171 | 7274 | prefer |
| mheidari-all | 0.596 | 0.516 | 153 | 21188 | observe |
| DeltaKronecker-all | 0.391 | 1.0 | 2 | 5856 | observe |
| xiaoji235-airport-v2ray-all | 0.391 | 1.0 | 2 | 5750 | observe |
| tg-oneclickvpnkeys | 0.298 | 0.6 | 5 | 134 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4791 | observe |
| Epodonios-all | 0.255 | None | 0 | 7817 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 8616 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 6019 | observe |
| barry-far-vless | 0.255 | None | 0 | 6306 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4138 | observe |
| Au1rxx-clash | 0.249 | None | 0 | 1862 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| cn-block | ClientOSError | - | 50 |
| geo | ClientOSError | - | 33 |
| cn-block | TimeoutError | - | 17 |
| 204 | TimeoutError | - | 14 |
| 204 | ProxyConnectionError | - | 9 |
| 204 | ProxyError | - | 8 |
| speed | TimeoutError | - | 7 |
| geo | TimeoutError | - | 6 |
| 204 | ClientOSError | - | 3 |
| speed | ProxyError | - | 2 |
| speed | ClientOSError | - | 2 |
| cn-block | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
