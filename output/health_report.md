# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-01 04:27:00 |
| 运行耗时 | 238.3s |
| 订阅源总数 | 107 |
| 健康订阅源 | 103 |
| 原始节点 | 75750 |
| 去重后节点 | 23199 |
| TCP 可达 | 3000 |
| 真实可用 | 531 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23199 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.5 |
| geo | 1.4 |
| tcp | 30.7 |
| probe | 54.6 |
| real_test | 115.8 |
| generate | 31.2 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 42689 |
| trojan | 12952 |
| vmess | 10181 |
| shadowsocks | 9322 |
| hysteria2 | 254 |
| shadowsocksr | 152 |
| http | 135 |
| socks | 58 |
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
| 77.49 | shadowsocks | 242.3 | 654.6 | 22.17 | 0.0 | 10.0 | 12.7 | 16.62 | Au1rxx-base64 | 37.19.198.160 |
| 77.47 | shadowsocks | 243.1 | 635.6 | 22.15 | 0.0 | 10.0 | 12.7 | 16.62 | Au1rxx-base64 | 37.19.198.244 |
| 77.41 | shadowsocks | 245.7 | 660.9 | 22.09 | 0.0 | 10.0 | 12.7 | 16.62 | Au1rxx-base64 | 37.19.198.236 |
| 74.84 | shadowsocks | 283.4 | 660.0 | 21.22 | 0.0 | 10.0 | 12.7 | 16.62 | Au1rxx-base64 | 156.146.38.168 |
| 74.52 | shadowsocks | 278.3 | 634.0 | 21.34 | 0.0 | 10.0 | 12.7 | 16.62 | Au1rxx-base64 | 156.146.38.170 |
| 74.51 | shadowsocks | 241.3 | 633.3 | 22.19 | 0.0 | 10.0 | 12.7 | 16.62 | Au1rxx-base64 | 37.19.198.243 |
| 74.09 | shadowsocks | 282.0 | 651.8 | 21.25 | 0.0 | 10.0 | 12.7 | 16.62 | Au1rxx-base64 | 156.146.38.169 |
| 74.02 | vless | 266.0 | 726.6 | 21.62 | 0.0 | 10.0 | 4.8 | 17.6 | mheidari-all | 47.253.226.114 |
| 73.34 | vless | 253.1 | 643.6 | 21.92 | 0.0 | 10.0 | 4.8 | 16.62 | Au1rxx-base64 | 159.89.87.21 |
| 73.28 | shadowsocks | 283.4 | 649.4 | 21.22 | 0.0 | 10.0 | 12.7 | 16.62 | Au1rxx-base64 | 156.146.38.167 |
| 70.97 | shadowsocks | 301.2 | 705.1 | 20.81 | 0.0 | 10.0 | 12.7 | 17.6 | mheidari-all | 198.98.53.130 |
| 70.83 | shadowsocks | 306.9 | 589.5 | 20.67 | 0.0 | 10.0 | 12.7 | 16.62 | Au1rxx-base64 | 173.244.56.9 |
| 70.81 | hysteria2 | 349.8 | 685.2 | 19.68 | 0.0 | 10.0 | 11.25 | 16.62 | Au1rxx-base64 | 62.210.124.146 |
| 69.79 | shadowsocks | 318.5 | 569.2 | 20.4 | 0.0 | 10.0 | 12.7 | 16.62 | Au1rxx-base64 | 108.181.118.10 |
| 69.76 | shadowsocks | 316.7 | 596.9 | 20.45 | 0.0 | 10.0 | 12.7 | 16.62 | Au1rxx-base64 | 108.181.0.177 |
| 69.39 | shadowsocks | 304.4 | 820.4 | 20.73 | 0.0 | 9.68 | 12.7 | 16.62 | Au1rxx-base64 | tinkered-pennies-puppies.freesocks.work |
| 69.22 | vless | 343.8 | 646.4 | 19.82 | 0.0 | 10.0 | 4.8 | 17.6 | mheidari-all | 104.19.87.194 |
| 69.15 | shadowsocks | 358.0 | 730.2 | 19.49 | 0.0 | 10.0 | 12.7 | 16.62 | Au1rxx-base64 | 173.244.56.6 |
| 69.06 | shadowsocks | 368.6 | 990.8 | 19.24 | 0.0 | 10.0 | 12.7 | 16.62 | Au1rxx-base64 | 172.234.202.34 |
| 68.67 | shadowsocks | 601.8 | 1689.4 | 13.85 | 0.0 | 10.0 | 12.7 | 16.62 | Au1rxx-base64 | 108.181.57.93 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| Au1rxx-base64 | 0.831 | 0.84 | 50 | 90 | prefer |
| Surfboard-tg-mixed | 0.795 | 0.716 | 335 | 5595 | prefer |
| mheidari-all | 0.572 | 0.492 | 297 | 16003 | observe |
| DeltaKronecker-all | 0.412 | 0.33 | 185 | 7352 | observe |
| nscl5-all | 0.356 | 1.0 | 2 | 1113 | observe |
| abc-configs-readme-latest30 | 0.312 | 1.0 | 2 | 18 | observe |
| ermaozi | 0.256 | 1.0 | 1 | 28 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4139 | observe |
| Epodonios-all | 0.255 | None | 0 | 6537 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6630 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4151 | observe |
| barry-far-vless | 0.255 | None | 0 | 4720 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5373 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 175 |
| geo | TimeoutError | - | 103 |
| geo | ClientOSError | - | 36 |
| speed | TimeoutError | - | 25 |
| 204 | ProxyError | - | 14 |
| cn-block | TimeoutError | - | 10 |
| cn-block | ClientOSError | - | 7 |
| 204 | ClientOSError | - | 7 |
| 204 | TimeoutError | - | 4 |
| cn-block | ProxyError | - | 2 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 191 | 300 | - |
| global | False | 197 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
