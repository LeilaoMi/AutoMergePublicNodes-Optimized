# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-16 04:29:58 |
| 运行耗时 | 820.0s |
| 订阅源总数 | 107 |
| 健康订阅源 | 95 |
| 原始节点 | 85338 |
| 去重后节点 | 23260 |
| TCP 可达 | 3000 |
| 真实可用 | 515 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23260 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.7 |
| geo | 1.4 |
| tcp | 37.9 |
| probe | 273.2 |
| real_test | 420.1 |
| generate | 80.7 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 52099 |
| vmess | 12921 |
| shadowsocks | 9526 |
| trojan | 8331 |
| hysteria2 | 1567 |
| http | 680 |
| shadowsocksr | 130 |
| socks | 68 |
| hysteria | 9 |
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
| 83.19 | hysteria2 | 249.2 | 676.0 | 22.01 | 0.0 | 10.0 | 12.5 | 19.78 | mheidari-all | 159.223.157.129 |
| 82.91 | vless | 229.5 | 609.1 | 22.47 | 0.0 | 10.0 | 11.48 | 18.96 | Au1rxx-base64 | 195.123.235.177 |
| 82.61 | vless | 242.4 | 687.1 | 22.17 | 0.0 | 10.0 | 11.48 | 18.96 | Au1rxx-base64 | 47.253.226.114 |
| 82.59 | vless | 243.0 | 643.5 | 22.15 | 0.0 | 10.0 | 11.48 | 18.96 | Au1rxx-base64 | 137.184.218.169 |
| 82.33 | shadowsocks | 227.8 | 623.1 | 22.51 | 0.0 | 10.0 | 14.04 | 19.78 | mheidari-all | 37.19.198.243 |
| 82.12 | shadowsocks | 236.6 | 649.5 | 22.3 | 0.0 | 10.0 | 14.04 | 19.78 | mheidari-all | 37.19.198.244 |
| 81.88 | vless | 274.0 | 671.4 | 21.44 | 0.0 | 10.0 | 11.48 | 18.96 | Au1rxx-base64 | 169.40.42.231 |
| 81.68 | vless | 282.6 | 634.5 | 21.24 | 0.0 | 10.0 | 11.48 | 18.96 | Au1rxx-base64 | 169.40.42.235 |
| 81.45 | vless | 292.4 | 663.3 | 21.01 | 0.0 | 10.0 | 11.48 | 18.96 | Au1rxx-base64 | 169.40.42.89 |
| 80.81 | vless | 319.9 | 809.0 | 20.37 | 0.0 | 10.0 | 11.48 | 18.96 | Au1rxx-base64 | 169.40.42.184 |
| 80.71 | vless | 324.3 | 878.3 | 20.27 | 0.0 | 10.0 | 11.48 | 18.96 | Au1rxx-base64 | 169.40.42.229 |
| 80.55 | vless | 275.7 | 612.2 | 21.4 | 0.0 | 10.0 | 11.48 | 18.96 | Au1rxx-base64 | 169.40.42.16 |
| 80.43 | vless | 336.4 | 913.9 | 19.99 | 0.0 | 10.0 | 11.48 | 18.96 | Au1rxx-base64 | 169.40.42.35 |
| 80.34 | vless | 340.4 | 870.6 | 19.9 | 0.0 | 10.0 | 11.48 | 18.96 | Au1rxx-base64 | 169.40.42.182 |
| 80.29 | vless | 342.5 | 957.8 | 19.85 | 0.0 | 10.0 | 11.48 | 18.96 | Au1rxx-base64 | 185.95.231.156 |
| 80.25 | vless | 344.3 | 934.2 | 19.81 | 0.0 | 10.0 | 11.48 | 18.96 | Au1rxx-base64 | 169.40.42.163 |
| 80.1 | vless | 285.1 | 744.2 | 21.18 | 0.0 | 10.0 | 11.48 | 18.96 | Au1rxx-base64 | 169.40.42.74 |
| 79.88 | vless | 360.1 | 851.2 | 19.44 | 0.0 | 10.0 | 11.48 | 18.96 | Au1rxx-base64 | 169.40.42.95 |
| 79.88 | vless | 360.2 | 979.1 | 19.44 | 0.0 | 10.0 | 11.48 | 18.96 | Au1rxx-base64 | 169.40.42.133 |
| 79.86 | vless | 361.3 | 870.5 | 19.42 | 0.0 | 10.0 | 11.48 | 18.96 | Au1rxx-base64 | 169.40.42.225 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.93 | 0.865 | 275 | 1685 | prefer |
| ermaozi | 0.736 | 0.727 | 55 | 407 | prefer |
| Surfboard-tg-mixed | 0.71 | 0.632 | 190 | 7549 | prefer |
| mheidari-all | 0.653 | 0.574 | 115 | 16114 | observe |
| ermaozi-get_subscribe | 0.467 | 0.857 | 7 | 438 | observe |
| DeltaKronecker-all | 0.308 | 0.225 | 187 | 5932 | observe |
| 10ium-HighSpeed | 0.289 | 1.0 | 1 | 839 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| tg-oneclickvpnkeys | 0.262 | 1.0 | 1 | 163 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5015 | observe |
| Epodonios-all | 0.255 | None | 0 | 8042 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 8939 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 6134 | observe |
| barry-far-vless | 0.255 | None | 0 | 6344 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 119 |
| geo | ClientOSError | - | 51 |
| speed | TimeoutError | - | 49 |
| speed | ClientOSError | - | 27 |
| 204 | ProxyError | - | 19 |
| cn-block | ClientOSError | - | 17 |
| cn-block | TimeoutError | - | 17 |
| 204 | TimeoutError | - | 14 |
| 204 | ClientOSError | - | 2 |
| speed | ProxyError | - | 2 |
| 204 | ProxyConnectionError | - | 1 |
| cn-block | ProxyError | - | 1 |
| 204 | ServerDisconnectedError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
