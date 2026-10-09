# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-09 13:10:17 |
| 运行耗时 | 880.4s |
| 订阅源总数 | 107 |
| 健康订阅源 | 94 |
| 原始节点 | 98198 |
| 去重后节点 | 27459 |
| TCP 可达 | 3000 |
| 真实可用 | 414 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 27459 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 8.1 |
| geo | 1.5 |
| tcp | 47.1 |
| probe | 358.2 |
| real_test | 367.9 |
| generate | 97.5 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 57722 |
| vmess | 15607 |
| shadowsocks | 11983 |
| trojan | 10661 |
| hysteria2 | 1482 |
| http | 437 |
| shadowsocksr | 166 |
| socks | 80 |
| anytls | 30 |
| hysteria | 17 |
| tuic | 13 |

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
| 85.99 | hysteria2 | 231.2 | 243.0 | 22.43 | 5.89 | 10.0 | 14.48 | 19.64 | Au1rxx-base64 | 158.101.148.79 |
| 84.0 | hysteria2 | 224.6 | 213.1 | 22.58 | 7.01 | 6.87 | 14.48 | 19.64 | Au1rxx-base64 | open.2ml.bid |
| 82.05 | shadowsocks | 210.9 | 571.6 | 22.9 | 0.0 | 10.0 | 13.51 | 19.64 | Au1rxx-base64 | 149.22.95.183 |
| 80.37 | hysteria2 | 333.1 | 788.1 | 20.07 | 0.0 | 10.0 | 14.48 | 19.64 | Au1rxx-base64 | 66.94.121.46 |
| 78.56 | vless | 209.8 | 545.9 | 22.92 | 0.0 | 10.0 | 6.0 | 19.64 | Au1rxx-base64 | 15.204.97.216 |
| 78.38 | vless | 217.7 | 558.9 | 22.74 | 0.0 | 10.0 | 6.0 | 19.64 | Au1rxx-base64 | 15.204.97.197 |
| 76.39 | trojan | 311.9 | 317.9 | 20.56 | 3.08 | 10.0 | 13.47 | 19.64 | Au1rxx-base64 | 45.32.52.173 |
| 76.38 | trojan | 253.9 | 574.9 | 21.9 | 0.0 | 10.0 | 13.47 | 19.64 | Au1rxx-base64 | 34.220.15.24 |
| 76.36 | trojan | 271.7 | 692.7 | 21.49 | 0.0 | 9.26 | 13.47 | 19.64 | Au1rxx-base64 | alert-titmouse.rooster465.autos |
| 75.94 | shadowsocks | 267.4 | 557.1 | 21.59 | 0.0 | 10.0 | 13.51 | 19.64 | Au1rxx-base64 | 108.181.0.177 |
| 75.94 | shadowsocks | 291.7 | 328.6 | 21.02 | 2.68 | 10.0 | 13.51 | 19.64 | Au1rxx-base64 | 149.22.87.240 |
| 75.74 | shadowsocks | 264.2 | 734.3 | 21.66 | 0.0 | 10.0 | 13.51 | 19.64 | Au1rxx-base64 | 5.78.51.123 |
| 75.52 | hysteria2 | 348.3 | 768.4 | 19.71 | 0.0 | 10.0 | 14.48 | 19.64 | Au1rxx-base64 | 129.213.91.185 |
| 74.92 | trojan | 342.9 | 291.8 | 19.84 | 4.06 | 8.92 | 13.47 | 19.64 | Au1rxx-base64 | musical-terrier.rooster465.autos |
| 74.53 | vless | 268.3 | 573.9 | 21.57 | 0.0 | 10.0 | 6.0 | 19.64 | Au1rxx-base64 | 144.202.126.147 |
| 74.29 | trojan | 395.6 | 297.7 | 18.62 | 3.83 | 9.41 | 13.47 | 19.64 | Au1rxx-base64 | obliging-louse.rooster465.autos |
| 73.45 | trojan | 379.7 | 1013.2 | 18.99 | 0.0 | 8.85 | 13.47 | 19.64 | Au1rxx-base64 | pro-mako.rooster465.autos |
| 73.39 | vless | 217.2 | 565.0 | 22.75 | 0.0 | 10.0 | 6.0 | 19.64 | Au1rxx-base64 | 15.204.97.219 |
| 72.37 | shadowsocks | 390.4 | 821.5 | 18.74 | 0.0 | 10.0 | 13.51 | 19.64 | Au1rxx-base64 | 37.19.198.160 |
| 72.3 | shadowsocks | 392.8 | 823.5 | 18.68 | 0.0 | 10.0 | 13.51 | 19.64 | Au1rxx-base64 | 37.19.198.236 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.984 | 0.915 | 293 | 1810 | prefer |
| zhangkai | 0.966 | 1.0 | 23 | 144 | prefer |
| mheidari-all | 0.803 | 0.733 | 45 | 23165 | prefer |
| Surfboard-tg-mixed | 0.68 | 0.604 | 53 | 7139 | observe |
| DeltaKronecker-all | 0.472 | 0.391 | 128 | 5154 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4984 | observe |
| Epodonios-all | 0.255 | None | 0 | 7541 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 10038 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5578 | observe |
| barry-far-vless | 0.255 | None | 0 | 5830 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4362 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |
| Au1rxx-clash | 0.247 | None | 0 | 1810 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | TimeoutError | - | 37 |
| 204 | ProxyError | - | 35 |
| cn-block | TimeoutError | - | 35 |
| speed | TimeoutError | - | 13 |
| geo | TimeoutError | - | 12 |
| speed | ClientOSError | - | 11 |
| cn-block | ClientOSError | - | 9 |
| geo | ClientOSError | - | 9 |
| cn-block | ProxyError | - | 7 |
| 204 | ProxyConnectionError | - | 3 |
| 204 | ClientOSError | - | 3 |
| speed | ProxyError | - | 1 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
