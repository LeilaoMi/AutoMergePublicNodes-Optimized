# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-20 04:32:58 |
| 运行耗时 | 609.7s |
| 订阅源总数 | 107 |
| 健康订阅源 | 96 |
| 原始节点 | 87371 |
| 去重后节点 | 25387 |
| TCP 可达 | 3000 |
| 真实可用 | 581 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 25387 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.2 |
| geo | 1.4 |
| tcp | 42.4 |
| probe | 218.9 |
| real_test | 314.5 |
| generate | 25.3 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 52095 |
| vmess | 13925 |
| shadowsocks | 10730 |
| trojan | 8635 |
| hysteria2 | 1106 |
| http | 667 |
| shadowsocksr | 121 |
| socks | 73 |
| hysteria | 12 |
| tuic | 4 |
| anytls | 3 |

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
| 82.6 | hysteria2 | 242.5 | 638.3 | 22.16 | 0.0 | 10.0 | 13.24 | 18.3 | Au1rxx-base64 | 159.223.157.129 |
| 80.41 | vless | 236.0 | 623.4 | 22.31 | 0.0 | 10.0 | 9.8 | 18.3 | Au1rxx-base64 | 195.123.235.177 |
| 80.38 | shadowsocks | 236.5 | 657.1 | 22.3 | 0.0 | 10.0 | 13.78 | 18.3 | Au1rxx-base64 | 37.19.198.243 |
| 80.3 | vless | 240.8 | 684.1 | 22.2 | 0.0 | 10.0 | 9.8 | 18.3 | Au1rxx-base64 | 79.141.172.154 |
| 79.82 | vless | 261.6 | 645.4 | 21.72 | 0.0 | 10.0 | 9.8 | 18.3 | Au1rxx-base64 | 138.124.60.146 |
| 79.25 | shadowsocks | 285.3 | 802.3 | 21.17 | 0.0 | 10.0 | 13.78 | 18.3 | Au1rxx-base64 | 37.19.198.244 |
| 79.06 | vless | 294.4 | 643.7 | 20.96 | 0.0 | 10.0 | 9.8 | 18.3 | Au1rxx-base64 | 169.40.42.168 |
| 79.04 | shadowsocks | 272.9 | 696.9 | 21.46 | 0.0 | 10.0 | 13.78 | 18.3 | Au1rxx-base64 | yyz-ca-01.blncvpn4u.cc |
| 78.98 | shadowsocks | 297.1 | 841.7 | 20.9 | 0.0 | 10.0 | 13.78 | 18.3 | Au1rxx-base64 | 37.19.198.160 |
| 78.93 | vless | 300.2 | 738.9 | 20.83 | 0.0 | 10.0 | 9.8 | 18.3 | Au1rxx-base64 | 216.152.147.28 |
| 78.68 | vless | 310.8 | 825.6 | 20.58 | 0.0 | 10.0 | 9.8 | 18.3 | Au1rxx-base64 | 169.40.42.179 |
| 78.62 | vless | 313.5 | 869.7 | 20.52 | 0.0 | 10.0 | 9.8 | 18.3 | Au1rxx-base64 | 137.184.218.169 |
| 78.31 | vless | 326.9 | 883.4 | 20.21 | 0.0 | 10.0 | 9.8 | 18.3 | Au1rxx-base64 | 169.40.42.182 |
| 78.27 | vless | 328.7 | 907.7 | 20.17 | 0.0 | 10.0 | 9.8 | 18.3 | Au1rxx-base64 | 185.95.231.156 |
| 78.16 | vless | 333.5 | 780.4 | 20.06 | 0.0 | 10.0 | 9.8 | 18.3 | Au1rxx-base64 | 169.40.42.15 |
| 78.16 | vless | 333.6 | 842.2 | 20.06 | 0.0 | 10.0 | 9.8 | 18.3 | Au1rxx-base64 | 169.40.42.184 |
| 77.98 | vless | 285.2 | 694.6 | 21.18 | 0.0 | 10.0 | 9.8 | 18.3 | Au1rxx-base64 | 167.17.69.171 |
| 77.94 | vless | 342.8 | 925.4 | 19.84 | 0.0 | 10.0 | 9.8 | 18.3 | Au1rxx-base64 | 169.40.42.231 |
| 77.83 | shadowsocks | 325.2 | 858.4 | 20.25 | 0.0 | 10.0 | 13.78 | 18.3 | Au1rxx-base64 | 38.180.135.156 |
| 77.72 | vless | 339.7 | 833.0 | 19.91 | 0.0 | 10.0 | 9.8 | 18.3 | Au1rxx-base64 | 130.107.73.148 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.921 | 0.856 | 362 | 1654 | prefer |
| ermaozi | 0.742 | 0.736 | 53 | 365 | prefer |
| Surfboard-tg-mixed | 0.694 | 0.615 | 234 | 7138 | observe |
| DeltaKronecker-all | 0.498 | 0.416 | 77 | 6421 | observe |
| mheidari-all | 0.467 | 0.385 | 117 | 15978 | observe |
| ermaozi-get_subscribe | 0.401 | 0.714 | 7 | 394 | observe |
| mahdibland-V2RayAggregator | 0.335 | 1.0 | 1 | 4251 | observe |
| 10ium-ScrapeCategorize-Vless | 0.287 | 0.5 | 2 | 5174 | observe |
| xiaoji235-airport-v2ray-all | 0.277 | 0.2 | 15 | 3625 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| Epodonios-all | 0.255 | None | 0 | 7601 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3996 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 8830 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5693 | observe |
| barry-far-vless | 0.255 | None | 0 | 5908 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 82 |
| speed | TimeoutError | - | 54 |
| geo | ClientOSError | - | 49 |
| 204 | ProxyError | - | 20 |
| speed | ClientOSError | - | 20 |
| cn-block | ClientOSError | - | 19 |
| 204 | ProxyConnectionError | - | 13 |
| cn-block | TimeoutError | - | 12 |
| 204 | TimeoutError | - | 12 |
| cn-block | ProxyError | - | 5 |
| 204 | ClientOSError | - | 2 |
| sing-box exited 1 |  [31mFATAL[0m[0000] start service: start inbound/socks[socks-in]: listen tcp 127.0.0.1:38660: bind: address already in use | - | 1 |
| 204 | ServerDisconnectedError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
