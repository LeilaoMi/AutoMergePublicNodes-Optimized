# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-09 05:50:23 |
| 运行耗时 | 1036.9s |
| 订阅源总数 | 107 |
| 健康订阅源 | 94 |
| 原始节点 | 98042 |
| 去重后节点 | 27766 |
| TCP 可达 | 3000 |
| 真实可用 | 495 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 27766 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.6 |
| geo | 1.5 |
| tcp | 47.2 |
| probe | 344.6 |
| real_test | 558.2 |
| generate | 80.8 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 57654 |
| vmess | 15603 |
| shadowsocks | 12057 |
| trojan | 10510 |
| hysteria2 | 1414 |
| http | 480 |
| shadowsocksr | 174 |
| socks | 90 |
| anytls | 31 |
| hysteria | 17 |
| tuic | 12 |

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
| 83.23 | hysteria2 | 285.7 | 725.1 | 21.16 | 0.0 | 10.0 | 14.25 | 19.32 | Au1rxx-base64 | 129.213.91.185 |
| 81.86 | hysteria2 | 288.9 | 593.7 | 21.09 | 0.0 | 10.0 | 14.25 | 19.32 | Au1rxx-base64 | 66.94.121.46 |
| 81.85 | shadowsocks | 240.9 | 597.6 | 22.2 | 0.0 | 10.0 | 14.33 | 19.32 | Au1rxx-base64 | 156.146.38.169 |
| 81.79 | shadowsocks | 243.5 | 627.5 | 22.14 | 0.0 | 10.0 | 14.33 | 19.32 | Au1rxx-base64 | 156.146.38.170 |
| 81.48 | shadowsocks | 257.1 | 637.9 | 21.83 | 0.0 | 10.0 | 14.33 | 19.32 | Au1rxx-base64 | 156.146.38.168 |
| 80.9 | shadowsocks | 238.8 | 604.3 | 22.25 | 0.0 | 10.0 | 14.33 | 19.32 | Au1rxx-base64 | 156.146.38.167 |
| 79.56 | hysteria2 | 312.3 | 286.6 | 20.55 | 4.25 | 9.02 | 14.25 | 19.32 | Au1rxx-base64 | open.2ml.bid |
| 79.55 | vless | 317.1 | 749.9 | 20.44 | 0.0 | 10.0 | 12.04 | 19.32 | Au1rxx-base64 | 159.89.87.21 |
| 79.51 | shadowsocks | 305.0 | 750.1 | 20.72 | 0.0 | 10.0 | 14.33 | 19.32 | Au1rxx-base64 | 37.19.198.160 |
| 79.5 | shadowsocks | 308.4 | 739.0 | 20.64 | 0.0 | 10.0 | 14.33 | 19.32 | Au1rxx-base64 | 37.19.198.236 |
| 78.34 | vless | 272.9 | 556.1 | 21.46 | 0.0 | 10.0 | 12.04 | 19.32 | Au1rxx-base64 | 47.251.108.158 |
| 78.19 | hysteria2 | 321.7 | 330.9 | 20.33 | 2.59 | 9.52 | 14.25 | 19.32 | Au1rxx-base64 | 158.101.148.79 |
| 77.95 | vless | 349.3 | 756.1 | 19.69 | 0.0 | 10.0 | 12.04 | 19.32 | Au1rxx-base64 | 66.70.179.198 |
| 77.77 | vless | 404.8 | 1010.5 | 18.41 | 0.0 | 10.0 | 12.04 | 19.32 | Au1rxx-base64 | 185.95.231.156 |
| 77.6 | vless | 335.2 | 725.0 | 20.02 | 0.0 | 10.0 | 12.04 | 19.32 | Au1rxx-base64 | 144.202.126.147 |
| 77.51 | vless | 295.9 | 613.3 | 20.93 | 0.0 | 10.0 | 12.04 | 19.32 | Au1rxx-base64 | 107.173.237.146 |
| 76.78 | vless | 402.0 | 950.6 | 18.47 | 0.0 | 10.0 | 12.04 | 19.32 | Au1rxx-base64 | 2.24.124.64 |
| 76.74 | shadowsocks | 337.5 | 796.7 | 19.96 | 0.0 | 10.0 | 14.33 | 19.32 | Au1rxx-base64 | 15.204.246.132 |
| 76.66 | vless | 427.8 | 988.3 | 17.88 | 0.0 | 10.0 | 12.04 | 19.32 | Au1rxx-base64 | 169.40.42.133 |
| 76.45 | shadowsocks | 409.4 | 1127.9 | 18.3 | 0.0 | 10.0 | 14.33 | 19.32 | Au1rxx-base64 | 66.23.204.214 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.982 | 0.914 | 370 | 1763 | prefer |
| DeltaKronecker-all | 0.78 | 0.714 | 28 | 5197 | prefer |
| ermaozi-get_subscribe | 0.642 | 0.623 | 53 | 607 | observe |
| zhangkai | 0.555 | 1.0 | 8 | 144 | observe |
| Au1rxx-clash | 0.325 | 1.0 | 1 | 1761 | observe |
| mheidari-all | 0.323 | 0.242 | 372 | 23125 | observe |
| Surfboard-tg-mixed | 0.305 | 0.3 | 10 | 7069 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| tg-OutlineReleasedKey | 0.257 | 1.0 | 1 | 50 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5081 | observe |
| Epodonios-all | 0.255 | None | 0 | 7569 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3996 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9901 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5581 | observe |
| barry-far-vless | 0.255 | None | 0 | 5823 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 158 |
| speed | TimeoutError | - | 64 |
| 204 | ProxyError | - | 33 |
| geo | ClientOSError | - | 30 |
| speed | ClientOSError | - | 28 |
| cn-block | TimeoutError | - | 16 |
| 204 | TimeoutError | - | 15 |
| cn-block | ClientOSError | - | 4 |
| 204 | ClientOSError | - | 2 |
| cn-block | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
