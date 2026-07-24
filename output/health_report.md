# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-24 19:42:28 |
| 运行耗时 | 307.9s |
| 订阅源总数 | 107 |
| 健康订阅源 | 102 |
| 原始节点 | 83183 |
| 去重后节点 | 22837 |
| TCP 可达 | 3000 |
| 真实可用 | 708 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22837 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.3 |
| geo | 1.3 |
| tcp | 33.1 |
| probe | 66.6 |
| real_test | 162.0 |
| generate | 39.6 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 47164 |
| trojan | 15150 |
| vmess | 10276 |
| shadowsocks | 9965 |
| hysteria2 | 396 |
| socks | 79 |
| shadowsocksr | 76 |
| http | 51 |
| hysteria | 15 |
| tuic | 9 |
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
| 74.64 | vless | 220.1 | 486.2 | 22.68 | 0.0 | 10.0 | 6.52 | 16.44 | mheidari-all | 104.16.9.20 |
| 74.55 | vless | 218.2 | 472.0 | 22.73 | 0.0 | 10.0 | 6.52 | 16.3 | DeltaKronecker-all | 104.25.161.29 |
| 74.12 | vless | 217.3 | 486.4 | 22.75 | 0.0 | 10.0 | 6.52 | 16.44 | mheidari-all | 198.41.209.87 |
| 74.09 | trojan | 306.5 | 315.7 | 20.68 | 3.16 | 10.0 | 13.51 | 16.44 | mheidari-all | 31.223.184.82 |
| 74.02 | shadowsocks | 257.8 | 273.6 | 21.81 | 4.74 | 10.0 | 12.96 | 17.38 | Au1rxx-base64 | 149.22.87.241 |
| 73.89 | trojan | 307.1 | 321.2 | 20.67 | 2.95 | 10.0 | 13.51 | 16.44 | mheidari-all | 31.223.184.238 |
| 73.72 | shadowsocks | 306.7 | 685.2 | 20.68 | 0.0 | 10.0 | 12.96 | 17.38 | Au1rxx-base64 | 108.181.0.177 |
| 73.67 | trojan | 305.3 | 318.4 | 20.71 | 3.06 | 10.0 | 13.51 | 16.44 | mheidari-all | 31.223.184.149 |
| 72.27 | trojan | 305.6 | 312.8 | 20.7 | 3.27 | 10.0 | 13.51 | 16.44 | mheidari-all | 95.85.94.112 |
| 72.15 | trojan | 305.5 | 315.6 | 20.71 | 3.17 | 10.0 | 13.51 | 16.44 | mheidari-all | 95.85.94.17 |
| 71.99 | trojan | 307.3 | 316.5 | 20.66 | 3.13 | 10.0 | 13.51 | 16.44 | mheidari-all | 31.223.184.109 |
| 71.58 | shadowsocks | 324.2 | 696.7 | 20.27 | 0.0 | 10.0 | 12.96 | 17.38 | Au1rxx-base64 | 156.146.38.170 |
| 71.49 | trojan | 326.3 | 373.6 | 20.23 | 0.99 | 10.0 | 13.51 | 16.44 | mheidari-all | 95.85.94.199 |
| 71.16 | trojan | 327.3 | 381.1 | 20.2 | 0.71 | 10.0 | 13.51 | 16.44 | mheidari-all | 31.223.184.125 |
| 71.16 | trojan | 328.1 | 381.4 | 20.18 | 0.7 | 10.0 | 13.51 | 16.44 | mheidari-all | 31.223.184.164 |
| 71.15 | trojan | 303.7 | 311.9 | 20.75 | 3.3 | 10.0 | 13.51 | 16.3 | DeltaKronecker-all | 31.223.184.172 |
| 71.13 | trojan | 304.8 | 312.7 | 20.72 | 3.27 | 10.0 | 13.51 | 16.3 | DeltaKronecker-all | 95.85.94.185 |
| 71.04 | trojan | 327.2 | 383.2 | 20.2 | 0.63 | 10.0 | 13.51 | 16.44 | mheidari-all | 95.85.94.148 |
| 71.01 | shadowsocks | 369.8 | 824.9 | 19.22 | 0.0 | 10.0 | 12.96 | 17.38 | Au1rxx-base64 | 172.245.235.84 |
| 70.92 | trojan | 308.6 | 314.6 | 20.64 | 3.2 | 10.0 | 13.51 | 16.3 | DeltaKronecker-all | 31.223.184.58 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.976 | 1.0 | 36 | 61 | prefer |
| Surfboard-tg-mixed | 0.854 | 0.779 | 104 | 5475 | prefer |
| Au1rxx-base64 | 0.835 | 0.824 | 119 | 432 | prefer |
| mheidari-all | 0.809 | 0.73 | 596 | 19355 | prefer |
| DeltaKronecker-all | 0.603 | 0.524 | 105 | 5559 | observe |
| xiaoji235-airport-v2ray-all | 0.391 | 1.0 | 2 | 3847 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4588 | observe |
| Epodonios-all | 0.255 | None | 0 | 6668 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3967 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6766 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4271 | observe |
| barry-far-vless | 0.255 | None | 0 | 4905 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5027 | observe |
| nscl5-all | 0.255 | None | 0 | 3124 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 69 |
| geo | TimeoutError | - | 65 |
| cn-block | TimeoutError | - | 32 |
| 204 | TimeoutError | - | 29 |
| 204 | ProxyError | - | 17 |
| geo | ClientOSError | - | 11 |
| cn-block | ProxyError | - | 10 |
| cn-block | ClientOSError | - | 10 |
| speed | TimeoutError | - | 8 |
| 204 | ClientOSError | - | 4 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
