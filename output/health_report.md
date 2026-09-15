# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-15 11:38:37 |
| 运行耗时 | 630.9s |
| 订阅源总数 | 107 |
| 健康订阅源 | 95 |
| 原始节点 | 90261 |
| 去重后节点 | 25575 |
| TCP 可达 | 3000 |
| 真实可用 | 426 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 25575 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 3.6 |
| geo | 1.3 |
| tcp | 41.3 |
| probe | 287.7 |
| real_test | 224.3 |
| generate | 72.5 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 55603 |
| vmess | 13054 |
| shadowsocks | 10071 |
| trojan | 8804 |
| hysteria2 | 1849 |
| http | 667 |
| shadowsocksr | 128 |
| socks | 56 |
| hysteria | 14 |
| anytls | 8 |
| tuic | 7 |

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
| 83.7 | hysteria2 | 201.4 | 499.9 | 23.12 | 0.0 | 10.0 | 14.0 | 17.58 | Au1rxx-base64 | 107.175.219.48 |
| 80.47 | shadowsocks | 189.7 | 498.0 | 23.39 | 0.0 | 10.0 | 14.0 | 17.58 | Au1rxx-base64 | 108.181.0.177 |
| 77.25 | shadowsocks | 332.4 | 846.7 | 20.08 | 0.0 | 10.0 | 14.0 | 17.58 | Au1rxx-base64 | 156.146.38.168 |
| 77.03 | shadowsocks | 254.7 | 611.1 | 21.88 | 0.0 | 10.0 | 14.0 | 15.34 | Surfboard-tg-mixed | 156.146.38.167 |
| 75.77 | vless | 209.4 | 535.4 | 22.93 | 0.0 | 10.0 | 5.26 | 17.58 | Au1rxx-base64 | 45.149.172.80 |
| 75.66 | hysteria2 | 322.4 | 903.6 | 20.32 | 0.0 | 10.0 | 14.0 | 15.34 | Surfboard-tg-mixed | 45.149.172.80 |
| 74.78 | shadowsocks | 247.1 | 555.5 | 22.06 | 0.0 | 10.0 | 14.0 | 15.34 | Surfboard-tg-mixed | 5.78.51.123 |
| 74.42 | vless | 267.8 | 512.0 | 21.58 | 0.0 | 10.0 | 5.26 | 17.58 | Au1rxx-base64 | 172.233.139.46 |
| 74.34 | vless | 271.3 | 647.5 | 21.5 | 0.0 | 10.0 | 5.26 | 17.58 | Au1rxx-base64 | 172.235.43.210 |
| 73.75 | shadowsocks | 286.8 | 634.8 | 21.14 | 0.0 | 10.0 | 14.0 | 15.34 | Surfboard-tg-mixed | 23.150.248.20 |
| 73.23 | hysteria2 | 208.5 | 545.7 | 22.95 | 0.0 | 10.0 | 14.0 | 15.34 | Surfboard-tg-mixed | 45.149.172.74 |
| 72.47 | shadowsocks | 329.3 | 667.8 | 20.15 | 0.0 | 10.0 | 14.0 | 17.58 | Au1rxx-base64 | 198.98.53.130 |
| 72.26 | vless | 274.5 | 689.4 | 21.42 | 0.0 | 10.0 | 5.26 | 17.58 | Au1rxx-base64 | 198.200.42.129 |
| 71.97 | vless | 212.7 | 545.5 | 22.85 | 0.0 | 10.0 | 5.26 | 17.58 | Au1rxx-base64 | 192.3.247.109 |
| 70.28 | vless | 294.2 | 536.9 | 20.97 | 0.0 | 10.0 | 5.26 | 17.58 | Au1rxx-base64 | 144.172.104.26 |
| 70.2 | vless | 225.1 | 502.4 | 22.57 | 0.0 | 10.0 | 5.26 | 17.58 | Au1rxx-base64 | 172.64.229.170 |
| 69.67 | shadowsocks | 433.7 | 929.9 | 17.74 | 0.0 | 10.0 | 14.0 | 17.58 | Au1rxx-base64 | 108.181.57.93 |
| 69.42 | vless | 286.7 | 546.9 | 21.14 | 0.0 | 10.0 | 5.26 | 17.58 | Au1rxx-base64 | 150.241.102.181 |
| 69.17 | hysteria2 | 446.2 | 765.0 | 17.45 | 0.0 | 9.47 | 14.0 | 17.58 | Au1rxx-base64 | 62.210.124.146 |
| 69.03 | hysteria2 | 513.0 | 953.9 | 15.9 | 0.0 | 9.51 | 14.0 | 17.58 | Au1rxx-base64 | 5.129.235.85 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.902 | 0.847 | 313 | 1440 | prefer |
| mheidari-all | 0.901 | 0.831 | 65 | 21594 | prefer |
| Surfboard-tg-mixed | 0.684 | 0.606 | 109 | 7608 | observe |
| ermaozi | 0.684 | 0.673 | 52 | 425 | observe |
| DeltaKronecker-all | 0.401 | 0.571 | 7 | 5932 | observe |
| ermaozi-get_subscribe | 0.273 | 1.0 | 1 | 447 | observe |
| tg-oneclickvpnkeys | 0.261 | 1.0 | 1 | 148 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5015 | observe |
| Epodonios-all | 0.255 | None | 0 | 8009 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 8760 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 6177 | observe |
| barry-far-vless | 0.255 | None | 0 | 6343 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4258 | observe |
| Au1rxx-clash | 0.233 | None | 0 | 1440 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | TimeoutError | - | 22 |
| 204 | ProxyError | - | 20 |
| geo | ClientOSError | - | 20 |
| cn-block | TimeoutError | - | 20 |
| cn-block | ClientOSError | - | 14 |
| geo | TimeoutError | - | 10 |
| speed | TimeoutError | - | 8 |
| speed | ClientOSError | - | 7 |
| 204 | ClientOSError | - | 2 |
| cn-block | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
