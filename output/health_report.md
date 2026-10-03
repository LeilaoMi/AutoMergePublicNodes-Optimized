# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-03 16:08:45 |
| 运行耗时 | 449.9s |
| 订阅源总数 | 107 |
| 健康订阅源 | 94 |
| 原始节点 | 99539 |
| 去重后节点 | 27336 |
| TCP 可达 | 3000 |
| 真实可用 | 320 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 27336 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.6 |
| geo | 1.4 |
| tcp | 47.3 |
| probe | 187.2 |
| real_test | 123.4 |
| generate | 83.0 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 60957 |
| vmess | 15426 |
| shadowsocks | 11436 |
| trojan | 9371 |
| hysteria2 | 1544 |
| http | 521 |
| shadowsocksr | 170 |
| socks | 65 |
| anytls | 24 |
| hysteria | 17 |
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
| 82.42 | vless | 264.5 | 686.0 | 21.65 | 0.0 | 10.0 | 11.61 | 19.16 | Au1rxx-base64 | 137.184.218.169 |
| 81.51 | vless | 300.6 | 739.9 | 20.82 | 0.0 | 10.0 | 11.61 | 19.16 | Au1rxx-base64 | 66.70.179.198 |
| 81.4 | vless | 308.7 | 754.7 | 20.63 | 0.0 | 10.0 | 11.61 | 19.16 | Au1rxx-base64 | 169.40.42.90 |
| 81.19 | vless | 317.7 | 745.0 | 20.42 | 0.0 | 10.0 | 11.61 | 19.16 | Au1rxx-base64 | 169.40.42.104 |
| 79.87 | hysteria2 | 281.5 | 757.9 | 21.26 | 0.0 | 10.0 | 12.63 | 17.08 | mheidari-all | 159.223.157.129 |
| 78.4 | vless | 271.5 | 644.7 | 21.49 | 0.0 | 10.0 | 11.61 | 17.08 | mheidari-all | 216.227.161.95 |
| 77.62 | hysteria2 | 311.7 | 567.0 | 20.56 | 0.0 | 10.0 | 12.63 | 19.16 | Au1rxx-base64 | 192.255.128.123 |
| 77.36 | vless | 340.2 | 708.9 | 19.9 | 0.0 | 10.0 | 11.61 | 19.16 | Au1rxx-base64 | 198.251.78.29 |
| 77.1 | shadowsocks | 284.3 | 657.3 | 21.2 | 0.0 | 10.0 | 12.69 | 19.16 | Au1rxx-base64 | 156.146.38.167 |
| 75.73 | vless | 400.8 | 959.7 | 18.5 | 0.0 | 10.0 | 11.61 | 19.16 | Au1rxx-base64 | 169.40.42.168 |
| 75.68 | vless | 322.0 | 852.6 | 20.32 | 0.0 | 10.0 | 11.61 | 19.16 | Au1rxx-base64 | 159.89.87.21 |
| 75.58 | shadowsocks | 326.2 | 813.8 | 20.23 | 0.0 | 10.0 | 12.69 | 19.16 | Au1rxx-base64 | 66.23.205.28 |
| 75.17 | shadowsocks | 340.3 | 947.1 | 19.9 | 0.0 | 10.0 | 12.69 | 17.08 | mheidari-all | 15.204.247.206 |
| 75.16 | vless | 337.1 | 635.4 | 19.97 | 0.0 | 10.0 | 11.61 | 19.16 | Au1rxx-base64 | 172.235.43.210 |
| 74.86 | shadowsocks | 314.9 | 718.0 | 20.49 | 0.0 | 10.0 | 12.69 | 19.16 | Au1rxx-base64 | 108.181.57.93 |
| 74.77 | vless | 336.5 | 637.4 | 19.99 | 0.0 | 10.0 | 11.61 | 19.16 | Au1rxx-base64 | 172.235.38.85 |
| 74.26 | vless | 334.1 | 698.0 | 20.04 | 0.0 | 10.0 | 11.61 | 19.16 | Au1rxx-base64 | 23.191.200.206 |
| 73.7 | vless | 486.9 | 1173.2 | 16.51 | 0.0 | 10.0 | 11.61 | 19.16 | Au1rxx-base64 | 23.191.200.207 |
| 73.53 | hysteria2 | 495.1 | 1302.3 | 16.32 | 0.0 | 10.0 | 12.63 | 17.08 | mheidari-all | 129.213.91.185 |
| 73.29 | vless | 376.5 | 682.4 | 19.06 | 0.0 | 10.0 | 11.61 | 19.16 | Au1rxx-base64 | 15.204.97.216 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.945 | 0.877 | 260 | 1778 | prefer |
| ermaozi | 0.911 | 0.917 | 24 | 656 | prefer |
| mheidari-all | 0.862 | 0.788 | 85 | 23342 | prefer |
| Surfboard-tg-mixed | 0.335 | 1.0 | 1 | 7404 | observe |
| ermaozi-get_subscribe | 0.274 | 1.0 | 1 | 478 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5192 | observe |
| Epodonios-all | 0.255 | None | 0 | 7883 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9374 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 6035 | observe |
| barry-far-vless | 0.255 | None | 0 | 6273 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4335 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| cn-block | TimeoutError | - | 13 |
| 204 | TimeoutError | - | 11 |
| 204 | ProxyError | - | 6 |
| 204 | ProxyConnectionError | - | 5 |
| geo | TimeoutError | - | 5 |
| speed | ClientOSError | - | 4 |
| speed | TimeoutError | - | 4 |
| cn-block | ProxyError | - | 2 |
| geo | ClientOSError | - | 2 |
| cn-block | ClientOSError | - | 1 |
| 204 | ClientOSError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
