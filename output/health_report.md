# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-25 11:41:40 |
| 运行耗时 | 516.5s |
| 订阅源总数 | 107 |
| 健康订阅源 | 94 |
| 原始节点 | 96970 |
| 去重后节点 | 26327 |
| TCP 可达 | 3000 |
| 真实可用 | 290 |
| Verified 输出 | 290 |
| Global 输出 | 300 |
| All 输出 | 26327 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.0 |
| geo | 1.5 |
| tcp | 42.9 |
| probe | 263.1 |
| real_test | 121.0 |
| generate | 81.0 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 58825 |
| vmess | 15169 |
| shadowsocks | 11416 |
| trojan | 8991 |
| hysteria2 | 1643 |
| http | 635 |
| shadowsocksr | 172 |
| socks | 73 |
| anytls | 24 |
| hysteria | 15 |
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
| 80.94 | shadowsocks | 234.2 | 595.6 | 22.36 | 0.0 | 8.67 | 14.41 | 19.5 | Au1rxx-base64 | 198.98.53.130 |
| 78.19 | hysteria2 | 274.4 | 708.8 | 21.43 | 0.0 | 8.77 | 14.35 | 19.5 | Au1rxx-base64 | 159.223.157.129 |
| 77.5 | shadowsocks | 281.2 | 735.5 | 21.27 | 0.0 | 10.0 | 14.41 | 15.82 | Surfboard-tg-mixed | 37.19.198.243 |
| 76.87 | vless | 251.4 | 631.5 | 21.96 | 0.0 | 8.9 | 6.51 | 19.5 | Au1rxx-base64 | 195.211.98.43 |
| 76.27 | vless | 275.1 | 695.6 | 21.41 | 0.0 | 8.85 | 6.51 | 19.5 | Au1rxx-base64 | 137.184.218.169 |
| 76.01 | vless | 281.8 | 720.7 | 21.25 | 0.0 | 8.75 | 6.51 | 19.5 | Au1rxx-base64 | 79.141.172.154 |
| 75.35 | shadowsocks | 284.7 | 640.3 | 21.19 | 0.0 | 10.0 | 14.41 | 15.82 | Surfboard-tg-mixed | 156.146.38.167 |
| 75.16 | vless | 291.9 | 726.8 | 21.02 | 0.0 | 8.81 | 6.51 | 19.5 | Au1rxx-base64 | 66.70.179.198 |
| 73.91 | vless | 377.6 | 996.7 | 19.04 | 0.0 | 8.86 | 6.51 | 19.5 | Au1rxx-base64 | 185.95.231.156 |
| 72.93 | vless | 361.1 | 830.8 | 19.42 | 0.0 | 8.85 | 6.51 | 19.5 | Au1rxx-base64 | 169.40.42.74 |
| 72.61 | vless | 343.7 | 766.1 | 19.82 | 0.0 | 8.84 | 6.51 | 19.5 | Au1rxx-base64 | 169.40.42.179 |
| 72.49 | vless | 353.1 | 934.6 | 19.61 | 0.0 | 6.87 | 6.51 | 19.5 | Au1rxx-base64 | ww9.levikogjgfdd.ir |
| 72.43 | shadowsocks | 466.8 | 1206.2 | 16.97 | 0.0 | 10.0 | 14.41 | 15.82 | Surfboard-tg-mixed | 15.235.75.71 |
| 72.27 | vless | 385.4 | 937.4 | 18.86 | 0.0 | 8.9 | 6.51 | 19.5 | Au1rxx-base64 | 169.40.42.75 |
| 71.59 | hysteria2 | 426.6 | 875.5 | 17.9 | 0.0 | 10.0 | 14.35 | 15.82 | Surfboard-tg-mixed | 130.49.161.70 |
| 71.54 | vless | 339.2 | 771.4 | 19.93 | 0.0 | 8.8 | 6.51 | 19.5 | Au1rxx-base64 | 169.40.42.232 |
| 71.49 | vless | 289.6 | 731.1 | 21.08 | 0.0 | 8.9 | 6.51 | 19.5 | Au1rxx-base64 | 162.35.96.39 |
| 71.4 | vless | 400.9 | 885.4 | 18.5 | 0.0 | 8.76 | 6.51 | 19.5 | Au1rxx-base64 | 169.40.42.35 |
| 71.23 | vless | 303.6 | 771.4 | 20.75 | 0.0 | 8.97 | 6.51 | 19.5 | Au1rxx-base64 | 162.35.96.15 |
| 71.15 | vless | 451.0 | 1168.7 | 17.34 | 0.0 | 8.86 | 6.51 | 19.5 | Au1rxx-base64 | 158.69.112.254 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.925 | 0.864 | 191 | 1624 | prefer |
| mheidari-all | 0.886 | 0.817 | 60 | 22444 | prefer |
| Surfboard-tg-mixed | 0.737 | 0.662 | 68 | 7280 | prefer |
| ermaozi | 0.576 | 0.565 | 46 | 338 | observe |
| DeltaKronecker-all | 0.372 | 0.444 | 9 | 5452 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5293 | observe |
| Epodonios-all | 0.255 | None | 0 | 7869 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9069 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5801 | observe |
| barry-far-vless | 0.255 | None | 0 | 6140 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4324 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | ProxyConnectionError | - | 25 |
| 204 | ProxyError | - | 15 |
| 204 | TimeoutError | - | 15 |
| cn-block | TimeoutError | - | 11 |
| geo | TimeoutError | - | 6 |
| speed | TimeoutError | - | 5 |
| cn-block | ClientOSError | - | 4 |
| 204 | ClientOSError | - | 4 |
| speed | ClientOSError | - | 2 |
| geo | ProxyError | - | 1 |
| geo | ClientOSError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 290 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
