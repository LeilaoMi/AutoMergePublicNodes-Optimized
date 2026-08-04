# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-04 14:32:52 |
| 运行耗时 | 265.4s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 86444 |
| 去重后节点 | 24261 |
| TCP 可达 | 3000 |
| 真实可用 | 548 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 24261 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.8 |
| geo | 1.3 |
| tcp | 36.8 |
| probe | 60.6 |
| real_test | 128.2 |
| generate | 32.7 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 52797 |
| vmess | 12971 |
| shadowsocks | 10050 |
| trojan | 9369 |
| hysteria2 | 1008 |
| socks | 79 |
| shadowsocksr | 68 |
| http | 63 |
| hysteria | 19 |
| tuic | 10 |
| anytls | 10 |

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
| 80.07 | http | 400.4 | 1097.7 | 18.51 | 0.0 | 10.0 | 14.78 | 19.78 | zhangkai | 138.199.35.213 |
| 79.74 | http | 414.7 | 1162.6 | 18.18 | 0.0 | 10.0 | 14.78 | 19.78 | zhangkai | 138.199.35.200 |
| 79.64 | http | 419.1 | 1171.7 | 18.08 | 0.0 | 10.0 | 14.78 | 19.78 | zhangkai | 138.199.35.217 |
| 79.59 | http | 421.2 | 1183.6 | 18.03 | 0.0 | 10.0 | 14.78 | 19.78 | zhangkai | 138.199.35.214 |
| 79.5 | http | 425.1 | 1196.2 | 17.94 | 0.0 | 10.0 | 14.78 | 19.78 | zhangkai | 138.199.35.198 |
| 79.45 | http | 427.3 | 1195.3 | 17.89 | 0.0 | 10.0 | 14.78 | 19.78 | zhangkai | 138.199.35.219 |
| 78.96 | hysteria2 | 241.7 | 268.6 | 22.18 | 4.93 | 9.87 | 12.86 | 16.2 | Au1rxx-base64 | 45.76.202.45 |
| 78.29 | http | 477.2 | 1345.9 | 16.73 | 0.0 | 10.0 | 14.78 | 19.78 | zhangkai | 138.199.35.207 |
| 78.02 | http | 489.1 | 1369.6 | 16.46 | 0.0 | 10.0 | 14.78 | 19.78 | zhangkai | 138.199.35.199 |
| 77.75 | shadowsocks | 209.3 | 494.3 | 22.93 | 0.0 | 10.0 | 12.62 | 16.2 | Au1rxx-base64 | 173.244.56.9 |
| 77.45 | shadowsocks | 200.7 | 489.4 | 23.13 | 0.0 | 10.0 | 12.62 | 16.2 | Au1rxx-base64 | 108.181.0.177 |
| 77.22 | shadowsocks | 210.9 | 495.9 | 22.9 | 0.0 | 10.0 | 12.62 | 16.2 | Au1rxx-base64 | 108.181.118.10 |
| 76.99 | shadowsocks | 203.5 | 509.0 | 23.07 | 0.0 | 10.0 | 12.62 | 16.2 | Au1rxx-base64 | 173.244.56.6 |
| 76.64 | shadowsocks | 252.3 | 612.7 | 21.94 | 0.0 | 10.0 | 12.62 | 16.2 | Au1rxx-base64 | 156.146.38.167 |
| 76.21 | shadowsocks | 260.2 | 624.0 | 21.76 | 0.0 | 10.0 | 12.62 | 16.2 | Au1rxx-base64 | 156.146.38.168 |
| 75.59 | vless | 256.6 | 634.9 | 21.84 | 0.0 | 10.0 | 7.55 | 16.2 | Au1rxx-base64 | 192.204.50.220 |
| 74.91 | shadowsocks | 255.9 | 617.0 | 21.86 | 0.0 | 10.0 | 12.62 | 16.2 | Au1rxx-base64 | 156.146.38.169 |
| 74.83 | vless | 222.9 | 522.5 | 22.62 | 0.0 | 10.0 | 7.55 | 16.2 | Au1rxx-base64 | 69.46.46.13 |
| 74.6 | vless | 215.5 | 536.4 | 22.79 | 0.0 | 10.0 | 7.55 | 16.2 | Au1rxx-base64 | 172.247.109.66 |
| 74.19 | hysteria2 | 349.5 | 760.8 | 19.69 | 0.0 | 10.0 | 12.86 | 16.2 | Au1rxx-base64 | 138.124.68.188 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.984 | 1.0 | 52 | 72 | prefer |
| Au1rxx-base64 | 0.913 | 0.847 | 471 | 1684 | prefer |
| DeltaKronecker-all | 0.7 | 0.622 | 119 | 5788 | observe |
| mheidari-all | 0.633 | 0.579 | 19 | 20302 | observe |
| Surfboard-tg-mixed | 0.622 | 0.667 | 15 | 5397 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| tg-OutlineReleasedKey | 0.257 | 1.0 | 1 | 58 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5251 | observe |
| Epodonios-all | 0.255 | None | 0 | 5995 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3996 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7036 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4315 | observe |
| barry-far-vless | 0.255 | None | 0 | 4658 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5110 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | TimeoutError | - | 32 |
| geo | ClientOSError | - | 21 |
| 204 | ProxyError | - | 16 |
| geo | TimeoutError | - | 11 |
| speed | TimeoutError | - | 11 |
| cn-block | TimeoutError | - | 11 |
| speed | ClientOSError | - | 10 |
| 204 | ClientOSError | - | 7 |
| cn-block | ProxyError | - | 5 |
| cn-block | ClientOSError | - | 3 |
| sing-box exited 1 |  [31mFATAL[0m[0000] start service: start inbound/socks[socks-in]: listen tcp 127.0.0.1:42803: bind: address already in use | - | 1 |
| speed | ClientPayloadError | - | 1 |
| geo | ProxyError | - | 1 |
| sing-box exited 1 |  [31mFATAL[0m[0000] start service: start inbound/socks[socks-in]: listen tcp 127.0.0.1:36461: bind: address already in use | - | 1 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
