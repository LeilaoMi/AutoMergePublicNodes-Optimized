# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-24 14:01:41 |
| 运行耗时 | 341.0s |
| 订阅源总数 | 107 |
| 健康订阅源 | 102 |
| 原始节点 | 82875 |
| 去重后节点 | 22678 |
| TCP 可达 | 3000 |
| 真实可用 | 775 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22678 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.3 |
| geo | 1.3 |
| tcp | 32.5 |
| probe | 68.9 |
| real_test | 193.1 |
| generate | 39.9 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 46945 |
| trojan | 15334 |
| vmess | 10140 |
| shadowsocks | 9847 |
| hysteria2 | 404 |
| shadowsocksr | 69 |
| socks | 59 |
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
| 80.51 | shadowsocks | 211.2 | 568.1 | 22.89 | 0.0 | 10.0 | 13.44 | 18.18 | Au1rxx-base64 | 149.22.95.183 |
| 77.07 | trojan | 309.3 | 316.0 | 20.62 | 3.15 | 10.0 | 13.98 | 19.2 | mheidari-all | 95.85.94.90 |
| 76.31 | trojan | 305.1 | 316.4 | 20.72 | 3.13 | 10.0 | 13.98 | 19.2 | mheidari-all | 31.223.184.43 |
| 76.31 | trojan | 306.1 | 314.8 | 20.69 | 3.2 | 10.0 | 13.98 | 19.2 | mheidari-all | 31.223.184.238 |
| 75.95 | trojan | 308.2 | 322.6 | 20.64 | 2.9 | 10.0 | 13.98 | 19.2 | mheidari-all | 95.85.94.165 |
| 75.83 | vless | 210.7 | 478.3 | 22.9 | 0.0 | 10.0 | 4.73 | 19.2 | mheidari-all | 104.16.9.20 |
| 75.29 | trojan | 322.1 | 358.0 | 20.32 | 1.58 | 10.0 | 13.98 | 19.2 | mheidari-all | 95.85.94.199 |
| 75.22 | shadowsocks | 310.9 | 690.5 | 20.58 | 0.0 | 10.0 | 13.44 | 18.18 | Au1rxx-base64 | 108.181.0.177 |
| 74.57 | trojan | 327.9 | 375.7 | 20.19 | 0.91 | 10.0 | 13.98 | 19.2 | mheidari-all | 95.85.94.148 |
| 74.5 | shadowsocks | 257.6 | 267.1 | 21.81 | 4.98 | 10.0 | 13.44 | 18.18 | Au1rxx-base64 | 149.22.87.241 |
| 74.31 | trojan | 305.2 | 315.4 | 20.71 | 3.17 | 10.0 | 13.98 | 19.2 | mheidari-all | 95.85.94.112 |
| 73.76 | shadowsocks | 310.4 | 648.1 | 20.59 | 0.0 | 10.0 | 13.44 | 18.18 | Au1rxx-base64 | 156.146.38.170 |
| 73.54 | trojan | 389.9 | 830.7 | 18.75 | 0.0 | 10.0 | 13.98 | 19.2 | mheidari-all | 163.245.196.68 |
| 73.51 | trojan | 327.0 | 378.1 | 20.21 | 0.82 | 10.0 | 13.98 | 19.2 | mheidari-all | 31.223.184.125 |
| 72.85 | shadowsocks | 349.0 | 761.3 | 19.7 | 0.0 | 10.0 | 13.44 | 18.18 | Au1rxx-base64 | 156.146.38.167 |
| 72.82 | trojan | 355.1 | 742.7 | 19.56 | 0.0 | 10.0 | 13.98 | 18.18 | Au1rxx-base64 | 64.94.95.118 |
| 71.78 | trojan | 365.1 | 494.3 | 19.33 | 0.0 | 10.0 | 13.98 | 19.2 | mheidari-all | 31.223.184.164 |
| 71.5 | trojan | 429.5 | 829.0 | 17.84 | 0.0 | 10.0 | 13.98 | 19.2 | mheidari-all | 153.75.250.171 |
| 71.46 | trojan | 330.7 | 375.4 | 20.12 | 0.92 | 10.0 | 13.98 | 19.2 | mheidari-all | 31.223.184.109 |
| 71.32 | shadowsocks | 307.6 | 416.3 | 20.66 | 0.0 | 10.0 | 13.44 | 18.18 | Au1rxx-base64 | 149.22.87.204 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.975 | 1.0 | 35 | 61 | prefer |
| Au1rxx-base64 | 0.869 | 0.857 | 119 | 432 | prefer |
| mheidari-all | 0.822 | 0.743 | 684 | 19570 | prefer |
| DeltaKronecker-all | 0.815 | 0.739 | 134 | 5559 | prefer |
| Surfboard-tg-mixed | 0.794 | 0.725 | 40 | 5218 | prefer |
| xiaoji235-airport-v2ray-all | 0.391 | 1.0 | 2 | 3847 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4588 | observe |
| Epodonios-all | 0.255 | None | 0 | 6424 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3975 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6965 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4143 | observe |
| barry-far-vless | 0.255 | None | 0 | 4809 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5027 | observe |
| nscl5-all | 0.255 | None | 0 | 3124 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 71 |
| speed | ClientOSError | - | 46 |
| cn-block | TimeoutError | - | 31 |
| 204 | TimeoutError | - | 26 |
| 204 | ProxyError | - | 19 |
| geo | ClientOSError | - | 17 |
| speed | TimeoutError | - | 9 |
| 204 | ClientOSError | - | 6 |
| cn-block | ProxyError | - | 5 |
| cn-block | ClientOSError | - | 4 |
| geo | ProxyError | - | 3 |
| speed | ProxyError | - | 3 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
