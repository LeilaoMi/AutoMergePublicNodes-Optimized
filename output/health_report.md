# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.9.1 |
| 更新时间 | 2026-06-21 10:05:31 |
| 运行耗时 | 429.2s |
| 订阅源总数 | 107 |
| 健康订阅源 | 104 |
| 原始节点 | 73085 |
| 去重后节点 | 21857 |
| TCP 可达 | 796 |
| 真实可用 | 601 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 21857 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.8 |
| geo | 1.3 |
| tcp | 62.9 |
| probe | 110.6 |
| real_test | 185.2 |
| generate | 64.4 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 42402 |
| shadowsocks | 10161 |
| trojan | 9953 |
| vmess | 9895 |
| hysteria2 | 236 |
| http | 182 |
| shadowsocksr | 157 |
| socks | 91 |
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
| 75.21 | shadowsocks | 235.3 | 635.9 | 22.33 | 0.0 | 10.0 | 14.64 | 14.34 | Au1rxx-base64 | 37.19.198.244 |
| 75.11 | shadowsocks | 239.5 | 642.4 | 22.23 | 0.0 | 10.0 | 14.64 | 14.34 | Au1rxx-base64 | 37.19.198.160 |
| 74.95 | shadowsocks | 246.4 | 668.0 | 22.07 | 0.0 | 10.0 | 14.64 | 14.34 | Au1rxx-base64 | 37.19.198.236 |
| 72.79 | shadowsocks | 340.0 | 934.2 | 19.91 | 0.0 | 10.0 | 14.64 | 14.34 | Au1rxx-base64 | 161.129.71.148 |
| 72.45 | shadowsocks | 282.9 | 648.8 | 21.23 | 0.0 | 10.0 | 14.64 | 14.34 | Au1rxx-base64 | 156.146.38.170 |
| 72.41 | shadowsocks | 334.8 | 928.8 | 20.03 | 0.0 | 10.0 | 14.64 | 14.34 | Au1rxx-base64 | 69.164.240.83 |
| 72.24 | trojan | 290.1 | 624.1 | 21.06 | 0.0 | 10.0 | 12.79 | 16.64 | mheidari-all | 64.94.95.118 |
| 72.04 | shadowsocks | 286.4 | 664.6 | 21.15 | 0.0 | 10.0 | 14.64 | 14.34 | Au1rxx-base64 | 156.146.38.169 |
| 71.74 | shadowsocks | 342.2 | 949.7 | 19.86 | 0.0 | 10.0 | 14.64 | 14.34 | Au1rxx-base64 | 69.164.240.86 |
| 71.66 | shadowsocks | 281.9 | 652.8 | 21.25 | 0.0 | 10.0 | 14.64 | 14.34 | Au1rxx-base64 | 156.146.38.167 |
| 71.61 | shadowsocks | 285.9 | 660.6 | 21.16 | 0.0 | 10.0 | 14.64 | 14.34 | Au1rxx-base64 | 156.146.38.168 |
| 71.05 | vless | 356.4 | 884.8 | 19.53 | 0.0 | 10.0 | 10.37 | 16.64 | mheidari-all | 185.156.47.96 |
| 70.99 | shadowsocks | 417.6 | 1172.3 | 18.11 | 0.0 | 10.0 | 14.64 | 14.34 | Au1rxx-base64 | 205.209.109.194 |
| 70.77 | shadowsocks | 405.6 | 1137.7 | 18.39 | 0.0 | 10.0 | 14.64 | 14.34 | Au1rxx-base64 | 68.168.209.194 |
| 70.31 | vless | 328.4 | 851.1 | 20.18 | 0.0 | 10.0 | 10.37 | 19.26 | Surfboard-tg-mixed | 185.173.144.212 |
| 69.53 | shadowsocks | 260.2 | 671.0 | 21.75 | 0.0 | 10.0 | 14.64 | 9.64 | DeltaKronecker-all | 108.181.57.93 |
| 69.38 | shadowsocks | 245.1 | 654.0 | 22.1 | 0.0 | 10.0 | 14.64 | 9.64 | DeltaKronecker-all | 142.93.183.235 |
| 69.07 | shadowsocks | 411.9 | 759.7 | 18.24 | 0.0 | 10.0 | 14.64 | 19.26 | Surfboard-tg-mixed | 51.254.142.162 |
| 68.71 | shadowsocks | 420.3 | 771.7 | 18.05 | 0.0 | 10.0 | 14.64 | 19.26 | Surfboard-tg-mixed | 195.93.253.240 |
| 68.63 | shadowsocks | 424.8 | 775.4 | 17.94 | 0.0 | 10.0 | 14.64 | 19.26 | Surfboard-tg-mixed | 141.227.152.129 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.991 | 1.0 | 69 | 131 | prefer |
| Au1rxx-base64 | 0.897 | 0.914 | 35 | 138 | prefer |
| mheidari-all | 0.858 | 0.78 | 291 | 14998 | prefer |
| Surfboard-tg-mixed | 0.84 | 0.762 | 332 | 4684 | prefer |
| DeltaKronecker-all | 0.334 | 0.246 | 65 | 6748 | observe |
| Barabama-yudou | 0.318 | 1.0 | 2 | 166 | observe |
| nscl5-all | 0.303 | 1.0 | 1 | 1204 | observe |
| abc-configs-readme-latest30 | 0.256 | 1.0 | 1 | 26 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4494 | observe |
| Epodonios-all | 0.255 | None | 0 | 7269 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7017 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 3546 | observe |
| barry-far-vless | 0.255 | None | 0 | 4394 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4510 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 64 |
| 204 | TimeoutError | - | 28 |
| 204 | ProxyError | - | 27 |
| geo | TimeoutError | - | 21 |
| cn-block | TimeoutError | - | 20 |
| cn-block | ClientOSError | - | 9 |
| speed | TimeoutError | - | 9 |
| geo | ClientOSError | - | 7 |
| speed | ProxyError | - | 5 |
| geo | ProxyError | - | 2 |
| cn-block | ProxyError | - | 2 |
| 204 | ClientOSError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
