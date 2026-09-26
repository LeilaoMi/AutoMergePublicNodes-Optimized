# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-26 11:17:16 |
| 运行耗时 | 569.0s |
| 订阅源总数 | 107 |
| 健康订阅源 | 94 |
| 原始节点 | 96784 |
| 去重后节点 | 26417 |
| TCP 可达 | 3000 |
| 真实可用 | 367 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 26417 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 8.0 |
| geo | 1.5 |
| tcp | 43.9 |
| probe | 212.1 |
| real_test | 207.2 |
| generate | 96.3 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 58833 |
| vmess | 15182 |
| shadowsocks | 11225 |
| trojan | 8968 |
| hysteria2 | 1571 |
| http | 672 |
| shadowsocksr | 176 |
| socks | 98 |
| anytls | 32 |
| hysteria | 15 |
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
| 76.4 | hysteria2 | 370.7 | 750.0 | 19.2 | 0.0 | 9.43 | 12.75 | 18.48 | Au1rxx-base64 | 66.94.121.46 |
| 76.31 | shadowsocks | 262.7 | 626.5 | 21.7 | 0.0 | 10.0 | 13.62 | 16.9 | Surfboard-tg-mixed | 5.78.51.123 |
| 75.25 | shadowsocks | 286.7 | 570.9 | 21.14 | 0.0 | 10.0 | 13.62 | 18.48 | Au1rxx-base64 | 173.244.56.6 |
| 74.77 | hysteria2 | 270.5 | 311.5 | 21.52 | 3.32 | 8.0 | 12.75 | 18.48 | Au1rxx-base64 | open.w2m.ink |
| 74.06 | shadowsocks | 302.8 | 669.3 | 20.77 | 0.0 | 10.0 | 13.62 | 16.9 | Surfboard-tg-mixed | 198.98.53.130 |
| 73.84 | shadowsocks | 289.6 | 557.2 | 21.07 | 0.0 | 10.0 | 13.62 | 16.9 | Surfboard-tg-mixed | 108.181.0.177 |
| 73.83 | shadowsocks | 336.8 | 770.3 | 19.98 | 0.0 | 9.44 | 13.62 | 18.48 | Au1rxx-base64 | 37.19.198.243 |
| 73.22 | shadowsocks | 313.5 | 329.7 | 20.52 | 2.64 | 9.44 | 13.62 | 18.48 | Au1rxx-base64 | 149.22.87.204 |
| 73.01 | vless | 307.6 | 734.4 | 20.66 | 0.0 | 9.27 | 5.98 | 18.48 | Au1rxx-base64 | 79.141.172.154 |
| 72.84 | shadowsocks | 396.0 | 945.0 | 18.61 | 0.0 | 10.0 | 13.62 | 18.48 | Au1rxx-base64 | 37.19.198.236 |
| 72.58 | shadowsocks | 370.7 | 885.1 | 19.2 | 0.0 | 8.78 | 13.62 | 18.48 | Au1rxx-base64 | yyz-ca-01.blncvpn4u.cc |
| 72.45 | shadowsocks | 330.7 | 779.8 | 20.12 | 0.0 | 10.0 | 13.62 | 16.9 | Surfboard-tg-mixed | 185.156.47.97 |
| 72.3 | vless | 304.8 | 719.6 | 20.72 | 0.0 | 10.0 | 5.98 | 16.9 | Surfboard-tg-mixed | 5.78.159.214 |
| 72.07 | shadowsocks | 419.0 | 976.3 | 18.08 | 0.0 | 9.44 | 13.62 | 18.48 | Au1rxx-base64 | 15.204.247.206 |
| 72.04 | shadowsocks | 370.7 | 800.7 | 19.2 | 0.0 | 10.0 | 13.62 | 18.48 | Au1rxx-base64 | 108.181.57.93 |
| 72.03 | shadowsocks | 403.4 | 966.2 | 18.44 | 0.0 | 9.36 | 13.62 | 18.48 | Au1rxx-base64 | 37.19.198.244 |
| 71.79 | vless | 268.9 | 568.8 | 21.55 | 0.0 | 9.26 | 5.98 | 18.48 | Au1rxx-base64 | 172.235.43.210 |
| 71.23 | shadowsocks | 316.3 | 663.7 | 20.46 | 0.0 | 10.0 | 13.62 | 18.48 | Au1rxx-base64 | 149.22.95.183 |
| 70.66 | trojan | 282.7 | 559.3 | 21.23 | 0.0 | 10.0 | 9.12 | 16.9 | Surfboard-tg-mixed | 100.42.228.109 |
| 70.54 | shadowsocks | 325.3 | 360.9 | 20.25 | 1.47 | 9.79 | 13.62 | 16.9 | Surfboard-tg-mixed | 149.22.87.240 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.958 | 0.895 | 238 | 1660 | prefer |
| Surfboard-tg-mixed | 0.757 | 0.68 | 128 | 7247 | prefer |
| mheidari-all | 0.727 | 0.651 | 83 | 22392 | prefer |
| mahdibland-V2RayAggregator | 0.335 | 1.0 | 1 | 4355 | observe |
| ermaozi | 0.282 | 0.256 | 39 | 352 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| DeltaKronecker-all | 0.259 | 0.333 | 3 | 5512 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5242 | observe |
| Epodonios-all | 0.255 | None | 0 | 7713 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3995 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 8992 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5840 | observe |
| barry-far-vless | 0.255 | None | 0 | 6071 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.241 | None | 0 | 1660 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | TimeoutError | - | 27 |
| cn-block | TimeoutError | - | 24 |
| 204 | ProxyError | - | 23 |
| cn-block | ClientOSError | - | 11 |
| 204 | ProxyConnectionError | - | 10 |
| geo | TimeoutError | - | 9 |
| cn-block | ProxyError | - | 8 |
| speed | TimeoutError | - | 8 |
| speed | ClientOSError | - | 3 |
| 204 | ClientOSError | - | 2 |
| geo | ClientOSError | - | 1 |
| geo | ProxyError | - | 1 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
