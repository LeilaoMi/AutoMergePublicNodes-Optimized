# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-15 01:41:08 |
| 运行耗时 | 381.5s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 75507 |
| 去重后节点 | 20655 |
| TCP 可达 | 3000 |
| 真实可用 | 1182 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 20655 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.5 |
| geo | 0.9 |
| tcp | 32.6 |
| probe | 68.9 |
| real_test | 240.2 |
| generate | 33.4 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 41334 |
| trojan | 11661 |
| vmess | 10502 |
| shadowsocks | 10254 |
| hysteria2 | 1411 |
| http | 180 |
| socks | 78 |
| shadowsocksr | 72 |
| tuic | 8 |
| hysteria | 7 |

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
| 85.24 | http | 190.1 | 494.7 | 23.38 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.209 |
| 85.22 | http | 190.7 | 488.4 | 23.36 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.204 |
| 85.2 | http | 191.6 | 488.5 | 23.34 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.210 |
| 85.17 | http | 193.1 | 502.3 | 23.31 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.208 |
| 85.13 | http | 194.8 | 500.6 | 23.27 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.213 |
| 85.12 | http | 195.0 | 499.5 | 23.26 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.199 |
| 85.11 | http | 195.5 | 501.2 | 23.25 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.197 |
| 85.1 | http | 196.0 | 512.6 | 23.24 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.214 |
| 85.09 | http | 196.5 | 500.0 | 23.23 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.211 |
| 85.06 | http | 197.7 | 502.5 | 23.2 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.220 |
| 85.05 | http | 198.3 | 509.7 | 23.19 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.215 |
| 85.02 | http | 199.3 | 497.6 | 23.16 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.195 |
| 85.01 | http | 200.1 | 510.5 | 23.15 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.212 |
| 84.9 | http | 204.7 | 523.2 | 23.04 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.206 |
| 82.38 | shadowsocks | 210.3 | 517.6 | 22.91 | 0.0 | 10.0 | 13.47 | 20.0 | Au1rxx-base64 | 173.244.56.6 |
| 82.07 | shadowsocks | 202.1 | 455.4 | 23.1 | 0.0 | 10.0 | 13.47 | 20.0 | Au1rxx-base64 | 108.181.118.10 |
| 82.04 | shadowsocks | 203.2 | 484.0 | 23.07 | 0.0 | 10.0 | 13.47 | 20.0 | Au1rxx-base64 | 108.181.0.177 |
| 81.45 | shadowsocks | 250.6 | 608.8 | 21.98 | 0.0 | 10.0 | 13.47 | 20.0 | Au1rxx-base64 | 173.244.56.9 |
| 81.32 | shadowsocks | 256.0 | 587.3 | 21.85 | 0.0 | 10.0 | 13.47 | 20.0 | Au1rxx-base64 | 156.146.38.170 |
| 80.91 | shadowsocks | 256.8 | 594.6 | 21.83 | 0.0 | 10.0 | 13.47 | 20.0 | Au1rxx-base64 | 156.146.38.168 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | 0.981 | 738 | 1681 | prefer |
| zhangkai | 0.999 | 1.0 | 127 | 159 | prefer |
| DeltaKronecker-all | 0.848 | 0.77 | 257 | 3485 | prefer |
| Surfboard-tg-mixed | 0.75 | 0.672 | 183 | 5718 | prefer |
| mheidari-all | 0.376 | 0.333 | 15 | 15517 | observe |
| nscl5-all | 0.352 | 0.5 | 6 | 2081 | observe |
| 10ium-ScrapeCategorize-Vless | 0.335 | 1.0 | 1 | 5157 | observe |
| tg-oneclickvpnkeys | 0.261 | 1.0 | 1 | 160 | observe |
| Epodonios-all | 0.255 | None | 0 | 6388 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3996 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7639 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4415 | observe |
| barry-far-vless | 0.255 | None | 0 | 4744 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 3992 | observe |
| Au1rxx-clash | 0.242 | None | 0 | 1681 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | TimeoutError | - | 33 |
| geo | TimeoutError | - | 32 |
| geo | ClientOSError | - | 31 |
| 204 | TimeoutError | - | 17 |
| cn-block | TimeoutError | - | 15 |
| speed | ClientOSError | - | 8 |
| cn-block | ClientOSError | - | 5 |
| 204 | ClientOSError | - | 4 |
| 204 | ProxyError | - | 2 |
| cn-block | ProxyError | - | 1 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
