# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-14 04:34:31 |
| 运行耗时 | 850.3s |
| 订阅源总数 | 107 |
| 健康订阅源 | 95 |
| 原始节点 | 89766 |
| 去重后节点 | 25427 |
| TCP 可达 | 3000 |
| 真实可用 | 488 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 25427 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.2 |
| geo | 1.4 |
| tcp | 43.4 |
| probe | 288.6 |
| real_test | 429.9 |
| generate | 80.8 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 54889 |
| vmess | 13293 |
| shadowsocks | 10508 |
| trojan | 8383 |
| hysteria2 | 1794 |
| http | 670 |
| shadowsocksr | 131 |
| socks | 57 |
| tuic | 18 |
| hysteria | 14 |
| anytls | 9 |

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
| 82.28 | vless | 272.5 | 631.6 | 21.47 | 0.0 | 9.87 | 11.74 | 19.2 | Au1rxx-base64 | 198.251.78.29 |
| 81.8 | vless | 290.1 | 698.1 | 21.06 | 0.0 | 9.8 | 11.74 | 19.2 | Au1rxx-base64 | 79.141.172.154 |
| 80.58 | hysteria2 | 284.9 | 670.1 | 21.18 | 0.0 | 10.0 | 13.12 | 17.38 | mheidari-all | 159.223.157.129 |
| 80.53 | vless | 306.8 | 727.0 | 20.67 | 0.0 | 9.87 | 11.74 | 19.2 | Au1rxx-base64 | 47.253.226.114 |
| 79.0 | shadowsocks | 250.0 | 613.3 | 21.99 | 0.0 | 10.0 | 13.63 | 17.38 | mheidari-all | 156.146.38.169 |
| 78.95 | shadowsocks | 252.3 | 624.7 | 21.94 | 0.0 | 10.0 | 13.63 | 17.38 | mheidari-all | 156.146.38.168 |
| 78.78 | hysteria2 | 297.9 | 580.8 | 20.88 | 0.0 | 9.83 | 13.12 | 19.2 | Au1rxx-base64 | 66.94.121.46 |
| 78.46 | shadowsocks | 232.9 | 567.3 | 22.39 | 0.0 | 10.0 | 13.63 | 16.44 | Surfboard-tg-mixed | 156.146.38.167 |
| 78.34 | vless | 289.9 | 615.4 | 21.07 | 0.0 | 9.96 | 11.74 | 19.2 | Au1rxx-base64 | 64.49.38.3 |
| 78.23 | vless | 333.1 | 699.6 | 20.07 | 0.0 | 9.87 | 11.74 | 19.2 | Au1rxx-base64 | 167.17.69.171 |
| 78.0 | vless | 302.0 | 680.3 | 20.79 | 0.0 | 9.99 | 11.74 | 19.2 | Au1rxx-base64 | 195.123.235.177 |
| 77.94 | hysteria2 | 265.6 | 518.8 | 21.63 | 0.0 | 9.72 | 13.12 | 19.2 | Au1rxx-base64 | 107.175.219.48 |
| 77.75 | vless | 334.0 | 796.7 | 20.05 | 0.0 | 10.0 | 11.74 | 19.2 | Au1rxx-base64 | 185.95.231.156 |
| 77.59 | vless | 300.7 | 537.6 | 20.82 | 0.0 | 9.85 | 11.74 | 19.2 | Au1rxx-base64 | 150.241.102.181 |
| 77.15 | vless | 309.8 | 730.4 | 20.61 | 0.0 | 10.0 | 11.74 | 16.44 | Surfboard-tg-mixed | 47.89.186.170 |
| 77.14 | vless | 301.5 | 570.4 | 20.8 | 0.0 | 10.0 | 11.74 | 19.2 | Au1rxx-base64 | 144.172.104.26 |
| 77.1 | shadowsocks | 270.1 | 603.2 | 21.53 | 0.0 | 10.0 | 13.63 | 16.44 | Surfboard-tg-mixed | 23.150.248.20 |
| 76.77 | vless | 407.6 | 977.9 | 18.34 | 0.0 | 9.82 | 11.74 | 19.2 | Au1rxx-base64 | 169.40.42.231 |
| 76.76 | vless | 307.0 | 732.2 | 20.67 | 0.0 | 9.96 | 11.74 | 19.2 | Au1rxx-base64 | 184.107.106.68 |
| 76.56 | vless | 313.1 | 671.2 | 20.53 | 0.0 | 9.83 | 11.74 | 19.2 | Au1rxx-base64 | 169.40.42.184 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.859 | 0.794 | 315 | 1684 | prefer |
| Surfboard-tg-mixed | 0.797 | 0.72 | 164 | 7482 | prefer |
| mheidari-all | 0.584 | 0.504 | 127 | 15963 | observe |
| ermaozi | 0.583 | 0.571 | 28 | 417 | observe |
| ermaozi-get_subscribe | 0.427 | 0.667 | 9 | 444 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| Epodonios-all | 0.255 | None | 0 | 7945 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3996 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 8786 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 6107 | observe |
| barry-far-vless | 0.255 | None | 0 | 6350 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4222 | observe |
| DeltaKronecker-all | 0.247 | 0.163 | 190 | 5892 | downweight |
| Au1rxx-clash | 0.242 | None | 0 | 1684 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 123 |
| geo | ClientOSError | - | 67 |
| speed | TimeoutError | - | 56 |
| speed | ClientOSError | - | 52 |
| 204 | ProxyError | - | 25 |
| cn-block | TimeoutError | - | 19 |
| cn-block | ClientOSError | - | 13 |
| 204 | TimeoutError | - | 12 |
| 204 | ClientOSError | - | 2 |
| cn-block | ProxyError | - | 1 |
| 204 | ServerDisconnectedError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
