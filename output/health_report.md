# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-26 16:18:04 |
| 运行耗时 | 580.7s |
| 订阅源总数 | 107 |
| 健康订阅源 | 94 |
| 原始节点 | 96747 |
| 去重后节点 | 26321 |
| TCP 可达 | 3000 |
| 真实可用 | 345 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 26321 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.9 |
| geo | 1.5 |
| tcp | 43.3 |
| probe | 239.0 |
| real_test | 213.0 |
| generate | 77.0 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 58774 |
| vmess | 15341 |
| shadowsocks | 11280 |
| trojan | 8927 |
| hysteria2 | 1515 |
| http | 609 |
| shadowsocksr | 172 |
| socks | 78 |
| anytls | 25 |
| hysteria | 15 |
| tuic | 11 |

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
| 76.85 | vless | 403.7 | 1074.6 | 18.43 | 0.0 | 8.71 | 10.77 | 19.16 | Au1rxx-base64 | 79.141.172.154 |
| 75.63 | vless | 463.9 | 1197.4 | 17.04 | 0.0 | 8.66 | 10.77 | 19.16 | Au1rxx-base64 | 198.251.78.29 |
| 75.0 | vless | 290.2 | 626.9 | 21.06 | 0.0 | 8.78 | 10.77 | 19.16 | Au1rxx-base64 | 172.64.229.170 |
| 74.64 | shadowsocks | 254.5 | 622.7 | 21.89 | 0.0 | 10.0 | 12.61 | 15.14 | Surfboard-tg-mixed | 156.146.38.169 |
| 74.36 | shadowsocks | 284.1 | 720.7 | 21.2 | 0.0 | 10.0 | 12.61 | 15.14 | Surfboard-tg-mixed | 156.146.38.167 |
| 73.91 | vless | 350.8 | 704.2 | 19.66 | 0.0 | 8.77 | 10.77 | 19.16 | Au1rxx-base64 | 169.40.42.184 |
| 73.83 | shadowsocks | 405.3 | 1036.2 | 18.4 | 0.0 | 8.79 | 12.61 | 19.16 | Au1rxx-base64 | 37.19.198.243 |
| 73.64 | vless | 371.9 | 779.9 | 19.17 | 0.0 | 8.72 | 10.77 | 19.16 | Au1rxx-base64 | 192.255.193.161 |
| 73.37 | vless | 419.8 | 966.6 | 18.06 | 0.0 | 8.68 | 10.77 | 19.16 | Au1rxx-base64 | 169.40.42.235 |
| 73.34 | vless | 290.4 | 605.3 | 21.06 | 0.0 | 10.0 | 10.77 | 15.14 | Surfboard-tg-mixed | 172.235.38.85 |
| 73.29 | vless | 399.5 | 922.3 | 18.53 | 0.0 | 8.71 | 10.77 | 19.16 | Au1rxx-base64 | 169.40.42.104 |
| 73.22 | vless | 432.5 | 1011.2 | 17.77 | 0.0 | 8.68 | 10.77 | 19.16 | Au1rxx-base64 | 169.40.42.163 |
| 72.98 | vless | 385.7 | 810.6 | 18.85 | 0.0 | 8.73 | 10.77 | 19.16 | Au1rxx-base64 | 195.123.240.65 |
| 72.95 | vless | 367.4 | 850.0 | 19.27 | 0.0 | 8.71 | 10.77 | 19.16 | Au1rxx-base64 | 169.40.42.202 |
| 72.95 | vless | 399.9 | 907.0 | 18.52 | 0.0 | 8.69 | 10.77 | 19.16 | Au1rxx-base64 | 169.40.42.95 |
| 72.89 | vless | 462.8 | 1176.6 | 17.06 | 0.0 | 8.68 | 10.77 | 19.16 | Au1rxx-base64 | 185.95.231.156 |
| 72.76 | vless | 432.9 | 961.7 | 17.76 | 0.0 | 8.71 | 10.77 | 19.16 | Au1rxx-base64 | 169.40.42.229 |
| 72.57 | vless | 315.7 | 544.0 | 20.47 | 0.0 | 8.65 | 10.77 | 19.16 | Au1rxx-base64 | 137.175.82.40 |
| 72.24 | vless | 397.8 | 863.1 | 18.57 | 0.0 | 8.78 | 10.77 | 19.16 | Au1rxx-base64 | 169.40.42.74 |
| 72.13 | shadowsocks | 358.3 | 908.5 | 19.48 | 0.0 | 10.0 | 12.61 | 14.54 | mheidari-all | yyz-ca-01.blncvpn4u.cc |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.936 | 0.873 | 268 | 1642 | prefer |
| mheidari-all | 0.742 | 0.667 | 63 | 22551 | prefer |
| Surfboard-tg-mixed | 0.694 | 0.616 | 99 | 7263 | observe |
| ermaozi | 0.426 | 0.421 | 19 | 296 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5242 | observe |
| Epodonios-all | 0.255 | None | 0 | 7742 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3996 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 8947 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5823 | observe |
| barry-far-vless | 0.255 | None | 0 | 6056 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.241 | None | 0 | 1642 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |
| 10ium-HighSpeed | 0.209 | None | 0 | 839 | observe |
| DeltaKronecker-all | 0.207 | 0.0 | 1 | 5512 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| cn-block | TimeoutError | - | 26 |
| 204 | TimeoutError | - | 26 |
| 204 | ProxyError | - | 13 |
| cn-block | ClientOSError | - | 13 |
| speed | TimeoutError | - | 9 |
| 204 | ProxyConnectionError | - | 8 |
| geo | TimeoutError | - | 5 |
| speed | ClientOSError | - | 4 |
| geo | ClientOSError | - | 3 |
| cn-block | ProxyError | - | 2 |
| 204 | ClientOSError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
