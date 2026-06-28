# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-06-28 19:42:59 |
| 运行耗时 | 285.3s |
| 订阅源总数 | 107 |
| 健康订阅源 | 105 |
| 原始节点 | 76621 |
| 去重后节点 | 23024 |
| TCP 可达 | 3000 |
| 真实可用 | 518 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23024 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.7 |
| geo | 1.4 |
| tcp | 30.6 |
| probe | 54.3 |
| real_test | 144.0 |
| generate | 48.2 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 43041 |
| trojan | 12661 |
| vmess | 11105 |
| shadowsocks | 9244 |
| hysteria2 | 233 |
| shadowsocksr | 151 |
| http | 136 |
| socks | 42 |
| hysteria | 6 |
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
| 80.28 | vless | 255.5 | 722.2 | 21.86 | 0.0 | 10.0 | 11.12 | 17.3 | mheidari-all | 47.253.226.114 |
| 78.53 | vless | 288.1 | 703.0 | 21.11 | 0.0 | 10.0 | 11.12 | 17.3 | mheidari-all | 162.159.18.241 |
| 77.86 | shadowsocks | 242.2 | 618.7 | 22.17 | 0.0 | 10.0 | 12.39 | 17.3 | mheidari-all | 198.98.53.130 |
| 77.37 | shadowsocks | 242.0 | 650.3 | 22.18 | 0.0 | 10.0 | 12.39 | 17.3 | mheidari-all | 108.181.57.93 |
| 76.71 | shadowsocks | 230.7 | 640.0 | 22.44 | 0.0 | 10.0 | 12.39 | 15.88 | Au1rxx-base64 | 37.19.198.160 |
| 76.68 | shadowsocks | 232.0 | 641.1 | 22.41 | 0.0 | 10.0 | 12.39 | 15.88 | Au1rxx-base64 | 37.19.198.236 |
| 76.65 | shadowsocks | 233.2 | 639.7 | 22.38 | 0.0 | 10.0 | 12.39 | 15.88 | Au1rxx-base64 | 37.19.198.243 |
| 76.64 | shadowsocks | 233.7 | 643.5 | 22.37 | 0.0 | 10.0 | 12.39 | 15.88 | Au1rxx-base64 | 37.19.198.244 |
| 75.65 | vless | 408.2 | 711.7 | 18.33 | 0.0 | 10.0 | 11.12 | 17.3 | mheidari-all | 104.18.42.68 |
| 74.94 | vless | 338.4 | 847.1 | 19.94 | 0.0 | 10.0 | 11.12 | 15.88 | Surfboard-tg-mixed | 137.184.218.169 |
| 73.76 | shadowsocks | 276.1 | 634.5 | 21.39 | 0.0 | 10.0 | 12.39 | 15.88 | Au1rxx-base64 | 156.146.38.168 |
| 73.37 | shadowsocks | 278.8 | 640.4 | 21.32 | 0.0 | 10.0 | 12.39 | 15.88 | Au1rxx-base64 | 156.146.38.167 |
| 72.5 | vless | 266.0 | 662.4 | 21.62 | 0.0 | 10.0 | 11.12 | 10.76 | DeltaKronecker-all | 162.159.252.15 |
| 72.23 | vless | 277.6 | 707.4 | 21.35 | 0.0 | 10.0 | 11.12 | 10.76 | DeltaKronecker-all | 104.19.142.226 |
| 71.77 | shadowsocks | 322.7 | 751.1 | 20.31 | 0.0 | 10.0 | 12.39 | 15.88 | Au1rxx-base64 | 156.146.38.170 |
| 71.73 | shadowsocks | 280.0 | 655.4 | 21.3 | 0.0 | 10.0 | 12.39 | 15.88 | Au1rxx-base64 | 156.146.38.169 |
| 70.68 | vless | 457.5 | 1167.5 | 17.19 | 0.0 | 10.0 | 11.12 | 15.88 | Surfboard-tg-mixed | 130.107.73.148 |
| 70.19 | shadowsocks | 297.1 | 581.9 | 20.9 | 0.0 | 10.0 | 12.39 | 15.88 | Au1rxx-base64 | 173.244.56.9 |
| 69.43 | vless | 436.4 | 787.5 | 17.68 | 0.0 | 10.0 | 11.12 | 17.3 | mheidari-all | 34.213.172.16 |
| 69.3 | vless | 405.2 | 799.0 | 18.4 | 0.0 | 10.0 | 11.12 | 15.88 | Surfboard-tg-mixed | 162.159.38.165 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| mheidari-all | 0.844 | 0.766 | 295 | 16170 | prefer |
| Au1rxx-base64 | 0.821 | 0.839 | 31 | 82 | prefer |
| Surfboard-tg-mixed | 0.717 | 0.638 | 304 | 5276 | prefer |
| DeltaKronecker-all | 0.654 | 0.576 | 59 | 6788 | observe |
| nscl5-all | 0.302 | 1.0 | 1 | 1174 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4327 | observe |
| Epodonios-all | 0.255 | None | 0 | 7727 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3984 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7087 | observe |
| barry-far-vless | 0.255 | None | 0 | 4558 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5325 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| xiaoji235-airport-v2ray-all | 0.225 | None | 0 | 1261 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 79 |
| 204 | TimeoutError | - | 33 |
| 204 | ProxyError | - | 18 |
| cn-block | TimeoutError | - | 18 |
| geo | TimeoutError | - | 14 |
| speed | TimeoutError | - | 13 |
| 204 | ClientOSError | - | 11 |
| geo | ClientOSError | - | 7 |
| cn-block | ClientOSError | - | 6 |
| geo | ProxyError | - | 5 |
| cn-block | ProxyError | - | 3 |
| speed | ProxyError | - | 3 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
