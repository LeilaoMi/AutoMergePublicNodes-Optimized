# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-06-17 18:01:28 |
| 运行耗时 | 110.9s |
| 订阅源总数 | 44 |
| 健康订阅源 | 44 |
| 原始节点 | 43727 |
| 去重后节点 | 18109 |
| TCP 可达 | 1500 |
| 真实可用 | 51 |
| Verified 输出 | 51 |
| Global 输出 | 51 |
| All 输出 | 18109 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 3.1 |
| geo | 1.2 |
| tcp | 19.6 |
| probe | 26.4 |
| real_test | 40.3 |
| generate | 20.3 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 22438 |
| shadowsocks | 8317 |
| trojan | 7055 |
| vmess | 5486 |
| hysteria2 | 204 |
| http | 95 |
| shadowsocksr | 87 |
| socks | 38 |
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
| 57.44 | vless | 333.6 | 862.1 | 20.05 | 0.0 | 10.0 | 1.29 | 12.1 | DeltaKronecker-all | 69.46.46.10 |
| 55.46 | vmess | 513.9 | 808.2 | 15.88 | 0.0 | 10.0 | 12.86 | 12.1 | DeltaKronecker-all | 45.90.106.24 |
| 53.83 | vmess | 593.8 | 1080.2 | 14.03 | 0.0 | 10.0 | 12.86 | 12.1 | DeltaKronecker-all | 51.89.41.22 |
| 53.68 | vmess | 598.5 | 1103.5 | 13.92 | 0.0 | 10.0 | 12.86 | 12.1 | DeltaKronecker-all | 141.95.65.9 |
| 52.29 | trojan | 517.3 | 787.8 | 15.8 | 0.0 | 10.0 | 7.61 | 12.1 | DeltaKronecker-all | 104.17.121.43 |
| 52.26 | trojan | 512.7 | 809.1 | 15.91 | 0.0 | 10.0 | 7.61 | 12.1 | DeltaKronecker-all | 45.130.125.75 |
| 52.18 | trojan | 514.1 | 764.7 | 15.88 | 0.0 | 10.0 | 7.61 | 12.1 | DeltaKronecker-all | 162.159.253.41 |
| 51.65 | trojan | 528.4 | 748.3 | 15.55 | 0.0 | 10.0 | 7.61 | 12.1 | DeltaKronecker-all | 104.16.122.175 |
| 51.11 | vmess | 326.6 | 582.2 | 20.22 | 0.0 | 10.0 | 12.86 | 5.24 | Barabama-yudou | 82.198.246.233 |
| 50.82 | trojan | 504.3 | 744.2 | 16.11 | 0.0 | 10.0 | 7.61 | 12.1 | DeltaKronecker-all | 45.130.125.76 |
| 49.5 | hysteria2 | 393.0 | 675.4 | 18.68 | 0.0 | 10.0 | 7.5 | 5.2 | Au1rxx-base64 | 62.210.124.146 |
| 48.24 | http | 712.3 | 925.5 | 11.29 | 0.0 | 9.71 | 14.42 | 9.18 | snakem982 | 84.239.49.253 |
| 48.03 | http | 715.0 | 945.5 | 11.23 | 0.0 | 9.71 | 14.42 | 9.18 | snakem982 | 84.239.14.159 |
| 47.79 | http | 729.8 | 965.2 | 10.89 | 0.0 | 9.75 | 14.42 | 9.18 | snakem982 | 84.239.14.158 |
| 47.54 | http | 722.2 | 945.6 | 11.06 | 0.0 | 9.3 | 14.42 | 9.18 | snakem982 | 84.239.14.148 |
| 47.13 | http | 759.4 | 1036.6 | 10.2 | 0.0 | 9.71 | 14.42 | 9.18 | snakem982 | 84.239.49.39 |
| 46.96 | http | 769.4 | 1120.0 | 9.97 | 0.0 | 9.68 | 14.42 | 9.18 | snakem982 | 84.239.49.173 |
| 46.92 | http | 765.7 | 1099.7 | 10.05 | 0.0 | 9.58 | 14.42 | 9.18 | snakem982 | 84.239.49.162 |
| 46.91 | http | 770.0 | 1159.7 | 9.95 | 0.0 | 9.66 | 14.42 | 9.18 | snakem982 | 84.239.49.154 |
| 46.74 | trojan | 754.3 | 814.9 | 10.32 | 0.0 | 10.0 | 7.61 | 12.1 | DeltaKronecker-all | 104.17.121.9 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.964 | 1.0 | 24 | 73 | prefer |
| DeltaKronecker-all | 0.38 | 0.295 | 78 | 7763 | observe |
| Surfboard-tg-mixed | 0.32 | 0.5 | 4 | 4729 | observe |
| Au1rxx-base64 | 0.26 | 1.0 | 1 | 118 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 2000 | observe |
| Epodonios-all | 0.255 | None | 0 | 3000 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3000 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 3000 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 3741 | observe |
| barry-far-vless | 0.255 | None | 0 | 2000 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4541 | observe |
| mheidari-all | 0.255 | None | 0 | 2000 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |
| Barabama-yudou | 0.214 | 0.5 | 2 | 166 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 16 |
| 204 | ProxyError | - | 11 |
| 204 | TimeoutError | - | 11 |
| geo | status | 429 | 6 |
| cn-block | ClientOSError | - | 3 |
| speed | ProxyError | - | 3 |
| cn-block | TimeoutError | - | 3 |
| geo | ProxyError | - | 2 |
| geo | status | 403 | 1 |
| speed | TimeoutError | - | 1 |
| cn-block | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 102 | 51 | - |
| global | False | 106 | 51 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
