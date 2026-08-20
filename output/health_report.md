# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-20 01:42:04 |
| 运行耗时 | 399.9s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 91151 |
| 去重后节点 | 23547 |
| TCP 可达 | 3000 |
| 真实可用 | 1275 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23547 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.7 |
| geo | 1.1 |
| tcp | 37.1 |
| probe | 77.3 |
| real_test | 242.2 |
| generate | 37.6 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 51054 |
| trojan | 17474 |
| shadowsocks | 10763 |
| vmess | 9626 |
| hysteria2 | 1682 |
| shadowsocksr | 198 |
| http | 165 |
| socks | 131 |
| anytls | 33 |
| hysteria | 15 |
| tuic | 10 |

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
| 84.77 | trojan | 232.9 | 534.4 | 22.39 | 0.0 | 10.0 | 14.88 | 20.0 | mheidari-all | 34.222.243.142 |
| 84.72 | trojan | 234.7 | 536.5 | 22.34 | 0.0 | 10.0 | 14.88 | 20.0 | mheidari-all | 44.246.163.102 |
| 84.62 | trojan | 239.4 | 552.4 | 22.24 | 0.0 | 10.0 | 14.88 | 20.0 | mheidari-all | 35.90.27.143 |
| 84.58 | trojan | 240.8 | 548.8 | 22.2 | 0.0 | 10.0 | 14.88 | 20.0 | Au1rxx-base64 | 35.91.138.234 |
| 84.52 | trojan | 222.1 | 538.1 | 22.64 | 0.0 | 10.0 | 14.88 | 20.0 | mheidari-all | 14.1.28.76 |
| 84.39 | trojan | 240.4 | 562.5 | 22.21 | 0.0 | 10.0 | 14.88 | 20.0 | Au1rxx-base64 | 54.213.46.211 |
| 84.34 | trojan | 238.8 | 555.7 | 22.25 | 0.0 | 10.0 | 14.88 | 20.0 | Au1rxx-base64 | 34.210.213.17 |
| 84.2 | trojan | 239.2 | 556.7 | 22.24 | 0.0 | 10.0 | 14.88 | 20.0 | mheidari-all | 54.245.126.186 |
| 83.84 | trojan | 272.9 | 657.1 | 21.46 | 0.0 | 10.0 | 14.88 | 20.0 | Au1rxx-base64 | 44.247.89.62 |
| 83.76 | trojan | 276.2 | 661.3 | 21.38 | 0.0 | 10.0 | 14.88 | 20.0 | mheidari-all | 44.243.85.47 |
| 83.57 | trojan | 241.4 | 560.5 | 22.19 | 0.0 | 10.0 | 14.88 | 20.0 | Au1rxx-base64 | 35.88.120.18 |
| 83.54 | trojan | 285.7 | 693.2 | 21.16 | 0.0 | 10.0 | 14.88 | 20.0 | Au1rxx-base64 | 35.160.249.189 |
| 83.46 | trojan | 289.3 | 698.7 | 21.08 | 0.0 | 10.0 | 14.88 | 20.0 | Au1rxx-base64 | 34.220.224.252 |
| 83.34 | trojan | 294.7 | 702.1 | 20.96 | 0.0 | 10.0 | 14.88 | 20.0 | Au1rxx-base64 | 35.92.245.6 |
| 83.33 | vless | 260.0 | 623.1 | 21.76 | 0.0 | 10.0 | 11.57 | 20.0 | Au1rxx-base64 | 38.244.21.216 |
| 83.32 | trojan | 287.6 | 701.2 | 21.12 | 0.0 | 10.0 | 14.88 | 20.0 | Au1rxx-base64 | 100.22.163.167 |
| 83.32 | trojan | 295.4 | 725.8 | 20.94 | 0.0 | 10.0 | 14.88 | 20.0 | mheidari-all | 35.88.210.26 |
| 83.12 | trojan | 286.3 | 695.2 | 21.15 | 0.0 | 10.0 | 14.88 | 20.0 | mheidari-all | 54.188.176.255 |
| 82.6 | trojan | 240.0 | 559.5 | 22.22 | 0.0 | 10.0 | 14.88 | 20.0 | Au1rxx-base64 | 34.221.30.108 |
| 82.19 | shadowsocks | 201.0 | 476.9 | 23.13 | 0.0 | 10.0 | 13.56 | 20.0 | mheidari-all | 108.181.0.177 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | 0.991 | 680 | 1789 | prefer |
| zhangkai | 0.997 | 1.0 | 113 | 144 | prefer |
| Surfboard-tg-mixed | 0.734 | 0.667 | 24 | 6430 | prefer |
| mheidari-all | 0.681 | 0.601 | 784 | 20672 | observe |
| xiaoji235-airport-v2ray-all | 0.335 | 1.0 | 1 | 5974 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5067 | observe |
| Epodonios-all | 0.255 | None | 0 | 7184 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3987 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7353 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5059 | observe |
| barry-far-vless | 0.255 | None | 0 | 5381 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4086 | observe |
| Au1rxx-clash | 0.247 | None | 0 | 1789 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |
| 10ium-HighSpeed | 0.209 | None | 0 | 839 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 128 |
| geo | ClientOSError | - | 85 |
| speed | TimeoutError | - | 75 |
| speed | ClientOSError | - | 19 |
| cn-block | TimeoutError | - | 14 |
| 204 | TimeoutError | - | 7 |
| cn-block | ClientOSError | - | 6 |
| 204 | ClientOSError | - | 6 |
| 204 | ProxyError | - | 4 |
| cn-block | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
