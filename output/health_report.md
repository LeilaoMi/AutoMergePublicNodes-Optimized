# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-25 08:19:17 |
| 运行耗时 | 319.6s |
| 订阅源总数 | 107 |
| 健康订阅源 | 102 |
| 原始节点 | 78921 |
| 去重后节点 | 22393 |
| TCP 可达 | 3000 |
| 真实可用 | 842 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22393 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.3 |
| geo | 1.3 |
| tcp | 31.0 |
| probe | 61.9 |
| real_test | 177.8 |
| generate | 42.2 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 45180 |
| trojan | 13285 |
| vmess | 10186 |
| shadowsocks | 9686 |
| hysteria2 | 357 |
| socks | 73 |
| shadowsocksr | 71 |
| http | 50 |
| tuic | 17 |
| hysteria | 15 |
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
| 80.47 | shadowsocks | 222.9 | 609.4 | 22.62 | 0.0 | 10.0 | 13.37 | 18.48 | Au1rxx-base64 | 198.98.53.130 |
| 80.37 | shadowsocks | 227.3 | 622.4 | 22.52 | 0.0 | 10.0 | 13.37 | 18.48 | Au1rxx-base64 | 37.19.198.236 |
| 80.31 | shadowsocks | 229.9 | 635.5 | 22.46 | 0.0 | 10.0 | 13.37 | 18.48 | Au1rxx-base64 | 37.19.198.244 |
| 80.03 | shadowsocks | 241.8 | 666.6 | 22.18 | 0.0 | 10.0 | 13.37 | 18.48 | Au1rxx-base64 | 37.19.198.243 |
| 76.95 | shadowsocks | 288.3 | 666.6 | 21.1 | 0.0 | 10.0 | 13.37 | 18.48 | Au1rxx-base64 | 156.146.38.170 |
| 76.44 | trojan | 256.4 | 694.8 | 21.84 | 0.0 | 10.0 | 14.32 | 13.28 | mheidari-all | 153.75.250.171 |
| 75.6 | trojan | 298.9 | 656.9 | 20.86 | 0.0 | 10.0 | 14.32 | 18.48 | Au1rxx-base64 | 64.94.95.115 |
| 74.95 | shadowsocks | 293.9 | 685.8 | 20.97 | 0.0 | 10.0 | 13.37 | 18.48 | Au1rxx-base64 | 156.146.38.168 |
| 74.44 | shadowsocks | 284.9 | 650.5 | 21.18 | 0.0 | 10.0 | 13.37 | 18.48 | Au1rxx-base64 | 156.146.38.169 |
| 72.88 | shadowsocks | 396.5 | 963.2 | 18.6 | 0.0 | 10.0 | 13.37 | 18.48 | Au1rxx-base64 | 108.181.57.93 |
| 72.34 | hysteria2 | 404.6 | 634.0 | 18.41 | 0.0 | 10.0 | 12.0 | 18.48 | Au1rxx-base64 | 62.210.124.146 |
| 72.21 | shadowsocks | 342.0 | 879.3 | 19.86 | 0.0 | 10.0 | 13.37 | 18.48 | Au1rxx-base64 | 185.196.61.82 |
| 71.87 | hysteria2 | 430.4 | 865.8 | 17.81 | 0.0 | 10.0 | 12.0 | 18.48 | Au1rxx-base64 | 5.255.102.165 |
| 71.78 | trojan | 301.9 | 649.0 | 20.79 | 0.0 | 10.0 | 14.32 | 13.28 | mheidari-all | 163.245.196.68 |
| 71.4 | shadowsocks | 294.1 | 679.3 | 20.97 | 0.0 | 10.0 | 13.37 | 18.48 | Au1rxx-base64 | 156.146.38.167 |
| 71.18 | trojan | 678.9 | 1850.0 | 12.06 | 0.0 | 10.0 | 14.32 | 18.48 | Au1rxx-base64 | 148.72.168.35 |
| 71.09 | shadowsocks | 348.9 | 657.8 | 19.7 | 0.0 | 10.0 | 13.37 | 18.48 | Au1rxx-base64 | 108.181.118.10 |
| 69.95 | shadowsocks | 407.5 | 859.9 | 18.35 | 0.0 | 10.0 | 13.37 | 18.48 | Au1rxx-base64 | 108.181.0.177 |
| 69.5 | shadowsocks | 404.3 | 739.7 | 18.42 | 0.0 | 10.0 | 13.37 | 18.48 | Au1rxx-base64 | 158.173.20.171 |
| 69.03 | trojan | 346.0 | 884.1 | 19.77 | 0.0 | 10.0 | 14.32 | 8.12 | DeltaKronecker-all | 64.74.163.118 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.976 | 1.0 | 36 | 61 | prefer |
| Au1rxx-base64 | 0.861 | 0.848 | 132 | 432 | prefer |
| mheidari-all | 0.845 | 0.766 | 479 | 17378 | prefer |
| DeltaKronecker-all | 0.779 | 0.7 | 227 | 5838 | prefer |
| Surfboard-tg-mixed | 0.675 | 0.596 | 282 | 5473 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4879 | observe |
| Epodonios-all | 0.255 | None | 0 | 6614 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3973 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6346 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4256 | observe |
| barry-far-vless | 0.255 | None | 0 | 4927 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5009 | observe |
| nscl5-all | 0.255 | None | 0 | 2974 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |
| 10ium-HighSpeed | 0.209 | None | 0 | 839 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 132 |
| speed | ClientOSError | - | 55 |
| cn-block | TimeoutError | - | 29 |
| 204 | ProxyError | - | 26 |
| geo | ClientOSError | - | 24 |
| 204 | TimeoutError | - | 18 |
| speed | TimeoutError | - | 14 |
| cn-block | ClientOSError | - | 7 |
| cn-block | ProxyError | - | 6 |
| geo | ProxyError | - | 4 |
| 204 | ClientOSError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
