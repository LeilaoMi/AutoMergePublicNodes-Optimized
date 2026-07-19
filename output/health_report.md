# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-19 08:32:14 |
| 运行耗时 | 331.2s |
| 订阅源总数 | 107 |
| 健康订阅源 | 100 |
| 原始节点 | 84921 |
| 去重后节点 | 23703 |
| TCP 可达 | 3000 |
| 真实可用 | 793 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23703 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.5 |
| geo | 1.3 |
| tcp | 32.9 |
| probe | 70.4 |
| real_test | 195.7 |
| generate | 25.3 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 49173 |
| trojan | 14158 |
| vmess | 10976 |
| shadowsocks | 10057 |
| hysteria2 | 304 |
| shadowsocksr | 125 |
| http | 56 |
| socks | 51 |
| hysteria | 15 |
| tuic | 5 |
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
| 76.26 | shadowsocks | 249.6 | 608.8 | 22.0 | 0.0 | 10.0 | 14.04 | 14.22 | Au1rxx-base64 | 156.146.38.169 |
| 76.12 | shadowsocks | 255.8 | 628.3 | 21.86 | 0.0 | 10.0 | 14.04 | 14.22 | Au1rxx-base64 | 156.146.38.168 |
| 76.05 | shadowsocks | 258.6 | 630.5 | 21.79 | 0.0 | 10.0 | 14.04 | 14.22 | Au1rxx-base64 | 156.146.38.170 |
| 75.89 | shadowsocks | 251.9 | 620.3 | 21.95 | 0.0 | 10.0 | 14.04 | 14.22 | Au1rxx-base64 | 156.146.38.167 |
| 75.88 | shadowsocks | 265.9 | 673.4 | 21.62 | 0.0 | 10.0 | 14.04 | 14.22 | Au1rxx-base64 | 37.19.198.244 |
| 75.85 | shadowsocks | 267.2 | 665.8 | 21.59 | 0.0 | 10.0 | 14.04 | 14.22 | Au1rxx-base64 | 37.19.198.243 |
| 75.84 | shadowsocks | 267.8 | 672.4 | 21.58 | 0.0 | 10.0 | 14.04 | 14.22 | Au1rxx-base64 | 37.19.198.160 |
| 75.44 | shadowsocks | 270.3 | 677.6 | 21.52 | 0.0 | 10.0 | 14.04 | 13.88 | mheidari-all | 198.98.53.130 |
| 74.34 | shadowsocks | 310.9 | 849.9 | 20.58 | 0.0 | 10.0 | 14.04 | 14.22 | Au1rxx-base64 | 50.114.177.235 |
| 73.59 | shadowsocks | 328.6 | 850.4 | 20.17 | 0.0 | 10.0 | 14.04 | 13.88 | mheidari-all | 185.196.61.82 |
| 72.62 | shadowsocks | 359.3 | 912.3 | 19.46 | 0.0 | 10.0 | 14.04 | 13.64 | Surfboard-tg-mixed | 108.181.57.93 |
| 71.84 | shadowsocks | 259.8 | 548.0 | 21.76 | 0.0 | 10.0 | 14.04 | 14.22 | Au1rxx-base64 | 108.181.0.177 |
| 71.23 | shadowsocks | 283.2 | 573.6 | 21.22 | 0.0 | 10.0 | 14.04 | 14.22 | Au1rxx-base64 | 173.244.56.6 |
| 71.02 | shadowsocks | 291.9 | 571.8 | 21.02 | 0.0 | 10.0 | 14.04 | 14.22 | Au1rxx-base64 | 149.22.95.183 |
| 70.88 | trojan | 360.8 | 816.8 | 19.43 | 0.0 | 10.0 | 14.1 | 10.88 | DeltaKronecker-all | 64.94.95.115 |
| 70.79 | trojan | 358.4 | 896.4 | 19.48 | 0.0 | 10.0 | 14.1 | 10.88 | DeltaKronecker-all | 64.94.95.114 |
| 70.02 | trojan | 372.3 | 936.6 | 19.16 | 0.0 | 10.0 | 14.1 | 10.88 | DeltaKronecker-all | 64.94.95.117 |
| 69.91 | vmess | 381.0 | 1025.2 | 18.96 | 0.0 | 9.81 | 12.0 | 13.64 | Surfboard-tg-mixed | 67.220.95.3 |
| 69.7 | shadowsocks | 293.7 | 563.0 | 20.98 | 0.0 | 10.0 | 14.04 | 14.22 | Au1rxx-base64 | 108.181.118.10 |
| 69.33 | shadowsocks | 283.6 | 565.1 | 21.21 | 0.0 | 10.0 | 14.04 | 14.22 | Au1rxx-base64 | 173.244.56.9 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.976 | 1.0 | 36 | 61 | prefer |
| Surfboard-tg-mixed | 0.929 | 0.853 | 177 | 5438 | prefer |
| Au1rxx-base64 | 0.854 | 0.854 | 123 | 149 | prefer |
| DeltaKronecker-all | 0.62 | 0.54 | 274 | 6235 | observe |
| mheidari-all | 0.556 | 0.476 | 731 | 20430 | observe |
| xiaoji235-airport-v2ray-all | 0.438 | 1.0 | 3 | 4642 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| roosterkid-openproxylist-v2ray | 0.261 | 1.0 | 1 | 150 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4478 | observe |
| Epodonios-all | 0.255 | None | 0 | 6647 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3971 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6843 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4126 | observe |
| barry-far-vless | 0.255 | None | 0 | 4872 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5355 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 249 |
| geo | TimeoutError | - | 171 |
| geo | ClientOSError | - | 54 |
| cn-block | TimeoutError | - | 35 |
| speed | TimeoutError | - | 18 |
| 204 | TimeoutError | - | 12 |
| cn-block | ClientOSError | - | 6 |
| 204 | ClientOSError | - | 4 |
| cn-block | ProxyError | - | 3 |
| speed | ProxyError | - | 1 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
