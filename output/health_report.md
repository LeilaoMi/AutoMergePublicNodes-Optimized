# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-27 21:19:18 |
| 运行耗时 | 562.8s |
| 订阅源总数 | 107 |
| 健康订阅源 | 94 |
| 原始节点 | 96200 |
| 去重后节点 | 26757 |
| TCP 可达 | 3000 |
| 真实可用 | 412 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 26757 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.2 |
| geo | 1.5 |
| tcp | 43.0 |
| probe | 216.4 |
| real_test | 203.6 |
| generate | 91.1 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 58740 |
| vmess | 14864 |
| shadowsocks | 11361 |
| trojan | 8922 |
| hysteria2 | 1451 |
| http | 573 |
| shadowsocksr | 170 |
| socks | 72 |
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
| 81.0 | vless | 252.4 | 712.0 | 21.94 | 0.0 | 10.0 | 11.06 | 18.0 | Au1rxx-base64 | 47.253.226.114 |
| 79.8 | vless | 249.5 | 702.0 | 22.0 | 0.0 | 8.74 | 11.06 | 18.0 | Au1rxx-base64 | 79.141.172.154 |
| 79.13 | vless | 284.3 | 716.6 | 21.2 | 0.0 | 8.87 | 11.06 | 18.0 | Au1rxx-base64 | 66.70.179.198 |
| 78.97 | vless | 245.9 | 690.6 | 22.09 | 0.0 | 8.82 | 11.06 | 18.0 | Au1rxx-base64 | 47.253.144.114 |
| 78.97 | vless | 286.0 | 763.2 | 21.16 | 0.0 | 8.75 | 11.06 | 18.0 | Au1rxx-base64 | 169.40.42.232 |
| 78.78 | vless | 267.3 | 711.7 | 21.59 | 0.0 | 8.75 | 11.06 | 18.0 | Au1rxx-base64 | 169.40.42.16 |
| 78.74 | vless | 296.9 | 657.3 | 20.9 | 0.0 | 8.78 | 11.06 | 18.0 | Au1rxx-base64 | 169.40.42.35 |
| 78.63 | vless | 300.7 | 680.3 | 20.82 | 0.0 | 8.75 | 11.06 | 18.0 | Au1rxx-base64 | 169.40.42.231 |
| 78.62 | vless | 303.1 | 694.6 | 20.76 | 0.0 | 8.8 | 11.06 | 18.0 | Au1rxx-base64 | 169.40.42.104 |
| 78.4 | vless | 310.5 | 843.1 | 20.59 | 0.0 | 8.75 | 11.06 | 18.0 | Au1rxx-base64 | 169.40.42.184 |
| 78.34 | vless | 315.4 | 855.4 | 20.48 | 0.0 | 8.8 | 11.06 | 18.0 | Au1rxx-base64 | 169.40.42.163 |
| 78.32 | shadowsocks | 219.7 | 589.8 | 22.69 | 0.0 | 10.0 | 12.93 | 16.7 | Surfboard-tg-mixed | 198.98.53.130 |
| 78.25 | vless | 261.0 | 636.0 | 21.74 | 0.0 | 8.75 | 11.06 | 18.0 | Au1rxx-base64 | 195.211.98.43 |
| 78.05 | vless | 327.8 | 820.4 | 20.19 | 0.0 | 8.8 | 11.06 | 18.0 | Au1rxx-base64 | 169.40.42.212 |
| 77.98 | vless | 242.1 | 680.5 | 22.17 | 0.0 | 8.75 | 11.06 | 18.0 | Au1rxx-base64 | 47.90.153.88 |
| 77.76 | vless | 340.2 | 868.2 | 19.9 | 0.0 | 8.8 | 11.06 | 18.0 | Au1rxx-base64 | 169.40.42.179 |
| 77.65 | vless | 348.1 | 950.2 | 19.72 | 0.0 | 8.87 | 11.06 | 18.0 | Au1rxx-base64 | 169.40.42.74 |
| 77.58 | vless | 347.2 | 819.8 | 19.74 | 0.0 | 8.78 | 11.06 | 18.0 | Au1rxx-base64 | 169.40.42.229 |
| 77.54 | vless | 353.1 | 970.4 | 19.61 | 0.0 | 8.87 | 11.06 | 18.0 | Au1rxx-base64 | 185.95.231.233 |
| 77.5 | shadowsocks | 255.2 | 711.5 | 21.87 | 0.0 | 10.0 | 12.93 | 16.7 | Surfboard-tg-mixed | 37.19.198.160 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.895 | 0.831 | 261 | 1652 | prefer |
| Surfboard-tg-mixed | 0.839 | 0.762 | 164 | 7018 | prefer |
| mheidari-all | 0.798 | 0.725 | 69 | 22680 | prefer |
| ermaozi | 0.471 | 0.457 | 35 | 289 | observe |
| DeltaKronecker-all | 0.373 | 0.6 | 5 | 5466 | observe |
| xiaoji235-airport-v2ray-all | 0.335 | 1.0 | 1 | 6752 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5327 | observe |
| Epodonios-all | 0.255 | None | 0 | 7540 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9353 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5592 | observe |
| barry-far-vless | 0.255 | None | 0 | 5823 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4185 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.241 | None | 0 | 1652 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| cn-block | TimeoutError | - | 26 |
| 204 | TimeoutError | - | 25 |
| 204 | ProxyConnectionError | - | 16 |
| speed | ClientOSError | - | 14 |
| speed | TimeoutError | - | 10 |
| cn-block | ClientOSError | - | 9 |
| geo | TimeoutError | - | 9 |
| 204 | ProxyError | - | 6 |
| 204 | ClientOSError | - | 4 |
| geo | ProxyError | - | 2 |
| sing-box exited 1 |  [31mFATAL[0m[0000] start service: start inbound/socks[socks-in]: listen tcp 127.0.0.1:35366: bind: address already in use | - | 1 |
| speed | ProxyError | - | 1 |
| cn-block | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
