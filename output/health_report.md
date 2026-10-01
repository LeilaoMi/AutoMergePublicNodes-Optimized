# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-01 12:59:47 |
| 运行耗时 | 568.4s |
| 订阅源总数 | 107 |
| 健康订阅源 | 94 |
| 原始节点 | 98134 |
| 去重后节点 | 27405 |
| TCP 可达 | 3000 |
| 真实可用 | 417 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 27405 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.9 |
| geo | 1.6 |
| tcp | 45.3 |
| probe | 253.0 |
| real_test | 178.7 |
| generate | 82.8 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 60363 |
| vmess | 15497 |
| shadowsocks | 11364 |
| trojan | 8880 |
| hysteria2 | 1317 |
| http | 400 |
| shadowsocksr | 174 |
| socks | 64 |
| anytls | 51 |
| hysteria | 16 |
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
| 78.96 | hysteria2 | 263.5 | 574.9 | 21.68 | 0.0 | 10.0 | 14.29 | 17.44 | Au1rxx-base64 | 192.255.128.123 |
| 78.59 | shadowsocks | 249.3 | 613.4 | 22.01 | 0.0 | 10.0 | 13.14 | 17.44 | Au1rxx-base64 | 156.146.38.169 |
| 77.76 | shadowsocks | 284.9 | 737.9 | 21.18 | 0.0 | 10.0 | 13.14 | 17.44 | Au1rxx-base64 | 37.19.198.244 |
| 77.75 | shadowsocks | 285.6 | 740.8 | 21.17 | 0.0 | 10.0 | 13.14 | 17.44 | Au1rxx-base64 | 37.19.198.160 |
| 77.52 | shadowsocks | 295.3 | 747.3 | 20.94 | 0.0 | 10.0 | 13.14 | 17.44 | Au1rxx-base64 | 37.19.198.243 |
| 77.06 | vless | 228.1 | 618.2 | 22.5 | 0.0 | 10.0 | 7.12 | 17.44 | Au1rxx-base64 | 195.211.98.43 |
| 76.98 | hysteria2 | 260.4 | 694.1 | 21.75 | 0.0 | 10.0 | 14.29 | 17.44 | Au1rxx-base64 | 129.213.91.185 |
| 76.92 | shadowsocks | 256.4 | 729.1 | 21.84 | 0.0 | 10.0 | 13.14 | 17.44 | Au1rxx-base64 | 103.214.111.162 |
| 76.92 | shadowsocks | 257.6 | 633.8 | 21.82 | 0.0 | 10.0 | 13.14 | 17.44 | Au1rxx-base64 | 156.146.38.168 |
| 76.23 | vless | 264.0 | 693.0 | 21.67 | 0.0 | 10.0 | 7.12 | 17.44 | Au1rxx-base64 | 79.141.172.154 |
| 76.12 | shadowsocks | 355.8 | 929.3 | 19.54 | 0.0 | 10.0 | 13.14 | 17.44 | Au1rxx-base64 | 156.146.38.167 |
| 75.23 | vless | 302.2 | 739.8 | 20.78 | 0.0 | 10.0 | 7.12 | 17.44 | Au1rxx-base64 | 137.184.218.169 |
| 74.57 | vless | 289.9 | 701.6 | 21.07 | 0.0 | 10.0 | 7.12 | 17.44 | Au1rxx-base64 | 159.89.87.21 |
| 74.3 | vless | 272.5 | 637.8 | 21.47 | 0.0 | 10.0 | 7.12 | 17.44 | Au1rxx-base64 | 195.123.235.177 |
| 73.46 | vless | 356.8 | 884.4 | 19.52 | 0.0 | 10.0 | 7.12 | 17.44 | Au1rxx-base64 | 169.40.42.224 |
| 73.42 | shadowsocks | 256.4 | 621.6 | 21.84 | 0.0 | 10.0 | 13.14 | 17.44 | Au1rxx-base64 | 156.146.38.170 |
| 73.24 | shadowsocks | 458.6 | 1302.5 | 17.16 | 0.0 | 10.0 | 13.14 | 17.44 | Au1rxx-base64 | yyz-ca-01.blncvpn4u.cc |
| 73.04 | shadowsocks | 304.8 | 638.2 | 20.72 | 0.0 | 10.0 | 13.14 | 17.44 | Au1rxx-base64 | 149.22.95.183 |
| 72.64 | vless | 419.1 | 1081.3 | 18.08 | 0.0 | 10.0 | 7.12 | 17.44 | Au1rxx-base64 | 185.95.231.156 |
| 72.21 | vless | 263.2 | 659.1 | 21.69 | 0.0 | 10.0 | 7.12 | 17.44 | Au1rxx-base64 | 198.251.78.29 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.96 | 1.0 | 20 | 144 | prefer |
| mheidari-all | 0.887 | 0.941 | 17 | 23162 | prefer |
| Au1rxx-base64 | 0.866 | 0.797 | 310 | 1787 | prefer |
| Surfboard-tg-mixed | 0.752 | 0.675 | 117 | 7144 | prefer |
| DeltaKronecker-all | 0.537 | 0.456 | 103 | 5603 | observe |
| ermaozi | 0.479 | 1.0 | 6 | 56 | observe |
| tg-oneclickvpnkeys | 0.314 | 1.0 | 2 | 66 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5324 | observe |
| Epodonios-all | 0.255 | None | 0 | 7625 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3996 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9489 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5788 | observe |
| barry-far-vless | 0.255 | None | 0 | 6032 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4241 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 91 |
| cn-block | TimeoutError | - | 17 |
| 204 | TimeoutError | - | 14 |
| 204 | ProxyError | - | 9 |
| geo | TimeoutError | - | 9 |
| cn-block | ClientOSError | - | 9 |
| speed | TimeoutError | - | 7 |
| geo | ClientOSError | - | 2 |
| geo | ProxyError | - | 1 |
| cn-block | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
