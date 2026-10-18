# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-18 04:50:47 |
| 运行耗时 | 329.2s |
| 订阅源总数 | 107 |
| 健康订阅源 | 93 |
| 原始节点 | 99074 |
| 去重后节点 | 27914 |
| TCP 可达 | 3000 |
| 真实可用 | 512 |
| Verified 输出 | 130 |
| Global 输出 | 300 |
| All 输出 | 27914 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.2 |
| geo | 1.5 |
| tcp | 88.6 |
| probe | 88.9 |
| real_test | 97.6 |
| china_check | 32.5 |
| write_verified | 0.1 |
| generate | 13.0 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 58344 |
| vmess | 16758 |
| shadowsocks | 11771 |
| trojan | 9850 |
| hysteria2 | 1311 |
| http | 757 |
| shadowsocksr | 171 |
| socks | 65 |
| anytls | 24 |
| hysteria | 17 |
| tuic | 6 |

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
| 94.19 | shadowsocks | 241.8 | 1.3 | 22.18 | 14.95 | 10.0 | 13.32 | 17.74 | Au1rxx-base64 | 156.146.38.169 |
| 92.13 | shadowsocks | 241.6 | 2.9 | 22.18 | 14.89 | 10.0 | 13.32 | 17.74 | Au1rxx-base64 | 156.146.38.168 |
| 89.05 | shadowsocks | 331.6 | 1.2 | 20.1 | 14.95 | 10.0 | 13.32 | 17.74 | Au1rxx-base64 | 37.19.198.244 |
| 89.01 | vless | 296.5 | 8.4 | 20.91 | 14.69 | 5.7 | 10.65 | 17.74 | Au1rxx-base64 | 147.45.60.160 |
| 88.92 | shadowsocks | 272.0 | 4.2 | 21.48 | 14.84 | 8.91 | 13.32 | 17.74 | Au1rxx-base64 | 173.244.56.9 |
| 88.01 | shadowsocks | 362.2 | 1.8 | 19.39 | 14.93 | 9.99 | 13.32 | 17.74 | Au1rxx-base64 | 37.19.198.160 |
| 87.96 | shadowsocks | 333.4 | 2.5 | 20.06 | 14.9 | 10.0 | 13.32 | 17.74 | Au1rxx-base64 | 37.19.198.243 |
| 87.09 | vless | 248.7 | 1.2 | 22.02 | 14.95 | 3.74 | 10.65 | 17.74 | Au1rxx-base64 | 45.32.69.110 |
| 86.2 | vless | 321.8 | 7.2 | 20.33 | 14.73 | 10.0 | 10.65 | 17.74 | Au1rxx-base64 | 69.48.201.136 |
| 85.88 | vless | 230.4 | 2.5 | 22.44 | 14.9 | 3.74 | 10.65 | 17.74 | Au1rxx-base64 | 47.251.25.74 |
| 85.85 | hysteria2 | 239.3 | 3.5 | 22.24 | 14.87 | 0.0 | 12.0 | 17.74 | Au1rxx-base64 | 66.94.121.46 |
| 85.48 | shadowsocks | 359.9 | 3.5 | 19.45 | 14.87 | 10.0 | 13.32 | 17.74 | Au1rxx-base64 | 103.11.76.248 |
| 85.25 | vless | 278.9 | 0.2 | 21.32 | 14.99 | 5.71 | 10.65 | 17.74 | Au1rxx-base64 | 176.122.183.26 |
| 85.0 | shadowsocks | 273.0 | 2.4 | 21.46 | 14.91 | 10.0 | 13.32 | 17.74 | Au1rxx-base64 | 173.244.56.6 |
| 84.91 | trojan | 364.9 | 0.3 | 19.33 | 14.99 | 9.66 | 13.45 | 17.74 | Au1rxx-base64 | 108.61.186.37 |
| 84.69 | shadowsocks | 303.3 | 0.9 | 20.76 | 14.97 | 9.67 | 13.32 | 17.74 | Au1rxx-base64 | 149.22.87.240 |
| 84.65 | vless | 270.0 | 1.1 | 21.53 | 14.96 | 5.71 | 10.65 | 17.74 | Au1rxx-base64 | 67.209.184.133 |
| 84.5 | vless | 316.0 | 0.4 | 20.46 | 14.98 | 3.64 | 10.65 | 17.74 | Au1rxx-base64 | 208.84.100.209 |
| 84.38 | vless | 324.1 | 8.6 | 20.28 | 14.68 | 5.45 | 10.65 | 17.74 | Au1rxx-base64 | 154.9.241.170 |
| 84.36 | shadowsocks | 330.1 | 0.1 | 20.14 | 15.0 | 9.65 | 13.32 | 17.74 | Au1rxx-base64 | 149.22.87.204 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.989 | 0.97 | 99 | 710 | prefer |
| Au1rxx-base64 | 0.948 | 0.879 | 413 | 1776 | prefer |
| Surfboard-tg-mixed | 0.643 | 0.9 | 10 | 7181 | observe |
| DeltaKronecker-all | 0.519 | 1.0 | 5 | 4999 | observe |
| Surfboard-tg-vless | 0.372 | 0.444 | 9 | 5616 | observe |
| mheidari-all | 0.358 | 0.275 | 142 | 23946 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4986 | observe |
| Epodonios-all | 0.255 | None | 0 | 7667 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9903 | observe |
| barry-far-vless | 0.255 | None | 0 | 5884 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4295 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |
| Au1rxx-clash | 0.246 | None | 0 | 1776 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 104 |
| geo | ClientOSError | - | 23 |
| speed | ClientOSError | - | 14 |
| 204 | ProxyError | - | 7 |
| 204 | TimeoutError | - | 7 |
| cn-block | ClientOSError | - | 5 |
| cn-block | ProxyError | - | 2 |
| geo | ProxyError | - | 1 |
| 204 | ClientOSError | - | 1 |
| cn-block | TimeoutError | - | 1 |
| speed | TimeoutError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 66 | 130 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
