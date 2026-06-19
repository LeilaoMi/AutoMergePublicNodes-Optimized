# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.9.1 |
| 更新时间 | 2026-06-19 10:54:28 |
| 运行耗时 | 448.1s |
| 订阅源总数 | 107 |
| 健康订阅源 | 106 |
| 原始节点 | 72574 |
| 去重后节点 | 21825 |
| TCP 可达 | 698 |
| 真实可用 | 544 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 21825 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.9 |
| geo | 1.3 |
| tcp | 66.0 |
| probe | 104.4 |
| real_test | 202.2 |
| generate | 69.3 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 41686 |
| shadowsocks | 10562 |
| trojan | 9983 |
| vmess | 9762 |
| hysteria2 | 223 |
| shadowsocksr | 159 |
| http | 107 |
| socks | 65 |
| anytls | 19 |
| hysteria | 6 |
| tuic | 2 |

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
| 77.0 | shadowsocks | 229.4 | 596.9 | 22.47 | 0.0 | 10.0 | 13.67 | 16.96 | mheidari-all | 198.98.53.130 |
| 76.56 | shadowsocks | 228.3 | 634.9 | 22.49 | 0.0 | 10.0 | 13.67 | 16.5 | Au1rxx-base64 | 37.19.198.236 |
| 76.5 | shadowsocks | 231.0 | 643.2 | 22.43 | 0.0 | 10.0 | 13.67 | 16.5 | Au1rxx-base64 | 37.19.198.160 |
| 76.39 | shadowsocks | 235.6 | 648.7 | 22.32 | 0.0 | 10.0 | 13.67 | 16.5 | Au1rxx-base64 | 37.19.198.244 |
| 75.06 | vmess | 297.0 | 818.6 | 20.9 | 0.0 | 10.0 | 12.5 | 19.76 | Surfboard-tg-mixed | 67.220.85.46 |
| 74.01 | shadowsocks | 230.5 | 637.7 | 22.44 | 0.0 | 10.0 | 13.67 | 16.5 | Au1rxx-base64 | 37.19.198.243 |
| 73.42 | shadowsocks | 282.5 | 646.3 | 21.24 | 0.0 | 10.0 | 13.67 | 16.5 | Au1rxx-base64 | 156.146.38.169 |
| 73.3 | vless | 299.8 | 629.6 | 20.84 | 0.0 | 10.0 | 10.71 | 16.5 | Au1rxx-base64 | 193.233.202.7 |
| 73.29 | shadowsocks | 280.9 | 651.3 | 21.28 | 0.0 | 10.0 | 13.67 | 16.5 | Au1rxx-base64 | 156.146.38.168 |
| 72.91 | shadowsocks | 281.1 | 655.2 | 21.27 | 0.0 | 10.0 | 13.67 | 16.5 | Au1rxx-base64 | 156.146.38.167 |
| 72.88 | vless | 339.8 | 871.5 | 19.91 | 0.0 | 10.0 | 10.71 | 16.96 | mheidari-all | 185.156.47.96 |
| 72.05 | shadowsocks | 319.0 | 765.3 | 20.39 | 0.0 | 10.0 | 13.67 | 16.5 | Au1rxx-base64 | 156.146.38.170 |
| 71.77 | vless | 340.5 | 870.0 | 19.9 | 0.0 | 10.0 | 10.71 | 19.76 | Surfboard-tg-mixed | 37.1.212.241 |
| 70.69 | vless | 326.1 | 596.8 | 20.23 | 0.0 | 10.0 | 10.71 | 19.76 | Surfboard-tg-mixed | 67.230.170.34 |
| 70.44 | shadowsocks | 427.7 | 1090.3 | 17.88 | 0.0 | 10.0 | 13.67 | 16.5 | Au1rxx-base64 | 149.28.255.6 |
| 69.98 | trojan | 456.2 | 818.3 | 17.22 | 0.0 | 10.0 | 13.36 | 19.76 | Surfboard-tg-mixed | 3.8.238.251 |
| 69.82 | trojan | 454.2 | 790.3 | 17.26 | 0.0 | 10.0 | 13.36 | 19.76 | Surfboard-tg-mixed | 212.183.88.136 |
| 69.76 | shadowsocks | 249.9 | 656.0 | 21.99 | 0.0 | 10.0 | 13.67 | 10.6 | DeltaKronecker-all | 108.181.57.93 |
| 69.66 | shadowsocks | 332.0 | 762.0 | 20.09 | 0.0 | 10.0 | 13.67 | 16.5 | Au1rxx-base64 | 107.172.250.161 |
| 69.42 | trojan | 352.4 | 606.6 | 19.62 | 0.0 | 10.0 | 13.36 | 19.76 | Surfboard-tg-mixed | 172.64.50.27 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.966 | 1.0 | 25 | 73 | prefer |
| Au1rxx-base64 | 0.916 | 0.922 | 77 | 121 | prefer |
| mheidari-all | 0.865 | 0.788 | 259 | 15002 | prefer |
| Surfboard-tg-mixed | 0.832 | 0.754 | 272 | 4682 | prefer |
| DeltaKronecker-all | 0.68 | 0.603 | 63 | 6989 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4458 | observe |
| Epodonios-all | 0.255 | None | 0 | 7124 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3975 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6752 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 3547 | observe |
| barry-far-vless | 0.255 | None | 0 | 4215 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4527 | observe |
| nscl5-all | 0.229 | None | 0 | 1360 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| cn-block | TimeoutError | - | 37 |
| speed | ClientOSError | - | 36 |
| 204 | TimeoutError | - | 24 |
| geo | TimeoutError | - | 15 |
| 204 | ProxyError | - | 15 |
| speed | TimeoutError | - | 11 |
| geo | ClientOSError | - | 8 |
| speed | ProxyError | - | 5 |
| geo | ProxyError | - | 2 |
| cn-block | ClientOSError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
