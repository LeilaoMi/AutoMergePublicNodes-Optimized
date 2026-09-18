# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-18 11:07:05 |
| 运行耗时 | 648.8s |
| 订阅源总数 | 107 |
| 健康订阅源 | 94 |
| 原始节点 | 83513 |
| 去重后节点 | 22980 |
| TCP 可达 | 3000 |
| 真实可用 | 391 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22980 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.4 |
| geo | 1.4 |
| tcp | 37.4 |
| probe | 255.8 |
| real_test | 258.5 |
| generate | 89.2 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 49723 |
| vmess | 13256 |
| shadowsocks | 10074 |
| trojan | 8223 |
| hysteria2 | 1378 |
| http | 649 |
| shadowsocksr | 127 |
| socks | 69 |
| hysteria | 8 |
| anytls | 4 |
| tuic | 2 |

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
| 79.74 | shadowsocks | 298.5 | 818.6 | 20.87 | 0.0 | 10.0 | 14.43 | 18.94 | Au1rxx-base64 | 38.180.135.156 |
| 78.88 | hysteria2 | 308.6 | 626.5 | 20.63 | 0.0 | 10.0 | 14.25 | 18.94 | Au1rxx-base64 | 66.94.121.46 |
| 78.37 | shadowsocks | 357.8 | 1038.8 | 19.5 | 0.0 | 10.0 | 14.43 | 18.94 | Au1rxx-base64 | 15.204.247.206 |
| 78.02 | shadowsocks | 278.2 | 644.9 | 21.34 | 0.0 | 10.0 | 14.43 | 18.94 | Au1rxx-base64 | 156.146.38.169 |
| 77.83 | shadowsocks | 286.0 | 656.7 | 21.16 | 0.0 | 10.0 | 14.43 | 18.94 | Au1rxx-base64 | 156.146.38.167 |
| 77.62 | vless | 250.7 | 701.8 | 21.98 | 0.0 | 10.0 | 6.7 | 18.94 | Au1rxx-base64 | 79.141.172.154 |
| 77.09 | vless | 273.4 | 605.4 | 21.45 | 0.0 | 10.0 | 6.7 | 18.94 | Au1rxx-base64 | 169.40.42.168 |
| 76.91 | vless | 281.1 | 618.5 | 21.27 | 0.0 | 10.0 | 6.7 | 18.94 | Au1rxx-base64 | 169.40.42.225 |
| 76.84 | vless | 274.5 | 730.1 | 21.42 | 0.0 | 10.0 | 6.7 | 18.94 | Au1rxx-base64 | 169.40.42.16 |
| 76.3 | vless | 307.7 | 852.9 | 20.66 | 0.0 | 10.0 | 6.7 | 18.94 | Au1rxx-base64 | 137.184.218.169 |
| 75.98 | vless | 321.4 | 885.7 | 20.34 | 0.0 | 10.0 | 6.7 | 18.94 | Au1rxx-base64 | 185.95.231.156 |
| 75.96 | vless | 279.2 | 749.1 | 21.32 | 0.0 | 10.0 | 6.7 | 18.94 | Au1rxx-base64 | 169.40.42.231 |
| 75.68 | vless | 289.2 | 763.6 | 21.08 | 0.0 | 10.0 | 6.7 | 18.94 | Au1rxx-base64 | 169.40.42.75 |
| 75.57 | vless | 338.9 | 794.2 | 19.93 | 0.0 | 10.0 | 6.7 | 18.94 | Au1rxx-base64 | 169.40.42.133 |
| 75.56 | vless | 277.5 | 745.5 | 21.35 | 0.0 | 10.0 | 6.7 | 18.94 | Au1rxx-base64 | 169.40.42.74 |
| 75.47 | vless | 343.5 | 886.5 | 19.83 | 0.0 | 10.0 | 6.7 | 18.94 | Au1rxx-base64 | 169.40.42.104 |
| 75.44 | shadowsocks | 293.0 | 635.7 | 21.0 | 0.0 | 10.0 | 14.43 | 18.94 | Au1rxx-base64 | 23.150.248.20 |
| 75.39 | hysteria2 | 254.0 | 634.2 | 21.9 | 0.0 | 10.0 | 14.25 | 10.34 | mheidari-all | 159.223.157.129 |
| 75.27 | vless | 351.9 | 864.2 | 19.63 | 0.0 | 10.0 | 6.7 | 18.94 | Au1rxx-base64 | 169.40.42.52 |
| 75.23 | vless | 353.8 | 974.5 | 19.59 | 0.0 | 10.0 | 6.7 | 18.94 | Au1rxx-base64 | 169.40.42.95 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.906 | 0.844 | 256 | 1622 | prefer |
| mheidari-all | 0.788 | 0.717 | 46 | 15778 | prefer |
| ermaozi | 0.76 | 0.756 | 45 | 378 | prefer |
| Surfboard-tg-mixed | 0.651 | 0.571 | 154 | 7294 | observe |
| DeltaKronecker-all | 0.484 | 0.4 | 45 | 6040 | observe |
| mahdibland-V2RayAggregator | 0.335 | 1.0 | 1 | 4241 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| Epodonios-all | 0.255 | None | 0 | 7751 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 8957 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5763 | observe |
| barry-far-vless | 0.255 | None | 0 | 5979 | observe |
| Au1rxx-clash | 0.24 | None | 0 | 1622 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |
| 10ium-HighSpeed | 0.209 | None | 0 | 839 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | TimeoutError | - | 39 |
| geo | TimeoutError | - | 23 |
| speed | TimeoutError | - | 21 |
| cn-block | TimeoutError | - | 19 |
| geo | ClientOSError | - | 18 |
| 204 | ProxyError | - | 14 |
| cn-block | ClientOSError | - | 11 |
| speed | ClientOSError | - | 9 |
| cn-block | ProxyError | - | 4 |
| 204 | ClientOSError | - | 2 |
| geo | ProxyError | - | 1 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
