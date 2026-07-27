# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-27 19:47:37 |
| 运行耗时 | 311.2s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 85905 |
| 去重后节点 | 22931 |
| TCP 可达 | 3000 |
| 真实可用 | 712 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22931 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.7 |
| geo | 1.4 |
| tcp | 31.7 |
| probe | 65.2 |
| real_test | 169.4 |
| generate | 37.9 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 49138 |
| trojan | 15528 |
| vmess | 10394 |
| shadowsocks | 9897 |
| hysteria2 | 680 |
| shadowsocksr | 105 |
| socks | 66 |
| http | 63 |
| hysteria | 15 |
| anytls | 11 |
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
| 82.03 | hysteria2 | 263.4 | 671.8 | 21.68 | 0.0 | 10.0 | 12.69 | 19.76 | Au1rxx-base64 | 159.223.157.129 |
| 80.93 | shadowsocks | 260.1 | 649.1 | 21.76 | 0.0 | 10.0 | 13.41 | 19.76 | Au1rxx-base64 | 37.19.198.160 |
| 80.16 | shadowsocks | 268.9 | 677.0 | 21.55 | 0.0 | 10.0 | 13.41 | 19.76 | Au1rxx-base64 | 37.19.198.244 |
| 78.69 | shadowsocks | 335.1 | 854.5 | 20.02 | 0.0 | 10.0 | 13.41 | 19.76 | Au1rxx-base64 | 185.196.61.82 |
| 78.61 | hysteria2 | 269.5 | 682.1 | 21.54 | 0.0 | 7.62 | 12.69 | 19.76 | Au1rxx-base64 | usa1.spectrumproxy.shop |
| 77.74 | shadowsocks | 397.9 | 1064.2 | 18.57 | 0.0 | 10.0 | 13.41 | 19.76 | Au1rxx-base64 | 156.146.38.170 |
| 76.32 | trojan | 435.8 | 1127.2 | 17.69 | 0.0 | 10.0 | 12.71 | 19.76 | Au1rxx-base64 | 64.94.95.117 |
| 75.99 | shadowsocks | 456.1 | 1221.8 | 17.22 | 0.0 | 10.0 | 13.41 | 19.76 | Au1rxx-base64 | 156.146.38.169 |
| 75.88 | trojan | 459.2 | 1189.8 | 17.15 | 0.0 | 10.0 | 12.71 | 19.76 | Au1rxx-base64 | 64.94.95.114 |
| 75.65 | trojan | 434.0 | 1122.4 | 17.73 | 0.0 | 10.0 | 12.71 | 19.76 | Au1rxx-base64 | 64.94.95.115 |
| 75.61 | trojan | 467.3 | 1219.8 | 16.96 | 0.0 | 10.0 | 12.71 | 19.76 | Au1rxx-base64 | 64.94.95.118 |
| 75.18 | shadowsocks | 334.1 | 711.0 | 20.04 | 0.0 | 10.0 | 13.41 | 19.76 | Au1rxx-base64 | 108.181.57.93 |
| 75.13 | trojan | 449.3 | 1139.7 | 17.38 | 0.0 | 10.0 | 12.71 | 19.76 | Au1rxx-base64 | 163.245.196.68 |
| 74.8 | shadowsocks | 313.2 | 600.3 | 20.53 | 0.0 | 10.0 | 13.41 | 19.76 | Au1rxx-base64 | 173.244.56.6 |
| 74.36 | shadowsocks | 302.2 | 613.4 | 20.78 | 0.0 | 10.0 | 13.41 | 19.76 | Au1rxx-base64 | 173.244.56.9 |
| 74.21 | shadowsocks | 312.8 | 857.5 | 20.54 | 0.0 | 10.0 | 13.41 | 19.76 | Au1rxx-base64 | 50.114.177.134 |
| 73.99 | hysteria2 | 375.5 | 701.1 | 19.09 | 0.0 | 9.81 | 12.69 | 19.76 | Au1rxx-base64 | 62.210.124.146 |
| 73.88 | shadowsocks | 521.3 | 1431.1 | 15.71 | 0.0 | 10.0 | 13.41 | 19.76 | Au1rxx-base64 | 37.19.198.243 |
| 72.67 | shadowsocks | 487.3 | 1325.8 | 16.5 | 0.0 | 10.0 | 13.41 | 19.76 | Au1rxx-base64 | 37.19.198.236 |
| 72.4 | hysteria2 | 459.9 | 902.6 | 17.13 | 0.0 | 9.95 | 12.69 | 19.76 | Au1rxx-base64 | 5.255.102.165 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.987 | 1.0 | 59 | 74 | prefer |
| Au1rxx-base64 | 0.975 | 0.917 | 446 | 1499 | prefer |
| DeltaKronecker-all | 0.672 | 0.594 | 69 | 5643 | observe |
| mheidari-all | 0.627 | 0.547 | 358 | 19371 | observe |
| xiaoji235-airport-v2ray-all | 0.349 | 0.667 | 3 | 3959 | observe |
| Surfboard-tg-mixed | 0.326 | 0.267 | 15 | 5739 | observe |
| tg-Farah_VPN | 0.263 | 1.0 | 1 | 200 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4831 | observe |
| Epodonios-all | 0.255 | None | 0 | 6710 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3964 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6251 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4648 | observe |
| barry-far-vless | 0.255 | None | 0 | 5170 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4997 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 94 |
| speed | ClientOSError | - | 59 |
| 204 | TimeoutError | - | 19 |
| cn-block | TimeoutError | - | 16 |
| geo | ClientOSError | - | 15 |
| cn-block | ClientOSError | - | 11 |
| speed | TimeoutError | - | 10 |
| 204 | ProxyError | - | 6 |
| 204 | ClientOSError | - | 5 |
| cn-block | ProxyError | - | 3 |
| geo | ProxyError | - | 2 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
