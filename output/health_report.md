# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-02 12:24:09 |
| 运行耗时 | 632.7s |
| 订阅源总数 | 107 |
| 健康订阅源 | 94 |
| 原始节点 | 97754 |
| 去重后节点 | 26970 |
| TCP 可达 | 3000 |
| 真实可用 | 392 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 26970 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.5 |
| geo | 1.5 |
| tcp | 46.3 |
| probe | 272.6 |
| real_test | 235.5 |
| generate | 71.2 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 59633 |
| vmess | 15413 |
| shadowsocks | 11463 |
| trojan | 8909 |
| hysteria2 | 1524 |
| http | 521 |
| shadowsocksr | 169 |
| socks | 60 |
| anytls | 35 |
| hysteria | 17 |
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
| 84.72 | hysteria2 | 264.3 | 657.2 | 21.66 | 0.0 | 10.0 | 14.42 | 19.74 | Au1rxx-base64 | 159.223.157.129 |
| 81.31 | shadowsocks | 252.3 | 705.9 | 21.94 | 0.0 | 10.0 | 13.63 | 19.74 | Au1rxx-base64 | 37.19.198.160 |
| 80.75 | shadowsocks | 233.1 | 634.4 | 22.38 | 0.0 | 10.0 | 13.63 | 19.74 | Au1rxx-base64 | 198.98.53.130 |
| 80.19 | hysteria2 | 289.9 | 572.0 | 21.07 | 0.0 | 10.0 | 14.42 | 19.74 | Au1rxx-base64 | 192.255.128.123 |
| 79.12 | shadowsocks | 260.2 | 719.6 | 21.75 | 0.0 | 10.0 | 13.63 | 19.74 | Au1rxx-base64 | 37.19.198.236 |
| 78.45 | shadowsocks | 354.0 | 891.7 | 19.58 | 0.0 | 10.0 | 13.63 | 19.74 | Au1rxx-base64 | 185.156.47.97 |
| 78.11 | vless | 257.8 | 706.4 | 21.81 | 0.0 | 10.0 | 6.56 | 19.74 | Au1rxx-base64 | 159.89.87.21 |
| 78.08 | shadowsocks | 311.4 | 859.7 | 20.57 | 0.0 | 10.0 | 13.63 | 18.38 | Surfboard-tg-mixed | 15.204.247.206 |
| 77.91 | shadowsocks | 377.6 | 898.3 | 19.04 | 0.0 | 10.0 | 13.63 | 19.74 | Au1rxx-base64 | 51.222.200.165 |
| 77.83 | shadowsocks | 280.9 | 646.2 | 21.28 | 0.0 | 10.0 | 13.63 | 19.74 | Au1rxx-base64 | 156.146.38.167 |
| 77.74 | vless | 273.9 | 695.8 | 21.44 | 0.0 | 10.0 | 6.56 | 19.74 | Au1rxx-base64 | 66.70.179.198 |
| 77.35 | shadowsocks | 283.5 | 657.5 | 21.21 | 0.0 | 10.0 | 13.63 | 18.38 | Surfboard-tg-mixed | 156.146.38.169 |
| 77.25 | hysteria2 | 362.6 | 624.3 | 19.38 | 0.0 | 9.68 | 14.42 | 19.74 | Au1rxx-base64 | 66.94.121.46 |
| 77.01 | shadowsocks | 280.0 | 651.1 | 21.3 | 0.0 | 10.0 | 13.63 | 18.38 | Surfboard-tg-mixed | 156.146.38.168 |
| 77.0 | hysteria2 | 451.1 | 749.8 | 17.34 | 0.0 | 10.0 | 14.42 | 19.74 | Au1rxx-base64 | 129.213.91.185 |
| 76.51 | vless | 326.8 | 871.3 | 20.21 | 0.0 | 10.0 | 6.56 | 19.74 | Au1rxx-base64 | 169.40.42.232 |
| 76.29 | shadowsocks | 278.7 | 707.7 | 21.33 | 0.0 | 10.0 | 13.63 | 19.74 | Au1rxx-base64 | 138.199.48.82 |
| 76.22 | shadowsocks | 295.1 | 697.2 | 20.95 | 0.0 | 10.0 | 13.63 | 19.74 | Au1rxx-base64 | 66.23.201.172 |
| 76.02 | hysteria2 | 420.0 | 861.0 | 18.06 | 0.0 | 10.0 | 14.42 | 19.74 | Au1rxx-base64 | 5.129.235.85 |
| 75.78 | hysteria2 | 401.0 | 692.5 | 18.5 | 0.0 | 10.0 | 14.42 | 19.74 | Au1rxx-base64 | 62.210.124.146 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.893 | 0.828 | 291 | 1673 | prefer |
| ermaozi | 0.871 | 0.875 | 24 | 618 | prefer |
| mheidari-all | 0.817 | 0.745 | 55 | 23059 | prefer |
| Surfboard-tg-mixed | 0.76 | 0.683 | 123 | 7176 | prefer |
| DeltaKronecker-all | 0.337 | 0.429 | 7 | 4981 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5276 | observe |
| Epodonios-all | 0.255 | None | 0 | 7676 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| Pawdroid | 0.255 | 1.0 | 1 | 12 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9234 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5828 | observe |
| barry-far-vless | 0.255 | None | 0 | 6070 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4310 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| cn-block | TimeoutError | - | 32 |
| 204 | TimeoutError | - | 22 |
| speed | ClientOSError | - | 12 |
| speed | TimeoutError | - | 11 |
| 204 | ProxyError | - | 9 |
| cn-block | ClientOSError | - | 8 |
| geo | TimeoutError | - | 6 |
| 204 | ClientOSError | - | 4 |
| cn-block | ProxyError | - | 2 |
| geo | ClientOSError | - | 2 |
| geo | ProxyError | - | 2 |
| sing-box exited 1 |  [31mFATAL[0m[0000] start service: start inbound/socks[socks-in]: listen tcp 127.0.0.1:44860: bind: address already in use | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
