# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-05 14:20:12 |
| 运行耗时 | 600.5s |
| 订阅源总数 | 107 |
| 健康订阅源 | 94 |
| 原始节点 | 98602 |
| 去重后节点 | 27263 |
| TCP 可达 | 3000 |
| 真实可用 | 446 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 27263 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.5 |
| geo | 1.4 |
| tcp | 46.7 |
| probe | 251.1 |
| real_test | 212.1 |
| generate | 84.9 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 58350 |
| vmess | 15937 |
| shadowsocks | 11579 |
| trojan | 10369 |
| hysteria2 | 1422 |
| http | 636 |
| shadowsocksr | 171 |
| socks | 74 |
| anytls | 27 |
| tuic | 20 |
| hysteria | 17 |

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
| 82.53 | hysteria2 | 284.4 | 727.8 | 21.19 | 0.0 | 10.0 | 13.64 | 19.2 | Au1rxx-base64 | 129.213.91.185 |
| 80.68 | shadowsocks | 273.5 | 692.1 | 21.45 | 0.0 | 10.0 | 14.03 | 19.2 | Au1rxx-base64 | 156.146.38.168 |
| 80.16 | shadowsocks | 295.8 | 753.4 | 20.93 | 0.0 | 10.0 | 14.03 | 19.2 | Au1rxx-base64 | 156.146.38.167 |
| 79.97 | shadowsocks | 304.2 | 794.3 | 20.74 | 0.0 | 10.0 | 14.03 | 19.2 | Au1rxx-base64 | 156.146.38.169 |
| 79.53 | shadowsocks | 303.8 | 727.2 | 20.75 | 0.0 | 10.0 | 14.03 | 19.2 | Au1rxx-base64 | 37.19.198.236 |
| 79.51 | shadowsocks | 311.5 | 762.0 | 20.57 | 0.0 | 10.0 | 14.03 | 19.2 | Au1rxx-base64 | 37.19.198.160 |
| 78.93 | shadowsocks | 309.5 | 741.2 | 20.61 | 0.0 | 10.0 | 14.03 | 19.2 | Au1rxx-base64 | 37.19.198.244 |
| 78.3 | hysteria2 | 318.4 | 308.5 | 20.41 | 3.43 | 9.26 | 13.64 | 19.2 | Au1rxx-base64 | open.w2m.ink |
| 77.98 | hysteria2 | 331.3 | 714.6 | 20.11 | 0.0 | 10.0 | 13.64 | 19.2 | Au1rxx-base64 | 66.94.121.46 |
| 77.64 | shadowsocks | 309.3 | 741.0 | 20.62 | 0.0 | 10.0 | 14.03 | 19.2 | Au1rxx-base64 | 37.19.198.243 |
| 77.15 | shadowsocks | 294.3 | 769.1 | 20.97 | 0.0 | 10.0 | 14.03 | 19.2 | Au1rxx-base64 | 156.146.38.170 |
| 76.79 | shadowsocks | 303.1 | 692.9 | 20.76 | 0.0 | 10.0 | 14.03 | 19.2 | Au1rxx-base64 | 140.82.63.79 |
| 76.7 | shadowsocks | 269.0 | 727.9 | 21.55 | 0.0 | 10.0 | 14.03 | 18.62 | Surfboard-tg-mixed | 66.23.204.210 |
| 74.54 | shadowsocks | 323.5 | 734.6 | 20.29 | 0.0 | 10.0 | 14.03 | 18.62 | Surfboard-tg-mixed | 5.78.51.123 |
| 74.44 | trojan | 334.1 | 643.8 | 20.04 | 0.0 | 8.97 | 14.04 | 19.2 | Au1rxx-base64 | happy-gibbon.rooster465.autos |
| 74.44 | shadowsocks | 521.5 | 1426.0 | 15.71 | 0.0 | 10.0 | 14.03 | 19.2 | Au1rxx-base64 | 138.199.48.82 |
| 74.4 | shadowsocks | 294.1 | 526.7 | 20.97 | 0.0 | 10.0 | 14.03 | 18.62 | Surfboard-tg-mixed | 108.181.118.10 |
| 74.31 | shadowsocks | 383.2 | 958.6 | 18.91 | 0.0 | 10.0 | 14.03 | 18.62 | Surfboard-tg-mixed | 15.204.233.41 |
| 73.8 | vless | 291.4 | 581.5 | 21.03 | 0.0 | 10.0 | 7.42 | 19.2 | Au1rxx-base64 | 107.173.237.146 |
| 73.67 | hysteria2 | 323.5 | 303.5 | 20.29 | 3.62 | 9.59 | 13.64 | 19.2 | Au1rxx-base64 | 132.226.14.77 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| mheidari-all | 0.978 | 0.912 | 57 | 23423 | prefer |
| Au1rxx-base64 | 0.934 | 0.864 | 301 | 1816 | prefer |
| Surfboard-tg-mixed | 0.784 | 0.707 | 133 | 7151 | prefer |
| DeltaKronecker-all | 0.507 | 0.471 | 17 | 5300 | observe |
| ermaozi | 0.505 | 0.476 | 63 | 701 | observe |
| tg-LonUp_M | 0.262 | 1.0 | 1 | 172 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5111 | observe |
| Epodonios-all | 0.255 | None | 0 | 7645 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9196 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5695 | observe |
| barry-far-vless | 0.255 | None | 0 | 5930 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4375 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |
| Au1rxx-clash | 0.248 | None | 0 | 1816 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | TimeoutError | - | 42 |
| 204 | ProxyError | - | 31 |
| cn-block | TimeoutError | - | 14 |
| speed | TimeoutError | - | 11 |
| speed | ClientOSError | - | 9 |
| geo | ClientOSError | - | 8 |
| geo | TimeoutError | - | 6 |
| cn-block | ClientOSError | - | 4 |
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
