# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-14 21:51:51 |
| 运行耗时 | 628.1s |
| 订阅源总数 | 107 |
| 健康订阅源 | 95 |
| 原始节点 | 89958 |
| 去重后节点 | 25660 |
| TCP 可达 | 3000 |
| 真实可用 | 468 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 25660 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 3.7 |
| geo | 1.4 |
| tcp | 41.8 |
| probe | 278.7 |
| real_test | 223.4 |
| generate | 79.1 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 55643 |
| vmess | 13045 |
| shadowsocks | 10188 |
| trojan | 8360 |
| hysteria2 | 1892 |
| http | 604 |
| shadowsocksr | 125 |
| socks | 55 |
| anytls | 22 |
| hysteria | 14 |
| tuic | 10 |

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
| 82.82 | hysteria2 | 287.4 | 652.3 | 21.13 | 0.0 | 10.0 | 14.25 | 18.54 | Au1rxx-base64 | 159.223.157.129 |
| 81.93 | hysteria2 | 267.4 | 549.9 | 21.59 | 0.0 | 9.56 | 14.25 | 18.54 | Au1rxx-base64 | 66.94.121.46 |
| 80.78 | shadowsocks | 247.8 | 613.0 | 22.04 | 0.0 | 10.0 | 14.29 | 18.54 | Au1rxx-base64 | 156.146.38.167 |
| 80.76 | shadowsocks | 252.6 | 615.7 | 21.93 | 0.0 | 10.0 | 14.29 | 18.54 | Au1rxx-base64 | 156.146.38.168 |
| 80.19 | shadowsocks | 258.9 | 643.8 | 21.79 | 0.0 | 9.57 | 14.29 | 18.54 | Au1rxx-base64 | 156.146.38.170 |
| 79.64 | shadowsocks | 282.3 | 736.1 | 21.24 | 0.0 | 9.57 | 14.29 | 18.54 | Au1rxx-base64 | 156.146.38.169 |
| 79.01 | shadowsocks | 254.2 | 636.2 | 21.89 | 0.0 | 9.57 | 14.29 | 18.54 | Au1rxx-base64 | 23.150.248.20 |
| 78.86 | vless | 318.0 | 748.2 | 20.42 | 0.0 | 10.0 | 10.74 | 18.54 | Au1rxx-base64 | 47.253.226.114 |
| 77.47 | vless | 314.0 | 695.8 | 20.51 | 0.0 | 10.0 | 10.74 | 18.54 | Au1rxx-base64 | 169.40.42.74 |
| 77.28 | shadowsocks | 281.8 | 669.6 | 21.25 | 0.0 | 10.0 | 14.29 | 18.54 | Au1rxx-base64 | 37.19.198.236 |
| 76.86 | hysteria2 | 344.4 | 783.1 | 19.81 | 0.0 | 9.5 | 14.25 | 18.54 | Au1rxx-base64 | 107.175.219.48 |
| 76.84 | vless | 328.8 | 733.0 | 20.17 | 0.0 | 10.0 | 10.74 | 18.54 | Au1rxx-base64 | 185.95.231.156 |
| 76.22 | vless | 377.5 | 935.7 | 19.04 | 0.0 | 10.0 | 10.74 | 18.54 | Au1rxx-base64 | 216.152.147.28 |
| 76.15 | vless | 303.9 | 673.8 | 20.74 | 0.0 | 10.0 | 10.74 | 18.54 | Au1rxx-base64 | 195.123.235.177 |
| 75.87 | vless | 378.7 | 861.3 | 19.01 | 0.0 | 10.0 | 10.74 | 18.54 | Au1rxx-base64 | 66.70.179.198 |
| 75.71 | shadowsocks | 295.4 | 702.9 | 20.94 | 0.0 | 10.0 | 14.29 | 18.54 | Au1rxx-base64 | 37.19.198.243 |
| 75.7 | vless | 356.1 | 767.6 | 19.54 | 0.0 | 10.0 | 10.74 | 18.54 | Au1rxx-base64 | 167.17.69.171 |
| 75.64 | shadowsocks | 383.9 | 978.0 | 18.89 | 0.0 | 10.0 | 14.29 | 18.54 | Au1rxx-base64 | 15.204.246.132 |
| 75.61 | shadowsocks | 356.5 | 902.8 | 19.53 | 0.0 | 9.57 | 14.29 | 18.54 | Au1rxx-base64 | 37.19.198.160 |
| 75.37 | shadowsocks | 288.7 | 564.9 | 21.1 | 0.0 | 9.52 | 14.29 | 18.54 | Au1rxx-base64 | 149.22.95.183 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.993 | 0.926 | 311 | 1752 | prefer |
| Surfboard-tg-mixed | 0.721 | 0.644 | 90 | 7602 | prefer |
| mheidari-all | 0.612 | 0.532 | 186 | 21195 | observe |
| ermaozi | 0.61 | 0.6 | 35 | 393 | observe |
| ermaozi-get_subscribe | 0.272 | 1.0 | 1 | 427 | observe |
| tg-oneclickvpnkeys | 0.26 | 1.0 | 1 | 135 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4914 | observe |
| Epodonios-all | 0.255 | None | 0 | 7941 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 8691 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 6098 | observe |
| barry-far-vless | 0.255 | None | 0 | 6284 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4099 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.245 | None | 0 | 1752 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| cn-block | ClientOSError | - | 53 |
| geo | ClientOSError | - | 36 |
| 204 | TimeoutError | - | 19 |
| cn-block | TimeoutError | - | 15 |
| 204 | ProxyError | - | 13 |
| speed | ClientOSError | - | 7 |
| speed | TimeoutError | - | 4 |
| geo | TimeoutError | - | 4 |
| 204 | ClientOSError | - | 3 |
| cn-block | ProxyError | - | 2 |
| geo | ProxyError | - | 1 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
