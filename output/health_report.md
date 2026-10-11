# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-11 12:42:15 |
| 运行耗时 | 871.8s |
| 订阅源总数 | 107 |
| 健康订阅源 | 94 |
| 原始节点 | 98718 |
| 去重后节点 | 27554 |
| TCP 可达 | 3000 |
| 真实可用 | 514 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 27554 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.8 |
| geo | 1.3 |
| tcp | 47.4 |
| probe | 345.5 |
| real_test | 394.8 |
| generate | 76.9 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 57607 |
| vmess | 15774 |
| shadowsocks | 11948 |
| trojan | 10867 |
| hysteria2 | 1601 |
| http | 633 |
| shadowsocksr | 163 |
| socks | 70 |
| anytls | 30 |
| hysteria | 16 |
| tuic | 9 |

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
| 81.89 | shadowsocks | 238.1 | 547.6 | 22.27 | 0.0 | 10.0 | 14.39 | 19.82 | Au1rxx-base64 | 5.78.51.123 |
| 81.65 | hysteria2 | 260.5 | 246.0 | 21.75 | 5.77 | 8.32 | 13.45 | 19.82 | Au1rxx-base64 | open.2ml.bid |
| 80.7 | hysteria2 | 257.2 | 309.8 | 21.82 | 3.38 | 9.9 | 13.45 | 19.82 | Au1rxx-base64 | 158.101.148.79 |
| 80.16 | hysteria2 | 321.3 | 744.0 | 20.34 | 0.0 | 10.0 | 13.45 | 19.82 | Au1rxx-base64 | 129.213.91.185 |
| 79.19 | vless | 208.5 | 521.8 | 22.95 | 0.0 | 10.0 | 6.42 | 19.82 | Au1rxx-base64 | 154.9.241.170 |
| 78.89 | vless | 221.4 | 544.6 | 22.65 | 0.0 | 10.0 | 6.42 | 19.82 | Au1rxx-base64 | 154.12.38.202 |
| 77.91 | shadowsocks | 264.3 | 585.5 | 21.66 | 0.0 | 10.0 | 14.39 | 19.82 | Au1rxx-base64 | 173.244.56.6 |
| 77.64 | shadowsocks | 286.0 | 622.5 | 21.16 | 0.0 | 10.0 | 14.39 | 19.82 | Au1rxx-base64 | 149.22.95.183 |
| 76.97 | vless | 215.1 | 513.2 | 22.8 | 0.0 | 10.0 | 6.42 | 19.82 | Au1rxx-base64 | 137.175.82.40 |
| 76.88 | vless | 308.4 | 807.8 | 20.64 | 0.0 | 10.0 | 6.42 | 19.82 | Au1rxx-base64 | 154.12.38.159 |
| 76.14 | shadowsocks | 298.7 | 335.7 | 20.86 | 2.41 | 9.91 | 14.39 | 19.82 | Au1rxx-base64 | 149.22.87.241 |
| 75.85 | vless | 274.0 | 611.7 | 21.44 | 0.0 | 10.0 | 6.42 | 19.82 | Au1rxx-base64 | 15.204.97.216 |
| 75.43 | shadowsocks | 255.5 | 625.3 | 21.86 | 0.0 | 10.0 | 14.39 | 19.82 | Au1rxx-base64 | 156.146.38.168 |
| 75.18 | shadowsocks | 257.9 | 628.9 | 21.81 | 0.0 | 10.0 | 14.39 | 19.82 | Au1rxx-base64 | 156.146.38.169 |
| 75.01 | shadowsocks | 360.5 | 787.1 | 19.43 | 0.0 | 10.0 | 14.39 | 19.82 | Au1rxx-base64 | 37.19.198.244 |
| 74.8 | vless | 270.2 | 601.8 | 21.52 | 0.0 | 10.0 | 6.42 | 19.82 | Au1rxx-base64 | 15.204.97.197 |
| 74.78 | trojan | 341.5 | 342.3 | 19.87 | 2.17 | 9.89 | 13.24 | 19.82 | Au1rxx-base64 | 18.183.212.83 |
| 74.71 | trojan | 338.5 | 337.9 | 19.94 | 2.33 | 9.91 | 13.24 | 19.82 | Au1rxx-base64 | 45.32.52.173 |
| 74.67 | shadowsocks | 291.1 | 728.7 | 21.04 | 0.0 | 10.0 | 14.39 | 19.82 | Au1rxx-base64 | 156.146.38.170 |
| 74.62 | trojan | 340.9 | 347.4 | 19.89 | 1.97 | 9.89 | 13.24 | 19.82 | Au1rxx-base64 | 13.230.76.132 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.988 | 0.917 | 362 | 1835 | prefer |
| mheidari-all | 0.913 | 0.846 | 52 | 23631 | prefer |
| DeltaKronecker-all | 0.906 | 0.841 | 44 | 5372 | prefer |
| Surfboard-tg-mixed | 0.716 | 0.638 | 141 | 7157 | prefer |
| ermaozi | 0.493 | 0.5 | 18 | 635 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5099 | observe |
| Epodonios-all | 0.255 | None | 0 | 7574 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9584 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5553 | observe |
| barry-far-vless | 0.255 | None | 0 | 5786 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4318 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |
| Au1rxx-clash | 0.248 | None | 0 | 1835 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| cn-block | TimeoutError | - | 24 |
| 204 | TimeoutError | - | 20 |
| 204 | ProxyError | - | 13 |
| speed | ClientOSError | - | 11 |
| geo | ClientOSError | - | 9 |
| geo | TimeoutError | - | 8 |
| speed | TimeoutError | - | 8 |
| cn-block | ClientOSError | - | 8 |
| 204 | ClientOSError | - | 4 |
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
