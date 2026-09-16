# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-16 11:25:31 |
| 运行耗时 | 693.9s |
| 订阅源总数 | 107 |
| 健康订阅源 | 96 |
| 原始节点 | 87785 |
| 去重后节点 | 24305 |
| TCP 可达 | 3000 |
| 真实可用 | 455 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 24305 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.6 |
| geo | 1.4 |
| tcp | 41.1 |
| probe | 276.4 |
| real_test | 232.8 |
| generate | 135.6 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 52933 |
| vmess | 13613 |
| shadowsocks | 10040 |
| trojan | 8791 |
| hysteria2 | 1549 |
| http | 653 |
| shadowsocksr | 129 |
| socks | 62 |
| hysteria | 8 |
| tuic | 5 |
| anytls | 2 |

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
| 79.77 | shadowsocks | 243.6 | 651.0 | 22.14 | 0.0 | 8.96 | 14.07 | 18.6 | Au1rxx-base64 | 37.19.198.244 |
| 77.93 | hysteria2 | 235.5 | 636.9 | 22.33 | 0.0 | 10.0 | 13.64 | 13.06 | mheidari-all | 159.223.157.129 |
| 77.76 | vless | 264.1 | 628.1 | 21.66 | 0.0 | 10.0 | 7.5 | 18.6 | Au1rxx-base64 | 169.40.42.133 |
| 77.68 | vless | 267.9 | 680.9 | 21.58 | 0.0 | 10.0 | 7.5 | 18.6 | Au1rxx-base64 | 167.17.69.171 |
| 77.3 | vless | 284.0 | 615.5 | 21.2 | 0.0 | 10.0 | 7.5 | 18.6 | Au1rxx-base64 | 169.40.42.74 |
| 77.05 | vless | 294.9 | 762.3 | 20.95 | 0.0 | 10.0 | 7.5 | 18.6 | Au1rxx-base64 | 169.40.42.163 |
| 76.97 | vless | 298.4 | 648.6 | 20.87 | 0.0 | 10.0 | 7.5 | 18.6 | Au1rxx-base64 | 169.40.42.75 |
| 76.69 | vless | 310.4 | 836.8 | 20.59 | 0.0 | 10.0 | 7.5 | 18.6 | Au1rxx-base64 | 137.184.218.169 |
| 76.43 | shadowsocks | 274.4 | 631.1 | 21.43 | 0.0 | 8.59 | 14.07 | 18.6 | Au1rxx-base64 | 156.146.38.170 |
| 76.43 | vless | 321.9 | 851.4 | 20.33 | 0.0 | 10.0 | 7.5 | 18.6 | Au1rxx-base64 | 169.40.42.223 |
| 76.24 | vless | 329.9 | 833.8 | 20.14 | 0.0 | 10.0 | 7.5 | 18.6 | Au1rxx-base64 | 66.70.179.198 |
| 76.04 | shadowsocks | 284.8 | 653.0 | 21.19 | 0.0 | 8.67 | 14.07 | 18.6 | Au1rxx-base64 | 156.146.38.169 |
| 75.8 | vless | 348.8 | 938.5 | 19.7 | 0.0 | 10.0 | 7.5 | 18.6 | Au1rxx-base64 | 169.40.42.224 |
| 75.75 | vless | 351.1 | 877.0 | 19.65 | 0.0 | 10.0 | 7.5 | 18.6 | Au1rxx-base64 | 169.40.42.16 |
| 75.74 | vless | 351.6 | 816.3 | 19.64 | 0.0 | 10.0 | 7.5 | 18.6 | Au1rxx-base64 | 169.40.42.35 |
| 75.7 | vless | 343.6 | 910.1 | 19.83 | 0.0 | 10.0 | 7.5 | 18.6 | Au1rxx-base64 | 169.40.42.104 |
| 75.64 | vless | 350.3 | 812.3 | 19.67 | 0.0 | 10.0 | 7.5 | 18.6 | Au1rxx-base64 | 169.40.42.184 |
| 75.64 | vless | 356.1 | 841.2 | 19.54 | 0.0 | 10.0 | 7.5 | 18.6 | Au1rxx-base64 | 169.40.42.235 |
| 75.61 | vless | 357.2 | 836.7 | 19.51 | 0.0 | 10.0 | 7.5 | 18.6 | Au1rxx-base64 | 169.40.42.15 |
| 75.55 | vless | 359.6 | 902.4 | 19.45 | 0.0 | 10.0 | 7.5 | 18.6 | Au1rxx-base64 | 169.40.42.225 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.916 | 0.85 | 301 | 1687 | prefer |
| mheidari-all | 0.811 | 0.738 | 65 | 16003 | prefer |
| DeltaKronecker-all | 0.777 | 0.71 | 31 | 6081 | prefer |
| ermaozi | 0.775 | 0.768 | 56 | 407 | prefer |
| Surfboard-tg-mixed | 0.735 | 0.658 | 114 | 7446 | prefer |
| ermaozi-get_subscribe | 0.427 | 0.4 | 20 | 438 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| tg-oneclickvpnkeys | 0.262 | 1.0 | 1 | 178 | observe |
| roosterkid-openproxylist-v2ray | 0.261 | 1.0 | 1 | 150 | observe |
| Epodonios-all | 0.255 | None | 0 | 8003 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9052 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 6044 | observe |
| barry-far-vless | 0.255 | None | 0 | 6340 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4206 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | ClientOSError | - | 28 |
| 204 | ProxyError | - | 26 |
| cn-block | TimeoutError | - | 18 |
| 204 | TimeoutError | - | 15 |
| speed | ClientOSError | - | 12 |
| cn-block | ClientOSError | - | 11 |
| speed | TimeoutError | - | 11 |
| geo | TimeoutError | - | 10 |
| 204 | ClientOSError | - | 3 |
| cn-block | ProxyError | - | 2 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
