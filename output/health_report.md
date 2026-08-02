# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-02 03:33:44 |
| 运行耗时 | 311.0s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 78379 |
| 去重后节点 | 23363 |
| TCP 可达 | 3000 |
| 真实可用 | 730 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23363 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.8 |
| geo | 1.3 |
| tcp | 34.7 |
| probe | 60.0 |
| real_test | 190.0 |
| generate | 20.2 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 46914 |
| vmess | 12403 |
| shadowsocks | 10055 |
| trojan | 8038 |
| hysteria2 | 616 |
| http | 157 |
| shadowsocksr | 78 |
| socks | 70 |
| anytls | 26 |
| hysteria | 14 |
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
| 80.41 | http | 311.4 | 715.5 | 20.57 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 156.146.59.25 |
| 79.28 | http | 316.7 | 712.8 | 20.45 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 156.146.59.16 |
| 79.25 | http | 315.7 | 681.5 | 20.47 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 156.146.59.50 |
| 79.09 | http | 280.7 | 561.4 | 21.28 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.202 |
| 78.95 | http | 281.0 | 568.2 | 21.27 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.208 |
| 78.91 | http | 289.0 | 572.9 | 21.09 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.204 |
| 78.86 | http | 284.6 | 573.2 | 21.19 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.197 |
| 78.79 | http | 290.3 | 594.0 | 21.06 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.198 |
| 78.79 | http | 295.4 | 605.8 | 20.94 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.212 |
| 78.76 | http | 289.9 | 592.4 | 21.07 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.209 |
| 78.67 | http | 289.9 | 588.6 | 21.07 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.196 |
| 78.64 | http | 290.1 | 590.1 | 21.06 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.206 |
| 78.59 | http | 295.1 | 604.5 | 20.95 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.207 |
| 78.44 | http | 331.5 | 739.1 | 20.1 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 156.146.59.7 |
| 78.41 | http | 288.2 | 577.3 | 21.11 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.195 |
| 78.34 | http | 296.7 | 591.3 | 20.91 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.216 |
| 78.22 | http | 325.1 | 727.6 | 20.25 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 156.146.59.33 |
| 78.19 | http | 313.3 | 541.0 | 20.53 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.211 |
| 78.13 | http | 326.2 | 719.0 | 20.23 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 156.146.59.21 |
| 78.11 | http | 298.6 | 609.1 | 20.87 | 0.0 | 10.0 | 14.9 | 20.0 | zhangkai | 138.199.35.199 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 1.0 | 1.0 | 147 | 194 | prefer |
| Au1rxx-base64 | 0.948 | 0.886 | 501 | 1590 | prefer |
| Surfboard-tg-mixed | 0.647 | 0.568 | 118 | 5146 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| nscl5-all | 0.262 | 0.5 | 2 | 1354 | observe |
| tg-OutlineReleasedKey | 0.257 | 1.0 | 1 | 57 | observe |
| Epodonios-all | 0.255 | None | 0 | 5783 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3973 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6873 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4069 | observe |
| barry-far-vless | 0.255 | None | 0 | 4431 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5071 | observe |
| mheidari-all | 0.255 | 0.222 | 9 | 16695 | observe |
| Au1rxx-clash | 0.239 | None | 0 | 1590 | observe |
| DeltaKronecker-all | 0.237 | 0.156 | 430 | 5497 | downweight |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 270 |
| speed | ClientOSError | - | 64 |
| geo | ClientOSError | - | 58 |
| speed | TimeoutError | - | 52 |
| cn-block | TimeoutError | - | 22 |
| 204 | ProxyError | - | 6 |
| cn-block | ClientOSError | - | 5 |
| 204 | ClientOSError | - | 4 |
| 204 | TimeoutError | - | 4 |
| cn-block | ProxyError | - | 3 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
