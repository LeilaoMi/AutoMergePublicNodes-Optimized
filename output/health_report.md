# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-22 11:29:06 |
| 运行耗时 | 657.8s |
| 订阅源总数 | 107 |
| 健康订阅源 | 97 |
| 原始节点 | 91703 |
| 去重后节点 | 25251 |
| TCP 可达 | 3000 |
| 真实可用 | 413 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 25251 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 10.4 |
| geo | 1.5 |
| tcp | 42.2 |
| probe | 257.5 |
| real_test | 198.2 |
| generate | 148.0 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 53889 |
| vmess | 14816 |
| shadowsocks | 11214 |
| trojan | 9282 |
| hysteria2 | 1600 |
| http | 634 |
| shadowsocksr | 142 |
| socks | 80 |
| anytls | 21 |
| hysteria | 17 |
| tuic | 8 |

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
| 77.5 | shadowsocks | 358.4 | 926.8 | 19.48 | 0.0 | 10.0 | 14.38 | 18.14 | Au1rxx-base64 | 15.204.246.132 |
| 77.43 | hysteria2 | 246.2 | 670.4 | 22.08 | 0.0 | 10.0 | 14.25 | 18.14 | Au1rxx-base64 | 159.223.157.129 |
| 77.4 | vless | 254.7 | 695.2 | 21.88 | 0.0 | 10.0 | 7.38 | 18.14 | Au1rxx-base64 | 79.141.172.154 |
| 77.12 | vless | 267.0 | 662.9 | 21.6 | 0.0 | 10.0 | 7.38 | 18.14 | Au1rxx-base64 | 138.124.60.146 |
| 76.85 | vless | 278.7 | 665.6 | 21.33 | 0.0 | 10.0 | 7.38 | 18.14 | Au1rxx-base64 | 169.40.42.225 |
| 76.83 | vless | 279.2 | 668.7 | 21.31 | 0.0 | 10.0 | 7.38 | 18.14 | Au1rxx-base64 | 195.211.98.43 |
| 76.78 | shadowsocks | 346.5 | 893.1 | 19.76 | 0.0 | 10.0 | 14.38 | 18.14 | Au1rxx-base64 | 185.156.47.97 |
| 76.71 | vless | 284.4 | 682.6 | 21.19 | 0.0 | 10.0 | 7.38 | 18.14 | Au1rxx-base64 | 169.40.42.52 |
| 76.38 | hysteria2 | 323.5 | 658.2 | 20.29 | 0.0 | 9.08 | 14.25 | 18.14 | Au1rxx-base64 | 66.94.121.46 |
| 76.32 | shadowsocks | 229.0 | 601.0 | 22.48 | 0.0 | 10.0 | 14.38 | 13.46 | Surfboard-tg-mixed | 198.98.53.130 |
| 76.21 | vless | 306.2 | 738.7 | 20.69 | 0.0 | 10.0 | 7.38 | 18.14 | Au1rxx-base64 | 169.40.42.184 |
| 75.47 | vless | 338.2 | 829.0 | 19.95 | 0.0 | 10.0 | 7.38 | 18.14 | Au1rxx-base64 | 66.70.179.198 |
| 75.38 | vless | 342.2 | 961.4 | 19.86 | 0.0 | 10.0 | 7.38 | 18.14 | Au1rxx-base64 | 34.85.179.6 |
| 75.27 | vless | 346.9 | 801.2 | 19.75 | 0.0 | 10.0 | 7.38 | 18.14 | Au1rxx-base64 | 169.40.42.163 |
| 74.58 | vless | 376.8 | 887.9 | 19.06 | 0.0 | 10.0 | 7.38 | 18.14 | Au1rxx-base64 | 169.40.42.229 |
| 74.47 | shadowsocks | 349.0 | 815.0 | 19.7 | 0.0 | 9.36 | 14.38 | 18.14 | Au1rxx-base64 | 108.181.57.93 |
| 74.12 | vless | 396.6 | 1074.3 | 18.6 | 0.0 | 10.0 | 7.38 | 18.14 | Au1rxx-base64 | 169.40.42.95 |
| 73.9 | vless | 337.0 | 760.4 | 19.98 | 0.0 | 10.0 | 7.38 | 18.14 | Au1rxx-base64 | 169.40.42.35 |
| 73.84 | vless | 378.9 | 894.7 | 19.01 | 0.0 | 10.0 | 7.38 | 18.14 | Au1rxx-base64 | 169.40.42.212 |
| 73.68 | shadowsocks | 264.3 | 716.2 | 21.66 | 0.0 | 10.0 | 14.38 | 11.64 | mheidari-all | 37.19.198.236 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.904 | 0.841 | 295 | 1630 | prefer |
| ermaozi | 0.643 | 0.636 | 33 | 369 | observe |
| Surfboard-tg-mixed | 0.593 | 0.513 | 150 | 7157 | observe |
| mheidari-all | 0.406 | 0.324 | 188 | 19835 | observe |
| DeltaKronecker-all | 0.305 | 0.3 | 10 | 6324 | observe |
| xiaoji235-airport-v2ray-all | 0.287 | 0.5 | 2 | 4242 | observe |
| ermaozi-get_subscribe | 0.256 | 0.5 | 4 | 393 | observe |
| Epodonios-all | 0.255 | None | 0 | 7495 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3995 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9028 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5792 | observe |
| barry-far-vless | 0.255 | None | 0 | 5817 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4344 | observe |
| Au1rxx-clash | 0.24 | None | 0 | 1630 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| cn-block | ClientOSError | - | 70 |
| geo | ClientOSError | - | 54 |
| speed | ClientOSError | - | 35 |
| 204 | ProxyError | - | 27 |
| cn-block | TimeoutError | - | 25 |
| geo | TimeoutError | - | 25 |
| 204 | TimeoutError | - | 19 |
| speed | TimeoutError | - | 11 |
| 204 | ClientOSError | - | 3 |
| cn-block | ProxyError | - | 2 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
