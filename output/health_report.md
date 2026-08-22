# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-22 06:53:37 |
| 运行耗时 | 301.9s |
| 订阅源总数 | 107 |
| 健康订阅源 | 99 |
| 原始节点 | 91263 |
| 去重后节点 | 23609 |
| TCP 可达 | 3000 |
| 真实可用 | 777 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23609 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 9.6 |
| geo | 1.4 |
| tcp | 39.1 |
| probe | 53.8 |
| real_test | 163.5 |
| generate | 34.4 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 51782 |
| trojan | 15874 |
| shadowsocks | 10916 |
| vmess | 10589 |
| hysteria2 | 1549 |
| shadowsocksr | 203 |
| http | 167 |
| socks | 123 |
| anytls | 32 |
| hysteria | 15 |
| tuic | 13 |

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
| 82.34 | shadowsocks | 252.4 | 683.4 | 21.94 | 0.0 | 10.0 | 14.4 | 20.0 | Au1rxx-base64 | 37.19.198.244 |
| 81.7 | shadowsocks | 248.1 | 622.1 | 22.03 | 0.0 | 9.52 | 14.4 | 20.0 | Au1rxx-base64 | 155.138.136.240 |
| 81.62 | shadowsocks | 252.7 | 682.8 | 21.93 | 0.0 | 9.29 | 14.4 | 20.0 | Au1rxx-base64 | 37.19.198.243 |
| 81.41 | shadowsocks | 269.2 | 735.2 | 21.55 | 0.0 | 9.46 | 14.4 | 20.0 | Au1rxx-base64 | 37.19.198.160 |
| 80.68 | shadowsocks | 298.1 | 822.1 | 20.88 | 0.0 | 9.4 | 14.4 | 20.0 | Au1rxx-base64 | 37.19.198.236 |
| 80.59 | shadowsocks | 306.1 | 778.9 | 20.69 | 0.0 | 10.0 | 14.4 | 20.0 | Au1rxx-base64 | 51.79.49.116 |
| 79.66 | shadowsocks | 317.5 | 822.3 | 20.43 | 0.0 | 9.33 | 14.4 | 20.0 | Au1rxx-base64 | 38.180.135.156 |
| 79.34 | shadowsocks | 284.0 | 659.9 | 21.2 | 0.0 | 9.26 | 14.4 | 20.0 | Au1rxx-base64 | 156.146.38.169 |
| 78.87 | shadowsocks | 282.2 | 650.8 | 21.24 | 0.0 | 9.23 | 14.4 | 20.0 | Au1rxx-base64 | 156.146.38.168 |
| 78.28 | shadowsocks | 279.4 | 649.8 | 21.31 | 0.0 | 9.23 | 14.4 | 20.0 | Au1rxx-base64 | 156.146.38.167 |
| 78.06 | shadowsocks | 327.8 | 601.2 | 20.19 | 0.0 | 10.0 | 14.4 | 20.0 | Au1rxx-base64 | 156.146.38.170 |
| 77.6 | vless | 272.7 | 647.1 | 21.46 | 0.0 | 10.0 | 7.78 | 18.36 | Surfboard-tg-mixed | 169.40.42.229 |
| 77.56 | vless | 287.9 | 741.7 | 21.11 | 0.0 | 9.28 | 7.78 | 20.0 | Au1rxx-base64 | 169.40.42.179 |
| 77.55 | shadowsocks | 290.0 | 627.0 | 21.07 | 0.0 | 9.35 | 14.4 | 20.0 | Au1rxx-base64 | 23.150.248.20 |
| 77.51 | vless | 267.0 | 635.0 | 21.6 | 0.0 | 9.42 | 7.78 | 20.0 | Au1rxx-base64 | 195.211.98.214 |
| 77.24 | vless | 272.9 | 606.2 | 21.46 | 0.0 | 10.0 | 7.78 | 20.0 | Au1rxx-base64 | 216.227.161.95 |
| 77.19 | shadowsocks | 312.0 | 710.4 | 20.55 | 0.0 | 9.32 | 14.4 | 20.0 | Au1rxx-base64 | 108.181.57.93 |
| 77.05 | vless | 301.0 | 721.2 | 20.81 | 0.0 | 10.0 | 7.78 | 20.0 | Au1rxx-base64 | 209.200.246.86 |
| 77.0 | vless | 288.9 | 796.1 | 21.09 | 0.0 | 9.23 | 7.78 | 20.0 | Au1rxx-base64 | 45.138.100.226 |
| 76.99 | shadowsocks | 353.9 | 677.4 | 19.58 | 0.0 | 9.52 | 14.4 | 20.0 | Au1rxx-base64 | 51.79.64.198 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.997 | 1.0 | 112 | 144 | prefer |
| Au1rxx-base64 | 0.992 | 0.942 | 446 | 1299 | prefer |
| Surfboard-tg-mixed | 0.855 | 0.778 | 171 | 6140 | prefer |
| mheidari-all | 0.444 | 0.363 | 295 | 21732 | observe |
| nscl5-all | 0.335 | 1.0 | 1 | 3321 | observe |
| tg-oneclickvpnkeys | 0.261 | 1.0 | 1 | 151 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5096 | observe |
| Epodonios-all | 0.255 | None | 0 | 6729 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3992 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7142 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4954 | observe |
| barry-far-vless | 0.255 | None | 0 | 5261 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4074 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 5974 | observe |
| Au1rxx-clash | 0.227 | None | 0 | 1299 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 101 |
| geo | ClientOSError | - | 86 |
| speed | TimeoutError | - | 35 |
| speed | ClientOSError | - | 15 |
| 204 | TimeoutError | - | 15 |
| cn-block | TimeoutError | - | 12 |
| 204 | ProxyError | - | 8 |
| cn-block | ClientOSError | - | 8 |
| 204 | ClientOSError | - | 2 |
| cn-block | ProxyError | - | 1 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
