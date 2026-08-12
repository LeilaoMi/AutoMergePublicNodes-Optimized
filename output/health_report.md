# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-12 02:27:29 |
| 运行耗时 | 289.1s |
| 订阅源总数 | 107 |
| 健康订阅源 | 102 |
| 原始节点 | 80730 |
| 去重后节点 | 22951 |
| TCP 可达 | 3000 |
| 真实可用 | 699 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22951 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.6 |
| geo | 1.5 |
| tcp | 34.6 |
| probe | 56.0 |
| real_test | 156.0 |
| generate | 36.4 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 46023 |
| vmess | 13158 |
| trojan | 10399 |
| shadowsocks | 9621 |
| hysteria2 | 1203 |
| http | 159 |
| shadowsocksr | 75 |
| socks | 67 |
| tuic | 15 |
| hysteria | 10 |

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
| 81.36 | hysteria2 | 279.6 | 668.1 | 21.3 | 0.0 | 10.0 | 12.5 | 18.66 | Au1rxx-base64 | 159.223.157.129 |
| 81.18 | hysteria2 | 292.0 | 713.3 | 21.02 | 0.0 | 10.0 | 12.5 | 18.66 | Au1rxx-base64 | 138.124.68.188 |
| 80.05 | shadowsocks | 231.5 | 606.9 | 22.42 | 0.0 | 10.0 | 12.97 | 18.66 | Au1rxx-base64 | 156.146.38.170 |
| 79.84 | shadowsocks | 240.6 | 627.0 | 22.21 | 0.0 | 10.0 | 12.97 | 18.66 | Au1rxx-base64 | 156.146.38.168 |
| 79.6 | http | 317.0 | 680.7 | 20.44 | 0.0 | 10.0 | 14.88 | 19.96 | zhangkai | 156.146.59.8 |
| 79.04 | http | 315.6 | 722.1 | 20.47 | 0.0 | 10.0 | 14.88 | 19.96 | zhangkai | 156.146.59.25 |
| 78.99 | http | 317.3 | 729.8 | 20.43 | 0.0 | 10.0 | 14.88 | 19.96 | zhangkai | 156.146.59.5 |
| 78.99 | http | 324.9 | 709.7 | 20.26 | 0.0 | 10.0 | 14.88 | 19.96 | zhangkai | 156.146.59.21 |
| 78.62 | http | 287.1 | 584.3 | 21.13 | 0.0 | 10.0 | 14.88 | 19.96 | zhangkai | 138.199.35.214 |
| 78.6 | hysteria2 | 282.5 | 699.2 | 21.24 | 0.0 | 7.2 | 12.5 | 18.66 | Au1rxx-base64 | usa1.spectrumproxy.shop |
| 78.59 | http | 285.6 | 576.0 | 21.17 | 0.0 | 10.0 | 14.88 | 19.96 | zhangkai | 138.199.35.208 |
| 78.51 | http | 309.6 | 689.4 | 20.61 | 0.0 | 10.0 | 14.88 | 19.96 | zhangkai | 156.146.59.23 |
| 78.42 | http | 296.4 | 587.7 | 20.92 | 0.0 | 10.0 | 14.88 | 19.96 | zhangkai | 138.199.35.204 |
| 78.38 | http | 287.7 | 585.0 | 21.12 | 0.0 | 10.0 | 14.88 | 19.96 | zhangkai | 138.199.35.199 |
| 78.29 | http | 295.8 | 591.9 | 20.93 | 0.0 | 10.0 | 14.88 | 19.96 | zhangkai | 138.199.35.210 |
| 78.27 | http | 291.0 | 590.0 | 21.04 | 0.0 | 10.0 | 14.88 | 19.96 | zhangkai | 138.199.35.195 |
| 78.25 | http | 294.3 | 540.0 | 20.96 | 0.0 | 10.0 | 14.88 | 19.96 | zhangkai | 138.199.35.211 |
| 78.22 | trojan | 412.7 | 1081.9 | 18.22 | 0.0 | 10.0 | 14.34 | 18.66 | Au1rxx-base64 | 64.94.95.115 |
| 78.21 | shadowsocks | 298.0 | 721.6 | 20.88 | 0.0 | 10.0 | 12.97 | 18.66 | Au1rxx-base64 | 37.19.198.243 |
| 78.15 | http | 291.0 | 592.5 | 21.04 | 0.0 | 10.0 | 14.88 | 19.96 | zhangkai | 138.199.35.206 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.999 | 1.0 | 128 | 159 | prefer |
| Au1rxx-base64 | 0.919 | 0.854 | 446 | 1650 | prefer |
| Surfboard-tg-mixed | 0.749 | 0.671 | 161 | 5950 | prefer |
| mheidari-all | 0.494 | 0.413 | 172 | 16697 | observe |
| nscl5-all | 0.267 | 0.5 | 2 | 1481 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5419 | observe |
| Epodonios-all | 0.255 | None | 0 | 6635 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7586 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4851 | observe |
| barry-far-vless | 0.255 | None | 0 | 5220 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5196 | observe |
| ninja-vless | 0.251 | 0.333 | 3 | 1791 | observe |
| Au1rxx-clash | 0.241 | None | 0 | 1650 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 107 |
| geo | ClientOSError | - | 56 |
| speed | TimeoutError | - | 50 |
| cn-block | TimeoutError | - | 40 |
| speed | ClientOSError | - | 27 |
| 204 | TimeoutError | - | 20 |
| 204 | ProxyError | - | 6 |
| cn-block | ClientOSError | - | 4 |
| cn-block | ProxyError | - | 3 |
| 204 | ClientOSError | - | 2 |
| speed | ClientPayloadError | - | 1 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
