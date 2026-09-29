# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-29 05:27:45 |
| 运行耗时 | 917.8s |
| 订阅源总数 | 107 |
| 健康订阅源 | 94 |
| 原始节点 | 96799 |
| 去重后节点 | 27001 |
| TCP 可达 | 3000 |
| 真实可用 | 504 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 27001 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.4 |
| geo | 1.5 |
| tcp | 44.0 |
| probe | 312.4 |
| real_test | 478.3 |
| generate | 74.3 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 59488 |
| vmess | 14853 |
| shadowsocks | 11299 |
| trojan | 8877 |
| hysteria2 | 1344 |
| http | 643 |
| shadowsocksr | 170 |
| socks | 78 |
| anytls | 24 |
| hysteria | 15 |
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
| 81.08 | vless | 269.4 | 638.1 | 21.54 | 0.0 | 9.12 | 11.8 | 18.62 | Au1rxx-base64 | 195.123.235.177 |
| 80.61 | vless | 290.0 | 733.1 | 21.06 | 0.0 | 9.13 | 11.8 | 18.62 | Au1rxx-base64 | 47.90.153.88 |
| 80.09 | vless | 301.3 | 682.1 | 20.8 | 0.0 | 8.94 | 11.8 | 18.62 | Au1rxx-base64 | 169.40.42.52 |
| 79.96 | vless | 315.1 | 786.2 | 20.48 | 0.0 | 9.06 | 11.8 | 18.62 | Au1rxx-base64 | 169.40.42.225 |
| 79.92 | shadowsocks | 276.7 | 715.4 | 21.37 | 0.0 | 10.0 | 14.49 | 18.06 | mheidari-all | 37.19.198.236 |
| 79.9 | vless | 320.6 | 795.4 | 20.36 | 0.0 | 9.12 | 11.8 | 18.62 | Au1rxx-base64 | 169.40.42.15 |
| 79.55 | vless | 373.7 | 958.2 | 19.13 | 0.0 | 10.0 | 11.8 | 18.62 | Au1rxx-base64 | 169.40.42.104 |
| 79.45 | hysteria2 | 261.0 | 671.4 | 21.74 | 0.0 | 10.0 | 13.75 | 18.06 | mheidari-all | 159.223.157.129 |
| 79.19 | vless | 306.2 | 741.0 | 20.69 | 0.0 | 9.07 | 11.8 | 18.62 | Au1rxx-base64 | 66.70.179.198 |
| 79.14 | hysteria2 | 265.0 | 557.3 | 21.64 | 0.0 | 8.87 | 13.75 | 18.62 | Au1rxx-base64 | 192.255.128.123 |
| 78.87 | vless | 362.8 | 942.7 | 19.38 | 0.0 | 9.07 | 11.8 | 18.62 | Au1rxx-base64 | 185.95.231.233 |
| 78.77 | vless | 374.2 | 765.2 | 19.12 | 0.0 | 9.23 | 11.8 | 18.62 | Au1rxx-base64 | 169.40.42.16 |
| 78.62 | vless | 373.9 | 955.1 | 19.12 | 0.0 | 10.0 | 11.8 | 18.62 | Au1rxx-base64 | 169.40.42.133 |
| 78.49 | shadowsocks | 289.3 | 684.9 | 21.08 | 0.0 | 10.0 | 14.49 | 18.06 | mheidari-all | 23.150.248.20 |
| 78.1 | vless | 293.1 | 715.0 | 20.99 | 0.0 | 9.06 | 11.8 | 18.62 | Au1rxx-base64 | 169.40.42.89 |
| 77.99 | vless | 313.6 | 719.8 | 20.52 | 0.0 | 8.94 | 11.8 | 18.62 | Au1rxx-base64 | 169.40.42.179 |
| 77.79 | vless | 399.9 | 1037.9 | 18.52 | 0.0 | 9.01 | 11.8 | 18.62 | Au1rxx-base64 | 169.40.42.35 |
| 77.77 | vless | 407.7 | 1079.2 | 18.34 | 0.0 | 9.01 | 11.8 | 18.62 | Au1rxx-base64 | 185.95.231.156 |
| 77.7 | vless | 322.6 | 599.9 | 20.31 | 0.0 | 10.0 | 11.8 | 18.06 | mheidari-all | 104.21.14.116 |
| 77.62 | shadowsocks | 354.7 | 780.5 | 19.57 | 0.0 | 10.0 | 14.49 | 18.06 | mheidari-all | 15.204.247.206 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.849 | 0.786 | 355 | 1609 | prefer |
| Surfboard-tg-mixed | 0.747 | 0.676 | 37 | 7005 | prefer |
| ermaozi | 0.691 | 0.688 | 32 | 354 | observe |
| mheidari-all | 0.403 | 0.322 | 540 | 22589 | observe |
| tg-oneclickvpnkeys | 0.26 | 1.0 | 1 | 121 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5326 | observe |
| Epodonios-all | 0.255 | None | 0 | 7625 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9567 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5633 | observe |
| barry-far-vless | 0.255 | None | 0 | 6028 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4237 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |
| Au1rxx-clash | 0.239 | None | 0 | 1609 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 175 |
| speed | TimeoutError | - | 89 |
| speed | ClientOSError | - | 70 |
| geo | ClientOSError | - | 57 |
| 204 | TimeoutError | - | 22 |
| 204 | ProxyError | - | 18 |
| cn-block | TimeoutError | - | 18 |
| 204 | ProxyConnectionError | - | 14 |
| cn-block | ClientOSError | - | 8 |
| 204 | ClientOSError | - | 4 |
| speed | ClientPayloadError | - | 2 |
| cn-block | ProxyError | - | 1 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
