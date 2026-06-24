# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-06-24 04:08:20 |
| 运行耗时 | 217.2s |
| 订阅源总数 | 107 |
| 健康订阅源 | 105 |
| 原始节点 | 77147 |
| 去重后节点 | 22469 |
| TCP 可达 | 3000 |
| 真实可用 | 553 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22469 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.1 |
| geo | 1.4 |
| tcp | 29.0 |
| probe | 49.7 |
| real_test | 110.0 |
| generate | 22.0 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 45861 |
| trojan | 10563 |
| vmess | 10211 |
| shadowsocks | 9866 |
| hysteria2 | 235 |
| http | 161 |
| shadowsocksr | 157 |
| socks | 85 |
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
| 77.54 | shadowsocks | 199.1 | 484.1 | 23.17 | 0.0 | 10.0 | 12.93 | 15.94 | Au1rxx-base64 | 108.181.118.10 |
| 77.38 | shadowsocks | 206.1 | 504.1 | 23.01 | 0.0 | 10.0 | 12.93 | 15.94 | Au1rxx-base64 | 108.181.0.177 |
| 76.72 | shadowsocks | 256.1 | 704.3 | 21.85 | 0.0 | 10.0 | 12.93 | 15.94 | Au1rxx-base64 | 216.105.168.18 |
| 75.08 | shadowsocks | 225.1 | 532.9 | 22.57 | 0.0 | 10.0 | 12.93 | 15.94 | Au1rxx-base64 | 149.22.95.183 |
| 73.66 | shadowsocks | 258.9 | 633.9 | 21.79 | 0.0 | 10.0 | 12.93 | 15.94 | Au1rxx-base64 | 173.244.56.6 |
| 73.5 | trojan | 242.1 | 624.7 | 22.17 | 0.0 | 10.0 | 8.09 | 15.94 | Au1rxx-base64 | 45.61.58.89 |
| 73.49 | vless | 315.3 | 830.4 | 20.48 | 0.0 | 10.0 | 7.07 | 15.94 | Au1rxx-base64 | 15.204.97.219 |
| 73.44 | trojan | 253.6 | 626.6 | 21.91 | 0.0 | 10.0 | 8.09 | 15.94 | Au1rxx-base64 | 45.61.52.243 |
| 73.32 | vless | 322.7 | 847.7 | 20.31 | 0.0 | 10.0 | 7.07 | 15.94 | Au1rxx-base64 | 15.204.97.214 |
| 72.74 | shadowsocks | 289.7 | 645.0 | 21.07 | 0.0 | 10.0 | 12.93 | 15.94 | Au1rxx-base64 | 156.146.38.167 |
| 72.59 | shadowsocks | 295.4 | 648.3 | 20.94 | 0.0 | 10.0 | 12.93 | 15.94 | Au1rxx-base64 | 156.146.38.168 |
| 72.49 | shadowsocks | 301.3 | 680.0 | 20.8 | 0.0 | 10.0 | 12.93 | 15.94 | Au1rxx-base64 | 156.146.38.170 |
| 72.45 | shadowsocks | 291.8 | 653.9 | 21.02 | 0.0 | 10.0 | 12.93 | 15.94 | Au1rxx-base64 | 156.146.38.169 |
| 71.38 | vless | 212.0 | 481.0 | 22.87 | 0.0 | 10.0 | 7.07 | 14.44 | Surfboard-tg-mixed | 173.245.59.35 |
| 70.69 | shadowsocks | 295.0 | 342.1 | 20.95 | 2.17 | 9.92 | 12.93 | 15.94 | Au1rxx-base64 | 149.22.87.241 |
| 70.11 | shadowsocks | 300.8 | 354.8 | 20.81 | 1.7 | 9.93 | 12.93 | 15.94 | Au1rxx-base64 | 149.22.87.204 |
| 69.46 | shadowsocks | 234.0 | 549.2 | 22.36 | 0.0 | 10.0 | 12.93 | 15.94 | Au1rxx-base64 | 173.244.56.9 |
| 68.63 | shadowsocks | 304.4 | 361.7 | 20.73 | 1.44 | 9.92 | 12.93 | 15.94 | Au1rxx-base64 | 149.22.87.240 |
| 68.45 | shadowsocks | 179.7 | 484.0 | 23.62 | 0.0 | 10.0 | 12.93 | 11.0 | DeltaKronecker-all | 107.172.219.230 |
| 68.35 | shadowsocks | 363.3 | 727.3 | 19.37 | 0.0 | 10.0 | 12.93 | 15.94 | Au1rxx-base64 | 37.19.198.160 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.984 | 1.0 | 50 | 73 | prefer |
| mheidari-all | 0.904 | 0.844 | 32 | 15816 | prefer |
| Surfboard-tg-mixed | 0.89 | 0.812 | 309 | 5496 | prefer |
| Au1rxx-base64 | 0.796 | 0.797 | 79 | 135 | prefer |
| DeltaKronecker-all | 0.658 | 0.579 | 273 | 6437 | observe |
| Barabama-yudou | 0.318 | 1.0 | 2 | 166 | observe |
| nscl5-all | 0.301 | 1.0 | 1 | 1140 | observe |
| 10ium-HighSpeed | 0.289 | 1.0 | 1 | 839 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4576 | observe |
| Epodonios-all | 0.255 | None | 0 | 8143 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3976 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7676 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4190 | observe |
| barry-far-vless | 0.255 | None | 0 | 4932 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4664 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 104 |
| geo | TimeoutError | - | 46 |
| 204 | TimeoutError | - | 13 |
| cn-block | TimeoutError | - | 8 |
| cn-block | ClientOSError | - | 5 |
| geo | ClientOSError | - | 5 |
| speed | TimeoutError | - | 5 |
| 204 | ClientOSError | - | 3 |
| geo | ProxyError | - | 3 |
| speed | ProxyError | - | 1 |
| 204 | ProxyError | - | 1 |
| cn-block | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
