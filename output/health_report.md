# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-19 03:30:07 |
| 运行耗时 | 299.1s |
| 订阅源总数 | 107 |
| 健康订阅源 | 100 |
| 原始节点 | 88550 |
| 去重后节点 | 23429 |
| TCP 可达 | 3000 |
| 真实可用 | 804 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23429 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.1 |
| geo | 1.0 |
| tcp | 33.8 |
| probe | 59.1 |
| real_test | 172.8 |
| generate | 27.3 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 51441 |
| trojan | 15198 |
| vmess | 10884 |
| shadowsocks | 10467 |
| hysteria2 | 293 |
| shadowsocksr | 128 |
| socks | 62 |
| http | 56 |
| hysteria | 15 |
| tuic | 5 |
| anytls | 1 |

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
| 76.85 | shadowsocks | 252.0 | 614.3 | 21.94 | 0.0 | 8.83 | 11.74 | 18.34 | Au1rxx-base64 | 156.146.38.168 |
| 76.8 | shadowsocks | 254.7 | 626.8 | 21.88 | 0.0 | 8.84 | 11.74 | 18.34 | Au1rxx-base64 | 156.146.38.169 |
| 76.69 | shadowsocks | 260.3 | 645.5 | 21.75 | 0.0 | 8.86 | 11.74 | 18.34 | Au1rxx-base64 | 37.19.198.236 |
| 76.59 | shadowsocks | 264.6 | 660.2 | 21.65 | 0.0 | 8.86 | 11.74 | 18.34 | Au1rxx-base64 | 37.19.198.160 |
| 76.22 | shadowsocks | 258.2 | 638.9 | 21.8 | 0.0 | 8.83 | 11.74 | 18.34 | Au1rxx-base64 | 156.146.38.167 |
| 75.88 | shadowsocks | 261.2 | 641.5 | 21.73 | 0.0 | 8.83 | 11.74 | 18.34 | Au1rxx-base64 | 156.146.38.170 |
| 75.01 | shadowsocks | 311.4 | 853.8 | 20.57 | 0.0 | 8.86 | 11.74 | 18.34 | Au1rxx-base64 | 50.114.177.235 |
| 73.38 | trojan | 370.3 | 925.1 | 19.21 | 0.0 | 10.0 | 14.33 | 14.86 | mheidari-all | 64.94.95.118 |
| 72.9 | shadowsocks | 278.0 | 680.8 | 21.34 | 0.0 | 10.0 | 11.74 | 14.86 | mheidari-all | 108.181.57.93 |
| 72.33 | trojan | 459.7 | 1285.9 | 17.14 | 0.0 | 10.0 | 14.33 | 14.86 | mheidari-all | 148.72.168.35 |
| 71.96 | trojan | 366.3 | 504.3 | 19.3 | 0.0 | 10.0 | 14.33 | 17.38 | Surfboard-tg-mixed | 188.114.98.0 |
| 71.21 | shadowsocks | 303.0 | 635.9 | 20.76 | 0.0 | 8.83 | 11.74 | 18.34 | Au1rxx-base64 | 149.22.95.183 |
| 71.02 | vmess | 416.2 | 1136.0 | 18.14 | 0.0 | 10.0 | 10.0 | 17.38 | Surfboard-tg-mixed | 67.220.95.3 |
| 70.69 | shadowsocks | 292.1 | 591.3 | 21.02 | 0.0 | 8.82 | 11.74 | 18.34 | Au1rxx-base64 | 173.244.56.6 |
| 70.65 | trojan | 397.4 | 604.9 | 18.58 | 0.0 | 10.0 | 14.33 | 17.38 | Surfboard-tg-mixed | 162.159.32.29 |
| 70.0 | trojan | 447.2 | 499.5 | 17.42 | 0.0 | 10.0 | 14.33 | 17.38 | Surfboard-tg-mixed | 104.17.148.22 |
| 69.88 | trojan | 486.4 | 804.3 | 16.52 | 0.0 | 10.0 | 14.33 | 17.38 | Surfboard-tg-mixed | 104.18.152.219 |
| 69.77 | trojan | 487.4 | 808.5 | 16.49 | 0.0 | 10.0 | 14.33 | 17.38 | Surfboard-tg-mixed | 198.62.62.23 |
| 69.77 | trojan | 492.1 | 815.9 | 16.39 | 0.0 | 10.0 | 14.33 | 17.38 | Surfboard-tg-mixed | 104.16.174.12 |
| 69.62 | trojan | 496.4 | 833.9 | 16.29 | 0.0 | 10.0 | 14.33 | 17.38 | Surfboard-tg-mixed | 104.18.152.77 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.976 | 1.0 | 36 | 61 | prefer |
| Au1rxx-base64 | 0.711 | 0.711 | 76 | 149 | prefer |
| mheidari-all | 0.694 | 0.614 | 653 | 20126 | observe |
| Surfboard-tg-mixed | 0.682 | 0.603 | 350 | 5442 | observe |
| DeltaKronecker-all | 0.544 | 0.464 | 209 | 9946 | observe |
| xiaoji235-airport-v2ray-all | 0.372 | 0.444 | 9 | 4642 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4371 | observe |
| Epodonios-all | 0.255 | None | 0 | 6663 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3970 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7072 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4204 | observe |
| barry-far-vless | 0.255 | None | 0 | 4859 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5340 | observe |
| nscl5-all | 0.255 | None | 0 | 2755 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 280 |
| geo | TimeoutError | - | 89 |
| geo | ClientOSError | - | 78 |
| speed | TimeoutError | - | 30 |
| cn-block | TimeoutError | - | 23 |
| 204 | ProxyError | - | 13 |
| 204 | TimeoutError | - | 6 |
| cn-block | ClientOSError | - | 6 |
| 204 | ClientOSError | - | 3 |
| cn-block | ProxyError | - | 2 |
| sing-box exited 1 |  [31mFATAL[0m[0000] start service: start inbound/socks[socks-in]: listen tcp 127.0.0.1:44792: bind: address already in use | - | 1 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
