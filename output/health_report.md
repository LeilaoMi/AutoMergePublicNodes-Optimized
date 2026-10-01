# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-01 22:39:36 |
| 运行耗时 | 481.7s |
| 订阅源总数 | 107 |
| 健康订阅源 | 94 |
| 原始节点 | 98426 |
| 去重后节点 | 27512 |
| TCP 可达 | 3000 |
| 真实可用 | 335 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 27512 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.4 |
| geo | 1.5 |
| tcp | 45.2 |
| probe | 227.2 |
| real_test | 126.2 |
| generate | 74.3 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 60553 |
| vmess | 15307 |
| shadowsocks | 11569 |
| trojan | 9016 |
| hysteria2 | 1304 |
| http | 377 |
| shadowsocksr | 165 |
| socks | 60 |
| anytls | 52 |
| hysteria | 16 |
| tuic | 7 |

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
| 82.28 | hysteria2 | 254.2 | 692.3 | 21.89 | 0.0 | 10.0 | 13.75 | 17.74 | mheidari-all | 159.223.157.129 |
| 79.02 | shadowsocks | 266.7 | 712.9 | 21.6 | 0.0 | 10.0 | 13.68 | 17.74 | mheidari-all | 37.19.198.244 |
| 78.83 | shadowsocks | 274.9 | 741.0 | 21.41 | 0.0 | 10.0 | 13.68 | 17.74 | mheidari-all | 37.19.198.160 |
| 78.68 | shadowsocks | 263.3 | 708.8 | 21.68 | 0.0 | 10.0 | 13.68 | 17.32 | Au1rxx-base64 | 37.19.198.243 |
| 78.25 | vless | 269.4 | 707.4 | 21.54 | 0.0 | 10.0 | 9.39 | 17.32 | Au1rxx-base64 | 137.184.218.169 |
| 78.18 | shadowsocks | 263.4 | 653.2 | 21.68 | 0.0 | 10.0 | 13.68 | 17.32 | Au1rxx-base64 | 140.82.63.79 |
| 78.01 | vless | 280.0 | 715.8 | 21.3 | 0.0 | 10.0 | 9.39 | 17.32 | Au1rxx-base64 | 169.40.42.184 |
| 77.95 | vless | 282.5 | 796.5 | 21.24 | 0.0 | 10.0 | 9.39 | 17.32 | Au1rxx-base64 | 79.141.172.154 |
| 77.37 | vless | 307.5 | 749.2 | 20.66 | 0.0 | 10.0 | 9.39 | 17.32 | Au1rxx-base64 | 169.40.42.104 |
| 77.33 | hysteria2 | 290.1 | 571.8 | 21.06 | 0.0 | 10.0 | 13.75 | 17.32 | Au1rxx-base64 | 192.255.128.123 |
| 77.3 | vless | 288.0 | 740.8 | 21.11 | 0.0 | 10.0 | 9.39 | 17.32 | Au1rxx-base64 | 169.40.42.133 |
| 77.25 | vless | 294.0 | 719.6 | 20.97 | 0.0 | 10.0 | 9.39 | 17.32 | Au1rxx-base64 | 66.70.179.198 |
| 77.11 | vless | 318.0 | 685.3 | 20.42 | 0.0 | 10.0 | 9.39 | 17.32 | Au1rxx-base64 | 169.40.42.35 |
| 77.05 | vless | 287.4 | 670.9 | 21.12 | 0.0 | 10.0 | 9.39 | 17.32 | Au1rxx-base64 | 169.40.42.89 |
| 76.67 | hysteria2 | 245.5 | 690.7 | 22.1 | 0.0 | 10.0 | 13.75 | 17.32 | Au1rxx-base64 | 129.213.91.185 |
| 76.42 | shadowsocks | 279.5 | 634.9 | 21.31 | 0.0 | 10.0 | 13.68 | 17.32 | Au1rxx-base64 | 156.146.38.167 |
| 76.35 | vless | 351.7 | 955.5 | 19.64 | 0.0 | 10.0 | 9.39 | 17.32 | Au1rxx-base64 | 159.89.87.21 |
| 76.27 | shadowsocks | 345.8 | 924.9 | 19.77 | 0.0 | 10.0 | 13.68 | 17.32 | Au1rxx-base64 | 15.204.246.132 |
| 75.9 | vless | 323.9 | 766.5 | 20.28 | 0.0 | 10.0 | 9.39 | 17.32 | Au1rxx-base64 | 169.40.42.15 |
| 75.84 | shadowsocks | 364.4 | 1035.6 | 19.34 | 0.0 | 10.0 | 13.68 | 17.32 | Au1rxx-base64 | 15.204.247.206 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.994 | 0.925 | 214 | 1818 | prefer |
| mheidari-all | 0.907 | 0.833 | 96 | 22987 | prefer |
| Surfboard-tg-mixed | 0.906 | 0.841 | 44 | 7183 | prefer |
| zhangkai | 0.745 | 0.762 | 21 | 144 | prefer |
| DeltaKronecker-all | 0.446 | 0.8 | 5 | 5603 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5324 | observe |
| Epodonios-all | 0.255 | None | 0 | 7711 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3996 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9539 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5811 | observe |
| barry-far-vless | 0.255 | None | 0 | 6097 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4310 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |
| Au1rxx-clash | 0.248 | None | 0 | 1818 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | TimeoutError | - | 9 |
| 204 | ProxyConnectionError | - | 8 |
| cn-block | TimeoutError | - | 8 |
| 204 | ProxyError | - | 5 |
| speed | TimeoutError | - | 4 |
| speed | ClientOSError | - | 4 |
| geo | ClientOSError | - | 3 |
| geo | TimeoutError | - | 3 |
| 204 | ClientOSError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
