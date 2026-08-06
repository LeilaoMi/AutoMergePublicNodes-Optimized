# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-06 14:28:48 |
| 运行耗时 | 214.3s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 89832 |
| 去重后节点 | 24596 |
| TCP 可达 | 3000 |
| 真实可用 | 482 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 24596 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.2 |
| geo | 1.5 |
| tcp | 37.5 |
| probe | 47.5 |
| real_test | 95.6 |
| generate | 26.0 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 52487 |
| vmess | 13308 |
| trojan | 12017 |
| shadowsocks | 10213 |
| hysteria2 | 1473 |
| socks | 171 |
| shadowsocksr | 74 |
| anytls | 30 |
| http | 24 |
| hysteria | 21 |
| tuic | 14 |

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
| 81.83 | hysteria2 | 273.7 | 658.4 | 21.44 | 0.0 | 9.1 | 12.39 | 20.0 | Au1rxx-base64 | 159.223.157.129 |
| 81.75 | hysteria2 | 281.6 | 704.7 | 21.26 | 0.0 | 9.1 | 12.39 | 20.0 | Au1rxx-base64 | 138.124.68.188 |
| 81.57 | shadowsocks | 235.5 | 585.1 | 22.33 | 0.0 | 9.16 | 14.08 | 20.0 | Au1rxx-base64 | 156.146.38.168 |
| 81.4 | shadowsocks | 242.8 | 609.3 | 22.16 | 0.0 | 9.16 | 14.08 | 20.0 | Au1rxx-base64 | 156.146.38.169 |
| 81.29 | shadowsocks | 247.5 | 604.3 | 22.05 | 0.0 | 9.16 | 14.08 | 20.0 | Au1rxx-base64 | 156.146.38.170 |
| 79.96 | trojan | 287.8 | 648.0 | 21.12 | 0.0 | 10.0 | 14.02 | 20.0 | Au1rxx-base64 | 163.245.196.68 |
| 79.89 | shadowsocks | 255.8 | 635.4 | 21.86 | 0.0 | 9.16 | 14.08 | 20.0 | Au1rxx-base64 | 156.146.38.167 |
| 77.82 | trojan | 325.5 | 760.7 | 20.24 | 0.0 | 10.0 | 14.02 | 20.0 | Au1rxx-base64 | 153.75.250.171 |
| 77.76 | shadowsocks | 304.2 | 723.0 | 20.74 | 0.0 | 9.16 | 14.08 | 20.0 | Au1rxx-base64 | 37.19.198.244 |
| 77.2 | vless | 263.7 | 577.9 | 21.67 | 0.0 | 10.0 | 8.35 | 20.0 | Au1rxx-base64 | 64.49.38.6 |
| 76.9 | trojan | 307.1 | 569.9 | 20.67 | 0.0 | 10.0 | 14.02 | 20.0 | Au1rxx-base64 | 44.242.235.129 |
| 76.64 | shadowsocks | 294.9 | 591.5 | 20.95 | 0.0 | 9.15 | 14.08 | 20.0 | Au1rxx-base64 | 173.244.56.6 |
| 76.35 | http | 328.5 | 703.3 | 20.17 | 0.0 | 10.0 | 14.32 | 19.12 | zhangkai | 138.199.35.214 |
| 76.18 | http | 338.9 | 732.1 | 19.93 | 0.0 | 10.0 | 14.32 | 19.12 | zhangkai | 138.199.35.207 |
| 75.99 | shadowsocks | 294.1 | 691.0 | 20.97 | 0.0 | 9.16 | 14.08 | 20.0 | Au1rxx-base64 | 37.19.198.236 |
| 75.9 | http | 325.6 | 695.4 | 20.24 | 0.0 | 10.0 | 14.32 | 19.12 | zhangkai | 138.199.35.199 |
| 75.87 | shadowsocks | 272.6 | 528.4 | 21.47 | 0.0 | 9.15 | 14.08 | 20.0 | Au1rxx-base64 | 108.181.0.177 |
| 75.58 | hysteria2 | 292.3 | 706.4 | 21.01 | 0.0 | 5.62 | 12.39 | 20.0 | Au1rxx-base64 | usa1.spectrumproxy.shop |
| 75.53 | shadowsocks | 310.4 | 659.3 | 20.59 | 0.0 | 9.16 | 14.08 | 20.0 | Au1rxx-base64 | 149.22.95.183 |
| 75.46 | http | 323.9 | 688.8 | 20.28 | 0.0 | 10.0 | 14.32 | 19.12 | zhangkai | 138.199.35.217 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | 0.941 | 405 | 1577 | prefer |
| zhangkai | 0.956 | 1.0 | 20 | 25 | prefer |
| Surfboard-tg-mixed | 0.617 | 0.538 | 119 | 5904 | observe |
| mheidari-all | 0.602 | 0.588 | 17 | 20767 | observe |
| DeltaKronecker-all | 0.461 | 0.545 | 11 | 5897 | observe |
| xiaoji235-airport-v2ray-all | 0.287 | 0.5 | 2 | 5184 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5219 | observe |
| Epodonios-all | 0.255 | None | 0 | 6534 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7693 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4729 | observe |
| barry-far-vless | 0.255 | None | 0 | 5092 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5212 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| nscl5-all | 0.24 | None | 0 | 1621 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | ClientOSError | - | 24 |
| geo | TimeoutError | - | 18 |
| 204 | TimeoutError | - | 15 |
| cn-block | TimeoutError | - | 15 |
| 204 | ProxyError | - | 7 |
| speed | TimeoutError | - | 6 |
| cn-block | ClientOSError | - | 5 |
| geo | ProxyError | - | 1 |
| cn-block | ProxyError | - | 1 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
