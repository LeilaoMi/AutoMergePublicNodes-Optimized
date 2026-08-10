# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-10 07:54:28 |
| 运行耗时 | 233.9s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 87298 |
| 去重后节点 | 24723 |
| TCP 可达 | 3000 |
| 真实可用 | 470 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 24723 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.7 |
| geo | 1.3 |
| tcp | 35.8 |
| probe | 55.4 |
| real_test | 109.6 |
| generate | 27.2 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 52276 |
| vmess | 13132 |
| trojan | 10533 |
| shadowsocks | 9724 |
| hysteria2 | 1405 |
| shadowsocksr | 73 |
| socks | 68 |
| http | 40 |
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
| 83.92 | http | 190.1 | 489.5 | 23.38 | 0.0 | 10.0 | 14.42 | 19.12 | zhangkai | 138.199.35.207 |
| 83.84 | http | 193.4 | 501.8 | 23.3 | 0.0 | 10.0 | 14.42 | 19.12 | zhangkai | 138.199.35.214 |
| 83.74 | http | 197.6 | 518.3 | 23.2 | 0.0 | 10.0 | 14.42 | 19.12 | zhangkai | 138.199.35.217 |
| 82.79 | http | 238.7 | 633.0 | 22.25 | 0.0 | 10.0 | 14.42 | 19.12 | zhangkai | 138.199.35.199 |
| 82.43 | shadowsocks | 190.1 | 460.0 | 23.38 | 0.0 | 10.0 | 14.35 | 19.2 | Au1rxx-base64 | 108.181.0.177 |
| 82.37 | shadowsocks | 192.5 | 461.6 | 23.32 | 0.0 | 10.0 | 14.35 | 19.2 | Au1rxx-base64 | 108.181.118.10 |
| 81.54 | shadowsocks | 250.0 | 608.1 | 21.99 | 0.0 | 10.0 | 14.35 | 19.2 | Au1rxx-base64 | 156.146.38.170 |
| 81.52 | shadowsocks | 250.8 | 616.3 | 21.97 | 0.0 | 10.0 | 14.35 | 19.2 | Au1rxx-base64 | 156.146.38.167 |
| 81.43 | shadowsocks | 254.9 | 623.7 | 21.88 | 0.0 | 10.0 | 14.35 | 19.2 | Au1rxx-base64 | 156.146.38.168 |
| 81.35 | shadowsocks | 258.1 | 626.4 | 21.8 | 0.0 | 10.0 | 14.35 | 19.2 | Au1rxx-base64 | 173.244.56.6 |
| 81.27 | shadowsocks | 261.7 | 635.2 | 21.72 | 0.0 | 10.0 | 14.35 | 19.2 | Au1rxx-base64 | 156.146.38.169 |
| 79.38 | shadowsocks | 256.8 | 679.5 | 21.83 | 0.0 | 10.0 | 14.35 | 19.2 | Au1rxx-base64 | 173.244.56.9 |
| 78.63 | vless | 187.9 | 484.1 | 23.43 | 0.0 | 10.0 | 6.0 | 19.2 | Au1rxx-base64 | 179.253.240.24 |
| 78.6 | vless | 187.5 | 477.0 | 23.44 | 0.0 | 9.96 | 6.0 | 19.2 | Au1rxx-base64 | 179.255.148.66 |
| 78.29 | vless | 202.6 | 530.7 | 23.09 | 0.0 | 10.0 | 6.0 | 19.2 | Au1rxx-base64 | 167.17.68.205 |
| 78.27 | trojan | 278.5 | 574.6 | 21.33 | 0.0 | 10.0 | 13.56 | 19.2 | Au1rxx-base64 | 44.244.3.114 |
| 78.16 | vless | 208.3 | 493.6 | 22.96 | 0.0 | 10.0 | 6.0 | 19.2 | Au1rxx-base64 | 186.241.106.97 |
| 77.72 | shadowsocks | 274.3 | 572.7 | 21.43 | 0.0 | 10.0 | 14.35 | 19.2 | Au1rxx-base64 | 149.22.95.183 |
| 77.43 | vless | 237.5 | 627.9 | 22.28 | 0.0 | 9.95 | 6.0 | 19.2 | Au1rxx-base64 | 70.39.198.183 |
| 77.05 | hysteria2 | 356.4 | 771.9 | 19.53 | 0.0 | 9.99 | 12.69 | 19.2 | Au1rxx-base64 | 138.124.68.188 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.956 | 1.0 | 20 | 25 | prefer |
| Au1rxx-base64 | 0.908 | 0.839 | 436 | 1742 | prefer |
| Surfboard-tg-mixed | 0.733 | 0.657 | 99 | 6647 | prefer |
| DeltaKronecker-all | 0.424 | 0.333 | 30 | 5881 | observe |
| mheidari-all | 0.413 | 0.32 | 25 | 20373 | observe |
| nscl5-all | 0.313 | 1.0 | 1 | 1442 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5327 | observe |
| Epodonios-all | 0.255 | None | 0 | 7338 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3994 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7807 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5394 | observe |
| barry-far-vless | 0.255 | None | 0 | 5713 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5191 | observe |
| Au1rxx-clash | 0.245 | None | 0 | 1742 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | TimeoutError | - | 40 |
| geo | TimeoutError | - | 28 |
| 204 | TimeoutError | - | 14 |
| cn-block | TimeoutError | - | 14 |
| speed | ClientOSError | - | 13 |
| 204 | ProxyError | - | 13 |
| geo | ClientOSError | - | 12 |
| 204 | ClientOSError | - | 6 |
| cn-block | ClientOSError | - | 3 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
