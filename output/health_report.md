# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-06 00:03:08 |
| 运行耗时 | 472.8s |
| 订阅源总数 | 107 |
| 健康订阅源 | 94 |
| 原始节点 | 98529 |
| 去重后节点 | 27355 |
| TCP 可达 | 3000 |
| 真实可用 | 512 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 27355 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.3 |
| geo | 1.2 |
| tcp | 46.5 |
| probe | 185.9 |
| real_test | 155.2 |
| generate | 79.7 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 58675 |
| vmess | 15715 |
| shadowsocks | 11618 |
| trojan | 10166 |
| hysteria2 | 1396 |
| http | 635 |
| shadowsocksr | 169 |
| socks | 92 |
| anytls | 27 |
| tuic | 19 |
| hysteria | 17 |

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
| 83.42 | vless | 216.3 | 497.9 | 22.77 | 0.0 | 10.0 | 11.09 | 19.56 | mheidari-all | 47.251.108.158 |
| 82.66 | vless | 211.3 | 504.2 | 22.89 | 0.0 | 10.0 | 11.09 | 18.68 | Au1rxx-base64 | 137.175.82.40 |
| 80.38 | shadowsocks | 206.0 | 492.3 | 23.01 | 0.0 | 10.0 | 13.19 | 18.68 | Au1rxx-base64 | 108.181.118.10 |
| 80.25 | hysteria2 | 243.8 | 282.9 | 22.13 | 4.39 | 9.46 | 12.5 | 18.68 | Au1rxx-base64 | open.w2m.ink |
| 80.03 | vless | 195.2 | 513.9 | 23.26 | 0.0 | 10.0 | 11.09 | 18.68 | Au1rxx-base64 | 66.42.97.171 |
| 79.99 | vless | 239.8 | 544.6 | 22.23 | 0.0 | 10.0 | 11.09 | 18.68 | Au1rxx-base64 | 23.95.222.127 |
| 79.76 | shadowsocks | 254.3 | 620.0 | 21.89 | 0.0 | 10.0 | 13.19 | 18.68 | Au1rxx-base64 | 156.146.38.168 |
| 79.1 | vless | 271.6 | 601.8 | 21.49 | 0.0 | 10.0 | 11.09 | 18.68 | Au1rxx-base64 | 15.204.97.216 |
| 78.81 | shadowsocks | 258.5 | 624.5 | 21.79 | 0.0 | 10.0 | 13.19 | 18.68 | Au1rxx-base64 | 156.146.38.169 |
| 78.57 | hysteria2 | 247.1 | 254.8 | 22.06 | 5.45 | 8.95 | 12.5 | 18.68 | Au1rxx-base64 | open.2ml.bid |
| 78.26 | hysteria2 | 321.6 | 752.5 | 20.33 | 0.0 | 10.0 | 12.5 | 18.68 | Au1rxx-base64 | 129.213.91.185 |
| 78.2 | hysteria2 | 332.3 | 733.1 | 20.09 | 0.0 | 10.0 | 12.5 | 19.56 | mheidari-all | 159.223.157.129 |
| 77.95 | vless | 414.4 | 586.5 | 18.18 | 0.0 | 10.0 | 11.09 | 18.68 | Au1rxx-base64 | 107.173.237.146 |
| 77.92 | vless | 329.4 | 867.1 | 20.15 | 0.0 | 10.0 | 11.09 | 18.68 | Au1rxx-base64 | 154.12.38.202 |
| 77.79 | vless | 303.3 | 655.7 | 20.76 | 0.0 | 10.0 | 11.09 | 19.56 | mheidari-all | 216.227.161.95 |
| 77.73 | shadowsocks | 257.2 | 626.6 | 21.82 | 0.0 | 10.0 | 13.19 | 18.68 | Au1rxx-base64 | 156.146.38.167 |
| 77.28 | shadowsocks | 309.8 | 750.5 | 20.61 | 0.0 | 10.0 | 13.19 | 18.68 | Au1rxx-base64 | 5.78.51.123 |
| 76.61 | shadowsocks | 212.5 | 527.7 | 22.86 | 0.0 | 10.0 | 13.19 | 19.56 | mheidari-all | 173.244.56.6 |
| 76.5 | shadowsocks | 217.2 | 543.1 | 22.75 | 0.0 | 10.0 | 13.19 | 19.56 | mheidari-all | 173.244.56.9 |
| 76.46 | hysteria2 | 307.5 | 682.8 | 20.66 | 0.0 | 10.0 | 12.5 | 18.68 | Au1rxx-base64 | 66.94.121.46 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | 0.928 | 334 | 1862 | prefer |
| Surfboard-tg-mixed | 1.0 | 0.962 | 53 | 7145 | prefer |
| mheidari-all | 0.939 | 0.865 | 126 | 23213 | prefer |
| ermaozi | 0.641 | 0.617 | 60 | 701 | observe |
| DeltaKronecker-all | 0.391 | 1.0 | 2 | 5300 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| tg-LonUp_M | 0.262 | 1.0 | 1 | 177 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5111 | observe |
| Epodonios-all | 0.255 | None | 0 | 7624 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9352 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5642 | observe |
| barry-far-vless | 0.255 | None | 0 | 5871 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4375 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | ProxyError | - | 24 |
| cn-block | TimeoutError | - | 16 |
| geo | ClientOSError | - | 7 |
| cn-block | ClientOSError | - | 4 |
| 204 | TimeoutError | - | 4 |
| geo | TimeoutError | - | 4 |
| speed | ProxyError | - | 3 |
| speed | TimeoutError | - | 3 |
| speed | ClientOSError | - | 2 |
| 204 | ClientOSError | - | 1 |
| cn-block | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
