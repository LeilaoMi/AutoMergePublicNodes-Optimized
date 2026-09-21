# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-21 22:01:53 |
| 运行耗时 | 605.2s |
| 订阅源总数 | 107 |
| 健康订阅源 | 96 |
| 原始节点 | 88299 |
| 去重后节点 | 25177 |
| TCP 可达 | 3000 |
| 真实可用 | 511 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 25177 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.9 |
| geo | 1.5 |
| tcp | 42.6 |
| probe | 268.4 |
| real_test | 201.2 |
| generate | 85.6 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 52966 |
| vmess | 14150 |
| shadowsocks | 10240 |
| trojan | 8810 |
| hysteria2 | 1268 |
| http | 627 |
| shadowsocksr | 139 |
| socks | 67 |
| hysteria | 14 |
| anytls | 12 |
| tuic | 6 |

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
| 80.31 | shadowsocks | 251.5 | 630.9 | 21.96 | 0.0 | 10.0 | 13.45 | 18.9 | mheidari-all | 156.146.38.168 |
| 80.09 | shadowsocks | 260.9 | 644.2 | 21.74 | 0.0 | 10.0 | 13.45 | 18.9 | mheidari-all | 156.146.38.170 |
| 79.58 | vless | 220.1 | 601.9 | 22.68 | 0.0 | 8.93 | 9.59 | 18.38 | Au1rxx-base64 | 195.211.98.43 |
| 79.51 | shadowsocks | 285.9 | 735.1 | 21.16 | 0.0 | 10.0 | 13.45 | 18.9 | mheidari-all | 37.19.198.244 |
| 79.43 | shadowsocks | 289.5 | 740.8 | 21.08 | 0.0 | 10.0 | 13.45 | 18.9 | mheidari-all | 37.19.198.160 |
| 79.39 | shadowsocks | 290.9 | 741.5 | 21.04 | 0.0 | 10.0 | 13.45 | 18.9 | mheidari-all | 37.19.198.236 |
| 78.98 | shadowsocks | 287.3 | 706.1 | 21.13 | 0.0 | 10.0 | 13.45 | 18.9 | mheidari-all | 15.204.247.206 |
| 78.33 | vless | 271.9 | 713.9 | 21.48 | 0.0 | 8.88 | 9.59 | 18.38 | Au1rxx-base64 | 79.141.172.154 |
| 77.87 | shadowsocks | 266.7 | 627.3 | 21.6 | 0.0 | 10.0 | 13.45 | 18.9 | mheidari-all | 23.150.248.20 |
| 77.5 | vless | 308.0 | 693.4 | 20.65 | 0.0 | 8.88 | 9.59 | 18.38 | Au1rxx-base64 | 169.40.42.179 |
| 76.89 | vless | 334.6 | 705.7 | 20.03 | 0.0 | 8.89 | 9.59 | 18.38 | Au1rxx-base64 | 169.40.42.133 |
| 76.81 | shadowsocks | 344.0 | 836.9 | 19.82 | 0.0 | 10.0 | 13.45 | 18.9 | mheidari-all | 38.180.135.156 |
| 76.61 | vless | 346.7 | 750.3 | 19.75 | 0.0 | 8.89 | 9.59 | 18.38 | Au1rxx-base64 | 169.40.42.173 |
| 76.4 | vless | 355.3 | 911.5 | 19.55 | 0.0 | 8.88 | 9.59 | 18.38 | Au1rxx-base64 | 169.40.42.89 |
| 76.31 | vless | 323.7 | 672.6 | 20.28 | 0.0 | 8.87 | 9.59 | 18.38 | Au1rxx-base64 | 169.40.42.225 |
| 76.03 | hysteria2 | 293.2 | 694.4 | 20.99 | 0.0 | 10.0 | 14.21 | 18.9 | mheidari-all | 159.223.157.129 |
| 75.69 | vless | 351.0 | 867.8 | 19.65 | 0.0 | 8.89 | 9.59 | 18.38 | Au1rxx-base64 | 169.40.42.90 |
| 75.52 | vless | 306.1 | 733.1 | 20.69 | 0.0 | 8.88 | 9.59 | 18.38 | Au1rxx-base64 | 169.40.42.163 |
| 75.42 | vless | 395.6 | 893.3 | 18.62 | 0.0 | 8.89 | 9.59 | 18.38 | Au1rxx-base64 | 169.40.42.35 |
| 75.14 | vless | 362.3 | 918.3 | 19.39 | 0.0 | 8.89 | 9.59 | 18.38 | Au1rxx-base64 | 169.40.42.52 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.937 | 0.87 | 277 | 1752 | prefer |
| Surfboard-tg-mixed | 0.891 | 0.819 | 72 | 7121 | prefer |
| ermaozi | 0.698 | 0.694 | 36 | 350 | observe |
| mheidari-all | 0.638 | 0.558 | 319 | 20197 | observe |
| DeltaKronecker-all | 0.489 | 0.667 | 9 | 6181 | observe |
| ermaozi-get_subscribe | 0.27 | 1.0 | 1 | 377 | observe |
| tg-oneclickvpnkeys | 0.261 | 1.0 | 1 | 138 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5290 | observe |
| Epodonios-all | 0.255 | None | 0 | 7717 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3996 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 8749 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5672 | observe |
| barry-far-vless | 0.255 | None | 0 | 6075 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4344 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| cn-block | ClientOSError | - | 56 |
| geo | ClientOSError | - | 35 |
| geo | TimeoutError | - | 27 |
| speed | ClientOSError | - | 27 |
| 204 | ProxyError | - | 17 |
| cn-block | TimeoutError | - | 17 |
| 204 | TimeoutError | - | 12 |
| speed | TimeoutError | - | 10 |
| cn-block | ProxyError | - | 2 |
| 204 | ClientOSError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
