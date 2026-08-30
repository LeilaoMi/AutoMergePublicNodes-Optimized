# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-30 11:43:52 |
| 运行耗时 | 280.0s |
| 订阅源总数 | 107 |
| 健康订阅源 | 94 |
| 原始节点 | 79168 |
| 去重后节点 | 21765 |
| TCP 可达 | 3000 |
| 真实可用 | 602 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 21765 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.3 |
| geo | 1.5 |
| tcp | 34.3 |
| probe | 58.0 |
| real_test | 140.7 |
| generate | 41.3 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 49358 |
| vmess | 10532 |
| shadowsocks | 10274 |
| trojan | 7159 |
| hysteria2 | 1474 |
| http | 169 |
| shadowsocksr | 134 |
| socks | 53 |
| hysteria | 7 |
| tuic | 7 |
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
| 85.72 | hysteria2 | 229.6 | 637.3 | 22.46 | 0.0 | 10.0 | 14.38 | 19.98 | Au1rxx-base64 | 159.223.157.129 |
| 82.8 | shadowsocks | 229.3 | 636.2 | 22.47 | 0.0 | 10.0 | 14.35 | 19.98 | Au1rxx-base64 | 37.19.198.160 |
| 82.8 | shadowsocks | 229.5 | 626.7 | 22.47 | 0.0 | 10.0 | 14.35 | 19.98 | Au1rxx-base64 | 37.19.198.244 |
| 82.73 | shadowsocks | 232.4 | 642.6 | 22.4 | 0.0 | 10.0 | 14.35 | 19.98 | Au1rxx-base64 | 37.19.198.243 |
| 82.48 | vless | 235.8 | 635.5 | 22.32 | 0.0 | 9.68 | 10.5 | 19.98 | Au1rxx-base64 | ql6k-m23nix.logicara.top |
| 82.47 | vless | 249.9 | 660.2 | 21.99 | 0.0 | 10.0 | 10.5 | 19.98 | Au1rxx-base64 | 169.40.42.52 |
| 82.43 | vless | 251.4 | 622.3 | 21.96 | 0.0 | 10.0 | 10.5 | 19.98 | Au1rxx-base64 | 172.105.104.54 |
| 82.39 | vless | 253.6 | 657.9 | 21.91 | 0.0 | 10.0 | 10.5 | 19.98 | Au1rxx-base64 | 169.40.42.89 |
| 82.39 | vless | 253.6 | 652.3 | 21.91 | 0.0 | 10.0 | 10.5 | 19.98 | Au1rxx-base64 | 169.40.42.16 |
| 82.31 | vless | 256.9 | 689.2 | 21.83 | 0.0 | 10.0 | 10.5 | 19.98 | Au1rxx-base64 | 38.77.133.141 |
| 82.27 | vless | 258.8 | 634.8 | 21.79 | 0.0 | 10.0 | 10.5 | 19.98 | Au1rxx-base64 | 195.211.99.49 |
| 82.1 | vless | 266.2 | 702.3 | 21.62 | 0.0 | 10.0 | 10.5 | 19.98 | Au1rxx-base64 | 169.40.42.212 |
| 81.45 | vless | 294.0 | 732.1 | 20.97 | 0.0 | 10.0 | 10.5 | 19.98 | Au1rxx-base64 | 169.40.42.235 |
| 81.34 | vless | 298.9 | 667.4 | 20.86 | 0.0 | 10.0 | 10.5 | 19.98 | Au1rxx-base64 | 169.40.42.184 |
| 81.28 | vless | 301.3 | 747.8 | 20.8 | 0.0 | 10.0 | 10.5 | 19.98 | Au1rxx-base64 | 169.40.42.182 |
| 81.05 | vless | 311.3 | 703.9 | 20.57 | 0.0 | 10.0 | 10.5 | 19.98 | Au1rxx-base64 | 169.40.42.74 |
| 80.86 | vless | 319.8 | 873.5 | 20.38 | 0.0 | 10.0 | 10.5 | 19.98 | Au1rxx-base64 | 169.40.42.229 |
| 80.75 | shadowsocks | 296.4 | 819.8 | 20.92 | 0.0 | 10.0 | 14.35 | 19.98 | Au1rxx-base64 | 38.180.135.156 |
| 80.68 | vless | 327.2 | 896.8 | 20.2 | 0.0 | 10.0 | 10.5 | 19.98 | Au1rxx-base64 | 79.127.243.217 |
| 80.45 | vless | 337.3 | 784.5 | 19.97 | 0.0 | 10.0 | 10.5 | 19.98 | Au1rxx-base64 | 169.40.42.225 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.997 | 0.928 | 345 | 1804 | prefer |
| zhangkai | 0.967 | 1.0 | 24 | 144 | prefer |
| Surfboard-tg-mixed | 0.844 | 0.768 | 142 | 6846 | prefer |
| DeltaKronecker-all | 0.8 | 0.723 | 191 | 5576 | prefer |
| mheidari-all | 0.699 | 1.0 | 10 | 15081 | observe |
| roosterkid-openproxylist-v2ray | 0.261 | 1.0 | 1 | 150 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4762 | observe |
| Epodonios-all | 0.255 | None | 0 | 7251 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3991 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7584 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5683 | observe |
| barry-far-vless | 0.255 | None | 0 | 5864 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 3949 | observe |
| Au1rxx-clash | 0.247 | None | 0 | 1804 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| cn-block | TimeoutError | - | 26 |
| 204 | TimeoutError | - | 19 |
| geo | ClientOSError | - | 16 |
| speed | TimeoutError | - | 13 |
| geo | TimeoutError | - | 9 |
| speed | ClientOSError | - | 9 |
| 204 | ProxyError | - | 8 |
| cn-block | ProxyError | - | 4 |
| 204 | ClientOSError | - | 4 |
| cn-block | ClientOSError | - | 3 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
