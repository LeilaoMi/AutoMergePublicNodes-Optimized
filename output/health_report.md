# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-13 11:38:22 |
| 运行耗时 | 584.6s |
| 订阅源总数 | 107 |
| 健康订阅源 | 95 |
| 原始节点 | 94200 |
| 去重后节点 | 25224 |
| TCP 可达 | 3000 |
| 真实可用 | 342 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 25224 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.9 |
| geo | 1.4 |
| tcp | 41.1 |
| probe | 252.5 |
| real_test | 202.4 |
| generate | 80.2 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 57890 |
| vmess | 13474 |
| shadowsocks | 10871 |
| trojan | 8890 |
| hysteria2 | 2205 |
| http | 640 |
| shadowsocksr | 129 |
| socks | 60 |
| hysteria | 15 |
| anytls | 14 |
| tuic | 12 |

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
| 78.92 | shadowsocks | 297.1 | 791.3 | 20.9 | 0.0 | 10.0 | 14.3 | 18.22 | Au1rxx-base64 | 15.204.247.175 |
| 77.49 | shadowsocks | 359.0 | 1037.8 | 19.47 | 0.0 | 10.0 | 14.3 | 18.22 | Au1rxx-base64 | 15.204.246.132 |
| 76.53 | vless | 232.1 | 653.5 | 22.4 | 0.0 | 10.0 | 5.91 | 18.22 | Au1rxx-base64 | 47.253.226.114 |
| 76.47 | vless | 234.8 | 618.4 | 22.34 | 0.0 | 10.0 | 5.91 | 18.22 | Au1rxx-base64 | 195.123.235.177 |
| 76.47 | hysteria2 | 326.1 | 690.9 | 20.23 | 0.0 | 10.0 | 13.04 | 18.22 | Au1rxx-base64 | 66.94.121.46 |
| 75.52 | vless | 275.9 | 729.8 | 21.39 | 0.0 | 10.0 | 5.91 | 18.22 | Au1rxx-base64 | 169.40.42.212 |
| 75.14 | vless | 292.5 | 779.8 | 21.01 | 0.0 | 10.0 | 5.91 | 18.22 | Au1rxx-base64 | 169.40.42.235 |
| 75.13 | vless | 292.8 | 721.8 | 21.0 | 0.0 | 10.0 | 5.91 | 18.22 | Au1rxx-base64 | 169.40.42.202 |
| 74.93 | vless | 301.3 | 831.3 | 20.8 | 0.0 | 10.0 | 5.91 | 18.22 | Au1rxx-base64 | 137.184.218.169 |
| 74.87 | vless | 304.0 | 686.9 | 20.74 | 0.0 | 10.0 | 5.91 | 18.22 | Au1rxx-base64 | 169.40.42.16 |
| 74.47 | vless | 321.2 | 813.6 | 20.34 | 0.0 | 10.0 | 5.91 | 18.22 | Au1rxx-base64 | 169.40.42.224 |
| 74.45 | vless | 255.1 | 664.6 | 21.87 | 0.0 | 10.0 | 5.91 | 18.22 | Au1rxx-base64 | 169.40.42.231 |
| 74.3 | vless | 328.8 | 835.7 | 20.17 | 0.0 | 10.0 | 5.91 | 18.22 | Au1rxx-base64 | 169.40.42.75 |
| 74.25 | vless | 331.0 | 831.6 | 20.12 | 0.0 | 10.0 | 5.91 | 18.22 | Au1rxx-base64 | 169.40.42.95 |
| 74.17 | vless | 334.2 | 821.1 | 20.04 | 0.0 | 10.0 | 5.91 | 18.22 | Au1rxx-base64 | 169.40.42.104 |
| 73.83 | vless | 348.9 | 890.0 | 19.7 | 0.0 | 10.0 | 5.91 | 18.22 | Au1rxx-base64 | 169.40.42.90 |
| 73.6 | vless | 359.0 | 862.9 | 19.47 | 0.0 | 10.0 | 5.91 | 18.22 | Au1rxx-base64 | 169.40.42.52 |
| 73.43 | vless | 366.0 | 930.4 | 19.3 | 0.0 | 10.0 | 5.91 | 18.22 | Au1rxx-base64 | 216.152.147.28 |
| 73.34 | vless | 370.2 | 993.7 | 19.21 | 0.0 | 10.0 | 5.91 | 18.22 | Au1rxx-base64 | 169.40.42.184 |
| 73.32 | vless | 316.5 | 854.5 | 20.45 | 0.0 | 10.0 | 5.91 | 18.22 | Au1rxx-base64 | 169.40.42.163 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.885 | 0.823 | 248 | 1633 | prefer |
| Surfboard-tg-mixed | 0.842 | 0.768 | 99 | 7439 | prefer |
| ermaozi | 0.684 | 0.674 | 43 | 436 | observe |
| mheidari-all | 0.509 | 0.426 | 47 | 20485 | observe |
| DeltaKronecker-all | 0.441 | 0.462 | 13 | 5892 | observe |
| xiaoji235-airport-v2ray-all | 0.335 | 1.0 | 1 | 5301 | observe |
| Au1rxx-clash | 0.32 | 1.0 | 1 | 1633 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| tg-oneclickvpnkeys | 0.259 | 1.0 | 1 | 102 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4839 | observe |
| Epodonios-all | 0.255 | None | 0 | 7887 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 8920 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 6075 | observe |
| barry-far-vless | 0.255 | None | 0 | 6291 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | ClientOSError | - | 24 |
| speed | ClientOSError | - | 22 |
| 204 | ProxyError | - | 20 |
| 204 | ProxyConnectionError | - | 16 |
| 204 | TimeoutError | - | 12 |
| cn-block | TimeoutError | - | 9 |
| cn-block | ClientOSError | - | 5 |
| geo | TimeoutError | - | 5 |
| speed | TimeoutError | - | 5 |
| 204 | ClientOSError | - | 3 |
| speed | ProxyError | - | 2 |
| cn-block | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
