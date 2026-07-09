# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-09 19:58:05 |
| 运行耗时 | 237.4s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 78644 |
| 去重后节点 | 23912 |
| TCP 可达 | 3000 |
| 真实可用 | 279 |
| Verified 输出 | 279 |
| Global 输出 | 293 |
| All 输出 | 23912 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.0 |
| geo | 1.3 |
| tcp | 32.2 |
| probe | 57.3 |
| real_test | 103.1 |
| generate | 38.6 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 44887 |
| trojan | 12585 |
| vmess | 10561 |
| shadowsocks | 9367 |
| hysteria2 | 832 |
| shadowsocksr | 146 |
| http | 135 |
| socks | 114 |
| hysteria | 10 |
| anytls | 5 |
| tuic | 2 |

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
| 78.22 | shadowsocks | 202.3 | 497.1 | 23.09 | 0.0 | 10.0 | 13.83 | 15.3 | Au1rxx-base64 | 173.244.56.6 |
| 77.8 | shadowsocks | 198.9 | 486.5 | 23.17 | 0.0 | 10.0 | 13.83 | 15.3 | Au1rxx-base64 | 108.181.0.177 |
| 77.7 | shadowsocks | 203.5 | 493.7 | 23.07 | 0.0 | 10.0 | 13.83 | 15.3 | Au1rxx-base64 | 108.181.118.10 |
| 77.35 | shadowsocks | 258.4 | 631.1 | 21.8 | 0.0 | 10.0 | 13.83 | 15.82 | mheidari-all | 107.172.219.230 |
| 76.38 | shadowsocks | 256.5 | 618.2 | 21.84 | 0.0 | 10.0 | 13.83 | 15.3 | Au1rxx-base64 | 156.146.38.170 |
| 75.49 | shadowsocks | 255.4 | 623.2 | 21.87 | 0.0 | 10.0 | 13.83 | 15.3 | Au1rxx-base64 | 156.146.38.168 |
| 74.65 | shadowsocks | 294.1 | 733.1 | 20.97 | 0.0 | 10.0 | 13.83 | 15.3 | Au1rxx-base64 | 156.146.38.167 |
| 74.37 | shadowsocks | 307.1 | 772.4 | 20.67 | 0.0 | 10.0 | 13.83 | 15.3 | Au1rxx-base64 | 156.146.38.169 |
| 73.0 | vless | 251.5 | 623.5 | 21.96 | 0.0 | 10.0 | 4.22 | 17.82 | Surfboard-tg-mixed | 198.41.209.87 |
| 72.93 | vless | 254.2 | 620.4 | 21.89 | 0.0 | 10.0 | 4.22 | 17.82 | Surfboard-tg-mixed | 104.16.9.20 |
| 72.87 | shadowsocks | 302.6 | 353.3 | 20.77 | 1.75 | 9.91 | 13.83 | 17.82 | Surfboard-tg-mixed | 149.22.87.240 |
| 72.43 | shadowsocks | 305.6 | 361.0 | 20.7 | 1.46 | 9.89 | 13.83 | 17.82 | Surfboard-tg-mixed | 149.22.87.204 |
| 72.25 | shadowsocks | 307.9 | 364.8 | 20.65 | 1.32 | 9.91 | 13.83 | 17.82 | Surfboard-tg-mixed | 149.22.87.241 |
| 72.04 | trojan | 346.2 | 846.5 | 19.76 | 0.0 | 10.0 | 10.42 | 15.3 | Au1rxx-base64 | 45.32.195.168 |
| 71.67 | shadowsocks | 283.6 | 667.9 | 21.21 | 0.0 | 10.0 | 13.83 | 15.3 | Au1rxx-base64 | 173.244.56.9 |
| 70.08 | shadowsocks | 346.9 | 733.9 | 19.75 | 0.0 | 10.0 | 13.83 | 15.3 | Au1rxx-base64 | 37.19.198.160 |
| 70.01 | shadowsocks | 353.0 | 734.7 | 19.61 | 0.0 | 10.0 | 13.83 | 15.3 | Au1rxx-base64 | 37.19.198.236 |
| 69.59 | shadowsocks | 364.0 | 774.5 | 19.35 | 0.0 | 10.0 | 13.83 | 15.3 | Au1rxx-base64 | 37.19.198.244 |
| 69.49 | trojan | 414.1 | 1052.8 | 18.19 | 0.0 | 10.0 | 10.42 | 15.3 | Au1rxx-base64 | 149.28.241.235 |
| 69.27 | shadowsocks | 360.0 | 730.2 | 19.44 | 0.0 | 10.0 | 13.83 | 15.3 | Au1rxx-base64 | 147.90.234.133 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| Au1rxx-base64 | 0.854 | 0.88 | 25 | 66 | prefer |
| Surfboard-tg-mixed | 0.591 | 0.512 | 260 | 5585 | observe |
| mheidari-all | 0.407 | 0.326 | 215 | 16918 | observe |
| nscl5-all | 0.364 | 1.0 | 2 | 1319 | observe |
| DeltaKronecker-all | 0.358 | 0.269 | 52 | 7533 | observe |
| xiaoji235-airport-v2ray-all | 0.349 | 0.667 | 3 | 2703 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4306 | observe |
| Epodonios-all | 0.255 | None | 0 | 6500 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3975 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6851 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4106 | observe |
| barry-far-vless | 0.255 | None | 0 | 4613 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5403 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 155 |
| geo | TimeoutError | - | 61 |
| 204 | ProxyError | - | 24 |
| 204 | TimeoutError | - | 22 |
| cn-block | TimeoutError | - | 16 |
| geo | ClientOSError | - | 13 |
| cn-block | ClientOSError | - | 6 |
| 204 | ClientOSError | - | 5 |
| geo | ProxyError | - | 5 |
| cn-block | ProxyError | - | 4 |
| speed | TimeoutError | - | 4 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 242 | 279 | - |
| global | False | 248 | 293 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
