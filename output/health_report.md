# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-17 15:48:30 |
| 运行耗时 | 305.0s |
| 订阅源总数 | 107 |
| 健康订阅源 | 93 |
| 原始节点 | 99259 |
| 去重后节点 | 27641 |
| TCP 可达 | 3000 |
| 真实可用 | 373 |
| Verified 输出 | 121 |
| Global 输出 | 300 |
| All 输出 | 27641 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.9 |
| geo | 1.5 |
| tcp | 87.3 |
| probe | 88.1 |
| real_test | 80.8 |
| china_check | 30.7 |
| generate | 10.8 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 58331 |
| vmess | 16633 |
| shadowsocks | 11967 |
| trojan | 10141 |
| hysteria2 | 1341 |
| http | 571 |
| shadowsocksr | 169 |
| socks | 57 |
| anytls | 26 |
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
| 94.66 | shadowsocks | 253.3 | 2.0 | 21.92 | 14.93 | 10.0 | 13.85 | 17.96 | Au1rxx-base64 | 149.22.95.183 |
| 93.17 | shadowsocks | 281.7 | 0.5 | 21.26 | 14.98 | 10.0 | 13.85 | 17.96 | Au1rxx-base64 | 173.244.56.9 |
| 93.05 | vless | 189.4 | 1.4 | 23.39 | 14.95 | 9.75 | 10.0 | 17.96 | Au1rxx-base64 | 176.122.183.26 |
| 92.31 | shadowsocks | 333.4 | 1.5 | 20.06 | 14.94 | 10.0 | 13.85 | 17.96 | Au1rxx-base64 | 103.11.76.248 |
| 91.94 | vless | 377.7 | 1.6 | 19.04 | 14.94 | 10.0 | 10.0 | 17.96 | Au1rxx-base64 | 51.81.203.63 |
| 91.35 | shadowsocks | 292.1 | 1.9 | 21.02 | 14.93 | 10.0 | 13.85 | 17.96 | Au1rxx-base64 | 156.146.38.167 |
| 91.27 | vless | 400.3 | 1.7 | 18.51 | 14.94 | 9.95 | 10.0 | 17.96 | Au1rxx-base64 | 95.111.212.241 |
| 91.24 | vless | 211.0 | 1.3 | 22.89 | 14.95 | 6.44 | 10.0 | 17.96 | Au1rxx-base64 | 154.40.55.185 |
| 90.95 | vless | 211.8 | 3.7 | 22.87 | 14.86 | 5.26 | 10.0 | 17.96 | Au1rxx-base64 | 154.9.241.170 |
| 90.74 | shadowsocks | 289.5 | 1.3 | 21.08 | 14.95 | 10.0 | 13.85 | 17.96 | Au1rxx-base64 | 156.146.38.169 |
| 89.66 | vless | 198.4 | 0.1 | 23.19 | 14.99 | 6.52 | 10.0 | 17.96 | Au1rxx-base64 | 45.63.53.81 |
| 89.46 | vless | 313.3 | 2.4 | 20.52 | 14.91 | 10.0 | 10.0 | 17.96 | Au1rxx-base64 | 147.45.60.160 |
| 87.81 | vless | 193.4 | 1.0 | 23.3 | 14.96 | 6.59 | 10.0 | 17.96 | Au1rxx-base64 | 67.209.184.133 |
| 86.92 | shadowsocks | 271.1 | 2.4 | 21.5 | 14.91 | 9.84 | 13.85 | 17.96 | Au1rxx-base64 | 149.22.87.240 |
| 86.53 | vless | 174.0 | 4.9 | 23.75 | 14.82 | 0.0 | 10.0 | 17.96 | Au1rxx-base64 | 47.251.108.158 |
| 86.46 | shadowsocks | 292.5 | 0.2 | 21.01 | 14.99 | 9.84 | 13.85 | 17.96 | Au1rxx-base64 | 149.22.87.241 |
| 85.89 | shadowsocks | 296.3 | 0.4 | 20.92 | 14.99 | 10.0 | 13.85 | 17.96 | Au1rxx-base64 | 156.146.38.168 |
| 85.75 | shadowsocks | 395.3 | 2.9 | 18.63 | 14.89 | 10.0 | 13.85 | 17.96 | Au1rxx-base64 | 37.19.198.244 |
| 85.58 | hysteria2 | 347.2 | 0.6 | 19.74 | 14.98 | 5.11 | 12.69 | 17.96 | Au1rxx-base64 | 129.213.91.185 |
| 85.51 | hysteria2 | 178.6 | 0.4 | 23.64 | 14.98 | 0.0 | 12.69 | 17.96 | Au1rxx-base64 | 179.255.104.98 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.928 | 0.931 | 29 | 623 | prefer |
| Au1rxx-base64 | 0.871 | 0.792 | 400 | 1993 | prefer |
| mheidari-all | 0.817 | 0.789 | 19 | 23770 | prefer |
| ninja-vless | 0.43 | 1.0 | 3 | 1791 | observe |
| Surfboard-tg-mixed | 0.374 | 0.281 | 32 | 7171 | observe |
| roosterkid-openproxylist-v2ray | 0.317 | 1.0 | 2 | 150 | observe |
| DeltaKronecker-all | 0.272 | 0.286 | 7 | 4999 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4986 | observe |
| Au1rxx-clash | 0.255 | None | 0 | 1993 | observe |
| Epodonios-all | 0.255 | None | 0 | 7678 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 10049 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5617 | observe |
| barry-far-vless | 0.255 | None | 0 | 5865 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4255 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 49 |
| geo | ClientOSError | - | 15 |
| 204 | ProxyError | - | 12 |
| speed | ClientOSError | - | 11 |
| 204 | TimeoutError | - | 9 |
| speed | ProxyError | - | 6 |
| cn-block | ProxyError | - | 4 |
| 204 | ClientOSError | - | 4 |
| geo | ProxyError | - | 3 |
| cn-block | ClientOSError | - | 3 |
| cn-block | TimeoutError | - | 2 |
| geo | TimeoutError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | True | 121 | 40 | 0.5 |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
