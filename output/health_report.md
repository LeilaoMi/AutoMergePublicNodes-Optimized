# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-22 14:13:58 |
| 运行耗时 | 323.5s |
| 订阅源总数 | 107 |
| 健康订阅源 | 102 |
| 原始节点 | 82354 |
| 去重后节点 | 22753 |
| TCP 可达 | 3000 |
| 真实可用 | 700 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22753 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.6 |
| geo | 1.3 |
| tcp | 31.9 |
| probe | 61.2 |
| real_test | 173.4 |
| generate | 51.1 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 48313 |
| trojan | 12656 |
| vmess | 10776 |
| shadowsocks | 10014 |
| hysteria2 | 398 |
| shadowsocksr | 78 |
| http | 50 |
| socks | 46 |
| hysteria | 16 |
| tuic | 5 |
| anytls | 2 |

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
| 77.63 | shadowsocks | 242.7 | 596.9 | 22.16 | 0.0 | 10.0 | 12.55 | 16.92 | Au1rxx-base64 | 156.146.38.169 |
| 76.28 | shadowsocks | 288.5 | 673.2 | 21.1 | 0.0 | 10.0 | 12.55 | 16.92 | Au1rxx-base64 | 37.19.198.160 |
| 75.52 | trojan | 401.6 | 1038.7 | 18.48 | 0.0 | 10.0 | 13.74 | 16.92 | Au1rxx-base64 | 64.94.95.117 |
| 75.35 | shadowsocks | 303.5 | 696.5 | 20.75 | 0.0 | 10.0 | 12.55 | 16.92 | Au1rxx-base64 | 37.19.198.236 |
| 74.5 | shadowsocks | 248.3 | 617.9 | 22.03 | 0.0 | 10.0 | 12.55 | 16.92 | Au1rxx-base64 | 156.146.38.170 |
| 74.27 | shadowsocks | 301.6 | 782.5 | 20.8 | 0.0 | 10.0 | 12.55 | 16.92 | Au1rxx-base64 | 156.146.38.168 |
| 73.86 | trojan | 445.8 | 1200.4 | 17.46 | 0.0 | 10.0 | 13.74 | 16.92 | Au1rxx-base64 | 64.94.95.114 |
| 73.81 | shadowsocks | 297.0 | 678.1 | 20.9 | 0.0 | 10.0 | 12.55 | 16.92 | Au1rxx-base64 | 37.19.198.243 |
| 73.16 | shadowsocks | 309.7 | 741.8 | 20.61 | 0.0 | 10.0 | 12.55 | 16.92 | Au1rxx-base64 | 37.19.198.244 |
| 72.13 | trojan | 574.9 | 1520.8 | 14.47 | 0.0 | 10.0 | 13.74 | 16.92 | Au1rxx-base64 | 148.72.168.35 |
| 72.12 | shadowsocks | 249.0 | 611.2 | 22.01 | 0.0 | 10.0 | 12.55 | 16.92 | Au1rxx-base64 | 156.146.38.167 |
| 71.84 | trojan | 587.4 | 1638.8 | 14.18 | 0.0 | 10.0 | 13.74 | 16.92 | Au1rxx-base64 | 64.94.95.115 |
| 71.77 | shadowsocks | 352.5 | 835.8 | 19.62 | 0.0 | 10.0 | 12.55 | 16.92 | Au1rxx-base64 | 185.196.61.82 |
| 71.67 | trojan | 594.7 | 1617.4 | 14.01 | 0.0 | 10.0 | 13.74 | 16.92 | Au1rxx-base64 | 64.94.95.118 |
| 70.95 | shadowsocks | 354.1 | 805.7 | 19.58 | 0.0 | 10.0 | 12.55 | 16.92 | Au1rxx-base64 | 173.244.56.9 |
| 70.92 | trojan | 339.6 | 630.5 | 19.92 | 0.0 | 10.0 | 13.74 | 16.92 | Au1rxx-base64 | 35.87.202.76 |
| 70.9 | trojan | 374.7 | 755.0 | 19.1 | 0.0 | 10.0 | 13.74 | 16.92 | Au1rxx-base64 | 44.252.127.212 |
| 70.74 | trojan | 340.7 | 651.7 | 19.89 | 0.0 | 10.0 | 13.74 | 16.92 | Au1rxx-base64 | 44.243.114.31 |
| 70.65 | shadowsocks | 322.6 | 661.7 | 20.31 | 0.0 | 10.0 | 12.55 | 16.92 | Au1rxx-base64 | 149.22.95.183 |
| 70.29 | shadowsocks | 355.6 | 750.0 | 19.55 | 0.0 | 10.0 | 12.55 | 16.92 | Au1rxx-base64 | 173.244.56.6 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.976 | 1.0 | 36 | 61 | prefer |
| mheidari-all | 0.887 | 0.809 | 377 | 19287 | prefer |
| Au1rxx-base64 | 0.828 | 0.813 | 193 | 432 | prefer |
| DeltaKronecker-all | 0.712 | 0.634 | 123 | 5212 | prefer |
| Surfboard-tg-mixed | 0.608 | 0.528 | 231 | 5364 | observe |
| xiaoji235-airport-v2ray-all | 0.391 | 1.0 | 2 | 4246 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4613 | observe |
| Epodonios-all | 0.255 | None | 0 | 6476 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3970 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6830 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4267 | observe |
| barry-far-vless | 0.255 | None | 0 | 4805 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5204 | observe |
| nscl5-all | 0.255 | None | 0 | 2197 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 81 |
| speed | ClientOSError | - | 61 |
| cn-block | TimeoutError | - | 55 |
| 204 | TimeoutError | - | 15 |
| 204 | ProxyError | - | 14 |
| cn-block | ClientOSError | - | 12 |
| geo | ClientOSError | - | 10 |
| speed | TimeoutError | - | 5 |
| cn-block | ProxyError | - | 4 |
| 204 | ClientOSError | - | 3 |
| speed | ProxyError | - | 2 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
