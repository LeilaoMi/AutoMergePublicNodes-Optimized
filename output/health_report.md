# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-22 21:49:39 |
| 运行耗时 | 287.5s |
| 订阅源总数 | 107 |
| 健康订阅源 | 92 |
| 原始节点 | 96237 |
| 去重后节点 | 26704 |
| TCP 可达 | 3000 |
| 真实可用 | 367 |
| Verified 输出 | 113 |
| Global 输出 | 300 |
| All 输出 | 26704 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.5 |
| geo | 1.7 |
| tcp | 79.6 |
| probe | 95.4 |
| real_test | 69.5 |
| china_check | 19.7 |
| write_verified | 0.1 |
| generate | 14.2 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 57050 |
| vmess | 17125 |
| shadowsocks | 12369 |
| trojan | 7877 |
| hysteria2 | 1359 |
| http | 298 |
| socks | 59 |
| shadowsocksr | 55 |
| anytls | 22 |
| hysteria | 17 |
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
| 95.44 | hysteria2 | 226.5 | 3.2 | 22.54 | 14.88 | 10.0 | 13.12 | 16.4 | Au1rxx-base64 | 129.213.91.185 |
| 91.85 | vless | 290.0 | 2.7 | 21.06 | 14.9 | 10.0 | 9.49 | 16.4 | Au1rxx-base64 | 169.40.42.235 |
| 91.83 | shadowsocks | 243.7 | 1.8 | 22.14 | 14.93 | 10.0 | 12.36 | 16.4 | Au1rxx-base64 | 37.19.198.236 |
| 91.52 | shadowsocks | 234.3 | 2.4 | 22.35 | 14.91 | 10.0 | 12.36 | 16.4 | Au1rxx-base64 | 185.230.230.18 |
| 91.48 | shadowsocks | 253.2 | 4.7 | 21.92 | 14.82 | 9.98 | 12.36 | 16.4 | Au1rxx-base64 | 37.19.198.244 |
| 91.07 | shadowsocks | 243.3 | 9.0 | 22.15 | 14.66 | 10.0 | 12.36 | 16.4 | Au1rxx-base64 | 193.151.163.18 |
| 91.0 | shadowsocks | 279.3 | 1.9 | 21.31 | 14.93 | 10.0 | 12.36 | 16.4 | Au1rxx-base64 | 37.19.198.160 |
| 90.63 | shadowsocks | 246.5 | 0.4 | 22.07 | 14.99 | 8.81 | 12.36 | 16.4 | Au1rxx-base64 | 37.19.198.243 |
| 90.12 | shadowsocks | 298.7 | 0.1 | 20.86 | 15.0 | 10.0 | 12.36 | 16.4 | Au1rxx-base64 | 185.215.132.18 |
| 89.91 | vless | 374.9 | 2.1 | 19.1 | 14.92 | 10.0 | 9.49 | 16.4 | Au1rxx-base64 | 169.40.42.168 |
| 89.75 | vless | 318.3 | 10.4 | 20.41 | 14.61 | 8.84 | 9.49 | 16.4 | Au1rxx-base64 | 169.40.42.90 |
| 89.59 | vless | 374.6 | 10.9 | 19.11 | 14.59 | 10.0 | 9.49 | 16.4 | Au1rxx-base64 | 169.40.42.231 |
| 89.56 | shadowsocks | 322.5 | 0.2 | 20.31 | 14.99 | 10.0 | 12.36 | 16.4 | Au1rxx-base64 | 185.215.132.9 |
| 89.55 | vless | 339.7 | 1.8 | 19.92 | 14.93 | 10.0 | 9.49 | 16.4 | Au1rxx-base64 | 169.40.42.229 |
| 89.47 | shadowsocks | 323.6 | 2.1 | 20.29 | 14.92 | 10.0 | 12.36 | 16.4 | Au1rxx-base64 | 45.86.51.18 |
| 89.45 | vless | 385.8 | 7.8 | 18.85 | 14.71 | 10.0 | 9.49 | 16.4 | Au1rxx-base64 | 169.40.42.89 |
| 88.91 | vless | 358.7 | 6.8 | 19.47 | 14.74 | 8.81 | 9.49 | 16.4 | Au1rxx-base64 | 185.95.231.156 |
| 88.4 | shadowsocks | 291.2 | 0.7 | 21.04 | 14.97 | 10.0 | 12.36 | 16.4 | Au1rxx-base64 | 156.146.38.169 |
| 87.17 | vless | 375.3 | 7.9 | 19.09 | 14.7 | 8.6 | 9.49 | 16.4 | Au1rxx-base64 | 5.34.178.120 |
| 87.11 | shadowsocks | 375.7 | 7.8 | 19.08 | 14.71 | 10.0 | 12.36 | 16.4 | Au1rxx-base64 | 193.151.160.9 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.982 | 0.972 | 72 | 573 | prefer |
| Au1rxx-base64 | 0.884 | 0.823 | 265 | 1601 | prefer |
| mheidari-all | 0.88 | 0.808 | 78 | 23896 | prefer |
| Surfboard-tg-mixed | 0.664 | 1.0 | 9 | 7066 | observe |
| DeltaKronecker-all | 0.407 | 0.455 | 11 | 3641 | observe |
| SoliSpirit-all | 0.335 | 1.0 | 1 | 10026 | observe |
| mahdibland-V2RayAggregator | 0.335 | 1.0 | 1 | 4176 | observe |
| roosterkid-openproxylist-v2ray | 0.317 | 1.0 | 2 | 150 | observe |
| tg-LonUp_M | 0.262 | 1.0 | 1 | 175 | observe |
| tg-oneclickvpnkeys | 0.257 | 1.0 | 1 | 54 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5015 | observe |
| Epodonios-all | 0.255 | None | 0 | 7550 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5426 | observe |
| barry-far-vless | 0.255 | None | 0 | 5640 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 35 |
| speed | ClientOSError | - | 15 |
| 204 | ProxyError | - | 7 |
| cn-block | ProxyError | - | 4 |
| geo | ClientOSError | - | 4 |
| 204 | TimeoutError | - | 3 |
| cn-block | ClientOSError | - | 2 |
| 204 | ClientOSError | - | 2 |
| geo | TimeoutError | - | 1 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 111 | 113 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
