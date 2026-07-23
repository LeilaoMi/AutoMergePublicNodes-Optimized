# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-23 19:31:20 |
| 运行耗时 | 289.0s |
| 订阅源总数 | 107 |
| 健康订阅源 | 102 |
| 原始节点 | 83072 |
| 去重后节点 | 22758 |
| TCP 可达 | 3000 |
| 真实可用 | 598 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22758 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.4 |
| geo | 1.3 |
| tcp | 32.5 |
| probe | 60.8 |
| real_test | 160.0 |
| generate | 30.0 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 48034 |
| trojan | 14356 |
| vmess | 10056 |
| shadowsocks | 10000 |
| hysteria2 | 421 |
| shadowsocksr | 75 |
| socks | 54 |
| http | 50 |
| hysteria | 14 |
| tuic | 9 |
| anytls | 3 |

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
| 76.4 | shadowsocks | 246.0 | 665.1 | 22.08 | 0.0 | 10.0 | 12.52 | 15.8 | Au1rxx-base64 | 37.19.198.244 |
| 75.59 | vless | 260.6 | 685.6 | 21.74 | 0.0 | 10.0 | 5.29 | 18.56 | mheidari-all | 47.89.186.170 |
| 75.07 | vless | 266.6 | 631.7 | 21.61 | 0.0 | 10.0 | 5.29 | 18.56 | mheidari-all | 154.193.55.183 |
| 74.37 | trojan | 301.9 | 646.9 | 20.79 | 0.0 | 10.0 | 12.23 | 18.56 | mheidari-all | 163.245.196.68 |
| 74.34 | shadowsocks | 313.5 | 846.9 | 20.52 | 0.0 | 10.0 | 12.52 | 15.8 | Au1rxx-base64 | 68.168.222.210 |
| 73.78 | shadowsocks | 280.0 | 646.9 | 21.3 | 0.0 | 10.0 | 12.52 | 15.8 | Au1rxx-base64 | 156.146.38.167 |
| 73.61 | shadowsocks | 237.3 | 637.4 | 22.29 | 0.0 | 10.0 | 12.52 | 15.8 | Au1rxx-base64 | 37.19.198.160 |
| 73.47 | shadowsocks | 329.4 | 829.8 | 20.15 | 0.0 | 10.0 | 12.52 | 15.8 | Au1rxx-base64 | 185.196.61.82 |
| 72.81 | vless | 304.6 | 685.3 | 20.73 | 0.0 | 10.0 | 5.29 | 18.56 | mheidari-all | 45.206.5.122 |
| 72.7 | shadowsocks | 275.5 | 639.1 | 21.4 | 0.0 | 10.0 | 12.52 | 15.8 | Au1rxx-base64 | 156.146.38.170 |
| 72.12 | shadowsocks | 277.8 | 640.5 | 21.35 | 0.0 | 10.0 | 12.52 | 15.8 | Au1rxx-base64 | 156.146.38.168 |
| 71.75 | shadowsocks | 229.6 | 600.7 | 22.46 | 0.0 | 10.0 | 12.52 | 15.8 | Au1rxx-base64 | 198.98.53.130 |
| 71.55 | shadowsocks | 239.8 | 637.1 | 22.23 | 0.0 | 10.0 | 12.52 | 15.8 | Au1rxx-base64 | 37.19.198.236 |
| 71.06 | vless | 281.4 | 558.2 | 21.26 | 0.0 | 10.0 | 5.29 | 18.56 | mheidari-all | 86.109.75.147 |
| 71.06 | hysteria2 | 367.4 | 735.1 | 19.27 | 0.0 | 10.0 | 12.5 | 15.8 | Au1rxx-base64 | 62.210.124.146 |
| 71.05 | trojan | 371.0 | 692.8 | 19.19 | 0.0 | 10.0 | 12.23 | 18.56 | mheidari-all | 91.107.145.13 |
| 70.23 | trojan | 410.6 | 776.7 | 18.27 | 0.0 | 10.0 | 12.23 | 18.56 | mheidari-all | 34.249.41.208 |
| 69.96 | trojan | 410.1 | 786.5 | 18.28 | 0.0 | 10.0 | 12.23 | 18.56 | mheidari-all | 108.131.197.101 |
| 69.65 | trojan | 488.5 | 1241.1 | 16.47 | 0.0 | 10.0 | 12.23 | 15.8 | Au1rxx-base64 | 148.72.168.35 |
| 69.44 | hysteria2 | 433.9 | 866.3 | 17.73 | 0.0 | 10.0 | 12.5 | 15.8 | Au1rxx-base64 | 5.255.102.165 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.976 | 1.0 | 36 | 61 | prefer |
| mheidari-all | 0.718 | 0.639 | 523 | 19362 | prefer |
| Au1rxx-base64 | 0.713 | 0.698 | 182 | 432 | prefer |
| DeltaKronecker-all | 0.638 | 0.561 | 41 | 5572 | observe |
| Surfboard-tg-mixed | 0.587 | 0.507 | 150 | 5429 | observe |
| xiaoji235-airport-v2ray-all | 0.287 | 0.5 | 2 | 4399 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4757 | observe |
| Epodonios-all | 0.255 | None | 0 | 6563 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3966 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6800 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4227 | observe |
| barry-far-vless | 0.255 | None | 0 | 4890 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4971 | observe |
| nscl5-all | 0.255 | None | 0 | 2435 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 119 |
| speed | ClientOSError | - | 92 |
| cn-block | TimeoutError | - | 61 |
| 204 | TimeoutError | - | 18 |
| geo | ClientOSError | - | 12 |
| speed | TimeoutError | - | 11 |
| cn-block | ProxyError | - | 7 |
| 204 | ProxyError | - | 7 |
| cn-block | ClientOSError | - | 5 |
| 204 | ClientOSError | - | 4 |
| speed | ProxyError | - | 1 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
