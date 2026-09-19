# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-19 04:15:32 |
| 运行耗时 | 714.1s |
| 订阅源总数 | 107 |
| 健康订阅源 | 95 |
| 原始节点 | 82099 |
| 去重后节点 | 23205 |
| TCP 可达 | 3000 |
| 真实可用 | 548 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23205 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.4 |
| geo | 1.4 |
| tcp | 38.0 |
| probe | 267.2 |
| real_test | 328.3 |
| generate | 72.7 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 50019 |
| vmess | 11887 |
| shadowsocks | 9927 |
| trojan | 8253 |
| hysteria2 | 1165 |
| http | 648 |
| shadowsocksr | 123 |
| socks | 64 |
| hysteria | 8 |
| anytls | 3 |
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
| 80.02 | shadowsocks | 259.9 | 650.5 | 21.76 | 0.0 | 10.0 | 13.88 | 18.38 | Au1rxx-base64 | 37.19.198.160 |
| 79.68 | vless | 251.4 | 620.0 | 21.96 | 0.0 | 10.0 | 9.34 | 18.38 | Au1rxx-base64 | 198.251.78.29 |
| 79.38 | shadowsocks | 287.7 | 727.9 | 21.12 | 0.0 | 10.0 | 13.88 | 18.38 | Au1rxx-base64 | 156.146.38.168 |
| 79.36 | shadowsocks | 288.7 | 736.1 | 21.1 | 0.0 | 10.0 | 13.88 | 18.38 | Au1rxx-base64 | 156.146.38.170 |
| 79.09 | vless | 276.8 | 709.5 | 21.37 | 0.0 | 10.0 | 9.34 | 18.38 | Au1rxx-base64 | 216.152.147.28 |
| 78.27 | hysteria2 | 275.9 | 596.6 | 21.39 | 0.0 | 10.0 | 13.5 | 18.38 | Au1rxx-base64 | 66.94.121.46 |
| 78.12 | vless | 294.3 | 703.0 | 20.97 | 0.0 | 10.0 | 9.34 | 18.38 | Au1rxx-base64 | 169.40.42.133 |
| 77.7 | shadowsocks | 338.6 | 884.0 | 19.94 | 0.0 | 10.0 | 13.88 | 18.38 | Au1rxx-base64 | 38.180.135.156 |
| 77.41 | vless | 297.2 | 716.1 | 20.9 | 0.0 | 10.0 | 9.34 | 18.38 | Au1rxx-base64 | 169.40.42.232 |
| 77.25 | vless | 326.4 | 799.8 | 20.22 | 0.0 | 10.0 | 9.34 | 18.38 | Au1rxx-base64 | 195.123.235.177 |
| 76.87 | hysteria2 | 265.6 | 663.7 | 21.63 | 0.0 | 10.0 | 13.5 | 12.84 | mheidari-all | 159.223.157.129 |
| 76.66 | vless | 322.5 | 792.7 | 20.31 | 0.0 | 10.0 | 9.34 | 18.38 | Au1rxx-base64 | 169.40.42.90 |
| 76.35 | vless | 374.8 | 941.4 | 19.1 | 0.0 | 10.0 | 9.34 | 18.38 | Au1rxx-base64 | 169.40.42.35 |
| 76.34 | vless | 337.0 | 808.5 | 19.98 | 0.0 | 10.0 | 9.34 | 18.38 | Au1rxx-base64 | 66.70.179.198 |
| 76.27 | vless | 382.7 | 914.0 | 18.92 | 0.0 | 10.0 | 9.34 | 18.38 | Au1rxx-base64 | 169.40.42.182 |
| 75.65 | vless | 300.0 | 670.6 | 20.83 | 0.0 | 10.0 | 9.34 | 18.38 | Au1rxx-base64 | 169.40.42.179 |
| 75.46 | shadowsocks | 358.8 | 890.7 | 19.47 | 0.0 | 10.0 | 13.88 | 18.38 | Au1rxx-base64 | 15.204.247.206 |
| 75.05 | vless | 421.7 | 1100.2 | 18.02 | 0.0 | 10.0 | 9.34 | 18.38 | Au1rxx-base64 | 185.95.231.156 |
| 74.87 | shadowsocks | 266.6 | 670.6 | 21.61 | 0.0 | 10.0 | 13.88 | 18.38 | Au1rxx-base64 | 37.19.198.236 |
| 74.83 | vless | 294.2 | 728.4 | 20.97 | 0.0 | 10.0 | 9.34 | 14.52 | Surfboard-tg-mixed | 47.253.226.114 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.946 | 0.88 | 317 | 1703 | prefer |
| ermaozi | 0.769 | 0.765 | 51 | 358 | prefer |
| Surfboard-tg-mixed | 0.739 | 0.66 | 247 | 7266 | prefer |
| mheidari-all | 0.506 | 0.425 | 113 | 13937 | observe |
| mahdibland-V2RayAggregator | 0.335 | 1.0 | 1 | 4241 | observe |
| ermaozi-get_subscribe | 0.288 | 0.364 | 11 | 387 | observe |
| 10ium-ScrapeCategorize-Vless | 0.259 | 0.333 | 3 | 5076 | observe |
| DeltaKronecker-all | 0.257 | 0.169 | 77 | 6040 | observe |
| Epodonios-all | 0.255 | None | 0 | 7793 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 8930 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5822 | observe |
| barry-far-vless | 0.255 | None | 0 | 6112 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.243 | None | 0 | 1704 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 94 |
| speed | TimeoutError | - | 46 |
| geo | ClientOSError | - | 31 |
| speed | ClientOSError | - | 30 |
| 204 | ProxyError | - | 26 |
| cn-block | TimeoutError | - | 24 |
| cn-block | ClientOSError | - | 12 |
| 204 | TimeoutError | - | 7 |
| 204 | ClientOSError | - | 1 |
| cn-block | ProxyError | - | 1 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
