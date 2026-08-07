# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-07 13:19:06 |
| 运行耗时 | 236.9s |
| 订阅源总数 | 107 |
| 健康订阅源 | 100 |
| 原始节点 | 82701 |
| 去重后节点 | 23372 |
| TCP 可达 | 3000 |
| 真实可用 | 468 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23372 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.5 |
| geo | 1.4 |
| tcp | 35.7 |
| probe | 48.4 |
| real_test | 106.3 |
| generate | 39.5 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 47542 |
| vmess | 12851 |
| trojan | 11180 |
| shadowsocks | 9644 |
| hysteria2 | 1294 |
| shadowsocksr | 69 |
| socks | 63 |
| http | 35 |
| hysteria | 13 |
| tuic | 10 |

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
| 85.16 | hysteria2 | 232.9 | 637.7 | 22.39 | 0.0 | 10.0 | 14.29 | 19.58 | Au1rxx-base64 | 159.223.157.129 |
| 84.99 | hysteria2 | 244.4 | 683.4 | 22.12 | 0.0 | 10.0 | 14.29 | 19.58 | Au1rxx-base64 | 138.124.68.188 |
| 82.02 | trojan | 258.2 | 703.4 | 21.8 | 0.0 | 10.0 | 13.64 | 19.58 | Au1rxx-base64 | 153.75.250.171 |
| 81.59 | shadowsocks | 220.0 | 591.2 | 22.69 | 0.0 | 10.0 | 13.32 | 19.58 | Au1rxx-base64 | 198.98.53.130 |
| 81.39 | shadowsocks | 228.5 | 626.0 | 22.49 | 0.0 | 10.0 | 13.32 | 19.58 | Au1rxx-base64 | 37.19.198.244 |
| 80.9 | shadowsocks | 249.7 | 697.7 | 22.0 | 0.0 | 10.0 | 13.32 | 19.58 | Au1rxx-base64 | 37.19.198.236 |
| 80.57 | hysteria2 | 253.3 | 703.0 | 21.91 | 0.0 | 5.79 | 14.29 | 19.58 | Au1rxx-base64 | usa1.spectrumproxy.shop |
| 80.52 | shadowsocks | 244.3 | 672.5 | 22.12 | 0.0 | 10.0 | 13.32 | 19.58 | Au1rxx-base64 | 68.168.222.210 |
| 79.94 | shadowsocks | 291.2 | 807.9 | 21.04 | 0.0 | 10.0 | 13.32 | 19.58 | Au1rxx-base64 | 37.19.198.160 |
| 77.05 | hysteria2 | 350.0 | 675.0 | 19.68 | 0.0 | 10.0 | 14.29 | 19.58 | Au1rxx-base64 | 62.210.124.146 |
| 75.57 | hysteria2 | 420.2 | 873.4 | 18.05 | 0.0 | 10.0 | 14.29 | 19.58 | Au1rxx-base64 | 5.255.102.165 |
| 73.37 | shadowsocks | 356.6 | 741.1 | 19.52 | 0.0 | 10.0 | 13.32 | 19.58 | Au1rxx-base64 | 173.244.56.6 |
| 73.24 | shadowsocks | 278.1 | 642.4 | 21.34 | 0.0 | 10.0 | 13.32 | 19.58 | Au1rxx-base64 | 156.146.38.170 |
| 73.19 | shadowsocks | 281.6 | 651.0 | 21.26 | 0.0 | 10.0 | 13.32 | 19.58 | Au1rxx-base64 | 156.146.38.169 |
| 72.91 | shadowsocks | 285.9 | 656.3 | 21.16 | 0.0 | 10.0 | 13.32 | 19.58 | Au1rxx-base64 | 156.146.38.168 |
| 72.79 | shadowsocks | 341.2 | 638.3 | 19.88 | 0.0 | 10.0 | 13.32 | 19.58 | Au1rxx-base64 | 108.181.0.177 |
| 72.77 | shadowsocks | 351.0 | 691.1 | 19.65 | 0.0 | 10.0 | 13.32 | 19.58 | Au1rxx-base64 | 149.22.95.183 |
| 72.7 | hysteria2 | 353.5 | 670.8 | 19.59 | 0.0 | 10.0 | 14.29 | 19.58 | Au1rxx-base64 | 31.76.113.32 |
| 72.7 | trojan | 378.1 | 608.1 | 19.03 | 0.0 | 10.0 | 13.64 | 19.58 | Au1rxx-base64 | 44.246.163.102 |
| 72.65 | trojan | 388.1 | 623.5 | 18.79 | 0.0 | 10.0 | 13.64 | 19.58 | Au1rxx-base64 | 44.242.235.129 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.994 | 0.937 | 347 | 1509 | prefer |
| zhangkai | 0.956 | 1.0 | 20 | 25 | prefer |
| DeltaKronecker-all | 0.638 | 0.559 | 195 | 5326 | observe |
| mheidari-all | 0.446 | 0.8 | 5 | 17690 | observe |
| Surfboard-tg-mixed | 0.403 | 0.31 | 29 | 6364 | observe |
| nscl5-all | 0.326 | 1.0 | 1 | 1772 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5282 | observe |
| Epodonios-all | 0.255 | None | 0 | 6987 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3996 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7685 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5147 | observe |
| barry-far-vless | 0.255 | None | 0 | 5471 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5247 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.235 | None | 0 | 1509 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 30 |
| 204 | ProxyError | - | 24 |
| geo | ClientOSError | - | 21 |
| 204 | TimeoutError | - | 16 |
| cn-block | TimeoutError | - | 14 |
| speed | TimeoutError | - | 11 |
| speed | ClientOSError | - | 9 |
| 204 | ClientOSError | - | 3 |
| cn-block | ClientOSError | - | 2 |
| cn-block | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
