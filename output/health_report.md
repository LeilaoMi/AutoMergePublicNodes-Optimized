# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-06-27 04:02:10 |
| 运行耗时 | 235.7s |
| 订阅源总数 | 107 |
| 健康订阅源 | 105 |
| 原始节点 | 75900 |
| 去重后节点 | 22867 |
| TCP 可达 | 3000 |
| 真实可用 | 515 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22867 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.8 |
| geo | 1.4 |
| tcp | 30.8 |
| probe | 52.0 |
| real_test | 108.5 |
| generate | 38.2 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 42681 |
| trojan | 11927 |
| vmess | 11184 |
| shadowsocks | 9515 |
| hysteria2 | 253 |
| shadowsocksr | 162 |
| socks | 87 |
| http | 80 |
| hysteria | 8 |
| tuic | 2 |
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
| 76.48 | vless | 260.8 | 731.9 | 21.74 | 0.0 | 10.0 | 9.92 | 14.82 | mheidari-all | 47.253.226.114 |
| 75.84 | shadowsocks | 227.0 | 628.0 | 22.52 | 0.0 | 10.0 | 10.84 | 16.48 | Au1rxx-base64 | 37.19.198.160 |
| 75.73 | shadowsocks | 231.8 | 638.9 | 22.41 | 0.0 | 10.0 | 10.84 | 16.48 | Au1rxx-base64 | 37.19.198.243 |
| 75.5 | shadowsocks | 241.7 | 673.0 | 22.18 | 0.0 | 10.0 | 10.84 | 16.48 | Au1rxx-base64 | 37.19.198.236 |
| 74.31 | shadowsocks | 221.7 | 604.3 | 22.65 | 0.0 | 10.0 | 10.84 | 14.82 | mheidari-all | 198.98.53.130 |
| 72.29 | shadowsocks | 285.2 | 664.5 | 21.17 | 0.0 | 10.0 | 10.84 | 16.48 | Au1rxx-base64 | 156.146.38.170 |
| 72.05 | shadowsocks | 285.1 | 654.1 | 21.18 | 0.0 | 10.0 | 10.84 | 16.48 | Au1rxx-base64 | 156.146.38.167 |
| 71.92 | shadowsocks | 303.0 | 826.0 | 20.76 | 0.0 | 10.0 | 10.84 | 14.82 | mheidari-all | 108.181.57.93 |
| 71.63 | shadowsocks | 387.2 | 1060.8 | 18.81 | 0.0 | 10.0 | 10.84 | 16.48 | Au1rxx-base64 | 172.234.202.34 |
| 71.45 | shadowsocks | 275.5 | 627.6 | 21.4 | 0.0 | 10.0 | 10.84 | 16.48 | Au1rxx-base64 | 156.146.38.169 |
| 71.15 | shadowsocks | 330.9 | 775.2 | 20.12 | 0.0 | 10.0 | 10.84 | 16.48 | Au1rxx-base64 | 156.146.38.168 |
| 71.14 | vless | 266.1 | 659.4 | 21.62 | 0.0 | 10.0 | 9.92 | 11.6 | DeltaKronecker-all | 104.25.161.29 |
| 70.81 | shadowsocks | 228.4 | 630.8 | 22.49 | 0.0 | 10.0 | 10.84 | 16.48 | Au1rxx-base64 | 37.19.198.244 |
| 69.69 | vless | 330.2 | 837.6 | 20.13 | 0.0 | 10.0 | 9.92 | 14.64 | Surfboard-tg-mixed | 137.184.218.169 |
| 69.62 | vless | 347.6 | 636.2 | 19.73 | 0.0 | 10.0 | 9.92 | 14.82 | mheidari-all | 173.245.59.35 |
| 69.19 | vless | 297.1 | 726.3 | 20.9 | 0.0 | 10.0 | 9.92 | 14.64 | Surfboard-tg-mixed | 15.223.121.250 |
| 68.91 | vless | 443.4 | 991.7 | 17.51 | 0.0 | 10.0 | 9.92 | 16.48 | Au1rxx-base64 | 159.89.87.21 |
| 68.56 | shadowsocks | 255.3 | 692.4 | 21.87 | 0.0 | 10.0 | 10.84 | 16.48 | Au1rxx-base64 | tinkered-pennies-puppies.freesocks.work |
| 68.49 | shadowsocks | 332.0 | 684.5 | 20.09 | 0.0 | 10.0 | 10.84 | 16.48 | Au1rxx-base64 | 173.244.56.6 |
| 68.42 | shadowsocks | 300.4 | 588.4 | 20.83 | 0.0 | 10.0 | 10.84 | 16.48 | Au1rxx-base64 | 173.244.56.9 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Surfboard-tg-mixed | 0.92 | 0.842 | 330 | 5149 | prefer |
| snakem982 | 0.89 | 1.0 | 18 | 39 | prefer |
| mheidari-all | 0.742 | 0.663 | 193 | 16221 | prefer |
| Au1rxx-base64 | 0.663 | 0.667 | 42 | 101 | observe |
| nscl5-all | 0.359 | 1.0 | 2 | 1186 | observe |
| DeltaKronecker-all | 0.343 | 0.261 | 234 | 6283 | observe |
| Epodonios-all | 0.255 | None | 0 | 7720 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3980 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7047 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 3785 | observe |
| barry-far-vless | 0.255 | None | 0 | 4565 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5248 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |
| 10ium-HighSpeed | 0.209 | None | 0 | 839 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 131 |
| geo | TimeoutError | - | 103 |
| geo | ClientOSError | - | 31 |
| cn-block | TimeoutError | - | 12 |
| cn-block | ClientOSError | - | 8 |
| 204 | ClientOSError | - | 7 |
| speed | TimeoutError | - | 6 |
| 204 | TimeoutError | - | 5 |
| 204 | ProxyError | - | 5 |
| cn-block | ProxyError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 293 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
