# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-10 05:35:08 |
| 运行耗时 | 1062.8s |
| 订阅源总数 | 107 |
| 健康订阅源 | 94 |
| 原始节点 | 97887 |
| 去重后节点 | 27738 |
| TCP 可达 | 3000 |
| 真实可用 | 510 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 27738 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.7 |
| geo | 1.5 |
| tcp | 49.4 |
| probe | 344.3 |
| real_test | 559.4 |
| generate | 102.6 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 57027 |
| vmess | 15714 |
| shadowsocks | 11919 |
| trojan | 10811 |
| hysteria2 | 1565 |
| http | 555 |
| shadowsocksr | 169 |
| socks | 70 |
| anytls | 28 |
| hysteria | 17 |
| tuic | 12 |

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
| 81.09 | hysteria2 | 321.2 | 743.2 | 20.34 | 0.0 | 10.0 | 14.32 | 19.66 | Au1rxx-base64 | 129.213.91.185 |
| 80.63 | shadowsocks | 260.2 | 630.0 | 21.76 | 0.0 | 10.0 | 13.21 | 19.66 | Au1rxx-base64 | 156.146.38.169 |
| 80.6 | shadowsocks | 261.3 | 634.1 | 21.73 | 0.0 | 10.0 | 13.21 | 19.66 | Au1rxx-base64 | 156.146.38.170 |
| 80.51 | shadowsocks | 261.2 | 633.4 | 21.73 | 0.0 | 10.0 | 13.21 | 19.66 | Au1rxx-base64 | 156.146.38.167 |
| 80.19 | shadowsocks | 263.8 | 638.8 | 21.67 | 0.0 | 10.0 | 13.21 | 19.66 | Au1rxx-base64 | 156.146.38.168 |
| 77.31 | vless | 315.7 | 617.0 | 20.47 | 0.0 | 10.0 | 12.15 | 19.66 | Au1rxx-base64 | 107.173.237.146 |
| 77.11 | vless | 307.1 | 575.5 | 20.67 | 0.0 | 10.0 | 12.15 | 19.66 | Au1rxx-base64 | 47.251.108.158 |
| 75.19 | vless | 347.0 | 725.4 | 19.75 | 0.0 | 10.0 | 12.15 | 19.66 | Au1rxx-base64 | 45.32.69.110 |
| 75.13 | hysteria2 | 352.2 | 435.7 | 19.62 | 0.0 | 9.52 | 14.32 | 19.66 | Au1rxx-base64 | 158.101.148.79 |
| 74.49 | vless | 402.0 | 801.2 | 18.47 | 0.0 | 10.0 | 12.15 | 19.66 | Au1rxx-base64 | 169.40.42.232 |
| 74.26 | vless | 369.0 | 583.3 | 19.24 | 0.0 | 10.0 | 12.15 | 19.66 | Au1rxx-base64 | 137.175.82.40 |
| 74.03 | vless | 393.5 | 704.5 | 18.67 | 0.0 | 10.0 | 12.15 | 19.66 | Au1rxx-base64 | 15.204.97.197 |
| 74.01 | vless | 393.6 | 698.9 | 18.67 | 0.0 | 10.0 | 12.15 | 19.66 | Au1rxx-base64 | 15.204.97.216 |
| 73.93 | vless | 446.7 | 965.3 | 17.44 | 0.0 | 10.0 | 12.15 | 19.66 | Au1rxx-base64 | 159.89.87.21 |
| 73.85 | vless | 405.0 | 756.0 | 18.4 | 0.0 | 10.0 | 12.15 | 19.66 | Au1rxx-base64 | 169.40.42.16 |
| 73.82 | vless | 414.8 | 811.3 | 18.18 | 0.0 | 10.0 | 12.15 | 19.66 | Au1rxx-base64 | 66.70.179.198 |
| 73.8 | vless | 395.0 | 769.7 | 18.63 | 0.0 | 10.0 | 12.15 | 19.66 | Au1rxx-base64 | 169.40.42.212 |
| 73.6 | shadowsocks | 334.6 | 634.6 | 20.03 | 0.0 | 10.0 | 13.21 | 19.66 | Au1rxx-base64 | 173.244.56.9 |
| 73.59 | shadowsocks | 316.6 | 616.6 | 20.45 | 0.0 | 10.0 | 13.21 | 19.66 | Au1rxx-base64 | 5.78.51.123 |
| 73.55 | shadowsocks | 360.9 | 787.8 | 19.42 | 0.0 | 10.0 | 13.21 | 19.66 | Au1rxx-base64 | 37.19.198.160 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.997 | 0.928 | 319 | 1786 | prefer |
| zhangkai | 0.964 | 1.0 | 22 | 144 | prefer |
| Surfboard-tg-mixed | 0.759 | 0.683 | 82 | 7155 | prefer |
| ermaozi-get_subscribe | 0.578 | 0.556 | 27 | 653 | observe |
| DeltaKronecker-all | 0.467 | 0.438 | 16 | 5154 | observe |
| mheidari-all | 0.411 | 0.33 | 339 | 23395 | observe |
| 10ium-ScrapeCategorize-Vless | 0.335 | 1.0 | 1 | 4984 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| Epodonios-all | 0.255 | None | 0 | 7634 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9590 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5643 | observe |
| barry-far-vless | 0.255 | None | 0 | 5793 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4346 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 148 |
| speed | TimeoutError | - | 39 |
| geo | ClientOSError | - | 34 |
| 204 | ProxyError | - | 23 |
| speed | ClientOSError | - | 22 |
| cn-block | TimeoutError | - | 12 |
| 204 | TimeoutError | - | 9 |
| 204 | ClientOSError | - | 5 |
| cn-block | ClientOSError | - | 5 |
| cn-block | ProxyError | - | 3 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
