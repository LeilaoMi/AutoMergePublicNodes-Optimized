# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-24 13:04:06 |
| 运行耗时 | 250.3s |
| 订阅源总数 | 107 |
| 健康订阅源 | 97 |
| 原始节点 | 78546 |
| 去重后节点 | 21951 |
| TCP 可达 | 3000 |
| 真实可用 | 572 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 21951 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.9 |
| geo | 1.5 |
| tcp | 35.1 |
| probe | 54.4 |
| real_test | 120.0 |
| generate | 32.3 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 49140 |
| shadowsocks | 10295 |
| vmess | 9988 |
| trojan | 7652 |
| hysteria2 | 1098 |
| http | 164 |
| shadowsocksr | 122 |
| socks | 77 |
| hysteria | 7 |
| tuic | 3 |

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
| 80.91 | shadowsocks | 233.3 | 592.6 | 22.38 | 0.0 | 10.0 | 14.09 | 18.44 | mheidari-all | 156.146.38.170 |
| 80.75 | shadowsocks | 240.0 | 614.3 | 22.22 | 0.0 | 10.0 | 14.09 | 18.44 | mheidari-all | 156.146.38.169 |
| 79.05 | shadowsocks | 246.3 | 632.8 | 22.08 | 0.0 | 10.0 | 14.09 | 16.88 | Surfboard-tg-mixed | 156.146.38.167 |
| 78.04 | shadowsocks | 346.8 | 845.7 | 19.75 | 0.0 | 9.06 | 14.09 | 19.4 | Au1rxx-base64 | 154.12.240.141 |
| 77.66 | hysteria2 | 334.7 | 743.1 | 20.03 | 0.0 | 10.0 | 13.7 | 18.44 | mheidari-all | 159.223.157.129 |
| 77.02 | shadowsocks | 293.1 | 677.5 | 20.99 | 0.0 | 8.96 | 14.09 | 19.4 | Au1rxx-base64 | 94.72.127.55 |
| 76.81 | trojan | 279.9 | 600.7 | 21.3 | 0.0 | 10.0 | 12.41 | 19.4 | Au1rxx-base64 | 14.1.28.76 |
| 76.43 | shadowsocks | 286.9 | 585.8 | 21.14 | 0.0 | 10.0 | 14.09 | 19.4 | Au1rxx-base64 | 108.181.0.177 |
| 76.04 | shadowsocks | 295.1 | 557.0 | 20.95 | 0.0 | 10.0 | 14.09 | 18.44 | mheidari-all | 173.244.56.9 |
| 75.83 | shadowsocks | 238.4 | 609.5 | 22.26 | 0.0 | 9.08 | 14.09 | 19.4 | Au1rxx-base64 | 156.146.38.168 |
| 75.82 | shadowsocks | 216.3 | 512.1 | 22.77 | 0.0 | 9.06 | 14.09 | 19.4 | Au1rxx-base64 | 152.67.250.45 |
| 75.5 | shadowsocks | 294.9 | 666.4 | 20.95 | 0.0 | 8.96 | 14.09 | 19.4 | Au1rxx-base64 | 155.138.136.240 |
| 75.42 | vless | 342.4 | 825.9 | 19.85 | 0.0 | 10.0 | 7.96 | 19.4 | Au1rxx-base64 | 15.204.97.209 |
| 75.2 | vless | 323.9 | 772.1 | 20.28 | 0.0 | 9.04 | 7.96 | 19.4 | Au1rxx-base64 | 15.204.97.214 |
| 75.16 | http | 481.7 | 1259.3 | 16.63 | 0.0 | 10.0 | 14.87 | 19.94 | zhangkai | 138.199.35.198 |
| 75.02 | shadowsocks | 310.5 | 723.7 | 20.59 | 0.0 | 10.0 | 14.09 | 18.44 | mheidari-all | 108.181.118.10 |
| 74.92 | trojan | 358.2 | 803.3 | 19.49 | 0.0 | 10.0 | 12.41 | 19.4 | Au1rxx-base64 | 35.91.251.124 |
| 74.49 | shadowsocks | 339.5 | 763.2 | 19.92 | 0.0 | 10.0 | 14.09 | 18.44 | mheidari-all | 37.19.198.160 |
| 74.37 | shadowsocks | 313.3 | 639.7 | 20.53 | 0.0 | 10.0 | 14.09 | 18.44 | mheidari-all | 149.22.95.183 |
| 74.23 | shadowsocks | 333.2 | 738.8 | 20.06 | 0.0 | 10.0 | 14.09 | 18.44 | mheidari-all | 37.19.198.236 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.966 | 1.0 | 23 | 144 | prefer |
| Au1rxx-base64 | 0.937 | 0.874 | 357 | 1628 | prefer |
| mheidari-all | 0.878 | 0.805 | 87 | 14541 | prefer |
| DeltaKronecker-all | 0.871 | 0.8 | 65 | 5914 | prefer |
| Surfboard-tg-mixed | 0.791 | 0.713 | 157 | 6395 | prefer |
| nscl5-all | 0.352 | 1.0 | 2 | 1008 | observe |
| 10ium-ScrapeCategorize-Vless | 0.335 | 1.0 | 1 | 4899 | observe |
| Epodonios-all | 0.255 | None | 0 | 6919 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3988 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7302 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5345 | observe |
| barry-far-vless | 0.255 | None | 0 | 5633 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4097 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.24 | None | 0 | 1629 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| cn-block | TimeoutError | - | 33 |
| geo | TimeoutError | - | 24 |
| 204 | TimeoutError | - | 21 |
| geo | ClientOSError | - | 9 |
| speed | TimeoutError | - | 7 |
| speed | ClientOSError | - | 7 |
| 204 | ClientOSError | - | 5 |
| cn-block | ClientOSError | - | 5 |
| 204 | ProxyError | - | 5 |
| cn-block | ProxyError | - | 4 |
| speed | ClientPayloadError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
