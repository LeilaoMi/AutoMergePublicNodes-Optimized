# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-30 22:12:04 |
| 运行耗时 | 461.5s |
| 订阅源总数 | 107 |
| 健康订阅源 | 94 |
| 原始节点 | 97982 |
| 去重后节点 | 27241 |
| TCP 可达 | 3000 |
| 真实可用 | 362 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 27241 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.5 |
| geo | 1.6 |
| tcp | 45.5 |
| probe | 203.0 |
| real_test | 126.8 |
| generate | 77.1 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 60174 |
| vmess | 15253 |
| shadowsocks | 11357 |
| trojan | 9116 |
| hysteria2 | 1348 |
| http | 440 |
| shadowsocksr | 171 |
| socks | 68 |
| anytls | 32 |
| hysteria | 15 |
| tuic | 8 |

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
| 83.13 | hysteria2 | 273.7 | 686.1 | 21.44 | 0.0 | 10.0 | 14.17 | 18.62 | mheidari-all | 159.223.157.129 |
| 78.05 | shadowsocks | 270.4 | 717.2 | 21.52 | 0.0 | 10.0 | 12.91 | 18.62 | mheidari-all | 37.19.198.244 |
| 77.74 | vless | 263.8 | 627.0 | 21.67 | 0.0 | 10.0 | 9.21 | 18.62 | mheidari-all | 216.227.161.95 |
| 77.49 | shadowsocks | 260.7 | 706.7 | 21.74 | 0.0 | 10.0 | 12.91 | 16.84 | Au1rxx-base64 | 37.19.198.160 |
| 77.41 | shadowsocks | 264.4 | 717.1 | 21.66 | 0.0 | 10.0 | 12.91 | 16.84 | Au1rxx-base64 | 37.19.198.236 |
| 77.39 | shadowsocks | 265.3 | 716.7 | 21.64 | 0.0 | 10.0 | 12.91 | 16.84 | Au1rxx-base64 | 37.19.198.243 |
| 77.09 | vless | 264.7 | 683.3 | 21.65 | 0.0 | 10.0 | 9.21 | 16.84 | Au1rxx-base64 | 137.184.218.169 |
| 76.98 | vless | 277.0 | 717.2 | 21.37 | 0.0 | 10.0 | 9.21 | 16.84 | Au1rxx-base64 | 169.40.42.224 |
| 76.97 | vless | 296.2 | 646.9 | 20.92 | 0.0 | 10.0 | 9.21 | 16.84 | Au1rxx-base64 | 169.40.42.232 |
| 76.7 | vless | 294.2 | 708.6 | 20.97 | 0.0 | 10.0 | 9.21 | 16.84 | Au1rxx-base64 | 66.70.179.198 |
| 76.66 | vless | 309.5 | 740.1 | 20.61 | 0.0 | 10.0 | 9.21 | 16.84 | Au1rxx-base64 | 169.40.42.75 |
| 76.0 | vless | 338.3 | 897.9 | 19.95 | 0.0 | 10.0 | 9.21 | 16.84 | Au1rxx-base64 | 169.40.42.202 |
| 75.59 | vless | 355.8 | 935.8 | 19.54 | 0.0 | 10.0 | 9.21 | 16.84 | Au1rxx-base64 | 169.40.42.168 |
| 75.55 | hysteria2 | 370.1 | 828.1 | 19.21 | 0.0 | 10.0 | 14.17 | 16.84 | Au1rxx-base64 | 192.255.128.123 |
| 75.35 | vless | 366.1 | 853.7 | 19.3 | 0.0 | 10.0 | 9.21 | 16.84 | Au1rxx-base64 | 169.40.42.173 |
| 75.24 | hysteria2 | 366.5 | 702.2 | 19.29 | 0.0 | 10.0 | 14.17 | 18.62 | mheidari-all | 62.210.124.146 |
| 75.2 | vless | 339.8 | 893.7 | 19.91 | 0.0 | 10.0 | 9.21 | 16.84 | Au1rxx-base64 | 169.40.42.104 |
| 75.04 | vless | 379.5 | 959.4 | 18.99 | 0.0 | 10.0 | 9.21 | 16.84 | Au1rxx-base64 | 169.40.42.212 |
| 75.0 | vless | 381.5 | 1038.5 | 18.95 | 0.0 | 10.0 | 9.21 | 16.84 | Au1rxx-base64 | 159.89.87.21 |
| 74.75 | vless | 297.7 | 699.4 | 20.89 | 0.0 | 10.0 | 9.21 | 16.84 | Au1rxx-base64 | 167.17.69.171 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Surfboard-tg-mixed | 0.94 | 0.878 | 41 | 7200 | prefer |
| Au1rxx-base64 | 0.914 | 0.844 | 302 | 1803 | prefer |
| mheidari-all | 0.892 | 0.821 | 78 | 22901 | prefer |
| zhangkai | 0.338 | 0.353 | 17 | 144 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5327 | observe |
| Epodonios-all | 0.255 | None | 0 | 7696 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3996 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9724 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5833 | observe |
| barry-far-vless | 0.255 | None | 0 | 6072 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4183 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |
| Au1rxx-clash | 0.247 | None | 0 | 1803 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 38 |
| 204 | ProxyConnectionError | - | 22 |
| cn-block | TimeoutError | - | 6 |
| 204 | ProxyError | - | 5 |
| 204 | TimeoutError | - | 5 |
| cn-block | ClientOSError | - | 4 |
| cn-block | ProxyError | - | 4 |
| geo | TimeoutError | - | 2 |
| 204 | ClientOSError | - | 1 |
| speed | TimeoutError | - | 1 |
| geo | ClientOSError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
