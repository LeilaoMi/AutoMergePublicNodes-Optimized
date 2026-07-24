# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-24 03:24:22 |
| 运行耗时 | 350.3s |
| 订阅源总数 | 107 |
| 健康订阅源 | 102 |
| 原始节点 | 83696 |
| 去重后节点 | 23126 |
| TCP 可达 | 3000 |
| 真实可用 | 859 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23126 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.2 |
| geo | 1.4 |
| tcp | 32.2 |
| probe | 64.4 |
| real_test | 211.0 |
| generate | 36.1 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 47325 |
| trojan | 15495 |
| shadowsocks | 10143 |
| vmess | 10125 |
| hysteria2 | 401 |
| shadowsocksr | 77 |
| socks | 58 |
| http | 51 |
| hysteria | 15 |
| tuic | 4 |
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
| 74.58 | shadowsocks | 252.2 | 626.9 | 21.94 | 0.0 | 10.0 | 12.38 | 14.26 | Au1rxx-base64 | 198.98.53.130 |
| 74.57 | shadowsocks | 252.8 | 610.8 | 21.93 | 0.0 | 10.0 | 12.38 | 14.26 | Au1rxx-base64 | 156.146.38.170 |
| 74.47 | shadowsocks | 257.0 | 630.5 | 21.83 | 0.0 | 10.0 | 12.38 | 14.26 | Au1rxx-base64 | 156.146.38.167 |
| 74.39 | shadowsocks | 260.3 | 637.6 | 21.75 | 0.0 | 10.0 | 12.38 | 14.26 | Au1rxx-base64 | 156.146.38.168 |
| 74.14 | shadowsocks | 271.2 | 662.1 | 21.5 | 0.0 | 10.0 | 12.38 | 14.26 | Au1rxx-base64 | 37.19.198.243 |
| 73.37 | shadowsocks | 282.7 | 704.7 | 21.23 | 0.0 | 10.0 | 12.38 | 14.26 | Au1rxx-base64 | 37.19.198.244 |
| 72.33 | shadowsocks | 327.8 | 840.6 | 20.19 | 0.0 | 10.0 | 12.38 | 14.26 | Au1rxx-base64 | 185.196.61.82 |
| 71.87 | shadowsocks | 282.7 | 709.1 | 21.23 | 0.0 | 10.0 | 12.38 | 14.26 | Au1rxx-base64 | 37.19.198.160 |
| 71.79 | vless | 205.0 | 581.1 | 23.03 | 0.0 | 10.0 | 4.4 | 14.36 | mheidari-all | 154.193.55.183 |
| 71.49 | trojan | 349.8 | 905.2 | 19.68 | 0.0 | 10.0 | 12.73 | 12.76 | DeltaKronecker-all | 64.74.163.118 |
| 71.12 | trojan | 459.8 | 1298.7 | 17.13 | 0.0 | 10.0 | 12.73 | 14.26 | Au1rxx-base64 | 148.72.168.35 |
| 70.29 | trojan | 278.0 | 634.3 | 21.34 | 0.0 | 10.0 | 12.73 | 11.74 | Surfboard-tg-mixed | 163.245.196.68 |
| 70.14 | vless | 276.5 | 680.4 | 21.38 | 0.0 | 10.0 | 4.4 | 14.36 | mheidari-all | 47.89.186.170 |
| 69.19 | shadowsocks | 283.0 | 572.1 | 21.23 | 0.0 | 10.0 | 12.38 | 14.26 | Au1rxx-base64 | 173.244.56.9 |
| 69.15 | trojan | 390.4 | 994.6 | 18.74 | 0.0 | 10.0 | 12.73 | 12.76 | DeltaKronecker-all | 153.75.250.171 |
| 68.89 | shadowsocks | 281.9 | 705.3 | 21.25 | 0.0 | 10.0 | 12.38 | 14.26 | Au1rxx-base64 | 37.19.198.236 |
| 68.86 | shadowsocks | 308.4 | 640.8 | 20.64 | 0.0 | 10.0 | 12.38 | 14.26 | Au1rxx-base64 | 149.22.95.183 |
| 68.77 | shadowsocks | 289.1 | 588.6 | 21.09 | 0.0 | 10.0 | 12.38 | 14.26 | Au1rxx-base64 | 108.181.0.177 |
| 68.32 | vmess | 402.7 | 1088.6 | 18.46 | 0.0 | 10.0 | 10.0 | 14.36 | mheidari-all | 67.220.95.3 |
| 68.08 | trojan | 400.7 | 720.8 | 18.5 | 0.0 | 9.87 | 12.73 | 14.36 | mheidari-all | 91.107.145.13 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.95 | 0.972 | 36 | 61 | prefer |
| Surfboard-tg-mixed | 0.912 | 0.838 | 99 | 5375 | prefer |
| DeltaKronecker-all | 0.822 | 0.745 | 153 | 5572 | prefer |
| Au1rxx-base64 | 0.759 | 0.744 | 199 | 432 | prefer |
| mheidari-all | 0.645 | 0.565 | 840 | 20024 | observe |
| 10ium-HighSpeed | 0.345 | 1.0 | 2 | 839 | observe |
| xiaoji235-airport-v2ray-all | 0.287 | 0.5 | 2 | 3843 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4757 | observe |
| Epodonios-all | 0.255 | None | 0 | 6509 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3976 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6957 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4163 | observe |
| barry-far-vless | 0.255 | None | 0 | 4750 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4971 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 206 |
| cn-block | TimeoutError | - | 71 |
| speed | ClientOSError | - | 61 |
| speed | TimeoutError | - | 44 |
| 204 | ProxyError | - | 38 |
| geo | ClientOSError | - | 37 |
| cn-block | ClientOSError | - | 5 |
| 204 | TimeoutError | - | 3 |
| cn-block | ProxyError | - | 3 |
| speed | ProxyError | - | 3 |
| geo | ProxyError | - | 2 |
| 204 | ClientOSError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
