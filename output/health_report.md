# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-27 03:44:26 |
| 运行耗时 | 356.8s |
| 订阅源总数 | 107 |
| 健康订阅源 | 102 |
| 原始节点 | 83507 |
| 去重后节点 | 22089 |
| TCP 可达 | 3000 |
| 真实可用 | 1052 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22089 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.5 |
| geo | 1.2 |
| tcp | 31.4 |
| probe | 71.8 |
| real_test | 225.3 |
| generate | 21.5 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 46231 |
| trojan | 15466 |
| shadowsocks | 10596 |
| vmess | 10271 |
| hysteria2 | 613 |
| shadowsocksr | 106 |
| socks | 93 |
| http | 84 |
| anytls | 22 |
| hysteria | 13 |
| tuic | 12 |

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
| 79.45 | hysteria2 | 243.6 | 655.0 | 22.14 | 0.0 | 10.0 | 13.85 | 19.56 | Au1rxx-base64 | 159.223.157.129 |
| 79.11 | shadowsocks | 225.5 | 596.7 | 22.56 | 0.0 | 10.0 | 10.99 | 19.56 | Au1rxx-base64 | 198.98.53.130 |
| 78.66 | hysteria2 | 258.5 | 699.2 | 21.79 | 0.0 | 7.46 | 13.85 | 19.56 | Au1rxx-base64 | usa1.spectrumproxy.shop |
| 78.54 | shadowsocks | 249.9 | 672.0 | 21.99 | 0.0 | 10.0 | 10.99 | 19.56 | Au1rxx-base64 | 37.19.198.160 |
| 78.41 | shadowsocks | 255.5 | 689.9 | 21.86 | 0.0 | 10.0 | 10.99 | 19.56 | Au1rxx-base64 | 37.19.198.244 |
| 77.82 | trojan | 297.7 | 639.0 | 20.89 | 0.0 | 10.0 | 14.01 | 19.56 | Au1rxx-base64 | 163.245.196.68 |
| 77.73 | trojan | 458.7 | 1278.9 | 17.16 | 0.0 | 10.0 | 14.01 | 19.56 | Au1rxx-base64 | 153.75.250.171 |
| 76.03 | trojan | 295.6 | 641.2 | 20.94 | 0.0 | 10.0 | 14.01 | 19.56 | Au1rxx-base64 | 64.94.95.115 |
| 76.02 | shadowsocks | 272.3 | 629.9 | 21.48 | 0.0 | 10.0 | 10.99 | 19.56 | Au1rxx-base64 | 156.146.38.169 |
| 75.78 | trojan | 328.3 | 740.8 | 20.18 | 0.0 | 10.0 | 14.01 | 19.56 | Au1rxx-base64 | 64.94.95.118 |
| 75.32 | shadowsocks | 340.5 | 845.8 | 19.9 | 0.0 | 10.0 | 10.99 | 19.56 | Au1rxx-base64 | 185.196.61.82 |
| 75.22 | hysteria2 | 419.0 | 855.7 | 18.08 | 0.0 | 10.0 | 13.85 | 19.56 | Au1rxx-base64 | 5.180.97.78 |
| 74.82 | shadowsocks | 281.3 | 642.8 | 21.27 | 0.0 | 10.0 | 10.99 | 19.56 | Au1rxx-base64 | 156.146.38.170 |
| 74.5 | hysteria2 | 432.8 | 882.2 | 17.76 | 0.0 | 10.0 | 13.85 | 19.56 | Au1rxx-base64 | 5.255.102.165 |
| 73.96 | shadowsocks | 331.3 | 801.9 | 20.11 | 0.0 | 10.0 | 10.99 | 19.56 | Au1rxx-base64 | 156.146.38.168 |
| 73.71 | shadowsocks | 242.5 | 641.4 | 22.16 | 0.0 | 10.0 | 10.99 | 19.56 | Au1rxx-base64 | 37.19.198.243 |
| 72.67 | trojan | 405.6 | 972.1 | 18.39 | 0.0 | 10.0 | 14.01 | 19.56 | Au1rxx-base64 | 64.94.95.117 |
| 72.53 | hysteria2 | 507.9 | 854.3 | 16.02 | 0.0 | 10.0 | 13.85 | 19.56 | Au1rxx-base64 | 62.210.124.146 |
| 72.37 | trojan | 462.5 | 1149.2 | 17.07 | 0.0 | 10.0 | 14.01 | 19.56 | Au1rxx-base64 | 64.94.95.114 |
| 72.19 | shadowsocks | 297.7 | 595.4 | 20.89 | 0.0 | 10.0 | 10.99 | 19.56 | Au1rxx-base64 | 173.244.56.6 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.991 | 0.933 | 555 | 1476 | prefer |
| zhangkai | 0.991 | 1.0 | 76 | 86 | prefer |
| DeltaKronecker-all | 0.815 | 0.739 | 153 | 4320 | prefer |
| Surfboard-tg-mixed | 0.747 | 0.672 | 64 | 5483 | prefer |
| mheidari-all | 0.519 | 0.438 | 666 | 19312 | observe |
| tg-oneclickvpnkeys | 0.483 | 1.0 | 6 | 149 | observe |
| xiaoji235-airport-v2ray-all | 0.438 | 1.0 | 3 | 3959 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4912 | observe |
| Epodonios-all | 0.255 | None | 0 | 6493 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3963 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6284 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4173 | observe |
| barry-far-vless | 0.255 | None | 0 | 4841 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5003 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 188 |
| speed | ClientOSError | - | 155 |
| speed | TimeoutError | - | 54 |
| geo | ClientOSError | - | 34 |
| cn-block | TimeoutError | - | 23 |
| cn-block | ClientOSError | - | 6 |
| 204 | ClientOSError | - | 6 |
| 204 | ProxyError | - | 5 |
| 204 | TimeoutError | - | 4 |
| speed | ProxyError | - | 2 |
| cn-block | ProxyError | - | 1 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
