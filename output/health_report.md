# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-21 19:43:32 |
| 运行耗时 | 278.3s |
| 订阅源总数 | 107 |
| 健康订阅源 | 102 |
| 原始节点 | 82288 |
| 去重后节点 | 22983 |
| TCP 可达 | 3000 |
| 真实可用 | 533 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22983 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.1 |
| geo | 1.0 |
| tcp | 31.4 |
| probe | 58.4 |
| real_test | 140.9 |
| generate | 41.4 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 48923 |
| trojan | 11863 |
| vmess | 10831 |
| shadowsocks | 10079 |
| hysteria2 | 407 |
| shadowsocksr | 75 |
| http | 51 |
| socks | 41 |
| hysteria | 12 |
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
| 74.72 | shadowsocks | 213.2 | 503.5 | 22.84 | 0.0 | 10.0 | 12.28 | 13.6 | Au1rxx-base64 | 173.244.56.6 |
| 74.63 | trojan | 247.6 | 555.3 | 22.05 | 0.0 | 10.0 | 11.72 | 13.6 | Au1rxx-base64 | primary-mallard.rooster465.autos |
| 74.58 | shadowsocks | 219.6 | 523.2 | 22.7 | 0.0 | 10.0 | 12.28 | 13.6 | Au1rxx-base64 | 173.244.56.9 |
| 73.9 | trojan | 249.6 | 571.1 | 22.0 | 0.0 | 10.0 | 11.72 | 13.6 | Au1rxx-base64 | engaging-elephant.rooster465.autos |
| 72.29 | trojan | 246.2 | 537.2 | 22.08 | 0.0 | 10.0 | 11.72 | 13.6 | Au1rxx-base64 | 16.148.129.80 |
| 72.21 | shadowsocks | 321.5 | 808.1 | 20.33 | 0.0 | 10.0 | 12.28 | 13.6 | Au1rxx-base64 | 149.22.95.183 |
| 71.54 | trojan | 251.6 | 559.8 | 21.95 | 0.0 | 10.0 | 11.72 | 13.6 | Au1rxx-base64 | 52.41.11.42 |
| 71.09 | vless | 187.1 | 499.0 | 23.45 | 0.0 | 10.0 | 3.32 | 15.32 | Surfboard-tg-mixed | 86.109.75.147 |
| 71.0 | trojan | 243.1 | 548.3 | 22.15 | 0.0 | 10.0 | 11.72 | 13.6 | Au1rxx-base64 | 35.90.87.253 |
| 70.84 | shadowsocks | 315.8 | 245.6 | 20.47 | 5.79 | 9.87 | 12.28 | 13.6 | Au1rxx-base64 | 149.22.87.204 |
| 70.66 | trojan | 256.6 | 563.9 | 21.84 | 0.0 | 10.0 | 11.72 | 13.6 | Au1rxx-base64 | 184.33.95.59 |
| 70.35 | trojan | 226.8 | 493.7 | 22.53 | 0.0 | 10.0 | 11.72 | 13.6 | Au1rxx-base64 | 35.87.202.76 |
| 69.99 | trojan | 242.1 | 547.4 | 22.17 | 0.0 | 10.0 | 11.72 | 13.6 | Au1rxx-base64 | 44.251.226.7 |
| 69.88 | trojan | 246.8 | 562.1 | 22.06 | 0.0 | 10.0 | 11.72 | 13.6 | Au1rxx-base64 | 52.26.202.76 |
| 69.88 | shadowsocks | 273.9 | 281.2 | 21.44 | 4.45 | 9.88 | 12.28 | 13.6 | Au1rxx-base64 | 149.22.87.240 |
| 69.84 | trojan | 248.6 | 556.0 | 22.02 | 0.0 | 10.0 | 11.72 | 13.6 | Au1rxx-base64 | 52.43.195.42 |
| 69.82 | trojan | 239.8 | 535.5 | 22.23 | 0.0 | 10.0 | 11.72 | 13.6 | Au1rxx-base64 | 34.217.29.0 |
| 69.82 | trojan | 246.6 | 547.3 | 22.07 | 0.0 | 10.0 | 11.72 | 13.6 | Au1rxx-base64 | 44.252.127.212 |
| 69.79 | trojan | 243.8 | 552.8 | 22.13 | 0.0 | 10.0 | 11.72 | 13.6 | Au1rxx-base64 | tidy-gopher.rooster465.autos |
| 69.76 | trojan | 252.1 | 554.6 | 21.94 | 0.0 | 10.0 | 11.72 | 13.6 | Au1rxx-base64 | harmless-akita.rooster465.autos |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.95 | 0.972 | 36 | 61 | prefer |
| Au1rxx-base64 | 0.833 | 0.819 | 193 | 432 | prefer |
| mheidari-all | 0.684 | 0.604 | 364 | 19482 | observe |
| Surfboard-tg-mixed | 0.613 | 0.533 | 210 | 5357 | observe |
| xiaoji235-airport-v2ray-all | 0.391 | 1.0 | 2 | 4304 | observe |
| DeltaKronecker-all | 0.302 | 0.2 | 25 | 5415 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4482 | observe |
| Epodonios-all | 0.255 | None | 0 | 6463 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3996 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6710 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4158 | observe |
| barry-far-vless | 0.255 | None | 0 | 4788 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5204 | observe |
| nscl5-all | 0.255 | None | 0 | 2111 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 99 |
| geo | TimeoutError | - | 95 |
| cn-block | TimeoutError | - | 41 |
| 204 | TimeoutError | - | 19 |
| 204 | ProxyError | - | 15 |
| geo | ClientOSError | - | 10 |
| cn-block | ClientOSError | - | 8 |
| 204 | ClientOSError | - | 4 |
| cn-block | ProxyError | - | 4 |
| speed | TimeoutError | - | 3 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
