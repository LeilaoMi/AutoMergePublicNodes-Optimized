# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.9.1 |
| 更新时间 | 2026-06-19 20:03:30 |
| 运行耗时 | 472.0s |
| 订阅源总数 | 107 |
| 健康订阅源 | 105 |
| 原始节点 | 72488 |
| 去重后节点 | 21995 |
| TCP 可达 | 743 |
| 真实可用 | 564 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 21995 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 2.9 |
| geo | 1.3 |
| tcp | 67.0 |
| probe | 109.0 |
| real_test | 239.8 |
| generate | 52.0 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 41214 |
| shadowsocks | 10680 |
| trojan | 10135 |
| vmess | 9840 |
| hysteria2 | 234 |
| shadowsocksr | 161 |
| http | 107 |
| socks | 90 |
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
| 76.33 | shadowsocks | 240.1 | 624.4 | 22.22 | 0.0 | 10.0 | 13.57 | 16.74 | Au1rxx-base64 | 173.244.56.6 |
| 75.85 | shadowsocks | 260.9 | 638.5 | 21.74 | 0.0 | 10.0 | 13.57 | 16.74 | Au1rxx-base64 | 156.146.38.167 |
| 75.71 | vless | 295.1 | 699.4 | 20.95 | 0.0 | 10.0 | 12.65 | 18.36 | Surfboard-tg-mixed | 23.27.134.55 |
| 75.43 | shadowsocks | 259.8 | 636.2 | 21.76 | 0.0 | 10.0 | 13.57 | 16.74 | Au1rxx-base64 | 156.146.38.170 |
| 74.96 | vless | 361.6 | 875.2 | 19.41 | 0.0 | 10.0 | 12.65 | 16.74 | Au1rxx-base64 | 15.204.97.214 |
| 73.46 | shadowsocks | 256.5 | 625.6 | 21.84 | 0.0 | 10.0 | 13.57 | 16.74 | Au1rxx-base64 | 156.146.38.168 |
| 72.68 | shadowsocks | 315.5 | 799.6 | 20.47 | 0.0 | 10.0 | 13.57 | 16.74 | Au1rxx-base64 | 156.146.38.169 |
| 72.51 | vless | 360.3 | 867.9 | 19.44 | 0.0 | 10.0 | 12.65 | 16.74 | Au1rxx-base64 | 15.204.97.219 |
| 72.17 | shadowsocks | 376.7 | 1052.3 | 19.06 | 0.0 | 10.0 | 13.57 | 16.74 | Au1rxx-base64 | 167.160.90.51 |
| 71.72 | vless | 370.1 | 389.3 | 19.21 | 0.4 | 9.92 | 12.65 | 18.36 | Surfboard-tg-mixed | 31.76.91.18 |
| 71.27 | shadowsocks | 277.4 | 601.0 | 21.36 | 0.0 | 10.0 | 13.57 | 16.74 | Au1rxx-base64 | 149.22.95.183 |
| 70.95 | vless | 358.9 | 406.3 | 19.47 | 0.0 | 9.9 | 12.65 | 18.36 | Surfboard-tg-mixed | 31.76.91.24 |
| 70.34 | vless | 384.9 | 497.7 | 18.87 | 0.0 | 9.91 | 12.65 | 18.38 | mheidari-all | 31.76.91.26 |
| 69.08 | vless | 441.0 | 373.9 | 17.57 | 0.98 | 9.41 | 12.65 | 18.38 | mheidari-all | 64.49.44.87 |
| 68.73 | shadowsocks | 308.6 | 370.1 | 20.63 | 1.12 | 9.89 | 13.57 | 16.74 | Au1rxx-base64 | 149.22.87.240 |
| 68.68 | shadowsocks | 307.3 | 363.2 | 20.66 | 1.38 | 9.5 | 13.57 | 16.74 | Au1rxx-base64 | 149.22.87.241 |
| 68.61 | shadowsocks | 307.6 | 367.8 | 20.66 | 1.21 | 9.59 | 13.57 | 16.74 | Au1rxx-base64 | 149.22.87.204 |
| 68.42 | shadowsocks | 352.6 | 757.6 | 19.61 | 0.0 | 10.0 | 13.57 | 16.74 | Au1rxx-base64 | 37.19.198.160 |
| 68.41 | shadowsocks | 354.8 | 735.4 | 19.57 | 0.0 | 10.0 | 13.57 | 16.74 | Au1rxx-base64 | 37.19.198.244 |
| 68.17 | shadowsocks | 357.7 | 748.2 | 19.5 | 0.0 | 10.0 | 13.57 | 16.74 | Au1rxx-base64 | 37.19.198.236 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.966 | 1.0 | 25 | 73 | prefer |
| Surfboard-tg-mixed | 0.899 | 0.821 | 357 | 4884 | prefer |
| mheidari-all | 0.817 | 0.739 | 268 | 14715 | prefer |
| Au1rxx-base64 | 0.717 | 0.731 | 26 | 75 | prefer |
| DeltaKronecker-all | 0.498 | 0.415 | 65 | 6989 | observe |
| nscl5-all | 0.309 | 1.0 | 1 | 1360 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4458 | observe |
| Epodonios-all | 0.255 | None | 0 | 7362 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3976 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6518 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 3572 | observe |
| barry-far-vless | 0.255 | None | 0 | 4234 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4527 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 52 |
| cn-block | TimeoutError | - | 33 |
| 204 | TimeoutError | - | 32 |
| geo | ClientOSError | - | 14 |
| speed | TimeoutError | - | 12 |
| 204 | ProxyError | - | 10 |
| geo | TimeoutError | - | 9 |
| 204 | ClientOSError | - | 6 |
| cn-block | ProxyError | - | 6 |
| cn-block | ClientOSError | - | 5 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
