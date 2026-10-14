# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-14 10:50:30 |
| 运行耗时 | 383.0s |
| 订阅源总数 | 107 |
| 健康订阅源 | 93 |
| 原始节点 | 98335 |
| 去重后节点 | 27212 |
| TCP 可达 | 3000 |
| 真实可用 | 73 |
| Verified 输出 | 73 |
| Global 输出 | 80 |
| All 输出 | 27212 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.3 |
| geo | 1.6 |
| tcp | 118.9 |
| probe | 111.0 |
| real_test | 84.4 |
| generate | 59.7 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 58084 |
| vmess | 16124 |
| shadowsocks | 11840 |
| trojan | 10198 |
| hysteria2 | 1304 |
| http | 483 |
| shadowsocksr | 167 |
| socks | 86 |
| anytls | 25 |
| hysteria | 18 |
| tuic | 6 |

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
| 80.51 | vless | 204.2 | 496.9 | 23.05 | 0.0 | 10.0 | 8.64 | 18.82 | Au1rxx-base64 | 45.32.69.110 |
| 80.5 | vless | 204.7 | 513.0 | 23.04 | 0.0 | 10.0 | 8.64 | 18.82 | Au1rxx-base64 | 144.202.126.147 |
| 80.3 | shadowsocks | 261.9 | 624.5 | 21.71 | 0.0 | 10.0 | 13.77 | 18.82 | Au1rxx-base64 | 156.146.38.170 |
| 79.9 | vless | 211.3 | 525.8 | 22.89 | 0.0 | 9.55 | 8.64 | 18.82 | Au1rxx-base64 | 154.29.145.196 |
| 79.05 | vless | 247.8 | 591.1 | 22.04 | 0.0 | 9.55 | 8.64 | 18.82 | Au1rxx-base64 | 154.12.38.159 |
| 75.07 | shadowsocks | 259.0 | 613.2 | 21.78 | 0.0 | 10.0 | 13.77 | 18.82 | Au1rxx-base64 | 156.146.38.168 |
| 73.84 | hysteria2 | 331.0 | 675.0 | 20.12 | 0.0 | 9.93 | 11.84 | 18.82 | Au1rxx-base64 | 66.94.121.46 |
| 73.14 | shadowsocks | 365.8 | 795.9 | 19.31 | 0.0 | 10.0 | 13.77 | 18.82 | Au1rxx-base64 | 37.19.198.160 |
| 71.71 | shadowsocks | 369.3 | 794.6 | 19.23 | 0.0 | 9.73 | 13.77 | 18.82 | Au1rxx-base64 | 37.19.198.243 |
| 71.15 | shadowsocks | 285.5 | 624.2 | 21.17 | 0.0 | 10.0 | 13.77 | 18.82 | Au1rxx-base64 | 149.22.95.183 |
| 68.87 | hysteria2 | 319.7 | 742.6 | 20.38 | 0.0 | 6.17 | 11.84 | 18.82 | Au1rxx-base64 | 129.213.91.185 |
| 68.58 | shadowsocks | 366.3 | 805.9 | 19.3 | 0.0 | 7.61 | 13.77 | 18.82 | Au1rxx-base64 | 37.19.198.236 |
| 67.44 | trojan | 453.3 | 875.1 | 17.28 | 0.0 | 2.81 | 13.88 | 18.82 | Au1rxx-base64 | 107.149.159.190 |
| 66.32 | vless | 438.0 | 843.9 | 17.64 | 0.0 | 7.77 | 8.64 | 18.82 | Au1rxx-base64 | 66.70.179.198 |
| 65.73 | vless | 393.8 | 912.5 | 18.66 | 0.0 | 7.93 | 8.64 | 18.82 | Au1rxx-base64 | 216.9.226.22 |
| 65.44 | shadowsocks | 456.4 | 1038.9 | 17.21 | 0.0 | 8.25 | 13.77 | 18.82 | Au1rxx-base64 | 15.204.233.41 |
| 64.11 | trojan | 580.4 | 699.5 | 14.34 | 0.0 | 8.47 | 13.88 | 18.82 | Au1rxx-base64 | 154.90.62.70 |
| 64.07 | shadowsocks | 592.9 | 1031.3 | 14.05 | 0.0 | 9.37 | 13.77 | 18.82 | Au1rxx-base64 | 82.38.31.159 |
| 63.73 | shadowsocks | 300.5 | 749.8 | 20.82 | 0.0 | 0.0 | 13.77 | 16.14 | Surfboard-tg-mixed | 156.146.38.167 |
| 63.72 | shadowsocks | 581.9 | 1001.9 | 14.31 | 0.0 | 9.23 | 13.77 | 18.82 | Au1rxx-base64 | 82.38.31.13 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi-get_subscribe | 0.976 | 0.967 | 60 | 598 | prefer |
| mheidari-all | 0.88 | 0.809 | 68 | 23983 | prefer |
| zhangkai | 0.861 | 1.0 | 17 | 144 | prefer |
| Au1rxx-base64 | 0.786 | 0.717 | 205 | 1786 | prefer |
| Surfboard-tg-mixed | 0.65 | 0.571 | 84 | 7056 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5125 | observe |
| DeltaKronecker-all | 0.255 | None | 0 | 4803 | observe |
| Epodonios-all | 0.255 | None | 0 | 7616 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 10026 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5579 | observe |
| barry-far-vless | 0.255 | None | 0 | 5831 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4216 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 50 |
| geo | ClientOSError | - | 12 |
| 204 | ProxyError | - | 9 |
| speed | ClientOSError | - | 9 |
| cn-block | ClientOSError | - | 7 |
| 204 | ProxyConnectionError | - | 6 |
| geo | TimeoutError | - | 6 |
| 204 | TimeoutError | - | 4 |
| cn-block | ProxyError | - | 3 |
| cn-block | TimeoutError | - | 2 |
| geo | ProxyError | - | 1 |
| 204 | ClientOSError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 57 | 73 | - |
| global | False | 75 | 80 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
