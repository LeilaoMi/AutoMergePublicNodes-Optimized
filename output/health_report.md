# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-18 16:20:38 |
| 运行耗时 | 623.4s |
| 订阅源总数 | 107 |
| 健康订阅源 | 95 |
| 原始节点 | 83896 |
| 去重后节点 | 23095 |
| TCP 可达 | 3000 |
| 真实可用 | 399 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23095 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.2 |
| geo | 1.4 |
| tcp | 38.1 |
| probe | 275.5 |
| real_test | 223.4 |
| generate | 78.8 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 50405 |
| vmess | 13226 |
| shadowsocks | 10067 |
| trojan | 8141 |
| hysteria2 | 1259 |
| http | 588 |
| shadowsocksr | 128 |
| socks | 65 |
| hysteria | 8 |
| anytls | 7 |
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
| 82.67 | hysteria2 | 243.2 | 647.9 | 22.15 | 0.0 | 10.0 | 13.5 | 18.12 | Au1rxx-base64 | 159.223.157.129 |
| 79.72 | vless | 237.1 | 596.5 | 22.29 | 0.0 | 10.0 | 9.31 | 18.12 | Au1rxx-base64 | 195.123.235.177 |
| 78.7 | shadowsocks | 242.8 | 651.3 | 22.16 | 0.0 | 10.0 | 13.42 | 18.12 | Au1rxx-base64 | 37.19.198.160 |
| 78.07 | vless | 308.2 | 679.2 | 20.64 | 0.0 | 10.0 | 9.31 | 18.12 | Au1rxx-base64 | 169.40.42.75 |
| 77.8 | vless | 320.2 | 804.0 | 20.37 | 0.0 | 10.0 | 9.31 | 18.12 | Au1rxx-base64 | 169.40.42.90 |
| 77.29 | vless | 342.2 | 853.5 | 19.86 | 0.0 | 10.0 | 9.31 | 18.12 | Au1rxx-base64 | 169.40.42.235 |
| 77.1 | vless | 350.0 | 804.4 | 19.67 | 0.0 | 10.0 | 9.31 | 18.12 | Au1rxx-base64 | 169.40.42.229 |
| 76.83 | vless | 361.7 | 825.8 | 19.4 | 0.0 | 10.0 | 9.31 | 18.12 | Au1rxx-base64 | 169.40.42.133 |
| 76.79 | vless | 324.0 | 849.7 | 20.28 | 0.0 | 10.0 | 9.31 | 18.12 | Au1rxx-base64 | 169.40.42.231 |
| 76.7 | vless | 367.7 | 993.0 | 19.27 | 0.0 | 10.0 | 9.31 | 18.12 | Au1rxx-base64 | 185.95.231.156 |
| 76.61 | hysteria2 | 308.3 | 614.2 | 20.64 | 0.0 | 10.0 | 13.5 | 18.12 | Au1rxx-base64 | 66.94.121.46 |
| 76.56 | vless | 373.7 | 943.2 | 19.13 | 0.0 | 10.0 | 9.31 | 18.12 | Au1rxx-base64 | 169.40.42.16 |
| 76.5 | vless | 367.6 | 919.7 | 19.27 | 0.0 | 10.0 | 9.31 | 18.12 | Au1rxx-base64 | 169.40.42.104 |
| 76.31 | vless | 384.5 | 897.1 | 18.88 | 0.0 | 10.0 | 9.31 | 18.12 | Au1rxx-base64 | 169.40.42.173 |
| 76.11 | vless | 393.0 | 1053.1 | 18.68 | 0.0 | 10.0 | 9.31 | 18.12 | Au1rxx-base64 | 169.40.42.168 |
| 76.1 | vless | 393.5 | 916.3 | 18.67 | 0.0 | 10.0 | 9.31 | 18.12 | Au1rxx-base64 | 169.40.42.74 |
| 75.82 | vless | 391.9 | 918.7 | 18.71 | 0.0 | 10.0 | 9.31 | 18.12 | Au1rxx-base64 | 169.40.42.89 |
| 75.64 | vless | 405.3 | 968.0 | 18.4 | 0.0 | 10.0 | 9.31 | 18.12 | Au1rxx-base64 | 169.40.42.163 |
| 75.59 | shadowsocks | 318.1 | 876.2 | 20.41 | 0.0 | 10.0 | 13.42 | 15.76 | mheidari-all | 37.19.198.243 |
| 75.42 | vless | 385.1 | 1034.7 | 18.86 | 0.0 | 10.0 | 9.31 | 18.12 | Au1rxx-base64 | 169.40.42.224 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.96 | 0.899 | 257 | 1596 | prefer |
| ermaozi | 0.828 | 0.84 | 25 | 325 | prefer |
| mheidari-all | 0.747 | 0.672 | 64 | 15758 | prefer |
| Surfboard-tg-mixed | 0.742 | 0.664 | 146 | 7397 | prefer |
| mahdibland-V2RayAggregator | 0.335 | 1.0 | 1 | 4241 | observe |
| DeltaKronecker-all | 0.314 | 0.222 | 18 | 6040 | observe |
| roosterkid-openproxylist-v2ray | 0.261 | 1.0 | 1 | 150 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5076 | observe |
| Epodonios-all | 0.255 | None | 0 | 7860 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 8960 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5909 | observe |
| barry-far-vless | 0.255 | None | 0 | 6127 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.239 | None | 0 | 1596 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | ClientOSError | - | 24 |
| 204 | ProxyError | - | 18 |
| 204 | TimeoutError | - | 16 |
| cn-block | TimeoutError | - | 15 |
| geo | TimeoutError | - | 15 |
| cn-block | ClientOSError | - | 12 |
| speed | ClientOSError | - | 11 |
| 204 | ProxyConnectionError | - | 5 |
| cn-block | ProxyError | - | 3 |
| speed | TimeoutError | - | 2 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
