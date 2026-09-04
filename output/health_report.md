# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-04 04:00:36 |
| 运行耗时 | 312.3s |
| 订阅源总数 | 107 |
| 健康订阅源 | 95 |
| 原始节点 | 82420 |
| 去重后节点 | 22769 |
| TCP 可达 | 3000 |
| 真实可用 | 612 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22769 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.0 |
| geo | 1.5 |
| tcp | 37.0 |
| probe | 89.9 |
| real_test | 145.6 |
| generate | 31.3 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 51281 |
| vmess | 11524 |
| shadowsocks | 9812 |
| trojan | 7901 |
| hysteria2 | 1544 |
| http | 141 |
| shadowsocksr | 126 |
| socks | 65 |
| tuic | 15 |
| hysteria | 10 |
| anytls | 1 |

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
| 86.09 | vless | 170.2 | 466.9 | 23.84 | 0.0 | 10.0 | 12.63 | 19.62 | Au1rxx-base64 | 173.255.242.56 |
| 86.09 | vless | 170.2 | 477.3 | 23.84 | 0.0 | 10.0 | 12.63 | 19.62 | Au1rxx-base64 | 74.207.245.124 |
| 86.06 | vless | 171.3 | 460.2 | 23.81 | 0.0 | 10.0 | 12.63 | 19.62 | Au1rxx-base64 | 45.33.107.237 |
| 86.05 | vless | 171.7 | 471.1 | 23.8 | 0.0 | 10.0 | 12.63 | 19.62 | Au1rxx-base64 | 50.116.9.184 |
| 86.05 | vless | 172.0 | 472.7 | 23.8 | 0.0 | 10.0 | 12.63 | 19.62 | Au1rxx-base64 | 173.255.242.235 |
| 86.04 | vless | 172.1 | 472.8 | 23.79 | 0.0 | 10.0 | 12.63 | 19.62 | Au1rxx-base64 | 173.230.155.55 |
| 85.79 | vless | 183.0 | 495.7 | 23.54 | 0.0 | 10.0 | 12.63 | 19.62 | Au1rxx-base64 | 31.58.50.200 |
| 85.72 | vless | 176.5 | 481.0 | 23.69 | 0.0 | 10.0 | 12.63 | 19.62 | Au1rxx-base64 | 192.155.87.188 |
| 85.58 | vless | 192.1 | 505.9 | 23.33 | 0.0 | 10.0 | 12.63 | 19.62 | Au1rxx-base64 | 172.233.156.123 |
| 85.49 | vless | 196.1 | 494.6 | 23.24 | 0.0 | 10.0 | 12.63 | 19.62 | Au1rxx-base64 | 172.235.38.85 |
| 85.44 | vless | 198.3 | 518.0 | 23.19 | 0.0 | 10.0 | 12.63 | 19.62 | Au1rxx-base64 | 172.236.252.35 |
| 85.42 | vless | 199.2 | 513.2 | 23.17 | 0.0 | 10.0 | 12.63 | 19.62 | Au1rxx-base64 | 172.235.43.210 |
| 85.38 | vless | 200.7 | 505.5 | 23.13 | 0.0 | 10.0 | 12.63 | 19.62 | Au1rxx-base64 | 172.233.139.46 |
| 85.34 | vless | 202.7 | 527.4 | 23.09 | 0.0 | 10.0 | 12.63 | 19.62 | Au1rxx-base64 | 172.239.67.156 |
| 85.17 | vless | 209.7 | 538.0 | 22.92 | 0.0 | 10.0 | 12.63 | 19.62 | Au1rxx-base64 | 172.239.67.231 |
| 85.1 | vless | 212.9 | 604.8 | 22.85 | 0.0 | 10.0 | 12.63 | 19.62 | Au1rxx-base64 | 45.79.103.108 |
| 84.77 | vless | 227.0 | 559.9 | 22.52 | 0.0 | 10.0 | 12.63 | 19.62 | Au1rxx-base64 | 172.233.156.118 |
| 83.89 | http | 199.2 | 503.0 | 23.17 | 0.0 | 10.0 | 14.44 | 19.28 | zhangkai | 138.199.35.198 |
| 83.49 | http | 216.5 | 568.8 | 22.77 | 0.0 | 10.0 | 14.44 | 19.28 | zhangkai | 138.199.35.216 |
| 81.96 | shadowsocks | 196.1 | 479.7 | 23.24 | 0.0 | 10.0 | 13.6 | 19.62 | Au1rxx-base64 | 108.181.118.10 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | 0.945 | 381 | 1753 | prefer |
| zhangkai | 0.922 | 0.955 | 22 | 144 | prefer |
| mheidari-all | 0.686 | 0.608 | 186 | 15793 | observe |
| DeltaKronecker-all | 0.517 | 0.437 | 252 | 6335 | observe |
| Surfboard-tg-mixed | 0.385 | 0.5 | 8 | 7237 | observe |
| tg-oneclickvpnkeys | 0.323 | 0.75 | 4 | 71 | observe |
| Epodonios-all | 0.255 | None | 0 | 7701 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7955 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 6022 | observe |
| barry-far-vless | 0.255 | None | 0 | 6237 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4133 | observe |
| Au1rxx-clash | 0.245 | None | 0 | 1753 | observe |
| 10ium-ScrapeCategorize-Vless | 0.226 | 0.2 | 5 | 4671 | downweight |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 99 |
| speed | TimeoutError | - | 39 |
| geo | ClientOSError | - | 32 |
| speed | ClientOSError | - | 29 |
| cn-block | TimeoutError | - | 18 |
| cn-block | ClientOSError | - | 9 |
| 204 | ProxyError | - | 9 |
| 204 | TimeoutError | - | 6 |
| 204 | ProxyConnectionError | - | 2 |
| 204 | ClientOSError | - | 2 |
| cn-block | ProxyError | - | 1 |
| speed | ClientPayloadError | - | 1 |
| 204 | ServerDisconnectedError | - | 1 |
| sing-box exited 1 |  [31mFATAL[0m[0000] start service: start inbound/socks[socks-in]: listen tcp 127.0.0.1:41601: bind: address already in use | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
