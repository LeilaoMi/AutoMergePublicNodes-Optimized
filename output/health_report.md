# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-09 20:55:08 |
| 运行耗时 | 558.8s |
| 订阅源总数 | 107 |
| 健康订阅源 | 95 |
| 原始节点 | 83567 |
| 去重后节点 | 22107 |
| TCP 可达 | 3000 |
| 真实可用 | 474 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22107 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.7 |
| geo | 1.4 |
| tcp | 36.9 |
| probe | 220.4 |
| real_test | 221.0 |
| generate | 74.4 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 50895 |
| vmess | 12152 |
| shadowsocks | 10142 |
| trojan | 7989 |
| hysteria2 | 1638 |
| http | 554 |
| shadowsocksr | 126 |
| socks | 53 |
| hysteria | 8 |
| tuic | 8 |
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
| 81.47 | vless | 227.1 | 591.6 | 22.52 | 0.0 | 10.0 | 10.63 | 18.32 | Au1rxx-base64 | 195.123.235.177 |
| 80.91 | vless | 251.5 | 657.0 | 21.96 | 0.0 | 10.0 | 10.63 | 18.32 | Au1rxx-base64 | 169.40.42.235 |
| 80.76 | vless | 257.9 | 725.2 | 21.81 | 0.0 | 10.0 | 10.63 | 18.32 | Au1rxx-base64 | 47.253.226.114 |
| 80.39 | vless | 273.9 | 680.9 | 21.44 | 0.0 | 10.0 | 10.63 | 18.32 | Au1rxx-base64 | 169.40.42.212 |
| 80.16 | vless | 283.6 | 635.3 | 21.21 | 0.0 | 10.0 | 10.63 | 18.32 | Au1rxx-base64 | 169.40.42.231 |
| 80.08 | vless | 287.2 | 645.9 | 21.13 | 0.0 | 10.0 | 10.63 | 18.32 | Au1rxx-base64 | 169.40.42.89 |
| 79.76 | vless | 301.1 | 833.8 | 20.81 | 0.0 | 10.0 | 10.63 | 18.32 | Au1rxx-base64 | 137.184.218.169 |
| 79.48 | shadowsocks | 242.3 | 671.3 | 22.17 | 0.0 | 10.0 | 12.99 | 18.32 | Au1rxx-base64 | 37.19.198.243 |
| 79.33 | shadowsocks | 248.6 | 687.9 | 22.02 | 0.0 | 10.0 | 12.99 | 18.32 | Au1rxx-base64 | 37.19.198.236 |
| 79.07 | vless | 324.4 | 871.8 | 20.27 | 0.0 | 10.0 | 10.63 | 18.32 | Au1rxx-base64 | 169.40.42.16 |
| 78.98 | vless | 334.6 | 844.8 | 20.03 | 0.0 | 10.0 | 10.63 | 18.32 | Au1rxx-base64 | 169.40.42.224 |
| 78.93 | vless | 336.8 | 852.0 | 19.98 | 0.0 | 10.0 | 10.63 | 18.32 | Au1rxx-base64 | 169.40.42.90 |
| 78.75 | vless | 344.5 | 874.7 | 19.8 | 0.0 | 10.0 | 10.63 | 18.32 | Au1rxx-base64 | 169.40.42.184 |
| 78.73 | vless | 313.1 | 847.4 | 20.53 | 0.0 | 10.0 | 10.63 | 18.32 | Au1rxx-base64 | 169.40.42.133 |
| 78.72 | shadowsocks | 253.7 | 721.3 | 21.91 | 0.0 | 10.0 | 12.99 | 18.32 | Au1rxx-base64 | 15.204.246.189 |
| 78.61 | vless | 350.9 | 980.0 | 19.66 | 0.0 | 10.0 | 10.63 | 18.32 | Au1rxx-base64 | 185.95.231.156 |
| 78.54 | vless | 353.9 | 844.7 | 19.59 | 0.0 | 10.0 | 10.63 | 18.32 | Au1rxx-base64 | 169.40.42.202 |
| 78.28 | vless | 294.6 | 780.4 | 20.96 | 0.0 | 10.0 | 10.63 | 18.32 | Au1rxx-base64 | 169.40.42.15 |
| 78.25 | vless | 366.4 | 869.9 | 19.3 | 0.0 | 10.0 | 10.63 | 18.32 | Au1rxx-base64 | 169.40.42.95 |
| 78.06 | vless | 241.9 | 634.8 | 22.18 | 0.0 | 6.93 | 10.63 | 18.32 | Au1rxx-base64 | ww9.levikogjgfdd.ir |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.972 | 0.913 | 311 | 1527 | prefer |
| mheidari-all | 0.901 | 0.846 | 26 | 16196 | prefer |
| DeltaKronecker-all | 0.863 | 0.793 | 58 | 5187 | prefer |
| ermaozi | 0.802 | 0.808 | 26 | 410 | prefer |
| Surfboard-tg-mixed | 0.79 | 0.713 | 136 | 7393 | prefer |
| tg-oneclickvpnkeys | 0.317 | 1.0 | 2 | 147 | observe |
| ermaozi-get_subscribe | 0.272 | 1.0 | 1 | 418 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4795 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 8955 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 6033 | observe |
| barry-far-vless | 0.255 | None | 0 | 6253 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4247 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| cn-block | TimeoutError | - | 17 |
| geo | ClientOSError | - | 16 |
| 204 | TimeoutError | - | 14 |
| 204 | ProxyError | - | 12 |
| cn-block | ClientOSError | - | 8 |
| geo | TimeoutError | - | 7 |
| speed | ClientOSError | - | 7 |
| 204 | ClientOSError | - | 4 |
| speed | TimeoutError | - | 2 |
| sing-box exited 1 |  [31mFATAL[0m[0000] start service: start inbound/socks[socks-in]: listen tcp 127.0.0.1:31319: bind: address already in use | - | 1 |
| cn-block | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
