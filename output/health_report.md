# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-26 13:46:28 |
| 运行耗时 | 314.3s |
| 订阅源总数 | 107 |
| 健康订阅源 | 102 |
| 原始节点 | 81669 |
| 去重后节点 | 22638 |
| TCP 可达 | 3000 |
| 真实可用 | 761 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22638 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.7 |
| geo | 1.3 |
| tcp | 31.4 |
| probe | 65.7 |
| real_test | 172.9 |
| generate | 38.2 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 46077 |
| trojan | 14770 |
| vmess | 10095 |
| shadowsocks | 9964 |
| hysteria2 | 498 |
| http | 84 |
| shadowsocksr | 77 |
| socks | 69 |
| hysteria | 15 |
| anytls | 12 |
| tuic | 8 |

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
| 81.49 | shadowsocks | 192.7 | 510.1 | 23.32 | 0.0 | 10.0 | 13.07 | 19.1 | Au1rxx-base64 | 173.244.56.6 |
| 80.89 | shadowsocks | 196.8 | 511.1 | 23.22 | 0.0 | 10.0 | 13.07 | 19.1 | Au1rxx-base64 | 108.181.118.10 |
| 80.89 | shadowsocks | 196.8 | 479.6 | 23.22 | 0.0 | 10.0 | 13.07 | 19.1 | Au1rxx-base64 | 108.181.0.177 |
| 77.44 | shadowsocks | 281.7 | 642.7 | 21.26 | 0.0 | 10.0 | 13.07 | 19.1 | Au1rxx-base64 | 156.146.38.170 |
| 76.59 | shadowsocks | 285.2 | 653.7 | 21.18 | 0.0 | 10.0 | 13.07 | 19.1 | Au1rxx-base64 | 156.146.38.169 |
| 76.3 | shadowsocks | 283.3 | 286.2 | 21.22 | 4.27 | 9.89 | 13.07 | 19.1 | Au1rxx-base64 | 149.22.87.204 |
| 76.11 | trojan | 378.0 | 898.7 | 19.03 | 0.0 | 10.0 | 13.68 | 19.1 | Au1rxx-base64 | 163.245.196.68 |
| 75.55 | shadowsocks | 336.8 | 816.8 | 19.98 | 0.0 | 10.0 | 13.07 | 19.1 | Au1rxx-base64 | 156.146.38.168 |
| 75.27 | shadowsocks | 296.1 | 650.3 | 20.92 | 0.0 | 10.0 | 13.07 | 19.1 | Au1rxx-base64 | 149.22.95.183 |
| 75.01 | trojan | 336.8 | 338.1 | 19.98 | 2.32 | 9.91 | 13.68 | 19.1 | Au1rxx-base64 | 31.223.184.43 |
| 74.94 | trojan | 337.4 | 336.3 | 19.97 | 2.39 | 9.89 | 13.68 | 19.1 | Au1rxx-base64 | 95.85.94.185 |
| 74.93 | trojan | 337.9 | 339.6 | 19.96 | 2.27 | 9.89 | 13.68 | 19.1 | Au1rxx-base64 | 95.85.94.148 |
| 74.9 | trojan | 336.5 | 340.2 | 19.99 | 2.24 | 9.88 | 13.68 | 19.1 | Au1rxx-base64 | 31.223.184.125 |
| 74.76 | trojan | 341.6 | 339.9 | 19.87 | 2.26 | 9.89 | 13.68 | 19.1 | Au1rxx-base64 | 95.85.94.142 |
| 74.73 | trojan | 341.4 | 342.4 | 19.87 | 2.16 | 9.89 | 13.68 | 19.1 | Au1rxx-base64 | 95.85.94.165 |
| 74.67 | trojan | 372.1 | 321.2 | 19.16 | 2.96 | 9.88 | 13.68 | 19.1 | Au1rxx-base64 | 31.223.184.82 |
| 74.64 | trojan | 340.0 | 342.2 | 19.91 | 2.17 | 9.88 | 13.68 | 19.1 | Au1rxx-base64 | 31.223.184.238 |
| 74.3 | trojan | 340.4 | 351.5 | 19.9 | 1.82 | 9.87 | 13.68 | 19.1 | Au1rxx-base64 | 95.85.94.90 |
| 73.98 | trojan | 427.7 | 307.0 | 17.88 | 3.49 | 9.91 | 13.68 | 19.1 | Au1rxx-base64 | 95.85.94.17 |
| 73.82 | trojan | 340.6 | 339.5 | 19.89 | 2.27 | 9.88 | 13.68 | 19.1 | Au1rxx-base64 | 31.223.184.153 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.99 | 1.0 | 75 | 86 | prefer |
| Au1rxx-base64 | 0.98 | 0.924 | 460 | 1458 | prefer |
| DeltaKronecker-all | 0.81 | 0.733 | 146 | 5950 | prefer |
| Surfboard-tg-mixed | 0.709 | 0.632 | 68 | 5591 | prefer |
| mheidari-all | 0.582 | 0.502 | 205 | 17236 | observe |
| tg-oneclickvpnkeys | 0.519 | 1.0 | 7 | 149 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4912 | observe |
| Epodonios-all | 0.255 | None | 0 | 6731 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3972 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6620 | observe |
| barry-far-vless | 0.255 | None | 0 | 5039 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4980 | observe |
| nscl5-all | 0.255 | None | 0 | 2896 | observe |
| xiaoji235-airport-v2ray-all | 0.24 | None | 0 | 1624 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 73 |
| speed | ClientOSError | - | 43 |
| cn-block | TimeoutError | - | 23 |
| speed | TimeoutError | - | 15 |
| geo | ClientOSError | - | 14 |
| 204 | TimeoutError | - | 14 |
| 204 | ProxyError | - | 7 |
| cn-block | ClientOSError | - | 6 |
| 204 | ClientOSError | - | 6 |
| cn-block | ProxyError | - | 3 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
