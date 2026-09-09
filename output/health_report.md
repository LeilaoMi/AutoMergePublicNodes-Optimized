# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-09 04:20:20 |
| 运行耗时 | 881.5s |
| 订阅源总数 | 107 |
| 健康订阅源 | 95 |
| 原始节点 | 85797 |
| 去重后节点 | 22922 |
| TCP 可达 | 3000 |
| 真实可用 | 530 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22922 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.2 |
| geo | 1.4 |
| tcp | 39.7 |
| probe | 340.4 |
| real_test | 406.1 |
| generate | 87.5 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 53136 |
| vmess | 11831 |
| shadowsocks | 10036 |
| trojan | 8359 |
| hysteria2 | 1576 |
| http | 638 |
| shadowsocksr | 127 |
| socks | 75 |
| hysteria | 9 |
| tuic | 8 |
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
| 81.1 | hysteria2 | 251.1 | 530.6 | 21.97 | 0.0 | 8.67 | 13.5 | 20.0 | Au1rxx-base64 | 66.94.121.46 |
| 80.75 | shadowsocks | 238.6 | 607.6 | 22.25 | 0.0 | 8.67 | 13.83 | 20.0 | Au1rxx-base64 | 156.146.38.169 |
| 78.43 | vless | 294.2 | 582.5 | 20.97 | 0.0 | 8.66 | 12.23 | 20.0 | Au1rxx-base64 | 172.235.38.85 |
| 78.36 | shadowsocks | 238.7 | 603.8 | 22.25 | 0.0 | 10.0 | 13.83 | 16.28 | Surfboard-tg-mixed | 156.146.38.168 |
| 78.31 | shadowsocks | 241.1 | 611.6 | 22.2 | 0.0 | 10.0 | 13.83 | 16.28 | Surfboard-tg-mixed | 156.146.38.167 |
| 77.8 | shadowsocks | 263.1 | 602.0 | 21.69 | 0.0 | 10.0 | 13.83 | 16.28 | Surfboard-tg-mixed | 156.146.38.170 |
| 77.61 | vless | 281.1 | 259.6 | 21.27 | 5.27 | 9.66 | 12.23 | 16.28 | Surfboard-tg-mixed | 31.76.91.72 |
| 77.51 | vless | 281.4 | 578.2 | 21.26 | 0.0 | 10.0 | 12.23 | 18.4 | DeltaKronecker-all | 38.246.229.58 |
| 77.32 | vless | 285.9 | 564.2 | 21.16 | 0.0 | 8.66 | 12.23 | 20.0 | Au1rxx-base64 | 172.233.139.46 |
| 76.82 | shadowsocks | 265.6 | 597.0 | 21.63 | 0.0 | 10.0 | 13.83 | 16.28 | Surfboard-tg-mixed | 23.150.248.20 |
| 76.61 | trojan | 247.7 | 604.5 | 22.04 | 0.0 | 10.0 | 9.17 | 18.4 | DeltaKronecker-all | 64.94.95.117 |
| 76.14 | vless | 315.9 | 588.9 | 20.47 | 0.0 | 8.61 | 12.23 | 20.0 | Au1rxx-base64 | 31.58.50.200 |
| 74.79 | vless | 370.9 | 759.4 | 19.19 | 0.0 | 8.68 | 12.23 | 20.0 | Au1rxx-base64 | 167.17.69.171 |
| 74.78 | vless | 419.0 | 955.6 | 18.08 | 0.0 | 8.68 | 12.23 | 20.0 | Au1rxx-base64 | 216.152.147.28 |
| 74.58 | vless | 398.2 | 875.0 | 18.56 | 0.0 | 8.75 | 12.23 | 20.0 | Au1rxx-base64 | 66.70.179.198 |
| 73.78 | vless | 369.1 | 359.8 | 19.23 | 1.51 | 8.58 | 12.23 | 20.0 | Au1rxx-base64 | 154.31.114.248 |
| 73.72 | shadowsocks | 303.1 | 670.7 | 20.76 | 0.0 | 10.0 | 13.83 | 16.28 | Surfboard-tg-mixed | 198.98.53.130 |
| 73.63 | vless | 390.5 | 726.1 | 18.74 | 0.0 | 8.71 | 12.23 | 20.0 | Au1rxx-base64 | 169.40.42.202 |
| 73.51 | shadowsocks | 268.2 | 528.0 | 21.57 | 0.0 | 10.0 | 13.83 | 16.28 | Surfboard-tg-mixed | 108.181.0.177 |
| 73.35 | vless | 405.2 | 753.5 | 18.4 | 0.0 | 8.86 | 12.23 | 20.0 | Au1rxx-base64 | 185.47.254.251 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.962 | 0.897 | 263 | 1690 | prefer |
| Surfboard-tg-mixed | 0.824 | 0.746 | 205 | 7520 | prefer |
| mheidari-all | 0.672 | 0.595 | 74 | 16648 | observe |
| ermaozi-get_subscribe | 0.61 | 0.6 | 20 | 473 | observe |
| ermaozi | 0.573 | 0.559 | 34 | 442 | observe |
| DeltaKronecker-all | 0.412 | 0.33 | 194 | 6097 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| tg-oneclickvpnkeys | 0.262 | 1.0 | 1 | 176 | observe |
| Epodonios-all | 0.255 | None | 0 | 7969 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 8963 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 6208 | observe |
| barry-far-vless | 0.255 | None | 0 | 6393 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4219 | observe |
| Au1rxx-clash | 0.243 | None | 0 | 1690 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 67 |
| geo | ClientOSError | - | 43 |
| 204 | ProxyError | - | 41 |
| speed | TimeoutError | - | 35 |
| speed | ClientOSError | - | 28 |
| cn-block | TimeoutError | - | 20 |
| 204 | TimeoutError | - | 15 |
| cn-block | ClientOSError | - | 4 |
| 204 | ProxyConnectionError | - | 3 |
| 204 | ClientOSError | - | 3 |
| cn-block | ProxyError | - | 2 |
| geo | ProxyError | - | 2 |
| sing-box exited 1 |  [31mFATAL[0m[0000] start service: start inbound/socks[socks-in]: listen tcp 127.0.0.1:37096: bind: address already in use | - | 1 |
| speed | ClientPayloadError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
