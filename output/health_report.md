# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-02 08:35:47 |
| 运行耗时 | 292.2s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 77331 |
| 去重后节点 | 22731 |
| TCP 可达 | 3000 |
| 真实可用 | 695 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22731 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.0 |
| geo | 1.4 |
| tcp | 34.6 |
| probe | 60.8 |
| real_test | 153.0 |
| generate | 36.4 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 45684 |
| vmess | 12301 |
| shadowsocks | 10258 |
| trojan | 8116 |
| hysteria2 | 611 |
| http | 165 |
| socks | 77 |
| shadowsocksr | 72 |
| anytls | 26 |
| hysteria | 14 |
| tuic | 7 |

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
| 85.35 | http | 187.1 | 483.5 | 23.45 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.204 |
| 85.32 | http | 188.1 | 478.7 | 23.42 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.202 |
| 85.29 | http | 189.7 | 494.1 | 23.39 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.206 |
| 85.27 | http | 190.4 | 493.6 | 23.37 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.217 |
| 85.23 | http | 192.1 | 477.6 | 23.33 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.197 |
| 85.17 | http | 194.6 | 494.1 | 23.27 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.215 |
| 85.16 | http | 195.4 | 493.5 | 23.26 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.208 |
| 85.06 | http | 199.4 | 492.0 | 23.16 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.195 |
| 85.04 | http | 200.2 | 496.7 | 23.14 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.207 |
| 85.0 | http | 201.9 | 501.1 | 23.1 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.216 |
| 84.99 | http | 202.6 | 511.1 | 23.09 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.200 |
| 84.97 | http | 203.4 | 506.6 | 23.07 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.205 |
| 84.97 | http | 203.5 | 499.2 | 23.07 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.198 |
| 84.96 | http | 203.6 | 506.8 | 23.06 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.218 |
| 84.96 | http | 204.0 | 508.5 | 23.06 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.210 |
| 84.95 | http | 204.1 | 510.4 | 23.05 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.220 |
| 84.95 | http | 204.2 | 489.3 | 23.05 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.214 |
| 84.92 | http | 205.5 | 509.4 | 23.02 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.211 |
| 84.87 | http | 207.9 | 530.5 | 22.97 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.209 |
| 84.86 | http | 208.0 | 509.4 | 22.96 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.212 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.996 | 0.986 | 219 | 344 | prefer |
| Au1rxx-base64 | 0.802 | 0.739 | 524 | 1604 | prefer |
| Surfboard-tg-mixed | 0.678 | 0.6 | 115 | 5167 | observe |
| DeltaKronecker-all | 0.48 | 0.395 | 43 | 4549 | observe |
| Epodonios-all | 0.335 | 1.0 | 1 | 5764 | observe |
| xiaoji235-airport-v2ray-all | 0.329 | 1.0 | 1 | 1861 | observe |
| roosterkid-openproxylist-v2ray | 0.261 | 1.0 | 1 | 150 | observe |
| chromego_merge | 0.258 | 1.0 | 1 | 70 | observe |
| tg-OutlineReleasedKey | 0.257 | 1.0 | 1 | 57 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3969 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6688 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 3990 | observe |
| barry-far-vless | 0.255 | None | 0 | 4406 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5071 | observe |
| Au1rxx-clash | 0.239 | None | 0 | 1604 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 66 |
| speed | TimeoutError | - | 55 |
| 204 | TimeoutError | - | 28 |
| cn-block | TimeoutError | - | 18 |
| speed | ClientOSError | - | 14 |
| geo | ClientOSError | - | 14 |
| 204 | ProxyError | - | 12 |
| 204 | ClientOSError | - | 8 |
| cn-block | ClientOSError | - | 5 |
| cn-block | ProxyError | - | 2 |
| sing-box exited 1 |  [31mFATAL[0m[0000] start service: start inbound/socks[socks-in]: listen tcp 127.0.0.1:49596: bind: address already in use | - | 1 |
| geo | parse | TimeoutError | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
