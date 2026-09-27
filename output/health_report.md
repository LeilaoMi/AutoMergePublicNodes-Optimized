# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-27 11:56:46 |
| 运行耗时 | 596.9s |
| 订阅源总数 | 107 |
| 健康订阅源 | 94 |
| 原始节点 | 95691 |
| 去重后节点 | 26593 |
| TCP 可达 | 3000 |
| 真实可用 | 418 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 26593 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.1 |
| geo | 1.4 |
| tcp | 43.4 |
| probe | 273.1 |
| real_test | 178.0 |
| generate | 93.9 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 58165 |
| vmess | 14701 |
| shadowsocks | 11300 |
| trojan | 9136 |
| hysteria2 | 1454 |
| http | 641 |
| shadowsocksr | 168 |
| socks | 77 |
| anytls | 26 |
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
| 78.96 | shadowsocks | 226.9 | 595.9 | 22.53 | 0.0 | 9.11 | 12.8 | 18.52 | Au1rxx-base64 | 198.98.53.130 |
| 78.16 | shadowsocks | 266.2 | 722.1 | 21.62 | 0.0 | 9.22 | 12.8 | 18.52 | Au1rxx-base64 | 37.19.198.244 |
| 78.08 | shadowsocks | 263.0 | 718.1 | 21.69 | 0.0 | 9.07 | 12.8 | 18.52 | Au1rxx-base64 | 37.19.198.243 |
| 77.0 | vless | 248.0 | 696.6 | 22.04 | 0.0 | 9.12 | 7.32 | 18.52 | Au1rxx-base64 | 79.141.172.154 |
| 76.92 | hysteria2 | 309.0 | 636.1 | 20.63 | 0.0 | 9.32 | 13.64 | 18.52 | Au1rxx-base64 | 66.94.121.46 |
| 75.92 | vless | 297.9 | 649.4 | 20.88 | 0.0 | 9.2 | 7.32 | 18.52 | Au1rxx-base64 | 169.40.42.202 |
| 75.84 | vless | 295.0 | 649.0 | 20.95 | 0.0 | 9.05 | 7.32 | 18.52 | Au1rxx-base64 | 169.40.42.95 |
| 75.79 | shadowsocks | 282.7 | 648.7 | 21.23 | 0.0 | 9.1 | 12.8 | 18.52 | Au1rxx-base64 | 156.146.38.167 |
| 75.75 | vless | 297.1 | 739.6 | 20.9 | 0.0 | 9.31 | 7.32 | 18.52 | Au1rxx-base64 | 66.70.179.198 |
| 75.57 | shadowsocks | 353.5 | 894.1 | 19.6 | 0.0 | 9.15 | 12.8 | 18.52 | Au1rxx-base64 | 38.180.135.156 |
| 75.12 | vless | 337.5 | 891.3 | 19.97 | 0.0 | 9.31 | 7.32 | 18.52 | Au1rxx-base64 | 169.40.42.52 |
| 75.09 | vless | 323.4 | 863.4 | 20.29 | 0.0 | 9.13 | 7.32 | 18.52 | Au1rxx-base64 | 169.40.42.133 |
| 75.09 | vless | 333.8 | 906.5 | 20.05 | 0.0 | 9.2 | 7.32 | 18.52 | Au1rxx-base64 | 185.95.231.156 |
| 75.06 | shadowsocks | 368.1 | 893.9 | 19.26 | 0.0 | 9.38 | 12.8 | 18.52 | Au1rxx-base64 | 185.156.47.97 |
| 74.64 | vless | 353.5 | 963.6 | 19.6 | 0.0 | 9.2 | 7.32 | 18.52 | Au1rxx-base64 | 185.95.231.233 |
| 74.5 | shadowsocks | 415.2 | 1075.5 | 18.17 | 0.0 | 9.01 | 12.8 | 18.52 | Au1rxx-base64 | 142.4.216.225 |
| 74.04 | vless | 330.9 | 825.5 | 20.12 | 0.0 | 9.13 | 7.32 | 18.52 | Au1rxx-base64 | 169.40.42.235 |
| 73.92 | vless | 361.2 | 848.1 | 19.42 | 0.0 | 9.05 | 7.32 | 18.52 | Au1rxx-base64 | 169.40.42.229 |
| 73.51 | vless | 365.7 | 847.7 | 19.31 | 0.0 | 9.03 | 7.32 | 18.52 | Au1rxx-base64 | 169.40.42.184 |
| 73.49 | vless | 287.9 | 709.1 | 21.11 | 0.0 | 9.13 | 7.32 | 18.52 | Au1rxx-base64 | 169.40.42.35 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.936 | 0.875 | 281 | 1589 | prefer |
| Surfboard-tg-mixed | 0.849 | 0.774 | 106 | 7025 | prefer |
| mheidari-all | 0.734 | 0.658 | 76 | 22397 | prefer |
| ermaozi | 0.505 | 0.491 | 57 | 338 | observe |
| DeltaKronecker-all | 0.418 | 0.5 | 10 | 5466 | observe |
| xiaoji235-airport-v2ray-all | 0.335 | 1.0 | 1 | 6752 | observe |
| 10ium-HighSpeed | 0.289 | 1.0 | 1 | 839 | observe |
| ermaozi-get_subscribe | 0.261 | 0.267 | 15 | 361 | observe |
| roosterkid-openproxylist-v2ray | 0.261 | 1.0 | 1 | 149 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5327 | observe |
| Epodonios-all | 0.255 | None | 0 | 7510 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3995 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 8971 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5637 | observe |
| barry-far-vless | 0.255 | None | 0 | 5862 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | ProxyError | - | 28 |
| 204 | ProxyConnectionError | - | 20 |
| 204 | TimeoutError | - | 19 |
| cn-block | TimeoutError | - | 16 |
| speed | TimeoutError | - | 15 |
| geo | TimeoutError | - | 13 |
| cn-block | ClientOSError | - | 7 |
| speed | ClientOSError | - | 7 |
| cn-block | ProxyError | - | 2 |
| geo | ClientOSError | - | 2 |
| 204 | ClientOSError | - | 1 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
