# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-17 21:18:13 |
| 运行耗时 | 512.8s |
| 订阅源总数 | 107 |
| 健康订阅源 | 95 |
| 原始节点 | 84619 |
| 去重后节点 | 23068 |
| TCP 可达 | 3000 |
| 真实可用 | 438 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23068 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.3 |
| geo | 1.4 |
| tcp | 36.1 |
| probe | 196.4 |
| real_test | 188.2 |
| generate | 84.4 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 50816 |
| vmess | 13348 |
| shadowsocks | 10081 |
| trojan | 8230 |
| hysteria2 | 1351 |
| http | 595 |
| shadowsocksr | 120 |
| socks | 66 |
| hysteria | 8 |
| tuic | 2 |
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
| 80.35 | vless | 247.1 | 697.1 | 22.06 | 0.0 | 10.0 | 9.73 | 18.56 | Au1rxx-base64 | 79.141.172.154 |
| 79.73 | vless | 263.5 | 695.8 | 21.68 | 0.0 | 10.0 | 9.73 | 18.56 | Au1rxx-base64 | 169.40.42.235 |
| 79.68 | vless | 276.1 | 612.2 | 21.39 | 0.0 | 10.0 | 9.73 | 18.56 | Au1rxx-base64 | 169.40.42.184 |
| 79.19 | vless | 297.2 | 671.8 | 20.9 | 0.0 | 10.0 | 9.73 | 18.56 | Au1rxx-base64 | 169.40.42.229 |
| 79.18 | vless | 297.6 | 729.8 | 20.89 | 0.0 | 10.0 | 9.73 | 18.56 | Au1rxx-base64 | 169.40.42.231 |
| 78.92 | vless | 308.6 | 819.8 | 20.63 | 0.0 | 10.0 | 9.73 | 18.56 | Au1rxx-base64 | 169.40.42.168 |
| 78.81 | vless | 309.0 | 824.0 | 20.63 | 0.0 | 10.0 | 9.73 | 18.56 | Au1rxx-base64 | 167.17.69.171 |
| 78.8 | vless | 313.9 | 712.2 | 20.51 | 0.0 | 10.0 | 9.73 | 18.56 | Au1rxx-base64 | 169.40.42.75 |
| 78.62 | hysteria2 | 233.1 | 642.6 | 22.38 | 0.0 | 10.0 | 13.24 | 14.1 | mheidari-all | 159.223.157.129 |
| 78.53 | vless | 325.5 | 904.3 | 20.24 | 0.0 | 10.0 | 9.73 | 18.56 | Au1rxx-base64 | 185.95.231.156 |
| 78.44 | vless | 250.3 | 666.2 | 21.98 | 0.0 | 10.0 | 9.73 | 18.56 | Au1rxx-base64 | 169.40.42.133 |
| 78.28 | shadowsocks | 314.2 | 828.9 | 20.5 | 0.0 | 10.0 | 13.72 | 18.56 | Au1rxx-base64 | 38.180.135.156 |
| 77.92 | vless | 351.8 | 918.6 | 19.63 | 0.0 | 10.0 | 9.73 | 18.56 | Au1rxx-base64 | 169.40.42.202 |
| 77.71 | vless | 340.6 | 865.5 | 19.89 | 0.0 | 10.0 | 9.73 | 18.56 | Au1rxx-base64 | 169.40.42.232 |
| 77.54 | vless | 368.4 | 870.7 | 19.25 | 0.0 | 10.0 | 9.73 | 18.56 | Au1rxx-base64 | 169.40.42.163 |
| 77.35 | vless | 286.8 | 638.9 | 21.14 | 0.0 | 10.0 | 9.73 | 18.56 | Au1rxx-base64 | 169.40.42.89 |
| 77.33 | vless | 283.9 | 620.9 | 21.21 | 0.0 | 10.0 | 9.73 | 18.56 | Au1rxx-base64 | 169.40.42.212 |
| 77.28 | vless | 307.5 | 647.6 | 20.66 | 0.0 | 10.0 | 9.73 | 18.56 | Au1rxx-base64 | 169.40.42.15 |
| 76.91 | vless | 373.8 | 987.7 | 19.12 | 0.0 | 10.0 | 9.73 | 18.56 | Au1rxx-base64 | 169.40.42.182 |
| 76.5 | vless | 251.9 | 651.7 | 21.95 | 0.0 | 10.0 | 9.73 | 18.56 | Au1rxx-base64 | 137.184.218.169 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| mheidari-all | 0.989 | 0.935 | 31 | 16164 | prefer |
| Au1rxx-base64 | 0.986 | 0.925 | 265 | 1619 | prefer |
| DeltaKronecker-all | 0.893 | 0.818 | 121 | 5931 | prefer |
| Surfboard-tg-mixed | 0.886 | 0.815 | 65 | 7499 | prefer |
| ermaozi | 0.449 | 0.5 | 16 | 357 | observe |
| mahdibland-V2RayAggregator | 0.335 | 1.0 | 1 | 4261 | observe |
| Epodonios-all | 0.255 | None | 0 | 7954 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 8875 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5936 | observe |
| barry-far-vless | 0.255 | None | 0 | 6157 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.24 | None | 0 | 1619 | observe |
| ermaozi-get_subscribe | 0.234 | 0.4 | 5 | 361 | downweight |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| cn-block | TimeoutError | - | 14 |
| 204 | ProxyError | - | 13 |
| geo | ClientOSError | - | 9 |
| geo | TimeoutError | - | 9 |
| 204 | TimeoutError | - | 8 |
| speed | ClientOSError | - | 6 |
| cn-block | ClientOSError | - | 4 |
| 204 | ClientOSError | - | 2 |
| speed | TimeoutError | - | 2 |
| cn-block | ProxyError | - | 1 |
| speed | ProxyError | - | 1 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
