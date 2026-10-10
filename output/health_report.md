# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-10 21:36:49 |
| 运行耗时 | 709.9s |
| 订阅源总数 | 107 |
| 健康订阅源 | 94 |
| 原始节点 | 98061 |
| 去重后节点 | 27327 |
| TCP 可达 | 3000 |
| 真实可用 | 462 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 27327 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.6 |
| geo | 1.3 |
| tcp | 46.8 |
| probe | 256.6 |
| real_test | 313.3 |
| generate | 87.1 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 57878 |
| vmess | 15839 |
| shadowsocks | 11746 |
| trojan | 10236 |
| hysteria2 | 1543 |
| http | 521 |
| shadowsocksr | 171 |
| socks | 72 |
| anytls | 32 |
| hysteria | 16 |
| tuic | 7 |

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
| 82.44 | hysteria2 | 287.6 | 729.3 | 21.12 | 0.0 | 10.0 | 13.8 | 19.02 | Au1rxx-base64 | 129.213.91.185 |
| 80.37 | shadowsocks | 236.9 | 605.9 | 22.29 | 0.0 | 10.0 | 13.06 | 19.02 | Au1rxx-base64 | 156.146.38.167 |
| 80.31 | shadowsocks | 239.5 | 608.3 | 22.23 | 0.0 | 10.0 | 13.06 | 19.02 | Au1rxx-base64 | 156.146.38.170 |
| 80.11 | shadowsocks | 248.2 | 641.7 | 22.03 | 0.0 | 10.0 | 13.06 | 19.02 | Au1rxx-base64 | 156.146.38.169 |
| 80.05 | hysteria2 | 293.5 | 285.3 | 20.98 | 4.3 | 9.62 | 13.8 | 19.02 | Au1rxx-base64 | 158.101.148.79 |
| 79.35 | shadowsocks | 281.3 | 717.3 | 21.27 | 0.0 | 10.0 | 13.06 | 19.02 | Au1rxx-base64 | 156.146.38.168 |
| 78.81 | shadowsocks | 304.3 | 746.6 | 20.73 | 0.0 | 10.0 | 13.06 | 19.02 | Au1rxx-base64 | 37.19.198.160 |
| 77.58 | hysteria2 | 293.1 | 279.4 | 20.99 | 4.52 | 7.04 | 13.8 | 19.02 | Au1rxx-base64 | open.2ml.bid |
| 77.34 | vless | 276.6 | 554.7 | 21.38 | 0.0 | 10.0 | 10.76 | 19.02 | Au1rxx-base64 | 47.251.108.158 |
| 77.32 | http | 296.2 | 608.5 | 20.92 | 0.0 | 10.0 | 14.32 | 19.2 | zhangkai | 138.199.35.198 |
| 77.25 | http | 292.0 | 594.4 | 21.02 | 0.0 | 10.0 | 14.32 | 19.2 | zhangkai | 138.199.35.216 |
| 77.1 | shadowsocks | 309.3 | 754.0 | 20.62 | 0.0 | 10.0 | 13.06 | 19.02 | Au1rxx-base64 | 37.19.198.243 |
| 77.01 | vless | 269.9 | 607.5 | 21.53 | 0.0 | 10.0 | 10.76 | 19.02 | Au1rxx-base64 | 172.245.253.16 |
| 76.33 | shadowsocks | 306.5 | 753.3 | 20.68 | 0.0 | 10.0 | 13.06 | 19.02 | Au1rxx-base64 | 37.19.198.244 |
| 76.27 | shadowsocks | 306.0 | 817.6 | 20.69 | 0.0 | 10.0 | 13.06 | 19.02 | Au1rxx-base64 | 66.23.205.83 |
| 76.0 | vless | 291.4 | 590.5 | 21.03 | 0.0 | 10.0 | 10.76 | 19.02 | Au1rxx-base64 | 45.32.69.110 |
| 75.83 | vless | 347.9 | 731.9 | 19.72 | 0.0 | 10.0 | 10.76 | 19.02 | Au1rxx-base64 | 169.40.42.179 |
| 75.76 | vless | 409.1 | 1027.9 | 18.31 | 0.0 | 10.0 | 10.76 | 19.02 | Au1rxx-base64 | 185.95.231.156 |
| 75.71 | vless | 392.6 | 950.8 | 18.69 | 0.0 | 10.0 | 10.76 | 19.02 | Au1rxx-base64 | 159.89.87.21 |
| 75.49 | vless | 260.3 | 605.6 | 21.75 | 0.0 | 10.0 | 10.76 | 17.96 | mheidari-all | 195.211.98.43 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.983 | 0.911 | 381 | 1850 | prefer |
| zhangkai | 0.966 | 1.0 | 23 | 144 | prefer |
| mheidari-all | 0.797 | 0.721 | 111 | 23925 | prefer |
| Surfboard-tg-mixed | 0.489 | 0.833 | 6 | 7118 | observe |
| ermaozi-get_subscribe | 0.3 | 0.263 | 19 | 580 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| DeltaKronecker-all | 0.259 | 0.333 | 3 | 5009 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4999 | observe |
| Epodonios-all | 0.255 | None | 0 | 7597 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9340 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5677 | observe |
| barry-far-vless | 0.255 | None | 0 | 5914 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4347 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | ProxyError | - | 17 |
| cn-block | TimeoutError | - | 17 |
| speed | ClientOSError | - | 11 |
| speed | TimeoutError | - | 9 |
| 204 | TimeoutError | - | 9 |
| geo | ClientOSError | - | 7 |
| 204 | ClientOSError | - | 4 |
| cn-block | ClientOSError | - | 4 |
| cn-block | ProxyError | - | 2 |
| geo | TimeoutError | - | 2 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
