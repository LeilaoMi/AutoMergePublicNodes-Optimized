# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-06-17 16:49:04 |
| 运行耗时 | 142.2s |
| 订阅源总数 | 44 |
| 健康订阅源 | 44 |
| 原始节点 | 43696 |
| 去重后节点 | 18218 |
| TCP 可达 | 272 |
| 真实可用 | 140 |
| Verified 输出 | 140 |
| Global 输出 | 142 |
| All 输出 | 18218 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 3.1 |
| geo | 1.2 |
| tcp | 40.4 |
| probe | 31.6 |
| real_test | 50.1 |
| generate | 15.8 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 22386 |
| shadowsocks | 8331 |
| trojan | 7097 |
| vmess | 5473 |
| hysteria2 | 174 |
| http | 95 |
| shadowsocksr | 95 |
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
| 55.68 | shadowsocks | 240.1 | 621.4 | 22.22 | 0.0 | 10.0 | 3.56 | 9.4 | Au1rxx-base64 | 37.19.198.236 |
| 55.63 | shadowsocks | 242.2 | 626.5 | 22.17 | 0.0 | 10.0 | 3.56 | 9.4 | Au1rxx-base64 | 37.19.198.244 |
| 55.53 | shadowsocks | 246.5 | 634.8 | 22.07 | 0.0 | 10.0 | 3.56 | 9.4 | Au1rxx-base64 | 37.19.198.243 |
| 55.46 | shadowsocks | 249.6 | 651.4 | 22.0 | 0.0 | 10.0 | 3.56 | 9.4 | Au1rxx-base64 | 37.19.198.160 |
| 52.45 | shadowsocks | 283.0 | 635.4 | 21.23 | 0.0 | 10.0 | 3.56 | 9.4 | Au1rxx-base64 | 156.146.38.170 |
| 52.29 | shadowsocks | 287.7 | 651.4 | 21.12 | 0.0 | 10.0 | 3.56 | 9.4 | Au1rxx-base64 | 156.146.38.167 |
| 52.2 | shadowsocks | 290.5 | 653.0 | 21.05 | 0.0 | 10.0 | 3.56 | 9.4 | Au1rxx-base64 | 156.146.38.169 |
| 50.47 | shadowsocks | 378.8 | 922.7 | 19.01 | 0.0 | 10.0 | 3.56 | 9.4 | Au1rxx-base64 | 149.28.255.6 |
| 49.84 | shadowsocks | 301.4 | 771.3 | 20.8 | 0.0 | 10.0 | 3.56 | 4.98 | mheidari-all | 198.98.53.130 |
| 49.76 | shadowsocks | 245.4 | 652.1 | 22.1 | 0.0 | 10.0 | 3.56 | 3.6 | DeltaKronecker-all | 108.181.57.93 |
| 49.7 | shadowsocks | 334.8 | 774.9 | 20.03 | 0.0 | 10.0 | 3.56 | 9.4 | Au1rxx-base64 | 107.172.250.161 |
| 48.64 | shadowsocks | 319.3 | 584.1 | 20.39 | 0.0 | 10.0 | 3.56 | 9.4 | Au1rxx-base64 | 173.244.56.9 |
| 48.06 | http | 733.1 | 983.7 | 10.81 | 0.0 | 9.63 | 13.45 | 10.56 | snakem982 | 84.239.14.148 |
| 47.79 | shadowsocks | 355.4 | 701.4 | 19.55 | 0.0 | 10.0 | 3.56 | 9.4 | Au1rxx-base64 | 173.244.56.6 |
| 47.52 | shadowsocks | 344.8 | 578.6 | 19.8 | 0.0 | 10.0 | 3.56 | 9.4 | Au1rxx-base64 | 149.22.95.183 |
| 47.47 | http | 761.1 | 1081.2 | 10.16 | 0.0 | 9.7 | 13.45 | 10.56 | snakem982 | 84.239.14.158 |
| 47.33 | http | 760.8 | 1045.3 | 10.17 | 0.0 | 9.58 | 13.45 | 10.56 | snakem982 | 84.239.49.201 |
| 47.26 | http | 770.0 | 1080.5 | 9.95 | 0.0 | 9.73 | 13.45 | 10.56 | snakem982 | 84.239.14.159 |
| 47.22 | http | 775.7 | 1060.1 | 9.82 | 0.0 | 9.71 | 13.45 | 10.56 | snakem982 | 84.239.49.57 |
| 47.16 | http | 777.6 | 1099.9 | 9.78 | 0.0 | 9.71 | 13.45 | 10.56 | snakem982 | 84.239.49.185 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| DeltaKronecker-all | 0.699 | 0.625 | 40 | 7763 | observe |
| ninja-vless | 0.685 | 0.621 | 29 | 1791 | observe |
| roosterkid-openproxylist-v2ray | 0.683 | 0.812 | 16 | 150 | observe |
| Au1rxx-base64 | 0.519 | 0.515 | 66 | 115 | observe |
| snakem982 | 0.47 | 0.466 | 58 | 73 | observe |
| Surfboard-tg-mixed | 0.441 | 0.353 | 34 | 4729 | observe |
| mheidari-all | 0.426 | 0.333 | 24 | 2000 | observe |
| nscl5-all | 0.294 | 1.0 | 1 | 967 | observe |
| SoliSpirit-all | 0.287 | 0.5 | 2 | 3000 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 2000 | observe |
| Epodonios-all | 0.255 | None | 0 | 3000 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3000 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 3741 | observe |
| barry-far-vless | 0.255 | None | 0 | 2000 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4541 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | status | 429 | 55 |
| geo | status | 403 | 50 |
| speed | ClientOSError | - | 7 |
| cn-block | ClientOSError | - | 6 |
| 204 | TimeoutError | - | 5 |
| cn-block | TimeoutError | - | 3 |
| 204 | ClientOSError | - | 3 |
| geo | TimeoutError | - | 2 |
| speed | TimeoutError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 236 | 140 | - |
| global | False | 249 | 142 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
