# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-06-17 18:40:17 |
| 运行耗时 | 186.4s |
| 订阅源总数 | 44 |
| 健康订阅源 | 44 |
| 原始节点 | 43687 |
| 去重后节点 | 18013 |
| TCP 可达 | 1500 |
| 真实可用 | 190 |
| Verified 输出 | 190 |
| Global 输出 | 199 |
| All 输出 | 18013 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 3.4 |
| geo | 1.2 |
| tcp | 19.4 |
| probe | 40.8 |
| real_test | 89.9 |
| generate | 31.7 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 22475 |
| shadowsocks | 8338 |
| trojan | 7003 |
| vmess | 5446 |
| hysteria2 | 198 |
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
| 59.85 | vless | 265.7 | 722.0 | 21.63 | 0.0 | 10.0 | 5.62 | 7.6 | DeltaKronecker-all | 47.253.226.114 |
| 58.89 | vless | 307.2 | 790.5 | 20.67 | 0.0 | 10.0 | 5.62 | 7.6 | DeltaKronecker-all | 152.53.171.40 |
| 58.41 | vless | 327.7 | 767.5 | 20.19 | 0.0 | 10.0 | 5.62 | 7.6 | DeltaKronecker-all | 154.88.3.147 |
| 58.28 | shadowsocks | 241.9 | 613.6 | 22.18 | 0.0 | 10.0 | 7.5 | 7.6 | DeltaKronecker-all | 147.90.234.133 |
| 57.64 | http | 730.9 | 928.3 | 10.86 | 0.0 | 9.58 | 14.42 | 19.28 | snakem982 | 84.239.49.178 |
| 57.59 | http | 728.6 | 957.2 | 10.91 | 0.0 | 9.59 | 14.42 | 19.28 | snakem982 | 84.239.49.173 |
| 57.58 | vless | 363.5 | 976.1 | 19.36 | 0.0 | 10.0 | 5.62 | 7.6 | DeltaKronecker-all | 193.202.11.143 |
| 57.54 | http | 748.9 | 1060.7 | 10.44 | 0.0 | 9.71 | 14.42 | 19.28 | snakem982 | 84.239.49.211 |
| 57.4 | http | 748.2 | 1043.4 | 10.46 | 0.0 | 9.68 | 14.42 | 19.28 | snakem982 | 84.239.49.202 |
| 57.18 | http | 755.3 | 1043.1 | 10.29 | 0.0 | 9.68 | 14.42 | 19.28 | snakem982 | 84.239.49.199 |
| 57.18 | http | 763.6 | 1090.0 | 10.1 | 0.0 | 9.71 | 14.42 | 19.28 | snakem982 | 84.239.49.57 |
| 57.1 | http | 759.0 | 946.5 | 10.21 | 0.0 | 9.59 | 14.42 | 19.28 | snakem982 | 84.239.49.154 |
| 56.93 | http | 770.3 | 1081.3 | 9.95 | 0.0 | 9.66 | 14.42 | 19.28 | snakem982 | 84.239.49.201 |
| 56.87 | http | 775.0 | 1141.0 | 9.84 | 0.0 | 9.7 | 14.42 | 19.28 | snakem982 | 84.239.49.215 |
| 56.84 | http | 776.8 | 1092.9 | 9.8 | 0.0 | 9.71 | 14.42 | 19.28 | snakem982 | 84.239.49.184 |
| 56.83 | http | 776.6 | 1114.3 | 9.8 | 0.0 | 9.71 | 14.42 | 19.28 | snakem982 | 84.239.14.159 |
| 56.83 | http | 777.5 | 1152.2 | 9.78 | 0.0 | 9.72 | 14.42 | 19.28 | snakem982 | 84.239.14.158 |
| 56.79 | http | 774.4 | 1100.3 | 9.85 | 0.0 | 9.67 | 14.42 | 19.28 | snakem982 | 84.239.49.214 |
| 56.75 | http | 779.9 | 1115.3 | 9.73 | 0.0 | 9.72 | 14.42 | 19.28 | snakem982 | 84.239.49.185 |
| 56.54 | http | 784.8 | 1131.3 | 9.61 | 0.0 | 9.65 | 14.42 | 19.28 | snakem982 | 84.239.49.212 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.459 | 0.455 | 55 | 73 | observe |
| DeltaKronecker-all | 0.355 | 0.275 | 590 | 7763 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| Au1rxx-base64 | 0.259 | 1.0 | 1 | 108 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 2000 | observe |
| Epodonios-all | 0.255 | None | 0 | 3000 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3000 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 3000 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 3741 | observe |
| barry-far-vless | 0.255 | None | 0 | 2000 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4541 | observe |
| mheidari-all | 0.255 | None | 0 | 2000 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Surfboard-tg-mixed | 0.226 | 0.2 | 5 | 4729 | downweight |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | status | 429 | 351 |
| speed | ClientOSError | - | 40 |
| geo | status | 403 | 18 |
| 204 | ProxyError | - | 13 |
| speed | TimeoutError | - | 12 |
| cn-block | TimeoutError | - | 8 |
| 204 | TimeoutError | - | 6 |
| 204 | ClientOSError | - | 4 |
| cn-block | ClientOSError | - | 3 |
| geo | ProxyError | - | 3 |
| cn-block | ProxyError | - | 2 |
| geo | TimeoutError | - | 1 |
| geo | ClientOSError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 51 | 190 | - |
| global | False | 51 | 199 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
