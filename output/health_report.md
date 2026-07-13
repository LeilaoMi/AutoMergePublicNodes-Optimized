# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-13 19:39:12 |
| 运行耗时 | 186.5s |
| 订阅源总数 | 107 |
| 健康订阅源 | 102 |
| 原始节点 | 77315 |
| 去重后节点 | 23920 |
| TCP 可达 | 3000 |
| 真实可用 | 205 |
| Verified 输出 | 205 |
| Global 输出 | 214 |
| All 输出 | 23920 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.7 |
| geo | 1.3 |
| tcp | 32.5 |
| probe | 43.6 |
| real_test | 68.8 |
| generate | 35.6 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 44894 |
| trojan | 11369 |
| vmess | 10794 |
| shadowsocks | 9485 |
| hysteria2 | 449 |
| shadowsocksr | 152 |
| http | 138 |
| socks | 27 |
| hysteria | 6 |
| tuic | 1 |

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
| 72.4 | shadowsocks | 252.0 | 622.6 | 21.94 | 0.0 | 10.0 | 11.72 | 12.74 | mheidari-all | 198.98.53.130 |
| 70.42 | shadowsocks | 316.1 | 794.4 | 20.46 | 0.0 | 10.0 | 11.72 | 12.74 | mheidari-all | 185.196.61.82 |
| 69.92 | shadowsocks | 292.2 | 719.5 | 21.01 | 0.0 | 10.0 | 11.72 | 12.74 | mheidari-all | 108.181.57.93 |
| 63.95 | http | 691.5 | 965.7 | 11.77 | 0.0 | 9.54 | 14.61 | 19.52 | snakem982 | 84.239.49.154 |
| 63.87 | http | 696.3 | 993.1 | 11.66 | 0.0 | 9.58 | 14.61 | 19.52 | snakem982 | 84.239.49.253 |
| 63.79 | http | 697.7 | 979.3 | 11.63 | 0.0 | 9.54 | 14.61 | 19.52 | snakem982 | 84.239.49.209 |
| 63.63 | http | 701.0 | 1020.5 | 11.55 | 0.0 | 9.54 | 14.61 | 19.52 | snakem982 | 84.239.49.40 |
| 63.6 | http | 704.5 | 994.2 | 11.47 | 0.0 | 9.54 | 14.61 | 19.52 | snakem982 | 84.239.49.245 |
| 63.5 | http | 709.4 | 1023.3 | 11.36 | 0.0 | 9.48 | 14.61 | 19.52 | snakem982 | 84.239.49.157 |
| 63.5 | http | 713.0 | 1039.7 | 11.27 | 0.0 | 9.6 | 14.61 | 19.52 | snakem982 | 84.239.49.196 |
| 63.48 | http | 707.3 | 1002.6 | 11.4 | 0.0 | 9.48 | 14.61 | 19.52 | snakem982 | 84.239.49.207 |
| 63.45 | http | 708.0 | 988.4 | 11.39 | 0.0 | 9.47 | 14.61 | 19.52 | snakem982 | 84.239.49.247 |
| 63.45 | http | 708.6 | 1016.7 | 11.38 | 0.0 | 9.54 | 14.61 | 19.52 | snakem982 | 84.239.14.159 |
| 63.44 | http | 711.6 | 1007.5 | 11.3 | 0.0 | 9.54 | 14.61 | 19.52 | snakem982 | 84.239.14.152 |
| 63.41 | http | 719.0 | 1135.4 | 11.14 | 0.0 | 9.49 | 14.61 | 19.52 | snakem982 | 193.176.84.32 |
| 63.3 | http | 715.8 | 1017.7 | 11.21 | 0.0 | 9.47 | 14.61 | 19.52 | snakem982 | 84.239.49.185 |
| 63.27 | http | 716.2 | 1003.3 | 11.2 | 0.0 | 9.54 | 14.61 | 19.52 | snakem982 | 84.239.49.55 |
| 63.24 | http | 722.8 | 1010.6 | 11.05 | 0.0 | 9.54 | 14.61 | 19.52 | snakem982 | 84.239.49.211 |
| 63.21 | http | 722.5 | 1040.2 | 11.05 | 0.0 | 9.54 | 14.61 | 19.52 | snakem982 | 84.239.49.42 |
| 63.2 | http | 721.9 | 1024.4 | 11.07 | 0.0 | 9.55 | 14.61 | 19.52 | snakem982 | 84.239.49.57 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| mheidari-all | 0.771 | 0.698 | 53 | 16297 | prefer |
| DeltaKronecker-all | 0.723 | 0.646 | 96 | 7926 | prefer |
| Surfboard-tg-mixed | 0.673 | 0.595 | 116 | 5561 | observe |
| Au1rxx-base64 | 0.259 | 1.0 | 1 | 91 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 3897 | observe |
| Epodonios-all | 0.255 | None | 0 | 6496 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3971 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6673 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4279 | observe |
| barry-far-vless | 0.255 | None | 0 | 4810 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5454 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| xiaoji235-airport-v2ray-all | 0.241 | None | 0 | 1647 | observe |
| nscl5-all | 0.236 | None | 0 | 1526 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 27 |
| speed | ClientOSError | - | 20 |
| 204 | TimeoutError | - | 19 |
| cn-block | TimeoutError | - | 8 |
| cn-block | ClientOSError | - | 6 |
| 204 | ProxyError | - | 6 |
| cn-block | ProxyError | - | 3 |
| geo | ClientOSError | - | 2 |
| 204 | ClientOSError | - | 2 |
| geo | ProxyError | - | 2 |
| speed | ProxyError | - | 2 |
| speed | TimeoutError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 208 | 205 | - |
| global | False | 222 | 214 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
